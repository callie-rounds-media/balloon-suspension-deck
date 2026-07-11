# Autonomous image generation — self-review rubric (Callie asleep 2026-07-10)

Driving ChatGPT tab 1355981339 (Kyle's unlimited account), hero attached. One continuous chat so GPT keeps the hero in context. Generate → screenshot → grade → re-prompt until clean → download to this folder → wire into deck → commit.

## Canonical hero (must match every shot)
eBay LIVE rainbow balloon HIGH in open sky, basket beneath with a couple people. Platform suspended DIRECTLY BENEATH the balloon on 4 corner cables. Football field on the platform: goalposts both ends, yard lines, field-light towers, eBay logos on the skirt. Golden-hour sunset, sea of clouds far below. Everyone ON the platform.

## HARD FAILS — reject and re-prompt
1. Platform beside / level with the balloon instead of hanging underneath it on cables.
2. Anyone or anything off the platform edge / floating in open air. Cheerleaders included — feet on the deck.
3. More than 6 players in any wide shot. Count them.
4. Invented elements not in the hero: crowd, stands, stadium, jumbotron, screens, second balloon, wrong branding, text gibberish.
5. Palette/lighting not matching golden-hour (no blue midday, no night, no neon).
6. AI artifacts: extra limbs, melted faces, distorted eBay logo, garbled card text.
7. Harsh/over-contrasty grade. Callie wants soft, pastel, fluffy clouds, gentle light.
8. Vertical crop. Concept photos are horizontal 16:9.

## The set
1. 01-cardbreak — close on ONE player on the field opening a sealed card pack, fan of cards to camera. Balloon+cables above, clouds below.
2. 02-pull — extreme close-up of hands holding ONE rare card up to the golden sky, balloon/clouds soft behind.
3. 03-ebaylive-app — BUILD IN HTML, not image-gen (phone showing eBay Live feed of the aerial game + Break'n Bad seller badge + bids ticking). Sharper hand-built.
4. 04-cobrand-wide — full drone wide, balloon in eBay Live livery + a Break'n Bad mark, platform below with EXACTLY 6 players + 3 cheerleaders, all on platform. Match hero geometry.
5. 05-cheer — close on 3 cheerleaders on the platform sideline mid-cheer, game blurred behind, balloon/cables above.

## Status log (update as I go)
- 01-cardbreak-a.png — APPROVED. Player kneeling on 50, fan of trading cards + sealed pack, balloon+cables above, clouds around, golden light. Correct geometry, matches hero.
- Download method that works: page-context fetch(img.src)->blob->a.download (saves to ~/Downloads), then cp into set/.
- Composer bottom ~ (660,653), send ~ (1103,652). Continuing one chat so GPT keeps hero context; reference "the same eBay LIVE balloon football scene".
- WORKFLOW NOTE: ChatGPT hangs on "One last tweak..." placeholder even after gen finishes. Fix: after ~30s, RELOAD the chat URL, then the finished image renders. Then download.
- 02-pull-a.png — APPROVED. Two hands holding a prismatic RC rookie card to the sunset, eBay LIVE balloon blurred behind, clouds below. Clean hands, correct branding, matches hero.
- 03-cheer-a.png — APPROVED. 3 cheerleaders in eBay tops on platform, pom-poms up, balloon+cables above, real game behind, clouds around, golden light. Clean.
- SEND NOTE: click composer, type, then press key "Return" to send (button moves and clicks miss).
- 04-wide-a.png — REJECT (too many players ~7-8). Kept as busy backup only.
- 04-wide-b.png — APPROVED. Wide co-brand hero: EXACTLY 6 players (3 red + 3 white at the 50) + 3 cheerleaders, balloon+cables above, suspended platform in clouds, lights, eBay skirt. Count-fix re-prompt worked ("exactly six, 3 red 3 white at the 50, remove extras").
- COUNT RULE learning: GPT overshoots player count on wide shots; fix by re-prompting with exact placement + colors, then re-count at full-res.
- 05-celebrate-a.png — APPROVED. Two teammates (red) on field reacting to a pulled card, balloon above, clouds below. Clean hands, card clear.
- 06-packtear-a.png — APPROVED. Hands ripping a foil card pack, cards spilling, balloon blurred behind, golden light. Clean.
- KEEPERS so far: 01-cardbreak-a, 02-pull-a, 03-cheer-a, 04-wide-b, 05-celebrate-a, 06-packtear-a. (04-wide-a = busy backup.)
