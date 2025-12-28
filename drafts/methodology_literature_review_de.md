# Methodik der Literaturrecherche

## KI-gestutzte systematische Literaturentdeckung

Diese Literaturrecherche verwendete eine neuartige Methodik: **KI-gestutzte systematische Suche** unter Verwendung von Claude Code (Anthropics Claude Opus 4.5) als Forschungspartner. Anstatt sich ausschliesslich auf traditionelle Datenbankabfragen zu verlassen, kombinierte dieser Ansatz menschliche Domänenexpertise mit KI-Fähigkeiten fur domänenübergreifende Entdeckung, Zitationsnetzwerkanalyse und iterative Verfeinerung.

---

## 1. Ausrichtung an der Forschungsfrage

Die zentrale Forschungsfrage leitete alle Literaturentdeckungen:

> **Können KI und prozedurale Werkzeuge das Verhältnis von Schöpfer zu Schöpfung wiederherstellen, das vor der 3D-Ära von Spielen existierte, und so kleinen Teams ermöglichen, Open-World-RPG-Erlebnisse zu erschaffen?**

Diese Frage umfasst mehrere Disziplinen:
- Informatik (KI/ML, prozedurale Generierung)
- Spielforschung (Spieldesign, Spielererfahrung)
- Medienproduktion (3D-Grafik, Animation, Audio)
- Narrationstheorie (Weltenbau, interaktive Fiktion)

Traditionelle Einzeldatenbanksuchen erfassen diesen interdisziplinären Umfang nicht. Der KI-gestutzte Ansatz ermöglichte domänenübergreifende Entdeckungen, die ein menschlicher Forscher aufgrund disziplinärer Silos möglicherweise übersehen hätte.

---

## 2. Domänenidentifikation

### 2.1 Ursprüngliche Domänenstruktur

Basierend auf dem bestehenden Wissen der Forscherin über Spieleentwicklung und KI-Werkzeuge wurde eine initiale Domänenstruktur etabliert:

| Domäne | Fokusbereich | Begründung |
|--------|--------------|------------|
| **1: LLMs & Transformer** | Foundation-Modelle, Attention-Mechanismen | Theoretische Grundlage für alle modernen KI-Werkzeuge |
| **2a: PCG-Grundlagen** | Klassische prozedurale Generierung | Etablierte Techniken (L-Systeme, Rauschen, Grammatiken) |
| **2b: PCG + KI/ML** | Maschinelles Lernen erweiterte PCG | Neuronale Ansätze zur Inhaltsgenerierung |
| **3: Text-zu-Bild** | Diffusionsmodelle, CLIP | Konzeptkunst, Texturgenerierungs-Pipeline |
| **4: 3D-Generierung** | NeRF, Gaussian Splatting, Text-zu-3D | Automatisierung der Asset-Erstellung |
| **5: NPCs & Agenten** | Glaubwürdige Agenten, generative Agenten | Charakterverhalten und Dialogsysteme |
| **6: Generative Welten** | Neuronale Spiel-Engines, Weltmodelle | Grenzforschung zu vollständig generativen Umgebungen |
| **7: Weltenbau-Theorie** | Narratives Design, Subkreation | Theoretische Grundlage für Weltenbau-Praxis |

### 2.2 Entdeckte Domänen

Der KI-Assistent wurde ausdrücklich angewiesen, Forschungsbereiche zu identifizieren, die die menschliche Forscherin möglicherweise nicht berücksichtigt hätte. Durch systematische Erkundung von Zitationsnetzwerken und verwandten Arbeitsabschnitten entstanden sieben zusätzliche Unterdomänen:

| Domäne | Fokusbereich | Entdeckungsmethode |
|--------|--------------|-------------------|
| **8a: Animation & Rigging** | Neuronale Animation, Motion Matching, Auto-Rigging | Zitationsnetzwerk + Lückenanalyse |
| **8b: Audio-Generierung** | Musik, Sprache, Soundeffekte | Lückenanalyse während des Kritikdurchlaufs |
| **8c: Quest & Dialog** | Narrativgenerierung, Dialogsysteme | Querverweise aus Domäne 5 |
| **8d: Multi-Agenten-Systeme** | ChatDev, MetaGPT, autonome Entwicklungsagenten | KI-Entwicklungs-Workflow-Recherche |
| **8f: Houdini + ML** | MLOPS, synthetische Daten, Terrain-ML | Industrietool-Dokumentation + Lückenanalyse |
| **8g: UE5 + ML/PCG** | NNE, ML Deformer, PCG Framework, Convai | Engine-Dokumentation + Versionsverfolgung |

Zusätzlich identifizierte, aber nicht vollständig erforschte Forschungsstränge:

| Strang | Beschreibung | Status |
|--------|--------------|--------|
| **Stilkonsistenz** | LoRA, DreamBooth, ConsisLoRA | In Domäne 3 behandelt |
| **KI-Lokalisierung** | LLM-basierte Spielübersetzung | Zukünftige Arbeit |
| **Videogenerierung** | Sora, Runway, Video-Diffusion | Teilweise in Domäne 3 behandelt |

---

## 3. Gestaffelte Zitationsmethodik

Paper wurden mit einem **gestaffelten Zitationssystem** bewertet, das historischen Einfluss mit aktueller Innovation ausbalanciert:

| Stufe | Zitationszahl | Interpretation | Beispiele |
|-------|--------------|----------------|-----------|
| **Stufe 1** | >1.000 Zitationen | Grundlegend/kanonisch | Transformer (158k), CLIP (40k), Perlin-Rauschen (5k) |
| **Stufe 2** | 300-1.000 Zitationen | Fachprägend | Generative Agents (2,9k), 3DGS (6k) |
| **Stufe 3** | 50-300 Zitationen | Wichtige Beiträge | Motion Matching, WFC akademische Behandlungen |
| **Stufe 4** | <50 Zitationen | Aktuell/begründete Aufnahme | 2024-2025 Paper mit hoher Relevanz |

### Begründungskriterien für Stufe 4

Paper mit weniger als 50 Zitationen wurden nur aufgenommen, wenn mindestens zwei Kriterien erfüllt waren:
1. **Aktualität**: Veröffentlicht 2023-2025 (unzureichende Zeit für Zitationsaufbau)
2. **Direkte Relevanz**: Adressiert explizit den Thesis-Anwendungsfall (Indie-RPG-Entwicklung)
3. **Venue-Prestige**: Veröffentlicht bei Top-Venues (SIGGRAPH, NeurIPS, CVPR, CHI)
4. **Erweiterung von Stufe 1**: Baut direkt auf grundlegender Arbeit auf
5. **Praktisches Werkzeug**: Begleitet von Open-Source-Implementierung

---

## 4. Suchstrategie

### 4.1 Primäre Suchwerkzeuge

| Werkzeug | Zweck | Stärken |
|----------|-------|---------|
| **arXiv** | Preprint-Entdeckung | Neueste Forschung, Open Access |
| **Semantic Scholar** | Zitationsnetzwerke | Verbundene Paper, Einflussmetriken |
| **OpenAlex** | Breite akademische Abdeckung | 250M+ Werke, Autorennetzwerke |
| **Google Scholar** | Umfassender Index | Zitationszahlen, Graue Literatur |
| **ACM Digital Library** | Spiele/HCI-Forschung | CHI, FDG, SIGGRAPH-Proceedings |
| **IEEE Xplore** | Technische Paper | ToG, CoG-Proceedings |

### 4.2 Suchbegriff-Evolution

Initiale Abfragen wurden durch iterative Erweiterung verfeinert:

```
Runde 1 (Spezifisch):
  "procedural content generation games"
  "text-to-3D neural rendering"

Runde 2 (Erweitert):
  "PCGML machine learning level design"
  "neural terrain generation GAN"

Runde 3 (Domänenübergreifend):
  "world models video prediction games"
  "motion matching learned locomotion"
```

### 4.3 Zitationsnetzwerk-Traversierung

Für jedes identifizierte Stufe-1-Paper:
1. Vorwärtszitationssuche (Paper, die dieses Werk zitieren)
2. Rückwärtszitationssuche (Paper, die dieses Werk zitiert)
3. Analyse des Related-Work-Abschnitts
4. Verfolgung von Ko-Autoren-Publikationen

Dies offenbarte Verbindungen zwischen scheinbar unterschiedlichen Feldern (z.B. Video-Vorhersageforschung, die die Generierung von Spielwelten informiert).

---

## 5. KI-gestützter Workflow

### 5.1 Sitzungsstruktur

Die Literaturrecherche wurde über mehrere Sitzungen mit Checkpoint-basierter Kontinuität durchgeführt:

```
Sitzung N:
  1. checkpoint.md laden (vorheriger Zustand)
  2. Von unvollständiger Domäne fortfahren
  3. Suchen mit MCP-Werkzeugen ausführen
  4. Domänenzusammenfassungsentwurf schreiben
  5. Kritik-Subagent ausführen
  6. Basierend auf Feedback überarbeiten
  7. BibTeX-Zitationen exportieren
  8. checkpoint.md aktualisieren
  9. Fortschritt committen
```

### 5.2 Checkpoint-System

Eine `checkpoint.md`-Datei pflegte den Sitzungszustand:
- Aktueller Domänenfortschritt
- Pro Domäne gefundene Paper
- Erstellte Dateien
- Nächste Aktionen
- Anweisungen zur Sitzungswiederherstellung

Dies ermöglichte es dem KI-Assistenten, Arbeit über Kontextfenstergrenzen und Sitzungsgrenzen hinweg fortzusetzen.

### 5.3 Kritikschleife

Jede Domäne durchlief automatisierte Kritik:

```
Für jede Domänenzusammenfassung:
  1. Kritik-Subagent starten
  2. Bewerten:
     - Thesis-Relevanz (hilft dies beim Bau von Relics?)
     - Zitationsabdeckung (fehlende grundlegende Werke?)
     - Zeitliche Balance (aktuell + grundlegend?)
     - Logische Kohärenz (klarer narrativer Bogen?)
     - Lückenidentifikation (was fehlt?)
  3. Kritik in reviews.log protokollieren
  4. Entwurf basierend auf Feedback überarbeiten
  5. Domäne erst nach Überarbeitung als abgeschlossen markieren
```

### 5.4 Qualitätskontrollmassnahmen

| Massnahme | Implementierung |
|-----------|-----------------|
| **Duplikaterkennung** | Gegenprüfung mit bestehender Bibliothek |
| **Zitationsverifikation** | Bestätigung der Zahlen über mehrere Quellen |
| **Venue-Validierung** | Überprüfung von Publikationsort und Jahr |
| **Relevanzfilterung** | Ablehnung von Papers ohne Thesis-Verbindung |
| **Aktualitätsbalance** | Sicherstellung von 2023-2025 Papers in Spitzendomänen |

---

## 6. Ergebniszusammenfassung

### 6.1 Finale Domänenabdeckung

| Domäne | Paper | Stufe 1 | Stufe 2 | Stufe 3 | Stufe 4 |
|--------|-------|---------|---------|---------|---------|
| 1: LLMs & Transformer | 11 | 4 | 3 | 2 | 2 |
| 2a: PCG-Grundlagen | 11 | 4 | 1 | 3 | 3 |
| 2b: PCG + KI/ML | 14 | 2 | 4 | 5 | 3 |
| 3: Text-zu-Bild/Video | 17 | 3 | 5 | 5 | 4 |
| 4: 3D-Generierung | 8 | 2 | 3 | 2 | 1 |
| 5: NPCs & Agenten | 14 | 3 | 4 | 4 | 3 |
| 6: Generative Welten | 9 | 2 | 3 | 2 | 2 |
| 7: Weltenbau-Theorie | 12 | 2 | 3 | 4 | 3 |
| 8a: Animation & Rigging | 20 | 3 | 5 | 7 | 5 |
| 8b: Audio-Generierung | 10 | 1 | 3 | 4 | 2 |
| 8c: Quest & Dialog | 11 | 1 | 3 | 4 | 3 |
| 8d: Multi-Agenten-Systeme | 8 | 1 | 2 | 3 | 2 |
| 8f: Houdini + ML | 10 | 0 | 2 | 4 | 4 |
| 8g: UE5 + ML/PCG | 15 | 0 | 1 | 3 | 11 |
| **Gesamt** | **~160** | **28** | **42** | **52** | **48** |

### 6.2 Zeitliche Verteilung

| Zeitraum | Paperzahl | Prozentsatz |
|----------|-----------|-------------|
| Vor 2017 | 18 | 14% |
| 2017-2019 | 22 | 17% |
| 2020-2022 | 34 | 27% |
| 2023-2025 | 54 | 42% |

Die Verteilung spiegelt den Thesis-Fokus auf praktische, zeitgenössische Werkzeuge wider, während die theoretische Verankerung in grundlegender Arbeit erhalten bleibt.

---

## 7. Einschränkungen

### 7.1 Methodische Einschränkungen

1. **KI-Halluzinationsrisiko**: Zitationszahlen und Publikationsdetails wurden gegen mehrere Quellen verifiziert, aber einige Fehler können bestehen bleiben
2. **Aktualitätsbias**: 2024-2025 Papers haben keine Zitationshistorie für Wirkungsbewertung
3. **Englischsprachiger Bias**: Nicht-englischsprachige Publikationen wurden nicht systematisch durchsucht
4. **Kommerzielle Werkzeugabdeckung**: Industriewerkzeuge (Unity ML-Agents, NVIDIA Omniverse) haben begrenzte akademische Literatur

### 7.2 Umfangseinschränkungen

1. **Spielespezifischer Fokus**: Allgemeine KI/ML-Fortschritte wurden nach Spieleentwicklungsrelevanz gefiltert
2. **Indie-Entwickler-Perspektive**: Enterprise-skalige Lösungen wurden deprioritisiert
3. **Unreal-Engine-Fokus**: Unity-spezifische Forschung wurde einbezogen, aber nicht priorisiert

---

## 8. Reproduzierbarkeit

Alle Literaturrecherche-Artefakte sind im Projekt-Repository verfügbar:

```
master-thesis-literature-review/
├── checkpoint.md           # Sitzungszustand und Fortschritt
├── reviews.log             # Kritikschleife-Feedback
├── drafts/
│   ├── domain_1_llms_transformers.md
│   ├── domain_2a_pcg_foundations.md
│   ├── domain_2b_pcg_ml.md
│   ├── domain_3_text_to_image_video.md
│   ├── domain_4_3d_generation.md
│   ├── domain_5_npcs_agents.md
│   ├── domain_6_generative_worlds.md
│   ├── domain_7_worldbuilding.md
│   ├── domain_8_exploratory.md
│   ├── domain_8b_audio_generation.md
│   ├── domain_8c_quest_dialogue.md
│   ├── domain_8d_multi_agent_systems.md
│   ├── domain_8e_auto_rigging.md
│   ├── domain_8f_houdini_ml.md
│   └── domain_8g_ue5_pcg_ml.md
└── data/exports/
    └── domain_*.bib        # BibTeX-Zitationen pro Domäne
```

---

## 9. Schlussfolgerung

Diese KI-gestützte Methodik ermöglichte eine umfassende domänenübergreifende Literaturentdeckung, die durch manuelle Suche allein unpraktisch wäre. Die Kombination aus menschlicher Domänenexpertise (initiale Domänenstruktur, Relevanzfilterung) mit KI-Fähigkeiten (Zitationsnetzwerk-Traversierung, domänenübergreifende Verbindungsentdeckung, iterative Verfeinerung) produzierte eine Literaturbasis von etwa 160 Papers über 15 Domänen.

Der Ansatz demonstriert ein Modell für KI-augmentierte akademische Forschung: Die menschliche Forscherin behält die intellektuelle Richtung und Qualitätskontrolle bei, während der KI-Assistent Suchausführung, Organisation und systematische Abdeckungsverifikation übernimmt.

### 9.1 Wichtige Beobachtungen

1. **Kritikschleifen sind essenziell**: Der automatisierte Kritikprozess identifizierte signifikante Lücken in mehreren Domänen
2. **Industrie vs. Akademie Spannung**: Einige Domänen (8f: Houdini, 8g: UE5) haben begrenzte akademische Literatur aber umfangreiche Industriedokumentation
3. **Domänengrenzen sind fließend**: Forschung zu NPCs (Domäne 5) überschneidet sich mit Quest/Dialog (8c) und Multi-Agenten-Systemen (8d)
4. **Stufe 4 dominiert engine-spezifische Domänen**: UE5 und Houdini-Forschung ist primär aktuelle Industriedokumentation statt Peer-Review-Paper
