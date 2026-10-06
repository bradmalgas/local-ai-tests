# Thought for 31 minutes 47 seconds

The user is asking for a premium, high-conversion landing page for an AI startup called "BlueMetric". The requirements are as follows:

- One self-contained index.html file
- Tailwind CSS via CDN, Google Fonts, FontAwesome CDN
- Dark mode aesthetic (deep black/slate) with electric blue and cyan gradients
- Glassmorphism on cards and navbar (user explicitly requested — adopt for cards/navbar, but avoid the generic centered hero trio… the user explicitly requested a hero with headline, subheadline, dual CTA, and animated visual. Need to balance — make the hero asymmetric, left-aligned with an animated network/data visual on the right, don't do the generic centered stack)
- Sticky nav, hero, features (3-4 cards in a responsive grid), footer
- Required animations: fade-in/slide-up on load, hover states (scale + shadow glow), continuous lightweight background animation in hero (floating orbs, typing effect, or moving gradient mesh)
- Responsive, perfect across all breakpoints

Design identity I want:

- Start with something distinctive — for a metrics/analytics AI company, maybe open with a live data terminal/metrics display. The user asked for a hero with headline, sub, dual CTA, and network animation. Can put an animated neural network canvas on one side, and start the hero with a "live metrics ticker" strip or command-line-style opening at the top. Let's do an asymmetric hero: left column with a small monospace "system status" line, big display headline with a distinctive accent (not gradient-filled headline… hmm, the user wants an electric blue/cyan gradient as a brand — gradient on a small word is OK. Avoid gradient-filled heading. Use gradient on one keyword, or solid color with a cyan underline/glow. Actually the user explicitly asked for "vibrant electric blue and cyan gradient" for the brand — can use gradient on the logo, buttons, and one accent word, but keep the headline body solid white. This respects the user request while avoiding a full gradient heading.)
- Distinctive typography: pair a display face with a readable body face. For a tech/AI data company:
    - Display: "Space Grotesk" (techy) or "Sora", or something more distinctive: "Unbounded" is a pretty distinctive display. Body: "Inter" or "Space Grotesk". Monospace: "JetBrains Mono" for data/terminal.
    - Let's pick: display = "Space Grotesk" is a bit overused… "Sora"? Or "Manrope" for body and "Space Grotesk" for display, plus "JetBrains Mono" for data readouts. Actually, let's go bolder: "Unbounded" is very distinctive but heavy. Hmm. For a metrics/analytics AI, "Space Grotesk" display + "Inter" body + "JetBrains Mono" for data/terminal fits. Or "Clash Display" isn't on Google Fonts. Google Fonts: "Space Grotesk", "Inter", "JetBrains Mono". OK.
    - Let me rethink: "Sora" for display (geometric, AI-ish), "Inter" for body, "JetBrains Mono" for code/terminal. Space Grotesk vs Sora — Space Grotesk has that quirky feel that fits the "instrument/terminal" identity. Going with Space Grotesk.

- A rich, content-filled page with multiple sections:
    - Sticky nav with a glass effect, active-link highlight via scroll spy
    - Hero: asymmetric, left copy + right animated canvas (neural network with pulsing nodes and data packets flowing), plus a live "metrics ticker" marquee at the top, maybe. Dual CTA ("Get Early Access" + "View the demo"/"Watch how it works"). Maybe an email-capture form.
    - Logo / trusted-by strip (fictional companies) — as a subtle marquee.
    - Metrics band: big animated counters (e.g., 99.2% prediction accuracy, 4.8B events/day, 320ms latency) with count-up animation on scroll.
    - Features: user said 3-4 cards in a responsive grid. Make it 4, but not a generic row of identical cards — vary the sizes (bento-style) to avoid the "row of identical feature cards" trope: 1 large + 3 smaller bento. Actually the user said "responsive grid of 3-4 feature cards with icons." Can do a bento grid: one wide card with mini visualization, a card with a terminal snippet, a card with a gauge, etc. Each card with an icon, different content — this satisfies the requirement while avoiding identical-card repetition. Let's do 4 cards in a 12-column bento: two rows; card A is 7 wide (with animated chart), card B is 5 wide (with terminal), card C is 5 wide, card D is 7 wide (with gauge/radar). Responsive: 1 col mobile, 2 col md, 12 col lg.
    - "How it works" section — 3 steps with a sticky visual? Signature motion: sticky 2-column — left sticky panel with step indicator, right side scrolls the steps. Or: left sticky code/terminal showing each step in sequence, steps on the right. This is a nice signature motion. Let's do it: "How BlueMetric works" — left sticky panel (live terminal/sequence display that updates based on the step shown in view via IntersectionObserver), 3–4 steps on the right.
    - Product/dashboard preview section: a fake dashboard built in pure HTML/CSS (glass panels, animated bars, sparkline canvas, radar chart) — this gives that "real product" feel. Slight parallax/tilt on mouse movement.
    - Testimonials: 2-3 quotes, maybe with a slight rotation, scattered postcard style.
    - Pricing? Maybe an early access tier — could be simple 3 tiers, but the "row of 3 identical cards" trope… user only asked for hero, features, footer + animations. I can add sections but keep pricing as 1 highlighted plan (early access, free during beta) + waitlist tiers, not a 3-card row. Better: a "Get early access" CTA section with an email form and tier selection (Pilot / Scale / Enterprise) as a segmented control — interactive: selecting the tier updates the copy/seat count. This is interactive and avoids the 3 identical cards.
    - FAQ accordion (a few items) — good for conversion.
    - Footer: copyright + social links + maybe small sitemap.

- Signature motion to include:
    1. Hero neural network canvas (continuous, lightweight, paused when not visible, maybe respects reduced motion).
    2. Live typing/scramble effect: scramble-decode on headline keywords, or monospace status line that cycles through phrases.
    3. Scroll reveal (IntersectionObserver) fade/slide with stagger.
    4. Count-up metrics.
    5. Marquee ticker (logo strip or metrics).
    6. Sticky 2-column "How it works" with step sync.
    7. Mouse parallax/tilt on dashboard preview.
    8. Noise overlay + subtle grid background.
    9. Custom cursor glow? Maybe a radial spotlight that follows the mouse over the hero. Light enough.
    10. Magnetic buttons? Maybe on the primary CTA — could be nice but watch perf; keep it simple: subtle scale + glow on hover (required).

- prefers-reduced-motion: gate canvas animation (draw a static frame), disable marquee (pause), reveal instant, skip scramble.

- Nav: glass, scroll-spy active state, mobile hamburger menu.

- "Get Early Access" button: opens a modal with an email form? This adds interactivity and conversion focus. Click shows a modal with a form; on submit show a success state with a fake queue position ("You're #2,431 in line"). Also the CTA section form does the same. Nice touch. Let's implement the modal.

Let me nail the visual identity concretely:

- Palette:
    - Base background: #05070d / #070b14 (deep bluish near-black)
    - Surface: #0b1220, rgba white 3-6%
    - Electric blue: #2563eb / #3b82f6; cyan: #22d3ee / #06b6d4; accents #7dd3fc
    - Text: primary #e6edf7, muted #8b98b0 / #64748b
    - Line: rgba(148, 163, 184, 0.12)
- Typography: Space Grotesk (display, weights 500/700), Inter (body 400/500/600), JetBrains Mono (data).
- Gradients: linear 135deg #2563eb → #06b6d4; glow shadows cyan.
- Grid background: subtle 1px lines via CSS background-image, with a mask that fades.
- Noise overlay: SVG data-uri feTurbulence, low opacity, fixed, pointer-events none.
- Section labels: monospace uppercase with a small square/dot marker, e.g., "[ 01 ] — CAPABILITIES".

Layout details:

- Nav: fixed top, glass (backdrop-blur), logo = a square mark with pulse rings + "BlueMetric" wordmark (Monospace "BM" glyph? or custom SVG waveform). Links: Product, How it works, Metrics(?), Pricing/Access, FAQ. Right: "Get Early Access" gradient button. Add a thin scroll progress bar at the top? Nice detail — a 2px gradient bar showing scroll progress. Adopting.
- Hero: 12-col grid. Left (span 6): monospace status line with a blinking cursor, cycling phrases (typing effect); H1 with a scramble-decode on load on the keyword; sub; CTA row (primary gradient "Get Early Access", secondary ghost "Watch the 90-sec tour" with play icon — maybe open a modal with fake terminal demo, or scroll to dashboard? Simpler: scroll to product section, or a small "demo" that replays the network… let's just have it scroll to the dashboard preview with a smooth scroll; or trigger a confetti-style pulse? Let's have it scroll to #product). Then a mini social proof: avatar stack + "2,300+ teams on the waitlist" with a live incrementing counter (increment every few seconds). Right (span 6): canvas neural net in a glass frame with HUD corners + a floating mini metric chip (glass chips: "anomaly detected −99.98%", etc.) with floating animations.
    - Behind the hero: canvas orbs? User asked for "continuous, lightweight background animation in hero (e.g., floating glowing orbs, typing effect, or moving gradient mesh)." The neural canvas IS the hero animation, plus a typing effect on the status line — 2 animations, plus a slow hue-drifting radial glow. Keep it light: canvas runs at ~30fps, pause off-screen via IO, reduced-motion → static draw.
- Ticker marquee: below hero, a thin band with monospace metrics scrolling (like a stock ticker): "▲ API P95 312ms ● 4.8B EVENTS/DAY ▲ ACCURACY 99.2% ..." CSS animation marquee, duplicate content, pause on hover, reduced-motion → static.
- Logo strip: "Trusted by data teams at" — text wordmarks (fictional: VANTIQ, Nordbank, Helios Robotics, Kite Labs, Arclight, Paddle.io…) in a second marquee, or a static row. Could combine with the ticker… maybe: ticker band (metrics) directly below hero, then a logo row above features. Or one marquee with alternating logos + metrics. Simpler: two marquees in one strip, moving in opposite directions. Rich. Let's do that: top marquee = logos (dim, hover to full opacity), bottom = metrics ticker. Actually to reduce clutter, one marquee with both, "trusted by" label on the left. Hmm, let's do: a strip with "TRUSTED BY TEAMS SHIPPING AT SCALE" + a single marquee of 8 text wordmarks, then the metrics band as its own section with count-ups later. Wait, the metrics band with counters — place it right after features, or as a full-width band after hero. Let's arrange the sections:

1. Nav (fixed) + scroll progress bar
2. Hero (canvas net, typing status, scramble headline, dual CTA, live waitlist counter, floating chips)
3. Marquee logo strip
4. Features (section label 01 — Capabilities): 4-card bento, each with different micro-visual:
    - A (7 col, tall): "Predictive anomaly detection" — animated bar/line chart (canvas or CSS bars animating) + icon
    - B (5 col): "Natural-language queries" — terminal snippet with typing loop
    - C (5 col): "Zero-pipe deployment" — code/deploy snippet or gauge
    - D (7 col): "Vector-native storage" — radar/scatter plot pulsing
      Hover: lift + glow + border highlight, icon color shift. Cards are glass.
5. Product preview (02 — The console): big glass dashboard mock built from divs: sidebar, KPI tiles, chart canvas (animated), table with rows, sparklines. Tilt on mouse. Label + copy on top. This gives real substance.
6. How it works (03): sticky 2-col — left sticky: heading + live "pipeline" visualization (3 nodes lighting up per active step) or a terminal whose lines change; right: 3-4 steps with titles, text, monospace step numbers. IO syncs the active step → highlight left visual + progress line.
7. Metrics band: 4 count-up stats (big monospace numerals): 99.2% accuracy, 4.8B events/day, 210ms median query, 63% fewer false alarms — with a subtle divider.
8. Testimonials: 3 slightly-rotated, scattered glass postcards (-3°, 2°, -1.5°), straighten on hover; monospace titles, quotes, avatars (gradient initial circles).
9. Access / Pricing (04 — Early access): heading + segmented tier control (Pilot / Scale / Enterprise) — JS updates description + price (All Free in beta) + perk list; then email input + "Reserve my spot" button → success state with a queue number. Also mention "No credit card. Cancel whenever."
10. FAQ: accordion 5 items, animated (max-height/grid-rows trick).
11. Final CTA band? Merged with access section; skip to avoid redundancy. Instead a mini "ready" banner → scroll to access. Or end with a footer.
12. Footer: top row logo + tagline + social icons (GitHub, X, LinkedIn, Discord) as glass icon buttons; columns: Product / Company / Resources links; bottom row: © 2025 BlueMetric, "All systems operational" pulse dot, "SOC 2 · GDPR" mono badges.

Modal: "Get Early Access" — glass modal with backdrop blur, form (email), tier preselected from the access section if applicable; on submit → spinner → success with assigned position in queue + close. Basic focus trap (at least Esc to close, click backdrop to close).

JS inventory (vanilla):

- Scramble/decode on hero headline keyword on load (reduced-motion: skip)
- Typing loop on status line (reduced: static)
- Neural canvas: nodes + edges + pulses; DPR aware; pause off-screen; reduced → draw one static frame
- IO reveal: [data-reveal] with stagger via --d custom property
- Count-up on visible (respect reduced → set final value)
- Scroll-spy for nav + progress bar
- Mobile menu toggle
- Access tier toggle
- Form submit → queue number (random 1200-3600), confetti? Maybe a small pulse of sparks via CSS
- Tilt on dashboard (pointermove, disabled on touch/reduced)
- FAQ accordion
- Modal open/close (Esc, backdrop), from multiple triggers [data-modal]
- Live waitlist counter in hero: base 2347, +1 random increment every 6-14s, with a flash
- Marquee: pure CSS, respect reduced (animation: none)
- Smooth scroll: CSS scroll-behavior + JS for offset? Use scroll-margin-top on sections.

Performance: keep node count modest (~70 nodes in hero, edges to nearest ~3). requestAnimationFrame single loop for canvas; pause when tab hidden (document.hidden) and when hero out of viewport.

Tailwind CDN: use https://cdn.tailwindcss.com with inline config for fonts/colors. Plus a &lt;style&gt; block for custom CSS (glass, noise, marquee keyframes, reveal, grid background, etc.). Note: Tailwind CDN console-warns in production but this is a demo.

FontAwesome: use cdnjs 6.5.x all.min.css.

Google Fonts: Space Grotesk (500,600,700), Inter (400,500,600), JetBrains Mono (400,500,700). Combine into one link.

Now content copy — make it sharp and specific:
Brand idea: BlueMetric = AI layer that turns raw telemetry/events into predictions — "the intuition layer for product teams".
Headline: "Your product, speaking its next move." or: "Metrics that see what happens next." Let me craft:

- Status line (monospace, typing): cycles: "▍ ingesting 4.8B events/day…" "▍ model v4.2 calibrated on your traffic" "▍ anomaly: checkout latency +38ms — predicted 41m ago" etc.
- H1: "See the next failure before your users do." with "next" or "before" scrambled? Scramble the whole headline once? Scrambling the whole big H1 might be heavy; scramble keyword "before" → cycle through words: "See the next [failure / rollout / revenue dip] before your users do." Word rotator with scramble decode. This is a strong signature. Let's do: "See the next &lt;span scramble&gt;failure&lt;/span&gt; before your users do." Rotating words: failure → outage → dip → rollout.
- Sub: "BlueMetric is the predictive telemetry layer for modern product teams. It ingests your full event stream, models the systems that touch it, and calls changes in behavior minutes — sometimes hours — before they surface."
- CTA: [Get Early Access →] [▷ Watch the 90-sec tour]
- Proof: avatar stack + "2,341 teams in the private beta queue" live counter + a "SOC 2 Type II" chip.

Hero right visual: canvas of a neural mesh with HUD frame + 3 floating glass chips: "anomaly flagged · 09:41:22 — p95 checkout +38ms", "forecast: signups +6.2% next 7d", "model confidence 0.97". Chips gently float (CSS keyframes with different durations). Canvas nodes drift slowly, edges, pulses traveling along random edges; colors: blue/cyan mix; occasional "alert" node flashes amber? Keep palette blue/cyan + one accent. Maybe keep it mono-cyan for brand. Add a soft radial glow behind.

Floating chip contents (mono, 11px):

- chip1 (top left, -translate): red? Use cyan: "◆ 14:02:11 · anomaly: p95 +38ms" with sub "routed → @scale team"
- chip2 (bottom right): "forecast · signups +6.2% / 7d" with a small sparkline (CSS bars)
- chip3 (mid right): "model confidence 0.97" with a gauge bar.
  Keep to 3 chips, 2 on mobile hidden.

Canvas HUD frame: absolute-positioned corner brackets via CSS (border on 4 spans). Caption bar at bottom inside frame: "blueMetric.core — live mesh · 128 nodes" + a blinking dot.

Ticker band below hero: border-y, mono 12px, items: "P95 LATENCY 312ms ▲0.4%" etc. Prefix each item with ● / ▲ / ▼. Duplicate list 2x, animate translateX -50%.

Logos: after ticker? Merged: place logo marquee + ticker in same section, but logos above, separated by a line. Two rows, each ~56px. Section total ~120px. OK.

Now for feature cards (id=product → actually "capabilities"):
Card A (lg:col-span-7): icon: fa-wave-square. Title: "Anomaly detection with a pulse." Text: "BlueMetric learns the heartbeat of every service — baselines drift with seasonality, deploys, traffic — and the moment a signal deviates, you know." Visual: CSS bars chart with anomaly bar + dashed forecast? Chart: canvas line with a spike; let's draw a simple canvas sparkline with anomaly highlight + label chip "predicted 41 min before alert". Implementation: mini canvas, draw 40 points, 1 anomaly peak with glow; animate a sweeping scan line? Reveal animation drawing the line (stroke-dash progress). Keep: static draw + a pulse dot moving along the anomaly point (JS or CSS overlay). Simpler: an overlay dot with CSS animation at the anomaly point. Let's do canvas draw on reveal.
Card B (lg:col-span-5): icon: fa-terminal / fa-comment. Title: "Query it like you'd ask a human." Text: "Ask in plain English. BlueMetric compiles intent into metrics, returns the number, the trend, and why it moved." Visual: terminal with a typed Q&A loop: Q: "why did activation dip Tuesday?" A: "−12.4% · attributed to v4.2 onboarding copy; rollback draft attached." Loop typing with reduced fallback.
Card C (lg:col-span-5): icon: fa-cube / fa-cloud-arrow-up. Title: "Zero-pipe deployment." Text: "One drop-in SDK or your existing Kafka topic. No schema, no warehouse, no week of plumbing. Live in under an hour." Visual: code snippet with syntax colors + "▸ deploy complete · 38s" status.
Card D (lg:col-span-7): icon: fa-diagram-project or fa-network-wired. Title: "A living map of your system." Text: "Every dependency, queue, and call graph is modeled continuously — so root cause is a hop, not a hunt." Visual: mini node graph canvas (static layout, pulsing nodes) or CSS radial map. Small canvas with 12 nodes & edges, pulses traveling. Reuse the same drawing helper as hero with fewer nodes.

Grid: lg: grid-cols-12; rows: A(7)+B(5), C(5)+D(7) — offset the 2nd row for rhythm. md: 2 cols (A span2? A md:col-span-2? Then B,C each span1, D span2). Mobile 1 col.

Card micro-interaction: on hover, border glows, icon shifts color, visual scales 1.02, "learn more →" appears? Keep: title arrow nudge.

Sticky 2-col HOW:

- Left sticky (lg): heading "From raw bytes to 'ah, that's why.'" + vertical pipeline visual: 4 nodes connected by a line; active node glows + label; also a terminal box showing a line for the active step:
  step lines:
    1. `▲ ingest   kafka.bluemetric.v1 → 1.2M evt/s`
    2. `▲ stream   windowed · keyed · 42µs/evt`
    3. `▲ predict  model.core  v4.2 · conf 0.97`
    4. `▲ act      slack #scale · runbook · rollback`
       Active step → corresponding line highlighted (add a color class), node filled.
- Right: 4 steps, each min-h ~55vh? Maybe not so tall; use py-16 each. Big monospace ghost numbers "01" behind.
  Steps copy:
  01 Ingest — "Point BlueMetric at anything that emits: SDK, OTel, Kafka, or logs. It reads everything and normalizes nothing — your raw signal stays raw."
  02 Model — "Every service, queue, and feature gets a live statistical twin. Baselines adapt to seasonality, deploys, and the chaos you didn't plan for."
  03 Predict — "When the twin drifts, you get a forecast, not a fire drill: what's about to happen, how confident we are, and the window to act."
  04 Act — "Findings land where work happens — Slack, PagerDuty, your ticketing. With the diff, the likely cause, and a one-click runbook."
  Left visual also includes a progress rail (thin bar with a fill based on active index).

Metrics band: full-bleed section with 4 stats:

- 99.2% "prediction accuracy on flagged incidents"
- 4.8B "events processed daily"
- 210ms "median query → answer"
- 63% "fewer false alarms vs. threshold alerts"
  Count-up with easing; monospace huge (clamp 2.5-4rem) with gradient? Keep numeral white, unit cyan. 1px dividers between; stacked 2x2 on mobile.

Testimonials (scattered): 3 postcards rotated -2.5°, 1.8°, -1.2°, translate offsets; glass; quote icon; quotes:

- "BlueMetric called our checkout regression 40 minutes before our on-call did. That's the whole pitch." — Mara Ellison, VP Eng, Nordbank
- "We deleted three dashboards and two alert rulesets. It replaced both." — Dev Okafor, SRE lead, Helios Robotics
- "Our PMs stopped guessing. They just ask." — June Park, Head of Product, Kite Labs
  Avatars: gradient circles with initials.
  Center a stack on mobile (less rotation).

Access section (id=access): label "04 · early access". Heading: "The queue is open. The price is zero." 2-col: left: tier segmented control + dynamic panel (name, "what you get" list updates, price "Free — for all of 2025"?) Actually beta: all tiers free; tiers differ by scope:

- Pilot: 1 product, 3 team seats, 7-day retention, email findings. Price: $0 in beta.
- Scale: 5 products, 25 seats, 90-day retention, Slack+PagerDuty sync, API access. $0 in beta (post-launch $490/mo).
- Enterprise: unlimited, SSO/SAML, private VPC or on-prem, dedicated model fine-tune, SLA. "Talk to us."
  Panel updates list + right rail with tier-specific note. Button → modal (with tier preselected).
  Right column: glass form card: heading "Reserve your spot", email input + "Reserve" button; on success: check + "You're #2,431 — we'll reach out within the hour." + confetti-esque pulse; small note: "No credit card. Beta ends when it ends — your seat locks at $0."
  Add a small avatar row "joined this week" or similar.

Tier toggle JS: data-tier buttons, panel content object, re-render list with a quick fade.

FAQ (id=faq): 5 items:

- "How is this different from Datadog or a generic observability stack?" → "They tell you what happened. BlueMetric tells you what's about to happen… we layer on top of your existing stack — we're a second opinion, not a rip-and-replace."
- "What data do you actually see?" → "Whatever you pipe in. Your raw payload can stay encrypted with field-level masking; models train on your traffic, never cross-tenant. SOC 2 Type II in flight, audit logs from day one."
- "How long until first value?" → "Most teams see their first prediction within the hour… full confidence builds over ~2 weeks as baselines season."
- "What happens when the beta ends?" → "Every beta seat locks in the founding price forever. No pricing cliff, no bait-and-switch."
- "Does it work with our stack?" → "SDKs for Node, Python, Go, Rust, Java; OTel and Kafka native; if it can emit an HTTP webhook, we can read it."

Footer: as planned.

Now let me write the actual code carefully.

Tailwind config:

```js
tailwind.config = {
    theme: {
        extend: {
            colors: {
                ink: {
                    950: "#04060c",
                    900: "#070b14",
                    800: "#0b1220",
                    700: "#101a2e",
                },
                volt: {
                    DEFAULT: "#2f7bff",
                    bright: "#3b82f6",
                    cyan: "#22d3ee",
                    ice: "#7dd3fc",
                },
                mist: { DEFAULT: "#8b98b3", dim: "#5c6a85", bright: "#e8eef9" },
            },
            fontFamily: {
                display: ['"Space Grotesk"', "sans-serif"],
                body: ["Inter", "sans-serif"],
                mono: ['"JetBrains Mono"', "monospace"],
            },
        },
    },
};
```

Hmm, naming volt for blue. OK.

Custom CSS:

- body background base with a subtle grid: `background-image: linear-gradient(rgba(59,130,246,.05) 1px, transparent 1px), linear-gradient(90deg, ...)` with a radial mask.
- .glass { background: rgba(255,255,255,0.04); border:1px solid rgba(148,163,184,.14); backdrop-filter: blur(14px); }
- .glass-strong for modal
- .btn-primary: gradient, glow shadow, hover: scale+shadow, active scale down.
- .btn-ghost: border, hover fill.
- .noise::after or a fixed .noise div with a data-uri svg, opacity .05, pointer-events none, z high? Place as fixed overlay z-50 but under modal? Modal z-[100], noise z-40. pointer-events none.
- Keyframes: float (chips), marquee, marquee2 (reverse), pulse-dot, blink (cursor), fadeUp for reveal (JS adds .in to reveal class: base .reveal {opacity:0; translateY(24px) scale?; transition ...}; .reveal.in {opacity 1; ...} with transition-delay var(--d)).
- @media (prefers-reduced-motion: reduce): disable animations, reveal visible, marquee none (or allow? set animation none and justify), canvas handled in JS.
- Selection color, subtle scrollbar style.

Scroll progress bar: fixed top 0, height 2px, gradient, width via JS transform scaleX, origin left, z-[60].

Nav active link: .nav-link class with aria-current → cyan color + underline dot.

Also ensure anchor smooth scroll: html {scroll-behavior:smooth} with override for reduced-motion; sections scroll-margin-top: 96px.

Mobile menu: hidden panel with links below nav; toggle via hamburger; closes on click.

Nav background: transparent at top; on scroll &gt;10 → glass + border. Implement with class toggle.

Then the JS. Let me write it structured:

```js
const prefersReduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
```

1. Nav scroll state + progress bar: single scroll listener with rAF throttle.
2. Scroll-spy: IO on sections with rootMargin -40%.
3. Mobile menu.
4. Reveal: IO threshold 0.15, add .in, unobserve. If reduced: add .in immediately.
5. Scramble rotator:

```js
const words = ["failure", "outage", "dip", "rollout"];
```

Scramble function: given an element, target word, use characters "!&lt;&gt;-\_\\/[]{}—=+\*^?#"; iterative reveal. On reduced: just swap text (no scramble, maybe just swap every 3s without scramble or static "failure"). Let's do: reduced → no rotation. 6) Hero typing line: phrases array, type/erase loop. Reduced → static first phrase. 7) Neural canvas (hero) — class Mesh {constructor(canvas, opts) ... build nodes in a box, edges to nearest k (k=2-3), pulses: pick random edge, t 0→1, speed; draw: edges as rgba(59,130,246,alpha by dist), nodes as r 1.5-3 with glow via shadowBlur (watch perf — shadowBlur costly; maybe use only for pulses via small pre-rendered radial gradient). Simplify: draw edges as lines, nodes as small circles; pulses as cyan circles with shadowBlur 8 only on pulses (count ~8) → fine.
Node drift: velocity small, bounce at edges. rAF loop; visibility check via IO on hero + document.hidden. Reduced: draw one static frame (no loop). 8) Mini canvas: bar chart (feature A) — draw on reveal: bars grow (rAF), line + anomaly glow; static on reduced.
Feature D graph: reuse Mesh with nodes=10, edges k=2, static positions (no drift) + pulses. 9) Terminal typing (feature B): loop 2 lines type with delay; reduced → show final. 10) Count-up: on visible IO, animate value over 1.4s easeOutCubic, format with suffix and decimals. Reduced → set final. 11) How-it-works sync: IO on steps (rootMargin center), set active index → update left nodes/lines + progress fill. Also on mobile, hide left? left visual becomes top (stacked) but maybe still keep visible, or hide to save space — keep visible, non-sticky on mobile, fine. 12) Tilt on dashboard: on wrapper pointermove (only if matchMedia('(pointer:fine)') and !reduced): rotateX/rotateY max 3 deg, transition none on move, reset on leave. 13) Access tier: button data-tier; map of content; panel update with small fade (retrigger class). 14) Form: both the access form and the modal form share a submit handler: preventDefault, validate email-ish (input type email required), button loading state (spinner), setTimeout 900ms → success view (hide form, show success with position number = 2400 + random 0-400 + maybe session counter increments live counter). Confetti-lite: generate 12 spark spans with random transform, animate via Web Animations API, remove. Reduced: skip sparks. 15) Modal: open/close functions; triggers [data-open-modal]; close on Esc/backdrop; basic focus management (focus email on open, restore focus). Lock body scroll while open (overflow hidden). 16) Live counter in hero: base number, setInterval 5000-9000 random increment 1-3, format with comma, quick pop class. 17) Chips float: CSS only. 18) FAQ: click to toggle, only one open at a time (close others), button aria-expanded, use grid-template-rows 0fr/1fr trick for smooth height.

Also for the dashboard canvas chart: an animated area line that draws on reveal, maybe with continuous subtle "scan" animation; plus KPI tiles. Keep it as one canvas with draw-once + a moving dot.

Let me also design the dashboard mock content (id=product):
Window frame: top bar with 3 dots + URL "console.bluemetric.io/overview"; body grid:

- Sidebar (hidden on mobile): logo mark, menu items (Overview active, Services, Forecasts, Anomalies, Runbooks, API) as small monospace items with icons.
- Main: KPI row: 4 tiles (p95 latency 212ms ↑2%, error rate 0.03% ↓, RPS 48.2k, confidence 0.97) each with a mini sparkline? Keep with delta chips.
- Big chart: "Checkout service — forecast vs. actual" canvas with 2 series: solid actual + dashed forecast + shaded confidence band. Draw animation.
- Right column: "Forecast queue" list 3 items with colored severity + time ("p95 +38ms — 41 min" amber… keep cyan/red? Use cyan info + 1 alert accent #f59e0b? Blue is the brand; a small amber alert adds realism. Use one amber for anomaly realism. OK, tiny accent is fine.)
- Table: "Recent signals" 4 rows, with monospace service name, delta, status chip.
  This is substantive. Tilt applies to the entire window.

Also add a small "scan" gradient sweep over the dashboard? Or a periodic vertical scan line over the chart. Can add a CSS moving highlight line. Optional; OK, add subtle.

Now let's actually write the code. It's a lot but let's go. Watch out for:

- Tailwind CDN + custom config script order: config after CDN script.
- Fonts preconnect.
- FontAwesome CDN.
- Escape backticks in template literals inside JS (no issue in HTML).
- SVG data URI for noise: use encodeURIComponent-safe string: `background-image:url("data:image/svg+xml,%3Csvg ...%3E")` — write manually encoded.

Noise data URI:
`data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.5'/%3E%3C/svg%3E`

Then marquee CSS:

```css
.marquee-track {
    display: flex;
    width: max-content;
    animation: marquee 40s linear infinite;
}
@keyframes marquee {
    to {
        transform: translateX(-50%);
    }
}
```

Two copies of content inside the track. Reverse: animation-direction: reverse.

Reveal CSS:

```css
.reveal {
    opacity: 0;
    transform: translateY(26px);
    transition:
        opacity 0.8s cubic-bezier(0.22, 1, 0.36, 1),
        transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
    transition-delay: var(--d, 0s);
}
.reveal.in {
    opacity: 1;
    transform: none;
}
@media (prefers-reduced-motion: reduce) {
    .reveal {
        opacity: 1;
        transform: none;
        transition: none;
    }
}
```

Button:

```css
.btn-primary {
    ...background: linear-gradient(135deg, #2563eb, #06b6d4);
    box-shadow: 0 8px 30px -8px rgba(37, 99, 235, 0.5);
    transition: ...;
}
.btn-primary:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 14px 44px -8px rgba(34, 211, 238, 0.55);
}
```

Hero glow: radial gradient, absolute, blur, slow drift (transform/scale keyframes 14s alternate). Reduced → static.

Neural canvas sizing: canvas fills the parent (aspect ratio ~4/3 or fixed h). ResizeObserver or on resize, resize with DPR.

Let me write the Mesh:

```js
function initMesh(canvas, {count=70, maxDist=110, drift=0.25, pulses=7, k=2}){
  const ctx = canvas.getContext('2d');
  let w,h,dpr, nodes=[], edges=[], pulses=[];
  function resize(){
    dpr = Math.min(window.devicePixelRatio||1, 2);
    const r = canvas.getBoundingClientRect();
    w=r.width; h=r.height;
    canvas.width=w*dpr; canvas.height=h*dpr;
    ctx.setTransform(dpr,0,0,dpr,0,0);
    seed();
  }
  function seed(){
    nodes = Array.from({length:count},()=&gt;({x:Math.random()*w,y:Math.random()*h,vx:(Math.random()-.5)*drift,vy:(Math.random()-.5)*drift,r:Math.random()*1.6+0.8}));
    // edges: for each node find nearest k
    edges=[];
    for(let i=0;i&lt;count;i++){
      const d = nodes.map((n,j)=&gt;({j,dist:Math.hypot(n.x-nodes[i].x,n.y-nodes[i].y)}))
        .filter(o=&gt;o.j!==i).sort((a,b)=&gt;a.dist-b.dist).slice(0,k);
      d.forEach(o=&gt;{ if(Math.hypot(nodes[i].x-nodes[o.j].x, nodes[i].y-nodes[o.j].y)&lt;maxDist) edges.push([i,o.j]); });
    }
    // dedupe? Not important; duplicates draw twice alpha, ok but dedupe via Set of key min-max
  }
  ...
  step: move nodes (bounce), respawn pulses along random edge
  draw: edges with alpha by distance; nodes; pulses with glow.
}
```

Dedupe edges with a Set `${a}_${b}`.

Loop with running flag; IO on hero canvas to start/stop.

Mini chart canvas (feature A): draws a baseline area + a spike. Write a generic draw function, animate with a progress param from 0→1, drawing points up to progress*len. Points: generate smooth-ish: 48 points: value = 40 + sin(i*0.3)\*6 + noise; anomaly at i=30: spikes +18 with decay. On reveal run rAF 1200ms. Colors: line cyan, area gradient fill, anomaly segment blue with a glow dot.

Feature D graph: Mesh with drift 0, 14 nodes, k=2, pulses 4 — run loop but pause off-view (use the same runner pattern). Actually simpler: static edges + pulsing glow via sin on nodes? To keep JS light, static layout + pulses is enough.

Unified approach: make an `animators` registry of {start,stop,fn} and a master rAF loop with visibility set. Simpler: each component has its own rAF but gates on `running`. Hero and D graph have separate rAF — fine (2 loops). OK.

Terminal typing (feature B):

```js
const q = "why did activation dip on tuesday?";
const a1 = "−12.4% vs 7d baseline · 94% attributed to v4.2 onboarding copy";
const a2 = "▸ rollback draft attached → runbook #R-118";
```

Type q char-by-char, pause, type a1, a2, hold 2.5s, clear, loop. Reduced: render all instantly.

Step sync detail:

```js
const steps = [...document.querySelectorAll('.step')];
IO with rootMargin: '-45% 0px -45% 0px' → entry.isIntersecting → setStep(idx)
setStep: update .pipe-node active class, .pipe-line highlight, terminal line highlight, progress fill height = (idx+1)/4.
```

Now HTML skeleton:

```html
&lt;!doctype html&gt; &lt;html lang="en" class="scroll-smooth"&gt; &lt;head&gt;
meta, title "BlueMetric — See the next failure before your users do" preconnect
fonts, font link (Space+Grotesk:wght@500;600;700 | Inter:wght@400;500;600 |
JetBrains+Mono:wght@400;500;700) font-awesome cdn tailwind cdn script + config
&lt;style&gt; ... custom ... &lt;/style&gt; &lt;/head&gt; &lt;body
class="bg-ink-950 text-mist font-body antialiased overflow-x-hidden"&gt; &lt;div
class="noise"&gt;&lt;/div&gt; &lt;div id="scrollbar-progress"&gt;&lt;/div&gt;
&lt;header id="nav"&gt; ... &lt;/header&gt; &lt;main&gt; &lt;section hero
id="top"&gt;...&lt;/section&gt; &lt;div logos/ticker band&gt;...&lt;/div&gt;
&lt;section id="capabilities"&gt;bento&lt;/section&gt; &lt;section
id="product"&gt;dashboard&lt;/section&gt; &lt;section id="how"&gt;sticky 2
col&lt;/section&gt; &lt;section metrics band&gt;counters&lt;/section&gt;
&lt;section #voices testimonials&lt;/section&gt; &lt;section #access tiers +
form&lt;/section&gt; &lt;section #faq accordion&lt;/section&gt; &lt;/main&gt;
&lt;footer&gt;...&lt;/footer&gt; &lt;div modal&gt;...&lt;/div&gt; &lt;script&gt;
... &lt;/script&gt;
```

Nav links: Capabilities (#capabilities), Product (#product), How it works (#how), Access (#access), FAQ (#faq). Logo: SVG mark — a small rounded square with 3 waveform lines / a pulse line. Make it: `&lt;span class="logo-mark"&gt;` a 28px div with a blue-cyan gradient border, inside an SVG polyline pulse. Wordmark: "BlueMetric" in Space Grotesk semibold; maybe style "Metric" differently? "Blue" cyan + "Metric" white? Nice.

Wait — section ids: user wanted features section; let's call nav "Features" → id #features. Use Features, Product, How it works, Access, FAQ.

Let me write the copy fully, then code.

Hero status phrases (typing):

- "booting blueMetric.core v4.2 …"
- "ingesting 4.8B events/day across 1,204 services"
- "baseline drift: checkout p95 +38ms — predicted 41m before detection"
- "forecast: signups +6.2% over next 72h (conf 0.97)"
  Prefix with a mono prompt: `$ ` or `▍`. Use "▍" blink block.

Waitlist: "2,341 teams queued" label + avatar stack (4 overlapping gradient circles with initials + 1 "+2,337").

Now dashboard KPI sparkline: small CSS bars or inline SVG polyline. Let's do inline SVG sparkline paths.

Chart canvas in dashboard: draw series actual (cyan solid), forecast (blue dashed), confidence band (translucent), anomaly marker with label. Animate progress. Add a faint vertical "now" line with "NOW" label.

Table rows:

- checkout · p95 latency · +38ms · [watching] (cyan chip)
- search-api · error rate · −0.02% · [clear]
- ingest-gw · rps · +12.1% · [predicted]
- auth · token rev. · +4.8% · [runbook sent]

Forecast queue items:

- amber: "checkout latency spike — 41m"
- cyan: "cache hit-rate decay — 2.5h"
- dim: "queue depth climb — 6h"

OK, time to write. Be mindful of total size, but richness is requested. Let's go.

Key implementation notes to keep code correct:

- Tailwind CDN: `&lt;script src="https://cdn.tailwindcss.com"&gt;&lt;/script&gt;` then a config script. Use arbitrary values in classes where needed like `bg-[rgba(255,255,255,.04)]`. Also define custom colors in the config: `ink`, `volt`, `cyan` exist; add `volt` and `abyss` palette.

Colors in config:

```js
colors: {
  abyss: {950:'#04060d',900:'#070b16',800:'#0a1122',700:'#0f1830'},
  volt: {500:'#2f6bff',400:'#4d8bff',600:'#2456e6', cyan:'#22d3ee', ice:'#8fd6ff'},
  mist: {500:'#93a1bc',400:'#71809e',300:'#a8b4cc',100:'#e9f0fb'}
}
```

- Custom classes in &lt;style&gt; to use: glass, glass-deep, btn-primary, btn-ghost, chip, section-label, reveal, marquee, noise, grid-bg, glow-orb, pulse-dot, nav-link-active, card-bento, corner (HUD bracket), spark-bar, etc.

Let me define:

```css
.glass {
    background: linear-gradient(
        160deg,
        rgba(255, 255, 255, 0.055),
        rgba(255, 255, 255, 0.02)
    );
    border: 1px solid rgba(148, 170, 214, 0.14);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
}
```

Card hover: `.feature-card{transition:transform .35s ..., box-shadow .35s, border-color .35s} .feature-card:hover{transform:translateY(-6px) scale(1.015);border-color:rgba(34,211,238,.4);box-shadow:0 24px 60px -20px rgba(34,211,238,.25), 0 0 0 1px rgba(34,211,238,.12)}`

Nav: `#site-nav{transition:background .3s, border-color .3s, backdrop-filter .3s} .scrolled{background:rgba(6,9,18,.72);border-color:...;backdrop-filter:blur(14px)}` — apply a border-b class.

Now write it all. Also make sure the headline isn't a centered trio: left-align 7/5 split — good, distinctive (data mesh on the right). Section headers: left-align with a monospace label.

Type scale: h1 clamp(2.6rem, 6vw, 4.6rem) tracking-tight leading-[1.02].

Let me write the complete file, compiling it in my head as I go.

Potential pitfalls:

- FontAwesome CDN link: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css
- Tailwind CDN: https://cdn.tailwindcss.com
- Fonts: https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&family=Space+Grotesk:wght@500;600;700&display=swap

Scroll-spy sections: use [data-spy] on sections; IO callback sets active among nav links matching href.

Modal HTML:

```html
&lt;div id="modal" class="fixed inset-0 z-[100] hidden items-center
justify-center p-4"&gt; &lt;div class="absolute inset-0 bg-black/70
backdrop-blur-sm" data-close&gt;&lt;/div&gt; &lt;div class="glass relative ...
max-w-md w-full"&gt; ... form ... &lt;/div&gt; &lt;/div&gt;
```

Toggle hidden with flex class.

Success: replace inner? Better to have 2 divs inside the modal, toggle.

Queue number: `2300 + Math.floor(Math.random()*300) + sessionBump`.

Also hero counter uses same queue base (2341); increment.

Tilt: `const fine = matchMedia('(pointer:fine)').matches;`

Reduced motion master switch also stops: marquee (CSS), chips float (CSS), orbs drift (CSS), typing (JS), scramble (JS), mesh (JS static), counters (JS instant), tilting (JS), dashboard chart animation (JS instant draw), step auto? Steps are IO-driven, keep — the change is content not motion, though add a smooth transition only if !reduced.

Now let me write the hero canvas sizing: container `relative h-[420px] lg:h-[520px]` with canvas absolute inset-0. HUD corners: 4 spans with borders.

Let me also add a "spec strip" in the hero below the CTAs? Already have the avatar counter. Enough.

Dashboard KPI tiles:

- p95 latency: 212ms, delta "+0.8%" (red? Actually an increase in latency is bad → amber), sparkline svg
- Error rate 0.031% ↓ (green? Use cyan for good),
- Throughput 48.2k rps,
- Model confidence 0.97,
  Small bar sparklines: a row of 8 divs heights? Inline SVG polyline is cleaner. Make a helper that returns a random-ish hardcoded path.

OK, let me write the code — the final one. Let me draft the main JS parts as I write.

One more: "Watch the 90-sec tour" button — on click, smooth scroll to #product and trigger a highlight pulse on the dashboard (add a .flash class with a ring animation). Implement simply: scrollIntoView + add a class that removes after 1.6s.

Also make sure everything works from file:// (CDN needed, ok).

Count-up format: value with decimals param & suffix; e.g., {end:99.2,dec:1,suf:'%'} etc. 4.8 → dec1. 210 → 0. 63 → 0.

Metrics band layout: grid 2x2 / 4 cols, with monospace numerals text-5xl + small-caps labels.

Scramble rotator detail:

```js
function scrambleTo(el, word){
  const chars='!&lt;&gt;-_/[]{}=+*^?#·:~';
  const len=word.length; let frame=0;
  const total = 26; // frames
  cancelAnimationFrame(el._sc);
  const step=()=&gt;{
    frame++;
    const prog=frame/total;
    let out='';
    for(let i=0;i&lt;len;i++){
      out += (i &lt; prog*len) ? word[i] : chars[(Math.random()*chars.length)|0];
    }
    el.textContent=out;
    if(frame&lt;total) el._sc=requestAnimationFrame(step); else el.textContent=word;
  };
  el._sc=requestAnimationFrame(step);
}
```

Rotation: setInterval 3200ms → next word → scramble. Keep width stable: words have different lengths; set min-width? Wrap in an inline-block span; the reflow is jarring. Can pad with spaces? Or make the same-length-ish words: "failure"(7), "outage"(6), "dip"(3), "rollout"(7). Reflow in the headline is acceptable but might cause layout shift… Use fixed-width via ch? Better: choose words of same length: "failure"(7), "outage·"(6)…hmm. Alternative: keep the word span `inline-block` with `min-width: 7ch`? A 3-char word in 7ch width looks sparse. Or rotate only same-length pairs: "failure" / "outages"(7)? outage=6. "failure"/"crashes"(7)/"dropoff"(7)/"backlog"(7)? "See the next failure|crash|dropoff|backlog before your users do." Hmm "crash" is 5. Let me use: ["failure","outage","backlog","degradation"? too long]. Let's pick from a set: failure(7), outage(6), backlog(7), drop-off(8), "downtime"(8) — all plausibly different lengths; mitigate shift by wrapping the word in a span with left-align and letting the rest of the line reflow — the headline line is "See the next failure" / "before your users do." — 2 lines! Line 1: "See the next X" where X changes length → line 1 width changes but the line break position is explicit? If I put &lt;br&gt; after the word, the word is at end of line 1; width changes don't shift anything except the caret end. OK: use &lt;br&gt; to put the word at end of line 1:

```
&lt;h1&gt;See the next &lt;span id="rotator"&gt;failure&lt;/span&gt;&lt;br&gt;before your users do.&lt;/h1&gt;
```

Line 1 right edge moves but visually acceptable. To reduce jitter, pad the rotator with `display:inline-block; min-width: 9ch;`? Hmm 9ch for "degradation"? Ch in display font — "degradation" is 11. Simpler: keep word set with same-ish length: ["failure","outage","backlog","churn·","latency"] — "See the next latency before your users do" reads fine; "churn" is good. Use ["failure","outage","backlog","churn","latency"] (7,6,7,5,7) — small variation, fine.

Terminal B: also include a blinking cursor char.

How-it-works left visual: 4-node vertical rail: each node = dot + label; rail connecting; terminal box at bottom showing 4 lines, active line in cyan + prefix "▸". Progress fill height = ((idx)/3)\*100%.

Let me count sections for nav: Features, Product, How it works, Access, FAQ — 5 links OK on lg.

Footer columns: Product (Capabilities, Console, Changelog, Roadmap), Company (About, Careers, Press), Resources (Docs, API, Status, Security). Social: GitHub, X, LinkedIn, Discord, RSS. Bottom: © 2025 BlueMetric, Inc. · All systems operational (pulsing green dot? Brand cyan) · SOC 2 · GDPR · "Built in 48h"? No.

Also include a mini "back to top" link.

Time to write the final code. Watch length; be efficient but complete. Also ensure no explanation, single code block only.

Let me write the CSS block in full:

```css
:root {
    --blue: #2f6bff;
    --cyan: #22d3ee;
    --ice: #8fd6ff;
    --bg: #04060d;
}
html {
    scroll-behavior: smooth;
}
section[id] {
    scroll-margin-top: 92px;
}
body::before? use a .bg-grid fixed .bg-grid {
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    background-image:
        linear-gradient(rgba(96, 140, 255, 0.045) 1px, transparent 1px),
        linear-gradient(90deg, rgba(96, 140, 255, 0.045) 1px, transparent 1px);
    background-size: 56px 56px;
    -webkit-mask-image: radial-gradient(
        ellipse 90% 70% at 50% 0%,
        #000 30%,
        transparent 75%
    );
    mask-image: ...;
}
```

Content is above: main z-10 relative.

Noise:

```css
.noise {
    position: fixed;
    inset: 0;
    z-index: 70;
    pointer-events: none;
    opacity: 0.05;
    background-image: url("data:image/svg+xml,...");
    background-size: 180px;
}
```

z above content but under modal(100) and nav? Nav is z-50… noise above nav OK (pointer none, subtle). OK z-70, modal 100, progress 80.

Orbs:

```css
.orb {
    position: absolute;
    border-radius: 9999px;
    filter: blur(70px);
    opacity: 0.55;
    pointer-events: none;
}
@keyframes orbDrift {
    0% {
        transform: translate(0, 0) scale(1);
    }
    50% {
        transform: translate(40px, -30px) scale(1.12);
    }
    100% {
        transform: translate(-30px, 24px) scale(0.96);
    }
}
```

Two orbs in hero: blue top-left, cyan bottom-right, animation 16s/20s alternate infinite. Reduced: none.

Chip float:

```css
@keyframes floaty {
    0%,
    100% {
        transform: translateY(0) rotate(var(--r, 0deg));
    }
    50% {
        transform: translateY(-10px) rotate(var(--r, 0deg));
    }
}
.floaty {
    animation: floaty 6s ease-in-out infinite;
}
```

Reveal, marquee, cursor blink:

```css
.cursor {
    display: inline-block;
    width: 8px;
    height: 1.05em;
    background: var(--cyan);
    vertical-align: text-bottom;
    animation: blink 1s steps(1) infinite;
}
@keyframes blink {
    50% {
        opacity: 0;
    }
}
```

Nav link underline:

```css
.nav-link {
    position: relative;
    transition: color 0.25s;
}
.nav-link::after {
    content: "";
    position: absolute;
    left: 0;
    right: 100%;
    bottom: -6px;
    height: 1px;
    background: linear-gradient(90deg, var(--blue), var(--cyan));
    transition: right 0.3s;
}
.nav-link:hover::after,
.nav-link.active::after {
    right: 0;
}
.nav-link.active {
    color: #fff;
}
```

Segmented control:

```css
.seg{position:relative}
.seg-btn{transition:...;z-10}
.seg-btn.active{color:#04121f} // over slide pill
.seg-pill{position:absolute;inset:0 auto 0 0;width:33.333%;background:linear-gradient(...);transition:transform .45s cubic-bezier(.22,1,.36,1);z-index:0}
```

JS sets transform translateX(100%\*idx).

FAQ:

```css
.faq-a{display:grid;grid-template-rows:0fr;transition:grid-template-rows .5s cubic-bezier(.22,1,.36,1)}
.faq-item.open .faq-a{grid-template-rows:1fr}
.faq-a &gt; div{overflow:hidden}
```

Icon rotation: .faq-item.open i{transform:rotate(45deg)} for plus icon → x.

Testimonial postcards:

```css
.postcard{transform:rotate(var(--tilt));transition:transform .45s cubic-bezier(.22,1,.36,1), box-shadow .45s, border-color}
.postcard:hover{transform:rotate(0) translateY(-6px) scale(1.02);...glow}
```

Reduced: no transform? hover transform still OK? prefers-reduced — should minimize; gate hover transforms in media query:

```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.001s !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.001s !important;
        scroll-behavior: auto !important;
    }
    .marquee-track {
        animation: none !important;
    }
    .orb,
    .floaty {
        animation: none !important;
    }
}
```

Note: universal .001s kills all transitions — acceptable for a11y, but does hover state still appear instantly? transition-duration .001 → instantaneous, fine. But counters use JS — handled separately. Reveal: set opacity 1.

Now the JS — let me write it in an organized IIFE with helpers. Draft:

```js
(()=&gt;{
const $=(s,c=document)=&gt;c.querySelector(s), $$=(s,c=document)=&gt;[...c.querySelectorAll(s)];
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
const fine=matchMedia('(pointer: fine)').matches;
const fmt=n=&gt;n.toLocaleString('en-US');

/* 1 scroll: nav bg + progress */
const nav=$('#site-nav'), prog=$('#scroll-prog');
let ticking=false;
function onScroll(){ if(!ticking){requestAnimationFrame(()=&gt;{const y=scrollY; nav.classList.toggle('scrolled',y&gt;8); const dh=document.documentElement.scrollHeight-innerHeight; prog.style.transform=`scaleX(${dh? y/dh:0})`; ticking=false;}); ticking=true;}}
addEventListener('scroll',onScroll,{passive:true}); onScroll();
```

Scroll-spy:

```js
const spySections=$$('[data-spy]');
const links=$$('.nav-link');
const spy=new IntersectionObserver(es=&gt;{es.forEach(e=&gt;{if(e.isIntersecting){links.forEach(l=&gt;l.classList.toggle('active',l.getAttribute('href')==='#'+e.target.id));}})},{rootMargin:'-40% 0px -55% 0px'});
spySections.forEach(s=&gt;spy.observe(s));
```

Mobile menu:

```js
const mmBtn=$('#mm-toggle'), mmPanel=$('#mm-panel');
mmBtn.addEventListener('click',()=&gt;{const open=mmPanel.classList.toggle('open'); mmBtn.setAttribute('aria-expanded',open); mmBtn.querySelector('i').className=open?'fa-solid fa-xmark':'fa-solid fa-bars'; nav.classList.toggle('mm-open',open);});
$$('#mm-panel a').forEach(a=&gt;a.addEventListener('click',()=&gt;{mmBtn.click && (mmPanel.classList.contains('open')&&mmBtn.click());}));
```

Careful: if not open, mmBtn.click() would reopen; guard as written.

Reveal:

```js
const revEls=$$('[data-reveal]');
if(reduced){revEls.forEach(el=&gt;el.classList.add('in'));}
else{const ro=new IntersectionObserver(es=&gt;{es.forEach(e=&gt;{if(e.isIntersecting){e.target.classList.add('in');ro.unobserve(e.target);}})},{threshold:.15,rootMargin:'0px 0px -40px 0px'});revEls.forEach(el=&gt;ro.observe(el));}
```

Stagger via inline `style="--d:.1s"` on data-reveal elements.

Mesh class (hero + feature graph). Implement once:

```js
function mesh(canvas,o={}){
 const {count=64,k=2,drift=.18,pulses=8,speed=1}=o;
 const ctx=canvas.getContext('2d');
 let W,H,dpr,nodes=[],edges=[],puls=[],raf=0,running=false,hidden=false;
 function resize(){dpr=Math.min(devicePixelRatio||1,2);const r=canvas.parentElement.getBoundingClientRect();W=r.width;H=r.height;canvas.width=W*dpr;canvas.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);seed();}
 function seed(){nodes=Array.from({length:count},()=&gt;({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*drift*2,vy:(Math.random()-.5)*drift*2,r:.7+Math.random()*1.6}));
  const seen=new Set();edges=[];
  for(let i=0;i&lt;count;i++){const near=nodes.map((n,j)=&gt;[j,Math.hypot(n.x-nodes[i].x,n.y-nodes[i].y)]).filter(p=&gt;p[1]&gt;1).sort((a,b)=&gt;a[1]-b[1]).slice(0,k+1);
   near.forEach(([j,d])=&gt;{if(d&gt;120)return;const key=Math.min(i,j)+'-'+Math.max(i,j);if(!seen.has(key)){seen.add(key);edges.push([i,j]);}});}
  puls=Array.from({length:pulses},()=&gt;spawnPuls());
  if(reduced)draw();
 }
 function spawnPuls(){const e=edges[(Math.random()*edges.length)|0]||[0,1];return{e,t:Math.random(),v:(.003+Math.random()*.006)*speed};}
 function step(){for(const n of nodes){n.x+=n.vx;n.y+=n.vy;if(n.x&lt;0||n.x&gt;W)n.vx*=-1;if(n.y&lt;0||n.y&gt;H)n.vy*=-1;}}
 function draw(){ctx.clearRect(0,0,W,H);
  ctx.lineWidth=1;
  for(const[a,b]of edges){const A=nodes[a],B=nodes[b];const d=Math.hypot(A.x-B.x,A.y-B.y);ctx.strokeStyle=`rgba(70,130,255,${Math.max(.02,.16-d/500).toFixed(3)})`;ctx.beginPath();ctx.moveTo(A.x,A.y);ctx.lineTo(B.x,B.y);ctx.stroke();}
  for(const n of nodes){ctx.fillStyle='rgba(143,214,255,.9)';ctx.beginPath();ctx.arc(n.x,n.y,n.r,0,7);ctx.fill();}
  ctx.save();ctx.shadowColor='rgba(34,211,238,.9)';ctx.shadowBlur=10;
  for(const p of puls){const A=nodes[p.e[0]],B=nodes[p.e[1]];const x=A.x+(B.x-A.x)*p.t,y=A.y+(B.y-A.y)*p.t;ctx.fillStyle='#22d3ee';ctx.beginPath();ctx.arc(x,y,2.2,0,7);ctx.fill();}
  ctx.restore();
 }
 function loop(){if(running&&!hidden){step();for(const p of puls){p.t+=p.v;if(p.t&gt;1){Object.assign(p,spawnPuls());}}draw();raf=requestAnimationFrame(loop);}}
 return{resize,start(){running=true;cancelAnimationFrame(raf);loop();},stop(){running=false;cancelAnimationFrame(raf);},toggleHidden(h){hidden=h; if(!h&&running&&!raf)loop();}};
}
```

Reduced: seed draws static; skip start().
Visibility: IO on canvas parent → if intersecting start else stop. Also visibilitychange.
Resize: debounce, call resize.

Hero canvas id="hero-mesh". Feature D canvas id="graph-mesh" with fewer count (16, k 2, drift 0.05, pulses 5, static-ish).

Mini chart (feature A):

```js
function miniChart(canvas){const ctx=canvas.getContext('2d');let pts=[];
 function build(){const dpr=...,W,H from parent;pts=Array.from({length:46},(_,i)=&gt;{let v=52 - Math.sin(i*.4)*5 - i*.15; v+= (i%7===0? 3:0); if(i&gt;28&&i&lt;34) v -= (34-i)*4.2; // dip
  return v;});}
 function draw(prog){...map pts to coords: x=i/(n-1)*W, y=H - v (v 0..~70 scale: y = H*0.9 - (v)*H/80?) let's define v in px units directly: base 46px etc. Actually define v in 0..100: y=H - v/100*H*0.7 - H*0.15.
  Draw area: path to bottom with gradient fill rgba(34,211,238,.12)
  Draw line up to prog*len points; segment in anomaly region colored red? Use cyan line, highlight anomaly points with blue glow + a dot + small label "−38% · predicted".}
 Animate prog 0→1 over 1300ms easeOutCubic on reveal; reduced → draw(1).
}
```

Dip = a metric dropping (e.g., conversion). Label: "conv −38% · called 41m ahead". Color: line #22d3ee; anomaly dot #f0b429? Small amber OK? Palette is blue/cyan focused — use blue #4d8bff for anomaly ring + ice for label. Keep in-family.

Dashboard chart:

```js
function dashChart(canvas){...
 generate actual: 40 pts rising with noise; forecast: continues 12 pts, diverging + band ± widens.
 draw(prog): actual solid cyan w/2, glow; forecast dashed blue; band fill blue .08; "NOW" vertical line at join.
 Animate 1400ms on reveal.
}
```

Counters:

```js
function counters(){$$('[data-count]').forEach(el=&gt;{const end=parseFloat(el.dataset.count),dec=+(el.dataset.dec||0),suf=el.dataset.suf||'';const run=()=&gt;{if(reduced){el.textContent=end.toFixed(dec)+suf;return;}const t0=performance.now(),dur=1500;const tick=t=&gt;{const p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3);el.textContent=(end*e).toFixed(dec)+suf;if(p&lt;1)requestAnimationFrame(tick);};requestAnimationFrame(tick);};new IntersectionObserver((es,o)=&gt;{es.forEach(en=&gt;{if(en.isIntersecting){run();o.disconnect();}})},{threshold:.4}).observe(el);});}
```

Typing line:

```js
const phrases=[...];const tl=$('#type-line');
if(reduced){tl.textContent=phrases[0];}
else{(function type(){let pi=0,ci=0,del=false;const cur=phrases[pi];
 function f(){ if(!del){ci++; tl.textContent=cur.slice(0,ci); if(ci===cur.length){del=true;setTimeout(f,1800);return;}}
  else{ci-=3; if(ci&lt;=0){ci=0;del=false;pi=(pi+1)%phrases.length;} tl.textContent=phrases[pi].slice(0,ci); }
  setTimeout(f, del?18: 34+Math.random()*40);} f();})();}
```

Rotator with scramble as planned; reduced → static.

Waitlist:

```js
let queue=2341;const ql=$('#queue-count');
const paintQ=()=&gt;{ql.textContent=fmt(queue);ql.parentElement.classList.remove('pop');void ql.offsetWidth;ql.parentElement.classList.add('pop');};
setInterval(()=&gt;{queue+=1+((Math.random()*2)|0);paintQ();}, 7000+Math.random()*5000);
```

Pop: keyframe scale 1.15 color cyan, quick.

Step sync:

```js
const steps=$$('.step');
const nodes=$$('.pipe-node');const lines=$$('.pipe-line');const rows=$$('.pipe-row');const fill=$('#pipe-fill');
function setStep(i){nodes.forEach((n,j)=&gt;n.classList.toggle('on',j&lt;=i));rows.forEach((r,j)=&gt;r.classList.toggle('on',j===i));fill.style.height=((i+1)/steps.length*100)+'%';}
const so=new IntersectionObserver(es=&gt;{es.forEach(e=&gt;{if(e.isIntersecting)setStep(steps.indexOf(e.target));})},{rootMargin:'-45% 0px -45%'});
steps.forEach(s=&gt;so.observe(s));setStep(0);
```

Tilt:

```js
const tiltEl=$('#dash-window');
if(fine&&!reduced){const wrap=$('#dash-wrap');wrap.addEventListener('pointermove',e=&gt;{const r=wrap.getBoundingClientRect();const x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;tiltEl.style.transform=`perspective(1200px) rotateX(${(-y*4).toFixed(2)}deg) rotateY(${(x*5).toFixed(2)}deg)`;});wrap.addEventListener('pointerleave',()=&gt;{tiltEl.style.transform='perspective(1200px)';});}
```

Tiers:

```js
const tiers={pilot:{...},scale:{...},ent:{...}};
$$('.seg-btn').forEach(b=&gt;b.addEventListener('click',()=&gt;{setTier(b.dataset.tier);$$('.seg-btn').forEach(x=&gt;x.classList.toggle('active',x===b));$('.seg-pill').style.transform=`translateX(${['pilot','scale','ent'].indexOf(b.dataset.tier)*100}%)`;});
function setTier(k){const t=tiers[k];...update #tier-name,#tier-price,#tier-desc, render perks list items (li with check icon); retrigger fade class.}
```

Form:

```js
function wireForm(formEl,{after}){formEl.addEventListener('submit',e=&gt;{e.preventDefault();const btn=$('button',formEl);btn.disabled=true;btn.classList.add('loading');setTimeout(()=&gt;{btn.classList.remove('loading');after&&after();},900);});}
```

Success: swap panels: form card: hide form, show #form-success, fill #queue-num with (2400+ (Math.random()\*240|0)) and tier. Sparks:

```js
function sparks(host){if(reduced)return;for(let i=0;i&lt;14;i++){const s=document.createElement('span');s.className='spark';s.style.setProperty('--a',(i/14*360)+'deg');s.style.setProperty('--d',(160+Math.random()*120)+'px');s.style.background=Math.random()&gt;.5?'#22d3ee':'#2f6bff';host.appendChild(s);s.animate([{transform:`translate(0,0) rotate(var(--a))`,opacity:1},{transform:`translate(0,-100%)`...}]}
```

Hmm spark physics: place at button center; animate translate along angle: use CSS: .spark{position:absolute;width:6px;height:6px;border-radius:50%;left:50%;top:50%;} with JS computing dx=Math.cos(a)*d, dy=Math.sin(a)*d; animate transform translate(dx,dy) scale(0). Fine.

Modal:

```js
const modal=$('#access-modal');
function openModal(tierKey){if(tierKey)setTier(tierKey,{quiet:true})? Modal has its own? Simpler: modal form just has email + tier text filled from current. Set #modal-tier text. modal.classList.remove('hidden');modal.classList.add('flex');document.body.style.overflow='hidden';setTimeout(()=&gt;$('#modal-email').focus(),50);lastFocus=document.activeElement;}
function closeModal(){modal.classList.add('hidden');modal.classList.remove('flex');document.body.style.overflow='';lastFocus?.focus();}
$$('[data-open-modal]').forEach(b=&gt;b.addEventListener('click',e=&gt;{e.preventDefault();openModal(b.dataset.tier);}));
$$('[data-close-modal]').forEach(b=&gt;b.addEventListener('click',closeModal));
addEventListener('keydown',e=&gt;{if(e.key==='Escape'&&!modal.classList.contains('hidden'))closeModal();});
```

Modal content: mini brand header, "You're in." no — open state = form; after submit success view inside modal (reuse success markup via class toggles). Give modal its own success div.

Both forms (access section + modal): on success update that respective success block.

FAQ:

```js
$$('.faq-item').forEach(item=&gt;{const btn=$('.faq-q',item);btn.addEventListener('click',()=&gt;{const open=item.classList.contains('open');$$('.faq-item.open').forEach(o=&gt;{o.classList.remove('open');$('.faq-q',o).setAttribute('aria-expanded','false');});if(!open){item.classList.add('open');btn.setAttribute('aria-expanded','true');}});});
```

Tour button:

```js
$('#tour-btn').addEventListener('click',()=&gt;{$('#product').scrollIntoView({behavior:reduced?'auto':'smooth'});const w=$('#dash-window');w.classList.add('flash');setTimeout(()=&gt;w.classList.remove('flash'),1800);});
```

.flash {animation: flashRing 1.8s} keyframes of box-shadow pulse cyan.

Terminal B (feature card): ids tb-q, tb-a1, tb-a2; type loop as planned. Reduced: set text.

Also pause heavy loops when tab hidden:

```js
document.addEventListener('visibilitychange',()=&gt;{if(document.hidden){heroMesh.stop();graphMesh.stop();}else{ioVisible&&heroMesh.start();...}})
```

Simplify: use IO flag stored per mesh.

Now the copy for the tier data:

```js
const tiers = {
    pilot: {
        name: "Pilot",
        tag: "for a single product",
        price: "$0",
        note: "during the entire beta",
        perks: [
            "1 product / 3 team seats",
            "7-day history & live views",
            "Email + digest findings",
            "Community support",
        ],
        foot: "Full price after beta: $120/mo",
    },
    scale: {
        name: "Scale",
        tag: "for platform teams",
        price: "$0",
        note: "during the entire beta",
        perks: [
            "5 products / 25 seats",
            "90-day history + API access",
            "Slack, PagerDuty & GitHub sync",
            "Priority model fine-tunes",
        ],
        foot: "Full price after beta: $490/mo",
    },
    ent: {
        name: "Enterprise",
        tag: "for critical systems",
        price: "Custom",
        note: "we will be in touch",
        perks: [
            "Unlimited products & seats",
            "Private VPC or on-prem",
            "SSO/SAML, audit log, DPA",
            "Dedicated engineer + SLA",
        ],
        foot: "Custom contracts, no surprise uplift",
    },
};
```

Panel: big name + tag; price left; list; foot small monospace.

Access section left heading: "Pick your lane. Pay nothing." description: "The beta is free for every tier. When it ends, your lane locks in at the founding price — forever." Right form card as described.

FAQ answers as drafted.

Testimonial data inline in HTML.

Hero right chips content as set earlier.

Marquee logos: 8 names styled in different display treatments: VANTIQ (bold), "nordbank" (lowercase italic?), HELIOS Robotics, "kite labs", ARCLIGHT, "paddle&co", "meridian", "FLUXO". Keep font-display, opacity .45, hover 1.

Ticker items:
"P95 LATENCY 312ms ▲0.4%" "EVENTS/DAY 4.8B ▲2.1%" "PREDICTION ACCURACY 99.2% ▲0.3%" "FALSE ALARMS −63% ▼" "MTTR 11m 40s ▼42%" "UPTIME 99.999%" "ACTIVE MODELS 1,204"
Separators: " ✦ " or a middle dot with a cyan diamond. Use span.tsep "·"

Now — section label component: `&lt;div class="sec-label"&gt;&lt;span class="sec-no"&gt;01&lt;/span&gt;&lt;span&gt;CAPABILITIES&lt;/span&gt;&lt;span class="sec-rule"&gt;&lt;/span&gt;&lt;/div&gt;` monospace, cyan no, letter-spaced.

Heading sizes: h2: text-3xl md:text-5xl font-display font-semibold tracking-tight.

OK, feature bento grid code:

```html
&lt;section id="features" data-spy class="relative py-24 md:py-32"&gt; &lt;div
class="max-w-7xl mx-auto px-5 md:px-8"&gt; &lt;div class="flex items-end
justify-between gap-6 mb-12 md:mb-16 flex-wrap" data-reveal&gt; &lt;div
class="max-w-xl"&gt; &lt;div class="sec-label ..."&gt;01 /
CAPABILITIES&lt;/div&gt; &lt;h2&gt;Four instruments. &lt;br class="hidden
md:block"&gt; One calm picture.&lt;/h2&gt; &lt;p class="mt-4 text-mist-500
..."&gt;Built like lab equipment...&lt;/p&gt; &lt;/div&gt; &lt;a class="hidden
md:inline-flex ...mono small" href="#access"&gt;or just get the keys &lt;i
class="fa-arrow-right"&gt;&lt;/i&gt;&lt;/a&gt; &lt;/div&gt; &lt;div class="grid
grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-5"&gt; A: md:col-span-2
lg:col-span-7 B: lg:col-span-5 C: lg:col-span-5 D: md:col-span-2 lg:col-span-7
&lt;/div&gt; &lt;/div&gt; &lt;/section&gt;
```

Card structure:

```html
&lt;article class="feature-card glass rounded-2xl p-6 md:p-8 relative
overflow-hidden group" data-reveal style="--d:.05s"&gt; &lt;div
class="icon-tile"&gt;...&lt;/div&gt; &lt;h3 class="font-display text-xl ..."&gt;
&lt;p class="text-sm text-mist-500 ..."&gt; &lt;div class="visual ..."&gt;
&lt;/article&gt;
```

(Use rounded-xl/2xl — glassmorphism was requested.)

Icon tile: `w-11 h-11 rounded-lg bg-[linear-gradient(135deg,rgba(47,107,255,.25),rgba(34,211,238,.25))] border border-white/10 flex items-center justify-center text-volt-ice` with i.

Now let me think about "How it works" left rail visual markup:

```html
&lt;div class="glass rounded-2xl p-6"&gt; &lt;div class="flex gap-5"&gt; &lt;div
class="relative w-1 flex-none"&gt; &lt;div class="w-px h-full
bg-white/10"&gt;&lt;/div&gt; &lt;div id="pipe-fill" class="absolute top-0 left-0
w-px bg-gradient-to-b from-blue to-cyan" style="height:25%"&gt;&lt;/div&gt;
nodes absolute at 0,33.3,66.6,100%... &lt;/div&gt; node labels... &lt;/div&gt;
&lt;div terminal rows&gt; &lt;/div&gt;
```

Simpler: a vertical list of 4 "pipe-step" items: dot + label + sub; plus a connecting line via border-l. Each `.pipe-node` = li with a dot. Fill bar as an absolute behind. Then a terminal box of 4 mono lines below.

Row content (mono, text-[11px]):

1. `ingest   kafka.blue.v1  →  1.2M evt/s`
2. `stream   window=60s  key=service  · 42µs/evt`
3. `predict  core v4.2  ·  conf 0.97`
4. `act      slack #scale  ·  runbook #R-118`
   Active: text-cyan + "▸" prefix; else dim.

Right steps: each `.step` block:

```html
&lt;div class="step relative py-10 md:py-14 border-t border-white/5"
data-reveal&gt; &lt;span class="step-no"&gt;01&lt;/span&gt; &lt;h3 ...&gt; &lt;p
...&gt; &lt;/div&gt;
```

step-no: monospace text-5xl/6xl font-display, color transparent with -webkit-text-stroke? Use a huge dim mono number absolute to left? Simpler: a row: monospace cyan "01" + content.

Metrics band: wrap with a gradient hairline top/bottom: `border-y border-white/8 bg-[radial-gradient(...)]`.

Testimonial section: heading "Heard on the other side of the pager." 3 postcards.

Access: id access.

FAQ: 2 col: left sticky-ish heading + "Still curious? hi@bluemetric.io" link; right accordion.

Footer: 4-col grid.

Also "flash" keyframe:

```css
@keyframes flashRing {
    0%,
    100% {
        box-shadow: 0 0 0 0 rgba(34, 211, 238, 0);
    }
    40% {
        box-shadow:
            0 0 0 10px rgba(34, 211, 238, 0.18),
            0 0 60px rgba(34, 211, 238, 0.35);
    }
}
.flash {
    animation: flashRing 1.8s ease;
}
```

Success check styling.

Now — let me write it all out. Also don't forget: hero CTA "Get Early Access" opens the modal (data-open-modal). Primary button in access section is "Reserve my spot →" which triggers the form in place. Both fine.

Let me double-check the required items: sticky nav ✓ smooth anchors ✓ highlighted CTA ✓; hero headline/sub/dual CTA ✓ + animated network ✓; features 4 cards grid ✓; footer with copyright + social ✓; fade/slide on load ✓ (reveal + hero load anim: add .in on load after DOMContentLoaded + small delay); hover scale + glow ✓; continuous background anim in hero (mesh canvas + typing + orbs) ✓; responsive ✓.

Hero load anim: hero elements get data-reveal with --d stagger; IO fires immediately since they're in viewport → nice.

Edge: Tailwind CDN generates classes from DOM at runtime — including classes added via JS? The CDN Play watches the DOM (MutationObserver) and generates on the fly — yes, it does. Good, JS-added classes (like the active class) are pre-declared in CSS anyway.

Let me finalize the copy details and write the file. Aim for clean, consistent code.

Font note: Space Grotesk is fine for display, no italics. Use uppercase mono for labels.

Let me write out the final HTML, carefully, in full.

Also the title/meta description.

One more consideration — file size: big but fine.

Let me finalize chart drawing functions concretely.

miniChart (card A — "conversions" dip):

```js
function miniChart(cv){
 const ctx=cv.getContext('2d');let W,H,dpr,pts,raf;
 const N=48;
 function gen(){pts=Array.from({length:N},(_,i)=&gt;{
   let v=64 - i*0.35 + Math.sin(i*0.55)*5 + Math.sin(i*0.21)*3;
   if(i&gt;=30&&i&lt;=36)v-=Math.sin((i-30)/6*Math.PI)*26; // smooth dip
   return v;});}
 function resize(){dpr=Math.min(devicePixelRatio||1,2);const r=cv.parentElement.getBoundingClientRect();W=r.width;H=r.height;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);gen();paint(1);}
 function y(v){return H*0.92 - (v/100)*H*0.72;}
 function x(i){return (i/(N-1))*(W-24)+12;}
 function paint(p){
  ctx.clearRect(0,0,W,H);
  const upto=Math.max(2,Math.floor(N*p));
  // area
  const grad=ctx.createLinearGradient(0,0,0,H);grad.addColorStop(0,'rgba(34,211,238,.18)');grad.addColorStop(1,'rgba(34,211,238,0)');
  ctx.beginPath();ctx.moveTo(x(0),H);
  for(let i=0;i&lt;upto;i++)ctx.lineTo(x(i),y(pts[i]));
  ctx.lineTo(x(upto-1),H);ctx.closePath();ctx.fillStyle=grad;ctx.fill();
  // line
  ctx.beginPath();
  for(let i=0;i&lt;upto;i++){i?ctx.lineTo(x(i),y(pts[i])):ctx.moveTo(x(i),y(pts[i]));}
  ctx.strokeStyle='#39c6ff';ctx.lineWidth=1.8;ctx.stroke();
  // anomaly marker
  if(p&gt;=1){
    let mi=30,iv=1e9;for(let i=30;i&lt;=36;i++)if(pts[i]&lt;iv){iv=pts[i];mi=i;}
    ctx.save();ctx.shadowColor='#2f6bff';ctx.shadowBlur=12;
    ctx.fillStyle='#4d8bff';ctx.beginPath();ctx.arc(x(mi),y(iv),3.4,0,7);ctx.fill();ctx.restore();
    ctx.fillStyle='rgba(143,214,255,.9)';ctx.font='10px "JetBrains Mono"';
    ctx.fillText('−38% · called 41m ahead', x(mi)-8, y(iv)-12);
  }
 }
 ... rAF animate over 1300ms easeOut on reveal
}
```

Dip value 26 → ~"−38%"? whatever, label is fixed.

Dash chart:

```js
function dashChart(cv){
 similar; actual 42 pts: v=50+sin(i*.3)*6+i*.2+noise; forecast 14 pts continues with upward drift + band.
 draw: band: path along forecast+off, back along −off; off=3+i*0.9 (i in forecast idx)
 dashed: ctx.setLineDash([4,4]); strokeStyle 'rgba(77,139,255,.9)'
 vertical now line at join x + label 'NOW'
}
```

Animate prog on reveal; static on reduced.

Noise: use deterministic pseudo-noise: Math.sin(i*12.9898)*43758.5453 %1 pattern — or Math.random once in gen is fine (regenerates on resize, that's fine).

Graph mesh on card D: count 16, drift .04, k 2, pulses 5, edge dist 140.

Hero mesh: count based on width? Fixed 70; on mobile smaller area — canvas parent h 420 — 70 nodes OK, might scale count by area: count = Math.min(90, Math.max(36, (W*H)/9000)) computed on seed. Let me parameterize in seed: `const n = Math.round(Math.min(85, Math.max(34, (W*H)/9000)));` for hero; for the graph mesh just use a given fixed count.

Add an `auto` flag.

OK, writing the final answer now. No explanation — output just the code block.

Also make sure id uniqueness and script correctness. Let me carefully write out the whole file mentally in order:

HEAD: meta, title, description, favicon (inline SVG data URI — a small pulse square; nice touch: `&lt;link rel="icon" href="data:image/svg+xml,..."&gt;` a blue gradient square with a cyan line) — keep simple: a blue square with "B"? use a pulse SVG.

FA icon check (6.x names): fa-wave-square ✓, fa-terminal ✓, fa-cube ✓, fa-diagram-project ✓, fa-satellite-dish ✓, fa-gauge-high ✓, fa-bolt ✓, fa-magnifying-glass-chart ✓, fa-arrow-right, fa-play, fa-bars, fa-xmark, fa-check, fa-plus, fa-quote-left, fa-github (brands), fa-x-twitter (brands), fa-linkedin-in, fa-discord, fa-shield-halved, fa-server, fa-table-cells-large, fa-chart-line, fa-tower-broadcast, fa-plug, fa-brain, fa-bell, fa-magnifying-glass, fa-rotate-left, fa-ellipsis. Fine.

Nav CTA button: gradient + hover scale/glow, small arrow icon.

Hero HTML:

```html
&lt;section id="top" class="relative min-h-screen flex items-center
overflow-hidden pt-28 pb-16 md:pt-0"&gt; orbs x2, canvas? no — canvas on the
right. &lt;div class="max-w-7xl mx-auto px-5 md:px-8 w-full relative z-10"&gt;
&lt;div class="grid lg:grid-cols-12 gap-10 lg:gap-8 items-center"&gt; &lt;div
class="lg:col-span-6 xl:col-span-6"&gt; &lt;p class="font-mono text-[13px]
text-volt-cyan flex items-center gap-2" data-reveal&gt; &lt;span
class="pulse-dot"&gt;&lt;/span&gt;&lt;span
id="type-line"&gt;&lt;/span&gt;&lt;span class="cursor"&gt;&lt;/span&gt;
&lt;/p&gt; &lt;h1 class="mt-6 font-display text-[2.6rem] leading-[1.04]
sm:text-5xl md:text-6xl xl:text-[4.2rem] tracking-tight text-mist-100"
data-reveal style="--d:.08s"&gt; See the next &lt;span id="rotator"
class="text-volt-ice relative"&gt;failure&lt;/span&gt;&lt;br&gt;before your
users do. &lt;/h1&gt; &lt;p class="mt-6 text-mist-500 text-base md:text-lg
max-w-lg leading-relaxed" data-reveal style="--d:.16s"&gt;sub...&lt;/p&gt;
&lt;div class="mt-9 flex flex-wrap items-center gap-4" data-reveal
style="--d:.24s"&gt; &lt;button class="btn-primary" data-open-modal&gt;Get Early
Access &lt;i class="fa-solid fa-arrow-right"&gt;&lt;/i&gt;&lt;/button&gt;
&lt;button class="btn-ghost" id="tour-btn"&gt;&lt;i class="fa-solid
fa-play"&gt;&lt;/i&gt; Watch the 90-sec tour&lt;/button&gt; &lt;/div&gt; &lt;div
class="mt-10 flex items-center gap-4" data-reveal style="--d:.32s"&gt; avatars,
counter &lt;/div&gt; &lt;/div&gt; &lt;div class="lg:col-span-6 relative"
data-reveal style="--d:.2s"&gt; &lt;div class="mesh-frame glass rounded-2xl
relative h-[380px] sm:h-[440px] lg:h-[540px]"&gt; &lt;canvas id="hero-mesh"
class="absolute inset-0 w-full h-full"&gt;&lt;/canvas&gt; corners x4 chips x3
bottom caption bar &lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;/div&gt;
&lt;/section&gt;
```

rotator color: text-volt-ice with a subtle glow text-shadow? "text-transparent bg-clip-text"? Avoid gradient-filled heading — user asked for gradient brand; the word is… use solid ice with a cyan glow shadow. OK.

Avatar stack: 5 circles: 4 initials (ME, DO, JP, +) with different gradient hues in the blue family + last one "+2.3k"? Counter is separate: "2,341 teams in the beta queue" with the number as #queue-count in cyan. Avatars: ring-2 ring-ink-900 -ml-3.

The pulse-dot: small cyan dot with a ping animation:

```css
.pulse-dot {
    position: relative;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #22d3ee;
}
.pulse-dot::after {
    content: "";
    position: absolute;
    inset: -4px;
    border-radius: 50%;
    border: 1px solid rgba(34, 211, 238, 0.6);
    animation: ping 1.8s cubic-bezier(0, 0, 0.2, 1) infinite;
}
@keyframes ping {
    0% {
        transform: scale(0.6);
        opacity: 1;
    }
    100% {
        transform: scale(1.8);
        opacity: 0;
    }
}
```

Mesh frame corners:

```html
&lt;span class="hud-corner top-0 left-0"&gt;&lt;/span&gt; etc
.hud-corner{position:absolute;width:18px;height:18px;border-color:rgba(143,214,255,.5)}
.hud-tl{border-left:1.5px solid;border-top:1.5px solid} ...
```

Define via 4 classes.

Chips:

```html
&lt;div class="chip glass floaty"
style="--d:0s;--r:-2deg;left:6%;top:12%"&gt;&lt;div class="chip-dot
bg-amber?"&gt;&lt;/div&gt;...
```

Wait, colors: keep amber for anomaly chip? "anomaly" is conceptually amber/red. A small amber dot adds realism and breaks mono-cyan monotony — acceptable as a data accent. Use #fbbf24 for anomaly chip only.

Chip content:

1. (top-left): `▲ anomaly · p95 +38ms` / `routed → #scale · 14:02`
2. (right-mid): `forecast · signups +6.2% / 7d` with a 5-bar mini spark (CSS bars)
3. (bottom-left): `model confidence &lt;span&gt;0.97&lt;/span&gt;` with a thin progress bar
   Hide 3 on small: maybe `hidden sm:block` for chip 2/3; keep 1 on mobile.

Bottom caption bar: absolute bottom-0 inset-x-0 border-t border-white/10 px-4 py-2.5 flex justify-between mono text-[11px] text-mist-400: "blueMetric.core — live mesh · 128 nodes" + "1.2M evt/s" right with a dot.

Then the logo + ticker band:

```html
&lt;div class="relative border-y border-white/8 bg-white/[.015] py-6
overflow-hidden"&gt; &lt;div class="flex items-center"&gt; &lt;div
class="shrink-0 pl-6 pr-8 ..."&gt;&lt;span class="font-mono text-[11px]
tracking-[.2em] text-mist-400"&gt;TRUSTED IN PREVIEW BY&lt;/span&gt;&lt;/div&gt;
&lt;div class="marquee flex-1 overflow-hidden mask-fade"&gt; &lt;div
class="marquee-track"&gt; [logos x2] &lt;/div&gt; &lt;/div&gt; &lt;/div&gt;
&lt;div class="mt-4 ticker overflow-hidden border-t border-white/5 pt-4"&gt;
&lt;div class="marquee-track marquee-rev"&gt; items x2 &lt;/div&gt; &lt;/div&gt;
&lt;/div&gt;
```

mask-fade: mask-image linear-gradient(90deg, transparent, black 8%, black 92%, transparent).
Logos: `&lt;span class="logo-item font-display text-lg tracking-wide"&gt;VANTIQ&lt;/span&gt;` etc., separated by diamond dot.

Then sections. Let me just write.

Dashboard KPI tiles:

```html
&lt;div class="kpi glass rounded-xl p-4"&gt; &lt;div class="font-mono
text-[10px] tracking-widest text-mist-400"&gt;P95 LATENCY&lt;/div&gt; &lt;div
class="mt-1 flex items-end justify-between"&gt; &lt;span class="font-display
text-2xl text-mist-100"&gt;212&lt;small&gt;ms&lt;/small&gt;&lt;/span&gt;
&lt;span class="delta up"&gt;▲ 2.1%&lt;/span&gt; &lt;/div&gt; &lt;svg
class="spark w-full h-8 mt-2" viewBox="0 0 100 30"
preserveAspectRatio="none"&gt;&lt;path d="M0 22 L10 20 ..." stroke="#22d3ee"
fill="none" stroke-width="1.5" opacity=".8"/&gt;&lt;/svg&gt; &lt;/div&gt;
```

Delta classes: .delta{font-mono text-[10px] px-1.5 py-0.5 rounded} .delta.bad{color:#fca5a5?} use amber for latency rise: #fbbf24; good cyan; keep .delta.warn{color:#fcd34d}.bad{color:#fb7185}.good{color:#34d399}? green — palette drift; use cyan for good, amber for warn, rose for bad (small accent OK).

Sidebar: hidden md:flex flex-col w-44 border-r border-white/8 p-3 gap-1: item mono text-[11px] py-1.5 px-2 rounded hover:bg-white/5; active: bg-[rgba(47,107,255,.15)] text-mist-100 with a left bar.

Chart card header: "checkout — actual vs forecast" + legend dots.

Signal table: mono text-[11px] grid rows of 4: [service, metric, delta, chip].

Forecast queue: 3 rows of dot + text + time.

Window: rounded-2xl glass-deep (stronger blur, border, big shadow) overflow-hidden. Title bar: dots + tab "overview · blueMetric console".

Also add a scan line: `.scanline{position:absolute;top:0;bottom:0;width:60px;background:linear-gradient(90deg,transparent,rgba(34,211,238,.05),transparent);animation:scan 7s linear infinite}` keyframes left -10% → 105%. Reduced: none. Inside the chart card area. Subtle.

Access section layout:

```html
&lt;section id="access" data-spy class="py-24 md:py-32 relative"&gt; &lt;div
class="max-w-7xl mx-auto px-5 md:px-8"&gt; &lt;div class="grid lg:grid-cols-2
gap-12 items-start"&gt; &lt;div data-reveal&gt; sec-label 04/EARLY ACCESS h2
"Pick your lane.&lt;br&gt;Pay nothing." p desc segmented control + panel (tier
card glass) &lt;/div&gt; &lt;div data-reveal style="--d:.15s"
class="access-form-card glass rounded-2xl p-8 relative overflow-hidden"&gt; orb
h3 "Reserve your spot" p small form: email input + button success div hidden:
check circle, "You're in — position #&lt;span id=queue-num&gt;" note small note:
"No credit card · one email to start · your seat locks at $0 when beta closes"
&lt;/div&gt; &lt;/div&gt; &lt;/div&gt; &lt;/section&gt;
```

FAQ section:

```html
&lt;section id="faq" data-spy class="py-24 md:py-32"&gt; grid lg:grid-cols-12
left col-span-4: label 05/FAQ, h2 "Questions,&lt;br&gt;answered straight.", p +
contact link mono right col-span-8: items &lt;/section&gt;
```

Footer:

```html
&lt;footer class="relative border-t border-white/8 bg-[#03050a]"&gt; &lt;div
class="max-w-7xl mx-auto px-5 md:px-8 py-14"&gt; &lt;div class="grid gap-10
md:grid-cols-12"&gt; brand col md:col-span-5: logo, tagline, socials 3 link cols
each md:col-span-2/... (5+2+2+3?) use 5/2/2/3 &lt;/div&gt; &lt;div class="mt-12
pt-6 border-t border-white/8 flex flex-col md:flex-row gap-4 items-center
justify-between"&gt; &lt;span class="mono text-xs text-mist-400"&gt;© 2025
BlueMetric, Inc. All metrics reserved.&lt;/span&gt; &lt;span class="mono text-xs
flex items-center gap-2 text-mist-400"&gt;&lt;span
class="pulse-dot"&gt;&lt;/span&gt; All systems predicting&lt;/span&gt; &lt;div
class="flex gap-2"&gt;badges SOC 2 / GDPR / 99.99% SLA&lt;/div&gt; &lt;/div&gt;
&lt;/div&gt; &lt;/footer&gt;
```

Modal markup:

```html
&lt;div id="access-modal" class="fixed inset-0 z-[100] hidden items-center
justify-center p-4" role="dialog" aria-modal="true"
aria-labelledby="modal-title"&gt; &lt;div class="absolute inset-0
bg-[#02030a]/80 backdrop-blur-sm" data-close-modal&gt;&lt;/div&gt; &lt;div
class="relative glass-deep rounded-2xl w-full max-w-md p-8 modal-card"&gt;
&lt;button close top-right X logo mini &lt;h3 id="modal-title"
class="font-display text-2xl mt-4"&gt;Get early access&lt;/h3&gt; &lt;p
class="text-sm text-mist-500 mt-2"&gt;One email. No card. Lane: &lt;span
id="modal-tier" class="text-volt-ice font-mono"&gt;Pilot&lt;/span&gt;&lt;/p&gt;
&lt;form id="modal-form" class="mt-6 space-y-3"&gt; &lt;input type="email"
required placeholder="you@company.com" class="input" id="modal-email"&gt;
&lt;button class="btn-primary w-full justify-center loading hidden?"&gt;Reserve
my spot&lt;/button&gt; &lt;/form&gt; &lt;div id="modal-success" class="hidden
text-center py-4"&gt; check icon circle gradient &lt;p class="font-display
text-xl"&gt;You're in.&lt;/p&gt; &lt;p class="mono text-sm text-mist-400
mt-2"&gt;Queue position &lt;span id="modal-q"
class="text-volt-ice"&gt;#2,418&lt;/span&gt;&lt;/p&gt; &lt;button
data-close-modal class="btn-ghost mt-6"&gt;Done&lt;/button&gt; &lt;/div&gt;
&lt;p class="text-[11px] font-mono text-mist-400/70 mt-4"&gt;beta seats lock at
$0 · we reply within the hour&lt;/p&gt; &lt;/div&gt; &lt;/div&gt;
```

Success also used in the access section form.

Modal open: also animate the card (scale/translate in) via CSS class: .modal-card{transform:translateY(12px) scale(.97);opacity:0;transition:.35s} .modal-in .modal-card{...} — add a 'show' class on the modal when opened.

Button loading: .loading{pointer-events:none;opacity:.7} .loading i? Swap text? Keep it simple: add spinner: `&lt;span class="spinner hidden"&gt;` CSS border spinner; on loading: spinner block, label opacity. Implementation: button contains `&lt;span class="btn-label"&gt;Reserve my spot &lt;i arrow&gt;&lt;/i&gt;&lt;/span&gt;&lt;span class="btn-spin hidden"&gt;&lt;i class="fa-solid fa-circle-notch fa-spin"&gt;&lt;/i&gt;&lt;/span&gt;`, toggle.

OK. Now the full JS. Also guard existence of everything.

One subtlety: Tailwind CDN classes used only inside JS-added DOM (sparks) — sparks are plain CSS, fine.

Also `#type-line` initial content: set in JS; if JS fails empty — put the first phrase directly in HTML and let JS retype from empty? For reduced, keep static. In JS set textContent='' at start then type.

OK — also add hero bottom fade to blend into next section: gradient overlay at hero bottom.

Also ensure `overflow-x-hidden` on body and that marquee doesn't cause horizontal scroll (the max-width track inside an overflow hidden container is fine).

Let me write the final. Be careful with quotes/escaping inside JS template strings (avoid backtick issues — fine inside HTML).

Also: `fa-x-twitter` exists in 6.4+. Use 6.5.2.

Now let me write everything out, compiling in my head as I go. Let's go.

The copy in the hero sub should feel specific, e.g.: "BlueMetric ingests your full event stream, learns a statistical twin of every service, and calls behavior changes minutes to hours before they surface — so your team ships with a crystal-ball, not a crystal-clear postmortem." Nice.

Heading alt: "See the next &lt;rotator&gt; before your users do." OK.

Section header wording:

- 01 CAPABILITIES — "Four instruments. One calm picture." Sub: "Not another dashboard graveyard. BlueMetric ships as a single pane of predictive glass — detection, forecast, cause, and action, fused."
- 02 THE CONSOLE — "The console, minus the noise." Sub: "Everything below is rendered live from the beta. No screenshots were harmed — this is the actual surface."
- 03 HOW IT WORKS — "Raw bytes in. 'Ah, that's why' out."
- (Metrics band no label? A small label "LIVE FROM BETA"? Add a label row)
- 04 EARLY ACCESS
- 05 FAQ

Testimonial section: 06? Let me keep it: order: features(01), console(02), how(03), [metrics band no label / "PROOF"], voices, access(04), faq(05). Label "04 · VOICES"? Renumber: 01 capabilities, 02 console, 03 pipeline, 04 voices (skip label? give "04 · VOICES"), 05 early access, 06 FAQ. OK, 6 labels.

Metrics band: no number, just a center label? Use "03.5"? no. Use a label "BETA TELEMETRY" for the metrics band. Fine — a monospace top label "◆ BETA TELEMETRY — MEASURED, NOT PROMISED".

Step right side needs enough scroll: py-14 + content each step, OK.

Let me now write the code in final. Watch length; be efficient but complete.

Also `#top` used by logo link.

Recheck mesh canvas inside rounded-2xl overflow-hidden → corners are crisp. Canvas class w-full h-full absolute — parent has explicit height, good. Mesh resize uses parent rect; but canvas is inset-0 → same rect.

ResizeObserver? Use window resize (debounced 150ms) → call each registered resizer (heroMesh.resize, graphMesh.resize, miniChart.resize, dashChart.resize). Simpler than RO; fine.

Reduced + canvas: draw static after each resize.

Also mesh step bounces: clamp if |v| tiny… OK.

Dash chart "now line" is at join index idx=J (e.g., 34 of 56 total: actual 0..33, forecast 34..47, band same).

Generate:

```js
const N=48, J=32;
actual: for i&lt;J: v=48 + Math.sin(i*.32)*7 + i*.35 + (rand*4-2)
forecast: for i=0..N-J-1: t=J+i: v= last + i*.9 + Math.sin(t*.3)*3 + rand*2
band off = 2 + (i)*.55
```

Paint with prog: draw actual up to floor(N*p) (may include forecast after J). Band always only when p&gt;=J/N*1.05; simpler: bandAlpha = clamp((p- (J/N))\*10) etc. Simple: if p &gt; J/N draw band full.

Label: "NOW" at x(J).

Colors: actual #22d3ee, forecast rgba(77,139,255,.85), band rgba(47,107,255,.09).

Good. Also grid lines: faint horizontal lines 4 lines.

Feature B terminal:

```html
&lt;div class="term glass rounded-lg ..."&gt; &lt;div class="term-bar"&gt;dots +
"nlq — natural language query"&lt;/div&gt; &lt;div class="p-4 font-mono
text-[12px] leading-relaxed min-h-[118px]"&gt; &lt;p
class="text-mist-400"&gt;&lt;span class="text-volt-cyan"&gt;ask ›&lt;/span&gt;
&lt;span id="tb-q"&gt;&lt;/span&gt;&lt;/p&gt; &lt;p class="text-mist-100 mt-3"
id="tb-a1"&gt;&lt;/p&gt; &lt;p class="text-volt-ice mt-1"
id="tb-a2"&gt;&lt;/p&gt; &lt;/div&gt; &lt;/div&gt;
```

JS type loop.

Code snippet (card C):

```
$ npx bluemetric init --source kafka
✓ connected  · topic  events.raw
✓ twin       · 128 services modeled
✓ live       · first prediction in 38s
```

Static with a final line + a blinking cursor; maybe an animation to reveal lines one by one on reveal (each line gets .in). Add a data-reveal-line: on card reveal, stagger add class via JS.

OK. Also "learn more" pseudo-link in cards? Skip to reduce noise; the visual + icon is enough.

Ensure IDs: hero-mesh, type-line, rotator, queue-count, tour-btn, dash-chart, dash-window, dash-wrap, graph-mesh, mini-chart, tb-q, tb-a1, tb-a2, pipe-fill, site-nav, scroll-prog, mm-toggle, mm-panel, access-modal, modal-email, modal-form, modal-success, modal-tier, modal-q, access-form, access-email, access-success, access-q, seg-pill, tier-name, tier-tag, tier-price, tier-perks, tier-foot, faq list items.

Data attributes: data-open-modal (buttons: nav CTA, hero CTA, maybe footer link), data-close-modal, data-reveal, data-spy, data-count, data-tier.

Class .step on 4 step wrappers; .pipe-node 4; .pipe-row 4.

Final check on the "no row of 3/4 identical cards" — bento is different (varying spans, different visuals) ✓. No gradient text headings ✓ (solid + solid ice rotator). Fonts ✓. Glass used (requested) but not sitewide — used on nav/cards ✓. Rounded: cards use rounded-xl/2xl — user asked for glass cards; keep 2xl but vary: dashboard 2xl, cards maybe rounded-xl. Fine.

Let me write the final code block. Careful with correctness:

- tailwind config script must come after the CDN script tag.
- custom colors I reference: text-mist-100, text-mist-500, text-mist-400, bg-ink-950, border-white/8 (arbitrary alpha via slash works in CDN? The opacity modifier on a named color white/8 → white is default palette ✓). Use /[0.02] arbitrary for rgba custom backgrounds.
- `font-display` etc from config.
- Avoid classes that need a plugin.

Also define in config: boxShadow? Instead use custom CSS.

Also `rounded-2xl` used for a few key cards — the user asked for glass cards; keep 2xl on dashboard & frame, xl on feature cards, mix OK.

Let me write. (Also add `overflow-x:clip` on html.)

For scroll-spy sections: hero id top (not in nav), features, product, how, access, faq → all data-spy + scroll-margin.

Active nav link is default: none/Features.

OK, writing the final output now. Ensure no stray backtick issues. Use standard quotes in JS.

Also don't forget the requirement "smooth fade-in / slide-up animations on elements as the page loads" — covered by reveals + hero --d stagger.

Also a subtle detail: selection styling, scrollbar:

```css
::selection {
    background: rgba(47, 107, 255, 0.35);
    color: #fff;
}
::-webkit-scrollbar {
    width: 10px;
}
::-webkit-scrollbar-thumb {
    background: #1a2540;
    border-radius: 8px;
}
::-webkit-scrollbar-track {
    background: #04060d;
}
```

Let me write the file.
