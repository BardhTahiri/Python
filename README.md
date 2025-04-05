
# 📌 Projekti i parë në Python

Ky është projekti im i parë i realizuar me Python, ku kam filluar të mësoj **sintaksën bazë** të gjuhës dhe kam përdorur disa nga paketat më të njohura për analizë të të dhënave si:

- `pandas` – për manipulim dhe analizë të të dhënave
- `matplotlib.pyplot` – për krijimin e grafikëve vizualë

---

## 🎯 Qëllimi i projektit

Qëllimi im ishte të:

- Mësoj si të lexoj të dhëna nga një **file CSV**
- Përdor **filtrim**, **grupim**, dhe **rendisje (sorting)** të të dhënave
- Krijoj **grafikë vizualë** për të paraqitur statistikat e ekipeve të NBA-së
- Eksploroj statistika të ndryshme të ekipeve nga sezoni 1997 deri 2022

---

## 📁 Folderi me të dhënat

Kam përdorur një csv file me emrin `NBA_Team_Stats2.csv`, i cili përmban statistika për ekipet e NBA-së për disa sezone të ndryshme. Në këtë skedar gjenden kolona si:

- `Year` – Sezoni
- `Team` – Emri i ekipit
- `Points` – Pikët totale
- `Offensive Overall` – Vlerësimi ofenziv
- `Defensive Overall` – Vlerësimi defenziv

---

## ⚙️ Çfarë bën ky projekt?

- Përdoruesi jep një **sezon (vit)** dhe paraqiten:
  - Top 5 ekipet sipas **pikëve**
  - Top 5 ekipet sipas **sulmit ofenziv**
  - Top 5 ekipet sipas **mbrojtjes defenzive**
- Tregon **top 5 ekipet me mesataren më të lartë të pikëve** nga 1997 deri 2022
- Tregon **top 5 ekipet më të mira defenzivisht**
- Lejon përdoruesin të zgjedhë një **ekip** dhe një **statistikë** për të parë ndryshimin e saj në vite

---

## 🖼️ Pamje të grafikëve

Projekti krijon grafikë të ndryshëm si:

- **Grafikë kolonash (bar chart)** për krahasime mes ekipeve
- **Grafikë linje (line chart)** për të parë progresin e një ekipi në një statistikë të caktuar

---

## 🚀 Si ta ekzekutosh projektin?

1. Sigurohu që ke instaluar paketat e nevojshme:

```bash
pip install pandas
pip install matplotlib
```

2. Vendos csv file `NBA_Team_Stats2.csv` në të njëjtin folder me skriptën.
3. Ekzekuto skriptën në terminal ose në një editor si PyCharm/VSCode:

```bash
python projekti.py
```

---

## 👨‍💻 Përfundim

Ky projekt më ndihmoi të:

- Kuptoj më mirë sintaksën e Python-it
- Përdor metodologji themelore të analizës së të dhënave
- Krijoj grafikë për të vizualizuar informacionin në mënyrë më të qartë

---

📂 **File kryesor**: `projekti.py`  
📊 **Të dhënat**: `NBA_Team_Stats2.csv`
