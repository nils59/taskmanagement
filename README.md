# Uzdevumu Pārvaldnieks

![screenshot](https://github.com/user-attachments/assets/c36ea4a7-f840-4640-8701-d93535e06be6)


Vienkārša uzdevumu pārvaldības programma, izveidota ar Python, izmantojot PySimpleGUI un SQLite. 
Projekts paredzēts lietotājiem, kuri vēlas vienkārši un pārskatāmi pārvaldīt savus darbus, izmantojot grafisko saskarni.



## Funkcionalitāte
- ✅ Lietotāja autentifikācija (pieteikšanās ar lietotājvārdu un paroli)
- ✅ Pievienot uzdevumu ar termiņu
- ✅ Dzēst izvēlēto uzdevumu
- ✅ Vēstures logs (pēdējās 10 izmaiņas)
- ✅ Datu saglabāšana SQLite datubāzē
- ✅ Kalendāra poga ērtai termiņa izvēlei


## 📂 Datubāzes struktūra

### Tabula `lietotaji`
| Kolonna       | Tips     |
|---------------|----------|
| id            | INTEGER PRIMARY KEY |
| lietotajvards | TEXT (unikāls) |
| parole        | TEXT     |

### Tabula `uzdevumi`
| Kolonna       | Tips     |
|---------------|----------|
| id            | INTEGER PRIMARY KEY |
| teksts        | TEXT     |
| termins       | TEXT     |
| izveidots     | TEXT     |
| lietotaja_id  | INTEGER (FK) |

## 🔐 Noklusētais lietotājs

- **Lietotājvārds:** `lietotajs`  
- **Parole:** `parole123`

## Kā lietot

1.Palaid taskmanagement.exe

2.Pieslēdzies ar lietotājvārdu/paroli

3.Pievieno vai dzēs uzdevumus izmantojot GUI

4.Skaties vēsturi izvēlnē “Vēsture”

Piezīmes
Visu uzdevumu informācija tiek saglabāta lokāli uzdevumi.db failā.

Portable versija – nav nepieciešama instalācija (ja kompilēta ar PyInstaller).

## Izmantotās Tehnoloģijas
- **Python 3.x** - Pamatprogrammēšanas valoda  
- **PySimpleGUI** - Lietotāja saskarnes izstrāde  
- **sqlite3** - Datu glabāšana  


## Licence
Šis projekts ir licencēts saskaņā ar [MIT Licenci](LICENSE).
