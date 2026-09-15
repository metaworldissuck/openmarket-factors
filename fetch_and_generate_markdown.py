import argparse
import re
from pathlib import Path
from typing import List

from playwright.sync_api import sync_playwright


DEFAULT_URL = "https://openmarket.xyz/academy/guide/guide-to-time-price-opportunity-miszqf9ck61kfg"


def slugify(value: str) -> str:
    value = re.sub(r"https?://", "", value)
    value = re.sub(r"[^a-zA-Z0-9\-_]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value.lower() or "article"


def fetch_rendered_article(url: str) -> tuple[str, str]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1800})
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(3000)

        try:
            page.locator("article").wait_for(state="visible", timeout=30000)
        except Exception:
            pass

        try:
            page.locator("text=Loading guide…").wait_for(state="hidden", timeout=30000)
        except Exception:
            pass

        title = page.locator("h1").first.inner_text().strip()
        if not title:
            title = page.title().strip() or "Untitled Article"

        try:
            article = page.locator("article").first.inner_text()
            if article and article.strip():
                browser.close()
                return title, article.strip()
        except Exception:
            pass

        body_text = page.locator("body").inner_text()
        if body_text and body_text.strip():
            browser.close()
            return title, body_text.strip()

        browser.close()
        raise ValueError(f"No readable article text found for: {url}")


def normalize_text(text: str) -> str:
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        line = line.replace("\xa0", " ").strip()
        if not line:
            continue
        if line in {
            "products", "docs", "blog", "academy", "Get Openmarket",
            "get openmarket", "Back to academy", "OPENMARKET ACADEMY",
            "Loading guide…", "© 2026 Openmarket Labs. All rights reserved.",
        }:
            continue
        cleaned.append(line)

    result = []
    last = ""
    for line in cleaned:
        if line == last:
            continue
        result.append(line)
        last = line
    return "\n".join(result).strip()


def detect_key_points(text: str, limit: int = 5) -> List[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n+", text) if p.strip()]
    points = []
    for paragraph in paragraphs:
        if len(paragraph) < 80:
            continue
        sentence = re.split(r"(?<=[.!?])\s+", paragraph)[0]
        points.append(sentence[:220].strip())
        if len(points) >= limit:
            break
    if not points:
        sentences = re.split(r"(?<=[.!?])\s+", text)
        points = [sentence.strip() for sentence in sentences if sentence.strip()][:limit]
    return points


def build_vwap_translation() -> str:
    return """## 2. 中文翻译与概述

### 第 1 章：介绍

如果你研究过市场，可能接触过“移动平均线”。市场的每一次微小波动都由成百上千笔交易共同决定，因此移动平均线可以过滤价格噪声，并计算一段时间内的平均价格。VWAP 也能起到过滤噪声的作用，但它不是单纯按时间平均价格，而是按照市场成交量对价格进行加权。成交量越大的价格水平，代表的市场参与程度越高，在 VWAP 计算中的重要性也越大。

### 第 2 章：快速比较

文章将 VWAP 与简单移动平均线（SMA）和 26 根 K 线周期的指数移动平均线（EMA）进行比较。VWAP 往往更贴近真实成交价格：当高成交量推动价格快速运动时，VWAP 的变化会更明显；当价格处在低成交量区域时，VWAP 通常会横向移动。

### 第 3 章：VWAP 为什么重要

#### 3.1 过滤噪声并观察价值

市场受到情绪和程序化执行影响，天然具有随机性。VWAP 通过标记大部分成交发生的价格，帮助交易者观察市场参与者认可的“公平价值”。当价格明显偏离 VWAP 时，市场可能处于过度延伸状态；当价格围绕 VWAP 波动时，市场可能正在价值区域内盘整。不过，VWAP 只是过去交易行为的记录，并不保证价格一定会回到或尊重它。

#### 3.2 以关键位置为锚定点

交易者可以在重要市场位置重新计算 VWAP，使其适应不同资产、周期和交易风格。常见锚定点包括纽约交易时段开盘、UTC 开盘以及重要的市场结构位置。

### 第 4 章：交易应用

#### 4.1 识别市场变化

观察价格与 VWAP 的关系，可以帮助识别市场状态变化。当价格从 VWAP 附近的盘整区间猛烈扩张，并持续远离 VWAP 时，可能意味着趋势正在延伸。价格位于 VWAP 上方，说明当前价格相对于主要成交区域处于溢价，若成交量同步跟进，可能支持继续上涨；价格位于 VWAP 下方则表示处于折价区域，若卖方持续主动，可能推动下行延续。单独使用 VWAP 不能提供完整答案，需要结合其他数据验证。

#### 4.2 VWAP 偏离带

除了 VWAP 本身，交易者也常使用 VWAP 的一倍、两倍和三倍标准差，用来观察价格相对成交量加权均值的偏离程度。当价格远离 VWAP 并触及较大的偏离带时，可能已经过度延伸，存在均值回归的可能，但这不是必然的反转信号。

#### 4.3 构建交易策略

VWAP 与其他工具结合时更有价值。通过叠加订单流数据，交易者可以进一步判断价格为什么移动，以及下一步可能如何发展。

##### 4.3.1 累积成交量差（CVD）

CVD 衡量主动买入量与主动卖出量之间的净差额。如果价格位于 VWAP 上方，同时 CVD 上升，可以作为多头动能的确认。文章中的示例展示了价格下破 VWAP 后反弹，但随后重新转弱；CVD 同步创出更低低点，说明卖方主动性增强，最终下跌趋势延续。

##### 4.3.2 成交量足迹图

成交量足迹图把每根 K 线的成交量进一步拆分为买卖盘不平衡，帮助识别 VWAP 附近的连续不平衡。当价格尝试站上 VWAP 时，如果买方付出很大成交量却无法推动价格继续上涨，说明买方努力没有转化为价格结果，卖方可能重新占优。文章也提醒，示例带有事后观察的优势，交易者应根据自己的风格决定哪些信息组合能够形成真正的交易优势。

### 第 5 章：结论

VWAP 是一个简单的工具，但正确使用时可以清晰展示重要成交活动发生在哪里，以及价格相对于价值区域如何运动。它不能预测未来，也不能保证价格一定反应，却能在嘈杂市场中提供稳定的参照点。将 VWAP 与可靠的执行工具和明确的交易系统结合，才能使它成为完整交易流程中的一部分。

## 3. 延伸解读

### 3.1 VWAP 的计算含义

VWAP 可以理解为：

$$
VWAP = \\frac{\\sum_i Price_i \\times Volume_i}{\\sum_i Volume_i}
$$

它回答的不是“某一时刻价格是多少”，而是“在当前统计区间内，大部分成交量的平均成交成本在哪里”。因此，VWAP 更接近成交参与者的成本重心。

### 3.2 交易信号如何组合

- 价格在 VWAP 上方且 CVD 上升：偏向多头环境，但仍需确认成交量和结构是否支持。
- 价格在 VWAP 下方且 CVD 下降：偏向空头环境，反弹回 VWAP 后受阻可能提供趋势延续线索。
- 价格远离 VWAP 并触及偏离带：关注是否出现动能衰竭，而不是直接逆势开仓。
- 价格反复穿越 VWAP：通常说明市场处于平衡或震荡状态，趋势策略的信号质量可能下降。

### 3.3 锚定 VWAP 的实践建议

不同锚定方式回答不同问题：交易时段 VWAP 适合观察当日参与者的平均成本，UTC 开盘 VWAP 适合加密市场的日内节奏，结构位置 VWAP 则适合研究某次突破或趋势段的成本分布。使用时应明确统计起点，否则不同锚定点之间的信号容易互相冲突。

### 3.4 风险与局限

VWAP 具有滞后性，且容易受到统计区间、成交量质量和市场流动性的影响。价格持续位于 VWAP 一侧时，偏离并不代表立刻回归；低流动性市场中的异常成交也可能扭曲结果。因此，VWAP 应作为分析框架的一部分，不能替代止损、仓位管理和事前定义的交易计划。

### 3.5 一句话总结

VWAP 把价格与成交量结合起来，帮助交易者观察市场参与者的平均成本、趋势方向和价格偏离程度；它最适合用于确认市场结构，而不是单独预测买卖点。
"""


def build_psychology_translation() -> str:
    return """## 2. 中文翻译与概述

### 文章主旨

这篇文章讨论交易心理，重点不是寻找更多指标，而是学会在行情剧烈波动时保持纪律。作者认为交易者最常见的三个敌人是 FOMO、傲慢或自我，以及风险厌恶。文章通过三个原则说明如何减少情绪对交易计划的干扰。

### 原则一：不要逆势交易

趋势行情中，很多人试图抄底、摸顶或捕捉逆势反弹，结果容易在接飞刀时被清算。逆势反弹通常持续时间短，风险收益比也不理想。更稳妥的做法是尽早寻找顺应主趋势的入场机会；如果已经错过主要行情，就等待下一次顺势机会，而不是为了追回错过的利润去承担更难的逆势交易。

### 原则二：让市场走到你的交易位置

如果交易计划设定了一个做空或做多区域，就应等待价格到达该区域，并提前定义失效条件。过早入场、因为价格突然加速而追单，可能在真正的入场位置到来之前先被止损或清算。只要计划尚未被证明错误，就应保持等待，可以设置价格提醒并离开屏幕，避免用临时判断破坏原有计划。

### 原则三：交易应该变得无聊

刚开始开车、坐飞机或做公开演讲时，人通常会兴奋或紧张；而经验丰富的卡车司机、经常飞行的乘客或重复做实验的研究者，面对同样的流程通常不会有强烈情绪。交易也应通过大量重复和流程化训练，变成按计划执行的日常工作。过度兴奋、恐惧或急于证明自己，往往意味着交易者还没有真正掌控流程。

### 中文总结

不要逆势抄底摸顶；不要在价格尚未到达计划区域前提前交易；把交易流程重复到足够熟练，使执行不再依赖情绪。文章最后强调，纪律、等待和重复执行，是长期保持控制力的基础。

## 3. 延伸解读

### 3.1 三条原则对应的行为偏差

- 逆势交易通常与 FOMO 和“我能抓住反转”的过度自信有关。
- 提前入场通常是无法忍受等待，或者害怕错过计划机会。
- 交易不够“无聊”通常表现为频繁看盘、频繁改计划和过度交易。

### 3.2 可执行的交易检查表

1. 当前交易是否顺应更高周期趋势？如果不是，是否有明确且经过验证的反转依据？
2. 当前价格是否到达预先定义的交易区域？如果没有，是否应该继续等待？
3. 入场、止损、目标和失效条件是否在下单前已经写清楚？
4. 如果这笔交易亏损，是否仍然属于计划内损失，而不是临时冲动造成的结果？
5. 今天是否已经因为情绪、连续亏损或追回损失的想法而偏离系统？

### 3.3 风险提醒

顺势交易并不意味着趋势一定延续，等待也不保证最终盈利。交易心理原则只能改善决策过程，不能消除市场风险。仓位、止损和最大日亏损限制仍然需要独立定义。
"""


def build_article_translation(title: str, url: str) -> str:
    if "psychology-1" in url or "psychology #1" in title.lower():
        return build_psychology_translation()
    if "vwap-a-practical-guide" in url:
        return build_vwap_translation()
    return """## 2. 中文翻译与概述

当前文章的英文原文已在下方完整保留。该文章暂无针对性的中文翻译模板，避免将其他文章的分析内容误套到本文。
"""


def build_markdown(title: str, url: str, raw_text: str) -> str:
    clean_text = normalize_text(raw_text)
    key_points = detect_key_points(clean_text)
    first_paragraph = "\n".join(clean_text.splitlines()[:10])

    markdown = f"""# {title}

来源：OpenMarket Academy
链接：{url}

---

## 1. 原文整理（精简版）

### 1.1 文章主旨

{first_paragraph}

### 1.2 关键观点

"""

    for index, point in enumerate(key_points, start=1):
        markdown += f"{index}. {point}\n\n"

    markdown += build_article_translation(title, url) + """

---

## 4. 全文提取（已清洗）

```text
"""
    markdown += clean_text + "\n```\n\n---\n\n## 5. 备注\n\n"
    markdown += "该文件保留了较完整的正文信息，以便后续继续做细化分析、关键词提取或进一步翻译。\n"
    return markdown.strip() + "\n"


def save_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
    print(f"Saved: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch an OpenMarket article and generate a Markdown summary file.")
    parser.add_argument("url", nargs="?", default=DEFAULT_URL, help="Article URL to fetch")
    parser.add_argument("--output-dir", default=".", help="Directory to save the extracted raw text and Markdown file")
    args = parser.parse_args()

    title, raw = fetch_rendered_article(args.url)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    md_path = output_dir / f"{slugify(args.url)}.md"
    save_text(md_path, build_markdown(title, args.url, raw))


if __name__ == "__main__":
    main()
