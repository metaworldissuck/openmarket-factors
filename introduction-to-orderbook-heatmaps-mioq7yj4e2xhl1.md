# Introduction to Orderbook Heatmaps

来源：OpenMarket Academy 文章
链接：https://openmarket.xyz/academy/guide/introduction-to-orderbook-heatmaps-mioq7yj4e2xhl1

---

## 1. 原文整理（精简版）

### 1.1 文章主旨

In markets, the advantage goes to those who see what others don't. While retail traders react to price movements, professional trading firms profit by understanding and exploiting order flow imbalances. Orderbook heatmaps quantify this edge by revealing exactly where liquidity exists and how it's shifting in real-time. It transforms complex orderbook data into clear visual patterns, revealing exactly where the market's structural weaknesses and opportunities exist.

This guide introduces the same orderbook analysis techniques used by high-frequency trading firms to identify liquidity clusters, recognize authentic support and resistance levels, and position ahead of significant price movements—often before conventional chart patterns form.

### 1.2 基本概念

What is an Orderbook?

- Limit Orders: orders placed at specific prices that wait to be filled
- Bids: buy orders below the current price
- Asks: sell orders above the current price
- Market Orders: orders that execute immediately at the best available price
- The Orderbook: the full collection of limit orders waiting to be filled

The orderbook shows the available liquidity at every price level. Heatmaps transform this information into a visual format that is easier to interpret than raw numbers.

### 1.3 Heatmap 的工作方式

A crypto orderbook heatmap displays:

- X-axis: time progression
- Y-axis: price levels
- Color intensity: volume/liquidity concentration at each price-time point

Brighter or more intense colors indicate higher order concentration, while darker colors indicate fewer orders.

### 1.4 Heatmap 为什么重要

Heatmaps reveal information that price charts alone cannot show:

- supply and demand imbalances
- support and resistance based on actual liquidity
- market participant intentions
- potential price targets and rejection zones

### 1.5 关键特征

#### Heatmap Blocks

Each block's intensity reveals how many buy or sell orders exist at different price levels during each time period. Stronger intensity means more orders.

Each block is the minimum unit of the heatmap. The size depends on the chosen granularity. In the example, each block represents a $25 price range.

- Blocks above the current price represent resting sell orders.
- Blocks below the current price represent resting buy orders.

#### Block Size & Resolution

Block size affects the resolution of the heatmap:

- smaller blocks provide higher resolution
- larger blocks provide a cleaner but less granular view

Current options include:

- SD (Standard Definition): balanced view, lower resource use
- HD (High Definition): more granular, reveals micro-structures in order flow

#### Heatmap Magnifier

The magnifier shows the exact liquidity values at a hovered position and surrounding blocks, allowing traders to inspect specific price points without losing the broader context.

#### Heatmap Units

Default view: native notional / base asset quantity
Optional view: USD

Benefits of USD view:

- easier comparison across assets
- intuitive market size interpretation
- clearer risk management
- better understanding of actual liquidity value

### 1.6 过滤与强度控制

Heatmap filtering helps focus on meaningful liquidity instead of noise.

#### Visibility & Intensity Sliders

- Threshold (left slider): minimum order size to display
- Ceiling (right slider): value at which the color intensity maxes out

This helps highlight important liquidity clusters while filtering weak noise.

Presets include:

- high sensitivity: reveals smaller order activity
- medium sensitivity: balanced view
- low sensitivity: shows only significant zones

#### Advanced Range Controls

Used for assets with very low unit prices or huge supply, where the normal thresholds are not meaningful.

- Min Bounds - Lower
- Max Bounds - Upper

### 1.7 其他可视化工具

#### Orderbook Depth Indicator

A simplified view of imbalances as layered areas on the chart.

Advantages:

- lower complexity
- lower performance requirements
- easier recognition of major imbalances

#### Delta Bar Indicator

Shows bid/ask liquidity imbalance period by period.

It helps identify:

- momentum shifts
- divergence between price and order flow
- short-term order imbalance changes

### 1.8 Heatmap Themes

Theme customization affects contrast and signal readability.

Single-color or dual-color themes can make liquidity patterns easier to see and reduce visual fatigue.

### 1.9 最终观点

Orderbook heatmaps are most powerful when used together with traditional indicators such as:

- open interest changes
- volume profile
- key support/resistance levels

The article emphasizes that heatmaps reveal intention, not guarantees. They show where liquidity exists and where it is shifting, giving traders a probabilistic edge before price action fully reflects it.

---

## 2. 中文翻译

# 订单簿热力图导读

在市场中，优势属于那些能看见别人看不见东西的人。零售交易者对价格波动做出反应，而专业交易公司则通过理解并利用订单流失衡来获利。订单簿热力图把这种优势量化出来，它能精准展示流动性存在在哪里，以及它如何实时变化。它把复杂的订单簿数据转化为清晰的视觉模式，揭示市场结构性弱点和机会所在。

这篇指南介绍的是与高频交易公司相同的订单簿分析方法：识别流动性簇、识别真实支撑位和阻力位，并在重大价格波动发生前布局——通常是在传统图表形态形成之前。

## 基本概念

### 什么是订单簿？

- 限价单：以特定价格挂出的订单，等待成交
- 买单（Bids）：当前价格以下的买入订单
- 卖单（Asks）：当前价格以上的卖出订单
- 市价单：按当下最优价格立即执行
- 订单簿：所有等待成交的限价单集合

订单簿显示的是每个价格水平上可用的流动性。热力图把这些信息转化成更容易理解的视觉形式。

## 热力图如何工作

加密货币订单簿热力图显示：

- X 轴：时间推进
- Y 轴：价格水平
- 颜色强度：在每个价格-时间点上的成交量/流动性集中程度

颜色越亮或越强，说明该区域的订单越集中；颜色越暗，说明该区域订单较少。

## 热力图为什么重要

热力图揭示了单纯价格图无法看见的信息：

- 供需失衡
- 基于真实流动性的支撑与阻力
- 市场参与者的意图
- 潜在价格目标与反弹/拒绝区域

## 关键特征

### 热力图方块

每个方块的强度显示在不同时段里，不同价格层级上有多少买单或卖单。强度越大，说明订单越多。

每个方块是热力图中的最小单位。方块大小取决于所选颗粒度。举例中，每个方块代表 25 美元的价格区间。

- 当前价格上方的方块代表挂起的卖单
- 当前价格下方的方块代表挂起的买单

### 方块大小与分辨率

方块大小会影响热力图分辨率：

- 更小的方块提供更高分辨率
- 更大的方块提供更干净但更粗糙的视图

目前提供两种选项：

- SD（标准分辨率）：平衡视图，资源占用更低
- HD（高分辨率）：更细粒度，能揭示订单流中的微观结构

### 热力图放大镜

放大镜可以让你直接查看鼠标悬停位置及其周围区域的精确流动性数据，便于窥探特定价位的真实挂单情况，同时保留更大范围的市场背景。

### 热力图单位

默认展示：原生名义值/基础资产数量
可切换：美元计价

美元视图的好处：

- 更容易跨资产比较
- 更容易理解不同资产的市场规模
- 更清晰的风险管理
- 更直观地理解流动性簇的实际资金量

## 过滤与强度控制

热力图过滤有助于集中关注有意义的流动性，而不是噪声。

### 可见性与强度滑块

- Threshold（阈值）：最小显示订单规模
- Ceiling（上限）：颜色强度达到最大值的阀值

这种设计能突出关键流动性区域，同时过滤掉低价值噪声。

预设敏感度包括：

- 高敏感：显示较小的订单活动
- 中敏感：平衡视图
- 低敏感：只显示重要的流动性区域

### 高级范围控制

当资产的单位价格非常低或供给极大时，默认范围可能不合适，此时可以调整：

- Min Bounds - Lower
- Max Bounds - Upper

## 其他可视化工具

### 订单簿深度指示器

它以分层区域的方式展示市场失衡，直观看到深度变化和潜在支撑/阻力区域。

优点：

- 更简单
- 计算要求更低
- 更容易识别重大失衡

### Delta Bar 指标

它展示每个时间周期的买卖流动性失衡，帮助识别：

- 动量变化
- 价格与订单流之间的背离
- 短期失衡的变化

## 热力图主题

主题可以提升对比度和信号可读性。单色或双色主题设计有助于让流动性模式更清晰，减少视觉疲劳。

## 总结

订单簿热力图最强大之处在于它与传统指标结合使用，例如：

- 持仓量变化
- 成交量分布
- 关键支撑/阻力位

文章强调：热力图揭示的是意图，而不是保证。它展示了哪里有流动性，以及它如何变化，让交易者在价格反映之前就先获得概率优势。

---

## 3. 核心总结（中文）

这篇文章的核心思想可以概括为：

> 订单簿热力图不是简单的“价格图”，而是“实时流动性分布图”。它帮助交易者看清市场中真正的买卖力量，并在价格形成前识别潜在机会和风险区域。

### 关键观点

1. 市场真正有价值的信息，往往不在表面的价格走势，而在订单簿深度中。
2. 价格图只能看到结果，热力图能看到“为什么会在这里形成压力”以及“哪里有真实的支撑和阻力”。
3. 热力图最适合识别：
   - 流动性簇
   - 支撑/阻力区
   - 买卖失衡
   - 价格可能被吸引或排斥的位置
4. 订单簿分析的核心不是预测绝对顶部和底部，而是识别市场中最大的成交意愿和最强的结构性支持。
5. 热力图本身不能保证成功，但它能提供比传统 K 线更早、更具体的市场信息。

---

## 4. 扩展说明：如何理解这篇文章对量化交易与实盘的意义

### 4.1 对量化交易的意义

订单簿热力图对量化交易非常重要，因为它直接反映了市场的“未成交意图”。

在量化研究中，它可以帮助我们做以下事情：

- 识别流动性峰值区域
- 判断某一价格区间是否真的有强买盘或强卖盘
- 观察订单簿的动态变化速率
- 识别“吸筹/分批出货”式的市场结构
- 作为交易信号的前置过滤条件

### 4.2 对实盘交易的意义

对实盘交易者而言，热力图最重要的是：

- 不被单纯价格动作误导
- 看到“真正的支撑与阻力”来自哪里
- 在价格冲击前识别潜在的流动性密集区
- 在市场噪声较大时，筛掉低质量交易信号

这意味着：

- 不是只看 K 线趋势
- 而是同时看：价格、时间、成交量、订单簿分布
- 这样更容易判断价格是否“有理由”继续走强或反转

### 4.3 对交易者的启示

交易者最容易犯的错误之一，是把价格当成唯一真相。其实价格只是成交结果，而订单簿是行动背景。热力图帮助我们从“看见结果”转向“看见原因”。

换句话说：

- 价格告诉你“市场在哪里”
- 订单簿告诉你“市场为什么在这里”
- 热力图告诉你“市场下一步可能往哪里走”

### 4.4 适合结合的分析工具

本篇文章建议将热力图和以下工具结合：

- Open Interest（未平仓合约）
- Volume Profile（成交量分布）
- 支撑/阻力位
- Delta / 买卖压差指标
- 趋势和波动率指标

这些工具组合起来，能明显提高信号质量。

### 4.5 一个更实用的理解框架

可以把订单簿热力图理解成三层信息：

1. 结构层：哪里有大量挂单
2. 强度层：买卖力量是否失衡
3. 动态层：这些流动性是否正在移动、消失或集中

如果一个价格区间同时满足：

- 流动性集中
- 买卖差异明显
- 趋势和结构支持

那么这通常比单纯价格线性波动更可能形成高概率交易机会。

---

## 5. 一句话总结

订单簿热力图是把市场的“隐藏力量”可视化的工具：它告诉我们哪里有真实的流动性、哪里有强烈的买卖意愿，以及市场是否在准备推进或反转。对量化与实盘交易者来说，它提供的是比传统价格分析更早、更深一层的市场认知。

---

## 6. 适合个人学习的行动建议

如果你准备学习订单簿热力图，可以按下面顺序推进：

1. 先理解订单簿的基本结构：买单、卖单、限价单、市场单
2. 再看热力图中的颜色强度与价格分布
3. 重点研究：支撑位、阻力位、流动性簇与失衡区域
4. 将热力图与成交量、趋势、持仓量结合分析
5. 不要只盯价格，学会判断“背后的流动性为什么这样排列”

这样学习，效率会明显高于只看 K 线。
