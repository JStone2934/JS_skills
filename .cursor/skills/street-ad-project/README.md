# street-ad-project · 街边小广告

[← 返回总览](../../../README.md)

---

## 概览

| 项 | 值 |
|----|-----|
| **Skill 文件** | [SKILL.md](SKILL.md) |
| **Prompt 模板** | [prompt-template.md](prompt-template.md) |
| **范例** | [examples.md](examples.md) |
| **标识** | `street-ad-project` |
| **触发方式** | `@street-ad-project`、或明言「按街边小广告 Skill 介绍项目」 |
| **自动启用** | 否（`disable-model-invocation: true`） |

用中国街边小广告的**土味 / 暧昧 / 灰色双关**语气，为项目写 parody 文案，并可生成仿非法张贴的竖版海报图（默认带项目链接）。仅在用户**显式点名**本 skill 时执行。

---

## 三种风格

| 路线 | 感觉 | 示例 |
|------|------|------|
| **办证刻章·土味** | 大字、包查包办、专治 | `头顶异响·包查` |
| **寂寞热线·暧昧** | 双关、夜深了、私聊梗 | `别抬头·我帮你盯` |
| **灰色双关·混搭** | 野一点；外挂/监控 parody | `天上监控·免费装` |

---

## 工作流程

```
1. 取材  → 读 README / URL，提炼卖点与气质
2. 定风格 → 土味 / 暧昧 / 混搭（默认混搭；可三种都要文案）
3. 定文案 → 短句 + 整版（含项目链接）
4. 定视觉 → 按项目特点定配色、字体、装饰（非千篇一律红底）
5. 出图  → GenerateImage 竖版 3:4，底部印 github.com/… 链接
6. 校验  → 标题可读、链接清晰、事实不歪曲
7. 交付  → 展示成图 + 可复制文案
```

---

## 核心规则

- **取材**：以 README 为准；夸张可俏皮，**事实不得歪曲**。
- **链接**：整版文案与海报图**均须**带项目 URL（用户指定则以指定为准）。
- **视觉**：配色/字体/元素随项目变化（GalGame 粉紫对话框、雷达磷光绿等），见 [prompt-template.md](prompt-template.md)。
- **质感**：保留歪贴、卷边、脏墙等小广告特征，但与项目色板融合。
- **安全**：幽默 parody；图中避开易审核拦截词（见 SKILL 出图安全表）。
- **交付**：默认不改仓库、不提交 git、不把图写入仓库，除非另行要求。

---

## 如何启用

```
@JS_skills/.cursor/skills/street-ad-project/SKILL.md
```

或简写：

```
@street-ad-project
```

**示例指令：**

- `@street-ad-project 给当前项目做混搭风格小广告，要出图带链接`
- `@street-ad-project 三种风格都要文案，只出混搭图`
- `@street-ad-project 横版广告墙，拼两个项目`

---

[← 返回总览](../../../README.md) · [查看 SKILL.md 全文 →](SKILL.md) · [Prompt 模板 →](prompt-template.md) · [范例 →](examples.md)
