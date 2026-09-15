# Guide To Orderbook Heatmaps：更完整的中文结构化解析

来源：OpenMarket Academy
链接：https://openmarket.xyz/academy/guide/guide-to-orderbook-heatmaps-misxt4467qg6xe

---

## 1. 文章主线：它不是交易预测器，而是“市场结构解读器”

这篇文章的主旨非常清晰：

> 市场的真实信息，不只是价格走势，而是隐藏在订单簿中的流动性、挂单强度和参与者意图。

它开篇就说明，价格并不是随机飘动的，而是由流动性分布决定的。价格会被密集的买卖盘吸引，遇到稀薄区域时会更容易加速；市场中的每一次动作，都是供需和参与者意图的结果。

因此，订单簿热力图不是要替代传统技术分析，而是补全一个重要的视角：

- 价格是结果；
- 订单簿是原因；
- 流动性是机制；
- 热力图是机制的可视化。

最值得记住的是：它帮助你看到“为什么价格会在这个位置被守住、被攻击、被吸收”，而不只是“价格现在涨了/跌了”。

---

## 2. 订单簿基础：读懂热力图，先懂“挂单”和“吃单”

### 2.1 限价单与市价单

作者首先解释了订单簿中最核心的两个对象：

- 限价单：挂在某个价格上的单子，等着被成交；它提供流动性，通常属于 maker。
- 市价单：按当前最优价格立即成交的单子，它消耗流动性，通常属于 taker。

这说明市场并不是只靠价格，而是靠买卖力量在不同价位上的“堆叠”与“消耗”来推动方向。

### 2.2 买盘、卖盘和流动性深度

文章继续定义：

- Bids：买盘，通常位于当前价格以下；
- Asks：卖盘，通常位于当前价格以上；
- 深度：同一价格区间里有多少订单在堆积；
- 短期动能：主动参与者吃单的速度和力度。

一个非常关键的理解是：

> 大量挂单不是“静态数字”，而是标志着市场对未来价格的承压或承接意愿。

### 2.3 主动 vs 被动：谁在推动价格，谁在守护区域

文章区分了：

- 被动参与者：挂限价单，提供流动性；
- 主动参与者：使用市价单去吃流动性。

这两种人驱动着市场的两种不同状态：

- 主动吃单：行情更像在“冲击”；
- 被动挂单：行情更像在“守住/承接”。

当一个区域长期有大量挂单，说明这里存在真实的流动性吸收或支撑；而当价格急速经过某个区域，说明主动性很强，市场在推动趋势。

### 2.4 订单队列与隐藏流动性

作者还引入了几个现实细节：

- 订单遵守队列机制；
- 大户可能不断调整挂单位置，制造看起来像强势/弱势的视觉；
- 并不是所有流动性都现形，冰山单、暗池流动性等会干扰表面观察。

这意味着：

> 订单簿热力图是强大的可视化工具，但它不是绝对真相；它必须和成交量、delta、OI、市场结构一起看。

---

## 3. 热力图如何工作：把“流动性变化”变成一张时间地图

### 3.1 线性维度：时间、价格、颜色强度

热力图的核心逻辑非常直观：

1. X 轴：时间
	每一列代表一段时间里的订单簿快照。

2. Y 轴：价格
	每一行表示某一价格等级。

3. 颜色强度：挂单密度
	颜色越深/越亮，说明该价格区间的流动性越大。

这样一张图，就能把市场中“谁在挂单、谁在撤单、谁在吃单”转成一个很容易追踪的变化结构。

### 3.2 历史叠加：它不是一张静态图，而是一张时间序列地图

作者强调，热力图的价值在于它叠加了历史信息：

- 订单被放进来；
- 订单被移走；
- 订单被吞掉；
- 订单在时间轴上不断改变。

这使它能“看见行为”，而不仅仅看某一瞬间的价格状态。

例如，某一区域长期积累大量挂单，最终却在突然一轮强势冲击中被消耗掉。这种“先积聚、再被扫掉”的结构非常重要，因为它说明市场在发生从平衡到失衡的变化。

### 3.3 实时深度 vs 累计深度

热力图通常分为两种观察方式：

- 实时深度：看当前时点订单簿；
- 累计深度：看历史上大量订单在该价区的累积分布。

这两个视角分别适合回答两个不同的问题：

- 实时深度：现在谁在守、谁在冲？
- 累计深度：长期来看，这里的结构是不是重要支撑/阻力？

这非常重要，因为市场中很多看起来很不起眼的价区，可能在历史上已经构成过多个重要的交易窗口。

### 3.4 层叠挂单与补充流动性

作者提出了另一个现实结构：

- 大户常常分层挂单；
- 价格靠近时，可能撤掉一部分；
- 价格反弹时，又补回一批；
- 这种行为会让市场看起来“像在守住”，但实际上可能只是做局或做掩护。

因此，热力图很重要，但不能绝对化。它最有效的地方，是把“市场诱导”和“真实承接”分开观察。

---

## 4. 为什么热力图对交易者重要：它解决的是“看不见的市场意图”

### 4.1 价格来自流动性，流动性来自参与者

文章最核心的主张是：

> 价格总是由市场参与者在某个价格区间上的实际行为推动，而不是单纯凭空出现。

所以，真正重要的，不是“价格最后在哪”，而是：

- 是谁在挂单；
- 是谁在吃单；
- 是市场在被动承接，还是主动突破；
- 这一层是否在形成真实支撑/阻力。

### 4.2 热力图让“支撑/阻力”变得更具体

传统支撑位往往是一个经验性的数字，而热力图将其变成一种“市场结构”体验：

- 某一层有大量买盘，不断吸收下行；
- 某一层有大量卖盘，不断压制上涨；
- 价格反复试探但不能突破，说明存在真实吸收；
- 价格一旦突破，往往意味着之前的挂单被清空，随后会出现更强的继续性或反转。

### 4.3 热力图能看到“市场控制者”与“诱导行为”

这篇文章尤其强调：

- 大户守护关键区域；
- 延迟触发流动性的释放；
- 通过挂单制造假强/假弱；
- 在关键地方诱导其他交易者参与。

这些现象并不常出现在普通 K 线中，但在热力图里却往往非常明显。

理解这一点，会让交易者从“盯价格”升级到“盯结构”。

---

## 5. 热力图中的关键形态：从颜色到行动模式

### 5.1 静态墙（Static Walls）

静态墙指的是：

- 某个价位附近长期存在大量挂单；
- 价格反复靠近但不容易穿破；
- 一旦破掉，通常伴随波动放大和止损触发。

这类结构通常意味着真实支撑或真实阻力，不只是单纯心理层。

### 5.2 动态流动性（Dynamic Liquidity）

动态流动性是指订单不是完全固定，而是随着价格移动而不断调整。通常这代表：

- 算法在控制跟随型挂单；
- 市场处于趋势或波动延续阶段；
- 一侧跟随另一侧移动，常伴随盘整或突破前的准备。

这类流动性更像“活墙”，比静态墙更难读，但也更能反映真实市场机制。

### 5.3 流动性空洞（Liquidity Voids）

空洞区域是：

- 价格附近很少有挂单；
- 市场很容易快速穿过；
- 这时冲击会更快，速度更高。

当价格从低流动性区快速穿过时，往往更容易形成一段“无阻力加速”。

### 5.4 吸收（Absorption）

吸收的关键特征是：

- 价格不断试图突破某一区域；
- 但大额挂单反复吞掉冲击；
- 最终价格没有继续强势突破，反而可能反转。

这意味着市场中的一方在主动承接大量主动卖盘，说明该区域存在强烈的“对抗性承压”。

### 5.5 扫单（Sweeps）

扫单发生在：

- 价格强势穿过一层；
- 订单迅速被吃掉；
- 成交量急剧增加，市场出现明显加速。

这种状态通常意味着：

- 强势行情正在确认；
- 止损位和短线仓位容易被触发；
- 后续可能延续更大幅度波动。

### 5.6 伪装挂单（Spoofing）

伪装挂单指的是：

- 一边突然挂出大量挂单，制造强势或弱势视觉；
- 但很快撤掉，不让价格真正突破。

这类行为会让热力图出现非常明显的“假强/假弱”现象。它说明：

> 热力图最怕“看图不看行为”。

你必须结合交易量、delta、S/R 结构和价格行为，才能避免被诱导。

---

## 6. 热力图的细节：分辨率、颜色、工具、单位，都会影响你看到什么

### 6.1 块状结构：每个颜色块都代表一种真实的市场积累

每一个热力图块本质上都代表：

- 某一时段、某一价格区间的挂单数量；
- 颜色越强，说明该区域的流动性越集中。

它帮助你快速识别：

- 哪里是市场“高压区”；
- 哪里是“稀薄区”；
- 价格是否在强支撑/强阻力附近反复试探。

### 6.2 分辨率：高分辨率看微观结构，低分辨率看大局

文章中提到：

- 小块 / 更高分辨率：适合观察短周期下的微观结构；
- 大块 / 低分辨率：更适合观察宏观流动性区域。

这非常重要，因为短线和长线观察的重点不同：

- 短线：看订单流动有无瞬间扭转；
- 中长线：看某一大价区是否持续有大量资金在守。

### 6.3 放大镜工具：不丢失全局，也能看到局部细节

文章里的放大镜工具非常实用，因为它允许交易者：

- 在全局图上继续观察局部价位；
- 查看某一处是否有高密度挂单；
- 解释价格为什么在某处受阻、为什么突然穿透。

### 6.4 计量单位：看原始量还是看美元尺度

热力图可以按：

- 代币数量；
- 或 USD 价值；

来展示挂单深度。

这两种单位并不等价：

- 代币量更适合研究相对结构；
- USD 价值更适合比较两个资产之间的资本强度。

---

## 7. 从观察转向应用：热力图不是买卖信号，而是市场结构背景

### 7.1 先看位置，再看反应，再看一致性

文章建议：

1. 位置：市场行为发生在趋势、区间、突破还是回撤区域？
2. 反应：价格和成交量在被测验时如何反应？
3. 一致性：同样的模式是否在不同周期重复出现？

如果这些条件同时成立，说明热力图信息就更可靠。

### 7.2 热力图最强的不是“给买入卖出”，而是“解释为什么”

真正优秀的研究方式不是“看热力图之后直接下单”，而是：

- 看哪里有流动性；
- 看谁在承压；
- 看价格是突破，还是被诱导；
- 看是否与成交量、CVD、OI 等工具形成互相解释。

在这种框架下，热力图会从“噪音图”变成“决策工具”。

---

## 8. 与其他数据整合：热力图的真正价值在于拼图式理解市场

### 8.1 OI（未平仓合约）

OI 的意思是市场中有多少仓位还没有对冲完。它更像“持仓承诺度”。

结合热力图看，关键是：

- 如果突破时 OI 上升，说明趋势更可信；
- 如果价格穿透强流动性区时 OI 下降，说明可能存在减仓或短线回撤；
- 如果在强烈吸收区域 OI 急升，往往说明有被套/被压制的交易者。

### 8.2 CVD（累计成交量差）

CVD 衡量的是买卖双方的主动性：

- CVD 上升：买入主动性强；
- CVD 下降：卖出主动性强；
- 若价格在某一层附近守住，但 CVD 继续提升，往往说明买盘正在逐步吸收卖盘。

热力图告诉你哪里有挂单，而 CVD 告诉你这些挂单是否真的在被吃掉或被承接。

### 8.3 Volume Delta（逐根 K 线的净成交量差）

这是更细的增强版过滤器：

- 若某个买盘墙附近出现强正 delta，说明市场有明显主动买入；
- 若某个卖盘墙附近出现强负 delta，说明卖方压力在加速。

它能帮助判断这是不是“单纯看起来像支撑/阻力”，还是“真实发生了被动承接/主动冲击”。

### 8.4 Volume Profile（成交量分布）

Volume Profile 显示的是不同价格区间的历史成交量分布。它通常能帮助识别：

- 哪些价格区间值得被当成价值区；
- 哪些区间长期被市场高频交易；
- 热力图中的大挂单是否落在关键成交区域上。

### 8.5 TPO / Market Profile（时间-价格分布）

TPO 关注的是价格停留多久。它与热力图组合起来时，非常有价值：

- 热力图：看“哪里有挂单”；
- TPO：看“价格花了多少时间停留在那里”；
- 市场结构：看“这里到底是价值区，还是单纯噪音区”。

### 8.6 最后一句话：热力图并不孤立

作者表达的核心思想是：

- 热力图看意图；
- CVD/Delta 看执行；
- OI 看承诺；
- Volume Profile/TPO 看价值区；
- 订单簿深度看流动性的变化。

所有这些工具一起，看市场才更完整。

---

## 9. 结论：订单簿热力图的真正价值，是帮助你理解“价格在背后被谁推动”

文章的结论很明确：

> 订单簿热力图并不直接预测方向，但它能让你看清市场中的真实供需分布、参与者意图和潜在失衡区域。

如果只看 K 线，你看到的是结果；
如果看订单簿和热力图，你看到的是过程；
如果再结合成交量、delta、OI 和流动性结构，你就更接近市场的真相。

这使它成为一个非常重要的交易认知工具，而不是单纯的“红线蓝线买卖信号”。

---

## 10. 一句话总结

订单簿热力图的关键价值，不在于让你一眼看出未来，而在于让你理解：

> 市场的每一个价格波动，都是某一段流动性结构发生变化的结果。

真正成熟的交易者，不只是看价格，还能看清价格背后的供需、吸收、诱导和承压结构。

---

## 11. 适合个人复盘的核心问题

读完这篇文章后，最值得自己反复检查的问题有：

1. 当前价格附近到底有多少真实挂单？
2. 这些挂单是在被动守住，还是正在被主动冲击？
3. 价格是否正在测试强支撑/强阻力，还是在制造假突破？
4. 热力图里的结构，是否和成交量、delta、OI 一致？
5. 当前区域是否属于真正的市场价值区，还是只是短暂噪音？

如果这些问题能持续回答得清楚，那么热力图就从“图表工具”升级成了“交易认知框架”。

---

## 12. 原文节选（便于后续逐段细读）

```text
Video Walkthrough
Begin with the video guide for a visual overview of orderbook heatmap dynamics. Everything shown in the video is explained thoroughly in the text below, so you can revisit each concept with more depth.

1.0 Introduction
Every price move begins with a shift in order-book liquidity. Price gravitates toward dense liquidity and repels from thin zones. Every single price movement is dictated by the balance or imbalance of liquidity, and the willingness of market participants to act on it.

2.0 Understanding the Orderbook
Before reading a heatmap, you need to understand what it represents:
Limit Orders – Orders placed at a set price, waiting to be filled. They add liquidity to the market. These orders pay maker fees.
Market Orders – Orders that execute immediately at the best available price. They remove liquidity. These orders pay taker fees.

3.0 How Heatmaps Work
Orderbook heatmaps translate raw order data into a visual timeline of liquidity. Every change in the book—orders placed, moved, or cancelled—is captured and color-coded so traders can track how liquidity evolves in real time.

4.0 Why Heatmaps Matter
Heatmaps expose what traditional charts can’t: the intent behind price action. Instead of just seeing where price moved, you can see why it moved there.

5.0 Key Features
Heatmap Blocks
Each block represents the resting liquidity at a specific price range over time. The color intensity shows how much volume sits at that level, brighter means heavier liquidity.

6.0 Interpreting Heatmap Behavior
Understanding how liquidity behaves is what turns a heatmap from noise into signal. Each pattern reflects trader intent and potential movement.

7.0 From Observation to Application
Once you can read how liquidity behaves, the next step is understanding what to do with it. A heatmap doesn’t give buy or sell signals, it provides context.

8.0 Combining Heatmaps with Other Data
A heatmap shows where liquidity sits and how it moves, but not what happens when it’s hit. To build a complete picture of market intent, combine it with other order-flow and positioning tools.

9.0 Conclusion
Together, they create a complete framework for understanding liquidity, aggression, and positioning, turning static visuals into actionable market context.
```

---

## 13. 备注

这版内容相比上一版进一步拆细了中间章节，重点扩展了“订单簿基础、热力图机制、流动性形态、交易意图判定、以及与其他工具的组合分析”五个核心维度，便于后续做学习笔记、研究复盘和实盘理解使用。
