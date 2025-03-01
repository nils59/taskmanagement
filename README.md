# Uzdevumu Pārvaldnieks

![screenshot](https://github.com/user-attachments/assets/c36ea4a7-f840-4640-8701-d93535e06be6)


Vienkārša uzdevumu pārvaldības programma, izveidota ar PySimpleGUI. Programma ļauj pievienot, dzēst un pārvaldīt uzdevumus ar datumu termiņiem.


## Lejupielāde

1. Dodieties uz [Release sadaļu]([https://github.com/yourusername/task-manager/releases](https://github.com/nils59/taskmanagement/releases/tag/1.0))
2. Lejupielādējiet jaunāko `taskmanagement.exe` failu
3. Saglabājiet failu savā datorā


🚀 **Portable versija** - nav nepieciešama instalācija!  

Veiciet dubultklikšķi uz `taskmanagement.exe` un programma tiks palaista.


**Pamatdarbības:**
1. **Pievienot uzdevumu**  
   - Ievadiet uzdevuma tekstu un termiņu (`YYYY-MM-DD`)  
   - Nospiediet "Pievienot"

2. **Dzēst uzdevumu**  
   - Atlasiet uzdevumu sarakstā  
   - Nospiediet "Dzēst"

3. **Skatīt vēsturi**  
   - Izvēlnē atlasiet "Vēsture → Skatīt"


## Funkcionalitāte
- ✅ Automātiska datu saglabāšana (`uzdevumi.json`)
- 📅 Iebūvēts kalendārs termiņu izvēlei
- 🛡️ Portabalā versija bez atkarībām
- 🔄 Vēstures logs ar pēdējām izmaiņām


## Testēšanas Pārskats

| Scenārijs                 | Rezultāts                         |
|---------------------------|-----------------------------------|
| Pievienot uzdevumu bez teksta | Kļūda: "Aizpildiet visus laukus!" |
| Ievadīt nepareizu datumu  | Kļūda: "Nepareizs formāts!"       |
| Dzēst no tukša saraksta   | Kļūda: "Saraksts ir tukšs!"       |


## Kursa Prasību Atbilstība

| Prasība                   | Statuss        | Pamatojums               |
|---------------------------|----------------|--------------------------|
| Datu struktūra            | ✅ Pabeigts    | Vēstures glabāšanai      |
| Bibliotēka (PySimpleGUI)  | ✅ Pabeigts    | GUI izstrādei            |
| Datu bāze (JSON)          | ⚠️ Daļēji     | Nav SQLite/MySQL integrācija |
| Lietotāju autentifikācija | ❌ Nav pabeigts | Nav implementēta         |


## Izmantotās Tehnoloģijas
- **Python 3.12** - Pamatprogrammēšanas valoda  
- **PySimpleGUI** - Lietotāja saskarnes izstrāde  
- **JSON** - Datu glabāšana  
- **Git** - Versiju kontrole  


## Licence
Šis projekts ir licencēts saskaņā ar [MIT Licenci](LICENSE).
