# GenerateImage prompt template

Fill every `{{slot}}`, then pass the result as `description`. Keep Chinese headlines verbatim in the prompt so lettering is accurate.

**Do not reuse a fixed masthead across projects.** Derive `masthead` and `masthead_typography` from the current project's README tone, domain, and stack each time.

## Orientation

| User intent | `aspect_ratio` (tool arg) | `orientation` (prompt text) | `layout_hint` |
|-------------|---------------------------|-------------------------------|---------------|
| Default / 横版 | `4:3` | `landscape` | Classic broadsheet: masthead top, headline spanning width, left column + right sidebar side by side, flow bar at bottom |
| 竖版 / portrait / 纵向 / 竖屏 | `3:4` | `portrait` | Vertical tabloid: masthead top, headline below, body columns **stacked top-to-bottom** (lead then sidebar, or narrow side column beside stacked blocks); flow bar at bottom, may wrap to two rows |

## Full template

```
Chinese tabloid newspaper front page, {{orientation}} {{aspect_ratio}}, cream aged newsprint with grain and faint ink bleed. Classic Chinese newspaper columns and rules — NOT a modern marketing poster.

LAYOUT ({{orientation}}):
{{layout_hint}}

MASTHEAD (sharp Chinese, project-adaptive):
- Newspaper name in large bold type: {{masthead}}
- Masthead typography (must match project style): {{masthead_typography}}
- Date line: {{date_line}}

MAIN HEADLINE (huge, spanning, sharp legible Chinese):
{{main_headline}}

SUBHEADLINE (sharp Chinese):
{{sub_headline}}

LEFT COLUMN lead (readable Chinese body, 2–4 sentences):
{{lead_paragraph}}

RIGHT SIDEBAR headlines (sharp Chinese, 1–2 items):
{{sidebar_headlines}}

{{#if has_readme_images}}
INSET PHOTOS from reference images (CRITICAL layout rules):
- Use the provided reference image(s) as 1–{{image_count}} small inset illustrations only.
- Place them inside a text column OR mid-page beside copy — like newspaper photo callouts with thin rules/captions.
- Do NOT make reference photos a full-bleed hero, banner, or page-dominating poster.
- Keep the masthead and main headline text-dominant; insets must stay secondary.
- Preserve recognizable content from each reference (product UI, hardware, diagram) so a reader can tell they match the project docs.
{{/if}}
{{#unless has_readme_images}}
No project photo insets. Rely on diagram/schematic only.
{{/unless}}

SCHEMATIC / FLOW (required, coexist with any insets):
{{schematic_or_flow}}

STYLE:
- Body text: black ink on cream paper, legible Simplified Chinese
- Masthead font MUST follow {{masthead_typography}} — it should feel native to this project's domain
- No purple gradients, no neon glow, no Instagram poster aesthetic, no UI card mashup
```

## Slot guide

| Slot | How to fill |
|------|-------------|
| `aspect_ratio` | `4:3` landscape (default) or `3:4` portrait when user asks 竖版 |
| `orientation` | `landscape` or `portrait` — must match `aspect_ratio` |
| `layout_hint` | Copy from Orientation table above; for portrait add: tall vertical page, columns stacked not forced side-by-side |
| `masthead` | Fictional name tailored to project domain (4–8 Chinese chars). **No global default.** |
| `masthead_typography` | Concrete font/style for masthead only, e.g. `粗黑宋体带油墨毛边，创客小报风` / `锐利现代黑体，偏科技周刊` / `仿宋庄重，学术内幕报` |
| `date_line` | Today's date + edition tag matching project, e.g. `2026年7月9日 · 创客专刊 · 竟有这样的事` |
| `main_headline` | Exaggerated hook tied to project |
| `sub_headline` | Accurate mechanism in one line |
| `lead_paragraph` | Facts + limits from README |
| `sidebar_headlines` | One bullet per line |
| `image_count` | `1`–`3` when using `reference_image_paths` |
| `schematic_or_flow` | Short flow or pin-safe wiring summary; must not contradict README |

### Masthead examples by project type (derive, don't copy blindly)

| Project type | `masthead` example | `masthead_typography` example |
|--------------|-------------------|------------------------------|
| ESP32 / hardware | `创客电报` | 粗宋体、铅字印刷感、略毛边 |
| AI / Agent | `智能奇闻周刊` | 锐利黑体、干净、略带未来感 |
| Web app | `全网爆料` | 现代黑体、利落 |
| Game | `游侠快讯` | 圆体或漫画标题字，活泼 |
| Data / research | `数据内幕周刊` | 仿宋、庄重克制 |

When calling the tool: set `reference_image_paths` only if README images were selected; omit the INSET PHOTOS block (use the “no project photo” line) when count is 0.

**Filename:** `{slug}-newspaper-front.png` (landscape) or `{slug}-newspaper-front-portrait.png` (portrait).

## Checklist before generate

- [ ] `aspect_ratio` and `orientation` match user request (竖版 → `3:4` + portrait layout)
- [ ] `masthead` and `masthead_typography` fit **this** project's README tone (not a reused default)
- [ ] Main title is Chinese and sensational but not false
- [ ] Pins/commands/triggers in lead or schematic match README
- [ ] Insets request says “small / secondary / not hero”
- [ ] Schematic or bottom flow is present even when insets exist
