# JS_skills · 说明

> **「设官分职，以为民极。」** — *《周礼·天官冢宰》*

本仓收藏 **Cursor Agent Skills**（`.cursor/skills/` 下的 `SKILL.md`）与演示脚本。在对话中 `@` 对应 skill，助手即按该 skill 的条贯作答。

![JS_skills 头版宣传图](assets/js-skills-newspaper-front.png)

---

## Skills 导航

点击下方标题，进入各 skill 的说明页：


| Skill                                                                       | 说明                            | 文档                                                       |
| --------------------------------------------------------------------------- | ----------------------------- | -------------------------------------------------------- |
| [zhou-li-citation](.cursor/skills/zhou-li-citation/README.md)               | 《周礼》引用体：开篇即礼、随文屡引、篇末钤印        | [→ 阅读](.cursor/skills/zhou-li-citation/README.md)        |
| [bible-citation](.cursor/skills/bible-citation/README.md)                   | 《圣经》引用体：开篇即经、译本语体、篇末「阿 门」     | [→ 阅读](.cursor/skills/bible-citation/README.md)          |
| [newspaper-project-front](.cursor/skills/newspaper-project-front/README.md) | 项目小报头版：读 README 取材，生成中文报纸风宣传图 | [→ 阅读](.cursor/skills/newspaper-project-front/README.md) |


---

## 快速上手

1. **纳仓**：将整个仓库并入你的项目，或只复制 `.cursor/skills/` 到目标项目的 `.cursor/skills/`。
2. **召之**：在 Cursor 对话中 `@` 对应路径，例如：
  ```
   @JS_skills/.cursor/skills/zhou-li-citation/SKILL.md
  ```
   路径以你当前工作区根目录为准。
3. **释之**：同一会话中若明确说「勿用周礼体」等，以你的指令为准；再次 `@` 该 skill 则条贯恢复。

> 各 skill 均设 `disable-model-invocation: true`，**不会自动启用**，须你显式 `@` 或点名。

---

## 目录结构

```
周礼_skills/
├── assets/
│   └── js-skills-newspaper-front.png
├── .cursor/skills/
│   ├── zhou-li-citation/
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   └── reference.md      # 旧牍存档；skill 运行时不得据此选句
│   ├── bible-citation/
│   │   ├── SKILL.md
│   │   └── README.md
│   └── newspaper-project-front/
│       ├── SKILL.md
│       ├── README.md
│       └── prompt-template.md
├── quicksort_demo.py
├── merge_sort_demo.py
└── README.md                 # 本页（总览）
```

---

## 附录

- [quicksort_demo.py](quicksort_demo.py) — Python 3 演示快速排序与堆排序；注释借《周礼》喻算法，与 skills 无必然关联。

```bash
python3 quicksort_demo.py
```

---

## 声明

- Skills 中文辞、体例由作者自定；引用《周礼》《圣经》时，请注意版权与学术引用规范。
- 公开仓库时，勿提交密钥、令牌等敏感信息。

---

*本页为总览索引；各 skill 的职守细则见上方链接。`SKILL.md` 为 Agent 实际执行的规则原文。欲观钤印、密引之全，须 `@` 各 `SKILL.md` 而后令助手答他题，乃见其实。*