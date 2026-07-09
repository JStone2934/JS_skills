---
name: newspaper-project-front
description: >-
  Generates a Chinese tabloid/newspaper front-page image that introduces the
  current project with sensational headlines. Masthead name and masthead typography
  adapt to each project's domain and tone (not a fixed default). Reads README for
  facts; embeds 1–3 README images as inset illustrations when present. Use only when
  the user explicitly invokes this skill (e.g. @newspaper-project-front) or asks to
  follow it by name.
disable-model-invocation: true
---

# Newspaper Project Front

用中文小报头版的夸张标题，做一张**介绍当前项目**的宣传图。仅在用户**显式点名**本 Skill 时执行。

## When to use

- 用户 `@newspaper-project-front` 或写出本 Skill 全名/路径并要求按此执行
- 用户明确说「按报纸头版 Skill 介绍这个项目」等点名措辞

不要在用户只说「介绍一下项目」「画张图」且未点名本 Skill 时自动启用。

## Workflow

复制并跟踪进度：

```
Progress:
- [ ] 1. 取材
- [ ] 2. 收图
- [ ] 3. 定文案
- [ ] 4. 出图
- [ ] 5. 校验
- [ ] 6. 交付
```

### 1. 取材

读项目根目录 `README.md`（或用户指定的文档）。提炼：

- 产品/仓库名
- 一句话卖点
- 关键机制或硬件事实（引脚、命令、协议等）
- 触发条件与限制（何时有效、何时不触发）

缺 README 时：问用户指定文档，或根据仓库内最显眼的说明文件取材；勿编造技术参数。

### 2. 收图

从 README（及同文档明确引用的路径）收集**本地**图片：

- 用 Grep 找 `!\[.*\]\([^)]+\)` 与相对路径的 `.png` / `.jpg` / `.jpeg` / `.webp` / `.gif`
- 解析为工作区绝对路径；跳过纯外链 URL（无法作 `reference_image_paths`）

筛选（最多 **3** 张）：

| 优先 | 排除 |
|------|------|
| 产品截图、硬件实物、架构图、演示结果 | 徽章（shields）、favicon、纯 logo 小图、装饰线 |

0 张：跳过配图，出图时仅用示意/流程图。

### 3. 定文案

中文小报语气；**夸张标题可以俏皮，事实不得歪曲**。

#### 3a. 定报名与报头字体（随项目变化，勿写死）

根据 README、项目名、技术栈与整体气质，**当场拟定**虚构报名与报头字体，不要套用固定名称。

**读项目气质**（可多选叠加）：

| 项目气质 | 报名方向示例 | 报头字体方向 |
|----------|--------------|--------------|
| 硬件 / 嵌入式 / 创客 | 「创客电报」「焊台奇谭号外」「极客硬件周刊」 | 粗黑宋、老式铅字、略带油墨毛边 |
| AI / Agent / 自动化 | 「智能奇闻周刊」「算法头条号外」「机器说话报」 | 锐利黑体、略未来感但仍像报纸 |
| Web / 全栈 / SaaS | 「全网爆料」「产品内幕快报」「接口风云」 | 现代黑体、干净利落 |
| 游戏 / 娱乐 | 「游侠快讯」「像素江湖号外」 | 活泼圆体或略带漫画感标题字 |
| 数据 / 科研 / 学术 | 「数据内幕周刊」「实验奇闻录」 | 仿宋、庄重宋体，克制戏剧感 |
| 安全 / 运维 | 「漏洞风云号外」「机房秘闻」 | 窄黑体、冷峻、高对比 |
| 开源 / 开发者工具 | 「开源江湖」「Commit 头条」 | 等宽感标题或简洁无衬线 |

规则：

- 报名 4–8 字为宜，可含「号外」「周刊」「快报」「内幕」等小报词，但须**贴合本项目领域**
- 报头字体与项目 UI/文档语气一致：严肃项目勿用卡通字，俏皮项目可更活泼
- 用户若指定报名或字体，从其值；否则每次根据**当前项目**重新拟定，不同项目应明显不同

| 角色 | 约定 |
|------|------|
| 报名 | 按上表与 README 气质拟定，**无全局默认** |
| 报头字体 | 与项目风格匹配的字体描述（写入 prompt 的 `masthead_typography`） |
| 主标题 | 夸张通栏大标题 |
| 副标题 | 准确说明机制或效果 |
| 导语 | 2–4 句，含关键事实与限制 |
| 侧栏 | 1–2 个花边小标题（可点出边界条件） |

日期行用**当天**真实日期；版次语可随项目微调（如硬件项目用「创客专刊」，AI 项目用「智能号外」）。完整 GenerateImage 骨架见 [prompt-template.md](prompt-template.md)。

### 4. 出图

调用 `GenerateImage`：

- `aspect_ratio`：默认 `4:3`
- `filename`：`{project-slug}-newspaper-front.png`（小写、连字符）
- 若有 README 图：把 1–3 个**绝对路径**写入 `reference_image_paths`
- `description`：按 [prompt-template.md](prompt-template.md) 填空；**必须写入**本项目拟定的 `masthead` 与 `masthead_typography`；并硬性写明：
  - 参考图只能作**栏内/中部一侧的小插图（inset）**，1–3 张
  - **禁止**做成通栏英雄大图或整页海报主视觉
  - 须另有简单示意或底部流程条，与配图**并存**

### 5. 校验

用 `Read` 打开生成图，检查：

- 主标题是否可读（中文少糊字）
- 报名、报头字体是否与项目气质匹配（不同项目不应千篇一律）
- 引脚、命令、触发条件等是否与 README 一致
- 配图是否像小插图，而非主导整版

不合格则改 prompt（必要时换参考图子集）重生成，最多再试 **2** 次。

### 6. 交付

- 在对话中展示图片（客户端会显示；勿重复贴大段 Markdown 图链）
- 用**简体中文**简短说明：拟定的报名、报头字体取向、主标题、是否用了 README 配图
- **默认不修改**仓库 README/代码；不提交 git
- 不把图写入仓库，除非用户另行要求

## Do not

- 未点名时自动介入
- 烧录、联调硬件或改固件
- 为「好看」捏造 README 没有的规格
