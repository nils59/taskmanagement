
# 📄 Uzdevumu pārvaldnieks – Dokumentācija

## Problēmas izpēte un analīze

### Izpētes metodes izvēle
Tika veikta novērošana un intervijas ar lietotājiem (skolēni un studenti), lai izprastu uzdevumu organizēšanas problēmas.

### Izpētes process
Lietotāji bieži aizmirst par termiņiem, izmantojot nepārskatāmas piezīmes vai aplikācijas.

### Secinājumi
Nepieciešama vienkārša programma uzdevumu pievienošanai, dzēšanai un termiņu pārvaldībai.

---

## Programmatūras prasību specifikācija

### Mērķauditorija
Skolēni, studenti un individuāli lietotāji, kas vēlas pārvaldīt savus darbus vienkāršā veidā.

### Funkcionālās prasības
- Uzdevumu pievienošana un dzēšana
- Termiņu pārvaldība
- Datu saglabāšana datubāzē
- Lietotāja autentifikācija

### Nefunkcionālās prasības
- Vienkāršs un saprotams GUI
- Datu drošība ar paroli
- Lokāla lietošana bez interneta

### Programmas skice
![Programmas skice](screenshot.png) *(pievienojams ekrānattēls)*

---

## Programmatūras izstrādes plāns

### Izstrādes modelis: Iteratīvais
1. Izpēte
2. GUI prototips
3. Funkcionalitātes pievienošana
4. Autentifikācija
5. Testēšana un dokumentācija

---

## Atkļūdošanas un testēšanas pārskats

| Scenārijs | Rezultāts |
|----------|-----------|
| Tukšs uzdevums | Kļūda: "Aizpildiet visus laukus!" |
| Nepareizs datums | Kļūda: "Nepareizs formāts!" |
| Dzēst no tukša | Kļūda: "Saraksts ir tukšs!" |
| Nepareiza parole | Kļūda: "Nepareizs lietotājvārds vai parole!" |
| Datu saglabāšana | Saglabāts uzdevumi.db failā |

---

## Lietotāja ceļvedis

1. **Palaid `taskmanagement.exe`**
2. **Ievadi lietotājvārdu un paroli**
3. **Pievieno uzdevumus**
4. **Dzēs izvēlētos uzdevumus**
5. **Skati vēsturi** izvēlnē "Vēsture → Skatīt"

---

## Programmas kods

Kods pievienots dokumentācijas pielikumā (`taskmanagement.py`). Strukturēts klasēs un komentēts.

---

## Piezīmes

- Izstrādāts ar Python un PySimpleGUI
- Datu saglabāšanai izmantota SQLite datubāze
- Noklusētais lietotājs: `lietotajs / parole123`
