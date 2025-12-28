# Der Neue Aufbruch der KI: Von Mathematischer Theorie zu Kreativen Werkzeugen

## Eine Umfassende Einführung für Medienfachleute

Dieses Dokument erklärt die Grundlagen moderner künstlicher Intelligenz für Leser, die Computer und digitale Medienproduktion verstehen, aber möglicherweise keinen Hintergrund in maschinellem Lernen haben. Es zeichnet den Weg von theoretischer Mathematik zu den KI-Werkzeugen nach, die heute kreative Industrien transformieren.

---

## Teil 1: Was KI Eigentlich Bedeutet (Und Was Nicht)

### 1.1 Der Begriff "Künstliche Intelligenz"

Der Begriff "künstliche Intelligenz" wurde 1956 auf einem Workshop am Dartmouth College geprägt. Die ursprüngliche Vision war ambitioniert: Maschinen erschaffen, die wie Menschen denken, lernen und Probleme lösen können. Diese Vision bleibt weitgehend unrealisiert.

Was wir heute "KI" nennen, wird genauer als **maschinelles Lernen** beschrieben - Systeme, die Muster in Daten finden und auf deren Grundlage Vorhersagen treffen. Diese Systeme "verstehen" nichts im menschlichen Sinne. Sie sind hochentwickelte Mustererkennungsmaschinen.

### 1.2 Die Zwei Ären der KI

**Klassische KI (1956-2010): Regelbasierte Systeme**

Frühe KI stützte sich auf von Menschen geschriebene Regeln:
- "WENN Spielergesundheit < 20 DANN fliehen"
- "WENN Feind sichtbar UND Waffe ausgerüstet DANN angreifen"

Dieser Ansatz funktionierte für enge Domänen, versagte aber bei allem, was Nuancen erforderte. Eine Schach-KI konnte Grossmeister durch die Auswertung von Millionen von Positionen schlagen, konnte aber keine Katze auf einem Foto erkennen.

**Moderne KI (2012-heute): Lernen aus Daten**

Der Durchbruch war, Maschinen ihre eigenen Regeln durch Analyse massiver Datensätze entdecken zu lassen. Anstatt zu programmieren, "wie eine Katze aussieht", zeigt man dem System Millionen von Katzenfotos und lässt es die Muster selbst herausfinden.

Diese Verschiebung - von menschengeschriebenen Regeln zu gelernten Mustern - ist die Grundlage für alles, was folgte.

---

## Teil 2: Die Mathematische Grundlage

### 2.1 Neuronale Netze: Von der Biologie Inspiriert, auf Mathematik Gebaut

Ein neuronales Netz ist eine in Schichten organisierte mathematische Funktion. Trotz des Namens hat es wenig mit echten Gehirnen zu tun.

**Die Grundeinheit: Ein Neuron**

Jedes künstliche Neuron führt einfache Mathematik durch:
1. Nimmt mehrere Eingabezahlen
2. Multipliziert jede Eingabe mit einem "Gewicht" (Wichtigkeit)
3. Addiert sie zusammen
4. Leitet durch eine "Aktivierungsfunktion" (typischerweise mit Nichtlinearität)
5. Gibt eine einzelne Zahl aus

```
Eingabe 1 (0,5) × Gewicht 1 (0,3) = 0,15
Eingabe 2 (0,8) × Gewicht 2 (0,7) = 0,56
                          Summe  = 0,71
                   Aktivierung → Ausgabe: 0,67
```

**Schichten von Neuronen**

Neuronen sind in Schichten organisiert:
- **Eingabeschicht**: Empfängt Rohdaten (Pixel, Wörter, Audiosamples)
- **Versteckte Schichten**: Transformieren Daten durch sukzessive Abstraktionen
- **Ausgabeschicht**: Produziert finale Vorhersage

Ein Netz mit vielen versteckten Schichten wird "tiefes" neuronales Netz genannt - daher "Deep Learning".

### 2.2 Lernen: Die Gewichte Anpassen

Das "Lernen" im maschinellen Lernen ist der Prozess, gute Gewichtswerte zu finden. Dies geschieht durch:

1. **Vorwärtsdurchlauf**: Daten fliessen durch das Netz, produzieren eine Vorhersage
2. **Verlustberechnung**: Vergleich der Vorhersage mit der korrekten Antwort
3. **Rückwärtsdurchlauf**: Berechnung, wie jedes Gewicht zum Fehler beigetragen hat
4. **Gewichtsaktualisierung**: Anpassung der Gewichte zur Fehlerreduzierung
5. **Wiederholung**: Verarbeitung von Millionen von Beispielen

Dieser Algorithmus, genannt **Backpropagation**, wurde in den 1980ern entwickelt, erforderte aber moderne Rechenleistung, um im grossen Massstab zu funktionieren.

### 2.3 Warum "Tief" Wichtig Ist

Jede Schicht lernt zunehmend abstrakte Merkmale:

```
Bilderkennungsbeispiel:
Schicht 1: Kanten, Gradienten
Schicht 2: Texturen, Ecken
Schicht 3: Teile (Augen, Ohren, Räder)
Schicht 4: Objekte (Katzen, Autos, Gesichter)
Schicht 5: Szenen (Wohnzimmer mit Katze auf Couch)
```

Dieses hierarchische Merkmalslernen ist der Grund, warum tiefe Netze komplexe Aufgaben bewältigen können, an denen klassische KI scheiterte.

---

## Teil 3: Die Deep-Learning-Revolution (2012-2017)

### 3.1 ImageNet und der GPU-Durchbruch

2012 gewann ein neuronales Netz namens **AlexNet** den ImageNet-Bildklassifizierungswettbewerb mit grossem Vorsprung. Zwei Faktoren ermöglichten dies:

1. **GPUs**: Grafikkarten, die für Spiele entwickelt wurden, erwiesen sich als perfekt für Neuronale-Netz-Mathematik (viele parallele Multiplikationen)
2. **Datenmenge**: Das Internet lieferte Millionen von beschrifteten Trainingsbildern

Dieser Moment markierte den Beginn der Dominanz des Deep Learning.

### 3.2 Convolutional Neural Networks (CNNs)

CNNs verarbeiten Bilder, indem sie kleine "Filter" über das Bild schieben und lokale Muster erkennen. Diese Architektur:
- Respektiert die räumliche Struktur von Bildern
- Verwendet weit weniger Parameter als vollständig verbundene Netze
- Ermöglicht effizientes Training auf GPUs

CNNs wurden zum Standard für Computer-Vision-Aufgaben: Objekterkennung, Segmentierung, Stiltransfer.

### 3.3 Recurrent Neural Networks (RNNs)

Für sequenzielle Daten (Text, Audio, Video) verarbeiten RNNs ein Element nach dem anderen, während sie ein "Gedächtnis" vorheriger Elemente aufrechterhalten. Varianten wie **LSTM** (Long Short-Term Memory) konnten längere Sequenzen verarbeiten.

Allerdings hatten RNNs Einschränkungen:
- Langsam: müssen Sequenzen Schritt für Schritt verarbeiten
- Gedächtnis verblasst: Schwierigkeiten mit langreichweitigen Abhängigkeiten
- Schwer zu parallelisieren

Diese Einschränkungen würden durch die Transformer-Architektur adressiert werden.

---

## Teil 4: Transformer - Die Architektur, die Alles Veränderte

### 4.1 "Attention Is All You Need" (2017)

Das Paper von Vaswani et al. führte die **Transformer**-Architektur ein. Mit über 158.000 Zitationen ist es wohl das einflussreichste KI-Paper, das je veröffentlicht wurde.

Die Schlüsselinnovation: **Self-Attention**.

### 4.2 Was Attention Tut

In einem Satz wie "Die Katze sass auf der Matte, weil sie müde war" - worauf bezieht sich "sie"? Für Menschen ist das offensichtlich - "sie" bezieht sich auf "Katze". Aber woher wissen wir das?

Self-Attention erlaubt jedem Wort, alle anderen Wörter zu "betrachten" und Relevanzbewertungen zu berechnen:

```
Abfrage: "sie"
Schlüssel: [Die, Katze, sass, auf, der, Matte, weil, sie, müde, war]
Scores:    [0,1, 0,7, 0,1, 0,0, 0,0, 0,1, 0,0, 0,0, 0,0, 0,0]
                 ↑
          Höchste Attention zu "Katze"
```

Dieser Mechanismus ermöglicht es Transformern, Beziehungen unabhängig von der Distanz in der Sequenz zu modellieren.

### 4.3 Warum Transformer Gewonnen Haben

| Eigenschaft | RNNs | Transformer |
|-------------|------|-------------|
| Parallele Verarbeitung | Nein (sequenziell) | Ja (alles auf einmal) |
| Langreichweitige Abhängigkeiten | Schwach | Stark |
| Trainingsgeschwindigkeit | Langsam | Schnell |
| Skalierbarkeit | Begrenzt | Hervorragend |

Transformer konnten auf weit mehr Daten durch parallele Berechnung trainiert werden. Diese Skalierbarkeit ermöglichte die grossen Sprachmodelle, die folgten.

---

## Teil 5: Grosse Sprachmodelle - Textvorhersage im Grossen Massstab

### 5.1 Die Überraschende Kraft der Nächste-Wort-Vorhersage

GPT-Modelle (Generative Pre-trained Transformer) werden auf eine einfache Aufgabe trainiert: **das nächste Wort vorhersagen**.

```
Eingabe:  "Die Hauptstadt von Frankreich ist"
Ziel: "Paris"
```

Das scheint trivial einfach. Doch wenn auf Milliarden von Parametern skaliert und auf Billionen von Wörtern trainiert, entsteht etwas Bemerkenswertes: Das Modell entwickelt scheinbares Wissen, Argumentationsfähigkeit und sogar Kreativität.

Warum? Um das nächste Wort genau vorherzusagen, muss das Modell lernen:
- Grammatik und Syntax
- Fakten über die Welt
- Logische Beziehungen
- Stilistische Muster
- Kontext und Nuancen

### 5.2 Die Skalierungsgesetze

Forschung zeigte, dass grössere Modelle, trainiert auf mehr Daten, konsistent besser abschnitten. Dies führte zu einem Wettrüsten:

| Modell | Jahr | Parameter | Trainingsdaten |
|--------|------|-----------|----------------|
| GPT-1 | 2018 | 117M | ~5GB Text |
| GPT-2 | 2019 | 1,5B | 40GB Text |
| GPT-3 | 2020 | 175B | ~570GB Text |
| GPT-4 | 2023 | ~1,8T (gesch.) | Unbekannt |

Mit GPT-3 begannen Modelle "emergente" Fähigkeiten zu zeigen - Fähigkeiten, die plötzlich bei einer bestimmten Grösse erschienen, anstatt sich graduell zu verbessern.

### 5.3 Wie Generierung Funktioniert: Tokens und Wahrscheinlichkeit

Text wird in **Tokens** umgewandelt (ungefähr Wortteile):

```
"Unglaublich" → ["Un", "glaub", "lich"]
```

Das Modell gibt Wahrscheinlichkeitsverteilungen über mögliche nächste Tokens aus:

```
Eingabe: "Es war einmal"
Wahrscheinlichkeiten:
  "ein" → 0,45
  "vor" → 0,25
  "eine" → 0,15
  ...
```

Generierung sampelt aus dieser Verteilung und führt kontrollierte Zufälligkeit ein (Temperatur). Niedrigere Temperatur = vorhersagbarere Ausgabe; höhere Temperatur = kreativer/zufälliger.

### 5.4 Instruktionsbefolgung und RLHF

Rohe Sprachmodelle vervollständigen Text, folgen aber Anweisungen nicht gut. **RLHF** (Reinforcement Learning from Human Feedback) feintuned Modelle, um:
- Benutzeranweisungen zu folgen
- Schädliche Anfragen abzulehnen
- Hilfreiche, ehrliche Antworten zu geben

Das ist es, was eine Textvervollständigungsmaschine in ChatGPT transformiert - einen konversationellen Assistenten.

---

## Teil 6: Von Wörtern zu Bildern - Diffusionsmodelle

### 6.1 Der Durchbruch: Latent Diffusion

Wenn Transformer Text revolutionierten, revolutionierten **Diffusionsmodelle** Bilder. Das Schlüsselpaper: "High-Resolution Image Synthesis with Latent Diffusion Models" (Rombach et al., 2022) - die Grundlage von Stable Diffusion.

### 6.2 Wie Diffusion Funktioniert

Die Kernidee ist kontraintuitiv: **Rauschen entfernen** lernen.

**Training:**
1. Nimm ein echtes Bild
2. Füge schrittweise zufälliges Rauschen hinzu, bis es reines Rauschen ist
3. Trainiere ein neuronales Netz, diesen Prozess umzukehren

**Generierung:**
1. Starte mit reinem Zufallsrauschen
2. Wende das Entrauschungsnetz wiederholt an
3. Sauberes Bild entsteht aus Rauschen

```
Reines Rauschen → Etwas weniger Rauschen → ... → Sauberes Bild
   Schritt 0        Schritt 1                    Schritt 1000
```

### 6.3 Die Magie des Latenten Raums

Auf vollauflösenden Bildern zu operieren ist rechenintensiv. Latent Diffusion arbeitet in einer komprimierten Repräsentation:

```
Bild (512×512×3) → Encoder → Latent (64×64×4) → Entrauschen → Decoder → Bild
         786k Werte           16k Werte
```

Diese 50-fache Kompression macht hochauflösende Generierung praktikabel.

### 6.4 Textkonditionierung mit CLIP

Wie wird "eine Katze mit Zylinder" zu einem Bild? Durch **CLIP** (Contrastive Language-Image Pre-training).

CLIP lernt, Text und Bilder zu verbinden, indem es auf 400 Millionen Bild-Text-Paaren aus dem Internet trainiert. Es erzeugt einen gemeinsamen "Einbettungsraum", in dem ähnliche Konzepte clustern:

```
Text: "eine Katze mit Zylinder"
        ↓
   CLIP Text-Encoder
        ↓
   [0,23, -0,45, 0,67, ...] ← Einbettungsvektor
        ↓
   Leitet Diffusions-Entrauschung
        ↓
   Bild, das zur Beschreibung passt
```

---

## Teil 7: Von 2D zu 3D - Neuronale Szenenrepräsentationen

### 7.1 Die 3D-Generierungs-Herausforderung

3D-Inhalte zu generieren ist schwieriger als 2D:
- Keine massiven beschrifteten 3D-Datensätze (anders als ImageNet für Bilder)
- 3D-Repräsentationen sind komplexer (Meshes, Volumen, Punktwolken)
- Muss aus jedem Blickwinkel funktionieren

### 7.2 Neural Radiance Fields (NeRF)

NeRF (2020) repräsentierte Szenen als neuronale Netze, die Farbe und Dichte für jede 3D-Koordinate ausgeben:

```
Eingabe: (x, y, z, Blickrichtung)
Ausgabe: (R, G, B, Dichte)
```

Gegeben Fotos aus mehreren Winkeln, lernt NeRF die zugrundeliegende 3D-Szene. Dies ermöglichte fotorealistische Novel-View-Synthese, war aber langsam zu rendern.

### 7.3 3D Gaussian Splatting

3D Gaussian Splatting (2023) repräsentiert Szenen als Millionen von farbigen 3D-Ellipsoiden ("Splats"). Anders als NeRF:
- Rendert in Echtzeit (100+ FPS)
- Explizite Repräsentation (editierbar)
- Geringerer Speicherbedarf

Dies ist jetzt der dominierende Ansatz für fotorealistische 3D-Erfassung.

### 7.4 Text-zu-3D: Der Heilige Gral

Text-zu-3D-Generierung kombiniert Diffusionsmodelle mit 3D-Optimierung:

**Score Distillation Sampling (DreamFusion, 2022):**
1. Starte mit zufälliger 3D-Form
2. Rendere aus zufälligem Blickwinkel
3. Frage Diffusionsmodell: "Sieht das aus wie [Prompt]?"
4. Aktualisiere 3D-Form basierend auf Feedback
5. Wiederhole aus verschiedenen Blickwinkeln

Dies erzeugt 3D-Objekte aus Textbeschreibungen, obwohl Qualität und Geschwindigkeit aktive Forschungsbereiche bleiben.

---

## Teil 8: Von Generierung zu Handlungsfähigkeit

### 8.1 Der Sprung zur Werkzeugnutzung

Ein Sprachmodell, das Text generiert, ist beeindruckend. Aber wie wird Textvorhersage zu einem "Agenten", der Aktionen ausführt?

Die Schlüsselerkenntnis: **Aktionen können als Text repräsentiert werden**.

```
Mensch: "Wie ist das Wetter in Tokio?"

Modellantwort:
<denken>Ich muss das Wetter prüfen. Ich nutze das Wetter-Werkzeug.</denken>
<werkzeug_aufruf>get_weather(ort="Tokio")</werkzeug_aufruf>

System: [Wetter-API gibt zurück: "Tokio: 15°C, teilweise bewölkt"]

Modellantwort:
Das Wetter in Tokio ist 15°C und teilweise bewölkt.
```

Das Modell lernt:
1. Erkennen, wann Werkzeuge benötigt werden
2. Werkzeugaufrufe korrekt formatieren
3. Ergebnisse interpretieren
4. Die Konversation fortsetzen

### 8.2 Chain of Thought und Schlussfolgern

Grössere Modelle können komplexes Schlussfolgern durchführen, wenn sie aufgefordert werden, "Schritt für Schritt zu denken":

```
F: Wenn ein Zug um 15:00 Uhr mit 60 km/h losfährt und ein anderer
   um 16:00 Uhr mit 80 km/h, wann treffen sie sich?

A: Lass mich das Schritt für Schritt durcharbeiten...
   - Um 16:00 Uhr hat der erste Zug 60 km zurückgelegt
   - Sei t = Stunden nach 16:00, wenn sie sich treffen
   - Position des ersten Zuges: 60 + 60t
   - Position des zweiten Zuges: 80t
   - Sie treffen sich, wenn gleich: 60 + 60t = 80t
   - Auflösen: 60 = 20t, also t = 3 Stunden
   - Sie treffen sich um 19:00 Uhr
```

Dieses "Chain of Thought"-Schlussfolgern entsteht natürlich in grossen Modellen und kann durch Prompting hervorgerufen werden.

### 8.3 Die Agenten-Schleife

Moderne KI-Agenten folgen einer iterativen Schleife:

```
1. BEOBACHTEN: Aufgabe oder Feedback empfangen
2. DENKEN: Situation analysieren, Ansatz planen
3. HANDELN: Werkzeugaufruf ausführen oder Ausgabe generieren
4. REFLEKTIEREN: Ergebnis bewerten
5. WIEDERHOLEN: Fortfahren bis Aufgabe abgeschlossen
```

Dies ist die Architektur hinter:
- ChatGPT mit Code-Interpreter
- Claude Code (dieses System)
- GitHub Copilot
- AutoGPT und ähnliche autonome Agenten

### 8.4 Multi-Agenten-Systeme

Aktuelle Forschung erkundet mehrere KI-Agenten, die zusammenarbeiten:

**ChatDev (2024)**: Simuliert ein Softwareunternehmen mit KI-Agenten in verschiedenen Rollen (CEO, Programmierer, Tester). Die Agenten diskutieren, überprüfen gegenseitig ihre Arbeit und iterieren an Softwareprojekten.

Dies deutet darauf hin, dass zukünftige kreative Werkzeuge orchestrierte Teams spezialisierter KI-Agenten beinhalten könnten.

---

## Teil 9: Von Vorhersage zu Schöpfung

### 9.1 Der Gemeinsame Faden

All diese Technologien teilen ein fundamentales Muster:

| Domäne | Eingabe | Ausgabe | Kernaufgabe |
|--------|---------|---------|-------------|
| Text | Vorherige Tokens | Nächstes Token | Fortsetzung vorhersagen |
| Bilder | Rauschen + Prompt | Weniger Rauschen | Originalbild vorhersagen |
| 3D | Ansichten + Prompt | Form | Konsistentes 3D vorhersagen |
| Audio | Vorherige Frames | Nächster Frame | Wellenform vorhersagen |
| Aktionen | Kontext + Ziel | Werkzeugaufruf | Nützliche Aktion vorhersagen |

Das vereinheitlichende Prinzip: **Muster aus Daten lernen, dann neue Instanzen nach diesen Mustern generieren**.

### 9.2 Warum Dies für Kreative Arbeit Wichtig Ist

Traditionelle digitale Inhaltserstellung erfordert:
- Jahre spezialisierter Ausbildung
- Teure Softwarelizenzen
- Signifikante Zeit pro Asset
- Grosse Teams für ambitionierte Projekte

KI-Werkzeuge bieten:
- Natürlichsprachliche Schnittstellen
- Schnelle Iteration
- Skalierbare Inhaltsgenerierung
- Zugänglichkeit für Einzelentwickler

Die Thesis-Frage - ob kleine Teams grosse Spielwelten erschaffen können - ist fundamental eine Frage, ob KI das Verhältnis von Schöpfer zu Schöpfung wiederherstellen kann, das vor modernen Produktionsanforderungen existierte.

### 9.3 Aktuelle Einschränkungen

KI-Generierungswerkzeuge bleiben in wichtigen Aspekten begrenzt:

| Einschränkung | Beispiel | Status |
|---------------|----------|--------|
| Konsistenz | Gleicher Charakter über Bilder | Teilweise gelöst (LoRA) |
| Kontrollierbarkeit | Präzise räumliche Layouts | Verbessert sich (ControlNet) |
| 3D-Qualität | Produktionsreife Assets | Frühe Stadien |
| Langform-Kohärenz | Romanlanges Erzählen | Ungelöst |
| Echtzeit-Generierung | Live-Spielinhalte | Aufkommend (Oasis, GameNGen) |

---

## Teil 10: Implikationen für Unabhängige Entwicklung

### 10.1 Die Sich Verändernde Landschaft

Für Indie-Entwickler bieten KI-Werkzeuge:

| Aufgabe | Traditionell | KI-Unterstützt |
|---------|--------------|----------------|
| Konzeptkunst | Künstler oder Outsourcing | Generieren + Verfeinern |
| 3D-Modellierung | Modellierer oder Assets | Basis generieren + Bearbeiten |
| Animation | Motion Capture oder manuell | Motion Matching + ML |
| Sprachaufnahme | Schauspieler + Studio | Sprachsynthese |
| Musik | Komponist oder lizenziert | KI-Komposition |
| Schreiben | Autoren | KI-Entwurf + menschliche Bearbeitung |
| Level-Design | Designer | KI-Generierung + Kuratierung |
| QA-Testing | Menschliche Tester | KI-Playtesting + Mensch |

### 10.2 Die Mensch-KI-Partnerschaft

Der effektivste Ansatz ist nicht "KI-Ersatz", sondern "KI-Augmentierung":

```
Menschliche Verantwortlichkeiten:
  - Kreative Richtung
  - Qualitätskuratierung
  - Kohärenzpflege
  - Emotionale Authentizität
  - Finale Genehmigung

KI-Verantwortlichkeiten:
  - Volumengenerierung
  - Variationsexploration
  - Technische Ausführung
  - Iterationsgeschwindigkeit
  - Musteranwendung
```

### 10.3 Ethische Überlegungen

Die KI-Revolution wirft wichtige Fragen auf:
- Trainingsdaten: Wurden Schöpfer für Trainingsmaterial entschädigt?
- Zuschreibung: Wie KI-generierte Inhalte creditieren?
- Arbeit: Was passiert mit verdrängten kreativen Arbeitern?
- Authentizität: Hat KI-generierte Kunst denselben Wert?

Diese Fragen haben keine einfachen Antworten, müssen aber berücksichtigt werden.

---

## Schlussfolgerung: Die Werkzeuge Verstehen

Der Fortschritt von mathematischer Theorie zu praktischen kreativen Werkzeugen folgt einem klaren Pfad:

```
Mathematische Grundlage (1980er)
    ↓
Neuronale Netze im Grossen Massstab (2012)
    ↓
Transformer & Attention (2017)
    ↓
Grosse Sprachmodelle (2018-2020)
    ↓
Diffusion für Bilder (2020-2022)
    ↓
3D-Generierung (2022-2024)
    ↓
Agenten & Werkzeugnutzung (2023-2025)
    ↓
Neuronale Spiel-Engines (2024-Zukunft)
```

Diesen Fortschritt zu verstehen hilft, den aktuellen Moment zu kontextualisieren: Wir befinden uns in einer Periode schneller Fähigkeitserweiterung, aber auch fundamentaler Einschränkungen. Die Werkzeuge sind mächtig, erfordern aber menschliche Richtung, Kuratierung und Integration.

Für den aufstrebenden Einzelentwickler eines Skyrim-grossen RPGs ist die Frage nicht "kann KI alles tun?", sondern vielmehr "welche Teile der Pipeline kann KI beschleunigen, und wo bleibt menschliche Kreativität essenziell?"

Diese Thesis erkundet diese Frage.

---

## Glossar

| Begriff | Definition |
|---------|------------|
| **Attention** | Mechanismus, der Modellen erlaubt, die Relevanz verschiedener Eingaben zu gewichten |
| **Backpropagation** | Algorithmus zur Berechnung von Gradienten für Gewichtsaktualisierungen |
| **CLIP** | Modell, das Text und Bilder in gemeinsamem Einbettungsraum verbindet |
| **Diffusion** | Generativer Prozess, der lernt, Rauschhinzufügung umzukehren |
| **Einbettung** | Dichte Vektorrepräsentation diskreter Eingaben (Wörter, Bilder) |
| **Feintuning** | Anpassung eines vortrainierten Modells an spezifische Aufgabe |
| **GAN** | Generative Adversarial Network - zwei konkurrierende Netze |
| **GPU** | Graphics Processing Unit - Hardware für parallele Berechnung |
| **Latenter Raum** | Komprimierte Repräsentation, in der Modelle operieren |
| **LLM** | Large Language Model - auf Text skaliert trainierter Transformer |
| **LoRA** | Low-Rank Adaptation - effiziente Feintuning-Methode |
| **NeRF** | Neural Radiance Field - neuronales Netz, das 3D-Szene kodiert |
| **Parameter** | Lernbare Gewichte in einem neuronalen Netz |
| **RLHF** | Reinforcement Learning from Human Feedback |
| **Token** | Grundeinheit der Textverarbeitung (ungefähr ein Wortteil) |
| **Transformer** | Architektur mit Self-Attention für Sequenzverarbeitung |

---

## Referenzierte Schlüsselpaper

1. Vaswani et al. (2017) - "Attention Is All You Need" - Transformer-Architektur
2. Brown et al. (2020) - "Language Models are Few-Shot Learners" - GPT-3
3. Radford et al. (2021) - "Learning Transferable Visual Models" - CLIP
4. Rombach et al. (2022) - "High-Resolution Image Synthesis with Latent Diffusion"
5. Mildenhall et al. (2020) - "NeRF: Representing Scenes as Neural Radiance Fields"
6. Kerbl et al. (2023) - "3D Gaussian Splatting for Real-Time Radiance Field Rendering"
7. Poole et al. (2022) - "DreamFusion: Text-to-3D using 2D Diffusion"
8. Park et al. (2023) - "Generative Agents: Interactive Simulacra of Human Behavior"
9. Ha & Schmidhuber (2018) - "World Models"
10. Bruce et al. (2024) - "Genie: Generative Interactive Environments"
