# GenerateImage prompt template · 街边小广告

Fill every `{{slot}}`, pass as `description`. Keep Chinese headlines **verbatim** in the prompt for legible lettering.

## Orientation

| User intent | `aspect_ratio` | Layout hint |
|-------------|----------------|-------------|
| Default / 竖版 | `3:4` | Vertical torn flyer on concrete wall, crooked paste |
| 横版 / 广告墙 | `16:9` or `4:3` | Wide wall with 1–3 flyers side by side |
| 双项目拼贴 | `16:9` | Two flyers on same pole/wall, different color schemes |

## Full template

```
Chinese street wall advertisement poster parody, wild edgy humor, NOT a real illegal service ad.

PROJECT AESTHETIC (must match this product — do not default to generic red/yellow):
- Domain vibe: {{domain_vibe}}
- Color scheme: {{color_scheme}}
- Headline typography: {{headline_typography}}
- Decorative motifs: {{decorative_motifs}}

STREET-FLYER TEXTURE (always include):
- Torn paper edges, illegally pasted on dirty concrete wall, slightly crooked angle
- Dashed border frame, crude hand-painted / flyer print look
- Black stars ★ acceptable but secondary to project motifs

COPY (sharp legible Simplified Chinese — use verbatim):
- Main headline (huge, outlined): {{main_headline}}
- Subline 1: {{subline_1}}
- Subline 2: {{subline_2}}
- Subline 3 (optional): {{subline_3}}
- Call to action: {{call_to_action}}

URL BAR (CRITICAL — bottom black or dark bar, white/green text, must be readable):
{{project_url}}

STYLE ROUTE: {{style_route}} (tufu = bold red/orange 办证风 | nuanmei = neon pink/purple night hotline | mix = edgy surveillance/gaming gray humor with project colors)

Do NOT use photorealistic people. Simple flat graphic / illustrated flyer. Humorous tech parody only.
```

## Slot guide

| Slot | How to fill |
|------|-------------|
| `domain_vibe` | One line from README tone, e.g. `GalGame romance UI`, `ADS-B desktop radar gadget` |
| `color_scheme` | Concrete colors tied to product — see table below |
| `headline_typography` | e.g. `rounded bold galgame title font` / `phosphor green stencil military` / `narrow black 办证体` |
| `decorative_motifs` | e.g. `dialogue boxes, SAVE button` / `radar rings, sweep line, squawk 7700` |
| `main_headline` | 4–12 chars, from §3 定文案 |
| `subline_*` | Selling points with · separators |
| `call_to_action` | `免费开源·自己下` etc. |
| `project_url` | `github.com/org/repo` or full https URL — **required on image** |
| `style_route` | `tufu` / `nuanmei` / `mix` |

## Project aesthetic mapping (derive each time)

| Project气质 | 配色 | 字体 | 装饰 |
|-------------|------|------|------|
| GalGame / 恋爱 / 对话 | 粉紫渐变、对话框白底、金黄选项钮 | 圆润粗标题、VN 对话框正文 | 对话框、选项 pill、SAVE、♥ |
| 雷达 / 航空 / 监控 | 深海军黑底、磷光绿 `#00FF41`、琥珀告警 | Stencil 军事标题、等宽终端副文 | 同心圆、扫描线、航迹点 |
| AI / Agent | 霓虹紫蓝、深色底 | 锐利黑体、略未来感 | 终端光标、神经网络简图 |
| 硬件 / 嵌入式 | 橙黑警示、pcb 绿 | 粗黑宋、油墨毛边 | 引脚示意、焊点、⚡ |
| Web / 开发者工具 | 深色底 + 品牌色 accent | 简洁无衬线 / 等宽 | 终端窗口、logo 角标 |
| 游戏 | 高饱和、像素或漫画色 | 漫画标题或像素字 | 血条、coin、手柄简图 |
| 安全 / 运维 | 黑底红字告警 | 窄黑体冷峻 | 锁、盾牌、日志行 |

**Cross-project rule:** 小广告「野贴」质感保留，但**色板与字体必须随上表（及 README）变化**。

## Style route tweaks

### tufu 办证刻章

- Prefer high-contrast red/orange ground **unless** it clashes with project mapping — then use project colors with 办证式粗黑描边
- Headline pattern: `★ {{topic}}包查 ★` / `专治{{pain_point}}`

### nuanmei 寂寞热线

- Dark purple/magenta night tones; neon pink accents
- Headline pattern: `夜深了·{{hook}}` / `别{{verb}}·我帮你{{verb2}}`
- Keep suggestive **humor only**; no explicit adult content in image text

### mix 灰色双关

- Use project-native palette (not generic red)
- Headline pattern: `{{thing}}·开挂神器` / `{{thing}}监控·免费装` / `{{thing}}·选项修复`
- Surveillance / gaming cheat / crack parody tone

## Content safety (image generation)

If blocked, rephrase on-image text:

| Avoid in image | Safer parody substitute |
|----------------|-------------------------|
| 泡妞、撩妹、少妇 | 选项修复、系统帮选、好感度可视 |
| 色情、上门服务 | 删掉；改「专属热线」「悄悄提醒」 |
| 破解版（敏感上下文） | 外挂神器、Bug 已修复 |

## Checklist before generate

- [ ] `project_url` present and legible in prompt
- [ ] Colors/fonts/motifs match **this** project (not generic template)
- [ ] `style_route` matches user request
- [ ] Chinese headlines copied verbatim into prompt
- [ ] Street-flyer torn/crooked texture included
- [ ] No false claims beyond README facts

**Filename:** `{slug}-street-ad-{style}.png`
