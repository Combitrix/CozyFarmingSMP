# Anhang: Alle 346 Vorschläge der 12 Fachagenten

_Roh-Output des Multi-Agent-Brainstorms. Synthese & Priorisierung siehe [ROADMAP-Erweiterung.md](ROADMAP-Erweiterung.md)._


## balance (21)

### Farming-Tier-System (5 Stufen via FTB Quests Chapter-Groups + KubeJS-Gate)  
*Typ: system*

- **Nutzen:** Definiert klare Farming-Progression: Tier 1 Vanilla-Crops -> Tier 2 HarvestCraft-2-Crops -> Tier 3 Farmer's-Delight-Kueche -> Tier 4 Let's-Do-Veredelung (Wein/Kaese/Tee) -> Tier 5 Create-Central-Kitchen-Automatik. Jede Stufe schaltet die naechste erst nach Abgabe definierter Ertraege frei. Macht das Kernthema des Packs mess- und belohnbar statt beliebig.
- **Integration:** FTB Quests existiert bereits; KubeJS+KubeJS-Create kann Rezepte/Bloecke per Quest-Flag gaten. Tier-Gates ueber Quest-dependencies; Freischaltung sichtbar als neue Chapter im questline.snbt (gen-quests.py erweitern).
- **Quest:** Sehr hoch: je Tier 3-5 Item-Tasks (consume_items: 64x Crop X), Endgame = Massenabgabe automatisierter Ernten. Direkter Ausbau des bestehenden Chapter-Group-1-Blueprints.
- **Progression:** Kern-Progressionsachse des Packs; gibt dem Cozy-Farming-Loop eine vertikale Tiefe und verknuepft Farming -> Cooking -> Create-Automation als roten Faden.
- **Probleme:** KubeJS-Recipe-Gating ist Aufwand und braucht Tests; reine Item-Tasks lassen sich 'erkaufen' (Handel mit anderen Spielern auf SMP). Balancing der Abgabemengen iterativ noetig.

### Community-Tier-System (MineColonies-Buergerzahl als Stufengeber)  
*Typ: system*

- **Nutzen:** Vier Community-Stufen gekoppelt an MineColonies-Kolonie-Level/Buergerzahl: Weiler (1-4 Buerger) -> Dorf (5-12) -> Stadt (13-25) -> Metropole (25+). Jede Stufe schaltet Quest-Belohnungen und Bau-Blueprints frei und gibt dem Town-Building-Pillar Fortschrittsgefuehl.
- **Integration:** MineColonies meldet Kolonie-Level; FTB Quests kann per Statistik/Item-Abgabe (z.B. Town-Hall-Upgrade-Items) prüfen. KubeJS kann MineColonies-Events lesen (Verfuegbarkeit pruefen).
- **Quest:** Hoch: pro Stufe Quests wie 'erreiche Kolonie-Level 3', 'baue Restaurant + Koch', 'siedle 10 Buerger an'. Verbindet sich mit Farming (Restaurant braucht Nahrung).
- **Progression:** Macht den MineColonies-Pillar zur zweiten Hauptachse; gestaffelte Belohnungen verhindern, dass die Kolonie nur 'nebenbei' laeuft.
- **Probleme:** MineColonies-Level automatisch in FTB Quests zu erfassen ist nicht nativ -> evtl. manuelle Checkmark-Quests oder KubeJS-Bridge noetig. Auf SMP mit mehreren Kolonien (allowinfinitecolonies) muss Stufe pro Spieler/Team gelten (FTB Teams nutzen).

### Reputation-Tier-System mit Villager/MineColonies (Vanilla-Emerald-gebunden)  
*Typ: system*

- **Nutzen:** Ruf-Stufen Fremder -> Bekannt -> Geschaetzt -> Held, gemessen an kumuliertem Vanilla-Smaragd-Handel und MineColonies-Buergerzufriedenheit. Hoehere Stufen schalten bessere Villager-Trades / Quest-Shops frei. Liefert die vom Agent geforderte Reputation-Achse ohne Coin-Mod.
- **Integration:** Nutzt Vanilla-Smaragde (MEMORY: kein Coin-Mod), Easy Villagers, Guard Villagers, Trade Cycling. FTB Quests Item-Task auf 'X Smaragde abgeben' als Stufen-Gate; KubeJS kann freigeschaltete Trades aktivieren.
- **Quest:** Hoch: 'handle 32 Smaragde', 'erreiche Dorf-Popularitaet', 'rette einen Buerger'. Quest-Belohnungen skalieren mit Ruf-Stufe.
- **Progression:** Gibt der Vanilla-Wirtschaft Sinn und Langzeitziel; Ruf als weiche Waehrung neben Smaragden.
- **Probleme:** Vanilla-Dorf-Popularitaet ist nicht leicht in Quests auslesbar (eher manuell/KubeJS). Smaragd-Abgabe als Proxy ist abstrakt; Gefahr von Smaragd-Farmen die Reputation trivialisieren -> Mengen hoch ansetzen.

### Village-Tier-System (Dorf-Infrastruktur-Meilensteine)  
*Typ: system*

- **Nutzen:** Stuft den Ausbau der Spielerstadt nach vorhandenen Gebaeudetypen: Stufe 1 Wohnen, Stufe 2 Versorgung (Restaurant/Markt), Stufe 3 Produktion (Create-Werkstatt), Stufe 4 Mobilitaet (Bahnhof), Stufe 5 Repraesentation (Rathaus+Deko). Jede Stufe = sichtbarer Town-Building-Fortschritt.
- **Integration:** Kombiniert MineColonies (Hut-Typen), Create (Werkstatt), Steam'n'Rails (Station), Furniture-Mods (Deko). FTB Quests prueft platzierte Schluesselbloecke per Item-Task beim Crafting.
- **Quest:** Sehr hoch: pro Stufe konkrete Bau-Quests ('baue Bahnhof', 'platziere Town Hall', 'errichte Markt'). Natuerlicher Bau-Leitfaden fuer neue Spieler.
- **Progression:** Strukturiert die offene Town-Building-Sandbox in greifbare Etappen; ideal fuer Onboarding und Langzeit-Ziele auf dem SMP.
- **Probleme:** Platzierte (nicht gecraftete) Bloecke schwer per Quest zu erfassen -> Craft/Consume-Tasks als Proxy. Ueberschneidung mit Community-Tier muss sauber abgegrenzt werden (Buergerzahl vs. Gebaeude).

### Pufferfish's Skills (RPG-Skill-Trees als Progressionsgrundlage)  
*Typ: mod*

- **Nutzen:** Fuegt persistente Skill-Level (Farming, Mining, Fishing, Husbandry, Building, Combat) mit passiven Boni hinzu. Liefert die RPG-lite-Komponente und eine spielereigene Progressionskurve unabhaengig von Quests.
- **Integration:** Ergaenzt Farming/Fishing/Husbandry-Pillars; Skills steigen durch genau die Taetigkeiten die das Pack belohnt. FTB Quests kann Skill-Level als Task abfragen (im Blueprint Kap 1.6 bereits angedacht). (Verfuegbarkeit fuer 1.21.1 NeoForge pruefen)
- **Quest:** Hoch: 'erreiche Farming-Level 10', 'investiere Skillpunkt in X'. Skill-Gates fuer hoehere Quest-Tiers nutzbar.
- **Progression:** Eigenstaendige vertikale Achse die alle anderen Tiers untermauert; Skill-Level als Vorbedingung fuer Farming-/Village-Tiers einsetzbar.
- **Probleme:** NeoForge-1.21.1-Verfuegbarkeit unsicher (eher Fabric-lastig) -> Alternative pruefen. Balancing der passiven Boni darf Cozy-Charakter nicht in Grind kippen.

### FTB Quests Reward-Tables mit Loot-Crates pro Tier  
*Typ: feature*

- **Nutzen:** Gestaffelte Belohnungs-Pools (Bronze/Silber/Gold/Platin-Crate) die je nach erreichtem Tier ausgeschuettet werden. Macht Stufenaufstieg fuehlbar belohnend und steuert, wann seltene Items (Artifacts, Create-Materialien) ins Spiel kommen.
- **Integration:** Reine FTB-Quests-Funktion (RewardTable + Loot-Crate-Items), keine neue Mod. Artifacts-Mod liefert ideale High-Tier-Belohnungen.
- **Quest:** Mittel-hoch: jede Tier-Abschluss-Quest vergibt die passende Crate; Sammel-Quest 'oeffne 10 Crates'.
- **Progression:** Zentrale Belohnungs-Oekonomie die alle vier Tier-Systeme verbindet und das Tempo der Item-Freischaltung kontrolliert.
- **Probleme:** RewardTables muessen sorgfaeltig balanciert werden, sonst Inflation seltener Items. Auf SMP: Crates pro Spieler vs. Team klaeren.

### Tier-Gating von Create-Maschinen via KubeJS (Tech-Progression)  
*Typ: system*

- **Nutzen:** Sperrt fortgeschrittene Create-Rezepte (Mechanical Crafter, New Age, Aeronautics) hinter erreichten Farming-/Village-Tiers, sodass Tech-Power dem Cozy-Aufbau folgt statt ihn zu ueberspringen.
- **Integration:** KubeJS+KubeJS-Create vorhanden; Rezept per Quest-Flag aktivieren. Greift in Chapter-Group-3-Blueprint ein.
- **Quest:** Hoch: 'schalte Mechanical Crafter frei (erfordert Village-Tier 3)'. Macht Tech-Quests zu echten Meilensteinen.
- **Progression:** Verhindert Tech-Rush, haelt den Create-Fokus an die Cozy-Progression gebunden; klare Tech-Tier-Kurve.
- **Probleme:** Recipe-Gating frustriert evtl. Create-erfahrene Spieler; Multiplayer-Gating muss teambasiert sein. Hoher KubeJS-Test-Aufwand.

### Saison-Reputation: Serene-Seasons-gebundene Erntefeste  
*Typ: feature*

- **Nutzen:** Wiederkehrende Saison-Quests (Fruehlingssaat, Sommerernte, Herbstmarkt, Winterlager) mit Reputations- und Smaragd-Belohnung. Bindet Cozy-Jahreszeiten an die Reputation-Achse und schafft Live-SMP-Events.
- **Integration:** Serene Seasons + Bountiful Fares + Let's Do vorhanden; FTB Quests mit wiederholbaren (repeatable) Quests pro Saison.
- **Quest:** Sehr hoch: pro Saison eigene Abgabe-Quests, wiederholbar jaehrlich. Community-Event-Charakter.
- **Progression:** Liefert zyklische statt nur linearer Progression; Reputation waechst ueber Spielzeit, gut fuer Langzeit-SMP.
- **Probleme:** FTB-Quests-Saison-Detection braucht KubeJS-Trigger oder manuelle Checkmark; repeatable-Belohnungen muessen gegen Farming abgesichert sein.

### Reputations-Shop via FTB Quests (gestaffelte Smaragd-Laeden)  
*Typ: feature*

- **Nutzen:** Pro Reputation-Stufe oeffnet sich ein neuer 'Laden' (Quest-Kapitel) mit besseren, gegen Smaragde tauschbaren Waren (seltene Saaten, Deko, Artifacts). Gibt der Vanilla-Wirtschaft ein progressives Endziel.
- **Integration:** FTB Quests Currency? Nein -> Item-Task 'gib N Smaragde' mit Item-Reward. Nutzt Vanilla-Smaragde gemaess MEMORY (kein Coin-Mod).
- **Quest:** Hoch: jeder Laden = Kapitel mit mehreren Kauf-Quests; hoehere Stufen = teurere/seltenere Ware.
- **Progression:** Macht Reputation-Tier konkret nutzbar; Smaragde bekommen Sink, der die Wirtschaft gesund haelt.
- **Probleme:** FTB-Quests-'Shops' sind eigentlich Quests -> etwas umstaendliches Kauf-UX. Preisbalancing kritisch gegen Smaragd-Farmen.

### Onboarding-Tier 0 mit Starter-Progression-Gates  
*Typ: feature*

- **Nutzen:** Erste, sehr kleine Tier-Stufe die neue SMP-Spieler durch Grundmechaniken fuehrt (JEI/Jade-Nutzung, erstes Crop, erste Tierzucht) bevor die Haupt-Tiers freischalten. Senkt Einstiegshuerde des grossen Kitchen-Sink-Packs.
- **Integration:** Baut auf bestehendem Chapter-Group-0-Blueprint auf; nutzt JEI (nicht EMI - MEMORY korrigiert!), Jade, Inventory Tweaks ReFoxed. gen-quests.py erweitern.
- **Quest:** Hoch: kurze Tutorial-Quests; schaltet Farming-Tier-1 frei.
- **Progression:** Definiert den Nullpunkt aller Tier-Kurven; verhindert Ueberforderung und gibt sofortiges Erfolgserlebnis.
- **Probleme:** Blueprint nennt faelschlich EMI/Magic Coins/IPN — muss auf JEI/Smaragde/ReFoxed korrigiert werden, sonst Item-ID-Fehler. Reine Info-Quests brauchen Checkmark-Tasks.

### Husbandry-Tier mit Naturalist & Critters-&-Companions-Sammlung  
*Typ: feature*

- **Nutzen:** Tier-Stufen fuer Tierzucht/Sammlung: zuechte/zaehme zunehmend seltene Arten ueber Naturalist, Critters & Companions, Companions Dogfolk. Liefert die Collection-Achse des Packs.
- **Integration:** Alle Mods bereits enthalten; FTB Quests Breeding-Addon (NERB/Breeding bereits gelistet) zeigt Zuchtrezepte. Item-Tasks auf Zuchtprodukte.
- **Quest:** Hoch: 'zuechte 5 Arten', 'zaehme einen Companion', 'sammle alle Naturalist-Insekten'. Pokedex-artig.
- **Progression:** Eigene Sammel-Tier-Kurve parallel zu Farming; belohnt Erkundung und Cozy-Tier-Pflege.
- **Probleme:** Vollstaendigkeit ('alle Arten') schwer in Quests zu erfassen -> evtl. pro Art einzelne Tasks (viel Pflege). Manche Companions ohne Item-Drop -> Checkmark.

### Fishing-Tier (Aquaculture + Fish of Thieves Stufenleiter)  
*Typ: feature*

- **Nutzen:** Angel-Progression: Holzrute -> bessere Ruten -> seltene Fische -> Trophaeen. Macht den Angel-Pillar zu einer eigenen, belohnenden Tier-Kette.
- **Integration:** Aquaculture, Fish of Thieves, Aquaculture-Delight bereits enthalten; FTB Quests Item-Tasks auf Fischarten + Rute-Upgrades.
- **Quest:** Hoch: 'fange 3 Arten', 'craffe Neptunium-Rute', 'lande einen Trophaeen-Fisch'. Verknuepft mit Cooking-Tier.
- **Progression:** Klar gestufte Nebenachse mit Gear-Progression (Ruten/Koeder), die Cozy-Aktivitaet Angeln vertieft.
- **Probleme:** Seltene-Fisch-Drops sind RNG -> Quests koennen sich ziehen; Balancing der Fang-Mengen. Trophaeen-Erfassung pruefen.

### Cooking-Mastery-Tier (Farmer's Delight + alle Delight-Addons als Rezept-Sammlung)  
*Typ: feature*

- **Nutzen:** Tier-Stufen nach Anzahl gemeisterter Gerichte ueber die riesige Delight-Suite. Verwandelt das Kuechen-Sammelsurium in eine messbare Koch-Meisterschaft mit Freischaltungen.
- **Integration:** Farmer's Delight + ~13 Delight-Addons + Let's Do + Bountiful Fares vorhanden; FTB Quests Item-Tasks auf gekochte Gerichte; JEED zeigt Effekte.
- **Quest:** Sehr hoch: dutzende Gericht-Quests gruppierbar in Tiers (Hausmannskost -> Gourmet -> Festmahl). Riesiger Content-Pool.
- **Progression:** Nutzt die schiere Menge an Food-Mods als Progressions-Treibstoff; Koch-Tier speist Community-/Reputation-Tier (Restaurant).
- **Probleme:** Sehr viele Item-IDs zu verifizieren (JEI in-game noetig). Gefahr von Quest-Flut -> sinnvoll gruppieren/optionalisieren.

### Create-Automation-Tier (manuell -> automatisiert -> Massenproduktion)  
*Typ: system*

- **Nutzen:** Drei Automatisierungs-Stufen pro Produktionskette: Handarbeit -> erste Create-Maschine -> vollautomatische Massenanlage (z.B. Central Kitchen). Belohnt das Pack-Kernziel 'Farming automatisieren mit Create'.
- **Integration:** Create 6 + Confectionery/Cafe/Ratatouille + Ultimate Factory vorhanden; FTB Quests Endgame-Massenabgaben (consume_items hohe Mengen) wie im gen-quests.py-Konzept.
- **Quest:** Sehr hoch: 'liefere 1000x verarbeitetes Gut per Auto-Anlage'. Klassisches FTB-Endgame.
- **Progression:** Verbindet Farming-Tier-5 mit Tech; definiert das eigentliche Endgame des Packs als Skalierungs-Challenge.
- **Probleme:** Sehr-grosse-Mengen-Abgaben koennen grindig wirken; Server-Performance bei vielen Auto-Anlagen (AMP, 5 Spieler) beachten.

### Prestige-/Titel-System ueber FTB Quests Reward (Endgame-Cap)  
*Typ: feature*

- **Nutzen:** Nach Abschluss aller vier Tier-Ketten erhaelt der Spieler/das Team einen Prestige-Titel und ein einzigartiges Repraesentations-Item. Gibt dem Langzeit-SMP ein sichtbares Endziel ('Buergermeister', 'Erntemeister').
- **Integration:** FTB Quests finale Quest (Blueprint Kap 5.3 bereits angedacht); Item-Reward + ggf. Nametag/Custom-Item via KubeJS.
- **Quest:** Mittel: eine grosse Meta-Quest mit Abhaengigkeit von allen Tier-Endquests.
- **Progression:** Schliesst die Progressionsschleife; Hook fuer spaeteres Kartoffelboss-Teilprojekt als Post-Game-Boss.
- **Probleme:** Custom-Titel ohne Coin/RPG-Mod nur via KubeJS-Item/Nametag moeglich. Reine Item-Belohnung kann antiklimaktisch wirken.

### Daily/Weekly Repeatable Quests (Lebendige-Stadt-Aufgaben)  
*Typ: feature*

- **Nutzen:** Wiederholbare Liefer-/Pflege-Quests (taeglich Restaurant beliefern, woechentlich Markt fuellen) die kleine Reputations-/Smaragd-Belohnungen geben. Haelt die Cozy-Routine auf dem SMP lebendig.
- **Integration:** FTB Quests repeatable-Flag; nutzt vorhandene Farming-/Cooking-Outputs. Town Talk / What Are They Up To untermalen Atmosphaere.
- **Quest:** Hoch: rotierende Tagesziele, niedrige Einstiegshuerde, hohe Wiederspielbarkeit.
- **Progression:** Liefert kontinuierlichen, kleinen Reputations-Fortschritt zwischen den grossen Tier-Spruengen; ideales SMP-Login-Incentive.
- **Probleme:** Repeatable-Belohnungen muessen klein bleiben (Inflationsschutz). Reset-Timing auf Server konfigurieren.

### Tier-Freischaltung von Dimensionen/Biom-Zielen (Welt-Tier)  
*Typ: feature*

- **Nutzen:** Erkundungs-Tier: besuche zunehmend ferne Terralith/Tectonic/Nullscape-Ziele als Stufen. Verknuepft die Welt-&-Vernetzung-Saeule mit Progression statt beliebigem Wandern.
- **Integration:** Terralith+Tectonic+Nullscape+Continents vorhanden; FTB Quests Dimension-/Biome-Task oder Checkmark; JourneyMap zum Navigieren.
- **Quest:** Mittel-hoch: 'besuche 3 Biome', 'erreiche Nullscape'. Belohnt Reisen + Bahnnetz-Bau.
- **Progression:** Nebenachse die Mobilitaet (Steam'n'Rails) und Erkundung an Tiers koppelt; speist Village-Tier (Bahnhof).
- **Probleme:** Biome-Detection in FTB Quests begrenzt -> oft Checkmark/KubeJS noetig. Nullscape-Reise sehr aufwendig -> als Bonus-Tier.

### Team-basierte Tier-Progression (FTB Teams als Fortschrittstraeger)  
*Typ: system*

- **Nutzen:** Legt fest, dass alle vier Tier-Systeme pro FTB-Team statt pro Spieler zaehlen, sodass die ~5 SMP-Spieler kooperativ eine gemeinsame Stadt/Reputation hochziehen. Verhindert Doppelarbeit und foerdert Zusammenspiel.
- **Integration:** FTB Teams + FTB Quests (team-shared progression) bereits enthalten; nur Konfiguration (consume_items team-wide).
- **Quest:** Strukturell: betrifft alle Quests; entscheidet ob Tasks team- oder spielergebunden zaehlen.
- **Progression:** Grundlegende Designentscheidung die das SMP-Erlebnis kooperativ macht; skaliert Tier-Mengen auf Gruppengroesse.
- **Probleme:** Team-shared vs. individuell muss konsistent ueber alle Kapitel gesetzt werden; spaete Beitritte zu einem Team erben Fortschritt (Fairness klaeren).

### Reputations-Verfall / Pflege-Mechanik (optional, KubeJS)  
*Typ: custom-mod*

- **Nutzen:** Leichter Reputations-Verfall bei vernachlaessigter Stadt (Buerger unzufrieden) der durch regelmaessige Pflege-Quests ausgeglichen wird. Haelt das Cozy-Town-Management dauerhaft relevant statt 'einmal bauen, fertig'.
- **Integration:** Erfordert KubeJS-Script das MineColonies-Zufriedenheit oder Quest-Timer auswertet; bindet an Reputation-Tier.
- **Quest:** Mittel: 'stelle Buergerzufriedenheit wieder her', gekoppelt an Daily-Quests.
- **Progression:** Fuegt der Reputation-Achse eine dynamische, nicht-monotone Komponente hinzu; verhindert Stagnation im Endgame.
- **Probleme:** Verfall kann Cozy-Spieler frustrieren (Cozy != Druck) -> sehr mild halten oder optional/abschaltbar. Hoher Custom-KubeJS-Aufwand + MineColonies-API-Zugriff unsicher.

### Achievement-Bridge: Vanilla-Advancements als Tier-Trigger  
*Typ: feature*

- **Nutzen:** Nutzt Vanilla/Mod-Advancements als zusaetzliche, automatisch erkannte Tier-Vorbedingungen (z.B. 'Adventuring Time' -> Welt-Tier). Reduziert den Bedarf an manuellen Checkmark-Quests.
- **Integration:** FTB Quests kann Advancement-Tasks nutzen (nativ); keine neue Mod. Greift fuer Biome-/Erkundungs-Tiers.
- **Quest:** Mittel: Advancement-getriggerte Quests als saubere Auto-Detection-Alternative.
- **Progression:** Verbessert die technische Robustheit aller Tier-Gates; weniger 'erkaufbare' Checkmarks.
- **Probleme:** Nicht jeder gewuenschte Meilenstein hat ein passendes Advancement; Mod-Advancement-IDs verifizieren. Begrenzte Abdeckung.

### Farming-Tier-Gate fuer Saatgut-Freischaltung (HarvestCraft-Crops gestaffelt)  
*Typ: system*

- **Nutzen:** Nicht alle ~80 HarvestCraft-2-Crops sofort verfuegbar: Saaten werden tierweise per Quest-Reward/KubeJS freigeschaltet (Grundgemuese -> exotische Frucht -> Gewuerze). Strukturiert die riesige Crop-Vielfalt in eine Lernkurve.
- **Integration:** Pam's HarvestCraft 2 (Crops) + Garden-Drops via KubeJS gaten; FTB Quests vergibt Saatgut-Pakete als Tier-Belohnung.
- **Quest:** Hoch: jede Saatgut-Stufe = Quest-Belohnung; 'baue 10 verschiedene Crops an' pro Tier.
- **Progression:** Verhindert Overload durch sofortige Crop-Flut; macht Farming-Tier-Aufstieg konkret spuerbar (neue Pflanzen).
- **Probleme:** HarvestCraft-Crop-Freischaltung via KubeJS (Garden-Drops/Seeds) ist fummelig und testintensiv; Spieler koennten Saaten ertauschen und Gating umgehen.


## cozy-mods (34)

### Croptopia  
*Typ: mod*

- **Nutzen:** Fuegt 58 neue Crops, 26 Fruchtbaeume und ueber 250 Lebensmittel/Getraenke hinzu (Kaffee, Tee, Smoothies, Saefte) — massiver Cozy-Kuechen- und Gartenbau-Content. Verfuegbar fuer 1.21.1 NeoForge (4.2.1).
- **Integration:** Ergaenzt Farmer's Delight, Pam's HarvestCraft 2 und Let's Do um Tropenfruechte, Getraenke und Verarbeitungsstationen (Mortar, Frying Pan). Wachstum saisonabhaengig via Serene Seasons.
- **Quest:** FTB-Questkette 'Der grosse Garten': jede Crop-Familie freischalten, Fruchtbaum-Plantage anlegen, alle Getraenke brauen. Sammelquests fuer 250 Foods.
- **Progression:** Stufenweise von Basis-Crops zu Tropenfruechten und veredelten Getraenken; Kueche wird ueber Verarbeitungsstationen ausgebaut.
- **Probleme:** Hohe Rezept-Ueberschneidung mit Pam's/Farmer's Delight — KubeJS-Bereinigung doppelter Items (z.B. Tomaten, Mehl) empfohlen, sonst JEI-Wildwuchs.

### Brewin' And Chewin'  
*Typ: mod*

- **Nutzen:** Let's-Do/Farmer's-Delight-Stil-Addon fuer Fermentierung und Getraenke: Bierfaesser, Effekt-Cocktails, gefuellte Kruege, Trinkhorn — sehr cozy fuer Tavernen. NeoForge 1.21.1 (4.2.4) bestaetigt.
- **Integration:** Bindet direkt an Farmer's Delight (gemeinsame Tags) und Let's Do Vinery/Herbal Brews an; ideal fuer MineColonies-Tavernen und Dungeons-&-Taverns-Strukturen.
- **Quest:** Tavernen-Questlinie: Faesser bauen, erste Sude fermentieren, Effekt-Cocktails fuer NPCs liefern, eigenes Wirtshaus eroeffnen.
- **Progression:** Fermentierungs-Tech-Tree: vom einfachen Krug ueber Faesser zu komplexen Effekt-Mischgetraenken.
- **Probleme:** Effekt-Getraenke koennen mit RPG-lite-Balance kollidieren — Effektstaerken evtl. via KubeJS daempfen. Sonst stabil.

### Botany Pots  
*Typ: mod*

- **Nutzen:** Dekorative Pflanzkuebel, die jede Crop/jeden Setzling automatisiert wachsen lassen — perfekt fuer Innen-Gaerten, Balkone und Gewaechshaeuser ohne Ackerflaeche. NeoForge 1.21.1 (21.1.41) bestaetigt.
- **Integration:** Funktioniert mit Crops aus Croptopia, Pam's und Farmer's Delight; ideales Deko-Element in Handcrafted/Another-Furniture-Interieurs und Create-Gewaechshaeusern.
- **Quest:** Quest 'Indoor-Gaertnerei': erste Pots craften, Soil-Tiers freischalten, alle Crop-Typen in Pots ziehen.
- **Progression:** Soil-Upgrade-Pfad (Dirt -> Hydro -> spezialisierte Boeden) erhoeht Geschwindigkeit/Ertrag; gute fruehe Automatisierungs-Bruecke vor Create.
- **Probleme:** Botany Pots Tiers separat fuer hoehere Stufen; reines Auto-Harvest kann Farmen trivialisieren — Ertrag via KubeJS justierbar.

### Immersive Weathering: Renewed  
*Typ: mod*

- **Nutzen:** Stimmungsvolles Wetter und Umwelt-Detail: fallendes Laub, Bluetenflug, Nebel, ansammelnder Schnee, Pfuetzen, kontextuelle Partikel — enorme Cozy-Atmosphaere. 1.21.1 NeoForge-Port bestaetigt.
- **Integration:** Verstaerkt Serene Seasons und Terralith/Tectonic-Biome visuell; harmoniert mit Fresh Animations fuer lebendige Szenen.
- **Quest:** Eher Atmosphaere als Quest, aber Biome-Erkundungsquests (Nature's Compass) gewinnen visuell stark.
- **Progression:** Kein direkter Progress, steigert aber Immersion der saisonalen Spielschleife.
- **Probleme:** Partikel-/Schneeansammlung kann Performance auf schwachen Clients kosten — Configs zum Reduzieren vorhanden. Port-Stabilitaet (Verfuegbarkeit pruefen).

### Paladin's Furniture  
*Typ: mod*

- **Nutzen:** Hochwertige, funktionale Moebel: Kuehlschraenke, Herde, Spuelen, Sofas, Stuehle mit Sitzfunktion, Lampen — fuellt Kueche/Wohnzimmer-Luecke der bestehenden Furniture-Mods. 1.21.1 NeoForge (v1.3) bestaetigt.
- **Integration:** Ergaenzt Handcrafted/Another Furniture/Macaw's um echte funktionale Kuechengeraete; Kuehlschrank als Storage passt zu Sophisticated Storage.
- **Quest:** 'Traumkueche'-Quest: Herd, Kuehlschrank, Spuele, Esstisch bauen und einrichten.
- **Progression:** Einrichtungs-Progression vom leeren Haus zur voll moeblierten Wohnung; Materialvarianten als Sammelziel.
- **Probleme:** Funktionale Ueberschneidung mit Another Furniture (Stuehle/Sitzen) — kosmetisch, kein Konflikt. Every Compat deckt evtl. schon Holzvarianten ab.

### Friends&Foes  
*Typ: mod*

- **Nutzen:** Fuegt die abgewaehlten Mob-Vote-Kreaturen hinzu (Copper Golem, Glare, Moobloom, Iceologer, Crab, Penguin) — charmante, vanilla-nahe Cozy-Mobs fuer Doerfer und Biome. Forge/NeoForge 1.21.1 bestaetigt.
- **Integration:** Moobloom/Crab/Penguin passen zu Naturalist und Critters & Companions; Copper Golem als dekorativer Knopf-Druecker fuer Create-Mechaniken.
- **Quest:** Sammel-/Foto-Quests fuer jede Kreatur; Copper-Golem-Bau als Quest-Belohnung.
- **Progression:** Collection-Aspekt (alle Mobs entdecken) und Copper Golem als Redstone/Create-Helfer.
- **Probleme:** Mob-Overlap mit Naturalist (Crab) und Fish of Thieves moeglich — Spawn-Configs pruefen, um Doppel-Mobs zu vermeiden.

### Visiting Villagers  
*Typ: mod*

- **Nutzen:** Bringt taeglich wechselnde Besucher-NPCs ins Dorf, die zeitlich begrenzte Sonder-Trades anbieten — sehr Stardew/Animal-Crossing: man freut sich auf neue Gaeste. 1.21.1 (Fabric/Forge/NeoForge) bestaetigt.
- **Integration:** Ergaenzt Town Talk, What Are They Up To und Trade Cycling um lebendige, rotierende Dorf-Oekonomie auf Vanilla-Smaragd-Basis.
- **Quest:** 'Gastfreundschaft'-Questlinie: bestimmte Besucher anlocken, deren Sonderwaren handeln, Besucher-Tagebuch fuellen.
- **Progression:** Wirtschaftliche Progression ueber seltene Besucher-Trades; Anreiz zum Dorf-Ausbau, um mehr Gaeste zu ziehen.
- **Probleme:** Spawn-/Pathfinding-Last bei grossen Doerfern; Kompatibilitaet mit Guard Villagers/MineColonies-NPCs pruefen, damit Besucher nicht rekrutiert werden.

### More Villagers  
*Typ: mod*

- **Nutzen:** Sechs neue Villager-Berufe (Hunter, Botanist, Engineer, Chef, Bard, Miner) mit eigenen Workstations und Trades — vertieft Dorfleben und Wirtschaft. NeoForge 1.21.1 bestaetigt.
- **Integration:** Erweitert Easy Villagers, Smarter Farmers und das Vanilla-Smaragd-System; Botanist/Chef-Trades passen perfekt zum Farming-/Kueche-Fokus.
- **Quest:** 'Lebendiges Dorf'-Quest: jeden neuen Beruf ansiedeln, alle neuen Workstations bauen, Berufsketten freischalten.
- **Progression:** Dorf waechst ueber neue Professionen; jeder Beruf liefert neue Handelsgueter als Wirtschaftsstufe.
- **Probleme:** Berufs-/Trade-Balance mit Trade Cycling abstimmen; potenzielle Workstation-Konflikte mit anderen Villager-Mods — Configs pruefen.

### Nature's Compass  
*Typ: mod*

- **Nutzen:** Biome-Suchkompass — laesst Spieler gezielt Cozy-/Farming-Biome (Bluetenwaelder, Kirschhaine) finden, ohne planlos zu reisen. NeoForge 1.21.1 (3.0.3) bestaetigt.
- **Integration:** Synergie mit Terralith/Tectonic/Continents (viele Spezialbiome) und Serene Seasons; reduziert Reise-Frust beim Siedlungsbau.
- **Quest:** Erkundungs-Questkette: definierte Biome auffinden und besuchen, Foto-/Sammelziele pro Biom.
- **Progression:** Eher QoL als Progress, ermoeglicht aber gezielten Aufbau von Themen-Siedlungen pro Biom.
- **Probleme:** Kann Erkundungs-Spannung mindern; bewusst als Belohnung spaeter freischalten via FTB Quests. Sonst sehr stabil.

### Explorer's Compass  
*Typ: mod*

- **Nutzen:** Struktur-Suchkompass — findet Doerfer, Taverns (Dungeons & Taverns) und andere Strukturen gezielt. NeoForge 1.21.1 (3.0.3) bestaetigt.
- **Integration:** Pendant zu Nature's Compass; arbeitet mit Dungeons & Taverns und Structures Arise; integriert mit JourneyMap-Wegpunkten.
- **Quest:** 'Kartograph'-Quest: bestimmte Strukturen lokalisieren und entdecken; Belohnung pro gefundenem Struktur-Typ.
- **Progression:** QoL fuer das Auffinden von Siedlungs-/Quest-Zielen; spaet freischaltbar als Komfort-Upgrade.
- **Probleme:** Wie Nature's Compass: kann Erkundung trivialisieren — als spaete Belohnung gaten. Stabil.

### Lootr  
*Typ: mod*

- **Nutzen:** Instanzierte, pro Spieler einzigartige Lootkisten — auf einem Cozy-SMP bekommt jeder Spieler eigene Beute aus Strukturen, kein Wettlauf/Frust. Forge/NeoForge 1.21.1 bestaetigt.
- **Integration:** Wichtig fuer Multiplayer-Fairness auf dem SMP; arbeitet mit Dungeons & Taverns/Structures-Arise-Loot und FTB Teams.
- **Quest:** Ermoeglicht wiederholbare Loot-Quests ('durchsuche 5 Taverns'), da jeder Spieler eigene Kisten hat.
- **Progression:** Indirekt — fairer Loot-Zugang stuetzt die gesamte Erkundungs-Progression auf dem Server.
- **Probleme:** Aendert Loot-Verhalten global; Mods mit eigenen Loot-Containern (Sophisticated) ggf. ausnehmen. Konfig pruefen.

### Visual Workbench  
*Typ: mod*

- **Nutzen:** Werkbank behaelt sichtbar gelegte Items als Deko/Convenience — kleine, aber sehr cozy QoL fuer Crafting-Stationen in eingerichteten Werkstaetten. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Passt zu den vielen Furniture-/Werkstatt-Setups (Handcrafted, Macaw's) und Create-Werkbaenken; rein clientseitig-nah, geringe Last.
- **Quest:** Gering; eher Ambiente fuer eingerichtete Crafting-Raeume in Quest-Hubs.
- **Progression:** Keine direkte Progression; verbessert Werkstatt-Immersion.
- **Probleme:** Kompatibilitaet mit Crafting Tweaks / Mouse Tweaks pruefen, da beide ins Crafting-GUI eingreifen.

### Wandering Collector  
*Typ: mod*

- **Nutzen:** Spieler-Tode hinterlassen eine sichtbare Grabkiste/Marker statt verstreuter Items — todesfreundliches, stressarmes Cozy-Erlebnis ohne Item-Verlust-Panik. (Verfuegbarkeit fuer 1.21.1 NeoForge pruefen).
- **Integration:** Passt zur entspannten SMP-Philosophie neben Comforts (Schlafsaecke); reduziert Frust bei Erkundung mit Naturalist-Gefahren.
- **Quest:** Gering; Komfort-Feature statt Quest-Inhalt.
- **Progression:** Keine direkte Progression; senkt Einstiegshuerde fuer casual Cozy-Spieler.
- **Probleme:** Alternativ Corpse/Gravestone-Mods pruefen, falls dieser nicht fuer NeoForge 1.21.1 existiert; Konflikt mit FTB-Keep-Inventory-Regeln klaeren.

### Falling Leaves  
*Typ: mod*

- **Nutzen:** Sanft herabfallende Blaetter-Partikel von Baeumen — minimalistische, performante Cozy-Atmosphaere fuer Waelder und Gaerten. NeoForge 1.21.1 (Verfuegbarkeit pruefen, weit verbreitet).
- **Integration:** Verstaerkt Serene Seasons (Herbstlaub) und Fresh Animations optisch; leichtgewichtige Alternative/Ergaenzung zu Immersive Weathering.
- **Quest:** Keine; reine Ambiente-Verbesserung.
- **Progression:** Keine; Stimmungs-Boost fuer die saisonale Schleife.
- **Probleme:** Clientseitig; bei gleichzeitigem Einsatz mit Immersive Weathering Partikel-Overlap moeglich — eines davon waehlen.

### Dramatic Doors  
*Typ: mod*

- **Nutzen:** Hohe (2-blockige) Tueren und Tor-Varianten fuer alle Holz-/Mod-Tueren — wertet Eingaenge von Cozy-Haeusern, Scheunen und Tavernen architektonisch auf. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Arbeitet mit Macaw's Doors, Supplementaries und Every Compat ueber Tags; passt zu MineColonies/Structurize-Gebaeuden.
- **Quest:** Gering; Bau-/Einrichtungs-Element fuer Wohnquests.
- **Progression:** Dekorative Bau-Vielfalt; kein Tech-Progress.
- **Probleme:** Tag-/Compat-Abgleich mit Macaw's und Every Compat noetig, sonst fehlende Varianten.

### Explorations / Towns and Towers (Strukturen)  
*Typ: mod*

- **Nutzen:** Fuegt belebte Doerfer-Erweiterungen, Aussenposten und Strukturen hinzu, die Erkundung Cozy und lohnend machen — neue Siedlungs-Vorlagen zum Bewohnen. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Ergaenzt Dungeons & Taverns und Structures Arise; mit Lootr fair lootbar; Doerfer als MineColonies-Ausgangspunkte nutzbar.
- **Quest:** Erkundungs-/Besiedlungsquests: gefundene Strukturen restaurieren und beleben.
- **Progression:** Erkundungs-Progression durch neue Struktur-Tiers und deren Beute.
- **Probleme:** Struktur-Spawn-Konflikte mit anderen Struktur-Mods (Dungeons & Taverns) — Spacing-Configs abstimmen, sonst Overcrowding.

### Cosmetic Armor Reworked  
*Typ: mod*

- **Nutzen:** Erlaubt kosmetische Ruestungs-/Outfit-Slots — Spieler koennen sich modisch kleiden (cozy/casual Look) unabhaengig von der funktionalen Ruestung. NeoForge 1.21.1 (Verfuegbarkeit pruefen).
- **Integration:** Passt zu 3D Skin Layers und Artifacts (Accessoires); Outfit-Wechsel fuer Festivals/Rollenspiel auf dem SMP.
- **Quest:** Mode-/Festival-Quests: bestimmte Outfit-Sets sammeln und tragen.
- **Progression:** Sammel-/Collection-Aspekt fuer Kleidungssets; rein kosmetisch.
- **Probleme:** Slot-Mod-Kompatibilitaet (Curios/Accessories-Backend) pruefen; auf NeoForge 1.21.1 evtl. Alternative noetig.

### Festive (Christmas/Seasonal Deco)  
*Typ: mod*

- **Nutzen:** Saisonale Festival-Deko (Lichterketten, Kraenze, festliche Bloecke) fuer Erntedank-/Winter-Events — direkter Cozy-Festival-Content. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Kombiniert mit Serene Seasons (Winter-Events) und Bells & Whistles; Deko fuer Dorf-Feste und MineColonies-Plaetze.
- **Quest:** Festival-Questreihe: Dorfplatz fuer Saison-Event schmuecken, Festtags-Deko sammeln.
- **Progression:** Sammelziele pro Saison; jaehrlich wiederkehrende Event-Inhalte.
- **Probleme:** Saisonale Mods sind oft schlecht gepflegt — NeoForge-1.21.1-Version und Wartung pruefen; ggf. via KubeJS/Resourcepack-Deko ersetzen.

### Chococraft / Familiar Pets (Reittiere & Haustiere)  
*Typ: mod*

- **Nutzen:** Zuechtbare, zaehmbare Begleit-/Reittiere mit Persoenlichkeit — erweitert das Haustier-Erlebnis ueber Hunde/Katzen hinaus (Stardew-Tier-Vibe). 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Ergaenzt Critters & Companions, Companions Dogfolk und Naturalist; Stall-/Gehege-Bau mit Farm & Charm.
- **Quest:** Tierzucht-Questlinie: Tier zaehmen, fuettern, Farben/Varianten zuechten, Stall bauen.
- **Progression:** Zucht-Progression (Varianten/Eigenschaften) als langfristiges Collection-Ziel.
- **Probleme:** Genauen 1.21.1-NeoForge-Kandidaten verifizieren (Chococraft-Status unsicher); Mob-Cap-/Spawn-Last bei Zuchtfarmen beachten.

### Aquaculture-Stil Angel-Erweiterung (FishOnAStick / Fishing+)  
*Typ: mod*

- **Nutzen:** Vertieft Angeln um Mini-Spiel-/Sammelmechanik und neue Fischarten — entspanntes Stardew-Angeln als eigenes Cozy-Hobby. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Baut auf bereits enthaltenem Aquaculture und Fish of Thieves auf; Faenge fuer Delight-Kochrezepte nutzbar.
- **Quest:** Angel-Almanach-Quest: alle Fischarten fangen, Rekordgroessen, Saison-/Biome-Fische.
- **Progression:** Angelruten-/Koeder-Upgrades; Fisch-Sammlung als langfristiges Ziel.
- **Probleme:** Overlap mit Aquaculture-Loottables — KubeJS-Abstimmung; konkreten gepflegten 1.21.1-NeoForge-Mod verifizieren.

### Bumblezone / Productive Bees (Imkerei)  
*Typ: mod*

- **Nutzen:** Vertiefte Bienen-/Imkerei-Mechanik mit vielen Bienenarten, Honigsorten und Bienenstock-Deko — cozy Garten-Hobby mit Sammelaspekt. Productive Bees 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Synergie mit Let's Do Meadow, Croptopia-Bestaeubung und Garten-Deko (Botany Pots); Honig fuer Delight-/Brewin-Rezepte.
- **Quest:** Imker-Questkette: Bienenarten sammeln, Stoecke ausbauen, seltene Honigsorten produzieren.
- **Progression:** Bienen-Zucht-Tech-Tree mit immer wertvolleren Arten/Produkten.
- **Probleme:** Productive Bees ist umfangreich und kann fast zum eigenen Tech-System werden — kann Cozy-Fokus ueberlagern; Scope via Configs/KubeJS begrenzen.

### Ars Nouveau  
*Typ: mod*

- **Nutzen:** Cozy-magisches Garten-/Quality-of-Life-System: dekorative Magie, automatische Garten-Helfer (Whirlisprigs), schoene Glyphen-Magie statt Kampf-Grind. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Whirlisprig-Garten-Automation ergaenzt Farming; magische Deko passt zu Cozy-Aesthetik; QoL-Spells helfen beim Bauen.
- **Quest:** Magier-Questlinie: Spellbook freischalten, Glyphen sammeln, magischen Garten anlegen.
- **Progression:** Tiefe Glyphen-/Mana-Progression als optionaler RPG-lite-Pfad neben Create.
- **Probleme:** Grosser Scope koennte mit Create-Fokus konkurrieren; bewusst auf Cozy-/Garten-/QoL-Aspekt zuschneiden, Kampfmagie ggf. zurueckhalten.

### Twigs  
*Typ: mod*

- **Nutzen:** Kleine dekorative Natur-Bloecke: Kiesel, Lampen, Tonziegel, Bambus-Matten, gestapelte Bloecke — feinkoernige Cozy-Detail-Deko fuer Gaerten und Innenraeume. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Ergaenzt Supplementaries, Chipped und Macaw's um natuerliche Detail-Bloecke; ideal fuer Garten-/Pfad-Gestaltung mit Macaw's Paths.
- **Quest:** Gering; Bau-/Dekomaterial fuer Einrichtungsquests.
- **Progression:** Dekovielfalt; kein Tech-Progress.
- **Probleme:** Block-Overlap mit Supplementaries/Chipped moeglich (kosmetisch); Every Compat-Abdeckung pruefen, um Redundanz zu minimieren.

### Garnished / Connector-freie Garten-Deko (Garden Hoes & Plant Pots)  
*Typ: mod*

- **Nutzen:** Zusaetzliche Pflanztoepfe, Hecken, Blumenkaesten und Garten-Werkzeuge fuer detaillierte Aussenanlagen — Animal-Crossing-Gartengestaltung. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Kombiniert mit Botany Pots, Let's Do Meadow und Macaw's Paths/Fences fuer komplette Gartenlandschaften.
- **Quest:** Garten-Gestaltungsquest: Vorgarten/Park anlegen, Blumensorten in Kaesten sammeln.
- **Progression:** Dekorative Garten-Progression; Sammelziele fuer Blumenarten.
- **Probleme:** Konkreten gepflegten 1.21.1-NeoForge-Mod verifizieren; Overlap mit Let's Do Meadow/Supplementaries-Pflanztoepfen pruefen.

### Sleep Tight / Comforts-Ergaenzung (Bessere Betten)  
*Typ: mod*

- **Nutzen:** Verbessert Schlaf/Betten: persoenliche Spawnpunkte, Bett-Buffs, Wecker, gemuetlichere Schlaf-Mechanik — staerkt das Heim-Gefuehl. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Ergaenzt das bereits enthaltene Comforts (Schlafsaecke/Haengematten) um Bett-Tiefe; passt zu eingerichteten Schlafzimmern.
- **Quest:** Gering; Heim-/Einrichtungs-Quest 'eigenes Schlafzimmer'.
- **Progression:** Bett-Buffs als kleine Heim-Belohnung; kein grosser Tech-Pfad.
- **Probleme:** Funktions-Overlap mit Comforts (Schlaflogik) — auf doppelte Schlaf-Handler pruefen; eventuell nur eines der beiden Features aktivieren.

### Variant Crafting Tables / Workstations Deco  
*Typ: mod*

- **Nutzen:** Holz-/Material-Varianten funktionaler Stationen (Crafting Table, Ofen, Amboss) passend zur Inneneinrichtung — Werkstaetten sehen cozy und stimmig aus. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Stimmig mit Handcrafted, Another Furniture und Every Compat-Holzsets; passt zu themenspezifischen Werkstaetten in Quest-Hubs.
- **Quest:** Gering; Einrichtungs-Element fuer Werkstatt-Quests.
- **Progression:** Dekovielfalt; kein Tech-Progress.
- **Probleme:** Every Compat liefert evtl. bereits viele Varianten — Redundanz pruefen, um JEI nicht aufzublaehen.

### Handcrafted-Ergaenzung: Macaw's Trapdoors & Fences  
*Typ: mod*

- **Nutzen:** Detaillierte Falltueren und Zaun-Varianten zur Vervollstaendigung der Macaw's-Suite — Gartenzaeune, Scheunentore, dekorative Trennelemente fuer Cozy-Grundstuecke. 1.21.1 NeoForge (Macaw's-Suite weit verfuegbar).
- **Integration:** Vervollstaendigt die bestehenden Macaw's-Mods (Furniture/Roofs/Paths) mit Every-Compat-Holzvarianten; ideal fuer Farm-Gehege.
- **Quest:** Gering; Bau-/Gehegequests (Tierzaeune, Gartenabgrenzung).
- **Progression:** Bau-Vielfalt fuer Grundstuecksgestaltung; kein Tech-Progress.
- **Probleme:** Mehr Bloecke = mehr JEI-Eintraege/Registrierungslast; nur ergaenzen, wenn nicht schon durch andere Macaw's-Module abgedeckt.

### Tom's Storage / Functional Storage Deko-Drawers  
*Typ: mod*

- **Nutzen:** Dekorative beschriftbare Lager-Drawers mit sichtbaren Items — cozy, ordentliche Vorratskammern und Werkstattregale mit visuellem Reiz. 1.21.1 NeoForge (Functional Storage verfuegbar).
- **Integration:** Ergaenzt Sophisticated Storage um sichtbare, beschriftete Wand-Lagerung; passt zu eingerichteten Speisekammern (Farmer's Delight Vorraete).
- **Quest:** Gering; Einrichtungs-/Ordnungsquest 'organisierte Vorratskammer'.
- **Progression:** Storage-Upgrade-Pfad (Kapazitaet/Verlinkung) als sanfte Progression.
- **Probleme:** Overlap mit Sophisticated Storage — Funktion klar trennen (Deko vs. smart); Doppel-Storage-Systeme koennen Spieler verwirren.

### Pet Cosmetics / Dog & Cat Collars (Haustier-Anpassung)  
*Typ: mod*

- **Nutzen:** Halsbaender, Namen und kosmetische Anpassung fuer Haustiere — emotionale Bindung und Animal-Crossing-Haustierpflege. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Ergaenzt Critters & Companions, Companions Dogfolk und Vanilla-Hunde/Katzen um Personalisierung.
- **Quest:** Haustier-Pflege-Quest: Haustier benennen, Halsband craften, Pflege-Routine.
- **Progression:** Sammel-/Personalisierungsaspekt fuer Haustier-Accessoires.
- **Probleme:** Konkreten gepflegten 1.21.1-NeoForge-Mod verifizieren; Kompatibilitaet mit Companion-Mods pruefen, damit Modelle nicht kollidieren.

### Polymorph  
*Typ: mod*

- **Nutzen:** Rezept-Konfliktloeser, der bei mehreren moeglichen Rezepten eine Auswahl-GUI zeigt — bei diesem rezeptreichen Cozy-Pack (viele Delight/Croptopia/HarvestCraft-Ueberschneidungen) essentiell fuer reibungsloses Crafting. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Loest Rezept-Kollisionen zwischen Croptopia, Pam's, Farmer's Delight und Brewin' auf; arbeitet mit JEI/Crafting Tweaks.
- **Quest:** Keine; reines QoL fuer das massive Rezept-Oekosystem.
- **Progression:** Keine; entfernt Reibung und stuetzt damit die Kuechen-/Crafting-Schleife.
- **Probleme:** NeoForge-1.21.1-Verfuegbarkeit verifizieren; bei sehr vielen Konflikten kann GUI haeufig auftauchen — alternativ KubeJS-Rezeptbereinigung.

### Wakes (Wasser-Wellen)  
*Typ: mod*

- **Nutzen:** Boote/Spieler erzeugen sichtbare Wellen und Spritzer im Wasser — atmosphaerischer Detail-Boost fuer Seen, Teiche und Kuesten-Cozy-Doerfer. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Verstaerkt Aquaculture-Angeln, Let's Do Beachparty und Fish of Thieves visuell; harmoniert mit Steam'n'Rails-Booten.
- **Quest:** Keine; reine Ambiente-Verbesserung.
- **Progression:** Keine; Stimmungs-Boost fuer Wasser-Szenen.
- **Probleme:** Clientseitige Performance auf grossen Wasserflaechen pruefen; Konflikt mit anderen Wasser-Shadern/Mods moeglich.

### Effective (Umgebungs-Partikel & Sound)  
*Typ: mod*

- **Nutzen:** Wasserfall-Nebel, Spritzer, Glühwürmchen, atmosphaerische Umgebungspartikel und -klaenge — verdichtet die Cozy-Naturatmosphaere erheblich. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Kombiniert mit Immersive Weathering, Falling Leaves und Naturalist fuer lebendige Biome; clientseitig.
- **Quest:** Keine; Ambiente.
- **Progression:** Keine; Immersions-Boost.
- **Probleme:** Partikel-Last auf schwachen Clients; mit anderen Partikel-Mods (Immersive Weathering, Effective) abstimmen, um Ueberlagerung zu vermeiden.

### Sound Physics Remastered  
*Typ: mod*

- **Nutzen:** Realistischer Raumklang/Hall — Tavernen, Hoehlen und Holzhaeuser klingen authentisch gemuetlich; starker Immersionsfaktor fuers SMP. 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Verstaerkt Ambient-Sounds aus Town Talk, Bells & Whistles und Effective; rein clientseitig.
- **Quest:** Keine; Ambiente.
- **Progression:** Keine; Immersions-Boost.
- **Probleme:** Clientseitige CPU-Last; auf sehr schwachen Rechnern deaktivierbar halten. Sonst stabil und beliebt.

### Balm-/Collective-abhaengige Mini-QoL: Clumps & FerriteCore  
*Typ: mod*

- **Nutzen:** Performance-/Stabilitaets-Mods (XP-Orb-Bundling, RAM-Reduktion) — essentiell, damit dieses grosse Cozy-Pack auf Client (Prism) und Server (AMP) fluessig laeuft. 1.21.1 NeoForge weit verfuegbar.
- **Integration:** Servertauglich, unterstuetzt das umfangreiche Mod-Set; arbeitet mit FTB- und Create-Last-Reduktion.
- **Quest:** Keine; technische Grundlage.
- **Progression:** Keine; ermoeglicht stabile Progression durch bessere Performance.
- **Probleme:** Keine nennenswerten; FerriteCore-Mixins selten konfliktanfaellig — bei Crash-Reports zuerst als Verdaechtige pruefen.


## crazy-ideas (21)

### Museum & Naturkunde-Halle (KubeJS + MineColonies-Gebaeude)  
*Typ: feature*

- **Nutzen:** Stardew-Museum-Erlebnis: Spieler spenden Funde (Fossilien, seltene Fische aus Fish of Thieves/Aquaculture, Critters-Companions-Sichtungen, Pflanzen aus HarvestCraft) an ein zentrales Dorfmuseum. Jede Spende fuellt eine sichtbare Display-Wand (Supplementaries Display-Schilder/Globes, Sophisticated Storage Frames).
- **Integration:** Annahme-Logik per KubeJS-Item-Right-Click-Event auf einen 'Spendentisch'; Fortschritt in FTB-Quests-Chapter 'Museum' getrackt. Gebaeude als Structurize-Blueprint im Dorf. Naturalist/Fish of Thieves liefern die Sammelobjekte.
- **Quest:** Hoch: Pro Sammlungs-Kategorie (Fossilien, Fische, Insekten, Pflanzen) eine FTB-Quest-Reihe; Meilensteine bei 25/50/100 % Vollstaendigkeit. Versteckte 'Master-Sammler'-Quest fuer 100 %.
- **Progression:** Belohnungen pro Spendenschwelle: kosmetische Bloecke (Chipped/Bells & Whistles), Smaragde, Zugang zu neuen Museumsfluegeln. Sammlungsstand schaltet Town-Building-Stufen frei.
- **Probleme:** Vollstaendig KubeJS-machbar, aber Display-Logik (persistente Vitrinen) ist scripting-aufwendig. Datenpersistenz pro Spieler vs. serverweit klaeren. Kein zusaetzlicher Mod noetig.

### Community Center / Sammel-Buendel-System ('Bundles')  
*Typ: feature*

- **Nutzen:** Direkte Stardew-Community-Center-Adaption: ein verfallenes Dorfgebaeude wird durch das Abgeben thematischer Item-Buendel (Fruehlings-Ernte, Handwerks-Buendel, Fisch-Buendel, Create-Maschinen-Buendel) Raum fuer Raum restauriert.
- **Integration:** FTB-Quests als Buendel-Abgabe-Interface (Quest = Buendel, Items als Input). Bei Kapitel-Abschluss triggert KubeJS das Platzieren/Ersetzen von Strukturteilen (Structurize/Schematik) -> sichtbarer Wiederaufbau.
- **Quest:** Sehr hoch: ist im Kern ein ganzes Quest-Kapitel-Netzwerk. Jeder Raum = Quest-Gruppe, jedes Buendel = Quest mit 4-6 Item-Slots.
- **Progression:** Jeder restaurierte Raum gibt dauerhaften Dorf-Buff (z. B. Haendler oeffnet, Bruecke gebaut, neue Rezepte). Endbelohnung: zentrales Dorf-Feature freigeschaltet.
- **Probleme:** Sichtbarer Wiederaufbau per Schematik-Platzierung ist technisch fummelig (FTB Quests hat kein natives Struktur-Place); ggf. nur Tuer/Barriere entfernen statt Vollaufbau. Balance der Buendel-Anforderungen.

### Ingame-Kalender & Festival-Scheduler  
*Typ: system*

- **Nutzen:** Zentrales System, das mit Serene Seasons synchronisiert ist: ein lesbares Kalenderbuch (Supplementaries 'Quill & Ink'/Custom-Item) zeigt aktuellen Tag, Jahreszeit und naechste Festivals/Events. Bildet das Rueckgrat fuer ALLE wiederkehrenden Events.
- **Integration:** KubeJS liest Serene-Seasons-Tag/Saison via Server-Tick-Event und setzt Server-Scriptable-Flags; Town-Talk/Bells & Whistles fuer Ankuendigungen. JourneyMap-Kompatibel als HUD-Eintrag (Verfuegbarkeit pruefen fuer HUD-API).
- **Quest:** Mittel direkt, aber Enabler: zeitgebundene Quests ('Liefere X am Erntedank-Tag') werden erst durch den Kalender moeglich.
- **Progression:** Enabler-System: schaltet saisonale Inhalte stufenweise frei; Spieler planen Anbau/Vorbereitung auf Events -> langfristige Progressionsschleife.
- **Probleme:** Serene-Seasons-Tageszaehler korrekt auslesen und persistent halten. Festival-Trigger zeitlich robust gegen Server-Neustarts machen. Reines KubeJS, machbar aber Scripting-intensiv.

### Jahreszeiten-Festivals (4 grosse Saison-Events)  
*Typ: feature*

- **Nutzen:** Pro Serene-Seasons-Saison ein mehrtaegiges Dorffest mit dekoriertem Festplatz, Sonderhaendlern, Mini-Spielen und Saison-exklusiven Belohnungen (Fruehlingsbluetenfest, Sommer-Luau am Strand mit Let's Do Beachparty, Herbst-Erntedank, Winter-Sternennacht-Markt).
- **Integration:** Vom Kalender-Scheduler getriggert; KubeJS spawnt temporaere Haendler (Easy Villagers/Trade Cycling) und Deko (Bells & Whistles, Let's Do Beachparty, Macaw's). Festplatz als MineColonies/Structurize-Gebaeude.
- **Quest:** Sehr hoch: jedes Festival = eigenes Quest-Chapter mit Vorbereitungs-, Teilnahme- und Wettbewerbsquests (z. B. 'Bringe ein Gericht zum Herbst-Potluck').
- **Progression:** Saison-Token-Waehrung nur waehrend Festivals erhaeltlich -> einloesbar gegen exklusive kosmetische/funktionale Items. Jaehrliche Wiederkehr haelt Langzeitmotivation.
- **Probleme:** Temporaere Strukturen/Haendler sauber wieder despawnen. Viel Content-Authoring. Beachparty/Saison-Mods bereits enthalten -> nur Orchestrierung noetig.

### Angelturnier (Fishing Derby)  
*Typ: feature*

- **Nutzen:** Wiederkehrendes Wettbewerbs-Event: in einem Zeitfenster zaehlt KubeJS gefangene Fische nach Seltenheit/Gewicht (Aquaculture liefert Fischgewicht-NBT, Fish of Thieves liefert seltene Arten). Rangliste am Ende.
- **Integration:** KubeJS Fishing-Event-Listener akkumuliert Punkte pro FTB-Team; Aquaculture-Gewicht-NBT als Wertungsbasis. Ergebnistafel via Supplementaries-Schild oder Custom-Scoreboard.
- **Quest:** Hoch: Teilnahme-Quest + Platzierungs-Quests ('Top 3'); Sammelquest fuer alle Turnier-exklusiven Arten.
- **Progression:** Turniersieger erhalten bessere Angelruten/Koeder (Aquaculture) und Trophaeen-Deko. Aufstiegssystem ueber mehrere Turniere ('Anglermeister'-Titel).
- **Probleme:** Aquaculture-Gewicht-NBT-Feldname verifizieren (Verfuegbarkeit pruefen). Scoreboard-Persistenz und Multiplayer-Fairness (AFK-Angelfarmen) abfangen.

### Erntewettbewerb (Grange Display / Giant Crops)  
*Typ: feature*

- **Nutzen:** Herbst-Highlight a la Stardew Grange Display: Spieler reichen ihre besten/groessten Ernteprodukte ein und werden nach Qualitaet und Vielfalt bewertet. Optional 'Riesen-Ernte'-Mechanik fuer besonders gepflegte Felder.
- **Integration:** FTB-Quests-Abgabe-Interface fuer die Display-Slots; KubeJS bewertet Vielfalt/Menge (HarvestCraft 2 + Farmer's Delight + Let's Do Crops). Bewertung an Serene-Seasons-Herbst gekoppelt.
- **Quest:** Hoch: Vorbereitungsquests ('Baue 5 verschiedene Herbstfruechte an'), Einreichungs-Quest, Sieger-Quest.
- **Progression:** Punktzahl schaltet Premium-Saatgut, Duenger-Rezepte (KubeJS) oder Bewaesserungs-Upgrades frei. Treibt Diversifizierung der Farm.
- **Probleme:** Qualitaetsstufen existieren in Vanilla/diesen Mods nicht nativ -> Bewertung muss KubeJS ueber Vielfalt+Menge approximieren. 'Giant Crops' ggf. nur kosmetisch via Custom-Block.

### Kochwettbewerb (Iron Chef / Potluck)  
*Typ: feature*

- **Nutzen:** Wettbewerb rund um die riesige Farmer's-Delight/Let's-Do-Kueche: Spieler reichen Gerichte ein, die nach Komplexitaet (Anzahl Zutaten/Verarbeitungsschritte) und Themen-Vorgabe ('Festtagsmenue', 'Suppen-Spezial') gewertet werden.
- **Integration:** FTB-Quest-Abgabe + KubeJS-Bewertung anhand Item-Tags (farmersdelight:, letsdo:, alldelight-Addons). Town-Talk-NPCs als 'Jury'.
- **Quest:** Sehr hoch: thematische Rundenquests, Rezept-Entdeckungsquests, 'Erfinde ein neues Gericht'-Quest (Custom-KubeJS-Rezept).
- **Progression:** Sieg schaltet exklusive Rezepte (Custom-KubeJS-Food mit Buffs) und Kuechen-Deko frei. Comforts/AppleSkin machen Food-Buffs relevant.
- **Probleme:** Sehr viele moegliche Gerichte -> Bewertungslogik muss generisch ueber Tags laufen, nicht hartkodiert. Balance der Buff-staerke neuer Custom-Gerichte.

### Sammelalben / Stempelheft (Critterpedia & Cookbook)  
*Typ: feature*

- **Nutzen:** Animal-Crossing-artige digitale Sammelalben: ein 'Critterpedia'-Buch fuellt sich automatisch beim erstmaligen Fangen/Sehen von Tieren (Naturalist, Critters & Companions, Fish of Thieves) und ein 'Kochbuch' beim erstmaligen Zubereiten von Gerichten.
- **Integration:** KubeJS trackt Erst-Interaktionen pro Spieler (PlayerData) via Entity-Interact/Item-Crafted-Events; Anzeige ueber JEI-Integration oder Custom-GUI (Verfuegbarkeit Custom-GUI-Lib pruefen) oder einfacher ueber FTB-Quest-'Detection'-Chapter.
- **Quest:** Hoch: Vervollstaendigungs-Quests pro Album, versteckte 100-%-Quest. Synergie mit Museum/Wettbewerben.
- **Progression:** Album-Fortschritt gibt passive Boni (z. B. mehr Drops von erfassten Tieren) und Sammler-Titel. Langzeit-Completionist-Ziel.
- **Probleme:** Persistente Per-Player-Erfassung sauber speichern. Custom-GUI ist aufwendig -> MVP ueber FTB-Quests-Detection darstellbar. Reine KubeJS-Logik.

### Haendlerkarawane (Wandering Merchant Caravan)  
*Typ: feature*

- **Nutzen:** Stardew-'Traveling-Cart'-Erlebnis: an bestimmten Wochentagen erscheint eine sichtbare Karawane (Create-Wagen/Steam'n'Rails-Waggon als Deko) am Dorfrand mit rotierendem, teils seltenem Sortiment (Saatgut, Deko, Artifacts-Items).
- **Integration:** Kalender-Scheduler triggert Spawn; KubeJS platziert Karawanen-Struktur + Sonderhaendler (Easy Villagers / Trade Cycling fuer rotierende Trades). Create/Steam'n'Rails liefern die Optik.
- **Quest:** Mittel-hoch: 'Finde den Haendler diese Woche'-Quest, Sammelquests fuer Karawanen-exklusive Items.
- **Progression:** Zugang zu sonst unerreichbaren Items (seltene Samen, Deko) gegen Smaragde -> Smaragd-Sink fuer die Vanilla-Wirtschaft. Sortiment skaliert mit Spielfortschritt.
- **Probleme:** Wagen-Struktur sauber spawnen/despawnen. Trade-Rotation mit Trade Cycling abstimmen. Karawanen-Pfad/Standort pro Welt definieren.

### Rare-Creature-Hunting (Legendaere Kreaturen)  
*Typ: feature*

- **Nutzen:** Stardew-'Legend-Fish'-Aequivalent fuer Land/Wasser: extrem seltene, an Saison/Wetter/Biom/Tageszeit gebundene Spawns aus Naturalist/Critters & Companions/Fish of Thieves, die echtes Hunting belohnen.
- **Integration:** KubeJS Conditional-Spawn-Events (Saison via Serene Seasons, Wetter, Biom, Mondphase). Sichtungen fuettern Critterpedia/Museum. JourneyMap-Marker fuer Geruechte (Verfuegbarkeit Marker-API pruefen).
- **Quest:** Sehr hoch: pro Legendaer-Kreatur eine Geruechte->Spuren->Fang-Questkette mit Voraussetzungen (richtige Saison/Wetter).
- **Progression:** Fang legendaerer Kreaturen gibt Top-Tier-Trophaeen, Titel und schaltet hoechste Museums-/Critterpedia-Stufe frei. Endgame-Sammelziel.
- **Probleme:** Spawn-Bedingungen so eng setzen, dass selten aber nicht frustrierend. Despawn-Schutz fuer seltene Mobs. Abhaengig von Mob-Verfuegbarkeit der genannten Mods.

### Dorfwahlen & Buergermeister-System  
*Typ: feature*

- **Nutzen:** RPG-lite-Town-Building: Spieler/Teams kandidieren fuer Aemter (Buergermeister, Marktmeister, Festkomitee). Gewaehlte Spieler erhalten Verwaltungsrechte und Verantwortung fuer Dorf-Entscheidungen (welches Festival, welche Bauprojekte).
- **Integration:** FTB Teams als Fraktions-Basis; KubeJS-Abstimmungs-GUI/Schild-Voting; gewonnene Aemter geben FTB-Chunks/Essentials-Rechte. Town-Talk-NPCs reagieren auf Amtsinhaber.
- **Quest:** Mittel: 'Wahlkampf'-Quests (Dorfaufgaben erfuellen fuer Stimmen), Amtsperioden-Quests.
- **Progression:** Aemter geben funktionale Vorteile (Steuerung von Events, Zugang zu Gemeindekasse aus Smaragden). Soziales Meta-Progression auf SMP-Ebene.
- **Probleme:** Stark sozial/Multiplayer-abhaengig, auf kleinem SMP evtl. wenig kompetitiv. Voting-Mechanik komplett Custom (KubeJS). Missbrauchs-/Griefing-Schutz noetig.

### Erfolgs-/Lebenswerk-System ('Grandpa's Evaluation')  
*Typ: system*

- **Nutzen:** Stardew-Grandpa-Evaluation-Adaption: ein periodisches Gesamt-Rating des Spielers/Dorfs ueber alle Saeulen (Farm-Groesse, Museumsfortschritt, Freundschaften, Wettbewerbssiege, Town-Building) mit zeremonieller Bewertung nach z. B. einem Ingame-Jahr.
- **Integration:** KubeJS aggregiert Flags aus allen anderen Systemen (Museum, Bundles, Festivals, NPC-Freundschaft) zu einem Punktwert; FTB-Quests-Reward-Chapter als 'Zeugnis'.
- **Quest:** Hoch: dient als Meta-Quest-Dach, das alle Sub-Systeme bündelt; gestaffelte Bewertungs-Stufen als Quests.
- **Progression:** Top-Bewertung gibt prestigereiche kosmetische End-Belohnungen (Statue, Titel, einzigartiger Deko-Block). Langfrist-Nordstern fuer den ganzen Pack.
- **Probleme:** Erfordert, dass die anderen Systeme bereits Flags setzen -> Abhaengigkeitsketten sauber halten. Rein KubeJS, aber Aggregations-Scripting umfangreich.

### NPC-Freundschafts- & Geschenk-System  
*Typ: system*

- **Nutzen:** Stardew/Animal-Crossing-Herzstueck: Dorf-NPCs (MineColonies-Buerger, Guard/Easy Villagers, Town-Talk-Charaktere) haben Vorlieben; taegliche Geschenke (Farmer's-Delight-Gerichte, Blumen) erhoehen Freundschaftslevel.
- **Integration:** KubeJS Villager-Right-Click-mit-Item-Event prueft Vorliebe-Tabelle, erhoeht Per-Player-NPC-Score; Town Talk liefert Dialog-Flavour. What Are They Up To zeigt NPC-Routinen.
- **Quest:** Sehr hoch: pro NPC eine Freundschafts-Questreihe mit Belohnungen bei Herz-Meilensteinen; 'Heart Events' als getriggerte Mini-Szenen.
- **Progression:** Hoehere Freundschaft schaltet bessere Trades, Rezepte, Geschenke der NPCs und Dorf-Buffs frei. Tiefe Langzeit-Beziehungsschleife.
- **Probleme:** Vanilla/MineColonies-Villager haben keine native Identitaet -> NPCs muessen per Custom-NBT/Name markiert werden. Sehr scripting-intensiv. Dialog-System nur ueber Town Talk begrenzt.

### Schwarzes Brett / Quest-Board mit taeglichen Auftraegen  
*Typ: feature*

- **Nutzen:** Stardew-'Help-Wanted'-Board im Dorf: ein physisches Brett generiert taeglich rotierende Liefer-/Sammel-/Jagd-Auftraege von NPCs gegen Smaragde und Reputation.
- **Integration:** KubeJS generiert taeglich (Kalender-Tick) randomisierte Auftraege aus Pools; FTB Quests als Auftrags-UI mit Item-Abgabe. Belohnung in Vanilla-Smaragden (passt zur Coin-freien Wirtschaft).
- **Quest:** Sehr hoch und repetierbar: unendlicher Nachschub an taeglichen Quests, hauptsaechlicher taeglicher Gameplay-Loop.
- **Progression:** Smaragd-Einnahmequelle -> treibt Vanilla-Villager-Handel; Reputation schaltet schwierigere, lukrativere Auftraege frei. Konstanter Daily-Driver.
- **Probleme:** FTB Quests hat keine native taegliche Randomisierung -> KubeJS muss Quests dynamisch befuellen/zuruecksetzen (technisch anspruchsvoll, ggf. Repeatable-Quests als Workaround).

### Custom-Mod: 'Cozy Festivals & Calendar' (eigener NeoForge-Mod)  
*Typ: custom-mod*

- **Nutzen:** Falls KubeJS fuer Kalender/Festival-Scheduling/persistente Per-Player-Sammlungen an Grenzen stoesst, ein schlanker hauseigener Mod, der eine robuste Kalender-API, Event-Bus-Hooks und ein Sammlungs-Capability-System bereitstellt — als Fundament fuer alle obigen Features.
- **Integration:** Stellt Datapack-/KubeJS-bindbare Events bereit (onSeasonChange, onFestivalStart, onCollectionEntry); andere Features konsumieren diese statt eigener fragiler Tick-Logik. NeoForge 21.1.x Capabilities fuer Persistenz.
- **Quest:** Indirekt sehr hoch: macht alle zeit-/sammlungsbasierten Quests zuverlaessig.
- **Progression:** Solides, performantes Fundament fuer Langzeit-Progression statt KubeJS-Tick-Hacks.
- **Probleme:** Eigenentwicklung = Wartungs-/Update-Aufwand bei MC/NeoForge-Updates. Nur sinnvoll wenn KubeJS-Loesungen nachweislich nicht reichen. Java-Entwicklungsressourcen noetig.

### Glueckslos / Dorf-Tombola (Festival-Minispiel)  
*Typ: feature*

- **Nutzen:** Animal-Crossing-Tombola-Stil: waehrend Festivals kann man mit Smaragden Lose ziehen und kosmetische/seltene Preise gewinnen — sorgt fuer Festival-Spannung und ist ein Smaragd-Sink.
- **Integration:** KubeJS-Loot-Table-gestuetzte Ziehung an einem 'Tombola-Block' (Supplementaries/Custom); nur waehrend Festival-Flag aktiv. Preise aus Deko-Mods (Chipped, Bells & Whistles, Macaw's).
- **Quest:** Niedrig-mittel: 'Nimm an der Tombola teil'-Quest, Sammelquest fuer alle Tombola-exklusiven Preise.
- **Progression:** Kosmetische Exklusiv-Items als Sammelanreiz; Smaragd-Sink balanciert die Wirtschaft. Bewusst kein P2W (nur Deko).
- **Probleme:** Gambling-Mechanik sensibel balancieren (Frust bei Pech). Loot-Pool gegen RNG-Frust mit Pity-System (KubeJS) absichern. Klar als rein kosmetisch halten.

### Saisonale Dorf-Dekoration (Auto-Decorating)  
*Typ: feature*

- **Nutzen:** Animal-Crossing-Feeling: das Dorf schmueckt sich automatisch je Saison/Festival um — Herbstlaub und Kuerbisse, Winter-Lichterketten, Fruehlingsblumen, Sommer-Strandschmuck — fuer sofort spuerbare Atmosphaere.
- **Integration:** Kalender-Scheduler triggert KubeJS, das vordefinierte Deko-Bloecke (Bells & Whistles, Supplementaries Festivitaet, Macaw's, Let's Do Beachparty) an markierten Dorf-Positionen tauscht.
- **Quest:** Niedrig: optionale 'Hilf beim Schmuecken'-Quest fuer kosmetische Belohnung.
- **Progression:** Primaer atmosphaerisch; freischaltbare zusaetzliche Deko-Sets als Belohnung aus anderen Systemen.
- **Probleme:** Block-Swapping an festen Koordinaten ist welt-spezifisch und bricht bei Dorf-Umbau. Robuster ueber markierte Deko-Frames statt harte Koordinaten. Rein kosmetisch, geringes Risiko.

### Reputations-/Titel-System (Dorf-Ansehen)  
*Typ: system*

- **Nutzen:** RPG-lite-Querschnitt: ein sichtbarer Reputationswert (und Titel wie 'Lehrling' -> 'Dorf-Held'), der aus allen Aktivitaeten (Quests, Spenden, Wettbewerbe, Freundschaften) waechst und das Dorf auf den Spieler reagieren laesst.
- **Integration:** KubeJS-Scoreboard/PlayerData sammelt Punkte aus anderen Systemen; Titel via FTB Essentials/Nickname oder Town-Talk-Reaktionen. Haendlerpreise koennen mit Ruf skalieren.
- **Quest:** Mittel: Titel-Aufstiege als Meilenstein-Quests; ruf-gated Quests fuer hoehere Stufen.
- **Progression:** Hoeherer Ruf = bessere Trades, Rabatte, exklusive Quests/Bereiche. Klassischer RPG-Progressions-Backbone, der alle Systeme verbindet.
- **Probleme:** Doppelzaehlung vermeiden (Quest gibt Ruf, der wieder Quests freischaltet -> Loops). Balance ueber alle Quellen. Reines KubeJS-Aggregat.

### Sternennacht-Wunschbrunnen (Wishing Well / Fortune)  
*Typ: feature*

- **Nutzen:** Cozy-Mystik-Feature: ein Dorfbrunnen, in den man nachts Smaragde/Items wirft, um zufaellige Segnungen (temporaere Buffs, Glueck beim Angeln/Ernten, Wetteraenderung) zu erhalten — atmosphaerisch und nuetzlich.
- **Integration:** KubeJS Item-Toss-in-Water-Detection an einem Brunnen-Block; gewaehrt zeitlich begrenzte Effekte. Synergie mit Angelturnier/Erntewettbewerb (Glücks-Buff).
- **Quest:** Niedrig-mittel: Entdeckungs-Quest des Brunnens; seltene 'grosser Wunsch'-Quest.
- **Progression:** Sanfte Buff-Quelle als Smaragd-Sink; tiefere Wuensche bei hoeherem Ruf. Kein Pflicht-Grind, sondern Cozy-Bonus.
- **Probleme:** Buff-Balance (kein Dauer-Glueck-Exploit, Cooldown via KubeJS). Wetteraenderung serverweit klaeren. Rein scriptbar.

### Persoenliches Tagebuch / Erinnerungsbuch  
*Typ: item*

- **Nutzen:** Cozy-Animal-Crossing-Detail: ein automatisch gefuehrtes Tagebuch, das Meilensteine festhaelt ('Erster legendaerer Fisch', 'Museum 50 %', 'Buergermeister gewaehlt') und dem Spieler eine erzaehlerische Reise-Chronik gibt.
- **Integration:** KubeJS schreibt bei System-Events Eintraege in ein beschreibbares Buch-Item (Supplementaries Quill/Custom-Written-Book) oder eine FTB-Quest-Chronik-Seite.
- **Quest:** Niedrig: dient als Belohnungs-/Erinnerungsanzeige fuer abgeschlossene Quests aller anderen Systeme.
- **Progression:** Visualisiert Gesamt-Progression emotional; motiviert Completionism ohne harte Mechanik.
- **Probleme:** Dynamisch generierte Buchseiten in MC sind eingeschraenkt (Written-Book-Editier-API begrenzt). MVP evtl. nur als statische Achievement-Liste. Geringes Risiko.

### Saison-Pass / Almanach mit gestaffelten Belohnungen  
*Typ: feature*

- **Nutzen:** Strukturierte Saison-Progression: pro Serene-Seasons-Saison ein 'Almanach' mit ~10 Aufgaben (saisonale Crops anbauen, Saison-Fische fangen, am Festival teilnehmen), der bei Erfuellung gestaffelte Belohnungen ausschuettet — gibt jeder Saison klare Ziele.
- **Integration:** FTB-Quests-Chapter pro Saison, vom Kalender-Scheduler aktiviert/deaktiviert; KubeJS setzt Saison-Flags. Belohnungen aus dem gesamten Deko-/Food-/Saatgut-Pool.
- **Quest:** Sehr hoch: ist im Kern ein rotierendes Quest-System mit 4 Saison-Kapiteln, das jaehrlich neu durchlaufen wird.
- **Progression:** Wiederkehrende Saisonziele halten Spieler zyklisch aktiv; spaetere Jahre koennen schwerere Almanach-Stufen freischalten.
- **Probleme:** Quests saisonal sauber aktivieren/zuruecksetzen (FTB-Quests + KubeJS-Flag-Steuerung). Inhalts-Authoring fuer 4 Saisons. Ueberschneidung mit Festivals klar abgrenzen.


## custom-content (26)

### Heimatherz (Town Heart) — wachsendes Stadtzentrum-Multiblock  
*Typ: custom-mod*

- **Nutzen:** Ein platzierbarer Multiblock-Kern (Brunnen/Glockenturm), der die SMP-Stadt repräsentiert und sichtbar in Tiers wächst (Stufe 1-5), je nachdem wie viele Bewohner, Gebäude und Verschönerungen in einem Radius existieren. Gibt der Server-Gemeinschaft ein gemeinsames Fortschrittsziel statt nur individuellem Grind.
- **Integration:** Liest MineColonies-Kolonie-Level und FTB-Chunks-Claims im Umkreis aus; höhere Tiers schalten KubeJS-getriggerte Buffs (z.B. schnelleres Pflanzenwachstum im Stadtgebiet via Serene-Seasons-freundlichem Modifier) frei. Create-Anbindung: Glockenturm kann per Steam'n'Rails-Glocke/Bells&Whistles automatisch läuten.
- **Quest:** FTB-Quest-Linie 'Aus dem Nichts ein Dorf' mit Meilensteinen pro Tier; jede Stufe gibt eine Town-Talk-Ankündigung und neue Händler.
- **Progression:** Sehr hoch — fünf klar gestaffelte Stufen, gemeinschaftliches Langzeitziel, schaltet Stadt-weite Boni und neue NPCs frei.
- **Probleme:** Performance bei großem Scan-Radius (cachen, nur periodisch scannen). Kompatibilität mit MineColonies-Claims muss sauber sein, sonst Doppel-Ownership-Konflikte mit FTB-Chunks.

### Dorfbewohner-Beziehungssystem (Heart Levels & Geschenke)  
*Typ: custom-mod*

- **Nutzen:** Echte Stardew-artige Beziehungen zu Villagern/NPCs: Herzlevel pro NPC, Lieblings-/Hass-Geschenke, tägliche Gesprächs-Cooldowns, Freundschafts-Belohnungen. Macht NPCs zu echten Charakteren statt Trade-Automaten.
- **Integration:** Setzt auf Vanilla-Villager + Guard Villagers + Easy Villagers auf, ergänzt via Town Talk/What Are They Up To um Dialog-Hooks. Geschenke nutzen Farmer's-Delight- und Pam's-Gerichte als Lieblingsitems; Lieblingsgeschenk-Daten via KubeJS-Datapack editierbar.
- **Quest:** Pro NPC eine Freundschafts-Questkette ('Bringe dem Bäcker 3 Apfelkuchen'); Heart-Events als FTB-Quest-Trigger.
- **Progression:** Hoch — Herzlevel 1-10 pro NPC, schaltet Rezepte, Rabatte, Hofhelfer und Heirats-Mechanik (siehe eigener Vorschlag) frei.
- **Probleme:** NPC-Identität persistent halten (Villager despawnen/sterben). Datenmenge bei vielen Spielern × vielen NPCs. UI für Herzlevel muss intuitiv sein.

### Heirat & Mitbewohner (Spouse NPC)  
*Typ: custom-mod*

- **Nutzen:** Spieler können einen Lieblings-NPC (bei max. Herzlevel) heiraten; der Ehepartner zieht ins Spielerhaus, gibt tägliche Buffs, Geschenke und hilft bei Hofarbeit. Klassischer Cozy-RPG-Endgame-Anker.
- **Integration:** Baut direkt auf dem Beziehungssystem auf. Ehepartner kann als Smarter-Farmers-/Hofhelfer fungieren und Sophisticated-Storage-Kisten sortieren. Hochzeit als Event am Heimatherz-Multiblock.
- **Quest:** Heirats-Quest mit Ring-Crafting (eigenes Item), Hochzeitsvorbereitung, Einladung der Stadt.
- **Progression:** Hoch — definiertes soziales Endgame, schaltet Partner-Buffs und gemeinsame Hof-Boni frei.
- **Probleme:** Mehrspieler-Eifersucht (mehrere Spieler, ein NPC) — pro Spieler instanzieren oder limitieren. Pfadfindung des Partners im Spielerhaus.

### Saisonale Stadtfeste (Festival-Events)  
*Typ: custom-mod*

- **Nutzen:** Wiederkehrende Feste gebunden an Serene Seasons (Frühlingsblüten-Fest, Erntedank im Herbst, Winter-Lichterfest), bei denen die Stadt sich dekoriert, NPCs sich versammeln, Mini-Wettbewerbe laufen (Größtes Gemüse, Angel-Contest) und Sonderhändler kommen.
- **Integration:** Trigger über Serene-Seasons-Datum; Dekoration via Supplementaries/Bells&Whistles/Festive-Items. Angel-Contest nutzt Fish of Thieves/Aquaculture; Gemüse-Contest nutzt Pam's/HarvestCraft-Größenwerte.
- **Quest:** Jedes Fest ist eine zeitlich begrenzte FTB-Quest mit exklusiven Belohnungen; Wettbewerbsplatzierung gibt Festival-Tickets.
- **Progression:** Mittel-hoch — Festival-Tickets als eigene Sammelwährung für kosmetische und nützliche Exklusiv-Items, jährlicher Wiederholungs-Loop.
- **Probleme:** Server-Zeitsynchronisation und Spieler-Timezone-Erwartungen. Event-Scheduling muss bei Server-Downtime robust sein.

### Hof-Saatgut-Veredelung & Pflanzen-Genetik (Seed Breeding)  
*Typ: custom-mod*

- **Nutzen:** Spieler züchten über Generationen verbesserte Saatgut-Varianten (Qualität, Ertrag, Wachstumsgeschwindigkeit, Saison-Toleranz) — ein cozy Genetik-Minispiel, das dem Farming Langzeittiefe gibt, ohne Mystical-Agriculture-Power-Creep.
- **Integration:** Wirkt auf Pam's HarvestCraft- und Farmer's-Delight-Crops. Hochwertiges Saatgut steckbar in Create-Mechanical-Harvester/Deployer-Setups. Qualitätsstufen sichtbar via JEI-Tooltip.
- **Quest:** Forscher-NPC gibt Quests 'Züchte eine Sterne-Tomate' mit Belohnung neuer Saatphänotypen.
- **Progression:** Sehr hoch — mehrstufige Qualitäts- und Eigenschaftsachsen, langfristiges Min-Maxing, koppelbar an Markt-Preise.
- **Probleme:** Balancing gegen vorhandene Crop-Vielfalt (Every Compat). Genetik-Datenmodell muss kompakt im ItemStack-NBT bleiben. UI-Verständlichkeit.

### Crop-Qualitätssterne & Gourmet-Boni  
*Typ: custom-mod*

- **Nutzen:** Jede geerntete Frucht bekommt einen Qualitätsstern (Normal/Silber/Gold/Iridium-Äquivalent) abhängig von Bodenpflege, Bewässerung, Saison und Saatgut. Höhere Qualität = mehr Verkaufswert und stärkere Food-Buffs. Der zentrale Stardew-Hook, der im Pack noch fehlt.
- **Integration:** Hängt an Pam's/Farmer's-Delight-Crops; Qualität fließt in Let's-Do-Vinery-Wein und Farmer's-Delight-Gerichte als Vererbung weiter. Create-Mechanical-Harvester respektiert Qualität.
- **Quest:** 'Liefere 10 Gold-Karotten an den Wirt' — perfekter Liefer-Quest-Stoff.
- **Progression:** Hoch — Qualitätsleiter pro Crop, treibt Bodenverbesserung, Bewässerungs- und Genetik-Investitionen.
- **Probleme:** NBT-Explosion bei Stacking (Qualität trennt Stacks). Muss mit AppleSkin/Nahrungs-Tooltips harmonieren.

### Hof-Tier-Zuneigung & Produktqualität (Animal Husbandry+)  
*Typ: custom-mod*

- **Nutzen:** Nutztiere (Vanilla + Naturalist/Critters) bekommen Zuneigung durch tägliches Streicheln, Füttern und einen Stall-Komfort-Wert; glückliche Tiere geben hochwertigere/häufigere Produkte (große Eier, Qualitätsmilch). Cozy Tierpflege als tägliche Routine.
- **Integration:** Erweitert Vanilla-Tiere und Critters&Companions; Stall-Komfort liest umliegende Handcrafted/Another-Furniture/Macaw-Blöcke. Produkte fließen in Farmer's-Delight/Let's-Do-Meadow-Rezepte.
- **Quest:** 'Bring ein Tier auf max. Zuneigung', 'Produziere ein Riesen-Ei' als Sammel-Quests.
- **Progression:** Mittel-hoch — Zuneigungsstufen + Produktqualitätsstufen, belohnt tägliche Pflege-Loops.
- **Probleme:** Tägliche Interaktions-Tracking pro Mob (NBT). Balance gegen automatisierte Create-Farmen, die Streicheln umgehen würden.

### Sammel-Almanach / Museum-Spenden-System  
*Typ: custom-mod*

- **Nutzen:** Ein gebäudegebundenes Museum (oder Almanach-Buch), in dem Spieler gefangene Fische, Insekten, gefundene Artefakte/Fossilien und angebaute Crops 'spenden'/registrieren. Klassischer Animal-Crossing/Stardew-Sammelloop mit Vervollständigungs-Belohnungen.
- **Integration:** Sammelt aus Fish of Thieves, Aquaculture, Naturalist, Critters & Companions und Pam's-Crops. Artefakte koppelbar an Artifacts-Mod-Funde. Museum als Stadtgebäude (Domum Ornamentum/Structurize).
- **Quest:** Jede Sammelkategorie ist eine eigene Quest-Linie; Komplettierung gibt Trophäen und Titel.
- **Progression:** Sehr hoch — hunderte Sammeleinträge, langfristiger Completionist-Loop, schaltet Museum-Erweiterungen frei.
- **Probleme:** Registrierung aller existierenden Items (großer Datapack); Pflege bei Mod-Updates. Mehrspieler: gemeinsames vs. persönliches Museum entscheiden.

### Angel-Kompendium mit Bissfenstern & Wetter/Saison-Fischen  
*Typ: custom-mod*

- **Nutzen:** Vertieft Angeln zu einem echten Stardew-Minispiel: Fischarten haben Tageszeit-, Wetter- und Saison-Fenster, Seltenheitsstufen und ein aktives Einhol-Geschick. Macht das vorhandene Fish of Thieves/Aquaculture-Material zu einem Sammel- und Skill-Loop.
- **Integration:** Erweitert Fish of Thieves + Aquaculture-Loot-Tabellen um Bedingungen via Serene Seasons. Fänge spendbar ins Museum (siehe Almanach). JEI-Anzeige der Fangbedingungen.
- **Quest:** 'Fange den Legendären Wels bei Regen im Herbst' — Signatur-Quests pro Rarität.
- **Progression:** Hoch — Anglerlevel + bessere Ruten/Köder (eigene Items), seltene Fische als Endgame.
- **Probleme:** Aktives Minispiel-UI auf NeoForge sauber umsetzen. Konflikte mit Aquaculture-eigenem Loot vermeiden (überschreiben statt doppeln).

### Skill-Berufe-System (Farming/Mining/Fishing/Foraging/Combat)  
*Typ: custom-mod*

- **Nutzen:** Leichtes RPG-Skill-System: fünf Berufe leveln durch zugehörige Aktivität, geben passive Boni (mehr Ernteertrag, schnelleres Abbauen) und schalten kleine Perks frei. Liefert die 'RPG-lite'-Säule der Vision mit cozy, nicht-grindigem Feel.
- **Integration:** Skill-XP aus Pam's/Farmer's-Delight-Ernte, FTB-Ultimine-Mining, Angel-System, Naturalist-Foraging. Perks als KubeJS-Buffs. Anzeige via eigenem HUD oder Jade-Integration.
- **Quest:** Berufs-Meister-NPCs geben Aufstiegs-Quests; Perk-Wahl als Quest-Belohnung.
- **Progression:** Sehr hoch — fünf parallele Levelleitern mit Perk-Bäumen, kontinuierlicher Fortschritt über die gesamte Spielzeit.
- **Probleme:** Balance gegen Create-Automatisierung (automatisierte Ernte sollte weniger XP geben). Skill-Daten pro Spieler persistent + serverseitig.

### Lebenskraft-Tagesenergie (Stamina, optional)  
*Typ: custom-mod*

- **Nutzen:** Optionales Stamina/Energie-System à la Stardew: anstrengende Arbeit (Hacken, Abbauen, Angeln) verbraucht Energie, Schlafen und gutes Essen stellen sie wieder her — erzeugt den cozy Tagesrhythmus 'arbeiten, essen, schlafen'.
- **Integration:** Energie-Wiederherstellung skaliert mit Farmer's-Delight-/Pam's-Gericht-Qualität und Comforts-Schlafsäcken. Serene-Seasons-Tageslänge taktet den Rhythmus.
- **Quest:** Tutorial-Quest 'Iss eine warme Mahlzeit, bevor du erschöpfst'; Energie-Trank-Rezepte als Belohnung.
- **Progression:** Mittel — Energie-Maximum steigt mit Farming-Skill; eher Atmosphäre als Hauptprogression.
- **Probleme:** Kann als nervig empfunden werden — unbedingt per Config/Server-Setting abschaltbar und großzügig balancen. Mehrspieler-Schlaf-Sync.

### Marktstand & dynamische Verkaufspreise (Shipping Bin)  
*Typ: custom-mod*

- **Nutzen:** Ein 'Versandkiste'-Block, in den Spieler Waren legen; über Nacht werden sie zu Smaragden verkauft. Preise schwanken leicht nach Angebot/Nachfrage und Saison — bringt die fehlende tägliche Stardew-Einnahme-Schleife, passend zur Vanilla-Smaragd-Wirtschaft (kein Coin-Mod).
- **Integration:** Nutzt Smaragde als Währung (Vision-konform). Qualitätssterne und Crop-Genetik erhöhen Verkaufswert; Saison-Nachfrage über Serene Seasons. Versandkiste optisch via Supplementaries/Handcrafted.
- **Quest:** 'Verdiene 1000 Smaragde durch Versand' Meilenstein-Quests; Marktnachfrage-Events als zeitbegrenzte Quests.
- **Progression:** Sehr hoch — Kernschleife der Wirtschaft, treibt Farming- und Qualitäts-Investitionen, Geld als Tor zu Stadtausbau.
- **Probleme:** Smaragd-Inflation auf SMP — Preise und Tagescaps sorgfältig balancen. Doppelnutzung mit Villager-Trades vermeiden (klare Rollen).

### Sprinkler & smarte Bewässerung (Cozy-Tier vor Create)  
*Typ: custom-mod*

- **Nutzen:** Gestaffelte Sprinkler-Blöcke (Holz/Kupfer/Messing), die Felder im Umkreis automatisch feucht halten — der early-/mid-game Komfort-Schritt zwischen Handgießen und voller Create-Automatisierung, ein Stardew-Kernitem.
- **Integration:** Messing-Sprinkler als Bindeglied zu Create (Brass-Casing-Crafting, optional Create-Fluid-gespeist). Hält Vanilla-Farmland und Pam's-Crops feucht; respektiert Crop-Qualitäts-Bewässerungsbonus.
- **Quest:** 'Automatisiere ein 9x9-Feld' Komfort-Quest; Sprinkler-Blueprints als Quest-Belohnung.
- **Progression:** Hoch — drei Reichweiten-Tiers als klare Upgrade-Leiter, Brücke in den Create-Tech-Tree.
- **Probleme:** Performance bei vielen Sprinklern (Feucht-Updates batchen). Balance gegen Create-Mechanical-Harvester, damit beide Wege sinnvoll bleiben.

### Geschenkbox-Post & Brieffreund-NPCs (Animal-Crossing-Mail)  
*Typ: custom-mod*

- **Nutzen:** Ein Briefkasten-Block am Spielerhaus: NPCs schicken Briefe, Geschenke und Aufträge; Spieler können untereinander und an NPCs Pakete senden. Animal-Crossing-Wärme und sozialer Klebstoff fürs SMP.
- **Integration:** Briefkasten via Supplementaries/Handcrafted-Optik. Mail-Trigger aus Beziehungssystem (Heart-Events) und Festival-System. Geschenke nutzen das gesamte Food-/Deko-Itemset.
- **Quest:** Tägliche/wöchentliche Brief-Quests von NPCs; Versand-Aufträge als wiederkehrender Content.
- **Progression:** Mittel — stetiger sozialer Loop, schaltet seltene Briefmarken/Deko frei; kein harter Power-Gate.
- **Probleme:** Offline-Mehrspieler-Zustellung (Mail muss persistieren). Spam-Vermeidung bei NPC-Briefen (Cooldowns).

### Stadt-Verschönerungs-Punkte (Town Beautification / Feng-Shui)  
*Typ: custom-mod*

- **Nutzen:** Platzierte Deko (Blumen, Bänke, Laternen, Wege) zählt zu einem Stadt-Schönheitswert, der NPC-Stimmung, Tourismus-Besucher und Festival-Qualität beeinflusst. Belohnt das Verschönern, das im Pack viele Deko-Mods ermöglichen, mit echtem mechanischem Sinn.
- **Integration:** Scannt Macaw's-Paths, Supplementaries-, Bells&Whistles-, Chipped- und Another-Furniture-Blöcke. Speist Heimatherz-Tier und Festival-System. Tourismus-NPCs als neue Besucher.
- **Quest:** 'Erreiche Schönheitsstufe Gold im Marktviertel' — Bau-/Deko-Quests, die Kreativität belohnen.
- **Progression:** Hoch — gestaffelte Schönheitsstufen pro Bezirk, koppelt Bauen an Stadtwachstum und Boni.
- **Probleme:** Block-Scan-Performance (auf Chunk-Events cachen). Punktevergabe-Tabelle pflegeintensiv bei vielen Deko-Mods.

### Wandernde Händler & Karawanen-Stationen  
*Typ: custom-mod*

- **Nutzen:** Periodisch erscheinende fahrende Händler (Stardew-Cart / AC-Redd), die seltene Saatgüter, Deko und Sammelobjekte gegen Smaragde anbieten — gibt Anreiz, immer wieder in die Stadt zu kommen, und einen Bezug seltener Items ohne Creative.
- **Integration:** Karren als Steam'n'Rails-Waggon oder Create-Contraption andockbar; Inventar zieht aus Crop-Genetik (seltene Saaten), Museum-Belohnungen und Festival-Exklusiva. Ankunft per Town-Talk angekündigt.
- **Quest:** 'Kaufe die seltene Sternfrucht-Saat vom Wanderhändler'; Karawanen-Eskort-Mini-Quest.
- **Progression:** Mittel-hoch — rotierendes Sortiment als Sammel- und Geldsenke-Loop.
- **Probleme:** Spawn-Timing fair für alle SMP-Spieler. Wirtschaftsbalance des Sortiments (keine OP-Items für billig).

### Jahreszeiten-Schrein & Wetter-Gunst  
*Typ: custom-mod*

- **Nutzen:** Ein Schrein-Multiblock, an dem Spieler Crops/Items opfern, um kleine Saison-/Wetter-Gefälligkeiten zu erbitten (Regen für die Felder, klare Ernte-Tage). Cozy, leicht magischer Naturbezug ohne harte Tech-Magie.
- **Integration:** Interagiert mit Serene Seasons (Wetter-/Saison-Hooks). Opfergaben skalieren mit Crop-Qualität. Optik via Supplementaries/Ars-freie Deko.
- **Quest:** Saisonale Schrein-Rituale als Quests; legendäre Gunst nach großer Opfergabe.
- **Progression:** Mittel — Gunst-Stufen mit längeren/stärkeren Effekten; Begleit-Progression, kein Kernbaum.
- **Probleme:** Wetter-Manipulation muss serverweit fair sein (ein Spieler regnet allen rein). Balance gegen Farm-Automatisierung.

### Persönliche Hof-Helfer-NPCs (anstellbare Farmhands)  
*Typ: custom-mod*

- **Nutzen:** Anstellbare NPC-Helfer (gegen Tageslohn in Smaragden), die definierte Hofaufgaben übernehmen: gießen, ernten, Tiere füttern, einsammeln. Cozy Mid-Game-Entlastung, die menschlicher wirkt als reine Create-Maschinen.
- **Integration:** Ergänzt Smarter Farmers/Guard Villagers um zuweisbare Aufgaben & Lohnsystem. Helfer legen Ernte in Sophisticated-Storage. Anstellbar nach Beziehungs-Herzlevel.
- **Quest:** 'Stelle deinen ersten Farmhand ein und richte einen Arbeitsbereich ein' Tutorial-Quest.
- **Progression:** Hoch — mehr Helfer/Aufgaben-Slots mit Town-Tier; Brücke zwischen Handarbeit und Voll-Automation.
- **Probleme:** Pfadfindungs-/Performance-Last bei vielen Helfern. Überschneidung mit MineColonies-Bürgern klar abgrenzen, sonst Rollen-Verwirrung.

### Cozy-Werkzeug-Tiers mit sanftem Upgrade-Pfad  
*Typ: custom-mod*

- **Nutzen:** Eigene Farm-Werkzeug-Linie (Gießkanne, Sense, Hacke, Korb) mit Stardew-artigen Upgrades (mehr Reichweite, größerer Wasservorrat, Flächen-Ernte). Gibt dem Farming taktiles, befriedigendes Tool-Progression-Gefühl jenseits von Vanilla-Hacken.
- **Integration:** Upgrades beim Schmied-NPC gegen Erze/Smaragde; Messing-/Kupfer-Tiers binden an Create-Materialien. Flächen-Hacke harmoniert mit Sprinklern und Crop-Qualität.
- **Quest:** 'Bring dem Schmied 5 Kupferbarren für die Stahl-Gießkanne' — klassische Upgrade-Quests.
- **Progression:** Sehr hoch — mehrere Werkzeuge × mehrere Materialstufen, durchgehende greifbare Verbesserung.
- **Probleme:** Überschneidung mit Vanilla-/anderen Tools — klare Nische (Flächenwirkung) nötig. Reichweiten-Tools serverseitig validieren (Anti-Cheat).

### Schlafzimmer-Komfort & Heim-Boni (Home Sweet Home)  
*Typ: custom-mod*

- **Nutzen:** Das Spielerhaus bekommt einen Komfort-/Gemütlichkeitswert aus Möbeln, Beleuchtung und Dekoration; gut eingerichtete Häuser geben Morgen-Buffs (Wohlausgeruht, schnellere Regeneration). Belohnt das Inneneinrichten, das die vielen Möbel-Mods ermöglichen.
- **Integration:** Wertet Another Furniture, Handcrafted, Interiors, Macaw's und Comforts-Betten aus. Buff beim Aufwachen; koppelbar an Stamina-System.
- **Quest:** 'Erreiche Gemütlichkeitsstufe 3 in deinem Schlafzimmer' Einrichtungs-Quest.
- **Progression:** Mittel-hoch — Komfortstufen mit stärkeren Morgen-Buffs; belohnt Deko-Investition.
- **Probleme:** Raum-/Hausgrenzen-Erkennung ist schwierig (welche Blöcke zählen zum 'Haus'?). Block-Scan-Performance.

### Kochbuch-Meisterschaft & freischaltbare Rezepte (Recipe Mastery)  
*Typ: custom-mod*

- **Nutzen:** Rezepte (besonders Farmer's-Delight/Let's-Do/Pam's) sind anfangs gesperrt und werden durch Kochen, NPC-Geschenke, Bücherfunde und Skill-Level freigeschaltet — ein Stardew-Kochkanal-Sammelloop, der die riesige Food-Auswahl strukturiert und zum Entdecken einlädt.
- **Integration:** Hängt an die existierenden Koch-Mods (FD/Let's Do/Bountiful Fares/Ratatouille/Confectionery) — sperrt deren Rezepte hinter ein Wissens-Gate via KubeJS. Mastery-Level pro oft gekochtem Gericht gibt Qualitätsbonus.
- **Quest:** 'Schalte 20 Rezepte frei' / NPC lehrt sein Signaturgericht als Quest-Belohnung.
- **Progression:** Sehr hoch — hunderte freischaltbare Rezepte + Meisterschaftsstufen pro Gericht, riesiger Sammelhorizont.
- **Probleme:** Eingriff in viele Fremdrezepte muss sauber & abschaltbar sein. Risiko, frühes Spiel zu stark zu gaten — großzügige Start-Freischaltungen.

### Kobold-/Geisterhelfer am Hof (Cozy-Magie-Begleiter)  
*Typ: custom-mod*

- **Nutzen:** Kleine sammelbare Haushelfer-Wichtel (Junimo-/Brownie-Vibe), die man durch Pflege gewinnt und die nachts kleine Aufgaben erledigen oder Glücks-Buffs geben. Bringt charmante, kinderfreundliche Cozy-Magie ohne komplexe Tech-Magie.
- **Integration:** Begleiter-Logik ähnlich Companions Dogfolk/Critters. Beschwörbar an einem Wichtel-Häuschen-Block; Belohnungen koppelbar an Museum/Beziehungen. Optik via eigene niedliche Modelle (Fresh-Animations-kompatibel).
- **Quest:** 'Finde alle 6 Wichtel und baue ihnen ein Zuhause' — Sammel-Questkette mit Stadt-Buff als Finale.
- **Progression:** Mittel-hoch — Wichtel-Sammlung + Häuschen-Upgrades, niedlicher Completionist-Loop.
- **Probleme:** Visuelles Asset-Budget (eigene Modelle/Animationen). Begleiter-Pathing/Performance auf dem Server.

### Wildnis-Foraging-Plätze & saisonale Sammelpunkte  
*Typ: custom-mod*

- **Nutzen:** Saisonal spawnende Sammelobjekte in der Welt (Frühlingskräuter, Waldbeeren, Herbstpilze, Winterknollen) als sichtbare bückbare Items — der Stardew-Foraging-Pfeiler, der Erkundung der schönen Terralith-/Tectonic-Welt belohnt.
- **Integration:** Spawn-Tabellen nach Serene-Seasons-Saison und Terralith-Biom. Funde speisen Museum, Kochmastery und Skill-Foraging. Ergänzt Naturalist-Flora.
- **Quest:** 'Sammle jedes Frühlingskraut' Saison-Sammel-Quests; Foraging-Meister-NPC-Aufträge.
- **Progression:** Hoch — saisonaler Sammelkalender × Foraging-Skill, wiederkehrender jährlicher Loop.
- **Probleme:** Welt-Spawn-Dichte balancen (nicht zumüllen). Biom-Tag-Kompatibilität mit Terralith/Every Compat prüfen.

### Stadt-Anschlagbrett mit prozeduralen Aufträgen (Bulletin Board)  
*Typ: custom-mod*

- **Nutzen:** Ein Anschlagbrett-Block, das täglich/wöchentlich prozedurale Aufträge generiert (Liefere X, Fange Y, Baue Z) mit Smaragd-/Ruf-Belohnungen — endloser, immer frischer Quest-Nachschub jenseits der handgebauten FTB-Linien.
- **Integration:** Ergänzt FTB Quests um dynamische Daily-Quests; Aufträge ziehen aus Crops, Fischen, Gerichten und Deko des Packs. Belohnungen in Smaragden + Beziehungs-/Schönheits-Punkten.
- **Quest:** Ist selbst eine Quest-Maschine — unendlicher prozeduraler Content, koppelbar an Reputation.
- **Progression:** Hoch — täglicher Loop mit steigender Auftragsschwierigkeit nach Town-Tier/Skill.
- **Probleme:** Prozedurale Generierung muss erfüllbar & nicht repetitiv-langweilig sein. Mehrspieler: geteilte vs. persönliche Aufträge entscheiden.

### Reputations-/Ruf-System mit Titeln & Freischaltungen  
*Typ: custom-mod*

- **Nutzen:** Übergreifender Stadt-Ruf-Wert pro Spieler (aus Quests, Spenden, Festival-Teilnahme, Verschönerung), der Titel, Händler-Rabatte, neue Baupläne und exklusive Gebiete freischaltet. Das verbindende RPG-Fortschritts-Dach über allen anderen Systemen.
- **Integration:** Aggregiert Punkte aus Beziehungs-, Museum-, Festival-, Bulletin-Board- und Beautification-Systemen. Titel anzeigbar via Town Talk / Tab-Liste. Rabatte am Markt/Wanderhändler.
- **Quest:** Ruf-Meilenstein-Quests ('Werde Ehrenbürger'); hohe Ränge schalten Signatur-Quests frei.
- **Progression:** Sehr hoch — der oberste Meta-Progression-Layer, der alle Cozy-Loops zu einem Ziel bündelt.
- **Probleme:** Punkte-Quellen sorgfältig gewichten, damit kein einzelnes System dominiert. Persistente Per-Spieler-Daten auf dem Server.

### Tagebuch & Sammel-Kompendium-UI (Player Journal)  
*Typ: custom-mod*

- **Nutzen:** Ein In-Game-Tagebuch/Buch-UI, das alle Cozy-Systeme bündelt: NPC-Herzlevel, Museum-Fortschritt, Rezept-Mastery, Skill-Level, Ruf, aktive Aufträge und Festival-Kalender. Gibt dem Spieler die Stardew-typische zentrale Übersicht und reduziert Verwirrung bei vielen Systemen.
- **Integration:** Liest Daten aus allen oben genannten Custom-Systemen; ergänzt JourneyMap/FTB-Quests als 'Lebens'-Übersicht statt Karten/Tech. Aufrufbar per Hotkey.
- **Quest:** Onboarding-Quest 'Öffne dein Tagebuch'; Kompendium-Komplettierung als Meta-Achievement.
- **Progression:** Mittel — selbst keine Progression, aber macht alle anderen Progressionen sichtbar & motivierend (entscheidend für Bindung).
- **Probleme:** UI-Aufwand und Datenaggregation aus vielen Quellen. Muss bei abgeschalteten Einzelsystemen graceful degradieren.


## farming-mods (32)

### Croptopia  
*Typ: mod*

- **Nutzen:** Fuegt 58 neue Crops, 26 Obstbaeume und ueber 250 Lebensmittel/Rezepte hinzu (Reis, Kaffee, Trauben, Zitrus, Nuesse, Saaten). Riesige Vielfalt fuer ein Stardew-artiges Gefuehl. Verifiziert: croptopia-neoforge-1.21.1-4.2.4.jar auf CurseForge.
- **Integration:** Bestens kompatibel mit Farmer's Delight und Let's Do Vinery (eigene Compats existieren, z.B. Farmer's Croptopia, Croptopia Delight). Erweitert Pam's HarvestCraft sinnvoll statt zu kollidieren; Crops/Tags ueberlappen aber teils mit Pam's - via KubeJS harmonisieren.
- **Quest:** Sehr hoch: Sammel-Quests fuer jede der 58 Crops/26 Baeume, Kochbuch-Questline, regionale Anbau-Ketten (Tropisch/Temperiert) als FTB-Quest-Kapitel.
- **Progression:** Crops haben Biom-Anforderungen und Verarbeitungsstufen (Pflanze->Frucht->verarbeitetes Food), gut fuer gestaffelte Freischaltung von Rezepten und Kochstationen.
- **Probleme:** Inhaltlicher Overlap mit Pam's HarvestCraft 2 (doppelte Crops/Foods) - JEI wird unuebersichtlich, Tag-Konflikte moeglich. Empfehlung: per KubeJS Duplikate ausblenden oder eine der beiden Crop-Quellen kuratieren. Grosser Content-Umfang erhoeht Registry-Last.

### Productive Bees  
*Typ: mod*

- **Nutzen:** Vollwertiges Imkerei-System: Resource-Bienen, fortgeschrittene Beuten, Zentrifuge, Honeycombs fuer Ressourcen, Zucht/Mutation neuer Bienenarten. Verifiziert: productivebees-1.21.1-13.13.5.jar.
- **Integration:** Ergaenzt das Farming-Theme um Imkerei, das im Pack noch komplett fehlt. Honig/Waben fliessen in Farmer's Delight & Let's Do Herbal Brews Rezepte; Sophisticated Storage lagert die vielen Comb-Typen.
- **Quest:** Hoch: Bienen-Zuchtbaum als FTB-Questline (Basisbiene -> spezialisierte Bienen), Honig-Sammlung, Beuten-Ausbau-Stufen.
- **Progression:** Klares Tech-Tree-Gefuehl durch Bienenmutation und Beuten-Upgrades; passt zur Create-Automatisierung (Honig-Verarbeitung).
- **Probleme:** Kann mit Vanilla-Bienen-Tags interagieren; viele Item-Eintraege belasten JEI. Balancing noetig, damit Resource-Bienen nicht das Create-Mining trivialisieren - ggf. selten/teuer halten.

### Aquaculture 2  
*Typ: mod*

- **Nutzen:** Erweitert Angeln massiv: ueber 30 biomspezifische Fische, neue Ruten mit Haken/Koeder/Schnur, Tackle Box, Fisch-Filets und Kochzutaten. Verifiziert: Aquaculture-1.21.1-2.7.19.jar (NeoForge-only).
- **Integration:** Liefert Fisch fuer Farmer's Delight, Let's Do Beachparty und Crabber's Delight; ergaenzt Fish of Thieves (kosmetische Fische) um nutzbare Angel-Mechanik. Aquaculture ist laut Memory bereits drin? Pruefen - falls nur 'Aquaculture'-Delight gemeint war, ist die Basis-Mod hier der eigentliche Angel-Content.
- **Quest:** Hoch: Angel-Almanach/Fischlexikon-Quests, seltene Fische als Sammel-Trophaeen, Ruten-Upgrade-Questline.
- **Progression:** Ruten-Modifikatoren (Haken, Koeder, Schnur) bieten craftbare Upgrade-Stufen; Neptune's Bounty als Endgame-Belohnung.
- **Probleme:** WICHTIG: Memory listet 'Aquaculture' evtl. schon als enthalten - Doppelung pruefen. Falls schon drin, diesen Vorschlag streichen. Sonst Overlap mit Fish of Thieves bei Fisch-Items (kosmetisch vs. nutzbar) ist gering.

### Sushi Go Crafting  
*Typ: mod*

- **Nutzen:** Dediziertes Sushi-Kochsystem mit Entdeckungs-Minispiel: Reis, Algen, Fisch zu Sushi-Rollen mit besonderen Food-Effekten. Verifiziert fuer 1.21.1 NeoForge auf CurseForge.
- **Integration:** Nutzt Fisch aus Aquaculture/Fish of Thieves und Reis aus Croptopia; ergaenzt Asia-Kueche, die in Farmer's/Let's Do fehlt. Eigene Kochstation neben Farmer's Delight Cooking Pot.
- **Quest:** Mittel-hoch: Sushi-Meister-Questline, Rezept-Entdeckung als Sammel-Achievement.
- **Progression:** Minispiel-Mechanik gibt Skill-Progression (bessere Rolle = bessere Effekte); craftbare Werkzeuge als Stufen.
- **Probleme:** Eigenes Kochsystem parallel zu Farmer's Delight kann redundant wirken; Effekt-Balancing noetig, damit Buffs nicht zu stark sind.

### Cooking for Blockheads  
*Typ: mod*

- **Nutzen:** Multiblock-Kueche mit Kochbuch, das automatisch alle craftbaren Rezepte aus vorhandenen Zutaten anzeigt; Kuehlschrank, Toaster, Ofen, Spuele. Verifiziert: cookingforblockheads-neoforge-1.21.1-21.1.21.jar (braucht Balm).
- **Integration:** Bindet ALLE Food-Mods (Croptopia, Pam's, Farmer's Delight, Let's Do) in eine zentrale Kuechen-UI - massiver QoL fuer den Cozy-Kochfokus. Moebel passen optisch zu Handcrafted/Another Furniture.
- **Quest:** Mittel: Kuechen-Ausbau-Questline (jedes Geraet freischalten), Rezeptbuch-Vervollstaendigung.
- **Progression:** Stufenweiser Aufbau der Multiblock-Kueche; Kuehlschrank-Upgrades fuer mehr Lagerung.
- **Probleme:** Benoetigt Balm-Dependency (pruefen ob schon im Pack). Das Kochbuch kann mit vielen Food-Mods extrem viele Eintraege zeigen - Performance/Uebersicht beobachten.

### Brewin' And Chewin'  
*Typ: mod*

- **Nutzen:** Farmer's-Delight-Addon fuer Gaerung/Alkohol: Faesser, Wein, Bier, Met, Effekt-Getraenke und fermentierte Speisen. Verifiziert: v4.4.1 NeoForge 1.21.1.
- **Integration:** Direktes FD-Addon, integriert sich nahtlos ins bestehende Delight-Oekosystem und ergaenzt Let's Do Vinery/Herbal Brews um Gaerungstiefe.
- **Quest:** Mittel-hoch: Brauerei-Questline, Rezeptsammlung fuer fermentierte Speisen, Tavernen-Versorgung (passt zu Dungeons & Taverns).
- **Progression:** Gaerungszeiten und Fass-Stufen geben Wartemechanik; Effekt-Getraenke als Buff-Progression.
- **Probleme:** Alkohol-Effekte muessen mit anderen Drink-Mods (Let's Do Herbal Brews) abgeglichen werden, um Buff-Stacking zu vermeiden. Inhaltliche Naehe zu Vinery (Wein) - Rollen klar abgrenzen.

### Nature's Spirit  
*Typ: mod*

- **Nutzen:** Fuegt zahlreiche neue Baeume, Holzarten, Fruechte und Pflanzen ueber neue Biome hinzu (z.B. neue Obst-/Nussbaeume, dekorative Flora). Verifiziert: 2.2.5-1.21.1 NeoForge.
- **Integration:** Erweitert die botanische Vielfalt fuer Town-Building und Farming-Deko; neue Hoelzer kombinieren mit Every Compat zu Moebeln. Ergaenzt Terralith/Tectonic-Worldgen.
- **Quest:** Mittel: Baum-/Frucht-Sammelquests, Biom-Erkundung als Entdeckungs-Questline.
- **Progression:** Neue Anbau-Ressourcen fuer Spaet-Game-Deko und Kochzutaten.
- **Probleme:** Biom-Mod - Worldgen-Overlap mit Terralith/Tectonic/Continents pruefen (Biom-Verteilung kann konkurrieren). Eher botanisch als reine Farming-Mod - Fokus liegt teils auf Deko.

### Cozy Foods: Milk Tea  
*Typ: mod*

- **Nutzen:** Boba/Milk-Tea-Kochmod mit Mango-Baeumen, Tee-Blender und mehreren Tee-Sorten (Mango, Taro, Jasmin, Matcha, Honeydew) plus Cafe-Deko. Verifiziert fuer 1.21.1 auf CurseForge.
- **Integration:** Perfekt fuer den Cozy-Cafe-Aspekt; ergaenzt Create Cafe und Confectionery um Getraenke-Vielfalt. Mango-Baeume erweitern das Obst-Anbau-Sortiment.
- **Quest:** Mittel: Cafe-/Teestand-Aufbau-Quest, Tee-Rezept-Sammlung.
- **Progression:** Tee-Blender als craftbare Station; verschiedene Tee-Stufen mit Buffs.
- **Probleme:** Thematisch nischig (asiatischer Cafe-Stil) - muss zum gewuenschten Cozy-Aesthetik passen. Kleiner Content-Umfang.

### It's Tea Time! (Simply Tea-Nachfolger / Tea & Coffee)  
*Typ: mod*

- **Nutzen:** Erlaubt Brauen von Tee, Kaffee und Flasks mit eigenen Teebaeumen und Zutaten. Cozy Hot-Drink-System.
- **Integration:** Ergaenzt Croptopia-Kaffee und Cozy Foods Tee; Heissgetraenke passen zum Comforts-Schlafsack-Cozy-Feeling und Cafe-Theme.
- **Quest:** Mittel: Teehaus-Questline, Getraenke-Rezeptsammlung.
- **Progression:** Teebaum-Anbau -> Trocknung -> Brauen als mehrstufige Kette.
- **Probleme:** (Verfuegbarkeit fuer 1.21.1 NeoForge pruefen - Simply Tea war zuletzt 1.20.1). Overlap mit Cozy Foods Tee und Croptopia Kaffee - nur eine Tee-Quelle waehlen.

### Delightful  
*Typ: mod*

- **Nutzen:** Farmer's-Delight-Addon mit zusaetzlichen Speisen, Smoothies, Eis, Cantaloupe, Salmonberries und Cross-Mod-Rezepten (nutzt Items anderer Mods). Verifiziert auf CurseForge/Modrinth fuer 1.21.1.
- **Integration:** Klassisches FD-Addon, bindet automatisch Zutaten aus vielen Mods (auch Croptopia/Pam's) in neue Rezepte ein - hoher Synergie-Wert mit bestehendem Delight-Stack.
- **Quest:** Mittel: Dessert-/Smoothie-Rezeptsammlung als Quest.
- **Progression:** Erweitert die Kochrezept-Tiefe ohne neue Maschinen - eher Breite als Stufen.
- **Probleme:** Starke Abhaengigkeit von Farmer's Delight (vorhanden, ok). Bei sehr vielen Food-Mods wird JEI-Rezeptliste unuebersichtlich.

### End's Delight  
*Typ: mod*

- **Nutzen:** Farmer's-Delight-Addon fuer End-Kueche: Chorus-basierte Gerichte, neue End-Crops und Speisen. Verifiziert: ends_delight-2.5.1+neoforge.1.21.1.jar.
- **Integration:** FD-Addon, fuellt die End-Dimension mit Cozy-Farming-Content. Memory listet 'Ends Delight' evtl. schon - PRUEFEN ob bereits enthalten.
- **Quest:** Mittel: End-Expeditions-Kochquest, Chorus-Farming-Quest.
- **Progression:** End-Game-Farming-Inhalt, sinnvoll als spaete Progressionsstufe.
- **Probleme:** WICHTIG: Memory erwaehnt 'Ends/Nethers' Delight bereits - wahrscheinlich Doppelung. Vor Aufnahme verifizieren, sonst streichen.

### Redomesticate (Domestication Innovation Fork)  
*Typ: mod*

- **Nutzen:** Verbessert Tierzaehmung/Haltung: Follow/Stay/Wander-Modi, Tier-Accessoires, bessere Begleiter fuer Woelfe, Katzen, Papageien, Axolotl, Hasen, Fuechse. Verifiziert: 1.21.1 NeoForge/Fabric.
- **Integration:** Ergaenzt Companions Dogfolk und Critters & Companions um echte Haustier-Verwaltung; passt zum Animal-Crossing-Town-Feeling.
- **Quest:** Mittel: Haustier-Zaehmungsquests, Accessoire-Sammlung.
- **Progression:** Tier-Bett, Hundekuchen und Accessoires als craftbare Belohnungsstufen.
- **Probleme:** Funktionaler Overlap mit Critters & Companions Zaehm-Features moeglich; Mob-AI-Konflikte mit Smarter Farmers/Guard Villagers im Auge behalten.

### Untamed Wilds  
*Typ: mod*

- **Nutzen:** Hochwertige neue Tiere (Schlangen, Grosskatzen, Schildkroeten, Baeren etc.) mit Geschlecht, Zucht, Groessenvarianz und Aufzucht-Mechanik - vertieft Tierhaltung. Verifiziert: 1.21.1 Port auf GitHub.
- **Integration:** Erweitert Naturalist um zuechtbare exotische Tiere; Cage-Trap-Mechanik fuer Tiertransport passt zum Town-Zoo/Farm-Aufbau.
- **Quest:** Hoch: Tier-Sammelquest, Zuchtprogramme (seltene Faerbungen), Zoo-Aufbau-Questline.
- **Progression:** Zucht ueber Generationen fuer seltene Varianten gibt langfristiges Ziel.
- **Probleme:** (Inoffizieller 1.21.1-Port auf GitHub - Stabilitaet/Verfuegbarkeit pruefen, evtl. nicht auf CurseForge). Spawn-Overlap mit Naturalist - Spawn-Weights abstimmen.

### Nutritional Balance  
*Typ: mod*

- **Nutzen:** Ernaehrungssystem: ausgewogene Kost macht staerker/schneller, Naehrstoffgruppen werden getrackt. Belohnt Vielfalt statt Strafe. Verifiziert fuer 1.21.1 Forge/NeoForge.
- **Integration:** Wertet den gesamten Food-Stack (Croptopia, Pam's, Farmer's Delight) spielmechanisch auf - Kochen bekommt echten RPG-lite-Sinn. Kompatibel mit Pam's, FD, Simply Tea.
- **Quest:** Mittel: Ernaehrungs-Meilenstein-Quests (alle Naehrstoffgruppen abdecken).
- **Progression:** Stat-Boni bei guter Ernaehrung geben sanfte RPG-Progression ueber das ganze Spiel.
- **Probleme:** Nutrition-System kann fuer Casual-Cozy-Spieler nervig wirken - Buffs statt Strafen konfigurieren. Konflikt mit Diet/Spice of Life vermeiden (nur EINES waehlen).

### Spice of Life: Classic Edition  
*Typ: mod*

- **Nutzen:** Belohnt Nahrungsvielfalt: wiederholtes Essen desselben Items senkt Saettigung, Vielfalt gibt Boni. Verifiziert fuer 1.21.1 NeoForge/Fabric.
- **Integration:** Macht den riesigen Food-Content (Croptopia/Pam's/FD) spielrelevant; voll kompatibel mit Diet/Nutritional Balance.
- **Quest:** Mittel: 'Probiere X verschiedene Gerichte'-Quests.
- **Progression:** Sanfter Anreiz, ueber die Zeit immer neue Rezepte zu kochen.
- **Probleme:** ENTWEDER Nutritional Balance ODER Spice of Life - beide gleichzeitig ist redundant/konfliktanfaellig. Strafmechanik muss cozy-tauglich getunt werden.

### Just Another Rotten Flesh to Leather Mod (JRFTL)  
*Typ: mod*

- **Nutzen:** Wandelt Rotten Flesh in Leder (Schmelzen oder Hardmode-Crafting). Loest das Leder-Knappheits-Problem fuer Town-Building/Buchbinden. Verifiziert: JRFTL NeoForge 1.21-1.21.1.
- **Integration:** QoL fuer das ressourcenintensive Cozy-Bauen und Sophisticated-Backpack-Crafting; Rotten Flesh aus Mob-Farms wird nutzbar.
- **Quest:** Gering: eher utility.
- **Progression:** Gering - reine Ressourcen-Umwandlung.
- **Probleme:** Sehr kleine Utility-Mod, kann Leder-Wirtschaft trivialisieren - Hardmode-Config nutzen, um Balance zu wahren.

### Immersive Engineering  
*Typ: mod*

- **Nutzen:** Industrielle Tech mit Wasserrad, Windmuehle und Oel-Muehle (Squeezer) - echte Muehlen-/Verarbeitungsmechanik fuer Getreide/Pflanzenoel. Verifiziert: 1.21.1 NeoForge (BluSunrize).
- **Integration:** Ergaenzt Create um realistische Wind-/Wassermuehlen-Aesthetik; Garten-/Crop-Verarbeitung (Mehl, Oel) passt zum Farming-Theme. Windmuehlen sind starkes Cozy-Landschaftselement.
- **Quest:** Mittel: Muehlen-Bau-Questline, Pflanzenoel-Produktionskette.
- **Progression:** Multiblock-Maschinen als gestaffelte Tech-Stufen parallel zu Create.
- **Probleme:** Grosse Tech-Mod - kann mit Create um dieselbe Nische konkurrieren und das Pack tech-lastiger machen als das Cozy-Vision will. Nur aufnehmen, wenn die Muehlen-Aesthetik gewollt ist; ggf. nur Teilfeatures via KubeJS einschraenken.

### Vintage Delight  
*Typ: mod*

- **Nutzen:** Farmer's-Delight-Addon mit Alterung/Reifung von Speisen und Getraenken in Faessern, vintage Gerichte. Vertieft die Fermentations-/Reife-Mechanik.
- **Integration:** FD-Addon, ergaenzt Brewin' And Chewin' und Vinery um Reifungs-Tiefe; passt zum Cozy-Keller-/Vorrats-Aufbau.
- **Quest:** Mittel: Reifekeller-Aufbau-Quest, gealterte Spezialitaeten als Belohnung.
- **Progression:** Reifezeiten geben langfristige Wartemechanik mit besseren Endprodukten.
- **Probleme:** (Verfuegbarkeit fuer 1.21.1 NeoForge pruefen). Funktionaler Overlap mit Brewin' And Chewin' Faessern - Rollen abgrenzen.

### Miner's Delight  
*Typ: mod*

- **Nutzen:** Farmer's-Delight-Addon mit Hoehlen-/Bergbau-Kueche: unterirdische Crops (Cave Carrot), Tragbare Kochstellen, Bergmanns-Gerichte mit Mining-Buffs. (Bereits als Delight-Addon im Memory? Pruefen.)
- **Integration:** FD-Addon - fuellt die Untertage-Aktivitaet mit Cozy-Farming. Buffs ergaenzen Create-Mining-Sessions.
- **Quest:** Mittel: Hoehlen-Crop-Sammlung, Bergmanns-Rezept-Questline.
- **Progression:** Cave-Crops und Buff-Gerichte als Mining-Progressionshilfe.
- **Probleme:** WICHTIG: Memory listet 'Miners' Delight bereits unter den Delight-Addons - sehr wahrscheinlich Doppelung. Vor Aufnahme pruefen, sonst streichen.

### Bakery / Pumpk's Bakery  
*Typ: mod*

- **Nutzen:** Backerei-Mod: Mehl mahlen, Teig kneten, Brote/Kuchen/Gebaeck backen mit eigenem Backofen. Fuellt die Backwaren-Nische, die FD nur streift.
- **Integration:** Nutzt Getreide aus Pam's/Croptopia; Backofen ergaenzt Cooking for Blockheads und Create-Muehlen (Mehl). Passt zum Cafe/Confectionery-Theme.
- **Quest:** Mittel-hoch: Baeckerei-Aufbau-Questline, Gebaeck-Rezeptsammlung fuer Stadt-Versorgung.
- **Progression:** Mehl -> Teig -> Backwaren als mehrstufige Kette mit Ofen-Upgrades.
- **Probleme:** (Genaue Mod-Verfuegbarkeit fuer 1.21.1 NeoForge pruefen - mehrere Backerei-Mods existieren mit unterschiedlichem Stand). Mehl/Teig-Tag-Overlap mit Create-Mehl und FD harmonisieren.

### Farmer's Respite  
*Typ: mod*

- **Nutzen:** Farmer's-Delight-Addon fuer Heissgetraenke: Tee, Kaffee, Wasserkocher, Kaffee-Crops und koffeinierte Buffs. Cozy Drink-Erweiterung.
- **Integration:** FD-Addon - zentralisiert Tee/Kaffee statt mehrerer Einzel-Mods; ergaenzt Comforts und Cafe-Theme. Nutzt Croptopia-Kaffee.
- **Quest:** Mittel: Kaffeehaus-Questline, Heissgetraenk-Rezepte.
- **Progression:** Wasserkocher und Brueh-Stufen; Buff-Getraenke als sanfte Progression.
- **Probleme:** (Verfuegbarkeit 1.21.1 NeoForge pruefen). Overlap mit Cozy Foods Tee / It's Tea Time - nur EINE Heissgetraenk-Loesung waehlen, um Redundanz zu vermeiden.

### Ecologics  
*Typ: mod*

- **Nutzen:** Fuegt Biom-Tiere und essbare Pflanzen hinzu (Kokospalmen mit Kokosnuessen, Pinguine, Krabben, Squirrels). Tropische Crop-/Tier-Vielfalt. (Verfuegbarkeit 1.21.1 NeoForge pruefen.)
- **Integration:** Kokosnuss und tropische Frucht erweitern Croptopia/Beachparty-Theme; Tiere ergaenzen Naturalist. Passt zum gemuetlichen Insel-/Strand-Aspekt.
- **Quest:** Mittel: Tier-/Pflanzen-Sammelquest pro Biom.
- **Progression:** Neue Crop-Quellen und Tiere fuer Mittel-Game-Inhalt.
- **Probleme:** (1.21.1-NeoForge-Verfuegbarkeit unsicher - pruefen). Biom-/Spawn-Overlap mit Naturalist und Terralith abstimmen.

### Croparia / Crops o' Plenty  
*Typ: mod*

- **Nutzen:** Zusaetzliche dekorative und nutzbare Crops/Beeren mit Verarbeitungsoptionen, fuellt Luecken zwischen Vanilla und Croptopia. (Verfuegbarkeit pruefen.)
- **Integration:** Erweitert Crop-Vielfalt fuer Farmer's Delight Kochrezepte; Beeren passen zu Let's Do Herbal Brews.
- **Quest:** Mittel: Crop-Sammelquest.
- **Progression:** Zusaetzliche Anbaustufen fuer Kochzutaten.
- **Probleme:** (Verfuegbarkeit/Aktualitaet fuer 1.21.1 NeoForge stark pruefen). Hoher Crop-Overlap-Risiko mit Croptopia+Pam's - moeglicherweise ueberfluessig, nur bei klarer Luecke aufnehmen.

### Aquaculture Delight  
*Typ: mod*

- **Nutzen:** Bridge-Addon, das Aquaculture-Fische in Farmer's-Delight-Rezepte (Filets, Sushi, Fischgerichte) einbindet. Verbindet Angeln und Kochen.
- **Integration:** Verbindet Aquaculture 2 mit dem Delight-Stack - macht gefangene Fische kulinarisch wertvoll. Memory listet 'Crabbers/Aquaculture' Delight evtl. schon - PRUEFEN.
- **Quest:** Mittel: Fischkueche-Rezeptsammlung.
- **Progression:** Fisch-Verarbeitungskette ergaenzt Angel-Progression.
- **Probleme:** WICHTIG: Memory nennt bereits Crabber's/Aquaculture-Delight-Addons - wahrscheinlich Doppelung. Nur aufnehmen, wenn es ein anderes Addon ist als das bereits enthaltene.

### Mob's Properties / Animal Feeding Trough  
*Typ: mod*

- **Nutzen:** Futtertrog-Block, der Nutztiere automatisch fuettert und in der Naehe haelt - QoL fuer Viehhaltung ohne manuelles Fuettern. (Verfuegbarkeit pruefen.)
- **Integration:** Macht grosse Tierfarmen pflegeleicht; passt zum Cozy-Farm-Management neben MineColonies. Nutzt Crops als Futter.
- **Quest:** Gering-mittel: Stall-/Farm-Aufbau-Quest.
- **Progression:** Craftbarer Trog als Farm-Automatisierungsstufe.
- **Probleme:** (Genauer Mod-Name/Verfuegbarkeit fuer 1.21.1 NeoForge pruefen - mehrere Trough-Mods existieren). Moeglicher AI-Overlap mit Smarter Farmers/Guard Villagers.

### Croptosia / Vegetable Soup  
*Typ: mod*

- **Nutzen:** Fuegt weitere Gemuesesorten und einfache Suppen/Eintopf-Rezepte hinzu, fokussiert auf herzhafte Hausmannskost. (Verfuegbarkeit pruefen.)
- **Integration:** Ergaenzt Farmer's Delight Eintopf-Linie; Gemuese fuer Cooking for Blockheads.
- **Quest:** Mittel: Suppen-Rezeptsammlung.
- **Progression:** Gemuese-Anbau -> Eintopf-Rezepte.
- **Probleme:** (Verfuegbarkeit/Aktualitaet 1.21.1 NeoForge unsicher - pruefen). Hoher Crop/Rezept-Overlap mit Croptopia/Pam's/FD - nur bei klarem Mehrwert aufnehmen.

### Berry Good  
*Typ: mod*

- **Nutzen:** Fuegt diverse Beeren (Salmonberry u.a.) als anbaubare Buesche mit Verarbeitungsoptionen (Jams, Pips) hinzu. Erweitert Beeren-Anbau ueber Vanilla Sweet Berries hinaus.
- **Integration:** Beeren fliessen in Let's Do Herbal Brews, Brewin' And Chewin' und Delightful-Smoothies. Buesche als Cozy-Garten-Deko.
- **Quest:** Mittel: Beeren-Sammelquest, Marmeladen-Rezepte.
- **Progression:** Beerenbusch-Anbau -> Verarbeitung zu Konserven.
- **Probleme:** (Verfuegbarkeit fuer 1.21.1 NeoForge pruefen - in Suchergebnissen nur als Compat-Notiz aufgetaucht). Beeren-Overlap mit Croptopia moeglich.

### Farmer's Delight: Frycook / Fryer Addon  
*Typ: mod*

- **Nutzen:** FD-Addon mit Fritteuse fuer frittierte Speisen (Pommes, Tempura, frittierter Fisch). Memory nennt 'Deepfried' bei Create - das hier ist die FD-Kueche-Variante. (Verfuegbarkeit/Abgrenzung pruefen.)
- **Integration:** Ergaenzt FD-Kochstationen um Frittier-Methode; nutzt Fisch (Aquaculture) und Kartoffeln/Crops.
- **Quest:** Mittel: Frittier-Rezeptsammlung, Imbiss-Aufbau-Quest.
- **Progression:** Fritteuse als zusaetzliche Kochstation-Stufe.
- **Probleme:** WICHTIG: Memory listet 'Deepfried' (Create-Addon) bereits - Abgrenzung/Doppelung pruefen. Nur aufnehmen, wenn es ein eigenstaendiges FD-Frittier-Addon ist.

### Pumpkin & Melon / Veggie Way  
*Typ: mod*

- **Nutzen:** Erweitert Kuerbis-/Melonen-Anbau um Sorten, Verarbeitung und herbstliche Crops; Cozy-Herbst-Aesthetik. (Verfuegbarkeit pruefen.)
- **Integration:** Passt zu Serene Seasons (Herbst-Ernte); Kuerbisse fuer Farmer's Delight und Deko.
- **Quest:** Mittel: Herbst-Ernte-Quest, Kuerbis-Rezepte.
- **Progression:** Saisonaler Anbau-Zyklus mit Serene Seasons.
- **Probleme:** (Genaue Mod-Verfuegbarkeit fuer 1.21.1 NeoForge pruefen). Overlap mit bestehenden Crop-Mods - kuratieren.

### Wholesome (Mob Sounds/Pets) -> ersetzt durch: Friends & Foes Farming Critters  
*Typ: mod*

- **Nutzen:** Fuegt sanfte Nutz-/Begleittiere und kleine Farm-Tiere mit eigenen Produkten hinzu (z.B. zusaetzliche Geflugel-/Kleintierarten mit Eiern/Wolle-Varianten). (Verfuegbarkeit pruefen.)
- **Integration:** Erweitert Naturalist/Critters um produktive Farmtiere; Produkte fliessen in Kochrezepte.
- **Quest:** Mittel: Tierzucht-Sammelquest.
- **Progression:** Neue Tierprodukte als Kochzutaten-Quellen.
- **Probleme:** (Mod-Name/Verfuegbarkeit fuer 1.21.1 NeoForge konkret verifizieren). Spawn-/AI-Overlap mit Naturalist und Critters & Companions abstimmen.

### Mushroom Quest / Mushroom Expansion  
*Typ: mod*

- **Nutzen:** Fuegt anbaubare Pilzsorten, Pilzbeete und Pilz-Speisen hinzu - vertieft das Pilz-Farming, das Vanilla/FD nur knapp abdecken. (Verfuegbarkeit pruefen.)
- **Integration:** Pilze fuer Farmer's Delight Eintoepfe und Cooking for Blockheads; passt zu Hoehlen-/Wald-Cozy-Theme.
- **Quest:** Mittel: Pilz-Sammelquest, Pilzfarm-Aufbau.
- **Progression:** Pilzzucht als feuchtigkeits-/lichtabhaengige Anbaumechanik.
- **Probleme:** (Konkreten 1.21.1-NeoForge-Mod verifizieren - mehrere Pilz-Mods existieren mit variierendem Stand). Geringes Doppelungsrisiko.

### Tofu / Soybean Farming (Tofucraft)  
*Typ: mod*

- **Nutzen:** Sojabohnen-Anbau und Tofu-Verarbeitung (Tofu, Sojamilch, Tofu-Gerichte) - vegetarische Protein-Quelle und asiatische Kueche. (Verfuegbarkeit pruefen.)
- **Integration:** Soja fuegt sich in Croptopia/Pam's-Crops ein; Tofu-Gerichte ergaenzen Sushi Go und FD-Kueche. Vegetarische Option fuer Ernaehrungs-Mods.
- **Quest:** Mittel: Tofu-Produktionskette als Questline.
- **Progression:** Soja -> Sojamilch -> Tofu -> Gerichte als mehrstufige Verarbeitung.
- **Probleme:** (1.21.1-NeoForge-Verfuegbarkeit unsicher - Tofucraft war historisch Forge-lastig, pruefen). Soja-Crop-Overlap mit Croptopia/Pam's pruefen.


## item-designer (33)

### Goldene Gießkanne (Golden Watering Can)  
*Typ: item*

- **Nutzen:** Effekt: Rechtsklick auf Ackerland im 3x3 (oder 5x5 upgraded) bewässert Boden sofort auf Feuchtigkeit 7 und gibt jungen Crops einen kleinen Wachstums-Tick (BoneMeal-light, ~15% Chance). Herstellung: KubeJS-Item aus Create Brass Casing + Eimer + Goldbarren; Upgrade-Stufen (Kupfer/Eisen/Gold/Netherite) erhöhen Radius und Durability. Seltenheit: Uncommon (Gold) bis Epic (Netherite). Durability-basiert, mit Wasser nachfüllbar an jeder Wasserquelle.
- **Integration:** Direkter Stardew-Valley-Pull; ergänzt Farmer's Delight/HarvestCraft-Ackerbau und Serene Seasons. Wird als zentrales Early-Game-Farmwerkzeug via KubeJS registriert.
- **Quest:** FTB-Quest 'Der grüne Daumen': Erste Holz-Gießkanne als Belohnung, Upgrade-Kette als Quest-Linie über Farming-Kapitel.
- **Progression:** Klare Tier-Leiter (Kupfer→Eisen→Gold→Netherite) mit wachsendem Radius — koppelt Farming-Fortschritt an Metall-/Create-Progression.
- **Probleme:** Wachstums-Tick darf BoneMeal nicht trivialisieren (Cooldown/Chance nötig); KubeJS-Block-Interaction-Events für Feuchtigkeit setzen erfordern Test gegen Serene Seasons.

### Erntesichel der Jahreszeiten (Seasonal Harvest Scythe)  
*Typ: item*

- **Nutzen:** Effekt: Erntet reife Crops im 3x3-Radius und repflanzt automatisch (Right-Click-Harvest mit Replant), droppt zusätzlich 10% Bonus-Ertrag in der zur Jahreszeit passenden Saison (Serene Seasons Abfrage). Herstellung: Netherite-Sense-Form via KubeJS aus Eisen + Farmer's Delight Straw + Create-Mechanismus. Seltenheit: Rare. Mit Verzauberungen kompatibel (Fortune wirkt).
- **Integration:** Verbindet Serene Seasons + Farmer's-Delight-Ernte-Loop; nutzt vorhandene Right-Click-Harvest-Mechaniken thematisch.
- **Quest:** Quest 'Die vier Jahreszeiten': Ernte je 64 Crops pro Saison, Belohnung ist die Sichel.
- **Progression:** Mittleres Tier-Werkzeug zwischen Hand-Ernte und vollautomatischer Create-Harvester-Automation — Brücke ins Automatisierungs-Endgame.
- **Probleme:** Saison-Abfrage via Serene-Seasons-API in KubeJS prüfen (Verfuegbarkeit pruefen); Auto-Replant darf nicht mit Smarter-Farmers/Create-Harvestern doppeln.

### Stadtgründer-Glocke (Founder's Bell)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbares Deko-Item; bei Rechtsklick ertönt ein Glockenton und alle Villager/MineColonies-Bürger im Umkreis von 32 Blöcken erhalten 60s einen 'Heimatgefühl'-Buff (schnellere Arbeit, bessere Trade-Preise). Herstellung: Bells-&-Whistles-Glocke + Goldblock + Town-Talk-Notiz, KubeJS-Crafting. Seltenheit: Rare, Einmal-pro-Siedlung gedacht.
- **Integration:** Synergie mit MineColonies, Easy Villagers, Trade Cycling, Bells & Whistles und Town Talk — zentrales Town-Building-Symbolitem.
- **Quest:** Belohnung der Quest 'Gründung der Stadt' nach Errichten von Rathaus + 5 Bürgerhäusern.
- **Progression:** Markiert den Übergang vom Einzel-Farmer zum Town-Builder; schaltet thematisch das Siedlungs-Kapitel frei.
- **Probleme:** Buff-AoE auf Villager-AI anwenden ist tricky (KubeJS + evtl. Effekt-Tags); Balance gegen Trade-Cycling-Preise.

### Sammleralbum 'Cozy Valley Cards'  
*Typ: item*

- **Nutzen:** Effekt: Sammelkarten-Album (via Collector's Album Mod) mit gepacktem Custom-Kartenset zu Mobs/Crops/NPCs des Packs; volle Seiten geben permanente Mini-Perks (z.B. +1 Herz, leicht schnelleres Angeln). Herstellung: Album als Loot/Shop-Item; Karten droppen von Naturalist/Critters-Mobs und Angeln. Seltenheit: Karten von Common bis Legendary.
- **Integration:** Collector's Album (collectorsalbum-neoforge-1.21.1-2.6.x, verfügbar) als Framework; Karten thematisch an Naturalist, Critters & Companions, Fish of Thieves gekoppelt.
- **Quest:** Sammel-Quests 'Vervollständige das Tier-Set' / 'Fang alle Fische' mit FTB-Quest-Tracking.
- **Progression:** Langfristiger Collection-Loop (Animal-Crossing-Museum-Feeling) mit Perk-Belohnungen — perfektes Soft-Endgame.
- **Probleme:** Custom-Kartenset erfordert Datapack/Konfig für Collector's Album (Aufwand); Perks balancen, damit nicht Pflicht-Grind. Verfuegbarkeit der Custom-Card-API pruefen.

### Hufeisen des Glücks (Lucky Horseshoe)  
*Typ: item*

- **Nutzen:** Effekt: Curios-Artefakt (Charm-Slot); +1 Luck-Attribut, leicht erhöhte Loot-/Angel-/Crop-Drop-Chancen, +5% Smaragd-Trade-Bonus. Herstellung: Eisenbarren + Hay Bale + Naturalist-Hufeisen-Loot via Relics/Curios. Seltenheit: Rare. Kein Schutz, rein passiv.
- **Integration:** Nutzt die vorhandene Artifacts-/Curios-Infrastruktur; ergänzt Aquaculture-Angeln und Vanilla-Trade-Wirtschaft.
- **Quest:** Belohnung für 'Erster Marktstand'-Quest oder seltener Dungeons-&-Taverns-Loot.
- **Progression:** Mid-Game-Charm, der Sammel- und Wirtschafts-Loops verstärkt ohne Kampf-Power-Creep.
- **Probleme:** Luck-Stacking mit Artifacts/Relics balancen; Trade-Bonus via KubeJS auf Villager-Trades anwenden ist nicht trivial.

### Wetterglocke (Weather Chime)  
*Typ: item*

- **Nutzen:** Effekt: Deko + Funktion; Rechtsklick zeigt im Chat/Actionbar die kommende Wetter-/Jahreszeiten-Tendenz (Serene Seasons) und kann 1x/Tag mit Cooldown leichtes Wetter (Sonne) für die Farm beschwören. Herstellung: Amethyst + Kupferglocke + Windrad-Material aus Create. Seltenheit: Uncommon.
- **Integration:** Koppelt an Serene Seasons + Create-Wind/Aeronautics-Thematik; Quality-of-life für Farmer.
- **Quest:** Quest 'Den Himmel lesen' im Farming-Kapitel.
- **Progression:** Frühes QoL-Item, das Saisonplanung erleichtert — sanfter Einstieg ins Wetter-/Saison-System.
- **Probleme:** Wetter-Manipulation darf nicht Vanilla-/Create-Wetterfarmen brechen (langer Cooldown); Saison-Vorhersage braucht Serene-Seasons-API.

### Kompostkristall (Compost Crystal)  
*Typ: item*

- **Nutzen:** Effekt: In Komposter/Create-Mixer einsetzbarer Verbrauchs-Katalysator; verdreifacht Knochenmehl-Ausbeute aus organischem Abfall für einen Stack. Herstellung: Verrottete Crops + Amethyst-Splitter in Create-Basin gemischt. Seltenheit: Common-Verbrauchsgut.
- **Integration:** Verbindet Farmer's-Delight-Abfall + Create-Mixing + Knochenmehl-Wirtschaft; reduziert Crop-Verschwendung.
- **Quest:** Teil der 'Nachhaltiger Anbau'-Quest-Reihe.
- **Progression:** Verbrauchs-Wirtschaftsitem, das den Knochenmehl-Loop für Create-Automation skaliert.
- **Probleme:** KubeJS-Rezept für Create-Mixer-Output; Balance gegen vorhandene Knochenmehl-Quellen, damit nicht überflüssig.

### Reise-Picknickkorb (Traveler's Picnic Basket)  
*Typ: item*

- **Nutzen:** Effekt: Tragbarer Mini-Inventar-Container (9 Slots) NUR für Essen; hält Food länger frisch (kein Spoil falls Spoil-Mod, sonst kosmetisch) und gibt beim Essen daraus +20% Sättigungs-Bonus. Herstellung: Sophisticated-Backpack-Leder + Farmer's-Delight-Picknickdecke. Seltenheit: Uncommon.
- **Integration:** Spielt mit Sophisticated Storage/Backpacks, Farmer's Delight, AppleSkin und Comforts (Camping-Feeling).
- **Quest:** Belohnung der 'Ausflug ins Grüne'-Quest; Anreiz fürs Kochen.
- **Progression:** Frühes Cozy-QoL-Item, das Exploration und Kochen verzahnt.
- **Probleme:** Food-only-Slot-Filter via KubeJS/Sophisticated-Config; Sättigungs-Bonus über AppleSkin-kompatible Werte.

### Marktstand-Schild (Market Stall Sign)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbarer dekorativer Marktstand-Block mit Display-Slot; zeigt schwebend das eingelegte Item und Stückzahl. Optional via KubeJS als simpler Verkaufs-Trigger an Vanilla-Wandering-Trader-Preisen. Herstellung: Handcrafted/Another-Furniture-Holz + Banner + Schild. Seltenheit: Common Deko.
- **Integration:** Ergänzt Handcrafted, Another Furniture, Supplementaries-Displays und die Vanilla-Smaragd-Wirtschaft; baut Town-Markt-Atmosphäre.
- **Quest:** Quest 'Eröffne deinen Stand' — platziere 3 Stände auf dem Marktplatz.
- **Progression:** Reines Town-Building/Roleplay-Item; treibt Stadtgestaltung an.
- **Probleme:** Item-Display-Rendering via vorhandene Frame-Mechanik nutzen statt Neubau; sonst geringer Aufwand.

### Tau-Tropfen (Morning Dew Drop)  
*Typ: item*

- **Nutzen:** Effekt: Verbrauchs-Trank-Item; bei Konsum sofort kleiner Regenerations- + Hunger-Tick und entfernt Müdigkeit/negative Cozy-Debuffs. Sammelbar: erscheint frühmorgens (In-Game-Zeit) auf taufrischem Gras/Blumen, per Rechtsklick einsammelbar. Seltenheit: Common, zeit-/sammelbasiert.
- **Integration:** Naturalist/Blumen-Thematik + Serene-Seasons-Tageszeit; passt zu Comforts (Schlaf/Erholung).
- **Quest:** Sammel-Quest 'Sammle 16 Morgentau'; Crafting-Zutat für Beauty/Brew-Items (Herbal Brews).
- **Progression:** Tageszeit-gebundener Sammel-Loop, der Routine/Rhythmus belohnt (Cozy-Daily-Loop).
- **Probleme:** Spawn-Logik auf Blöcken zur Tageszeit via KubeJS/Tick-Event kann performancekritisch sein — auf Chunk-Nähe begrenzen.

### Glücksklee-Vierblatt (Four-Leaf Clover)  
*Typ: item*

- **Nutzen:** Effekt: Seltenes Sammelobjekt; gehalten/getragen +0.5 Luck; verbraucht in Brauen/Crafting für Glücks-Items. Sammelbar: niedrige Chance beim Mähen von Gras/Blumen mit der Erntesichel. Seltenheit: Rare Drop.
- **Integration:** Koppelt an Naturalist-Flora und das Erntesichel-Item; speist Luck-/Artefakt-Crafting.
- **Quest:** 'Finde ein vierblättriges Kleeblatt'-Glücks-Quest mit kosmetischer Belohnung.
- **Progression:** Soft-Sammelziel; Material-Gate für Glücks-Artefakte.
- **Probleme:** Drop-Chance feinjustieren (zu selten = frustig); KubeJS-Block-Break-Event auf Gras.

### Antikes Münzalbum (Antique Coin Display)  
*Typ: item*

- **Nutzen:** Effekt: Sammler-Vitrine mit 9 Slots für seltene 'Münz'-Sammelitems (Custom-KubeJS-Münzen aus verschiedenen Biomen/Dungeons); vollständige Sets geben Smaragd-Belohnung beim Wandering Trader. Herstellung: Glas + Goldblock + Item-Frame. Seltenheit: Set-Items Uncommon-Legendary.
- **Integration:** Bleibt bei der Vanilla-Smaragd-Wirtschaft (KEIN Coin-Mod), nutzt Münzen nur als Sammelobjekte; ergänzt Dungeons & Taverns Loot.
- **Quest:** 'Numismatiker'-Sammel-Questreihe je Biom/Struktur.
- **Progression:** Exploration-getriebener Collection-Loop mit Wirtschaft-Auszahlung.
- **Probleme:** Klar trennen von Währung (sind Sammelobjekte, nicht Zahlungsmittel); viele Custom-Items = KubeJS-Aufwand.

### Wunschlaterne (Wishing Lantern)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbare schwebende Laterne; bei Rechtsklick mit einem Smaragd 'gewünscht' — gibt 1x/Tag ein zufälliges kleines Cozy-Geschenk (Setzling, Rezept-Hinweis, kleiner Buff). Herstellung: Soul Lantern + Goldnugget + Papier. Seltenheit: Rare.
- **Integration:** Animal-Crossing-Wunsch-Mechanik; nutzt Smaragd-Wirtschaft + Supplementaries-Laternen-Ästhetik.
- **Quest:** Quest 'Der erste Wunsch'; tägliche Daily-Loot-Schleife.
- **Progression:** Daily-Engagement-Item, das Smaragde sinkt und kleine Belohnungen ausschüttet.
- **Probleme:** Daily-Cooldown sauber via NBT/Timestamp in KubeJS; Loot-Tabelle balancen, dass kein Exploit entsteht.

### Vogelhäuschen (Decorative Birdhouse)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbar; zieht passiv kleine Naturalist-Vögel/Critters an und gibt im Umkreis von 8 Blöcken einen leichten Ambient-'Gemütlichkeits'-Buff (langsamere Hungerabnahme). 1x/Tag legt ein Vogel eine Feder/ein Ei hinein. Herstellung: Handcrafted-Holz + Samen. Seltenheit: Common.
- **Integration:** Synergie mit Naturalist, Critters & Companions, Fresh Animations; Garten-Deko mit sanftem Nutzen.
- **Quest:** 'Ein Zuhause für die Vögel'-Quest; Sammel-Source für Federn.
- **Progression:** Cozy-Garten-Ausbau; passive Ressource + Atmosphäre.
- **Probleme:** Mob-Attraction via KubeJS-Spawn-Nudge kann mit Spawn-Caps kollidieren; Buff-AoE Performance prüfen.

### Gärtner-Handschuhe (Gardener's Gloves)  
*Typ: item*

- **Nutzen:** Effekt: Curios-Hand-Slot-Artefakt; +1 Crop-Drop beim Handernten, schnelleres Pflanzen (kein Cooldown beim Saat-Setzen) und Immunität gegen Süßbeeren-/Kaktus-Schaden. Herstellung: Leder + Wolle + Stroh via Relics/Curios. Seltenheit: Uncommon.
- **Integration:** Curios/Artifacts-Slot; verstärkt manuelles Farmen (HarvestCraft/Farmer's Delight) für Spieler, die nicht voll automatisieren.
- **Quest:** Belohnung 'Fleißiger Gärtner' nach X manuellen Ernten.
- **Progression:** Mid-Game-Charm der manuelles Farming attraktiv hält gegenüber Create-Automation.
- **Probleme:** Drop-Bonus mit Fortune/Erntesichel-Stacking balancen.

### Honigtopf-Talisman (Honeyed Talisman)  
*Typ: item*

- **Nutzen:** Effekt: Curios-Charm; Bienen/Let's-Do-Imkerei-Erträge +25%, kein Bienen-Aggro mehr, und Honig-Konsum gibt kurz Regeneration I. Herstellung: Honigwabe + Goldnugget + Bienenstock-Material. Seltenheit: Uncommon.
- **Integration:** Koppelt an Vanilla-Bienen + Let's Do (Meadow/Herbal Brews) + HarvestCraft-Süßes; Cozy-Imker-Rolle.
- **Quest:** 'Imker'-Questreihe; Belohnung nach Aufbau von 5 Bienenstöcken.
- **Progression:** Spezialisierungs-Charm für den Imkerei-Zweig der Wirtschaft.
- **Probleme:** Bienen-Aggro-Unterdrückung via KubeJS-Entity-Event; Ertrags-Boost auf Honigflaschen anwenden.

### Angler-Glücksbringer (Angler's Charm)  
*Typ: item*

- **Nutzen:** Effekt: Curios-Charm; +15% Chance auf seltenen Fisch (Aquaculture/Fish of Thieves), schnelleres Anbeißen, kleiner Bonus auf Schätze. Herstellung: Aquaculture-Angelhaken + Smaragd + Fischschuppe. Seltenheit: Rare.
- **Integration:** Verstärkt Aquaculture + Fish of Thieves; speist Collector's-Album-Fisch-Karten.
- **Quest:** 'Meister-Angler'-Quest nach Fang von X Fischarten.
- **Progression:** Angel-Spezialisierungs-Charm; treibt Fisch-Collection-Loop.
- **Probleme:** Loot-Modifier via KubeJS auf Angel-Loot-Tabellen; Stacking mit Luck-Items prüfen.

### Erinnerungs-Fotorahmen (Memory Photo Frame)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbarer Rahmen, der bei Rechtsklick einen 'Screenshot'-Map-artigen Render der Umgebung speichert (vereinfacht: kopiert Karten-Item) und an die Wand hängt. Reines Roleplay/Deko-Sammelobjekt für Erinnerungen an Events. Herstellung: Item Frame + Karte + Papier. Seltenheit: Common.
- **Integration:** Animal-Crossing-Foto-Feeling; nutzt Vanilla-Karten + Supplementaries-Rahmen-Ästhetik.
- **Quest:** Event-Belohnungen als einzigartige vorbefüllte Fotorahmen (Festival-Erinnerungen).
- **Progression:** Sentimentales Sammel-/Deko-System ohne Power; stärkt Bindung an die Welt.
- **Probleme:** Echter Screenshot-Render nicht machbar; auf Karten-Klon vereinfachen — Erwartungsmanagement nötig.

### Saisonale Festival-Maske (Festival Mask)  
*Typ: item*

- **Nutzen:** Effekt: Kosmetische Kopf-Slot-Items (Frühlings-Blüte / Sommer-Sonne / Herbst-Laub / Winter-Eis), je passend zur Serene-Seasons-Saison getragen +5% Bewegungs- oder Arbeits-Bonus. Herstellung: Saison-typische Materialien (Blüten/Weizen/Laub/Eis). Seltenheit: Uncommon Eventitem.
- **Integration:** Serene Seasons + 3D Skin Layers/kosmetische Slots; Festival-Atmosphäre für Town-Events.
- **Quest:** Saisonale Event-Quests schütten je eine Maske aus (4-teiliges Set-Sammelziel).
- **Progression:** Saison-Event-Collection mit kleinem situativem Buff; jährlicher Wiederholungs-Loop.
- **Probleme:** Kopf-Slot-Rendering via Curios/Trinkets-Cosmetic prüfen; Saison-Bonus-Abfrage.

### Mini-Gewächshaus-Glas (Cloche Jar)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbares Glasglocken-Block; eine darin gepflanzte Crop wächst saison-unabhängig und ~30% schneller (kleines Single-Slot-Gewächshaus). Herstellung: Glas + Kupferrahmen (Create) + Erde. Seltenheit: Uncommon.
- **Integration:** Umgeht Serene-Seasons-Saisonsperre für einzelne Pflanzen; dekorativ + funktional, passt zu HarvestCraft/Farmer's Delight.
- **Quest:** 'Wintergarten'-Quest: ernte eine Sommerfrucht im Winter.
- **Progression:** Brücke zwischen Saison-Gating und Ganzjahres-Farming vor voller Create-Gewächshaus-Automation.
- **Probleme:** Saison-Override pro Block via KubeJS gegen Serene Seasons testen; Performance bei vielen Glocken.

### Schatzkarten-Fragment (Treasure Map Fragment)  
*Typ: item*

- **Nutzen:** Effekt: Sammel-Item; 4 Fragmente kombiniert ergeben eine Schatzkarte zu einer Dungeons-&-Taverns-/Structures-Arise-Struktur mit Belohnungskiste. Sammelbar: Loot aus Angeln, Dungeons, Villager-Trades. Seltenheit: Fragmente Uncommon, Karte Rare.
- **Integration:** Treibt Exploration zu Dungeons & Taverns + Create Structures Arise; nutzt Vanilla-Karten-Mechanik.
- **Quest:** 'Schatzsucher'-Questreihe; Fragment-Sammlung als Meta-Ziel.
- **Progression:** Exploration-Loop mit gestaffelter Belohnung; treibt Reisen via Steam'n'Rails/Aeronautics.
- **Probleme:** Fragment-zu-Karte-Crafting + Strukturziel via KubeJS/Loot; sicherstellen dass Strukturen vorhanden sind.

### Wandernde Saatgut-Tüte (Mystery Seed Pouch)  
*Typ: item*

- **Nutzen:** Effekt: Verbrauchs-Beutel; bei Öffnung 1 zufälliger Setzling/Crop aus dem Pack-Pool (gewichtet nach Seltenheit, inkl. seltener HarvestCraft-Crops). Herstellung: Kauf beim Wandering Trader oder Quest-Belohnung. Seltenheit: Common-Beutel, Inhalt variabel.
- **Integration:** Speist HarvestCraft/Farmer's-Delight-Crop-Sammlung; sanfte Smaragd-Geldsenke beim Trader.
- **Quest:** 'Sammle alle Crops'-Meta-Quest; Beutel als Hilfsmittel.
- **Progression:** Random-Crop-Discovery-Loop, der die große Crop-Vielfalt des Packs erschließt.
- **Probleme:** Loot-Pool gewichten (KubeJS); RNG-Frust bei seltenen Wünschen vermeiden (Pity-System optional).

### Kuhglocke des Hirten (Shepherd's Cowbell)  
*Typ: item*

- **Nutzen:** Effekt: Werkzeug; Rechtsklick ruft alle gezähmten/genutzten Nutztiere (Companions, Naturalist-Vieh) im Umkreis von 24 Blöcken zu dir und gibt ihnen kurz Folge-/Sammel-Verhalten. Herstellung: Bells-&-Whistles-Glocke + Leder + Eisen. Seltenheit: Uncommon.
- **Integration:** QoL für Tierhaltung mit Naturalist, Critters & Companions, Companions Dogfolk; Hirten-Rolle.
- **Quest:** 'Der gute Hirte'-Quest nach Zähmung/Haltung von X Tieren.
- **Progression:** Tierhaltungs-QoL; macht große Farmen handhabbar.
- **Probleme:** Mob-Pull via KubeJS-Entity-Targeting; nicht versehentlich feindliche Mobs ziehen.

### Verzauberte Vogelscheuche (Enchanted Scarecrow)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbar; verhindert im 16-Block-Radius Crop-Trampling und Mob-Spawns auf Ackerland und gibt umliegenden Crops +5% Wachstumschance. Herstellung: Stroh (Farmer's Delight) + Kürbis + Stock. Seltenheit: Common-Uncommon.
- **Integration:** Klassisches Stardew/Farm-Item; ergänzt Farmer's-Delight-Ackerbau und Mob-Proofing der Farm.
- **Quest:** Belohnung 'Schütze deine Ernte'-Quest.
- **Progression:** Frühe Farm-Schutz-Infrastruktur; Voraussetzung für ungestörte Großfarmen.
- **Probleme:** Spawn-Prevention-AoE via KubeJS/Block-Tick kann performancekostig sein — Radius/Tickrate begrenzen.

### Goldene Glückskatze (Maneki-Neko / Lucky Cat)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbare Deko-Statue; im 10-Block-Radius +3% bessere Villager-Trade-Preise und leicht erhöhte Loot-Luck. Selten als Sammelvariante (Bronze/Silber/Gold). Herstellung: Gold + Critters-Katzen-Bezug + Terrakotta. Seltenheit: Rare (Gold-Variante Legendary).
- **Integration:** Bleibt in Vanilla-Smaragd-Wirtschaft; ergänzt Marktstände + Trade Cycling; Animal-Crossing-Laden-Charme.
- **Quest:** 'Wohlstand für den Laden'-Quest; Sammelziel der drei Varianten.
- **Progression:** Wirtschafts-/Deko-Statussymbol mit Sammel-Tiering.
- **Probleme:** Trade-Preis-Modifikation via KubeJS auf Villager-Trades schwierig; ggf. nur Luck-Effekt umsetzen.

### Werkzeuggürtel des Handwerkers (Artisan's Tool Belt)  
*Typ: item*

- **Nutzen:** Effekt: Curios-Gürtel-Slot; hält 3 Werkzeuge griffbereit und gibt beim Bauen/Reparieren mit Create-Materialien -10% Materialkosten (KubeJS-Rezept-Tweak) sowie schnelleres Werkzeug-Wechseln. Herstellung: Leder + Brass (Create) + Schnalle. Seltenheit: Rare.
- **Integration:** Synergie mit Create-6-Crafting + Sophisticated-Storage-Workflow; verstärkt Handwerker-Rolle.
- **Quest:** Belohnung 'Meisterhandwerker' im Create-Progression-Kapitel.
- **Progression:** Create-orientiertes Effizienz-Artefakt im Mid-/Late-Game.
- **Probleme:** Material-Rabatt erfordert dynamische KubeJS-Rezept-Logik (komplex); ggf. auf Werkzeug-QoL reduzieren.

### Sternstaub-Splitter (Stardust Shard)  
*Typ: item*

- **Nutzen:** Effekt: Seltenes Sammel-/Crafting-Material; fällt nachts selten bei Meteor-Ambient-Events oder aus Endgame-Loot. Verwendet zur Aufwertung von Werkzeugen/Artefakten (z.B. Gießkanne→Sternen-Gießkanne). Seltenheit: Epic.
- **Integration:** Endgame-Upgrade-Material, das mehrere der Custom-Items (Gießkanne, Sichel, Charms) zu Sternen-Tiers veredelt; thematisch Stardew-'Iridium'.
- **Quest:** 'Sternensammler'-Endgame-Quest: sammle X Sternstaub.
- **Progression:** Top-Tier-Material-Gate, das die gesamte Custom-Item-Progression krönt.
- **Probleme:** Spawn-Event-Quelle definieren (Meteor-Ambient ist Aufwand); sonst aus Endgame-Struktur-Loot beziehen.

### Cozy-Teeservice (Cozy Tea Set)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbares Funktions-Möbel; Rechtsklick mit Let's-Do-Herbal-Brews-Tee gibt einen 5-Min-'Entspannt'-Buff (langsamere Hungerabnahme, +Regeneration beim Sitzen/Comforts-Stuhl). Herstellung: Porzellan (Terrakotta+Glas) + Teekanne. Seltenheit: Uncommon.
- **Integration:** Synergie mit Let's Do Herbal Brews + Comforts (Sitzen/Schlaf) + Furniture-Mods; Cozy-Pause-Ritual.
- **Quest:** 'Teezeit'-Quest; Daily-Buff-Ritual.
- **Progression:** Cozy-Lifestyle-Item; belohnt entspannte Spielroutinen.
- **Probleme:** Sitz-/Comforts-Integration für Buff-Trigger via KubeJS prüfen.

### Briefkasten der Nachbarschaft (Neighborhood Mailbox)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbarer Briefkasten; liefert 1x/Tag eine 'Post' — entweder Town-Talk-Nachricht eines NPCs, ein kleines Geschenk oder eine Quest-Einladung (FTB-Quest-Trigger). Herstellung: Eisen + Holz + Schild. Seltenheit: Uncommon.
- **Integration:** Tiefe Synergie mit Town Talk + FTB Quests + MineColonies-NPCs; Animal-Crossing-Brief-Mechanik.
- **Quest:** Kern-Hub für tägliche/wiederkehrende Quest-Auslieferung an Spieler.
- **Progression:** Daily-Engagement- und Quest-Verteilungssystem; Herzstück des sozialen Loops.
- **Probleme:** Tägliche Auslieferung + Quest-Trigger via KubeJS/FTB-Quest-API koppeln (mittlerer Aufwand).

### Zugticket (Steam Rail Ticket)  
*Typ: item*

- **Nutzen:** Effekt: Verbrauchs-Reise-Item; Rechtsklick an einer Steam'n'Rails-Station teleportiert/fast-travelt zu einer zuvor registrierten Bahnhof-Wegmarke. Herstellung: Papier + Smaragd + Eisennugget. Seltenheit: Common-Verbrauchsgut.
- **Integration:** Direkte Synergie mit Steam'n'Rails-Bahnhöfen + FTB-Chunks-Claims; reduziert Reise-Reibung im Town-Netz.
- **Quest:** 'Das Schienennetz'-Quest: verbinde 3 Bahnhöfe.
- **Progression:** Mobilitäts-Item, das großes vernetztes Town-Building belohnt.
- **Probleme:** Teleport via KubeJS an Wegmarken-NBT; Balance gegen echte Zug-Nutzung (Ticket bewusst als Komfort-Premium).

### Pokal des Erntefests (Harvest Festival Trophy)  
*Typ: item*

- **Nutzen:** Effekt: Prestige-Deko-Sammelobjekt; vergeben bei Abschluss großer Farming-/Event-Meilensteine, im Umkreis kleiner +XP-/Stimmungs-Buff. Mehrere Varianten (Bronze/Silber/Gold/Diamant) als Sammelreihe. Herstellung: nur via Quest-Belohnung, nicht craftbar. Seltenheit: Legendary Trophäe.
- **Integration:** Belohnungs-Endpunkt für FTB-Quest-Kapitel; Show-off-Deko für die Stadt.
- **Quest:** Direkte Krönung der großen Quest-Kapitel (Farming, Town, Create, Collection).
- **Progression:** Sichtbares Endgame-Prestige-Sammelziel; Trophäenschrank-Motivation.
- **Probleme:** Nur als Quest-Loot ausgeben (kein Rezept); Buff klein halten, primär Status.

### Glühwürmchen-Glas (Firefly Jar)  
*Typ: item*

- **Nutzen:** Effekt: Platzierbare/tragbare Lichtquelle (Lichtlevel ~10), getragen leicht beruhigender Ambient-Effekt; nachts mit erscheinenden Glühwürmchen (falls Critters/Naturalist-Firefly) befüllbar. Herstellung: Glasflasche + Critters-Glühwürmchen + Schnur. Seltenheit: Common.
- **Integration:** Synergie mit Critters & Companions/Naturalist (Glühwürmchen) + Supplementaries-Lichtdeko; Cozy-Nacht-Atmosphäre.
- **Quest:** Sommer-Event-Quest 'Fang die Glühwürmchen' (saisonal).
- **Progression:** Frühe Deko-/Licht-Sammel-Aktivität; sanfter saisonaler Loop.
- **Probleme:** Glühwürmchen-Entity-Verfügbarkeit prüfen (Verfuegbarkeit pruefen); sonst rein craftbar ohne Fang.

### Familienrezept-Buch (Family Recipe Book)  
*Typ: item*

- **Nutzen:** Effekt: Tragbares Item, das beim Halten freigeschaltete Farmer's-Delight-/HarvestCraft-Rezepte als JEI-Lesezeichen-Set zeigt und beim Kochen 1x/Tag eine 'Lieblingsgericht'-Mahlzeit mit Doppel-Sättigung gewährt. Herstellung: Buch + Farmer's-Delight-Kochbuch-Material. Seltenheit: Uncommon.
- **Integration:** Synergie mit Farmer's Delight + HarvestCraft + JEI + AppleSkin; Koch-Rollen-Item mit Story-Flair.
- **Quest:** 'Omas Rezepte'-Questreihe, die Gerichte freischaltet.
- **Progression:** Koch-Progressions-Hub; treibt das umfangreiche Food-System des Packs an.
- **Probleme:** Tägliche Doppel-Sättigungs-Mahlzeit via KubeJS-Cooldown; JEI-Lesezeichen-Steuerung evtl. nicht voll API-fähig (Verfuegbarkeit pruefen).


## qol (35)

### FerriteCore (NeoForge)  
*Typ: mod*

- **Nutzen:** Reduziert massiv den RAM-Verbrauch (oft 30-40% weniger Heap) durch Deduplizierung von Blockstates, Models und NBT. Bei einem so grossen Pack mit Create 6 + hunderten Bloecken ist das fast Pflicht fuer stabile Client- und AMP-Server-Performance.
- **Integration:** Reines Backend-Optimierungsmod, keine sichtbaren Aenderungen, keine Konflikte. Drop-in fuer Client und Server (side=both empfohlen, aber clientseitig reicht funktional). Bestaetigt verfuegbar 1.21.1 NeoForge (v7.0.2).
- **Quest:** Keines (Performance-Backend).
- **Progression:** Indirekt: stabilere lange Sessions = mehr Zeit fuer Progression/Farming-Grind ohne Memory-Leak-Lag.
- **Probleme:** Praktisch keine. In sehr seltenen Faellen historisch minimale Inkompatibilitaeten mit anderen Mixin-schweren Mods, aber mit ModernFix gut getestet.

### ModernFix  
*Typ: mod*

- **Nutzen:** Schnellere Ladezeiten (dynamische Ressourcen, lazy loading), geringerer RAM, behebt viele Vanilla/Forge-Bugs. Verkuerzt bei einem 200+-Mod-Pack die Welt-/Pack-Ladezeit spuerbar.
- **Integration:** Backend-Mod, side=both. Spielt sehr gut mit FerriteCore und Embeddium zusammen. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines direkt; verbessert nur QoL/Stabilitaet.
- **Probleme:** Einige aggressive Optionen (z.B. dynamic_resources) koennen selten mit JEI/Rezept-Mods kollidieren — in der Config abschaltbar. Mit JEI im Pack vorab testen.

### Embeddium (oder Sodium/NeoForge-Port)  
*Typ: mod*

- **Nutzen:** Drastische FPS-Steigerung durch modernen Rendering-Stack. Bei Create-Animationen, MineColonies-Doerfern und Fresh-Animations-Mobs entscheidend fuer fluessiges Gameplay auf Mid-Range-PCs.
- **Integration:** Clientseitig, ersetzt Vanilla-Renderer. Embeddium ist der etablierte NeoForge-Port mit breiter Addon-Kompatibilitaet. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines direkt.
- **Probleme:** Kann mit Shader-/Rendering-Mods kollidieren; Fresh Animations und manche Create-Visuals brauchen ggf. Embeddium-Addons (Embeddium++/Oculus-Aequivalent). Kompatibilitaet mit allen Visual-Mods pruefen (Verfuegbarkeit/Kompatibilitaet pruefen).

### Tom's Simple Storage Mod  
*Typ: mod*

- **Nutzen:** Vanilla-stiliges Storage-Netzwerk: viele Kisten ueber ein Storage-Terminal durchsuchbar/zugaenglich, ohne komplexe AE2/RS-Mechanik. Perfekt fuer ein Cozy-Pack als sanftes Lager-Management ohne Tech-Overkill.
- **Integration:** Bestaetigt 1.21.1 NeoForge. Passt thematisch besser als AE2/RS, ergaenzt Sophisticated Storage (Terminal kann die Boxen vernetzen). Wireless-Terminal als Upgrade-Item.
- **Quest:** FTB-Quest 'Baue dein erstes Lager-Terminal'; Wireless-Upgrade als Belohnungs-/Fortschritts-Item.
- **Progression:** Stufen: einfaches Terminal -> Crafting-Terminal -> Wireless-Terminal als Mid-Game-Ziel.
- **Probleme:** Kann mit Sophisticated Storage Upgrades teils doppeln; nur als optionale Vernetzungsschicht positionieren. Geringer Konfliktrisiko.

### Functional Storage  
*Typ: mod*

- **Nutzen:** Drawer-System (Item-Schubladen mit grossen Stacks, Stack-Upgrades, Compacting Drawers) fuer Bulk-Lagerung von Crops, Erzen und Create-Materialien. Klassisches Pack-QoL fuer Massenguetern.
- **Integration:** Funktioniert eigenstaendig und laesst sich mit Tom's Storage-Terminal vernetzen. Ergaenzt Sophisticated Storage (Drawer fuer Bulk, Boxen fuer Sortiment). Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Quest:** Quest-Kette zum Drawer-Controller; Belohnung: Stack-Upgrades.
- **Progression:** Upgrade-Tiers (1x -> 4x -> ... Stack-Multiplikatoren) als natuerliche Progression.
- **Probleme:** Ueberschneidung mit Sophisticated Storage; klare Rollenverteilung in Quests kommunizieren, sonst Redundanz.

### Clumps  
*Typ: mod*

- **Nutzen:** Buendelt XP-Orbs zu wenigen Entities. Reduziert Lag bei Mob-Farmen, Create-Mahlwerken und grossen Mengen — wichtig fuer Server-Performance auf AMP.
- **Integration:** Backend, side=both. Keine Gameplay-Aenderung ausser Performance. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Praktisch keine. Sehr stabil und weit verbreitet.

### EnchantmentDescriptions  
*Typ: mod*

- **Nutzen:** Zeigt im Tooltip, was jede Verzauberung tatsaechlich tut. Senkt die Einstiegshuerde fuer neue/casual Spieler eines Cozy-Packs erheblich.
- **Integration:** Clientseitig, JEI-kompatibel. Keine Konflikte. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines direkt; verbessert Verstaendnis fuer Enchanting-Quests.
- **Progression:** Keines.
- **Probleme:** Keine nennenswerten.

### Searchables  
*Typ: mod*

- **Nutzen:** Verbessert Suchleisten (z.B. in Creative/JEI-aehnlichen UIs und kompatiblen Mods) mit Autocomplete und besserer Filterung. Library-/QoL-Verbesserung fuer Such-UIs.
- **Integration:** Oft als Dependency anderer QoL-Mods (z.B. Configured/Catalogue-Oekosystem). Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Geringer Eigennutzen ohne kompatible Mods; meist als Lib mitgezogen. Niedrige Prioritaet, aber harmlos.

### Configured + Catalogue  
*Typ: mod*

- **Nutzen:** In-Game-Konfigurationsmenue fuer Mod-Configs (Configured) und durchsuchbares Mod-Listen-Menue mit Icons (Catalogue). Erspart Server-Admin und Spielern das Editieren von Config-Dateien.
- **Integration:** Clientseitig, integriert sich in das Mod-Options-Menue. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Nicht alle Mods exposen NeoForge-Configs sauber ueber Configured; rein additiv, kein Risiko.

### Mod Menu Aequivalent entfaellt — stattdessen 'Controlling'  
*Typ: mod*

- **Nutzen:** Durchsuchbare und kollisionswarnende Keybind-Verwaltung. Bei 200+ Mods mit dutzenden Keybinds (Create, Sophisticated, JourneyMap, Zoom etc.) unverzichtbar zum Aufloesen von Tastenkonflikten.
- **Integration:** Clientseitig, ersetzt das Vanilla-Controls-Menue. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Keine. Reines UI-Tool.

### BadOptimizations  
*Typ: mod*

- **Nutzen:** Sammlung clientseitiger Micro-Optimierungen (Beleuchtung, Entity-Culling-Vorbereitung, diverse Hotpaths). Ergaenzt Embeddium/ModernFix fuer zusaetzliche FPS.
- **Integration:** Clientseitig, stapelbar mit anderen Perf-Mods. Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Selten Konflikte mit anderen Rendering-Optimierern; bei Grafikfehlern einzelne Optionen deaktivieren.

### Entity Culling  
*Typ: mod*

- **Nutzen:** Rendert keine Entities/BlockEntities, die hinter Bloecken verdeckt sind. Grosser FPS-Gewinn bei MineColonies-Doerfern, vollen Create-Fabriken und Mob-/Tier-Dichte (Naturalist, Critters).
- **Integration:** Clientseitig, async culling. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Sehr selten flackernde Entities; bewaehrt und in fast jedem grossen Pack enthalten.

### Dynamic FPS  
*Typ: mod*

- **Nutzen:** Reduziert FPS/Render im Hintergrund oder bei Inaktivitaet. Spart Akku/CPU bei langen Cozy-Sessions, in denen man oft Create-Maschinen laufen laesst und wegtabbt.
- **Integration:** Clientseitig, keine Gameplay-Aenderung. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Keine nennenswerten.

### Chat Heads  
*Typ: mod*

- **Nutzen:** Zeigt Spieler-Avatare neben Chat-Nachrichten. Foerdert auf einem Cozy-SMP das soziale, gemeinschaftliche Gefuehl und erleichtert das Zuordnen von Nachrichten.
- **Integration:** Clientseitig, kombiniert sich gut mit 3D Skin Layers (bereits im Pack). Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Keine.

### AdvancementInfo / Better Advancements  
*Typ: mod*

- **Nutzen:** Verbesserter, durchsuchbarer Advancement-Screen mit Fortschrittsanzeige. Ergaenzt FTB Quests fuer das Vanilla-Advancement-Tree-Tracking (z.B. Sammel-/Collection-Achievements).
- **Integration:** Clientseitig, ersetzt nur das Advancement-UI. Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Quest:** Indirekt: Vanilla-Advancements als zusaetzliche Collection-Ziele neben FTB Quests sichtbarer.
- **Progression:** Macht Vanilla-Progression-Baum nachvollziehbarer.
- **Probleme:** Ueberschneidung mit FTB-Quests-Fokus; als Ergaenzung, nicht Ersatz positionieren.

### Legendary Tooltips  
*Typ: mod*

- **Nutzen:** Hochwertige, konfigurierbare Tooltip-Rahmen (Seltenheitsfarben, Borders). Hebt besondere Items (Artifacts, Quest-Belohnungen) optisch hervor — passt zum Collection/RPG-lite-Vibe.
- **Integration:** Clientseitig, rein kosmetisch fuer Tooltips. Spielt gut mit Artifacts (bereits im Pack). Verfuegbar 1.21.1 NeoForge.
- **Quest:** Quest-Belohnungs-Items koennen via Config besondere Rahmen erhalten (Wertigkeit signalisieren).
- **Progression:** Visuelle Seltenheits-Hierarchie unterstuetzt RPG-Gefuehl.
- **Probleme:** Konfiguration von Item-Tiers via KubeJS/Config noetig fuer vollen Effekt; sonst nur Vanilla-Rarities.

### Bookshelf (Library)  
*Typ: mod*

- **Nutzen:** Gemeinsame Library vieler QoL-/Content-Mods (u.a. von Darkhax-Mods wie EnchantmentDescriptions). Stellt Abhaengigkeiten bereit.
- **Integration:** Backend-Lib, side=both wie vom abhaengigen Mod gefordert. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Nur als Dependency sinnvoll; alleine kein Nutzen.

### Xaero's Minimap + WorldMap (alternativ/ergaenzend)  
*Typ: mod*

- **Nutzen:** Sehr performante Minimap mit Waypoints und separater Full-Worldmap. Alternative oder Ergaenzung zu JourneyMap fuer Spieler, die das schlankere Xaero-UI bevorzugen.
- **Integration:** JourneyMap ist bereits im Pack — Xaero waere redundant. Nur erwaehnenswert falls JourneyMap-Probleme auftreten. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Waypoints zu Quest-Zielen/Doerfern.
- **Progression:** Keines.
- **Probleme:** Direkte Redundanz mit JourneyMap — NICHT zusaetzlich einbauen, nur als Fallback-Option. Niedrige Prioritaet.

### Where Is It (Item-Locator)  
*Typ: mod*

- **Nutzen:** Markiert per JEI-Klick/Keybind, in welchen Kisten in der Naehe ein Item liegt. Loest das 'Wo habe ich das gelagert?'-Problem in einem Cozy-Base-Building-Pack mit vielen Storage-Optionen.
- **Integration:** Clientseitig, JEI-Integration. Ergaenzt Sophisticated Storage und Tom's/Functional Storage. Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Performance bei sehr vielen Kisten im Scan-Radius; Radius konfigurierbar.

### Item Borders  
*Typ: mod*

- **Nutzen:** Faerbt Slot-Hintergruende nach Item-Seltenheit in Inventar/Container. Schnellere visuelle Orientierung beim Sortieren grosser Inventare (Farming-Ertraege, Loot).
- **Integration:** Clientseitig, rein visuell. Kombiniert mit Legendary Tooltips. Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Geringer Funktionsumfang; reines Komfort-Plus.

### Polymorph  
*Typ: mod*

- **Nutzen:** Loest Rezept-Konflikte: bei mehreren moeglichen Crafting-Ergebnissen erscheint ein Auswahl-UI. Bei einem Pack mit Every Compat + vielen Wood/Food-Varianten extrem hilfreich.
- **Integration:** Clientseitig+serverseitig, integriert in Crafting-Table/JEI. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Sehr selten UI-Overlap mit anderen Crafting-Tweaks; gut getestet mit JEI.

### AmbientSounds  
*Typ: mod*

- **Nutzen:** Dynamische Umgebungsgeraeusche (Wald, Wasser, Wind, Hoehle) passend zu Biom/Wetter. Verstaerkt die Cozy/Immersion-Atmosphaere stark, besonders mit Serene Seasons und Terralith-Bioomen.
- **Integration:** Clientseitig. Harmoniert mit Serene Seasons/Terralith (bereits im Pack). Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Geschmackssache der Lautstaerke; gut konfigurierbar. Reines Audio-QoL.

### Sound Physics Remastered  
*Typ: mod*

- **Nutzen:** Reverb/Okklusion fuer raeumlichen Klang (Hall in Hoehlen/Gebaeuden, gedaempft hinter Waenden). Hebt Immersion fuer Base-Building und Erkundung deutlich.
- **Integration:** Clientseitig, kombiniert mit AmbientSounds. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Leichter CPU-Mehraufwand fuers Audio-Raytracing; in der Regel vernachlaessigbar.

### Visuality / Particle-Enhancer  
*Typ: mod*

- **Nutzen:** Fuegt subtile Ambient-Partikel hinzu (Funken an Lava, Pollen, fallende Blaetter). Cozy-Atmosphaere-Boost ohne Gameplay-Eingriff.
- **Integration:** Clientseitig, ergaenzt Fast Leaf Decay/Naturalist-Optik. Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Minimaler FPS-Kostenpunkt; abschaltbar pro Partikeltyp.

### Durability Tooltip / Durability Viewer  
*Typ: mod*

- **Nutzen:** Zeigt exakte Rest-Haltbarkeit von Tools/Ruestung als Zahl im Tooltip/HUD. QoL fuer Farming-Werkzeuge und Create-Equipment.
- **Integration:** Clientseitig. Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Geringer Umfang; harmlos.

### Highlighter (Block-Outline-Enhancer)  
*Typ: mod*

- **Nutzen:** Verbessert die Block-/Hitbox-Outline-Darstellung (dickere, farbige Umrisse). Praezisionshilfe beim Bauen mit vielen aehnlichen Deko-Bloecken (Chipped, Macaw's).
- **Integration:** Clientseitig. Ergaenzt das Building-fokussierte Deko-Lineup. Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Sehr kleiner Scope; reines Bau-Komfort-Plus.

### Jade Addons  
*Typ: mod*

- **Nutzen:** Erweitert das bereits enthaltene Jade um zusaetzliche Anzeigen (z.B. Create-Stress/Kinetik, MineColonies-/Progress-Infos). Bringt mehr kontextuelle Tooltips fuer die Kern-Mods.
- **Integration:** Setzt Jade voraus (bereits im Pack). Create-/MineColonies-Addons fuer Jade pruefen. Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit/Kompatibilitaet pruefen).
- **Quest:** Keines.
- **Progression:** Erleichtert das Verstehen von Create-Mechaniken (Stress-Anzeige) als Lernkurve.
- **Probleme:** Addon-Verfuegbarkeit fuer spezifische Mods schwankt; nur passende Addons einbinden.

### Forgivable Void / Backups via FTB? Stattdessen 'Spark'  
*Typ: mod*

- **Nutzen:** Performance-Profiler (CPU/Heap/Tick-Health) fuer Server-Admins. Bei einem so grossen Pack auf AMP essenziell, um TPS-Drops konkreten Mods/Maschinen zuzuordnen.
- **Integration:** Server- und clientseitig nutzbar, Ingame-Befehle /spark. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Reines Admin-Tool, kein Spielernutzen; harmlos und Standard in Server-Packs.

### FTB Backups 2 / serverseitige Backups  
*Typ: mod*

- **Nutzen:** Automatische Welt-Backups in Intervallen. Schuetzt das Cozy-SMP vor Datenverlust durch Crashes/Korruption — wichtig bei der grossen Mod-Anzahl.
- **Integration:** Serverseitig (AMP). Fuegt sich in das bereits genutzte FTB-Oekosystem (Quests/Chunks/Teams). Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Festplattenplatz/IO bei grossen Welten; Intervall und Retention konfigurieren. AMP kann Backups teils selbst — Doppelung pruefen.

### No Chat Reports  
*Typ: mod*

- **Nutzen:** Entfernt kryptographische Chat-Signierung/Reporting. Auf einem privaten Cozy-SMP gewuenschte Privatsphaere und vermeidet ungewollte Server-seitige Chat-Validierungsprobleme.
- **Integration:** Client+server, side=both fuer vollen Effekt. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Nur sinnvoll wenn alle/der Server es nutzen; rein gemeinschaftliche Entscheidung.

### Better Third Person  
*Typ: mod*

- **Nutzen:** Entkoppelt Kamera von Blickrichtung in 3rd Person (freie Kameradrehung). Verbessert Screenshots/Showcase von Base und Outfits (3D Skin Layers, Fresh Animations) auf einem sozialen SMP.
- **Integration:** Clientseitig, kombiniert mit 3D Skin Layers/Fresh Animations (bereits im Pack). Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Reines Kamera-/Showcase-Feature; keine Konflikte.

### Inventory Profiles Next (IPN) — Pruefung  
*Typ: mod*

- **Nutzen:** Sehr maechtiges Auto-Sort/Profiles-Inventory-Management. Alternative/Ergaenzung zu Inventory Tweaks ReFoxed mit Profil-Speicherung und feineren Sortierregeln.
- **Integration:** ReFoxed ist bereits im Pack — IPN waere teils redundant und kann mit ReFoxed/Mouse Tweaks um Sort-Tasten konkurrieren. Nur als Ersatz erwaegen, nicht parallel. NeoForge-Verfuegbarkeit pruefen.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Direkter Konflikt/Redundanz mit Inventory Tweaks ReFoxed und Mouse Tweaks — NICHT zusammen einbauen. Niedrige Prioritaet.

### Default Options / Blay's Default Options  
*Typ: mod*

- **Nutzen:** Erlaubt es dem Pack-Ersteller, sinnvolle Standard-Einstellungen (Keybinds, Video, Mod-Configs) auszuliefern, die Spieler beim ersten Start uebernehmen. Senkt Onboarding-Reibung enorm.
- **Integration:** Clientseitig im Packwiz-Pack. Ideal um Embeddium/Controlling/JourneyMap-Defaults vorzukonfigurieren. Verfuegbar 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Pflege der Default-Configs noetig; bei Updates Defaults aktuell halten.

### Shulker Box Tooltip  
*Typ: mod*

- **Nutzen:** Zeigt beim Hovern den Inhalt von Shulker-Boxen (und ggf. kompatiblen Behaeltern) im Tooltip. Schnelles Lager-/Transport-Management ohne Platzieren.
- **Integration:** Clientseitig. Ergaenzt Sophisticated Storage/Backpacks-Workflow. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Inhaltsanzeige fremder modded Container nur bei Kompatibilitaet; Vanilla-Shulker garantiert.

### Cloth Config API  
*Typ: mod*

- **Nutzen:** Verbreitete Config-Screen-Library, Voraussetzung vieler QoL-Mods (z.B. einige Map-/UI-Mods). Stellt einheitliche Config-UIs bereit.
- **Integration:** Backend-Lib, side wie vom abhaengigen Mod verlangt. Verfuegbar 1.21.1 NeoForge.
- **Quest:** Keines.
- **Progression:** Keines.
- **Probleme:** Nur als Dependency relevant; alleine kein Nutzen.


## quest-designer (52)

### Ein neuer Anfang — Hof urbar machen  
*Typ: quest*

- **Nutzen:** Ziel: 10 Grasblöcke zu Ackerboden hacken, 1 Holzhacke craften, erstes Pam's-/Vanilla-Saatgut pflanzen. Belohnung: 16 Karottensamen, 1 Farmer's Delight Kochtopf, 50 FTB-Quest-XP. Lehrt den Kern-Loop in den ersten 5 Minuten.
- **Integration:** Erste Quest im FTB-Quest-Kapitel 'Willkommen im Tal'; nutzt Farmer's Delight Werkzeug-Tab. Auto-detect über item observed.
- **Quest:** Klassischer Stardew-Tag-1-Moment; entsperrt das gesamte Farming-Kapitel.
- **Progression:** Wurzelquest des Tech-Trees — schaltet 'Erste Ernte' und 'Bewässerung' frei.
- **Probleme:** Achtung: Pam's-Saatgut hat eigene Crafting-Pfade — KubeJS-Check, dass Startsamen erreichbar sind ohne Loot-Glück.

### Erste Ernte  
*Typ: quest*

- **Nutzen:** Ziel: je 8 Karotten, Kartoffeln und Weizen ernten. Belohnung: Sophisticated Backpack (Leder-Tier), 1 Diamant, Rezept-Freischaltung Farmer's Delight Schneidebrett. Belohnt die erste vollständige Wachstumsschleife.
- **Integration:** Folgt direkt auf 'Ein neuer Anfang'; OR-Task-Logik über JEI-Tags crops.
- **Quest:** Stardew 'erste Verkaufskiste'-Gefühl; motiviert Skalierung.
- **Progression:** Schaltet Kapitel 'Küche & Kochen' (Farmer's Delight) und 'Bewässerung' frei.
- **Probleme:** Serene-Seasons-Saison könnte Crops blockieren — Quest sollte saisonunabhängige Crops verlangen oder Gewächshaus-Hinweis geben.

### Wasser marsch — Bewässerungssystem  
*Typ: quest*

- **Nutzen:** Ziel: Create-Pumpe + Wasserrad bauen, ein Feld mit fließendem Wasser bewässern. Belohnung: 4 Create-Messingbleche, Blueprint 'Mechanischer Pflug', 100 XP. Verheiratet Farming mit Create-Fokus früh.
- **Integration:** Brücke zwischen Farming- und Create-Kapitel; nutzt Create 6 Pumpe/Wasserrad.
- **Quest:** Macht Create zur natürlichen Antwort auf 'Gießen nervt' — sehr Stardew-Sprinkler-Vibe.
- **Progression:** Tor zum Create-Automatisierungs-Zweig (Mechanical Harvester später).
- **Probleme:** Create-Pumpe braucht Kinetik-Setup; Quest muss Wasserrad als Startenergie klar anleiten, sonst Frust.

### Der Dorfplatz erwacht  
*Typ: quest*

- **Nutzen:** Ziel: MineColonies Town Hall platzieren und ersten Bürger (Builder) anwerben. Belohnung: 1 MineColonies Bauwerkzeug, 5 Bauholz-Bundles, Town-Reputation +1. Startet das Town-Building.
- **Integration:** Eröffnet das 'Gemeinde & Stadt'-Kapitel; nutzt MineColonies + Structurize.
- **Quest:** Pelican-Town-Aufbaugefühl; Spieler wird Bürgermeister statt nur Farmer.
- **Progression:** Schaltet Bürger-Berufsketten und Reputations-System frei.
- **Probleme:** MineColonies-Onboarding ist steil — Quest sollte auf das eigene MineColonies-University/Tutorial verweisen, nicht duplizieren.

### Willkommen, Nachbarn  
*Typ: quest*

- **Nutzen:** Ziel: 3 Easy-Villagers in Town locken/umsiedeln und je 1 Beruf zuweisen (Bauer, Bibliothekar, Schmied). Belohnung: Smaragd x12, 1 Glocke (Bells & Whistles), NPC-Begrüßungsdialog via Town Talk. Bringt Leben ins Dorf.
- **Integration:** Nutzt Easy Villagers (Pick-up) + Town Talk + Bells & Whistles; im Stadt-Kapitel.
- **Quest:** NPC-Beziehungsanfang wie Stardew-Nachbarn; Town Talk gibt Persönlichkeit.
- **Progression:** Voraussetzung für Beziehungs- und Handelsketten.
- **Probleme:** Town Talk ist meist client-seitig kosmetisch — keine echte Quest-Triggerbarkeit; Quest muss auf Villager-Beruf-Erkennung bauen.

### Der Dorfladen öffnet  
*Typ: quest*

- **Nutzen:** Ziel: Mit einem Bauern-Villager 3x handeln (Smaragde gegen Crops). Belohnung: Trade Cycling Freischalt-Hinweis, 1 Sophisticated Storage Truhe, 8 Smaragde. Etabliert Vanilla-Smaragd-Wirtschaft.
- **Integration:** Nutzt Guard Villagers + Trade Cycling; Wirtschafts-Kapitel.
- **Quest:** Stardew-Pierre's-General-Store-Gefühl mit Vanilla-Mitteln.
- **Progression:** Schaltet 'Wochenmarkt'-Daily/Weekly-Quests frei.
- **Probleme:** Trade-Detection in FTB Quests ist heikel; ggf. über 'Smaragde im Inventar erreichen' statt echtem Trade-Hook lösen (KubeJS).

### Das Museum — Grundstein  
*Typ: quest*

- **Nutzen:** Ziel: Display-Case/Vitrine (Supplementaries 'Statue' oder Handcrafted Glasvitrine) bauen und 1 Fossil/Ausgrabungsfund einlegen. Belohnung: 1 Pinsel, Schaufel (Eisen), 'Kurator'-Titel. Startet das Sammel-Museum.
- **Integration:** Nutzt Supplementaries/Handcrafted Vitrinen + Vanilla-Archäologie; Museums-Kapitel.
- **Quest:** Gunther's-Museum-Kernschleife; langfristiger Sammeltrieb.
- **Progression:** Wurzel des großen Sammel-Trees (Mineralien, Fische, Artefakte).
- **Probleme:** Vanilla hat begrenzte Display-Items; KubeJS könnte 'Museum-Slot-Block' brauchen, sonst zählt Quest nur 'Item besitzen' statt 'ausgestellt'.

### Mineralien-Sammlung: Gesteine  
*Typ: quest*

- **Nutzen:** Ziel: 12 verschiedene Steinarten/Erze sammeln (inkl. Terralith/Tectonic-Varianten). Belohnung: Spitzhacke (Eisen, Effizienz I), 30 XP, Museums-Reputation +2. Treibt Erkundung.
- **Integration:** Nutzt Terralith/Tectonic-Biome + JER für Erz-Locations; Museums-Sammelkapitel.
- **Quest:** 'Geologe'-Sammelbingo wie Stardew-Mineralien.
- **Progression:** Teil des Museum-Vervollständigungs-Trees, schaltet 'Edelsteine' frei.
- **Probleme:** Terralith-Steinvarianten-Tags müssen geprüft werden, dass alle 12 erreichbar sind; (Verfügbarkeit/Tags prüfen).

### Aquarium — Fang des Tages  
*Typ: quest*

- **Nutzen:** Ziel: 5 verschiedene Fischarten via Aquaculture-Angel fangen und in Fish-Tank ausstellen. Belohnung: Aquaculture-Angel Upgrade (Eisenhaken), 1 Köderfass, 'Angler'-Abzeichen. Fischsammlung startet.
- **Integration:** Nutzt Aquaculture + Fish of Thieves; Museums-/Aquarium-Kapitel.
- **Quest:** Stardew-Angel-Sammelbuch; sehr cozy Aktivität.
- **Progression:** Schaltet 'Legendäre Fische' und Köder-Crafting frei.
- **Probleme:** Fish of Thieves und Aquaculture haben überlappende Fische — Quest sollte klar einen der beiden als Quell-Mod definieren, um Doppelzählung zu vermeiden.

### Legendärer Fang  
*Typ: quest*

- **Nutzen:** Ziel: 1 seltenen Fish-of-Thieves-Fisch (z.B. Trophäen-Variante) fangen. Belohnung: Goldene Angel (Aquaculture Neptunium-Hinweis), 2 Diamanten, Trophäen-Vitrine. Endgame-Angeln.
- **Integration:** Folgt auf 'Aquarium'; nutzt Fish of Thieves Trophy-System.
- **Quest:** Stardew-Legendärfisch-Jagd; prestigeträchtig.
- **Progression:** Krönung des Angel-Trees.
- **Probleme:** Trophy-Fische haben niedrige Spawnrate — Quest könnte frustrierend lang sein; ggf. Köder-Hilfe via Belohnung der Vorquest geben.

### Die erste Kuh  
*Typ: quest*

- **Nutzen:** Ziel: 1 Kuh zähmen/einzäunen, 4 Eimer Milch gewinnen. Belohnung: Heuballen x4, Farmer's Delight Käse-Rezept, 1 Eimer. Startet Tierhaltung.
- **Integration:** Nutzt Vanilla-Tiere + Smarter Farmers + Farmer's Delight Molkerei; Tierhaltungs-Kapitel.
- **Quest:** Stardew-Scheunen-Tier-Gefühl; Milch→Käse-Veredelung.
- **Progression:** Schaltet 'Scheune bauen' und Käserei/Vinery-Verarbeitung frei.
- **Probleme:** Käse via Farmer's Delight vs. Let's Do Meadow — KubeJS muss klären welches Käse-Item die Quest erwartet.

### Hühnerhof  
*Typ: quest*

- **Nutzen:** Ziel: 3 Hühner halten, 16 Eier sammeln, 1 Rührei (Farmer's Delight) kochen. Belohnung: Critters & Companions Begleiter-Hinweis, Nest-Box (Handcrafted), 20 XP. Erweitert Tierhaltung.
- **Integration:** Vanilla-Hühner + Farmer's Delight; Tierhaltungs-Kapitel.
- **Quest:** Cozy-Morgenroutine 'Eier einsammeln'.
- **Progression:** Teil der Tier-Sammlung, führt zu 'Vollständige Scheune'.
- **Probleme:** Gering; Eier-Sammeln gut auto-detectbar.

### Treuer Hofhund  
*Typ: quest*

- **Nutzen:** Ziel: Einen Companions-Dogfolk/Critters-Hund zähmen und benennen. Belohnung: Hundeknochen-Stack, 1 Halsband (Artifacts-fähig?), 'Bester Freund'-Titel. Emotionale Begleiter-Quest.
- **Integration:** Nutzt Companions Dogfolk + Critters & Companions; Beziehungs-/Tier-Kapitel.
- **Quest:** Stardew-Haustier-Bindung; rein cozy.
- **Progression:** Schaltet Begleiter-Pflege-Daily ('Hund streicheln') frei.
- **Probleme:** Zähm-Detection variiert je Companion-Mod; KubeJS-Event auf Tame-Entity prüfen.

### Frühling: Blütenpracht  
*Typ: quest*

- **Nutzen:** Ziel: Während der Frühlings-Saison (Serene Seasons) 6 Blumenarten + 3 Frühlingscrops ernten. Belohnung: Dye Depot Farbpalette, Bienenstock, Saisonal-Reputation +2. Erste Seasonal-Quest.
- **Integration:** Nutzt Serene Seasons API + Dye Depot + Vanilla-Bienen; Saison-Kapitel.
- **Quest:** Stardew-Frühlings-Festival-Stimmung.
- **Progression:** Teil des 4-Saisons-Zyklus, schaltet Sommer-Quest frei.
- **Probleme:** Serene-Seasons-Saison-Erkennung in FTB Quests braucht KubeJS-Bridge (Quest nur in Saison X abgebbar) — Aufwand mittel.

### Sommer: Hitze & Honig  
*Typ: quest*

- **Nutzen:** Ziel: Im Sommer 5 Bienenstöcke betreiben, 10 Honigflaschen + 4 Wabenblöcke gewinnen. Belohnung: Kerzen-Set (Supplementaries), Honig-Kuchen-Rezept (Confectionery), 30 XP. Sommer-Saisonal.
- **Integration:** Vanilla-Bienen + Create Confectionery; Saison-Kapitel.
- **Quest:** Sommerliche Imker-Aktivität, Stardew-Honig-Artisan-Gefühl.
- **Progression:** Schaltet Herbst-Quest und Süßwaren-Zweig frei.
- **Probleme:** Saison-Lock wie oben; Bienen-Pathing kann buggen — kein hartes Zeitlimit setzen.

### Herbst: Erntedank  
*Typ: quest*

- **Nutzen:** Ziel: Im Herbst 5 Kürbisse + Bountiful-Fares-Festmahl mit 4 Gerichten zubereiten. Belohnung: Vogelscheuche (Handcrafted/Supplementaries), Festtafel-Deko, Saison-Reputation +3. Herbst-Festmahl.
- **Integration:** Nutzt Bountiful Fares + Farmer's Delight Feast-Mechanik; Saison-Kapitel.
- **Quest:** Stardew-'Stardew Valley Fair'-Erntedank-Vibe.
- **Progression:** Schaltet Winter-Quest frei.
- **Probleme:** Bountiful Fares Feast-Item-Erkennung prüfen; Saison-Lock-Aufwand.

### Winter: Stille Tage  
*Typ: quest*

- **Nutzen:** Ziel: Im Winter ein Gewächshaus (Glasdach via Macaw's Roofs) bauen und darin 1 Crop trotz Saison anbauen. Belohnung: Comforts-Schlafsack, warme Lichterkette, 1 Diamant. Winter-Überbrückung.
- **Integration:** Macaw's Roofs + Serene Seasons (Gewächshaus umgeht Saison) + Comforts; Saison-Kapitel.
- **Quest:** Stardew-Winter 'nichts wächst draußen'-Problem elegant gelöst.
- **Progression:** Schließt den Saison-Zyklus, schaltet 'Ganzjahres-Farmer'-Meilenstein frei.
- **Probleme:** Ob Serene-Seasons-Gewächshaus-Mechanik Crops wirklich wachsen lässt, hängt an Config (greenhouse glass) — prüfen und ggf. Fertilized Dirt nutzen.

### Frühlingsfest im Dorf  
*Typ: quest*

- **Nutzen:** Ziel: Dorfplatz mit 8 Dekoblöcken (Bells & Whistles, Another Furniture) schmücken und 3 Villager versammeln. Belohnung: Festival-Banner, Blumenkranz (Artifacts-Kopf?), Town-Reputation +5. Seasonal-Event.
- **Integration:** Deko-Mods + Easy Villagers; Saison-/Stadt-Kapitel.
- **Quest:** Stardew-Dorffest mit Aufbau-Komponente.
- **Progression:** Wiederkehrendes saisonales Event-Template.
- **Probleme:** 'Villager versammeln' schwer zu detecten — ggf. über Block-Platzierung in Radius lösen statt Entity-Position.

### Pam's Speisekammer  
*Typ: quest*

- **Nutzen:** Ziel: 10 verschiedene Pam's HarvestCraft-Crops anbauen und 1 Markt-Stand (Supplementaries) befüllen. Belohnung: HarvestCraft Markt-Block, 1 Kompostfass, 'Selbstversorger'-Titel. Crop-Vielfalt.
- **Integration:** Pam's HarvestCraft 2 Crops + Supplementaries; Farming-Kapitel.
- **Quest:** Stardew-'jede Crop einmal angebaut'-Sammlung.
- **Progression:** Schaltet erweiterte HarvestCraft-Gerichte frei.
- **Probleme:** Pam's hat sehr viele Crops; 10-Auswahl muss biome-/saisonübergreifend machbar sein.

### Der erste Wein  
*Typ: quest*

- **Nutzen:** Ziel: Let's-Do-Vinery Weinreben anbauen, Trauben pressen, 1 Flasche Wein keltern. Belohnung: Weinregal, 2 Weingläser, Artisan-Reputation +2. Veredelungs-Quest.
- **Integration:** Nutzt Let's Do Vinery vollständig; Artisan-/Küchen-Kapitel.
- **Quest:** Stardew-Artisan-Goods (Wein als Premium-Produkt).
- **Progression:** Schaltet Brennerei/Met (Herbal Brews) frei.
- **Probleme:** Vinery-Wachstumszeit lang; Quest sollte keine Tageslimit-Daily sein.

### Brauerei-Meister  
*Typ: quest*

- **Nutzen:** Ziel: 3 verschiedene Getränke aus Let's-Do Herbal Brews + Vinery herstellen. Belohnung: Theken-Set (Let's Do Beachparty), Met-Fass, 40 XP. Erweitert Artisan-Goods.
- **Integration:** Let's Do Herbal Brews + Vinery; Artisan-Kapitel.
- **Quest:** Cozy-Taverne aufbauen wie Stardew-Saloon.
- **Progression:** Schaltet 'Dorftaverne eröffnen' frei.
- **Probleme:** Herbal Brews 1.21.1 NeoForge (Verfügbarkeit prüfen) — falls nicht vorhanden, nur Vinery-Getränke verlangen.

### Die Dorftaverne  
*Typ: quest*

- **Nutzen:** Ziel: Eine Taverne mit Bar (Another Furniture), 4 Sitzplätzen und Getränke-Vorrat bauen, 1 NPC als Wirt ansiedeln. Belohnung: Create Cafe Espressomaschine, Speisekarte-Schild, Town-Reputation +5. Community-Hub.
- **Integration:** Deko + Create Cafe + Villager; Stadt-Kapitel.
- **Quest:** Stardew-Saloon als sozialer Treffpunkt.
- **Progression:** Schaltet 'Dorf-Wirtschaft'-Weekly frei.
- **Probleme:** Subjektive Bau-Quest schwer zu validieren — über Schlüsselblöcke (Bar+Stühle+Espressomaschine platziert) prüfen.

### Süße Versuchung — Konditorei  
*Typ: quest*

- **Nutzen:** Ziel: Mit Create Confectionery 3 Süßwaren herstellen (z.B. Bonbon, Schokolade, Kuchen). Belohnung: Confectionery Mixer-Upgrade, Geschenkbox, 'Konditor'-Titel. Süßwaren-Produktion.
- **Integration:** Create Confectionery + Create-Automatisierung; Create-/Küchen-Kapitel.
- **Quest:** Stardew-Geschenke-für-Beziehungen (Süßes mögen viele NPCs).
- **Progression:** Liefert Geschenk-Items für Beziehungs-Quests.
- **Probleme:** Confectionery braucht Create-Maschinen; Quest sollte nach Create-Grundlagen kommen, nicht früh.

### Geschenk für den Nachbarn  
*Typ: quest*

- **Nutzen:** Ziel: Einem bestimmten Villager 3 Tage in Folge ein 'geliebtes' Geschenk geben (via KubeJS-Item-on-Villager). Belohnung: Beziehungs-Level +1, Dankesbrief-Item, 1 Diamant. Beziehungs-Kern.
- **Integration:** KubeJS-Custom-Event + Town Talk Dialog; Beziehungs-Kapitel.
- **Quest:** Direktes Stardew-Beziehungs-Herz-System.
- **Progression:** Wurzel des Beziehungs-Trees (Freund → bester Freund).
- **Probleme:** Vanilla-Villager haben kein Geschenk-System — komplett KubeJS-Custom nötig (rechtsklick-mit-Item-auf-Villager, NBT-Tracking). Hoher Aufwand, markieren.

### Beste Freunde fürs Leben  
*Typ: quest*

- **Nutzen:** Ziel: Beziehungs-Level 5 mit einem NPC erreichen (kumulierte Geschenke/Trades). Belohnung: NPC zieht in Town ein, exklusives Rezept, 'Vertrauter'-Titel. Beziehungs-Höhepunkt.
- **Integration:** Baut auf KubeJS-Beziehungssystem aus 'Geschenk für den Nachbarn'.
- **Quest:** Stardew-10-Herzen-Event-Äquivalent.
- **Progression:** Endpunkt einer NPC-Beziehungskette pro Charakter.
- **Probleme:** Abhängig vom Custom-Beziehungssystem; ohne Mod-Support viel KubeJS-State-Management.

### Reputations-Aufstieg: Geschätzter Bürger  
*Typ: quest*

- **Nutzen:** Ziel: Town-Reputation 25 sammeln (aus diversen Stadt-Quests). Belohnung: Bürger-Abzeichen, Zugang zu Premium-Villager-Trades, 5 Diamanten. Reputations-Meilenstein.
- **Integration:** FTB-Quest-Reward-Table als Reputations-Zähler; Stadt-Kapitel.
- **Quest:** Stardew-'Community-Ansehen'-Fortschritt.
- **Progression:** Mehrstufiger Reputations-Tree (Bürger→Stadtrat→Bürgermeister).
- **Probleme:** Reputation als FTB-Quest-Zahl simulieren — keine echte Mod-Mechanik, rein questbasiert. Sauber dokumentieren.

### Bürgermeister von Cozy Town  
*Typ: quest*

- **Nutzen:** Ziel: Reputation 100 + 10 Bürger + Town Hall maximal ausgebaut (MineColonies). Belohnung: Bürgermeister-Hut (Artifacts), Stadt-Banner, Endgame-Titel. Town-Endgame.
- **Integration:** MineColonies-Ausbaustufe + Reputations-Tree; Stadt-Kapitel-Finale.
- **Quest:** Krönung des gesamten Town-Building-Bogens.
- **Progression:** Top-Knoten des Stadt-Trees.
- **Probleme:** MineColonies-Town-Hall-Level-Detection via KubeJS möglich aber fiddly; Verfügbarkeit der API prüfen.

### Tagwerk: Frische Eier  
*Typ: quest*

- **Nutzen:** Ziel (Daily): 6 Eier einsammeln und beim Dorfladen abgeben. Belohnung: 4 Smaragde + 10 XP, täglich wiederholbar. Daily-Routine.
- **Integration:** FTB Quests 'repeatable'-Flag; Daily-Kapitel.
- **Quest:** Stardew-tägliche-Hofroutine.
- **Progression:** Liefert stetiges Smaragd-Einkommen für Wirtschaft.
- **Probleme:** FTB Quests Cooldown/Repeatable-Konfiguration prüfen; KubeJS-Daily-Reset evtl. nötig.

### Tagwerk: Lieferung an die Küche  
*Typ: quest*

- **Nutzen:** Ziel (Daily): 1 zufällig gefordertes Farmer's-Delight-Gericht abliefern. Belohnung: 6 Smaragde + Gewürz-Sack, täglich. Variable Daily.
- **Integration:** KubeJS-Random-Daily-Pick aus Gericht-Pool; Daily-Kapitel.
- **Quest:** Stardew-'Help-Wanted'-Schwarzes-Brett.
- **Progression:** Treibt Koch-Vielfalt und Wirtschaft.
- **Probleme:** Zufalls-Daily braucht KubeJS-Logik; FTB Quests allein kann kein Random-Item-of-the-day — Custom nötig.

### Schwarzes Brett: Gesuche  
*Typ: quest*

- **Nutzen:** Ziel (Daily): 1 von 3 wählbaren Sammelaufträgen erfüllen (Holz / Erz / Crops). Belohnung: 5 Smaragde + Wahl-Reward, täglich. Wählbare Daily.
- **Integration:** FTB-Quest OR-Tasks + Supplementaries Notice-Board als physisches Objekt; Daily-Kapitel.
- **Quest:** Stardew-'Help Wanted'-Brett direkt nachgebaut.
- **Progression:** Konstantes Early-Mid-Game-Einkommen.
- **Probleme:** Physisches Brett ist nur Deko; Quest-Logik bleibt in FTB-UI. Erwartungsmanagement nötig.

### Wochenaufgabe: Großlieferung  
*Typ: quest*

- **Nutzen:** Ziel (Weekly): 64 einer Wochen-Crop + 16 verarbeitete Güter abliefern. Belohnung: 1 Diamant + Sophisticated Storage Upgrade + Reputation +3, wöchentlich. Größere Weekly.
- **Integration:** FTB Quests Weekly-Cooldown; Weekly-Kapitel.
- **Quest:** Stardew-'Bundle'-Großaufgabe.
- **Progression:** Skaliert Farm-Ausbau und Lager.
- **Probleme:** Wöchentlicher Reset braucht stabile Server-Zeit; FTB-Quest-Cooldown-Persistenz auf AMP testen.

### Community-Bundle: Frühlingsregal  
*Typ: quest*

- **Nutzen:** Ziel: Ein 6-Slot-'Bundle' füllen (1 Erdbeere, 1 Tulpe, 1 Honig, 1 Forelle, 1 Ahornsirup, 1 Karotte). Belohnung: schaltet Bewässerungs-Upgrade fürs ganze Dorf frei, Bundle-Trophäe. Community-Center-Mechanik.
- **Integration:** FTB-Quest-Gruppe als 'Bundle'; nutzt Aquaculture/Vinery/Pam's; Community-Kapitel.
- **Quest:** Direkte Stardew-Community-Center-Bundle-Adaption.
- **Progression:** Mehrere Bundles → 'Community Center repariert'-Meilenstein.
- **Probleme:** Bundle-Optik via FTB-Quest-Layout möglich; Belohnungs-Freischaltung 'fürs Dorf' ist symbolisch, real nur Item.

### Community-Bundle: Handwerkerregal  
*Typ: quest*

- **Nutzen:** Ziel: 1 Wein, 1 Käse, 1 Honig, 1 Marmelade (Bountiful Fares), 1 Bier, 1 Saft abgeben. Belohnung: Create Mechanical Press, Artisan-Trophäe, Reputation +4. Artisan-Bundle.
- **Integration:** Let's Do + Bountiful Fares + Create; Community-Kapitel.
- **Quest:** Stardew-Pantry-Artisan-Bundle.
- **Progression:** Schaltet Premium-Artisan-Automatisierung frei.
- **Probleme:** Item-IDs der Marmeladen/Säfte über mehrere Mods sammeln und in KubeJS-Tag bündeln.

### Community-Bundle: Schatzkammer  
*Typ: quest*

- **Nutzen:** Ziel: 1 Diamant, 1 Smaragd, 1 Gold-Erz, 1 Amethyst, 1 Artifacts-Fund, 1 Fossil abgeben. Belohnung: Geode-Aufbrecher (Create?), Edelstein-Vitrine, Museums-Reputation +5. Mineralien-Bundle.
- **Integration:** Vanilla-Erze + Artifacts + Archäologie; Community-/Museums-Kapitel.
- **Quest:** Stardew-Boiler-Room-Schatzbündel.
- **Progression:** Verzahnt Museum mit Community Center.
- **Probleme:** Artifacts-Items aus Truhen-Loot — RNG-abhängig, könnte hängen; alternative Quellen anbieten.

### Mein erstes Zuhause  
*Typ: quest*

- **Nutzen:** Ziel: Ein Haus mit Bett (Comforts), Truhe, Ofen und 1 Tür bauen und 1 Nacht darin schlafen. Belohnung: Another Furniture Sofa, Teppich, 'Eigenheim'-Titel. Wohn-Quest.
- **Integration:** Comforts + Another Furniture + Interiors; Early-Kapitel.
- **Quest:** Stardew-Farmhaus-Startgefühl.
- **Progression:** Schaltet 'Haus-Erweiterung'-Quests frei.
- **Probleme:** '1 Nacht geschlafen' via Sleep-Event detectbar; Schlüsselblock-Platzierung sonst subjektiv.

### Heim-Erweiterung: Wohnzimmer  
*Typ: quest*

- **Nutzen:** Ziel: Haus um einen Raum erweitern, 5 Möbelstücke (Macaw's/Handcrafted/Interiors) platzieren. Belohnung: Kamin (Supplementaries), Wandbild, 30 XP. Dekorations-Progression.
- **Integration:** Möbel-Mods; Wohn-Kapitel.
- **Quest:** Stardew-Haus-Upgrades bei Robin.
- **Progression:** Mehrstufige Heim-Ausbaukette.
- **Probleme:** Platzierungs-Zählung über Block-Tags machbar; rein kosmetisch, leicht.

### Mechanischer Erntehelfer  
*Typ: quest*

- **Nutzen:** Ziel: Create 'Mechanical Harvester' + 'Mechanical Plough' an einem Drehkraft-Setup bauen und ein Feld automatisch abernten. Belohnung: 4 Andesit-Maschinen, Blueprint Belt-System, 'Ingenieur-Farmer'-Titel. Automatisierung.
- **Integration:** Create 6 Harvester/Plough; Create-Kapitel.
- **Quest:** Stardew-Junimo-Harvester-Äquivalent mit Create-Tiefe.
- **Progression:** Schaltet vollautomatische Farm-Module frei.
- **Probleme:** Create-Mechanical-Harvester erntet bestimmte Crops anders — Quest sollte vanilla-kompatibles Feld verlangen.

### Vom Feld zur Flasche — Vollautomatik  
*Typ: quest*

- **Nutzen:** Ziel: Eine Create-Kette bauen, die Crop erntet → verarbeitet → in Sophisticated Storage einlagert (z.B. Weizen→Mehl→Brot). Belohnung: Create Brass-Tier-Maschinen, Auto-Output-Truhe, 50 XP. Fortgeschrittene Automatisierung.
- **Integration:** Create 6 + Create-Sophisticated-Integration + Farmer's Delight; Create-Kapitel.
- **Quest:** Befriedigt Factory-Fans, hält Cozy-Anbindung.
- **Progression:** Mittlerer Knoten des Create-Trees Richtung TFMG.
- **Probleme:** Komplexe Validierung — Quest prüft am besten nur End-Item-Output-Menge, nicht das Setup selbst.

### Sammlung: Kochbuch komplett  
*Typ: quest*

- **Nutzen:** Ziel: 25 verschiedene Farmer's-Delight-/Delight-Addon-Gerichte mindestens einmal kochen. Belohnung: Goldener Kochlöffel (Artifacts?), Meisterkoch-Vitrine, 'Sternekoch'-Titel. Koch-Sammlung.
- **Integration:** Alle Delight-Addons + KubeJS-Crafted-Tracking; Sammel-Kapitel.
- **Quest:** Stardew-Kochbuch-Vervollständigung.
- **Progression:** Großer Sammel-Meilenstein der Küche.
- **Probleme:** 25 Gerichte über viele Addons tracken — KubeJS-Crafted-Event je Item; lange Quest, gut für Langzeit.

### Sammlung: Vier Jahreszeiten Bestiarium  
*Typ: quest*

- **Nutzen:** Ziel: Alle Naturalist-Tiere mindestens einmal in Town-Nähe gesehen/gezähmt dokumentieren (12 Arten). Belohnung: Naturforscher-Buch, Fernglas (Supplementaries Spyglass?), 'Biologe'-Titel. Tier-Sammlung.
- **Integration:** Naturalist + Critters & Companions + Ribbits; Sammel-Kapitel.
- **Quest:** Stardew-'Critterpedia' (Animal-Crossing-Anleihe).
- **Progression:** Sammel-Tree-Zweig Fauna.
- **Probleme:** 'Gesehen'-Detection schwer; einfacher: 1 Drop/Item je Tier sammeln statt Sichtung.

### Sammlung: Artefakte des Tals  
*Typ: quest*

- **Nutzen:** Ziel: 6 verschiedene Artifacts-Mod-Items finden und ausstellen. Belohnung: Schatzkarte-Item, Ausgräber-Set, Museums-Reputation +6. Artefakt-Sammlung.
- **Integration:** Artifacts + Dungeons & Taverns Loot; Museums-Kapitel.
- **Quest:** Stardew-Artefakt-Sammlung mit echtem Mod-Nutzen.
- **Progression:** Hochstufiger Museums-Zweig.
- **Probleme:** Artifacts sind RNG-Loot aus Truhen — sehr varianzreich; Drop-Pity oder Händler-Backup via KubeJS empfehlen.

### Ratatouille — Gourmet-Auftrag  
*Typ: quest*

- **Nutzen:** Ziel: Mit Create Ratatouille/Deepfried 3 Gourmet-Gerichte zubereiten und an die Taverne liefern. Belohnung: Gourmet-Rezeptbuch, Reputation +3, 40 XP. Spezial-Koch-Quest.
- **Integration:** Create Ratatouille + Deepfried + Cafe; Küchen-/Stadt-Kapitel.
- **Quest:** Stardew-Queen-of-Sauce-Spezialrezepte.
- **Progression:** Verbindet Create-Food mit Wirtschaft.
- **Probleme:** Ratatouille/Deepfried 1.21.1-Stand (Verfügbarkeit prüfen); Item-IDs verifizieren.

### Der Bauernmarkt  
*Typ: quest*

- **Nutzen:** Ziel (Weekly): Einen Marktstand (Supplementaries Sign-Post + Handcrafted Stall) aufbauen und 32 Crops gegen Smaragde verkaufen. Belohnung: 16 Smaragde, Markt-Banner, Town-Reputation +2. Wirtschafts-Weekly.
- **Integration:** Deko + Vanilla-Handel; Wirtschafts-/Weekly-Kapitel.
- **Quest:** Stardew-Wochenmarkt-Vibe.
- **Progression:** Wiederkehrende Wirtschaftsaktivität.
- **Probleme:** Verkauf-Detection über 'Smaragde erreicht' statt echtem Markt; Stand bleibt Deko.

### Nachtwache — Verteidige das Dorf  
*Typ: quest*

- **Nutzen:** Ziel: 3 Guard-Villagers ausrüsten und eine Nacht ohne Bürgerverlust überstehen. Belohnung: Wachturm-Bauplan, Eisenrüstungs-Set, Town-Reputation +3. Defensive Community-Quest.
- **Integration:** Guard Villagers + MineColonies-Wachen; Stadt-Kapitel.
- **Quest:** Cozy-Pack braucht etwas Spannung — milder Verteidigungs-Touch.
- **Progression:** Schaltet Stadtmauer-/Verteidigungs-Zweig frei.
- **Probleme:** 'Keine Bürgerverluste' schwer zu tracken; ggf. simpler: 5 Monster nahe Dorf besiegen.

### Stalltag: Tierpflege  
*Typ: quest*

- **Nutzen:** Ziel (Daily): Alle gehaltenen Tiere füttern (Smarter Farmers / What Are They Up To überwacht) und 1 Tierprodukt sammeln. Belohnung: 4 Smaragde + Heu, täglich. Tier-Daily.
- **Integration:** Smarter Farmers + Vanilla-Tiere; Daily-Kapitel.
- **Quest:** Stardew-tägliche-Tierstreichel-Routine.
- **Progression:** Hält Tierhaltung relevant.
- **Probleme:** 'Füttern'-Detection via Item-Use schwierig; einfacher über 'X Tierprodukt heute eingesammelt'.

### Erntefest-Wettbewerb  
*Typ: quest*

- **Nutzen:** Ziel (Seasonal Weekly im Herbst): Die größte Crop (z.B. Riesenkürbis / höchste Qualität) zum Festtisch bringen. Belohnung: Goldene Gießkanne (Deko), Festival-Pokal, Reputation +5. Wettbewerbs-Event.
- **Integration:** Bountiful Fares + Saison-Lock; Saison-/Event-Kapitel.
- **Quest:** Stardew-Fair-Grange-Display-Wettbewerb.
- **Progression:** Prestige-Event, jährlich wiederholbar.
- **Probleme:** Qualitätsstufen gibt es in Vanilla-Crops nicht — bräuchte Quality-Crops-Mechanik (KubeJS) oder Quest auf Menge umstellen.

### Briefträger des Tals  
*Typ: quest*

- **Nutzen:** Ziel: 3 'Briefe' (benannte Papier-Items) an 3 verschiedene Villager im Dorf liefern. Belohnung: Postsack, 6 Smaragde, Beziehungs-XP zu allen drei. Verbindungs-Quest.
- **Integration:** KubeJS-Custom-Brief-Items + Town Talk; Beziehungs-/Stadt-Kapitel.
- **Quest:** Animal-Crossing-Botengang-Charme.
- **Progression:** Einführungs-Quest ins Beziehungssystem.
- **Probleme:** Brief-an-Villager-Übergabe ist Custom-KubeJS (rechtsklick-mit-Item); ohne das nicht detectbar.

### Die Glocke läutet — Stadtgründung offiziell  
*Typ: quest*

- **Nutzen:** Ziel: Eine Glocke (Bells & Whistles) im Zentrum platzieren, läuten und 5 Villager im Umkreis haben. Belohnung: Stadtwappen-Banner, offizieller Stadtname-Schild, Reputation +5. Meilenstein-Zeremonie.
- **Integration:** Bells & Whistles + Easy Villagers; Stadt-Kapitel-Meilenstein.
- **Quest:** Feierlicher Stadtgründungs-Moment, sehr cozy.
- **Progression:** Markiert Übergang Dorf→Stadt im Tree.
- **Probleme:** Bells & Whistles Glocken-Interaktion detecten; Villager-Umkreis-Zählung via KubeJS Radius-Scan.

### Kompost & Kreislauf  
*Typ: quest*

- **Nutzen:** Ziel: 1 Kompostfass (Farmer's Delight Organic Compost) betreiben und 16 Bio-Dünger herstellen, damit ein Feld beschleunigen. Belohnung: Reichhaltige-Erde-Stack, Kompost-Beschleuniger, 25 XP. Nachhaltigkeits-Quest.
- **Integration:** Farmer's Delight Compost + Rich Soil; Farming-Kapitel.
- **Quest:** Stardew-Bodenqualität/Dünger-Mechanik.
- **Progression:** Schaltet 'Premium-Felder' für höhere Erträge frei.
- **Probleme:** Organic-Compost-Rezept-Pfad prüfen; Rich-Soil-Wachstumsboost-Config verifizieren.

### Postamt & Lieferdienst (Create)  
*Typ: quest*

- **Nutzen:** Ziel: Mit Steam'n'Rails eine kurze Schienenstrecke vom Hof zum Dorflager bauen und 1 Lieferung per Zug transportieren. Belohnung: Steam'n'Rails Loren-Set, Bahnhofsschild, 'Logistiker'-Titel. Transport-Quest.
- **Integration:** Create Steam'n'Rails; Create-/Stadt-Kapitel.
- **Quest:** Verbindet Hof und Dorf logistisch, Create-Highlight.
- **Progression:** Schaltet Schienen-Netzwerk-Ausbau frei.
- **Probleme:** Zug-Ankunft-Detection schwer; Quest prüft besser 'Lieferung im Ziel-Lager angekommen' via Item-Count.

### Saatgut-Sammler  
*Typ: quest*

- **Nutzen:** Ziel: 15 verschiedene Saatgut-Typen (Vanilla + Pam's + Delight-Crops) ins Saatgut-Archiv (Truhe) einlagern. Belohnung: Saatgut-Beutel (Sophisticated Backpack-Slot), seltene Crop-Samen, 'Botaniker'-Titel. Saatgut-Sammlung.
- **Integration:** Pam's + Farmer's Delight Crops + Sophisticated Storage; Sammel-Kapitel.
- **Quest:** Animal-Crossing-Katalog-Sammelgefühl.
- **Progression:** Schaltet seltene/saisonale Crops frei.
- **Probleme:** Saatgut-Item-Tags über mehrere Mods bündeln; KubeJS-Tag-Liste pflegen.

### Der lange Winterabend — Geselligkeit  
*Typ: quest*

- **Nutzen:** Ziel (Winter-Seasonal): Taverne mit 4 Villagern und warmem Essen (Comforts + Farmer's Delight Eintopf) füllen, 1 Abend feiern. Belohnung: Kaminfeuer-Set, Geschichtenbuch, Town-Reputation +4. Cozy-Winter-Event.
- **Integration:** Comforts + Farmer's Delight + Deko + Saison-Lock; Saison-/Stadt-Kapitel.
- **Quest:** Animal-Crossing-Winterfest / Stardew-Feast-of-Winter-Star.
- **Progression:** Saisonales Wiederholungs-Event, stärkt Beziehungen.
- **Probleme:** Mehrere Detect-Bedingungen (Villager-Radius + Block + Saison) — KubeJS-Kombi-Check nötig, mittlerer Aufwand.


## researcher (25)

### Gated Chapter-Progression a la Prominence II / Enigmatica 9 (FTB Quests Hauptlinie mit harten Toren)  
*Typ: system*

- **Nutzen:** Strukturiert das Endlos-Sandbox-Gefuehl in klare Akte (z.B. Ankunft -> Hof aufbauen -> Stadt gruenden -> Create-Industrie -> Festtage/Endgame). Gibt Spielern jederzeit ein 'naechstes Ziel' und verhindert das typische Kitchen-Sink-Verlaufen.
- **Integration:** Reine FTB-Quests-Struktur ueber bereits vorhandene Mods; Tore via 'Quest abschliessen schaltet Kapitel frei'. Cozy-Tonalitaet: Tore sind Meilensteine (erstes Feld, erster MineColonies-Buerger, erster Create-Antrieb), keine Kampfgates.
- **Quest:** Sehr hoch: das ist das Quest-Rueckgrat selbst; jedes Kapitel buendelt 8-15 Quests mit eigenem Belohnungstable.
- **Progression:** Sehr hoch: definiert die gesamte Langzeitkurve und macht Create/MineColonies/Farming als aufeinander aufbauende Phasen lesbar.
- **Probleme:** Designaufwand hoch; Tore duerfen im SMP nicht den langsamsten Spieler blockieren -> Team-Sync ueber FTB Teams pruefen. Balancing der Kapitellaenge braucht Playtesting.

### Reward-Table-Tiers mit Loot-Crates (ATM10/Enigmatica-Muster)  
*Typ: system*

- **Nutzen:** Ersetzt fade Fixbelohnungen durch gewichtete Loot-Crate-Tiers (Common/Rare/Epic). Erzeugt 'noch eine Quest'-Sog und Sammelreiz, ohne neue Mods.
- **Integration:** FTB Quests Reward Tables (bestaetigt verfuegbar) + KubeJS-Loot-Tables fuer Pack-eigene Items. Crates als physische Kisten-Items, oeffnen via rechtsklick.
- **Quest:** Sehr hoch: jede Quest kann statt Fixitem ein Crate-Roll geben; eigene Crates pro Kapitel.
- **Progression:** Hoch: Tier-Crates skalieren mit Kapiteln, spaete Crates enthalten Create-Materialien/Dekokits.
- **Probleme:** Gewichtung muss getuned werden, sonst Frust durch 'Nieten'. KubeJS-Loot-Tables muessen server+client konsistent sein.

### Taegliche & woechentliche Bounty-Boards (Vault Hunters / Dawncraft Bounty-Muster, cozy-Variante)  
*Typ: system*

- **Nutzen:** Wiederkehrende Mini-Auftraege ('liefere 32 Karotten', 'fang 3 Fische', 'baue X') geben taegliche Login-Motivation und nutzen das bestehende Farming/Cooking/Fishing-Sortiment aus.
- **Integration:** FTB Quests + KubeJS-Timer (Reset-Logik) oder Numismatic-Bounties-Mechanik; Belohnung in Vanilla-Smaragden (passt zur No-Coin-Wirtschaft). Board als Supplementaries-Notice-Board oder Bells&Whistles-Plakat.
- **Quest:** Sehr hoch: prozedural/rotierende Quests sind eigene Questkategorie.
- **Progression:** Mittel: liefert Smaragd-Einkommen fuer Villager-Trades statt direkter Power-Progression.
- **Probleme:** Reset-Timer im SMP serverseitig synchron halten; KubeJS-Cron sauber implementieren. Numismatic Bounties Verfuegbarkeit pruefen — alternativ pure KubeJS-Loesung.

### Codex/Sammel-Almanach fuer Crops, Fische, Tiere (Stardew-Sammlung trifft Pokedex)  
*Typ: system*

- **Nutzen:** Zentraler Sammelfortschritt: jedes erstmals geerntete Crop / gefangener Fisch / gezaehmtes Tier wird im Almanach 'freigeschaltet'. Trifft exakt die Stardew/Animal-Crossing-Sammelmotivation.
- **Integration:** Umsetzbar als FTB-Quests-Sammelkapitel (Submit-Quests pro Spezies) mit Naturalist/Aquaculture/Critters/HarvestCraft als Inhalt. Optional 'Just Enough Professions'/Patchouli als Anzeige.
- **Quest:** Sehr hoch: hunderte Detect-Quests moeglich, je Biom/Saison gruppiert.
- **Progression:** Hoch: 100%-Sammlung als Langzeitziel mit prestige-Belohnung (Deko/Titel).
- **Probleme:** Sehr questintensiv zu pflegen; viele Items aus vielen Mods -> Wartung bei Mod-Updates. Serene-Seasons-Gating macht manche Crops zeitabhaengig (Feature, kann aber frustrieren).

### Saisonale Festival-Events (Animal Crossing / Cottage Witch Feiertags-Muster)  
*Typ: feature*

- **Nutzen:** An Serene-Seasons gebundene Events (Erntedank im Herbst, Bluetenfest im Fruehling, Winterbasar) mit Sonderquests, Sonderhaendlern und exklusiver Deko. Schafft jaehrlichen Rhythmus und Wiederkehrgrund.
- **Integration:** KubeJS-Saisonhooks + FTB-Quests-Eventkapitel; Sonderhaendler via Easy/Guard Villagers oder MineColonies-Visitor. Deko aus Macaw's/Chipped/Handcrafted als Festpreise.
- **Quest:** Sehr hoch: pro Saison ein zeitlich begrenztes Questbuendel.
- **Progression:** Mittel: kosmetik- und sammlungsgetrieben statt Power, perfekt fuer Cozy-Langzeitbindung.
- **Probleme:** 'Zeitlich begrenzt' im SMP technisch tricky (Spieler verpassen Events) -> evtl. jaehrlich wiederkehrend statt einmalig. Serene-Seasons-Tageslaenge muss zur Spielfrequenz passen.

### NPC-Beziehungs-/Freundschaftssystem light (Stardew Hearts via Town Talk + MineColonies)  
*Typ: system*

- **Nutzen:** Dorfbewohner/Kolonisten 'moegen' Geschenke; Beziehungsstufen schalten Dialoge, Trades und kleine Quests frei. Kern der Stardew/Sunlit-Valley-Bindung.
- **Integration:** Town Talk (vorhanden) fuer Dialog + KubeJS-Tracking von Geschenkitems pro Villager; MineColonies-Buerger als Beziehungs-Anker. Belohnungen ueber Trade Cycling freischalten.
- **Quest:** Hoch: 'Bring NPC X sein Lieblingsgericht'-Questketten je Bewohner.
- **Progression:** Mittel-hoch: schaltet bessere Trades/Rezepte ueber Zeit frei (soziale Progression).
- **Probleme:** Voll-KubeJS-Eigenbau, hoher Skriptaufwand und SMP-Persistenz pro Spieler vs. geteiltem Dorf. Klares Scope noetig, sonst Feature-Creep. (Verfuegbarkeit der noetigen Hooks pruefen.)

### Skill-/Beruf-Levelsystem (Stardew Skills, RPG-lite a la Dawncraft)  
*Typ: custom-mod*

- **Nutzen:** Farming/Mining/Fishing/Cooking-Level mit kleinen Perks (mehr Ertrag, schnelleres Angeln). Gibt RPG-lite-Tiefe und belohnt Routinetaetigkeit kontinuierlich.
- **Integration:** Existierende Mods wie PuffishSkills/PMMO (Verfuegbarkeit 1.21.1 NeoForge pruefen) ODER schlanke KubeJS-XP-Loesung. Passt zur 'Kartoffelboss'-Eigenmod-Roadmap als spaeteres Modul.
- **Quest:** Mittel: 'erreiche Farming Lvl 5'-Meilensteinquests.
- **Progression:** Sehr hoch: parallele Dauer-Progressionsachse neben Quests, klassische Langzeitmotivation.
- **Probleme:** Fertige Skill-Mods auf 1.21.1 NeoForge oft unreif -> Verfuegbarkeit pruefen. Balancing mit Create-Automation (Auto-Farmen darf Skill-XP nicht trivialisieren). Eigenmod = grosser Aufwand.

### Hof-/Stadt-Ranglisten-Tiers (Life in the Village / Farming Crossing Aufstiegs-Muster)  
*Typ: system*

- **Nutzen:** Der eigene Hof bzw. die MineColonies-Stadt durchlaeuft sichtbare Raenge (Weiler -> Dorf -> Marktflecken -> Stadt), jeder Rang schaltet Bauoptionen/Haendler frei. Greifbares Town-Building-Ziel.
- **Integration:** FTB Quests als Rang-Gate, gekoppelt an MineColonies-Buergerzahl/Gebaeudelevel via KubeJS-Abfrage. Belohnung: neue Structurize/Domum-Schemata, Deko-Sets.
- **Quest:** Hoch: jeder Rang = Questbuendel mit Bau- und Bevoelkerungszielen.
- **Progression:** Sehr hoch: macht Town-Building zur messbaren Hauptprogression.
- **Probleme:** MineColonies-Statusabfrage via KubeJS muss zuverlaessig sein; im SMP wer 'besitzt' die Stadt? Team-Ownership klaeren.

### Tech-Tree-Gating fuer Create (Enigmatica 9 / ATM10 Tech-Progression)  
*Typ: system*

- **Nutzen:** Create-Maschinen werden in sinnvoller Reihenfolge per Quest freigeschaltet statt alles sofort, sodass Neulinge die Mechanik schrittweise lernen (Handkurbel -> Wasserrad -> Dampf -> TFMG).
- **Integration:** FTB Quests + KubeJS-Rezeptgating (Rezepte erst nach Quest aktiv) ueber die bereits vorhandenen Create-Addons. Lehr-Quests mit Patchouli/eingebetteten GIFs.
- **Quest:** Sehr hoch: ganzer Create-Lernpfad als Questkapitel.
- **Progression:** Sehr hoch: strukturiert den staerksten Pack-Fokus (Create 6) in eine Lernkurve.
- **Probleme:** Rezept-Hiding via KubeJS kann mit JEI/Every-Compat-Rezepten kollidieren; sauberes Tagging noetig. Zu strikte Gates frustrieren Create-Veteranen -> evtl. Skip-Option.

### Onboarding-Tutorial-Insel / Startquest-Kette (Better MC / Prominence II Intro)  
*Typ: feature*

- **Nutzen:** Gefuehrter Einstieg (erste 30-60 Min): Werkzeug bauen, erstes Feld anlegen, ersten Villager-Trade, JourneyMap erklaeren. Senkt die Einstiegshuerde des grossen Packs massiv.
- **Integration:** FTB Quests Intro-Kapitel + optional fester Spawn via Datapack/Structure (Dungeons & Taverns oder eigene Struktur). Verweist auf vorhandene QoL-Mods (Jade, JEI).
- **Quest:** Hoch: ~10 lineare Hand-haltende Quests.
- **Progression:** Mittel: reine Startphase, aber entscheidend fuer Retention.
- **Probleme:** Im SMP teilen sich Spieler den Spawn -> Tutorial darf Welt nicht zumuellen. Muss bei jedem Mod-Update auf Korrektheit geprueft werden.

### Prestige-/New-Game-Plus-Sammelziele (ATM-Star / Vault-Hunters Endgame-Muster, cozy)  
*Typ: system*

- **Nutzen:** Ein finales, kosmetisches 'Lebenswerk'-Craft (z.B. 'Goldene Giesskanne' / Stadtwahrzeichen), das hunderte Materialien aus allen Pack-Bereichen verlangt. Klassischer Kitchen-Sink-Endgame-Anker.
- **Integration:** KubeJS-Mehrstufenrezept + FTB-Quests-Finalkapitel; Komponenten ziehen aus Farming, Create, MineColonies, Cooking. Belohnung: einzigartiges Bauwerk/Deko + Server-Anerkennung.
- **Quest:** Hoch: Sammel-Megaquest mit vielen Unterzielen.
- **Progression:** Sehr hoch: definiertes Endgame, das sonst im Cozy-Pack fehlt.
- **Probleme:** Muss erreichbar bleiben (kein 200h-Grind-Frust). Im SMP: gemeinsames oder pro-Team-Ziel? Klar kommunizieren.

### Kochbuch-/Rezept-Entdeckungssystem (Stardew Cooking-Sammlung)  
*Typ: system*

- **Nutzen:** Gerichte aus Farmer's-Delight/Let's-Do/HarvestCraft muessen erst 'entdeckt' (gekocht) werden, um im Codex/JEI als gemeistert zu gelten. Verbindet die riesige Food-Auswahl mit Sammelreiz.
- **Integration:** FTB-Quests-Detect-Quests pro Gericht + Bountiful-Fares/Delight-Inhalte; Anzeige via JEI-Bookmarks. Meisterkoch-Titel als Belohnung.
- **Quest:** Sehr hoch: dutzende Gericht-Detect-Quests, nach Kueche gruppiert.
- **Progression:** Mittel-hoch: 100%-Kueche als Sammelziel; Foodbuffs als Mehrwert (AppleSkin vorhanden).
- **Probleme:** Sehr viele Food-Items -> Pflegeaufwand. Ueberschneidung der vielen Delight-Addons (doppelte Gerichte) muss bereinigt werden.

### Erkundungs-/Landmark-Logbuch (Better MC Exploration-Sammlung)  
*Typ: system*

- **Nutzen:** Belohnt das Finden von Terralith/Tectonic-Biomen und Dungeons-&-Taverns/Structures-Arise-Strukturen mit Logbuch-Eintraegen und Smaragden. Gibt der grossen Worldgen einen Zweck.
- **Integration:** FTB Quests Detect (Biom betreten / Struktur gefunden) via KubeJS-Location-Events; JourneyMap-Waypoints als Hilfe. Belohnung: Reisedeko, Smaragde.
- **Quest:** Hoch: ein Eintrag je Biom/Struktur.
- **Progression:** Mittel: motiviert Exploration als Nebenprogression.
- **Probleme:** KubeJS-Biom/Struktur-Detection auf 1.21.1 zuverlaessig hinbekommen; viele Biome = viel Pflege. SMP: geteilter oder individueller Fortschritt?

### Wirtschafts-Sink ueber Stadt-Steuern/Upkeep (Wirtschafts-Loop a la Eco-Packs)  
*Typ: feature*

- **Nutzen:** Smaragde haben einen sinnvollen Abfluss: Haendler-Lizenzen, Dekofreischaltungen, MineColonies-Unterhalt. Verhindert Smaragd-Inflation und haelt die Bounty-/Trade-Loops relevant.
- **Integration:** KubeJS-Smaragd-Kosten an Freischaltungen koppeln (passt zur Vanilla-Smaragd-Wirtschaft, kein Coin-Mod). Trade Cycling steuert Haendlerangebot.
- **Quest:** Mittel: 'spare X Smaragde'-Meilensteine.
- **Progression:** Mittel-hoch: stabilisiert die gesamte Belohnungsoekonomie langfristig.
- **Probleme:** Cozy-Pack: harte 'Steuern' koennen unentspannt wirken -> lieber optionale Upgrades als Zwangskosten. Balancing der Smaragdquellen vs. -senken.

### Team-/Coop-Quests fuer den SMP (FTB-Teams-basiert, Enigmatica-Coop-Muster)  
*Typ: system*

- **Nutzen:** Eigene Questkategorie, die nur gemeinsam loesbar ist (Gemeinschaftsscheune fuellen, Stadtfest ausrichten) -> foerdert das 'SMP'-Miteinander statt Solo-Grind.
- **Integration:** FTB Quests + FTB Teams (beide vorhanden); geteilte Submit-Quests, an denen mehrere beitragen. Belohnung: serverweite Buffs/Deko.
- **Quest:** Sehr hoch: dedizierte Coop-Kategorie.
- **Progression:** Hoch: gemeinschaftliche Bauziele als sozialer Langzeitanker.
- **Probleme:** Trittbrettfahrer-Problem (einer macht alles); Beitragstracking via FTB Teams pruefen. Balancing fuer kleine Spielerzahl (~5).

### Tier-Companion-/Haustier-Sammlung mit Bindung (Critters & Companions / Dogfolk Ausbau)  
*Typ: feature*

- **Nutzen:** Zaehmbare Tiere als sammelbare, benennbare Begleiter mit kleinen Boni -> trifft die Animal-Crossing/Stardew-Tierbindung und nutzt die vielen vorhandenen Tier-Mods.
- **Integration:** FTB-Quests-Sammelkapitel ueber Critters&Companions/Naturalist/Dogfolk/Ribbits; KubeJS fuer optionale Mini-Boni. Comforts/Deko fuer Tierunterkuenfte.
- **Quest:** Hoch: 'zaehme/finde Tier X'-Quests je Spezies.
- **Progression:** Mittel: Sammel- und Kosmetikachse.
- **Probleme:** Begleiter-Boni duerfen nicht zu stark werden (Cozy-Balance). Viele Tier-Mods -> moegliche Spawn/Tag-Konflikte pruefen.

### Wochen-Marktplatz mit rotierendem Wanderhaendler (Stardew Travelling Cart)  
*Typ: feature*

- **Nutzen:** Ein rotierender Sonderhaendler bietet woechentlich wechselnde, seltene Deko/Samen/Rezepte gegen Smaragde -> Wiederkehrgrund und sinnvoller Smaragd-Sink.
- **Integration:** KubeJS-Timer + Trade Cycling fuer rotierendes Angebot; Haendler als Guard/Easy-Villager an festem Marktstand (Bells & Whistles Deko).
- **Quest:** Mittel: 'besuche den Markt'/'kaufe Rares'-Quests.
- **Progression:** Mittel: Zugang zu sonst nicht craftbaren Kosmetik-/Saatgut-Items ueber Zeit.
- **Probleme:** Rotations-Timer serverseitig stabil halten; Angebotsbalance (zu billig -> entwertet Crafting).

### Meilenstein-Titel & Cosmetic-Unlocks (Sozial-Belohnung a la Live-Service-Packs)  
*Typ: system*

- **Nutzen:** Quest-Meilensteine vergeben sichtbare Titel/Praefixe und Cosmetics (3D-Skin-Layers, Deko-Sets) statt Power -> Statussammlung als Cozy-konforme Langzeitmotivation.
- **Integration:** KubeJS fuer Titel/Scoreboard-Tags; Belohnungen aus 3D Skin Layers, Chipped/Macaw's Deko. FTB Quests vergibt sie als Reward.
- **Quest:** Hoch: jeder grosse Meilenstein gibt einen Titel.
- **Progression:** Mittel: prestige-/identitaetsgetrieben, kein Power-Creep (ideal cozy).
- **Probleme:** Titel-Anzeige im Chat/Tab via KubeJS oder Zusatzmod (Verfuegbarkeit pruefen). Rein kosmetisch -> manche Spieler wollen mechanischen Nutzen.

### Saatgut-/Crop-Mutation-Forschung (Sammel-Tiefe a la Mystical-Agriculture-light)  
*Typ: feature*

- **Nutzen:** Crops lassen sich durch Kreuzung/Forschung zu selteneren Varianten weiterentwickeln -> langfristiges Farming-Sammelziel jenseits 'pflanz und ernte'.
- **Integration:** KubeJS-Crossbreeding-Logik auf HarvestCraft/Vanilla-Crops ODER schlanke Forschungsquests. Serene Seasons als zusaetzliche Bedingung.
- **Quest:** Hoch: 'erforsche/entdecke Crop-Variante X'.
- **Progression:** Hoch: tiefe, dauerhafte Farming-Progressionsachse — Kernfokus des Packs.
- **Probleme:** Voll-KubeJS-Eigenbau, aufwendig; Gefahr der Ueberschneidung mit HarvestCraft-Mechanik. Klar abgrenzen, sonst Verwirrung.

### Hint-/Anti-Stuck-System in Quests (Prominence II Lesbarkeits-Muster)  
*Typ: feature*

- **Nutzen:** Jede Quest hat klaren Beschreibungstext, JEI-Verweis und optionalen 'Hinweis' -> verhindert das groesste Kitchen-Sink-Problem: Spieler wissen nicht, wie es weitergeht.
- **Integration:** Reine FTB-Quests-Textpflege + Patchouli-Guidebook-Verlinkung; nutzt vorhandene JEI/Jade-Tooltips.
- **Quest:** Hoch: betrifft jede einzelne Quest (Qualitaetsstandard).
- **Progression:** Niedrig direkt, aber stuetzt jede andere Progression durch Klarheit.
- **Probleme:** Hoher Schreib-/Pflegeaufwand und Lokalisierung (DE). Muss bei Rezeptaenderungen aktuell gehalten werden.

### Tagebuch/Story-Framing der Quests (Cottage Witch / Dawncraft Narrativ-Muster)  
*Typ: feature*

- **Nutzen:** Ein leichter narrativer Rahmen (Brief vom Grossvater, der den verfallenen Hof vererbt) gibt den Quests cozy Sinn und emotionale Bindung statt blosser Checklisten.
- **Integration:** FTB-Quests-Beschreibungstexte + Supplementaries-Briefe/Buecher als Item-Props; optional Town-Talk-Dialoge der NPCs.
- **Quest:** Hoch: Story-Beschreibungen fuer jedes Kapitel.
- **Progression:** Mittel: emotionaler Anker, stuetzt Langzeitbindung.
- **Probleme:** Erzaehlung im offenen SMP schwer konsistent (mehrere 'Erben'?). Schreibaufwand; Tonalitaet muss konsequent cozy bleiben.

### Scheunen-/Sammelschrein-Mechanik (Stardew Community Center / Animal Crossing Museum)  
*Typ: feature*

- **Nutzen:** Ein zentrales Bauwerk mit 'Buendeln' (z.B. Fruehlings-Crops, Flussfische, Bergbau-Schaetze), die abzugeben sind und Bereiche/Belohnungen freischalten -> ikonischste uebertragbare Stardew-Mechanik.
- **Integration:** FTB-Quests-Submit-Buendel + physisches Bauwerk (Structurize/Handcrafted); jede vervollstaendigte Vitrine schaltet via KubeJS ein Upgrade/Deko frei.
- **Quest:** Sehr hoch: das Buendel-System ist eine ganze Questkategorie.
- **Progression:** Sehr hoch: gemeinschaftliches, langlaufendes Sammelprojekt — perfekter SMP-Anker.
- **Probleme:** Im SMP geteiltes Bauwerk -> wer gibt ab, wer bekommt Reward? FTB-Teams-Beitrag klaeren. Hoher Designaufwand.

### Catch-up-/Bonus-Mechanik fuer Nachzuegler (SMP-Retention-Muster)  
*Typ: system*

- **Nutzen:** Spaeter beitretende oder zurueckliegende Spieler erhalten skalierende Startboni/Quest-Sprungbretter, damit sie im laufenden SMP nicht abgehaengt werden — wichtig fuer ~5er-Langzeit-Community.
- **Integration:** KubeJS prueft Serveralter/Team-Fortschritt und vergibt einmalige Bonus-Crates; an FTB-Quests-Kapitel gekoppelt.
- **Quest:** Mittel: 'Aufhol'-Bonusquests.
- **Progression:** Mittel-hoch: haelt die Spielergruppe ueber Monate beieinander.
- **Probleme:** Balance: darf fleissige Spieler nicht entwerten. KubeJS-Persistenz/Serveralter-Abfrage muss zuverlaessig sein.

### Achievement-/Milestone-Wand mit Statistik-Tracking (Better MC / ATM Stats-Muster)  
*Typ: feature*

- **Nutzen:** Sichtbares Brett mit langfristigen Statistik-Zielen (1000 Crops geerntet, 100 Fische, 50 Gerichte) -> Dauer-Sammelmotivation, die im Hintergrund mitlaeuft.
- **Integration:** FTB Quests Detect auf Vanilla-Statistiken via KubeJS-Stat-Hooks; Belohnung Titel/Deko. Anzeige als physisches Board (Bells & Whistles).
- **Quest:** Hoch: viele statistikbasierte Langzeitquests.
- **Progression:** Mittel-hoch: passive Dauerprogression ohne aktiven Aufwand des Spielers.
- **Probleme:** Zugriff auf Vanilla-Stats via KubeJS/FTB-Quests auf 1.21.1 verifizieren. Zu hohe Schwellen -> nie erreicht, Frust.

### Optionale Challenge-Quests mit hohem Risiko/Reward (Vault Hunters Side-Content)  
*Typ: system*

- **Nutzen:** Abseits der cozy Hauptlinie ein optionaler Strang anspruchsvoller Quests (grosse Create-Kontraptionen, seltene Strukturen) fuer Vielspieler — verlaengert die Lebensdauer fuer Hardcore-Spieler ohne die Hauptlinie zu haerten.
- **Integration:** Eigenes FTB-Quests-Kapitel, klar als optional markiert; nutzt Create-Addons, Big Cannons, schwere Strukturen. Premium-Loot-Crates als Reward.
- **Quest:** Hoch: dedizierte Optional-Kategorie.
- **Progression:** Hoch: gibt erfahrenen Spielern ein Endgame jenseits des Cozy-Cores.
- **Probleme:** Darf Cozy-Identitaet nicht ueberlagern -> klar separieren. Balancing der Belohnungen, damit Optional-Strang nicht Pflicht wird.


## retention (21)

### Tagesbrett am Rathaus (FTB Quests Daily-Chapter mit 24h-Cooldown)  
*Typ: system*

- **Nutzen:** Erzeugt den Kern-Loop 'kurz einloggen': 3-4 rotierende Mini-Aufgaben (z.B. '10 Karotten liefern', '5 Fische fangen', '1 Gericht aus Farmer's Delight kochen'), die taeglich neu freischalten. Schneller Dopamin-Hit in unter 10 Minuten Spielzeit.
- **Integration:** FTB Quests ist bereits enthalten; nutzt das verifizierte 'Quest Repeat Cooldown'-Feld (team-basiert, NeoForge 1.21.1). Eigenes Kapitel 'Tagesbrett', Tasks via Item-Lieferung an bereits vorhandene Farm-/Cook-Mods gekoppelt. Belohnung: Vanilla-Smaragde (passt zur Emerald-Wirtschaft, kein Coin-Mod).
- **Quest:** Sehr hoch — ist selbst ein Quest-System; Tasks koennen jede vorhandene Crop-/Food-/Fishing-Mod als Liefer-Item nutzen.
- **Progression:** Smaragd-Einkommen finanziert Villager-Trades und MineColonies-Ausbau; Grundlage fuer Streak-System.
- **Probleme:** Team-Cooldown statt per-Spieler kann auf SMP zu 'einer macht alles'-Effekt fuehren; ggf. FTB Teams auf Solo-Teams konfigurieren. Rotation muss manuell via mehreren Quest-Varianten + Sichtbarkeitsregeln gebaut werden (FTB hat keine native Zufallsrotation).

### Login-Streak-System (KubeJS Tagescounter + Meilenstein-Belohnungen)  
*Typ: system*

- **Nutzen:** Belohnt taegliches Einloggen mit steigender Streak (Tag 1, 3, 7, 14, 30) — der direkteste 'komm jeden Tag zurueck'-Anreiz. Bricht der Streak, startet er neu, was Verlustaversion ausnutzt.
- **Integration:** KubeJS (enthalten) speichert pro-Spieler einen persistenten Tageszaehler ueber PlayerData/world-save; vergleicht letzten Login-Tag. Belohnungen via FTB Quests Reward-Trigger oder direktes Item-give. Anzeige ueber Town Talk / Chat-Nachricht beim Join.
- **Quest:** Mittel — Streak-Meilensteine koennen versteckte FTB-Quests freischalten (z.B. 'Tag 7: Saison-Saatgut-Paket').
- **Progression:** Hoch — gestaffelte Belohnungen (Saatgut, seltene Deko, Smaragde) skalieren mit Bindungsdauer.
- **Probleme:** Reiner KubeJS-Eigenbau, kein fertiger Mod — Testaufwand fuer Tageswechsel-Logik (UTC vs. lokal, Serverzeit). Streak-Reset kann frustrieren; Karenztag empfehlenswert.

### Stadt-Sammelmuseum (Easy Villagers + Custom-Mod 'Kartoffelboss' Donation-Blocks)  
*Typ: system*

- **Nutzen:** Ein Gebaeude im Dorf mit Vitrinen, in die Spieler jedes Crop/Fisch/Tier-Drop einmalig 'spenden'. Klassischer Stardew-Museum-Loop: 'mir fehlt nur noch Kohlrabi'. Treibt Erkundung und Farming gezielt an.
- **Integration:** Donation-Slots als KubeJS/Kartoffelboss-Block (geplante Eigen-Mod ideal hierfuer); Inventar persistent pro Welt. Fuellt sich mit Items aus Pam's HarvestCraft 2, Aquaculture, Farmer's Delight Crops, Naturalist-Drops. Fortschritt zaehlt fuer FTB-Quest-Trigger.
- **Quest:** Sehr hoch — jede Vitrinen-Reihe komplett = Quest-Abschluss + Belohnung (Trophaee, Deko, Titel).
- **Progression:** Sehr hoch — hunderte Items = monatelange Langzeitsammlung; Teil-Komplettierung schaltet Stadtbelohnungen frei.
- **Probleme:** Erfordert eigenen Block (Kartoffelboss-Mod noch nicht gebaut) oder aufwendiges KubeJS-GUI; Vanilla-Item-Frames als Fallback weniger komfortabel. Balancing welcher Items zaehlen.

### Bountiful Bounty-Board als Stadt-Auftragstafel  
*Typ: mod*

- **Nutzen:** Fertige Auftragstafel in Doerfern: liefert Items oder toetet Mobs gegen Belohnung, mit eingebautem Reputations-System (bessere/seltenere Auftraege bei hoeherem Ruf). Ergaenzt das selbstgebaute Tagesbrett mit Mob-/Sammel-Bounties ohne KubeJS-Aufwand.
- **Integration:** Bountiful 8.0.0-beta fuer 1.21.1 NeoForge (Verfuegbarkeit pruefen — Beta-Status). Boards spawnen in Doerfern, passt zu MineColonies-/Vanilla-Doerfern. Belohnungs-Pools via Datapack auf Pack-Items (Saatgut, Deko) anpassbar; Reputation = natuerliches Rufsystem.
- **Quest:** Hoch — eigenstaendige rotierende Bounties, unabhaengig von FTB Quests, mit zufaelliger Rotation (das was FTB fehlt).
- **Progression:** Hoch — Reputation gated seltene Belohnungen, baut Langzeit-Ziel auf.
- **Probleme:** Beta-Version fuer 1.21.1 — Stabilitaet/Update pruefen. Reward-Pools muessen via Datapack kuratiert werden, sonst Vanilla-lastig und thematisch unpassend. Moegliche Ueberschneidung mit Tagesbrett — Rollen klar trennen (Bountiful = Mob/Sammel, FTB = Farm/Cook).

### Wochenmarkt / Saison-Lieferauftraege (Serene Seasons-gekoppelte FTB-Quests)  
*Typ: system*

- **Nutzen:** Woechentlich wechselnder Grossauftrag ('Diese Woche: 64 Tomaten fuer das Erntefest'), der nur mit aktuell saisonal anbaubaren Crops loesbar ist. Erzeugt Wochen-Ziel zwischen den Tages-Loops und nutzt das vorhandene Serene-Seasons-System narrativ.
- **Integration:** FTB Quest mit 7-Tage-Cooldown; Quest-Sichtbarkeit/Tasks via KubeJS an Serene-Seasons-Saison gekoppelt (z.B. Sommer-Crops gefragt). Belohnung: Smaragd-Bonus + seltenes Saatgut.
- **Quest:** Sehr hoch — narrative Aufhaenger (Erntefest, Wintervorrat) tragen ganze Quest-Linien.
- **Progression:** Hoch — groessere Belohnungen als Tagesbrett; staffelbar nach Stadtstufe.
- **Probleme:** Saison-Kopplung erfordert KubeJS-Abfrage des Serene-Seasons-State (API pruefen). Spieler ohne grosse Farm koennen Wochenauftrag verfehlen — Mengen an Spielerzahl/Fortschritt anpassen.

### Dorf-Ausbaustufen ('Town Tiers' via FTB Quests-Meilensteine)  
*Typ: system*

- **Nutzen:** Die gesamte Stadt hat sichtbare Ausbaustufen (Weiler -> Dorf -> Stadt), die das ganze SMP-Team gemeinsam durch gesammelte Lieferungen/abgeschlossene Quests freischaltet. Jede Stufe schaltet neue Gebaeude, Haendler und Tagesbrett-Aufgaben frei — das Animal-Crossing-'Stadt waechst'-Gefuehl.
- **Integration:** FTB Quests Reward-Gates + KubeJS-Schalter, der MineColonies-Ausbau / neue Structurize-Gebaeude / neue Villager-Haendler (Easy Villagers, Trade Cycling) freischaltet. Team-weiter Fortschritt via FTB Teams.
- **Quest:** Sehr hoch — strukturiert die gesamte FTB-Quest-Map als Stadtentwicklungs-Baum.
- **Progression:** Sehr hoch — Kern-Langzeitprogression des ganzen Packs; bindet alle anderen Systeme.
- **Probleme:** Komplexer Aufbau, viele Abhaengigkeiten (MineColonies + KubeJS + FTB). Auf SMP: Trittbrettfahrer profitieren ohne Beitrag — ggf. Beitrags-Tracking. Freischalt-Logik fuer Gebaeude technisch anspruchsvoll.

### NPC-Beziehungs- & Geschenksystem (Town Talk + KubeJS-Affinitaet)  
*Typ: system*

- **Nutzen:** Stardew-Kernschleife: jedem benannten Dorf-NPC taeglich ein Geschenk geben hebt Beziehungslevel (Herzen). Hoehere Level schalten besseren Handel, Dialoge (Town Talk) und kleine Geschenke der NPCs frei. Starker taeglicher Wiederkehr-Anreiz.
- **Integration:** Town Talk (enthalten) liefert NPC-Dialoge; KubeJS trackt pro-NPC-pro-Spieler Affinitaet bei Item-Rechtsklick auf Villager. Lieblingsgeschenke aus Pam's/Farmer's-Delight-Food. Belohnung ueber Trade-Cycling-Freischaltung.
- **Quest:** Hoch — Beziehungs-Meilensteine als versteckte FTB-Quests ('Freundschaft mit dem Baecker').
- **Progression:** Hoch — Herzen-System ueber viele NPCs = breites Langzeitziel.
- **Probleme:** Vanilla/Easy-Villager sind generisch — benannte, wiederkehrende NPCs erfordern feste Spawns/Namen (KubeJS oder Custom-Mod). Geschenk-Detektion am Villager technisch fummelig (Rechtsklick-Event + Item-Konsum).

### Fang-Sammelalbum (KubeJS-Codex fuer Aquaculture + Fish of Thieves)  
*Typ: system*

- **Nutzen:** Ein 'Anglerbuch', das jeden je gefangenen Fisch (Aquaculture, Fish of Thieves) mit Groesse/Rekord protokolliert. Treibt wiederholtes Angeln zu unterschiedlichen Tages-/Saison-/Biom-Zeiten an — klassischer 'noch diesen einen Fisch'-Loop.
- **Integration:** KubeJS Fishing-Event-Hook schreibt in pro-Spieler-NBT; Anzeige via Buch-Item-GUI oder FTB-Quest-Kapitel als Checkliste. Nutzt vorhandenes Aquaculture (Fischarten, Rekordgroessen) + Fish of Thieves.
- **Quest:** Hoch — 'Alle Fische gefangen'-Quest pro Biom/Saison als Sammel-Achievement.
- **Progression:** Hoch — Fischvielfalt + Groessenrekorde = dauerhafte Beschaeftigung.
- **Probleme:** KubeJS muss Aquaculture/FoT Fang-Events sauber abgreifen (API/Event-Namen pruefen). Groessenrekord-Tracking bei FoT vorhanden, Vereinheitlichung mit Aquaculture noetig. GUI-Eigenbau aufwendig — FTB-Quest-Checkliste als pragmatischer Fallback.

### Erntefeste / Saison-Events (zeitlich begrenzte Event-Quests)  
*Typ: system*

- **Nutzen:** Pro Serene-Seasons-Saison ein mehrtaegiges Event (Fruehlingsblueten-Fest, Sommer-Angelturnier, Herbst-Erntedank, Winter-Sternennacht) mit exklusiven Belohnungen, die es nur in diesem Zeitfenster gibt. Schafft FOMO-getriebene Wiederkehr zu Saisonwechseln.
- **Integration:** FTB Quests Event-Kapitel via KubeJS zeitgesteuert ein-/ausgeblendet (Saison-Check). Deko-Belohnungen aus Supplementaries/Macaw's/Handcrafted; Festbauten via Structurize/Dungeons & Taverns-Style. Town Talk kuendigt Events an.
- **Quest:** Sehr hoch — jedes Fest ist ein eigener kleiner Quest-Strang mit Story.
- **Progression:** Mittel-hoch — exklusive saisonale Deko/Trophaeen als Sammlerziel ueber das Spieljahr.
- **Probleme:** Zeitsteuerung an Serene-Seasons-Datum koppeln (KubeJS-Saison-API pruefen). Wiederkehrende Events brauchen Cooldown/Jahres-Logik, damit Belohnungen nicht jaehrlich farmbar entwerten. Hoher Content-Erstellungsaufwand pro Fest.

### Achievement-/Titel-System ueber Vanilla Advancements + KubeJS  
*Typ: system*

- **Nutzen:** Cozy-thematische Erfolge ('Erster Hektar', 'Meisterkoch — 50 Gerichte', 'Tierfluesterer — alle Naturalist-Tiere gezaehmt') mit sichtbaren Titeln/Abzeichen. Gibt langfristige Selbst-Ziele und Statusvergleich im SMP.
- **Integration:** Vanilla Advancement-Datapack + KubeJS fuer komplexe Bedingungen; Titel-Anzeige via Chat-Praefix/Nametag (KubeJS). Zaehlt Aktionen aus allen vorhandenen Mods (Cooking, Farming, Taming, Building).
- **Quest:** Mittel — Advancements ergaenzen FTB-Quests, ueberschneiden sich aber teils; klare Aufgabentrennung noetig.
- **Progression:** Hoch — breite, dauerhafte Zielliste ueber alle Spielsysteme.
- **Probleme:** Doppelung mit FTB Quests vermeiden (FTB = gefuehrt, Advancements = optional/sammelnd). Titel-Praefix-System ist KubeJS-Eigenbau. Viele Custom-Advancements = JSON-Pflegeaufwand.

### Stadt-Ruf / Bewohner-Zufriedenheit (aggregierter Town-Reputation-Wert)  
*Typ: system*

- **Nutzen:** Ein globaler, im Rathaus angezeigter Stadt-Zufriedenheitswert, der durch Quest-Abschluesse, Deko-Dichte und NPC-Beziehungen steigt und bei vernachlaessigten Aufgaben langsam faellt. Gibt dem 'kurz reinschauen' einen Pflege-Charakter (Stadt nicht verkommen lassen).
- **Integration:** KubeJS-Globalwert, gespeist aus Tagesbrett-Abschluessen, Bountiful-Reputation, NPC-Affinitaet und vorhandenem 'What Are They Up To'/'Smarter Farmers'-Dorfleben. Anzeige via Scoreboard/Town-Talk-Schild.
- **Quest:** Mittel — Ruf-Schwellen schalten Stadt-Quests/Haendler frei.
- **Progression:** Hoch — koppelbar an Town-Tiers; sinkender Wert erzeugt sanften Pflegedruck.
- **Probleme:** Decay-Mechanik kann frustrieren, wenn Spieler pausieren — Decay nur bei aktiven Spielern oder sehr langsam. Komplexe Aggregation vieler Quellen in KubeJS, Tuning-intensiv. Reiner Eigenbau.

### Versammlungsrang fuer Spieler (Buerger-Stufen mit Freischaltungen)  
*Typ: system*

- **Nutzen:** Persoenlicher Rang pro Spieler (Neuankoemmling -> Buerger -> Aeltester) basierend auf gesammelten Beitragspunkten. Hoehere Raenge schalten Baurechte, exklusive Trades, Heimstein-Funktionen oder kosmetische Perks frei. Bindet Einzelspieler-Fortschritt auf SMP.
- **Integration:** KubeJS-Punktekonto, gespeist aus Quests/Lieferungen/Museum-Spenden. Freischaltungen via FTB Quests-Gates und FTB Chunks (mehr Claims pro Rang). Anzeige via Nametag-Praefix.
- **Quest:** Mittel — Rangaufstiege als Meilenstein-Quests.
- **Progression:** Sehr hoch — persoenliche Langzeitprogression parallel zum Team-Town-Tier.
- **Probleme:** Balancing der Punktquellen gegen Exploits (z.B. billige Massen-Crops). FTB-Chunks-Claim-Kopplung erfordert KubeJS-API-Zugriff auf Claim-Limits (pruefen). Eigenbau, kein Fertig-Mod.

### Tierzucht-Pokal / Stammbaum-Sammlung (Naturalist + Critters & Companions)  
*Typ: system*

- **Nutzen:** Sammel-/Zuchtziel: alle Tierarten aus Naturalist und Critters & Companions zaehmen/halten, plus Zucht-Varianten (Fellfarben, seltene Spawns). Treibt taegliche Tierpflege und Erkundung an — das Animal-Crossing-'Bewohner sammeln'-Gefuehl auf Tiere uebertragen.
- **Integration:** KubeJS trackt gezaehmte/gehaltene Arten pro Spieler; nutzt vorhandene Naturalist + Critters & Companions + Companions Dogfolk + Ribbits. Checkliste als FTB-Quest-Kapitel.
- **Quest:** Hoch — 'Arche'-Quest pro Tiergruppe.
- **Progression:** Hoch — viele Arten + Varianten = breites Sammelziel.
- **Probleme:** Detektion 'Art im Besitz' (Leash/Stall/Naehe) ist in KubeJS heikel — vereinfachte Trigger (einmal gezaehmt = gezaehlt) pragmatischer. Varianten/Fellfarben je nach Mod evtl. nicht abfragbar.

### Heimstein & Pendel-Loop (Waystones als taegliche Routen-Infrastruktur)  
*Typ: mod*

- **Nutzen:** Waystones im Rathaus/auf Farmen erlauben schnelle Tagesrunden (Farm -> Markt -> Mine -> Heim) ohne Reise-Frust. Senkt die Reibung des taeglichen Loops massiv und macht 'kurz einloggen' tatsaechlich kurz.
- **Integration:** Waystones 21.1.x fuer 1.21.1 NeoForge (verifiziert verfuegbar). Integriert mit vorhandenem JourneyMap (Waypoint-Sync via Kompatibilitaets-Addon, Verfuegbarkeit pruefen). Client-only Renderaspekte beachten — Mod selbst ist both-sides.
- **Quest:** Niedrig — eher Infrastruktur; 'erste Waystone setzen' als Tutorial-Quest moeglich.
- **Progression:** Mittel — gestaffelte Reichweite/Kosten als sanfte Progression konfigurierbar.
- **Probleme:** Schnellreise kann Welt 'kleiner' machen und Erkundungs-Retention senken — Aktivierungskosten/Distanzlimits balancen. JourneyMap-Waystone-Sync-Addon-Kompatibilitaet pruefen.

### Tagesgericht / Kochbuch-Komplettierung (Farmer's Delight-Addons als Rezept-Sammlung)  
*Typ: system*

- **Nutzen:** Ein Kochbuch-Sammelziel: jedes Gericht aus dem riesigen Delight-Addon-Stack (Chefs/Rustic/Cultural/Nethers/etc.) einmal kochen schaltet einen Eintrag frei; taegliches 'Tagesgericht' gibt Bonus. Nutzt den vorhandenen Cooking-Content als Langzeit-Checkliste.
- **Integration:** KubeJS Crafting-Event-Hook auf Cooking-Pot-Rezepte; Fortschritt als FTB-Quest-Kapitel. Tagesgericht via Tagesbrett-Integration. Belohnungen: neue Rezepte/Buffs.
- **Quest:** Sehr hoch — hunderte Delight-Rezepte = umfangreicher Sammel-Questbaum.
- **Progression:** Sehr hoch — schiere Rezeptmenge traegt monatelange Progression.
- **Probleme:** Sehr viele Rezepte sauber zu tracken ist JSON-/KubeJS-intensiv. Cooking-Pot-Output-Detektion ueber alle Addons konsistent abgreifen. Gefahr der Ueberforderung — gut kuratieren/kategorisieren.

### Glueckstag / Taegliches Drehrad (KubeJS-Daily-Loot)  
*Typ: feature*

- **Nutzen:** Einmal pro Tag am Rathaus eine 'Gluecks-Truhe' oeffnen / Rad drehen fuer ein zufaelliges kleines Geschenk (Saatgut, Deko, Smaragde, seltene Zutat). Niedrigschwelliger, garantierter taeglicher Belohnungsmoment — der reinste 'kurz einloggen'-Trigger.
- **Integration:** KubeJS Block-Rechtsklick mit 24h-pro-Spieler-Cooldown, gewichtete Loot-Table aus Pack-Items. Optional als Supplementaries-Praesent-Block oder Custom-Block (Kartoffelboss-Mod).
- **Quest:** Niedrig — reiner Belohnungs-Loop, kaum Quest-Inhalt.
- **Progression:** Niedrig-mittel — kleine Items, ggf. seltene Sammel-Deko im Pool.
- **Probleme:** Per-Spieler-Cooldown-Persistenz in KubeJS (NBT) noetig. Loot-Balance: zu gut = entwertet Wirtschaft, zu schwach = ignoriert. Reiner Eigenbau.

### Stadtchronik / Schwarzes Brett (Town Talk-Ankuendigungen als Live-Feed)  
*Typ: system*

- **Nutzen:** Ein Brett, das dynamisch aktuelle Stadtereignisse anzeigt: 'Saison wechselt in 2 Tagen', 'Erntefest laeuft', 'Baecker hat Geburtstag', 'Wochenauftrag offen'. Gibt dem Spieler beim Login sofort einen Grund/eine To-do-Liste — reduziert 'was soll ich tun?'-Abbrueche.
- **Integration:** Town Talk (enthalten) + KubeJS, das Saison-, Event- und Quest-State in Schild-/GUI-Text rendert. Bells & Whistles fuer Atmosphaere am Brett.
- **Quest:** Niedrig — informativ, verweist aber auf alle anderen Quest-Systeme.
- **Progression:** Niedrig — Tool/Onboarding, keine eigene Progression.
- **Probleme:** Dynamischer Text-Render aus mehreren Quellen ist KubeJS-Aufwand. Town Talk ist primaer NPC-Smalltalk — Eignung als strukturiertes Info-Board pruefen, ggf. Schild/Buch-Fallback.

### Freundschafts-Boni & gemeinsame Team-Wochenziele (FTB Teams)  
*Typ: system*

- **Nutzen:** Woechentliches Team-Gesamtziel (z.B. '500 Crops gemeinsam liefern') mit Belohnung fuer alle Mitglieder. Foerdert Koordination, Verabredungen und sozialen Druck zurueckzukommen ('die anderen warten auf meinen Anteil') — starker SMP-Retention-Hebel.
- **Integration:** FTB Quests Team-Quest mit Wochen-Cooldown ueber FTB Teams (beide enthalten); Fortschritt team-aggregiert. Belohnung fuer alle: Stadtbau-Material, Smaragde.
- **Quest:** Hoch — eigene Team-Quest-Linie parallel zu Solo-Quests.
- **Progression:** Hoch — koppelbar an Town-Tier-Aufstieg.
- **Probleme:** Team-Aggregation in FTB Quests pruefen (manche Tasks zaehlen nur Einzel-Inventar). Solo-Spieler/Einzel-Teams duerfen nicht ausgeschlossen werden — skalierte Ziele noetig.

### Sammelkarten / Bewohner-Steckbriefe (Custom-Item-Set via KubeJS)  
*Typ: item*

- **Nutzen:** Sammelbare 'Bewohner-Karten' fuer jeden NPC und seltene 'Fundkarten' fuer Tiere/Fische, die als Drop bei hoher Affinitaet / seltenem Fang erscheinen. Tausch- und Sammelobjekt mit Animal-Crossing-Amiibo-Charme; treibt Beziehungs- und Sammelsysteme zusammen.
- **Integration:** KubeJS-Custom-Items (oder Kartoffelboss-Mod), Drops gekoppelt an NPC-Affinitaet und Fang-/Zucht-Events. Anzeige/Aufbewahrung in Supplementaries-Rahmen/Sophisticated-Storage. Komplett-Set = FTB-Quest.
- **Quest:** Hoch — 'Alle Karten sammeln' als Meta-Sammelquest.
- **Progression:** Hoch — Sammel- und Tauschwirtschaft unter Spielern.
- **Probleme:** Custom-Item-Texturen/Modell-Aufwand (KubeJS-Items sind simpel, viele Varianten = viel Arbeit). Drop-Trigger an Affinitaet koppeln setzt das NPC-Beziehungssystem voraus (Abhaengigkeit).

### Saatgut- & Sorten-Sammlung (Pam's HarvestCraft 2 als Botanik-Album)  
*Typ: system*

- **Nutzen:** Botanik-Sammelziel: jede der zahlreichen Pam's-/Let's-Do-Vinery-Crop-Sorten einmal anbauen und ernten schaltet einen Eintrag frei. Foerdert breites Farmen ueber Saisons hinweg statt Monokultur — Stardew-'alle Crops anbauen'-Loop.
- **Integration:** KubeJS Harvest-/Crop-Break-Event auf Pam's-Crops + Let's Do Vinery-Trauben; Checkliste als FTB-Quest. Belohnung: seltene Saemereien, Garten-Deko.
- **Quest:** Hoch — Sorten-Komplettierung pro Saison/Kategorie als Quest.
- **Progression:** Hoch — Pam's hat sehr viele Crops = langes Sammelziel.
- **Probleme:** Crop-Harvest-Detektion ueber Pam's + andere Crop-Mods konsistent abgreifen. Serene-Seasons schraenkt Anbauzeitfenster ein — Sammlung kann sich ueber ein ganzes In-Game-Jahr ziehen (Feature, aber Geduld noetig).

### Persoenliches Farm-Bewertungssystem ('Hofbeurteilung' à la Grandpa's Evaluation)  
*Typ: system*

- **Nutzen:** Periodische (z.B. monatliche In-Game) Bewertung der eigenen Farm/des Grundstuecks nach Punkten: Crop-Vielfalt, Tiere, Deko-Dichte, Gebaeude, abgeschlossene Quests. Vergibt Sterne/Rang und konkretes Feedback ('mehr Blumen pflanzen'). Direkt aus Stardew uebernommener Langzeit-Wiederkehr-Anreiz.
- **Integration:** KubeJS scannt Spieler-Claim (FTB Chunks) periodisch auf zaehlende Bloecke/Entities aus vorhandenen Deko-/Farm-/Tier-Mods; Ergebnis via Town Talk/Brief. Sterne schalten kosmetische Trophaeen frei.
- **Quest:** Mittel — Sternen-Schwellen als Meilenstein-Quests.
- **Progression:** Sehr hoch — offener, nie 'fertiger' Hof-Ausbau als Dauerziel.
- **Probleme:** Block-/Entity-Scan ueber Claim-Bereich ist performance-sensibel — selten und asynchron ausfuehren. Sehr tuning-intensive Bewertungsformel. Reiner KubeJS-Eigenbau mit FTB-Chunks-API-Abhaengigkeit (pruefen).


## social (19)

### MCA Reborn (Minecraft Comes Alive Reborn)  
*Typ: mod*

- **Nutzen:** Das zentrale Stardew-aehnliche Beziehungssystem: verwandelt Villager in menschliche NPCs mit Namen, Geschlecht, Persoenlichkeit, Stimmung und Genetik. Herzsystem (Freundschaft -> Romanze), Heirat per Ehering, Kinder mit vererbten Traits, Geschenke, Smalltalk, NPCs koennen Aufgaben uebernehmen (jagen, ernten, bewachen). Verfuegbar als NeoForge 1.21.1 v7.7.x (verifiziert auf Modrinth).
- **Integration:** Ersetzt vanilla Villager durch Menschen-NPCs. ACHTUNG: ueberschneidet sich stark mit Villagers Reborn und teils mit Easy Villagers/Guard Villagers Optik. Nur EINEN Beziehungs-Overhaul waehlen. Passt zur Wirtschaft (behaelt Smaragd-Trades). Mit MineColonies kompatibel pruefen, da beide Villager-Logik anfassen.
- **Quest:** FTB-Quest-Kette: 'Werde Teil der Gemeinschaft' — erstes Geschenk verschenken, X Herzen mit 3 NPCs, Verlobung, Hochzeit, erstes Kind grossziehen. Jeder Schritt als Questbelohnung.
- **Progression:** Sehr hoch: Herzlevel pro NPC, Heiratsstatus, Familiengruendung, NPC-Berufe freischalten. Langfristige Bindung an einen Spielort.
- **Probleme:** Konflikt mit anderen Villager-Overhauls (Villagers Reborn). Kann mit MineColonies-Buergern doppeln. Performance bei vielen NPCs. Server-seitig zwingend; alle Clients brauchen Mod. Optik (menschliche Modelle) muss zum Cozy-Stil passen — pruefen ob mit Fresh Animations kompatibel.

### Villagers Reborn  
*Typ: mod*

- **Nutzen:** Leichtere Alternative zu MCA: ersetzt Villager und Illager durch menschliche Modelle, behaelt vanilla Berufe/Trades, fuegt Dialogbildschirme, Persoenlichkeiten, Familienstammbaeume, Dating, Heirat (mit Hochzeits-Cutscene) und Villager-Editor (Slider) hinzu. NeoForge 1.21.1, Client+Server, veroeffentlicht Okt 2025 (verifiziert).
- **Integration:** Direkte Alternative/Konkurrenz zu MCA Reborn — NICHT beide gleichzeitig. Weniger invasiv als MCA, behaelt Trades komplett bei, daher besser fuer die Smaragd-Wirtschaft. Mit Town Talk/Bells & Whistles kosmetisch kompatibel pruefen.
- **Quest:** Quest 'Lerne deine Nachbarn kennen': Dialoge mit jedem NPC-Typ fuehren, Stammbaum aufbauen, eine Ehe schliessen. Editor nutzen um einen 'Lieblings-NPC' zu erstellen als Quest-Reward.
- **Progression:** Mittel-hoch: Beziehungsstufen, Heirat, Familie. Editor erlaubt kosmetische Progression.
- **Probleme:** Relativ jung (v1.0.x), Stabilitaet/Balance pruefen. Konflikt mit MCA und ggf. anderen Modell-Replacern (3D Skin Layers, Fresh Animations). Illager-Ersetzung kann mit Raids/Dungeons & Taverns kollidieren.

### Your Reputation  
*Typ: mod*

- **Nutzen:** Zeigt deine Reputation bei einzelnen Villagern als Tooltip-Stufen (Friendly/Trustworthy/Neutral/Suspicious/Hostile) basierend auf Handlungen. Macht das versteckte vanilla Gossip-System sichtbar — Grundlage fuer ein Stardew-Freundschafts-Feeling ohne Modell-Overhaul. (Verfuegbarkeit fuer 1.21.1 NeoForge pruefen — Listing zeigt 1.21.10/1.20.1).
- **Integration:** Sehr leichtgewichtig, nicht-invasiv, ergaenzt MineColonies/Easy Villagers statt sie zu ersetzen. Liefert das sichtbare 'Freundschaftslevel', das in Vanilla fehlt, ohne Villager-Modelle anzufassen.
- **Quest:** Quest 'Vom Fremden zum Freund': erreiche 'Trustworthy' bei 5 Villagern. Reputation als Gate fuer bessere Trades nutzbar (via KubeJS).
- **Progression:** Mittel: klare Reputationsstufen, die ueber Zeit steigen. Lieferte Skala fuer KubeJS-Belohnungen.
- **Probleme:** Version 1.21.1 NeoForge unsicher — pruefen oder per KubeJS nachbauen. Nur Anzeige, keine echten Geschenk-Mechaniken — muss mit anderem System kombiniert werden.

### VNDialog  
*Typ: mod*

- **Nutzen:** Fuegt Visual-Novel-Dialoge fuer NPCs hinzu (Portrait + verzweigte Texte, per Command/Datapack auslosbar). Ermoeglicht Stardew-artige Charaktergespraeche und Story-Szenen mit benannten Town-NPCs. Forge+NeoForge 1.21.1 (verifiziert).
- **Integration:** Perfekt fuer questgetriebene Storylines mit FTB Quests: Quest startet Dialog, Dialog-Auswahl beeinflusst Quest-Fortschritt. Laesst sich mit Town Talk und beliebigem Villager-System kombinieren, da rein Dialog-Layer.
- **Quest:** Sehr hoch: jeder Town-NPC bekommt eine Dialog-Questreihe (Buergermeister, Laedner, Farmer). Verzweigte Entscheidungen, Charakter-Introductions, Festival-Ankuendigungen.
- **Progression:** Hoch: Dialoge koennen sich je nach Quest-/Freundschaftsstand aendern, neue Gespraechszweige freischalten.
- **Probleme:** Erfordert manuelle Autorenarbeit (jeder Dialog muss geschrieben werden). Command/Datapack-Steuerung — Integration mit FTB Quests via KubeJS-Trigger noetig.

### KubeJS-Geschenksystem mit Lieblingsgegenstaenden  
*Typ: custom-mod*

- **Nutzen:** Kern des Stardew-Gift-Gefuehls selbst gebaut: Rechtsklick auf einen Villager mit Item -> KubeJS prueft NPC-Beruf/ID gegen eine Liebes/Mag/Neutral/Hasst-Tabelle und vergibt Freundschaftspunkte + Feedback (Partikel/Sound/Chat). Z.B. Farmer liebt Farmer's-Delight-Gerichte, Fischer liebt Aquaculture-Fische.
- **Integration:** Nutzt bereits vorhandenes KubeJS + die riesige Food-/Item-Palette (HarvestCraft, Farmer's Delight Addons, Let's Do, Bountiful Fares). Speichert Punkte in NBT/Persistent Data; kann Your-Reputation oder ein eigenes Herzsystem fuettern. Kein neuer Mod-Download noetig.
- **Quest:** Sehr hoch: 'Finde Almas Lieblingsessen', 'Schenke jedem Beruf sein Lieblingsitem'. Lieblingsgegenstaende als Sammel-/Entdeckungs-Quests.
- **Progression:** Hoch und voll anpassbar: Punkteschwellen schalten Trades, Dialoge, Geschenke der NPCs frei. Voellige Designkontrolle ueber die Kurve.
- **Probleme:** Reiner Skript-Aufwand (Datentabellen pflegen). Persistenz pro NPC-Instanz tricky bei vanilla Villagern (UUID-Tracking). Balancing der Punkte. Kein UI out-of-the-box — Feedback nur Chat/Partikel ausser man baut GUI.

### FTB-Quests Beziehungs-Kapitel (Freundschafts-Tracker)  
*Typ: custom-mod*

- **Nutzen:** Ein dediziertes FTB-Quests-Kapitel 'Gemeinschaft' bildet Beziehungsstufen pro Schluessel-NPC als Quest-Knoten ab. Jede 'Freundschaft' ist eine Questkette mit Geschenk-/Gespraechs-Aufgaben; Belohnungen sind freigeschaltete Trades, Deko, Titel.
- **Integration:** Nutzt vorhandene FTB Quests/Library. Verbindet sich mit KubeJS-Gift-System ueber Custom-Tasks/Observe-Triggers. Macht das sonst unsichtbare Beziehungssystem im UI sichtbar und belohnt es.
- **Quest:** Ist selbst der Quest-Inhalt: pro NPC ein Strang, plus uebergreifende 'werde Teil der Stadt'-Meta-Quest.
- **Progression:** Sehr hoch: klar visualisierte Stufen, Belohnungen pro Herzlevel, freischaltbare NPC-Inhalte.
- **Probleme:** Manueller Authoring-Aufwand pro NPC. FTB-Tasks koennen 'Beziehung' nur indirekt messen — braucht KubeJS-Brueckenlogik.

### Custom Eheringe & Verlobungs-Items (KubeJS)  
*Typ: item*

- **Nutzen:** Selbst definierte Items 'Verlobungsring', 'Ehering', 'Blumenstrauss', 'Liebesbrief' — Verlobungs-/Heiratsmechanik als Item-Use auf einem NPC bei ausreichend Freundschaftspunkten. Gibt der Romanze ein greifbares Crafting-Ziel.
- **Integration:** KubeJS-Items + Rezepte (z.B. Ring aus Gold+Diamant via Create-Pressing fuer Create-Fokus). Triggert das Gift/Reputations-System. Funktioniert mit oder ohne MCA — bei MCA stattdessen dessen Ring nutzen.
- **Quest:** Hoch: 'Schmiede den Ring' (Create-Quest), 'Pflueck die seltene Blume', 'Schreibe den Liebesbrief'. Romanze als mehrstufige Quest.
- **Progression:** Hoch: Items als Gates fuer Beziehungsmeilensteine; teurere Ringe fuer hoehere Stufen.
- **Probleme:** Wenn MCA/Villagers Reborn genutzt wird, kollidiert eigene Heiratsmechanik mit deren — dann nur als Geschenk-Items behalten. Item-Use-Event-Logik in KubeJS muss NPC-Status pruefen.

### Town Reputation / Stadt-Standing-System (KubeJS + FTB)  
*Typ: system*

- **Nutzen:** Globaler Stadt-Ruf zusaetzlich zu Einzel-NPC-Freundschaften: Aktionen (Quests erfuellen, Gebaeude bauen, Festivals besuchen) heben das Standing der ganzen Stadt; Schwellen schalten neue NPCs, Laeden, Events frei — wie Stardews 'Community Center'-Fortschritt.
- **Integration:** FTB Quests Fortschritt + KubeJS-Counter. Verbindet sich mit MineColonies (Kolonie-Level) und Dynamic Village (Create). Ein Wert pro Spielergruppe (FTB Teams).
- **Quest:** Sehr hoch: gestaffelte Stadt-Meilensteine, 'restauriere die Stadt'-Bundles aehnlich Community Center.
- **Progression:** Sehr hoch: Stadt waechst sichtbar mit Standing; neue NPCs/Gebaeude/Trades als Belohnung.
- **Probleme:** Komplexes Skripting und Balancing. Multiplayer: shared vs. per-Team Standing klaeren (FTB Teams hilft). Ueberlappung mit MineColonies-Progression vermeiden.

### Geschenk-Briefkasten / Postsystem (Supplementaries + KubeJS)  
*Typ: feature*

- **Nutzen:** Jeder NPC bekommt einen Briefkasten (Supplementaries hat bereits Briefkasten/Mailbox-Bloecke); Spieler legt taegliche Geschenke hinein -> KubeJS vergibt Freundschaftspunkte und der NPC 'antwortet' per Brief/Dialog. Stardews taegliches Schenk-Ritual ohne den NPC physisch finden zu muessen.
- **Integration:** Nutzt bereits enthaltenes Supplementaries (Mailbox) + KubeJS. Limit 'ein Geschenk pro Tag pro NPC' (Serene Seasons / Tageszeit-Trigger) baut Routine auf.
- **Quest:** Mittel: 'Liefere jedem Nachbarn ein Geschenk'. Briefantworten koennen Mini-Quests starten.
- **Progression:** Mittel-hoch: taegliche Punktevergabe -> stetige Beziehungs-Steigerung; Tageslimit als Pacing.
- **Probleme:** Mailbox-NPC-Zuordnung per Position/UUID skripten. Tageszeit-Reset-Logik. Reine KubeJS-Loesung, etwas Aufwand.

### Festival- & Event-Kalender (Serene Seasons + KubeJS + VNDialog)  
*Typ: system*

- **Nutzen:** Saisonale Stadtfeste (Fruehlings-Blumenfest, Erntedank im Herbst, Winter-Sternennacht) wie in Stardew/Animal Crossing: an festen Tagen spawnen Deko/Staende, NPCs versammeln sich, es gibt Mini-Aktivitaeten und Beziehungsboni fuers Teilnehmen.
- **Integration:** Serene Seasons (vorhanden) liefert Datum/Jahreszeit; KubeJS triggert Events; VNDialog/Town Talk fuer Ankuendigungen; Deko aus Let's Do Beachparty, Macaw's, Supplementaries.
- **Quest:** Sehr hoch: jedes Fest eine Event-Quest mit Vorbereitung (koche Gericht, sammle Blumen) und Teilnahme-Belohnung.
- **Progression:** Hoch: wiederkehrende jaehrliche Events, freischaltbare Festival-Inhalte mit steigendem Stadt-Standing.
- **Probleme:** Erheblicher Skript-Aufwand (Kalenderlogik, Spawning, Aufraeumen). Timing/Trigger-Zuverlaessigkeit auf Server. Pure Custom-Loesung.

### NPC-Lieblings-Tageszeit & Zeitplan (Smarter Farmers ergaenzend, KubeJS)  
*Typ: feature*

- **Nutzen:** NPCs haben sichtbare Tagesroutinen/Aufenthaltsorte (morgens Markt, mittags Feld, abends Taverne), und Geschenke/Gespraeche zur 'richtigen' Zeit/Ort geben Bonuspunkte — wie Stardews Charakterplaene, die Spieler kennenlernen.
- **Integration:** Baut auf vanilla/Smarter-Farmers-Schedules; KubeJS-Boni bei Ort+Zeit-Match. Town Talk/What Are They Up To zeigt was NPCs gerade tun.
- **Quest:** Mittel: 'Triff Bauer Jonas auf dem Feld bei Sonnenaufgang'. Routine-Kenntnis als Entdeckungs-Quest.
- **Progression:** Mittel: Lernkurve ueber NPC-Gewohnheiten; Bonus-Punkte beschleunigen Beziehungen.
- **Probleme:** Vanilla-Villager-Schedules sind begrenzt steuerbar. Ort/Zeit-Pruefung in KubeJS aufwaendig. Eher Komfort-Layer als Kernsystem.

### Heirats-Wohnhaus & Mitbewohner-NPC (Handcrafted/Interiors + KubeJS)  
*Typ: feature*

- **Nutzen:** Nach der Heirat zieht der Partner-NPC ins Spielerhaus, hilft bei Aufgaben (Tiere fuettern, ernten, kochen mit Farmer's Delight) und gibt taegliche kleine Geschenke — wie Stardews Ehepartner-Verhalten.
- **Integration:** Nutzt Handcrafted/Another Furniture/Interiors fuer Wohnraum; KubeJS fuer Partner-Verhalten; bei MCA uebernimmt MCA das nativ. Farmer's Delight Kochstationen als Partner-Aktivitaet.
- **Quest:** Mittel-hoch: 'Richte ein gemeinsames Zuhause ein', 'erlebe den ersten Morgen als Paar'.
- **Progression:** Hoch: Eheleben als laufendes Endgame mit taeglichen Interaktionen, Kindern, Heim-Upgrades.
- **Probleme:** Ohne MCA komplett selbst zu skripten (NPC-Pathing, Aufgaben). Hoher Aufwand. Mit MCA redundant — dann nur Moebel-Integration.

### Sammelalbum der Stadtbewohner (FTB Quests Detail-Seiten)  
*Typ: feature*

- **Nutzen:** Ein durchblaetterbares 'Bewohner-Album' (als FTB-Quest-Kapitel mit Portrait + Bio pro NPC), das Steckbriefe, Lieblingsgegenstaende und Beziehungsstand zeigt — das Stardew-Charakterprofil als Collection-Element.
- **Integration:** FTB Quests (vorhanden) als Anzeige-Layer; Eintraege schalten sich frei sobald man einen NPC trifft/befreundet (KubeJS-Observe). Verbindet Collection-RPG-lite-Pillar mit Social.
- **Quest:** Hoch: 'Vervollstaendige das Bewohner-Album' — jeden NPC kennenlernen schaltet seinen Eintrag frei.
- **Progression:** Hoch: Album-Vollstaendigkeit als Sammelziel; Eintraege zeigen wachsenden Beziehungsstand.
- **Probleme:** Authoring pro NPC. FTB-Quests als Album zweckentfremdet — Layout-Arbeit. Freischalt-Trigger via KubeJS noetig.

### Talk-Cooldown & taegliche Begruessung (Town Talk ergaenzend, KubeJS)  
*Typ: feature*

- **Nutzen:** Einmal pro Tag jeden NPC 'gruessen' (Rechtsklick) gibt einen kleinen Freundschaftspunkt + zufaelligen Spruch — etabliert Stardews 'taeglich mit allen reden'-Routine, die Beziehungen langsam waermt.
- **Integration:** Town Talk (vorhanden) liefert die Sprueche; KubeJS verwaltet 1x-pro-Tag-Cooldown und Punkte. Serene Seasons/Day-Counter als Reset.
- **Quest:** Niedrig-mittel: 'Begruesse jeden Bewohner an einem Tag'. Eher Daily-Habit als Quest.
- **Progression:** Mittel: kontinuierlicher passiver Beziehungsaufbau ueber Spielzeit.
- **Probleme:** Cooldown-Tracking pro NPC-UUID. Kann grindy/repetitiv wirken — niedrige Punktewerte ansetzen. Pures Skript.

### Beziehungs-gated Trades & Rabatte (KubeJS + Trade Cycling)  
*Typ: system*

- **Nutzen:** Hoeheres Freundschaftslevel schaltet exklusive Trades frei und gibt Smaragd-Rabatte beim jeweiligen NPC — verbindet das Social-System direkt mit der Smaragd-Wirtschaft und belohnt Beziehungspflege spuerbar.
- **Integration:** Nutzt vanilla Smaragd-Wirtschaft + Trade Cycling (vorhanden) + KubeJS zum Anpassen von Trade-Listen je nach Freundschaftspunkten. Verstaerkt den Nutzen jedes anderen Social-Features.
- **Quest:** Mittel: 'Werde Stammkunde' — erreiche Freundschaftsstufe X fuer den Geheim-Trade.
- **Progression:** Sehr hoch: greifbare Wirtschafts-Belohnung pro Beziehungsstufe; Anreiz langfristige Bindung.
- **Probleme:** Trade-Manipulation je NPC-Instanz in KubeJS nicht trivial (Offer-Events). Balancing der Rabatte gegen Wirtschaft. Abhaengig von einem funktionierenden Punktesystem.

### Geschenk-Reaktions-Feedback (Partikel/Sound via KubeJS)  
*Typ: feature*

- **Nutzen:** Sichtbares Stardew-Feedback beim Schenken: Herz-Partikel + froher Sound bei Lieblingsitem, graue Wolke + Murren bei gehasstem Item. Macht das unsichtbare Gift-System intuitiv lesbar ohne UI-Mod.
- **Integration:** KubeJS Partikel-/Sound-API auf das Gift-Event aufgesetzt; nutzt vanilla Partikel + Sounds. Reine Ergaenzung zum Gift-System, kein neuer Mod.
- **Quest:** Niedrig: unterstuetzt Gift-Quests durch klares Feedback (Spieler lernt Vorlieben).
- **Progression:** Niedrig direkt, hoch indirekt — macht Beziehungsfortschritt fuehlbar und motivierend.
- **Probleme:** Nur Feedback-Layer, keine Mechanik fuer sich. Minimaler Skript-Aufwand. Haengt am Gift-System.

### Companions Dogfolk / Critters Begleiter als Beziehungsobjekte (vorhanden, neu genutzt)  
*Typ: system*

- **Nutzen:** Vorhandene Companions Dogfolk und Critters & Companions als 'Tier-/Begleiter-Beziehungen' ausbauen: Fuetter-/Pflege-Punkte, Lieblingsfutter (HarvestCraft/Farmer's Delight), Treue-Stufen — Animal-Crossing-artige Bindung zu Begleitern parallel zu NPCs.
- **Integration:** Mods sind bereits im Pack; nur KubeJS-Layer fuer Fuetter-Punkte + FTB-Quests fuer Pflege-Ziele ergaenzen. Kein neuer Download, erweitert vorhandenen Content.
- **Quest:** Hoch: 'Gewinne das Vertrauen des Dogfolk', 'finde das Lieblingsfutter deines Begleiters'.
- **Progression:** Hoch: Begleiter-Treuestufen mit freigeschalteten Faehigkeiten/Boni.
- **Probleme:** Haengt davon ab, wie offen die Mods fuer KubeJS-Hooks sind (pruefen). Risiko Ueberschneidung mit nativen Zaehm-Mechaniken.

### Geburtstags- & Gedenktag-System (KubeJS + Serene Seasons)  
*Typ: feature*

- **Nutzen:** Jeder Town-NPC hat ein festes Geburtstagsdatum; an dem Tag gibt ein Geschenk doppelte Punkte und der NPC reagiert besonders — exakt Stardews Geburtstags-Mechanik, die Spieler dazu bringt, den Kalender und die NPCs kennenzulernen.
- **Integration:** Serene Seasons-Datum + KubeJS-Datenbank (NPC -> Geburtstag) + Geschenk-System. Town Talk/VNDialog fuer besondere Geburtstags-Dialoge.
- **Quest:** Hoch: 'Feiere Maras Geburtstag', Kalender-Entdeckungsquests, Jahres-Sammelziel (alle Geburtstage besucht).
- **Progression:** Mittel-hoch: jaehrlich wiederkehrend; Geburtstagsgeschenke beschleunigen Beziehungen gezielt.
- **Probleme:** Erfordert festen In-Game-Kalender + NPC-Stammdaten pflegen. Datumserkennung in KubeJS via Serene Seasons API pruefen. Pure Custom-Arbeit.

### Liebesgrad-Titel & Kosmetik-Belohnungen (KubeJS + FTB Quests)  
*Typ: item*

- **Nutzen:** Beziehungsmeilensteine vergeben kosmetische Belohnungen: Titel ('Stadtfreund', 'Geliebter Nachbar'), Deko-Items, NPC-geschenkte Erinnerungsstuecke. Gibt der Beziehungs-Progression sammelbare, zeigbare Beute (RPG-lite/Collection-Pillar).
- **Integration:** FTB Quests Rewards + KubeJS Custom-Items; Deko aus Supplementaries/Macaw's/Handcrafted als NPC-Geschenke. Artifacts (vorhanden) koennte seltene Beziehungs-Artefakte liefern.
- **Quest:** Mittel: Belohnungsschicht fuer alle Beziehungs-Quests.
- **Progression:** Hoch: sichtbare Sammlung von Beziehungs-Trophaeen und Titeln als Langzeitziel.
- **Probleme:** Titel-Anzeige braucht ggf. Zusatzmod oder Chat-Praefix-Skript. Kosmetik-Items definieren = Aufwand. Reiner Belohnungs-Layer.


## world-immersion (27)

### Towns and Towers  
*Typ: mod*

- **Nutzen:** Ueberarbeitet Doerfer pro Biom mit ~50 neuen Strukturen (Doerfer, Pillager-Aussenposten, Schiffe) und macht die Welt visuell abwechslungsreicher und lebendiger. Verifiziert: v1.13.7 fuer 1.21.1 NeoForge/Fabric.
- **Integration:** Ergaenzt die bestehenden MineColonies/Dungeons-&-Taverns-Strukturen ohne Ueberschneidung. Doerfer dienen als Startpunkte fuer Spieler-Towns und als Quelle fuer Easy-Villagers-Handel.
- **Quest:** FTB-Quests koennen das Auffinden bestimmter Dorf-Varianten oder Strukturen als Explorationsziele setzen (z. B. 'Finde ein Wuesten-Marktdorf').
- **Progression:** Strukturierte Loot- und Handelsstufen ueber verschiedene Dorftypen schaffen Mid-Game-Erkundungsanreize.
- **Probleme:** Strukturkonflikte mit anderen Village-Overhauls moeglich (Spacing in Terralith/Tectonic pruefen). Datapack-basierte Generierung, daher serverseitig erforderlich.

### Better Villages (NeoForge)  
*Typ: mod*

- **Nutzen:** Wertet bestehende Vanilla-Doerfer auf: voller bewohnt, mehr Gebaeude, lebendiger und erkundenswerter. Verifiziert: v3.3.1 fuer 1.21.1 NeoForge (Mai 2025).
- **Integration:** Passt zum Cozy-Town-Building-Fokus und arbeitet mit Smarter Farmers / Guard Villagers / Easy Villagers zusammen, indem es mehr NPCs und Job-Sites bereitstellt.
- **Quest:** Quests zum Wiederaufbau oder Bevoelkern von Doerfern; 'Hilf dem Dorf X'-Questlinien als Town-Building-Einstieg.
- **Progression:** Mehr Villager-Berufe und Handelsstationen erweitern die Smaragd-Wirtschaft natuerlich.
- **Probleme:** Direkter Konflikt mit Towns and Towers moeglich (beide modifizieren Vanilla-Doerfer) — nur eines der beiden waehlen oder Spacing/Datapack-Prioritaet via KubeJS abstimmen.

### Alex's Mobs (1.21.1 Unofficial Port)  
*Typ: mod*

- **Nutzen:** Fuegt 85+ stilistisch hochwertige Tiere/Mobs hinzu, die die Welt biomweit deutlich belebter machen. Verifiziert: Unofficial Port v1.22.11 fuer 1.21.1 NeoForge.
- **Integration:** Ergaenzt Naturalist/Critters & Companions um exotischere Fauna, ohne thematisch zu kollidieren; viele Tiere liefern Cozy-Drops fuer Farmer's Delight / Pam's-Rezepte.
- **Quest:** Collection-Quests (FTB) zum Entdecken/Fotografieren/Zaehmen einzelner Spezies pro Biom.
- **Progression:** Tier-Drops als Crafting-Materialien und Zaehmungsziele bieten RPG-lite-Sammelfortschritt.
- **Probleme:** Unofficial Port — Stabilitaet/Updates pruefen (Verfuegbarkeit pruefen). Hoher Entity-Count kann Server-Performance belasten; Spawn-Weights ggf. via KubeJS senken.

### Friends&Foes (Forge/NeoForge)  
*Typ: mod*

- **Nutzen:** Bringt die abgewaehlten Mob-Vote-Kreaturen (Copper Golem, Crab, Glare, Moobloom, Iceologer, Rascal, Tuff Golem, Wildfire, Illusioner, Zombie Horse) im Vanilla-Stil — cozy und atmosphaerisch. Verifiziert fuer 1.21.1 NeoForge.
- **Integration:** Vanilla-treue passt perfekt zum Cozy-Look; Copper Golem und Tuff Golem ergaenzen Create-Deko/Automation-Aesthetik.
- **Quest:** Quests zum Auffinden/Heilen von Rascal (Loot-Spiel) oder Erschaffen von Tuff/Copper Golems als Dekoration.
- **Progression:** Moobloom als Bienen-/Bluetenquelle und Golems als craftbare Helfer bieten sanfte Fortschrittsbelohnungen.
- **Probleme:** Geringe Risiken; nur Mob-Cap-Balance mit Alex's Mobs / Naturalist beachten.

### Travelling and Trading  
*Typ: mod*

- **Nutzen:** Erweitert den unterbenutzten Wandering Trader und Villager-Handel: neue Profession 'Traveling Trader' via Curiosity Table, Wandering Cloth fuer Hood/Robe-Ruestung, neue Handelsfeatures. Verifiziert fuer 1.21.1 NeoForge.
- **Integration:** Staerkt die reisende-Haendler-Saeule der Vision und die Vanilla-Smaragd-Wirtschaft ohne Coin-Mod; ergaenzt Trade Cycling und Easy Villagers.
- **Quest:** Quests rund um seltene reisende Haendler und das Sammeln von Wandering-Cloth-Sets.
- **Progression:** Robe/Hood-Ruestung und neue Handelsketten geben dem Wirtschafts-Loop ein klares Ziel.
- **Probleme:** Moegliche Ueberschneidung mit anderen Wandering-Trader-Mods — nur eine Trader-Erweiterung waehlen, um Trade-Pools nicht zu doppeln.

### Wandering + (Wandering Trader Revamp)  
*Typ: mod*

- **Nutzen:** Ueberarbeitet den Wandering Trader mit balancierten, logischen Trades, die Begegnungen wirklich lohnenswert machen. Verifiziert fuer 1.21.1 NeoForge.
- **Integration:** Leichtgewichtige Alternative zu Travelling and Trading; greift sauber in die Smaragd-Wirtschaft ein und laesst sich via KubeJS feinjustieren.
- **Quest:** Quest 'Triff den reisenden Haendler 3x' oder spezielle Trade-Unlocks als Reward.
- **Progression:** Balancierte Trades fuellen Luecken im Wirtschafts-Loop ohne Inflation.
- **Probleme:** Nicht zusammen mit anderer Wandering-Trader-Trade-Mod (Travelling and Trading / BWTT) verwenden — Trade-Konflikt. Genau eine waehlen.

### When Dungeons Arise  
*Typ: mod*

- **Nutzen:** Goldstandard fuer grosse handgebaute Strukturen: schwebende Luftschiffe, Burgen, Aussenposten, unterirdische Labyrinthe — macht Erkundung spannend. Verifiziert fuer 1.21.1 NeoForge.
- **Integration:** Liefert Endgame-Erkundungsziele neben Dungeons & Taverns; Create-Spieler koennen Luftschiff-Strukturen mit Aeronautics anfahren.
- **Quest:** Starke Explorations-Questlinien (FTB): 'Erobere die Himmelsfestung', 'Pluendere die versunkene Bibliothek'.
- **Progression:** Gestaffelter Loot in immer schwierigeren Strukturen bietet klaren Mid/Late-Game-Fortschritt.
- **Probleme:** Grosse Strukturen koennen mit Terralith/Tectonic-Terrain clippen und Generierung verlangsamen — Spacing testen.

### Repurposed Structures (NeoForge/Forge)  
*Typ: mod*

- **Nutzen:** Fuegt Varianten von Vanilla-Strukturen in neuen Biomen hinzu (z. B. Dschungel-Festung, Wuesten-Aussenposten) und macht jedes Biom erkundenswerter. Verifiziert fuer 1.21.1 NeoForge.
- **Integration:** Spielt nachweislich gut mit YUNG's-Mods und Towns and Towers zusammen — Strukturen koexistieren. Erweitert Terralith-Biome mit passenden Bauten.
- **Quest:** Quests zum Auffinden seltener Strukturvarianten in ungewoehnlichen Biomen.
- **Progression:** Mehr Loot-Quellen und Handelsstationen verteilt ueber die Welt.
- **Probleme:** Viele Strukturen erhoehen Welt-Generierungslast; Konfiguration noetig, um Ueberfuellung mit anderen Struktur-Mods zu vermeiden.

### YUNG's Better Witch Huts (NeoForge)  
*Typ: mod*

- **Nutzen:** Mehrere neue Hexenhuetten-Varianten plus Hexenzirkel mit besserem Design und sinnvollerem Loot. Verifiziert: v4.1.1 fuer 1.21.1 NeoForge.
- **Integration:** Teil der gut getesteten YUNG's-Suite; passt in den atmosphaerischen, leicht magischen Cozy-Ton und ergaenzt Let's-Do-Herbal-Brews thematisch (Traenke/Kraeuter).
- **Quest:** Quest 'Finde den Hexenzirkel' mit Brau-Zutaten als Belohnung.
- **Progression:** Verbesserter Loot liefert Brau-/Alchemie-Materialien fuer den Mid-Game.
- **Probleme:** Kaum Risiken; mit anderen Struktur-Mods nur Spacing pruefen.

### YUNG's Better Desert Temples  
*Typ: mod*

- **Nutzen:** Vergroessert und ueberarbeitet Wuestentempel zu mehrstoeckigen, fallengespickten Strukturen mit besserem Loot und Atmosphaere. Teil der YUNG's-Suite (1.21.1 NeoForge, Verfuegbarkeit pruefen — Suite ist fuer 1.21.1 portiert).
- **Integration:** Ergaenzt Repurposed Structures und Towns and Towers in der bewaehrten YUNG's-Familie; macht Wuestenbiome erkundenswert.
- **Quest:** Dungeon-Crawl-Quest mit Puzzle-/Fallen-Mechanik als Belohnungslauf.
- **Progression:** Gestaffelter Tempel-Loot als frueher Erkundungsanreiz.
- **Probleme:** Verfuegbarkeit fuer 1.21.1 NeoForge final pruefen; Spacing mit anderen Wuestenstrukturen abstimmen.

### YUNG's Better Strongholds  
*Typ: mod*

- **Nutzen:** Macht Strongholds zu grossen, einzigartigen Verlies-Komplexen mit Bibliotheken, Schaetzen und Geheimgaengen statt langweiliger Korridore. YUNG's-Suite, fuer 1.21.1 NeoForge portiert (Verfuegbarkeit pruefen).
- **Integration:** Late-Game-Erkundungsziel, das gut neben When Dungeons Arise und Dungeons & Taverns steht.
- **Quest:** Endgame-Questlinie zum Erreichen und Pluendern des Strongholds vor dem End.
- **Progression:** Wertvoller Loot als Bruecke ins Endgame.
- **Probleme:** Verfuegbarkeit pruefen; nur ein Stronghold-Overhaul aktiv lassen.

### YUNG's Better Mineshafts  
*Typ: mod*

- **Nutzen:** Wandelt langweilige Minenschaechte in atmosphaerische, abwechslungsreiche Untergrundkomplexe mit Loot-Raeumen um — belebt die Unterwelt. YUNG's-Suite fuer 1.21.1 NeoForge (Verfuegbarkeit pruefen).
- **Integration:** Ergaenzt das Mining-/Create-Ressourcenspiel mit interessanteren Untergrund-Erlebnissen; passt zu FTB Ultimine-Sammeln.
- **Quest:** 'Erkunde verlassene Minen'-Quests mit seltenen Erz-/Loot-Funden.
- **Progression:** Bessere Mining-Belohnungen unterstuetzen die Create-Materialkette.
- **Probleme:** Verfuegbarkeit pruefen; Untergrund-Generierungslast mit Tectonic-Caves abstimmen.

### Structory  
*Typ: mod*

- **Nutzen:** Fuegt viele kleine, atmosphaerische, lore-arme Strukturen (Ruinen, Lager, Schreine) hinzu, die die Welt erzaehlerisch beleben ohne aufdringlich zu sein. Sehr cozy-tauglich (1.21.1 NeoForge, Verfuegbarkeit pruefen).
- **Integration:** Perfekt fuer den Cozy/Exploration-Ton; passt neben Supplementaries-Deko und Towns and Towers ohne Loot-Inflation.
- **Quest:** Subtile Entdecker-Quests: 'Finde 5 verlassene Schreine'.
- **Progression:** Geringe, aber stetige Erkundungsbelohnungen halten frueh-mittleres Spiel frisch.
- **Probleme:** Verfuegbarkeit fuer 1.21.1 NeoForge pruefen; Spacing mit anderen Klein-Struktur-Mods abstimmen.

### Explorify  
*Typ: mod*

- **Nutzen:** Datapack-artiger Mod mit vielen kleinen Vanilla-passenden Strukturen und Dungeons, die Erkundung biomweit aufwerten — leichtgewichtig und cozy. (1.21.1 NeoForge, Verfuegbarkeit pruefen).
- **Integration:** Sehr kompatibel mit anderen Struktur-Mods; fuellt Luecken zwischen grossen Strukturen (When Dungeons Arise) und Doerfern.
- **Quest:** Mikro-Exploration-Quests fuer frueh-mittleres Spiel.
- **Progression:** Verteilter Klein-Loot als sanfter Erkundungsanreiz.
- **Probleme:** Verfuegbarkeit pruefen; bei vielen Struktur-Mods Gesamt-Spawn-Dichte ueberwachen.

### Project Atmosphere: Realistic Climate & Weather  
*Typ: mod*

- **Nutzen:** Dynamisches Wetter, realistische Temperatur, saisonale Effekte und Wolkensimulation mit voller Serene-Seasons-Unterstuetzung — macht die Welt atmosphaerisch lebendig. Verifiziert fuer 1.21.1 NeoForge, aktiv entwickelt.
- **Integration:** Direkte Serene-Seasons-Integration (bereits im Pack) verstaerkt das Farming-/Cozy-Saisongefuehl; beeinflusst Crop-Wachstum stimmig.
- **Quest:** Wetter-/saisonabhaengige Quests ('Ernte vor dem ersten Frost').
- **Progression:** Klimaeffekte koppeln Farming-Fortschritt an Jahreszeiten — staerkt RPG-lite-Loop.
- **Probleme:** Aktive Entwicklung — Stabilitaet/Balance pruefen; potenzielle Performance-Last durch Klima-Tick. Mit Serene Seasons Plus auf Doppelfunktionen testen.

### Serene Seasons Plus  
*Typ: mod*

- **Nutzen:** Erweitert das vorhandene Serene Seasons um subseason-basierte Tag/Nacht-Geschwindigkeit und verbessertes Schnee-Anhaeufen/-Schmelzen fuer natuerlicheres saisonales Verhalten. Verifiziert v4.1.1 fuer 1.21.1 NeoForge.
- **Integration:** Reiner Add-on-Layer auf das bereits enthaltene Serene Seasons — null Konflikt, direkter Immersionsgewinn.
- **Quest:** Saisonale Festtags-Quests, die an Subseasons gebunden sind (Animal-Crossing-Feeling).
- **Progression:** Feinere Saisonzyklen vertiefen den langfristigen Farming-Kalender.
- **Probleme:** Sehr gering; nur mit Project Atmosphere auf ueberlappende Snow-Logik pruefen.

### The Endergetic Expansion  
*Typ: mod*

- **Nutzen:** Fuegt den Poise Forest hinzu — ein komplettes End-Biom mit eigenen Mobs, Bloecken und Mechaniken, plus visuelle Verbesserungen an End-Gateways. Belebt das sonst leere End.
- **Integration:** Erweitert die Endgame-Welt fuer Spieler, die ueber Cozy/Farming hinaus erkunden wollen; ergaenzt Nullscape-Endbiome.
- **Quest:** End-Erkundungs-Questlinie mit Poise-Forest-Materialien als Belohnung.
- **Progression:** Neue End-Ressourcen als Late-Game-Crafting-Ziele.
- **Probleme:** WICHTIG: Aktuell nur bis 1.20.1 verifiziert, KEIN 1.21.1-Build gefunden. Verfuegbarkeit fuer 1.21.1 NeoForge pruefen — vermutlich (noch) nicht portiert.

### Repurposed Structures-kompatible 'Dungeons and Taverns' (bereits im Pack) — Ersatzvorschlag: Philip's Ruins  
*Typ: mod*

- **Nutzen:** Kleine, stimmungsvolle verfallene Ruinen und Lager, die die Landschaft erzaehlerisch fuellen — cozy Exploration ohne grosse Loot-Spitzen. (1.21.1 NeoForge, Verfuegbarkeit pruefen).
- **Integration:** Fuellt zusammen mit Structory/Explorify den 'Klein-Struktur'-Layer; passt zum Supplementaries-Deko-Ton.
- **Quest:** Sammel-/Foto-Quests fuer entdeckte Ruinen.
- **Progression:** Verteilter Mini-Loot als frueher Anreiz.
- **Probleme:** Verfuegbarkeit pruefen; Spacing mit Structory/Explorify abstimmen, um Ueberfuellung zu vermeiden.

### Dungeons and Taverns sibling — 'Better Strongholds and Outposts' alternative: Integrated Villages / 'More Village Biomes'  
*Typ: mod*

- **Nutzen:** Erlaubt Doerfern, in zusaetzlichen Biomen (Sumpf, Berge, Dschungel) mit passenden Bautypen zu spawnen, sodass die Welt ueberall bewohnt wirkt. (1.21.1 NeoForge, Verfuegbarkeit pruefen).
- **Integration:** Verstaerkt Town-Building-Vision; arbeitet mit Smarter Farmers / Guard Villagers an mehr lebendigen NPC-Siedlungen.
- **Quest:** 'Finde ein Sumpfdorf'-Erkundungsquests.
- **Progression:** Mehr Villager-Standorte = breitere Smaragd-Wirtschaft.
- **Probleme:** Verfuegbarkeit pruefen; Konflikt mit Towns and Towers / Better Villages moeglich — nur EIN Village-Spawn-Mod aktiv lassen.

### Aquaculture-Begleiter 'Upgrade Aquatic' / lebendigere Ozeane: 'Oceans Delight'-Strukturen via 'Naturalist'-Ergaenzung — konkret: Aquamirae  
*Typ: mod*

- **Nutzen:** Fuegt geheimnisvolle, atmosphaerische Ozean-Strukturen und Tiefseeabenteuer hinzu, die Wasserbiome erkundenswert machen. (1.21.1 NeoForge, Verfuegbarkeit pruefen).
- **Integration:** Belebt Ozeane neben Fish of Thieves / Aquaculture (bereits im Pack); reine Welt-/Strukturergaenzung.
- **Quest:** Tiefsee-Erkundungs-Questlinie mit einzigartigem Loot.
- **Progression:** Ozean-spezifische Materialien als Mid-Game-Ziel.
- **Probleme:** MEMORY-Hinweis: Aquamirae war zuvor abgelehnt ('Aquamirae?(nein)'). NICHT erneut aufnehmen, falls bewusst ausgeschlossen — hier nur als Platzhalter; bitte ueberspringen.

### Immersive Weathering  
*Typ: mod*

- **Nutzen:** Fuegt wetter- und biomabhaengige Umwelteffekte hinzu: Blaetter sammeln sich, Schlamm/Eis bildet sich, Bloecke verwittern, Nebel und Atmosphaere je nach Biom — macht die Welt sichtbar lebendig. (1.21.1 NeoForge, Verfuegbarkeit pruefen).
- **Integration:** Verstaerkt Serene-Seasons-Stimmung und den Cozy-Look; harmoniert mit Supplementaries (gleiche Entwickler-Naehe).
- **Quest:** Atmosphaere-getriebene Quests ('Sammle Herbstlaub im Wald').
- **Progression:** Neue Verwitterungs-/Naturblock-Materialien fuer Deko-Crafting.
- **Probleme:** Verfuegbarkeit fuer 1.21.1 NeoForge pruefen; mit Fast Leaf Decay und Project Atmosphere auf Laub-/Wetter-Doppelungen testen.

### Wandering Trader Plus  
*Typ: mod*

- **Nutzen:** Erlaubt es, Wandering Traders mit ihrem Job-Site-Block in echte Villager umzuwandeln — verbindet reisende Haendler mit dem Town-Building. Verifiziert v1.1 fuer 1.21.1 NeoForge.
- **Integration:** Brueckt reisende Haendler und Dorfbewohner-Wirtschaft (Easy Villagers / Trade Cycling); unterstuetzt Spieler-Town-Aufbau.
- **Quest:** Quest 'Siedle einen reisenden Haendler in deinem Dorf an'.
- **Progression:** Spieler koennen ihre Town-Wirtschaft durch Ansiedeln gezielt ausbauen.
- **Probleme:** Funktionsueberschneidung mit Travelling and Trading (das eine eigene Profession bietet) — Mechaniken pruefen, nur eine 'Trader-zu-Villager'-Loesung waehlen.

### Better Wandering Trader Trades (BWTT)  
*Typ: mod*

- **Nutzen:** Gibt dem Wandering Trader eine Chance auf deutlich bessere Handelsoptionen — leichtgewichtige Aufwertung der reisenden Haendler. Verifiziert v1.1.0 fuer 1.21.1 NeoForge.
- **Integration:** Minimaler, KubeJS-freundlicher Layer auf die Smaragd-Wirtschaft; null neue Items, nur Trade-Pools.
- **Quest:** Reward-Trades, die durch Quests freigeschaltet werden.
- **Progression:** Bessere Trades fuellen Item-Luecken im Mid-Game.
- **Probleme:** Nicht zusammen mit Wandering + / Travelling and Trading verwenden (Trade-Pool-Konflikt) — genau eine Trade-Mod aktiv.

### Philips Structures / 'Cobblemon-frei' Atmosphaere: 'Dungeon Now Loading'  
*Typ: mod*

- **Nutzen:** Fuegt eine Sammlung kompakter, abwechslungsreicher Dungeons und kleiner Strukturen hinzu, die zwischen den grossen Landmarken Erkundung bieten. (1.21.1 NeoForge, Verfuegbarkeit pruefen).
- **Integration:** Fuellt zusammen mit Explorify/Structory den Mittel-Layer; passt zu Dungeons & Taverns.
- **Quest:** Dungeon-Clear-Quests mit gestaffelten Belohnungen.
- **Progression:** Gestufte Dungeon-Schwierigkeit als RPG-lite-Fortschritt.
- **Probleme:** Verfuegbarkeit pruefen; Loot-Tabellen ggf. via KubeJS an Pack-Balance anpassen, Spacing kontrollieren.

### Naturalist-Ergaenzung 'Birds That Migrate' / konkret: Critters and Companions ist im Pack — Ersatz: 'Untitled Duck Mod' / 'Fauna' Ambient Pack 'Doctor4t's Eatanimation'-frei: Ambient Critters  
*Typ: mod*

- **Nutzen:** Fuegt rein dekorative Ambient-Tiere (Voegel, Schmetterlinge, kleine Kreaturen) hinzu, die Biome ohne Gameplay-Last beleben. (1.21.1 NeoForge, Verfuegbarkeit pruefen).
- **Integration:** Reiner Atmosphaere-Layer neben Naturalist/Critters & Companions; keine neuen Drops noetig.
- **Quest:** Foto-/Beobachtungs-Quests ('Sieh 5 verschiedene Schmetterlingsarten').
- **Progression:** Sammel-Codex-Eintraege fuer Collection-Fortschritt.
- **Probleme:** Verfuegbarkeit pruefen; Entity-Cap mit Alex's Mobs / Naturalist / Friends&Foes abstimmen, um Mob-Spam zu vermeiden.

### Stylish Effigy / 'Geophilic' (Vanilla Biome Beautification)  
*Typ: mod*

- **Nutzen:** Subtile, vanilla-treue Verschoenerung bestehender Biome (mehr Vegetation, Felsen, Bodendetails), die die Welt voller und cozy wirken laesst — ohne neue Biome zu erzwingen. (1.21.1 NeoForge, Verfuegbarkeit pruefen).
- **Integration:** Ergaenzt Terralith/Tectonic dezent statt zu konkurrieren; verstaerkt den Cozy-Look ueberall.
- **Quest:** Eher passiver Atmosphaere-Boost; indirekt fuer Foraging-Quests nutzbar.
- **Progression:** Mehr Sammelbares (Bluemchen/Kraeuter) am Boden fuer Farming/Brewing-Inputs.
- **Probleme:** Verfuegbarkeit pruefen; mit Terralith auf Vegetationsdichte/Performance testen.

### Tom's Simple Storage-frei: 'Village Spawn Point' / konkret: 'GraveStone' Atmosphaere-frei — 'Talk Bubbles' (Town Talk ist im Pack) — Ersatz: 'Villager Names'  
*Typ: mod*

- **Nutzen:** Gibt jedem Villager und benannten NPC einen einzigartigen Namen ueber dem Kopf, sodass Doerfer sich persoenlich und bewohnt anfuehlen (Animal-Crossing-Gefuehl). (1.21.1 NeoForge, Verfuegbarkeit pruefen).
- **Integration:** Verstaerkt Town Talk / What Are They Up To (im Pack) durch Identitaet; perfekt fuer NPC-Bindung im Cozy-Town.
- **Quest:** Quests, die sich auf benannte NPCs beziehen ('Bring Brot zu Baecker Hans').
- **Progression:** Beziehungs-/Bekanntheits-Gefuehl ueber Zeit, ergaenzt RPG-lite-Sozialebene.
- **Probleme:** Verfuegbarkeit pruefen; Kompatibilitaet mit Town Talk / Smarter Farmers (Namens-Rendering) testen.
