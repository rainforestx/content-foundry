# PLATFORM-OPTIONS - where the directory property's articles live and publish

Status: analysis complete, awaiting operator ruling. Nothing publishes until the
decision card at the end is approved. Prepared 2026-08-06. Every capability,
pricing and policy claim below comes from a live lookup made on that date, cited
inline as [n] against the sources list. Items a lookup could not settle are
marked VERIFY-AT-DECISION, not guessed.

## 1. Framing

The decision: a publication surface for the directory property's articles. Four
accepted articles exist as fully self-contained HTML documents (~40 KB each,
inline CSS on the ratified token set, inline SVG figures, FAQPage JSON-LD in
the document as authored, zero external assets) in
`/workspace/content-foundry/articles/`. More arrive on the pipeline; an
autonomy trial is running. The artefact is a finished document - the platform's
only job is to serve those bytes unmodified under an owned domain.

This is NOT the EarX Stage-2 store platform decision (WiziShop / Selldone /
Shopify - a separate, later comparison per the commercial roadmap). The two are
kept distinct throughout; section 6 notes where this choice touches that one.

Binding constraints from the operator's architecture and roadmap docs:

- ~3 hours/week across the whole portfolio - operational overhead is a
  first-class criterion, and the agent pipeline must be able to publish
  programmatically with the operator only accepting.
- BrandJet owns the email channel; any capture wires to BrandJet, no new email
  tool. UK GDPR/PECR applies.
- GEO stack invariant: Topical Map (plan) -> Blazly (produce/publish) -> Visby
  (track). Blazly must be triaged as a candidate before anything is bought.
- Check owned LTDs before recommending any purchase; LTDs never load-bearing
  except behind swappable adapters.
- The pipeline's dynamic tone-adaptation loop is designed but dormant until the
  property emits reader signals (VOICE.md: "the operator is the only sensor"
  until then) - a platform with real analytics unblocks a designed capability.

## 2. Owned-tool triage (done first, per the invariant)

- **Blazly (owned, T4).** Its publishing model is generation inside Blazly then
  push to an external CMS - "publish or schedule directly to WordPress or
  Webflow" [3]. No hosted-pages-under-custom-domain capability appears in the
  vendor listing; blazly.ai itself refused automated fetch (403), so an
  in-account check is VERIFY-AT-DECISION. Even if a hosted surface exists, it
  is built to publish Blazly-generated content, not to ship foreign 40 KB
  standalone HTML documents byte-faithful. Verdict: not a host. Crucially,
  using it here would DISTORT the GEO invariant, not honour it - forcing these
  articles through Blazly means adopting WordPress or Webflow purely to give
  Blazly a publish target. Blazly's produce/publish lane and Visby's tracking
  of the property's domain are unaffected by hosting elsewhere.
- **Brilliant Directories (owned, activated - the confirmed directory
  platform).** BD supports a "Custom Widget as Web Page" page type that
  "excludes Brilliant Directories code and styling completely", can save .html
  file extensions, and allows per-page custom head tags [4]. BD also has a
  REST API (X-Api-Key) covering widgets, pages, forms, menus and redirects
  [5]. This makes BD the one serious owned candidate - evaluated in section 5.
- **Shareables (owned, T5).** Publishes spreadsheet/Teable DATA as sites -
  wrong artefact class (structured rows, not authored HTML documents). Not
  triaged live; excluded on class grounds. VERIFY only if the recommendation
  is rejected.
- **Site-builder LTDs in the dump** (WebWave x20, Brizy x10, Divhunt x10,
  Webstudio, Sitejet/Lindo, Phonesites, Pagemaker, FlexiFunnels): all visual
  builders that rebuild pages in their own runtime and templates. Shipping a
  complete standalone document with its own head is not their model, and none
  offers a git/API deploy path the agent pipeline could drive. Not triaged
  live individually; excluded on class grounds, same VERIFY caveat.
- **"2MakeU hosting"** appears in the dump's long tail with no capability
  notes; not worth a triage slot against a free first-party option.

Conclusion of triage: nothing owned needs to be displaced, and only BD earns a
full evaluation. No purchase is recommended anywhere below; the recommended
platform is free.

## 3. Candidate table

Scores: good / partial / poor, each with its evidence.

| Criterion | Cloudflare Pages | Brilliant Directories | GitHub Pages | Vercel / Netlify free | Blazly | WordPress |
|---|---|---|---|---|---|---|
| HTML fidelity | Good - serves the repo's bytes as-is; static assets, no rewriting [1] | Partial - "excludes BD code completely" page type exists, but content passes through the admin widget editor; byte-survival unproven [4] | Good - static bytes as-is [6] | Good - static bytes as-is [7][8] | Poor - publishes into WP/Webflow, not a byte-faithful host [3] | Poor - full document needs theme bypass via custom PHP templates or plugins [9] |
| SEO/GEO mechanics | Good - custom domains (100/project free), we author sitemap/canonicals in-repo, CDN speed [1] | Good - it IS the property's domain; platform handles sitemap; page-speed on BD stack unverified [4] | Partial - custom domain yes, soft 100 GB/month bandwidth [6] | Good mechanically [7][8] | n/a | Partial - plugin-dependent |
| Email capture to BrandJet | Good - static form + Pages Function (Workers free tier, 100k req/day) forwarding to BrandJet, whose current listing includes webhooks and API access [2][10] | Partial - BD forms + API exist [5]; BD-to-BrandJet bridge untested | Poor - no server side; third-party form endpoint needed [6] | Good (Functions) but moot - see next row | n/a | Good via plugins, at maintenance cost |
| Reader signals | Good - Cloudflare Web Analytics: free, cookieless, no consent banner needed under GDPR/PECR (privacy policy still required) [11] | Partial - GA integration; GA4 needs consent tooling under PECR | Partial - bring your own | Partial - paid or bring your own | n/a | Partial - plugins |
| Overhead at 3 hrs/week | Good - git push publishes; per-branch preview URLs are the operator acceptance gate; merge = live; wrangler direct upload as the non-git path [12] | Poor - admin-UI paste per article, or unproven API scripting; every publish costs operator or fragile-automation minutes [4][5] | Good - git push | Good - git push | n/a | Poor - hosting, updates, security patching |
| Cost vs owned | £0 on free tier; no bandwidth cap on any Pages tier [1] | £0 marginal (owned, activated) | £0 | Vercel Hobby bars commercial use incl. lead-gen pages -> Pro $20/mo [7]; Netlify free pauses the site when 300 credits (~15 GB) run out [8] | £0 but unusable | ~£5-15/mo hosting + time |
| EarX store tie-in | Good - platform-neutral static pages under an owned domain link anywhere; zero coupling to the Stage-2 choice | Partial - couples article URLs to BD's future on the property | Good | Good | n/a | Partial |
| Terms fit | Good - commercial use allowed on free tier [1] | Good | Poor - ToS bars sites primarily directed at facilitating commercial transactions; a lead-capturing commercial property is grey at best [6] | Poor (Vercel) / Poor (Netlify pause risk) [7][8] | n/a | Good |

## 4. Cloudflare Pages (recommended)

Free tier: 500 builds/month, 20,000 files/site, 25 MiB max per file, 100 custom
domains per project, and no hard bandwidth cap on any tier [1]. Our whole
four-article corpus is ~164 KB; headroom is effectively infinite.

Fidelity: static hosting - the deployed directory tree is served as authored.
JSON-LD stays exactly where the producer put it; the gates keep binding on the
same bytes the reader receives. Sitemap.xml, robots.txt and canonical tags are
authored artefacts in the repo, which means they fall under the existing gate
battery instead of a CMS's opinions - a mechanised-governance fit no CMS
offers.

Publish flow that matches the pilot's acceptance discipline: the pipeline
commits an article to a publishing branch; Pages builds a per-branch preview at
a stable alias URL; the operator reviews the RENDERED page (the operator's
existing review medium) and merging to production is the acceptance act
[12]. Deploys are also drivable headless via `wrangler pages deploy` with
auto-deploy off, if the git integration is not wanted [12]. Operator cost per
article: open preview link, approve merge - minutes.

Email capture: a plain HTML form in the article footer POSTs to a Pages
Function (runs on the Workers free plan, 100,000 requests/day shared quota
[10]) which forwards the address to BrandJet. BrandJet's current vendor
material lists "webhooks and API access included" [2] - but the internal
inventory recorded "no public API (CSV in)", so the exact intake mechanism is
VERIFY-AT-DECISION in-account. Fallback that still honours "no new email
tool": the Function appends to a store the operator batch-imports to BrandJet
as CSV. Consent checkbox + UK GDPR/PECR copy on the form; unsubscribe lives in
BrandJet sends per the roadmap.

Reader signals: Cloudflare Web Analytics is free on all plans, cookieless, uses
no persistent or immutable identifiers, and generally needs no consent banner
under GDPR (privacy policy still required) [11]. That gives page views,
referrers and Core Web Vitals per URL from day one - enough to switch VOICE.md's
tone-adaptation loop from "operator is the only sensor" to signal-driven. Known
limit: deliberately stateless, so no funnels or visitor journeys [11]; if the
loop later needs scroll/dwell depth, a self-hosted beacon on the same Function
quota is the upgrade path - a later decision, not this one.

GEO invariant: preserved, not bypassed. Topical Map can still plan subjects,
Visby tracks the domain regardless of host, and Blazly keeps its produce/publish
lane for content Blazly generates. Nothing here displaces a committed tool.

Requirement this creates: the property needs a domain on a Cloudflare DNS zone.
No doc read for this analysis names the property's domain - naming or buying
one (~£10/year at-cost if new) is part of the decision card. VERIFY-AT-DECISION:
whether a domain is already held for the property.

## 5. Brilliant Directories (runner-up)

The case for: BD is the confirmed, activated directory platform in the
portfolio, and the articles belong to the directory property - publishing them
on the property's own BD instance consolidates all authority on one domain from
day one. The mechanics exist: "Custom Widget as Web Page" excludes BD code and
styling completely, .html extensions can be created in the webpage builder, and
per-page custom head tags are supported [4]; a REST API covers widgets and
pages [5].

The case against, today: the directory build has not started, so there is no
live BD instance or domain to publish onto; per-article publishing is an
admin-UI paste (or API scripting against an editor pipeline whose byte-survival
for a 40 KB standalone document - style block, inline SVG, JSON-LD - is
unproven); and every article ties its URL to BD's future on the property.
VERIFY-AT-DECISION if this route is ever taken: paste one article through
Custom-Widget-as-Web-Page and diff served bytes against authored bytes.

The reconciliation: these are not exclusive. Cloudflare fronting the property's
DNS can serve the article corpus from Pages while BD serves the directory root
on the same domain later (Pages on a subdomain such as guides.<domain>, or
mounted on a path via a Worker route). Articles link into the directory and
back the moment it exists. Choosing Pages now neither delays nor prejudges the
BD build.

## 6. Rejected candidates - evidence

- **GitHub Pages:** ToS states Pages is "not intended for or allowed to be
  used as a free web-hosting service to run your online business... or any
  other website primarily directed at facilitating commercial transactions"
  [6]. A lead-capturing property feeding a retail business is at best grey;
  plus soft 100 GB/month bandwidth and no server-side path for the capture
  form [6]. Do not build a commercial asset on a hosting grace.
- **Vercel free (Hobby):** non-commercial use only, and their definition
  explicitly captures lead-generation landing pages and any deployment made
  for financial gain [7]. Our capture form makes the property commercial on
  their terms; compliant use costs Pro at $20/month against Cloudflare's £0.
- **Netlify free:** 300 credits/month (~15 GB bandwidth at 20 credits/GB,
  production deploys 15 credits each) and the site is PAUSED when credits run
  out [8]. A public property that can go dark on a traffic spike is
  disqualified.
- **WordPress (any conventional CMS):** shipping a standalone full-document
  page requires bypassing the theme via custom PHP page templates or
  theme-switching plugins; WordPress "doesn't recognize standalone HTML files
  as part of its content structure" [9]. Add hosting cost and a
  patch/update/security burden with no owner but the operator's 3 hours/week.
  Every property of our artefact class fights the platform's model.
- **Blazly as host / other owned builders:** section 2.

## 7. EarX Stage-2 note (not this decision)

Nothing above commits the store. Static articles under an owned domain can link
to eBay listings today and swap those links to the Stage-2 store (whichever of
WiziShop / Selldone / Shopify / other wins that comparison) by editing authored
HTML the pipeline already governs. Had we chosen a CMS or BD-coupled route, the
store comparison would inherit a constraint; this route hands it none. The one
positive coupling: the capture form starts filling the BrandJet list before the
store exists, which is the standing email workstream's whole point.

## 8. Recommendation

**Publish on Cloudflare Pages under an owned property domain, git-integrated
with per-branch preview deployments as the operator's acceptance gate; enable
Cloudflare Web Analytics at launch; add the form -> Pages Function -> BrandJet
capture as a follow-on approval once the BrandJet intake mechanism is verified
in-account.**

Runner-up: Brilliant Directories via Custom-Widget-as-Web-Page on the
property's BD instance.

Flip trigger: if the BD directory build starts AND the byte-fidelity test in
section 5 passes AND the operator rules that single-domain-single-platform
outweighs the per-article publish overhead, move the corpus to BD - the
articles are self-contained files, so migration is copy-paste by construction.
Short of all three, Pages stands; even after a BD launch, the
subdomain/path-mount coexistence in section 5 is the default.

## 9. Decision card

**The operator is asked to approve:**

1. Cloudflare Pages (free tier) as the publication platform for the directory
   property's articles.
2. The domain: name an existing held domain for the property, or approve
   registering one (~£10/year). VERIFY-AT-DECISION: current domain holdings.
3. The publish flow: pipeline commits to a publishing branch; operator accepts
   on the rendered preview URL; merge to production is the publish act.

**On approval:** Cloudflare account + Pages project created (£0); DNS zone
configured; articles repo connected with auto-deploy limited to the production
branch; Web Analytics enabled; sitemap/robots/canonical authoring added to the
pipeline's gate battery; the four accepted articles staged to a preview URL
for the operator's first acceptance pass. The BrandJet capture form ships only
after a second, separate approval covering the verified intake mechanism and
the GDPR/PECR consent copy.

**Defer-default:** if this card is not approved, nothing publishes anywhere.
The articles remain in the repo; no account is created, no domain bought, no
byte leaves the repo.

## Sources

1. Cloudflare Pages limits and pricing - developers.cloudflare.com/pages/platform/limits and devtoolreviews.com/reviews/cloudflare-pages-pricing-bandwidth-limits-2026 (free: 500 builds/mo, 20k files, 25 MiB/file, 100 custom domains/project, no hard bandwidth cap on any tier).
2. BrandJet features - appsumo.com/products/brandjet and brandjet.ai/features via search index ("syncs with HubSpot, Attio, Slack... webhooks and API access included"); direct fetch of brandjet.ai returned 403, so scope is in-account VERIFY-AT-DECISION.
3. Blazly publishing model - appsumo.com/products/blazly and blazly.ai via search index ("publish or schedule directly to WordPress or Webflow"); direct fetch returned 403; no hosted-pages capability found in any listing.
4. Brilliant Directories custom pages - support.brilliantdirectories.com "How to Create a New Static Page", "Create .HTML... File Extensions Using Webpage Builder", and Custom Widget as Web Page ("excludes Brilliant Directories code and styling completely"; per-page custom head tags).
5. Brilliant Directories API - support.brilliantdirectories.com "API Overview" and "API Endpoints Technical Reference" (X-Api-Key; widgets, pages, forms, menus, redirects CRUD).
6. GitHub Pages limits and ToS - docs.github.com/pages/getting-started-with-github-pages/github-pages-limits and docs.github.com/site-policy/github-terms/github-terms-for-additional-products-and-features (1 GB site, soft 100 GB/mo, commercial-use prohibition).
7. Vercel Hobby restrictions - vercel.com/docs/plans/hobby and vercel.com/docs/limits/fair-use-guidelines (non-commercial only; lead-gen pages named as commercial).
8. Netlify free plan - netlify.com/blog/introducing-netlify-free-plan and netli.fyi/blog/netlify-pricing-and-limits (300 credits/mo, 20 credits/GB bandwidth, site pauses at exhaustion).
9. WordPress standalone HTML - whitelabelcoders.com/blog/can-i-upload-my-own-html-to-wordpress and thirdbear.substack.com/p/disabling-your-active-wordpress-theme (theme bypass via custom templates/plugins; standalone HTML not part of the content model).
10. Pages Functions pricing - developers.cloudflare.com/pages/functions/pricing (Functions requests count against Workers free plan, 100,000 requests/day).
11. Cloudflare Web Analytics privacy - ctrl.blog/entry/review-cloudflare-analytics.html and ethicaldatahub.com/cloudflare-analytics-cookie-banner (free on all plans, no cookies/localStorage/fingerprinting; generally no consent banner; deliberately stateless, no funnels).
12. Cloudflare Pages git integration and previews - developers.cloudflare.com/pages/configuration/git-integration and /pages/configuration/preview-deployments (per-branch alias preview URLs; wrangler direct upload with auto-deploy disabled).
