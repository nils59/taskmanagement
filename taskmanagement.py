import PySimpleGUI as sg
import json
import os
from datetime import datetime
from collections import deque

# Konfigurācija
FAILS = "uzdevumi.json"
VESTURE = deque(maxlen=10)  # Saglabā pēdējās 10 izmaiņas
sg.theme("DarkGrey5")

class UzdevumuParvaldnieks:
    def __init__(self):
        self.uzdevumi = self.ieladet_uzdevumus()

    def ieladet_uzdevumus(self):
        if os.path.exists(FAILS):
            with open(FAILS, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def saglabat_uzdevumus(self):
        with open(FAILS, "w", encoding="utf-8") as f:
            json.dump(self.uzdevumi, f, ensure_ascii=False, indent=2)

    def pievienot_uzdevumu(self, teksts, termins):
        self.uzdevumi.append({"teksts": teksts, "termins": termins, "izveidots": str(datetime.now())})
        VESTURE.append(f"Pievienots: {teksts}")

    def dzest_uzdevumu(self, indekss):
        if 0 <= indekss < len(self.uzdevumi):
            VESTURE.append(f"Dzēsts: {self.uzdevumi[indekss]['teksts']}")
            del self.uzdevumi[indekss]

# GUI izkārtojums
layout = [
    [sg.Menu([["Fails", ["Saglabāt", "Iziet"]], ["Vēsture", ["Skatīt"]]])],
    [sg.Text("Uzdevums:"), sg.Input(key="-TEKSTS-", size=(30,1))],
    [sg.Text("Termiņš (YYYY-MM-DD):"), sg.Input(key="-TERMINS-", size=(10,1)),
     sg.CalendarButton("Izvēlēties", target="-TERMINS-", format="%Y-%m-%d")],
    [sg.Button("Pievienot"), sg.Button("Dzēst")],
    [sg.Listbox(values=[], size=(50,10), key="-SARAKSTS-")],
    [sg.Column([
        [sg.Text("Vēsture:")],
        [sg.Multiline(size=(30,10), key="-VESTURE-")],
        [sg.Button("Notīrīt vēsturi")]
    ], key="-VESTURE-COL-", visible=False)],
    [sg.StatusBar("Sagatavots", key="-STATUSS-")]
]

logs = sg.Window("Uzdevumu Pārvaldnieks", layout, finalize=True)
parvaldnieks = UzdevumuParvaldnieks()
logs["-VESTURE-"].Widget.pack_forget()  # Slēpt vēstures sadaļu sākumā

# Notikumu apstrāde
while True:
    notikums, vertibas = logs.read()

    if notikums in (sg.WIN_CLOSED, "Iziet"):
        parvaldnieks.saglabat_uzdevumus()
        break

    if notikums == "Pievienot":
        teksts = vertibas["-TEKSTS-"].strip()
        termins = vertibas["-TERMINS-"]

        if teksts and termins:
            try:
                datetime.strptime(termins, "%Y-%m-%d")
                parvaldnieks.pievienot_uzdevumu(teksts, termins)
                logs["-STATUSS-"].update("Uzdevums pievienots!")
                logs["-TEKSTS-"].update("")
                logs["-TERMINS-"].update("")
            except ValueError:
                sg.popup_error("Nepareizs datuma formāts!")
        else:
            sg.popup_error("Aizpildiet visus laukus!")

    if notikums == "Dzēst":
        if parvaldnieks.uzdevumi:
            try:
                parvaldnieks.dzest_uzdevumu(0)  # Dzēš pirmo sarakstu
                logs["-STATUSS-"].update("Uzdevums dzēsts!")
            except IndexError:
                sg.popup_error("Saraksts ir tukšs!")
        else:
            sg.popup_error("Nav ko dzēst!")

    if notikums == "Skatīt":
        logs["-VESTURE-COL-"].update(visible=True)
        logs["-VESTURE-"].update("\n".join(VESTURE))

    if notikums == "Notīrīt vēsturi":
        VESTURE.clear()
        logs["-VESTURE-"].update("")

    # Atjaunina uzdevumu sarakstu
    logs["-SARAKSTS-"].update(values=[f"{uzd['teksts']} (līdz {uzd['termins']})" for uzd in parvaldnieks.uzdevumi])

logs.close()
