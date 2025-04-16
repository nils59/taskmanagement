import PySimpleGUI as sg
import sqlite3
from datetime import datetime
from collections import deque

# === Konfigurācija ===
VESTURE = deque(maxlen=10)
sg.theme("DarkGrey5")

# === Datubāzes sākotnējā izveide ===
def inicializet_datubazi():
    con = sqlite3.connect("uzdevumi.db")
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS lietotaji (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lietotajvards TEXT UNIQUE NOT NULL,
            parole TEXT NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS uzdevumi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teksts TEXT NOT NULL,
            termins TEXT NOT NULL,
            izveidots TEXT,
            lietotaja_id INTEGER,
            FOREIGN KEY (lietotaja_id) REFERENCES lietotaji(id)
        )
    ''')
    # Noklusētais lietotājs: lietotajs / parole123
    cur.execute("INSERT OR IGNORE INTO lietotaji (lietotajvards, parole) VALUES (?, ?)", 
                ("lietotajs", "parole123"))
    con.commit()
    con.close()

# === Klase uzdevumu pārvaldībai ===
class UzdevumuParvaldnieks:
    def __init__(self, lietotaja_id):
        self.lietotaja_id = lietotaja_id
        self.con = sqlite3.connect("uzdevumi.db")
        self.cur = self.con.cursor()

    def ieladet_uzdevumus(self):
        self.cur.execute("SELECT id, teksts, termins FROM uzdevumi WHERE lietotaja_id=?", (self.lietotaja_id,))
        return self.cur.fetchall()

    def pievienot_uzdevumu(self, teksts, termins):
        self.cur.execute(
            "INSERT INTO uzdevumi (teksts, termins, izveidots, lietotaja_id) VALUES (?, ?, ?, ?)",
            (teksts, termins, str(datetime.now()), self.lietotaja_id)
        )
        VESTURE.append(f"Pievienots: {teksts}")
        self.con.commit()

    def dzest_uzdevumu(self, uzdevuma_id):
        self.cur.execute("SELECT teksts FROM uzdevumi WHERE id=?", (uzdevuma_id,))
        rinda = self.cur.fetchone()
        if rinda:
            VESTURE.append(f"Dzēsts: {rinda[0]}")
            self.cur.execute("DELETE FROM uzdevumi WHERE id=?", (uzdevuma_id,))
            self.con.commit()

# === Lietotāja pieteikšanās logs ===
def autentifikacija():
    layout = [
        [sg.Text("Lietotājvārds:"), sg.Input(key="-LIETOT-")],
        [sg.Text("Parole:"), sg.Input(password_char="*", key="-PAROLE-")],
        [sg.Button("Pieslēgties"), sg.Button("Iziet")]
    ]
    logs = sg.Window("Pieteikšanās", layout)
    while True:
        notikums, vertibas = logs.read()
        if notikums == "Iziet" or notikums == sg.WIN_CLOSED:
            logs.close()
            return None
        if notikums == "Pieslēgties":
            vards, parole = vertibas["-LIETOT-"], vertibas["-PAROLE-"]
            con = sqlite3.connect("uzdevumi.db")
            cur = con.cursor()
            cur.execute("SELECT id FROM lietotaji WHERE lietotajvards=? AND parole=?", (vards, parole))
            rezultats = cur.fetchone()
            con.close()
            if rezultats:
                logs.close()
                return rezultats[0]
            else:
                sg.popup_error("Nepareizs lietotājvārds vai parole!")

# === Galvenais logs ===
def galvenais_logs(parvaldnieks):
    layout = [
        [sg.Menu([["Fails", ["Iziet"]], ["Vēsture", ["Skatīt"]]])],
        [sg.Text("Uzdevums:"), sg.Input(key="-TEKSTS-")],
        [sg.Text("Termiņš (YYYY-MM-DD):"), sg.Input(key="-TERMINS-"), sg.CalendarButton("Izvēlēties", target="-TERMINS-", format="%Y-%m-%d")],
        [sg.Button("Pievienot"), sg.Button("Dzēst atlasīto")],
        [sg.Listbox(values=[], size=(50, 10), key="-SARAKSTS-", select_mode=sg.SELECT_MODE_SINGLE)],
        [sg.Column([
            [sg.Text("Vēsture:")],
            [sg.Multiline(size=(30,10), key="-VESTURE-")],
            [sg.Button("Notīrīt vēsturi")]
        ], key="-VESTURE-COL-", visible=False)],
        [sg.StatusBar("Sagatavots", key="-STATUSS-")]
    ]
    logs = sg.Window("Uzdevumu Pārvaldnieks", layout, finalize=True)
    logs["-VESTURE-"].Widget.pack_forget()

    def atjaunot():
        uzdevumi = parvaldnieks.ieladet_uzdevumus()
        logs["-SARAKSTS-"].update(values=[f"{u[0]}: {u[1]} (līdz {u[2]})" for u in uzdevumi])

    atjaunot()

    while True:
        notikums, vertibas = logs.read()
        if notikums in (sg.WIN_CLOSED, "Iziet"):
            break

        if notikums == "Pievienot":
            teksts, termins = vertibas["-TEKSTS-"].strip(), vertibas["-TERMINS-"]
            if teksts and termins:
                try:
                    datetime.strptime(termins, "%Y-%m-%d")
                    parvaldnieks.pievienot_uzdevumu(teksts, termins)
                    logs["-STATUSS-"].update("Uzdevums pievienots!")
                    logs["-TEKSTS-"].update("")
                    logs["-TERMINS-"].update("")
                    atjaunot()
                except ValueError:
                    sg.popup_error("Nepareizs datuma formāts!")
            else:
                sg.popup_error("Aizpildiet visus laukus!")

        if notikums == "Dzēst atlasīto":
            izvēlēts = vertibas["-SARAKSTS-"]
            if izvēlēts:
                uzdevuma_id = int(izvēlēts[0].split(":")[0])
                parvaldnieks.dzest_uzdevumu(uzdevuma_id)
                logs["-STATUSS-"].update("Uzdevums dzēsts!")
                atjaunot()
            else:
                sg.popup_error("Izvēlieties uzdevumu!")

        if notikums == "Skatīt":
            logs["-VESTURE-COL-"].update(visible=True)
            logs["-VESTURE-"].update("\n".join(VESTURE))

        if notikums == "Notīrīt vēsturi":
            VESTURE.clear()
            logs["-VESTURE-"].update("")

    logs.close()

# === Palaišana ===
if __name__ == "__main__":
    inicializet_datubazi()
    lietotaja_id = autentifikacija()
    if lietotaja_id:
        parvaldnieks = UzdevumuParvaldnieks(lietotaja_id)
        galvenais_logs(parvaldnieks)
