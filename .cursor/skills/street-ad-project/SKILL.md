---
name: street-ad-project
description: >-
  Generates Chinese street-flyer (街边小广告) copy and parody poster images for a
  project: earthy 办证刻章 style, ambiguous 寂寞热线 style, or edgy mixed 灰色双关
  style. Reads README for facts; adapts colors, typography, and motifs to project
  traits; embeds project URL on posters. Default portrait 3:4. Use only when the
  user explicitly invokes this skill (e.g. @street-ad-project) or asks to follow
  it by name.
disable-model-invocation: true
---

# Street Ad Project · 街边小广告

用中国街边小广告的土味、暧昧、灰色双关语气，为**当前项目**写文案并出一张（或一组）仿非法张贴的 parody 海报图。仅在用户**显式点名**本 Skill 时执行。

## When to use

- 用户 `@street-ad-project` 或写出本 Skill 全名/路径并要求按此执行
- 用户明确说「按街边小广告 Skill」「做小广告风格介绍这个项目」等点名措辞

不要在用户只说「介绍一下项目」「写点文案」且未点名本 Skill 时自动启用。

## Workflow

复制并跟踪进度：

```
Progress:
- [ ] 1. 取材
- [ ] 2. 定风格路线
- [ ] 3. 定文案
- [ ] 4. 定视觉
- [ ] 5. 出图
- [ ] 6. 校验
- [ ] 7. 交付
```

### 1. 取材

读项目根目录 `README.md`（或用户指定的文档 / GitHub 链接）。提炼：

- 项目/仓库名与**可公开链接**（GitHub、官网；优先 README 中的）
- 一句话痛点或 slogan
- 2–4 个可夸张但不歪曲的核心功能
- 气质关键词（恋爱/GalGame、监控、硬件、AI、游戏、工具……）

缺 README 时：根据仓库说明或用户给的 URL 取材；**勿编造**未载明的功能。

### 2. 定风格路线

用户未指定时，默认出 **混搭（灰色双关）**；若用户要「全套」「三种都要」，则三种各出一版文案（出图按用户要求，默认可只出混搭图）。

| 路线 | 语气 | 典型句式 |
|------|------|----------|
| **办证刻章·土味** | 大字、直白、包过包查、专治 | `头顶异响·包查` / `★ XX包办 ★` |
| **寂寞热线·暧昧** | 双关、暗示、夜深了、私聊 | `别抬头·我帮你盯` / `你说话的时候·没选项？` |
| **灰色双关·混搭** | 野一点；外挂/监控/破解梗 + 真实功能 | `天上监控·免费装` / `异性聊天·开挂神器` |

规则：

- 短句优先 **4–12 字**，醒目、可独立张贴
- 允许不特别准确，但**不得捏造项目没有的能力**
- 幽默 parody，非真实违法服务；避免真人色情、诈骗话术

### 3. 定文案

每种选定路线输出：

1. **短句** 3–5 条（每条一行）
2. **整版**（仿电线杆小广告排版，含 `★`、间隔号 `·`）：

```markdown
> **{{主标题}}**
> {{卖点行1}} · {{卖点行2}}
> {{卖点行3}}
> **{{行动号召}}**
>
> 👉 {{project_url}}
```

行动号召示例：`免费开源·自己下` / `免费下·自己装` / `寂寞XX族·专属热线`

用户只要文案不要图时，到本步即可交付。

### 4. 定视觉

**必须**根据项目特点单独拟定，勿所有项目共用红底黄字。参照 [prompt-template.md](prompt-template.md) 中的气质映射表。

要点：

- **配色**：与产品 UI / 领域一致（GalGame→粉紫对话框色；雷达→磷光绿 CRT；AI→霓虹紫蓝；硬件→橙黑警示……）
- **字体取向**：标题粗黑/圆体/Stencil/等宽终端等，写入 prompt 的 `headline_typography`
- **装饰元素**：对话框、雷达圈、芯片、终端光标等，贴合项目而非通用 `★` 堆砌
- **小广告质感**：歪贴、卷边、虚线框、脏墙背景、手绘传单感——**保留**，但与项目色板融合
- **链接**：海报**底部黑条或醒目色块**印 `github.com/org/repo` 或 README 中的短链；须可读

### 5. 出图

用户要图时，调用 `GenerateImage`：

| 项 | 约定 |
|----|------|
| `aspect_ratio` | 默认 `3:4` 竖版；用户要横版/广告墙时用 `16:9` 或 `4:3` |
| `filename` | `{project-slug}-street-ad-{style}.png`；`style` ∈ `tufu` / `nuanmei` / `mix` / `themed` |
| `description` | 按 [prompt-template.md](prompt-template.md) 填空 |

**出图安全（审核）**：图中文案若含「泡妞」「少妇」等易拦截词，改用游戏/技术 parody 表述（如「选项修复」「系统帮选」「好感度可视」），保持混搭气质。

可选：从 README 取 1 张本地产品截图作 `reference_image_paths`（绝对路径），作为海报角标/小插图，**勿**占满版心。

### 6. 校验

用 `Read` 打开生成图，检查：

- 主标题中文可读、少糊字
- **项目 URL 清晰可辨**
- 配色/元素是否与项目气质一致（不同项目不应千篇一律红底）
- 功能描述与 README 无严重背离

不合格则改 prompt 重生成，最多再试 **2** 次。

### 7. 交付

- 对话中展示图片（客户端会显示；勿重复贴大段 Markdown 图链）
- **简体中文**简述：采用的风格路线、主标题、视觉取向、链接、横竖版
- 同时给出整版文案（含链接），便于复制
- **默认不修改**仓库 README/代码；不提交 git
- 不把图写入仓库，除非用户另行要求

## Do not

- 未点名时自动介入
- 冒充真实办证、色情、诈骗类广告
- 为「更野」捏造 README 没有的功能
- 图中漏写用户要求展示的项目链接

## Additional resources

- GenerateImage 填空模板与气质映射：[prompt-template.md](prompt-template.md)
- 参考范例（文案与视觉取向）：[examples.md](examples.md)
