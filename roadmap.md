# AURA — lanserings- og markedsstrategi / launch & marketing strategy

**Arbeidsdokument / Working draft · 14 November 2026**

Dette er en foreslått strategi basert på grunnleggerens produktvisjon. Repoet var tomt ved oppstart. Ingen appkode, integrasjoner, sikkerhetsmekanismer eller utgivelser er verifisert i dette repoet. Beskrivelsene nedenfor er mål og releasekrav, ikke bekreftede funksjoner. Datoer settes først når kvalitetstersklene er bestått.

This is a proposed strategy based on the founder's product vision. The repository was empty at the start. No application code, integrations, security mechanisms or releases have been verified here. Descriptions below are goals and release gates, not confirmed features. Dates follow evidence of readiness.

## Norsk

### 1. Posisjon og merkevare

**Kjerne:** AURA gir deg et personlig hjem for underholdningen din, med lokal kontroll og valgfri tilkobling mellom enhetene. AuraOS er en selvstendig Android TV-launcher; AuraAmp og AuraBox er selvstendige apper for telefon og nettbrett. AURA skal ikke markedsføres som en medieserver, en abonnementstjeneste for innhold eller en kilde til gratis filmer og musikk.

**Merkevareløfte:** «Din verden. I dine hender.» / «Your world. In your hands.» Den emosjonelle signaturen er «Din egen film- og TV-maestro. Din DJ i mørket.» Bruk den som personlighet, mens produkttekst forklarer konkret hva appene gjør.

**Tre budskap:**

1. Et roligere utgangspunkt for TV, musikk og medier.
2. Lokale AURA-kontoer som utgangspunkt; koble til og synkroniser når du velger det.
3. Tydelig innsyn i hva som fungerer nå, hva som kommer og hvilke tjenester som mottar data.

Visuelt uttrykk: nesten svart, varm rav, dempede naturtoner, store typografiske flater, diskret bevegelse og god kontrast. Unngå generiske cyber-sikkerhetsløfter, overdreven glød og falske partnerlogoer. Bruk stabil skrivemåte: **AURA**, **AuraOS**, **AuraAmp**, **AuraBox**, **AuraConnect**, **Aura Guardian**. Grunnleggerens «Aura» er assistent-/vaktpersonligheten; Guardian er beskrivende sikkerhetsnavn i kommunikasjonen, ikke et ekstra produktløfte.

### 2. Produktarkitektur og status

| Del | Tiltenkt rolle | Status som kan kommuniseres nå | Krav før sterkere påstander |
| --- | --- | --- | --- |
| AuraOS | Selvstendig Android TV-launcher for fjernkontroll, apper og personlig startskjerm | Under utvikling; appimplementasjon ikke verifisert her | Installasjon, launcher-valg, navigasjon, tilgjengelighet og gjenoppretting testet på oppgitt enhetsmatrise |
| AuraAmp | Selvstendig musikkapp på telefon/nettbrett | Planlagt produktretning | Verifiserte plattformer, avspilling, innlogging til kilder og stabile kontroller |
| AuraBox | Selvstendig medieapp på telefon/nettbrett | Planlagt produktretning | Definert funksjonsgrense mot AuraAmp; støttede kilder, formater og enheter dokumentert |
| AuraConnect | Valgfri kryptert synk mellom brukerens enheter | Planlagt; arkitektur og krypteringsmodell ikke verifisert | Paring, nøkkelhåndtering, trusselmodell, tilbakekalling, konflikter, sletting og gjenoppretting testet |
| Aura Guardian | Lokal sikkerhetsvakt som undersøker tilgjengelige tegn på angrep og endring av kode | Planlagt; plattformbegrensninger må kartlegges | Dokumenterte signaler/rettigheter, tester av integritet, falske alarmer og tydelig forklaring av begrensninger |
| Aura-personalisering | Frivillig læring fra lokale preferanser for anbefalinger | Planlagt, med lokal behandling som mål | Separat opt-in, sletting/nullstilling, eksport, ressursbruk og nettverkstester |

Deezer, medieservere og Ultramax er **ønskede tilkoblinger**, ikke bekreftede partnerskap eller støttede integrasjoner. Lag en kompatibilitetsmatrise per app: API-tilgang, rettigheter, abonnement, region, autentisering, lisensvilkår, rategrenser og teststatus. Ikke anta samme støtte i alle tre apper. Avklar nøyaktig hvilken Ultramax-tjeneste/API som menes før offentlig integrasjonsløfte. Ikke publiser leverandørlogoer uten avklart bruksrett.

### 3. Personvern og sikkerhet som kan forklares ærlig

Målbildet er lokale AURA-kontoer og lokal lagring av profiler og preferanser. Lokal konto betyr ikke automatisk at all bruk er frakoblet eller anonym. Deezer og andre tilkoblede tjenester kan kreve egne kontoer og motta IP-adresse, søk, innholds-ID-er, tilgangstokener og bruksrelaterte forespørsler. Brukeren må få en konkret oversikt ved hver tilkobling. Medieservere kan være lokale eller eksterne.

AuraConnect skal være frivillig, med valg av data/enheter og manuell eller automatisk synk. «Kryptert» må beskrives presist: transportkryptering og ende-til-ende-kryptering er ulike løfter. Ikke hev ende-til-ende-kryptering før protokoll, nøkkelansvar og tester støtter dette. Avklar eventuell relay, oppdagelsestjeneste, metadata, driftslogger, backup og gjenoppretting. Synk flytter data mellom valgte enheter og eventuelle dokumenterte mellomledd; dette må fremgå i stedet for «data forlater aldri enheten».

Personalisering skal være av som standard inntil et eget samtykke er gitt. Brukeren skal kunne se læringsgrunnlaget, pause, slette og nullstille det uten å miste tilgang til appen. Lokal modellbehandling er et mål som må verifiseres ved inspeksjon av lagring og nettverk. Anbefalinger kan kreve tredjepartsmetadata uten at den lokale profilen skal sendes; dokumenter skillet.

Aura Guardian kan kun observere det operativsystemet og appens tillatelser tillater. Den er ikke en garanti mot kompromittert OS, skadevare eller alle kodeendringer, og skal ikke markedsføres som fullverdig antivirus eller uavhengig sikkerhetssertifisering. Definer hva varsler betyr, hvordan de håndteres og hvordan feilvarsler rapporteres.

Før ekstern beta: datakart per komponent, trusselmodell, nøkkellivssyklus, minst mulig rettigheter, signerte bygg og sikker oppdatering, redigering av logger, kontroll av avhengigheter, sletting/eksport og en test av nettverkstrafikk. Etabler privat sikkerhetsrapportering og publiser kun en kontakt som faktisk er operativ. Ingen hemmeligheter eller personlige logger i offentlige issues. Juridisk gjennomgang av personverntekst og leverandørvilkår er en lanseringsoppgave, ikke en påstått godkjenning.

**Tillatt nå:** «Utviklet med lokal kontroll som prinsipp», «valgfri synk er planlagt», «personalisering på enheten er målet». **Krever bevis:** «ingen data sendes ut», «100 % privat», «helt sikker», «oppdager alle angrep», «fungerer med alle tjenester».

### 4. Målgrupper og introduksjonsrekkefølge

Start med et avgrenset problem: Android TV-brukere som vil ha en personlig, ryddig startskjerm og forutsigbar fjernkontrollnavigasjon. Neste gruppe er musikk- og medieentusiaster som allerede har egne tjenester eller medieservere. Personverninteresserte er en naturlig gruppe, men tillit skal bygges gjennom dokumentasjon og kontroll, ikke absolutte slagord.

Anbefalt rekkefølge er AuraOS som første demonstrerbare inngang, deretter AuraAmp/AuraBox når hver app har en selvstendig verdi. AuraConnect og Guardian demonstreres som frivillige tillegg når kvalitet og begrensninger er klare. Bekreft rekkefølgen mot faktisk appstatus før en kampanje. Ikke gjør lanseringen av én app avhengig av uferdige løfter fra hele økosystemet.

### 5. Milepæler og beslutningsporter

Ingen kalenderdato er en offentlig forpliktelse. Hver fase får en navngitt ansvarlig når teamet er avklart; grunnleggeren eier godkjenning av budskap og release.

| Fase | Leveranser | Utgangskriterium |
| --- | --- | --- |
| M0: Fundament — nå | Landingsside, denne strategien, funksjonsregister, datakart, valgt første app | Alle påstander merket verifisert/under utvikling/planlagt; ingen døde CTA-er eller falske nedlastinger |
| M1: Intern alfa | Installerbart signert bygg, testplan, faktisk enhetsmatrise, skjermopptak fra app | Førstegangsbruk, fjernkontroll og gjenoppretting fungerer på testmatrisen; kjente feil oppført |
| M2: Lukket beta | Foreslått 15–30 testere, onboarding, changelog, feilmaling, personvernkontroller | Ingen åpne kritiske sikkerhets-/datatapfeil; foreslått mål: minst 90 % fullfører kjerneoppgave uten hjelp over to testomganger |
| M3: Offentlig beta | Verifisert distribusjonskanal, støtteliste, release notes, supportløp, oppdaterings-/rollback-plan | Foreslått mål: minst 99 % krasjfrie økter i en definert to ukers periode, med oppgitt utvalg og frivillig innsamling; kvalitative tester hvis datagrunnlaget er for lite |
| M4: Stabil lansering | Reell nedlastingsside, brukerveiledning, personvernside, rettigheter/lisenser og pressepakke | Akseptert feilbudsjett, testet oppdatering og gjenoppretting, kapasitet til å håndtere support |
| M5: Utvidelse | Nye app-/integrasjonsbetaer, frivillig synk og personalisering | Hver funksjon passerer egne personvern-, sikkerhets- og kompatibilitetsporter |

Tallene er forslag til styringsmål, ikke målte resultater. Avklar målemetode før betastart. Ikke legg inn skjult telemetri for å måle suksess.

### 6. Kanaler og innhold

- **GitHub:** første sannhetskilde for roadmap, versjoner og kjente begrensninger. Opprett passende issue-maler og aktiver Discussions først når modereringskapasitet finnes. Nettstedet lenker allerede til repoet; ingen annen kanal presenteres som opprettet.
- **Android TV-/launcher- og selvhostingmiljøer:** vurder relevante Reddit-fora og utviklerfora. Les gjeldende selvpromoteringsregler før posting. Be om tilbakemelding på ett konkret problem, vis en ekte demo, oppgi at du er utvikleren.
- **Video:** korte klipp med fjernkontrollflyt og skjermopptak fra virkelige bygg. Merk konseptvideoer eksplisitt. Før/etter skal vise samme maskinvare og faktisk atferd.
- **Norske teknologimiljøer:** lokal utviklingshistorie, kontroll og åpen fremdrift. Internasjonalt: engelsk produktforklaring og dokumenterte kompatibilitetsgrenser.
- **Små skapere og fagpresse:** først etter at en testbar beta finnes. Tilby pressekart, ærlige kjente feil og tydelig merking av eventuelle gaver/samarbeid. Ingen påståtte omtaler eller anmeldelser på forhånd.
- **Product Hunt og større lanseringsflater:** vurder etter offentlig beta og fungerende onboarding; ikke bruk én stor lanseringsdag til å kompensere for ustabilitet.

Forslag til rytme: én substansiell utviklingsoppdatering annenhver uke, ett ekte demonstrasjonsklipp ved milepæl og månedlig roadmap-opprydding. Publiser bare når det finnes fremdrift å vise. Før en enkel innholdslogg: målgruppe, budskap, faktisk funksjonsbevis, kanal, ansvarlig og oppfølging. Budsjett i starten: organisk arbeid og testerrekruttering; betalt annonsering først etter dokumentert aktivering og støttbar drift. Ingen bestemt annonsekostnad eller vekst loves.

### 7. Lanseringspakke og måling

Før en kampanje: forklar problemet i én setning, ha en 30–60 sekunders ekte demo, 3–5 skjermbilder med versjonsnummer, støttede enheter, installasjon/avinstallasjon, personvernoversikt, kjente feil, lisens-/innholdsforbehold og en operativ støttekanal. Test alle lenker og byggsignaturer. AURA leverer programvare; brukeren trenger egne innholdsrettigheter og eventuelle abonnementer.

Mål en enkel trakt: besøk → lesing av produkt/status → faktisk beta-/installasjonsvalg når tilgjengelig → fullført kjerneoppgave → frivillig tilbakemelding → fortsatt bruk. Bruk aggregert, minimert og samtykkebasert måling; vær bevisst at også hosting kan logge IP-adresser. Nåværende statiske side har ingen analyseverktøy, piksler, cookies eller skjemaer. Ikke publiser fabrikerte bruker-, venteliste- eller ytelsestall. Følg også kvalitative signaler: hvor brukere stopper, hvilke personvernvalg de misforstår og om supportbelastning øker.

### 8. Nettsideplan

**Første versjon i denne grenen:** responsiv engelsk landingsside uten avhengigheter under `website/`, mørk ravprofil, tydelig produktarkitektur, personvernforbehold og milepæler. TV-/musikkillustrasjonen er en CSS-konseptvisning, ikke et appskjermbilde. GitHub er den eneste eksterne handlingslenken. Ingen backend, innlogging, fungerende nedlastinger eller venteliste er konstruert.

**Neste innholdstrinn:** norsk språkversjon med egne URL-er og korrekt språkmetadata; produktsider med bare verifiserte funksjoner; detaljerte personvern-/sikkerhetssider basert på datakartet; tilgjengelighetsgjennomgang og reelle skjermbilder når de finnes. Legg til versjonsstyrt status per funksjon og kilde til verifikasjon.

**Når utgivelser finnes:** signer og kontroller nedlastinger, vis versjon/plattform/krav, lenk til ekte butikk- eller release-sider. Dersom venteliste senere velges, avklar leverandør, behandlingsgrunnlag, sletting, samtykke og faktisk mottak før skjema aktiveres. Ikke legg inn tomme e-postadresser, oppdiktet domene eller innsamling uten eierskap.

**Publisering:** vurder GitHub Pages fra `website/` via godkjent Actions-oppsett eller annen statisk vert. Denne PR-en deployer ikke automatisk. Velg domene, hosting og loggpolicy før offentlig publisering. Sjekk varemerke-/navnerettigheter før bred kampanje; navn er ikke rettslig klarert av dette dokumentet.

### 9. Viktigste åpne beslutninger

1. Faktisk appstatus og hvilken app som når alfa først.
2. Eksakt støtte per operativsystem, enhet og innholdstjeneste; hva Ultramax betegner.
3. AuraConnect-topologi, nøkkelmodell og eventuell relay/metadata.
4. Guardian-signaler som er teknisk mulige på vanlige, ikke-rootede enheter.
5. Distribusjon, lisens, eventuell prismodell og støttekapasitet.
6. Domene, operative kontaktkanaler, personvernansvar og eierskap til release-godkjenning.

## English

### 1. Positioning and brand

**Core:** AURA is a personal home for entertainment with local control and optional connections between devices. AuraOS is a standalone Android TV launcher. AuraAmp and AuraBox are standalone phone/tablet apps. Do not position AURA as a media server, content subscription service or source of free movies/music.

**Promise:** “Your world. In your hands.” The emotional signature is “Your own film & TV maestro. Your DJ after dark.” Pair expressive language with a concrete account of what each product does.

Lead with three messages: a calmer starting point for entertainment; local-first AURA accounts with connections you choose; transparent feature status and data boundaries. Use near-black, warm amber, restrained natural colors, spacious typography and accessible contrast. Keep names consistent: AURA, AuraOS, AuraAmp, AuraBox, AuraConnect and Aura Guardian. “Aura” is the assistant/guardian personality; Guardian describes its security role.

### 2. Product roles and evidence

| Component | Intended role | Honest current status | Evidence required before stronger claims |
| --- | --- | --- | --- |
| AuraOS | Standalone Android TV launcher for remote navigation, apps and a personal home screen | In development; implementation not verified in this repository | Tested installation, launcher selection, navigation, accessibility and recovery on a published device matrix |
| AuraAmp | Standalone music app for phones and tablets | Planned direction | Confirmed platforms, playback, source authentication and reliable controls |
| AuraBox | Standalone media app for phones and tablets | Planned direction | Clear scope relative to AuraAmp; tested sources, formats and devices |
| AuraConnect | Optional encrypted sync between selected devices | Planned; architecture not verified | Pairing, key lifecycle, threat model, revocation, conflicts, deletion and recovery tests |
| Aura Guardian | Local monitoring of supported attack and integrity signals | Planned; subject to platform permissions | Documented visibility, limitations, integrity tests and false-alarm handling |
| Aura personalization | Optional on-device learning for recommendations | Planned; local processing is the target | Separate opt-in, inspect/reset/delete controls, resource measurements and network verification |

Deezer, media servers and Ultramax are desired connections, not verified integrations or partnerships. Maintain an app-by-app compatibility matrix covering API access, provider terms, subscription/region restrictions, authentication, rate limits and test status. Clarify exactly which Ultramax service/API is intended. Do not assume every integration belongs to every app, or use provider logos without appropriate rights.

### 3. Privacy and security boundaries

Local AURA accounts and local preference storage are the design goal. A local account does not make connected use anonymous or offline. Third-party services may require separate accounts and receive IP addresses, searches, content identifiers, access tokens and service requests. Explain the data flow at connection time. Media servers may be local or remote.

AuraConnect should be optional, with selected data/devices and manual or automatic sync. Distinguish encryption in transit from end-to-end encryption; claim the latter only after protocol, key ownership and validation justify it. Document relays, device discovery, metadata, operational logs, backup and recovery. Sync moves data beyond the originating device, so “data never leaves your device” is not an accurate blanket promise.

Personalization should default off and require its own opt-in. Users should be able to inspect the learning inputs, pause, delete and reset them while retaining core app use. Verify local processing through storage/network inspection. Third-party metadata requests and local preference processing must be explained separately.

Aura Guardian can observe only what the operating system and permissions permit. It cannot guarantee detection of every attack, modified OS or malware infection. Do not claim antivirus-equivalent protection or independent certification. Explain alerts, response options and false-positive reporting.

Before external beta, require a component data inventory, threat model, key lifecycle, least-privilege review, signed builds, secure updates, log redaction, dependency checks, deletion/export and network inspection. Establish a genuinely operational private security-reporting route. Keep secrets and personal logs out of public issues. Review privacy wording and provider terms before launch; this document is not legal clearance.

Safe current wording: “Designed around local control,” “optional sync is planned,” and “on-device personalization is the goal.” Claims such as “no data ever leaves,” “100% private,” “completely secure,” “detects every attack” or “works with every service” require evidence and often remain inappropriate absolutes.

### 4. Audience and product sequence

Start with Android TV users seeking a calm personal home screen and predictable remote navigation. Then address music/media enthusiasts with existing services or servers. Privacy-minded users need concrete controls and documentation, not blanket promises.

Proposed sequence: demonstrate AuraOS first; introduce AuraAmp and AuraBox when each has independent value. Introduce sync, Guardian and learning only when evidence and limitations are available. Validate this order against actual application readiness. One app's release should not depend on unfinished ecosystem promises.

### 5. Milestones and release gates

Use readiness gates rather than unearned dates. Assign named owners once the team is confirmed; the founder owns messaging and release approval.

| Milestone | Deliverables | Exit gate |
| --- | --- | --- |
| M0 — foundation, now | Landing page, strategy, feature register, data inventory, first app selection | Every claim marked verified/in development/planned; no fake downloads or dead calls to action |
| M1 — internal alpha | Signed installable build, test plan, real device matrix, genuine recording | Onboarding, remote navigation and recovery pass on the matrix; known issues published |
| M2 — closed beta | Proposed 15–30 testers, onboarding, changelog, issue template, privacy controls | No unresolved critical security/data-loss defects; proposed target: 90% complete the core task unaided in two test rounds |
| M3 — public beta | Verified distribution, supported-device list, support route, updates and rollback | Proposed target: 99% crash-free sessions over a defined two-week period with sample size and voluntary collection disclosed; use qualitative testing if samples are inadequate |
| M4 — stable launch | Genuine downloads, guides, privacy details, rights/licenses, press kit | Accepted defect budget, tested updates/recovery and sustainable support capacity |
| M5 — expansion | Further app/integration betas, optional sync and personalization | Separate compatibility, privacy and security gates for each addition |

Numbers are proposed targets, not observed results. Agree measurement methods before recruitment. Do not add hidden telemetry to satisfy targets.

### 6. Launch channels and editorial plan

Use GitHub as the first source of truth for plans, releases and limitations. Add issue templates and enable Discussions when someone can moderate. Only the repository is presented as an existing channel today.

Consider relevant Android TV, launcher and self-hosting communities after checking their current self-promotion rules. Disclose the developer relationship, show an actual demo and ask for feedback on one specific problem. Produce short remote-navigation and playback demonstrations from real builds; label concepts. Compare the same hardware under comparable conditions.

Use Norwegian technology communities for the independent-development story and English material for international clarity. Approach small creators and specialist press once a testable beta and honest known-issues list exist. Disclose sponsored relationships. Consider larger launch platforms such as Product Hunt after public-beta onboarding is reliable. No outreach or account creation is performed by this PR.

Suggested cadence: one substantial development update every two weeks, a real demo at each milestone and a monthly roadmap review. Publish when there is evidence to share. Track audience, message, feature evidence, channel, owner and follow-up in a simple content log. Begin organically; consider paid acquisition only after activation and support are demonstrated. No fixed growth or advertising-cost promise.

### 7. Launch kit and measurement

Prepare a one-sentence problem statement, a genuine 30–60 second demo, 3–5 versioned screenshots, supported devices, install/uninstall instructions, privacy summary, known issues, content-rights caveat and an operational support route. Verify links and build signatures. AURA provides software; users need their own rights and any necessary subscriptions.

Measure visits → product/status understanding → actual beta/install choice when available → successful core task → voluntary feedback → continued use. Prefer minimal aggregate, consent-based methods; hosting may independently log IP addresses. The current static page includes no analytics, pixels, cookies or forms. Do not fabricate users, waitlist numbers or performance statistics. Track qualitative friction, misunderstood privacy controls and support workload alongside any quantitative results.

### 8. Website plan

This branch introduces a dependency-free English landing page in `website/`, with responsive dark amber styling, product roles, privacy caveats and milestones. The TV/music scene is a CSS concept, not a product screenshot. GitHub is the only external action destination. No login, backend, download or waitlist endpoint is implied.

Next: a Norwegian version with separate URLs and language metadata; product pages based on verified features; detailed privacy/security pages from the data inventory; accessibility review; real screenshots; and a versioned feature-status register linking to evidence.

Once releases exist, link to genuine stores or signed release assets with versions, requirements and support details. If a waitlist is later chosen, first establish a real provider, lawful collection basis, consent/deletion process and tested delivery. Never add invented contacts or unowned domains.

Deployment options include GitHub Pages publishing `website/` through an approved workflow or another static host. This PR does not deploy automatically. Choose domain, host and log policy before publishing. Review trademark/name rights before a broad campaign; this document does not clear them.

### 9. Decisions still open

Confirm actual app maturity and first alpha; supported operating systems/devices/services and the identity of Ultramax; AuraConnect topology, keys and metadata; Guardian's feasible signals on ordinary non-rooted devices; distribution, licensing, pricing and support capacity; domain, operational contacts, privacy responsibility and release ownership.
