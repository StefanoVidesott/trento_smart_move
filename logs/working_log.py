import os
import json
from datetime import datetime
from InquirerPy import inquirer

FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
FILE = f"{FILE_DIRECTORY}/worklogs.json"
MEMBERS = ["Stefano", "Thabo", "Alessandro"]

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def load_logs():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            data = f.read().strip()
            if not data:
                return []
            return json.loads(data)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️ Attenzione: il file dei log è corrotto, verrà resettato.")
        inquirer.text(
            qmark="👉",
            message="Premi invio per continuare..."
        ).execute()
        return []

def save_logs(logs):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4, ensure_ascii=False)

def validate_data(text):
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

def validate_ora(text):
    try:
        datetime.strptime(text, "%H:%M")
        return True
    except ValueError:
        return False

def add_log():
    logs = load_logs()

    print("\n== Aggiungi Log ==")

    utenti = inquirer.checkbox(
        qmark="👉",
        message="Membri coinvolti:",
        choices=MEMBERS,
        instruction="(usa frecce ↑↓ e spazio per selezionare)",
        validate=lambda result: len(result) > 0
    ).execute()

    # if len(utenti) == len(MEMBERS):
    #     utenti = ["team"]

    data = inquirer.text(
        qmark="👉",
        message="Data (YYYY-MM-DD):",
        default=datetime.today().strftime("%Y-%m-%d"),
        validate=validate_data
    ).execute()

    start = inquirer.text(
        qmark="👉",
        message="Ora inizio (HH:MM):",
        validate=validate_ora
    ).execute()

    end = inquirer.text(
        qmark="👉",
        message="Ora fine (HH:MM):",
        validate=validate_ora
    ).execute()

    descrizione = inquirer.text(
        qmark="👉",
        message="Descrizione attività:"
    ).execute()

    log = {
        "utenti": utenti,
        "data": data,
        "ora_inizio": start,
        "ora_fine": end,
        "descrizione": descrizione
    }

    logs.append(log)
    save_logs(logs)
    print("✔ log salvato!\n")
    inquirer.text(
        qmark="👉",
        message="Premi invio per continuare..."
    ).execute()

def view_logs():
    logs = load_logs()
    if not logs:
        print("\nNessun log salvato.\n")
        inquirer.text(
            qmark="👉",
            message="Premi invio per continuare..."
        ).execute()
        return

    print("\n== Logs ==")
    for i, log in enumerate(logs, 1):
        utenti = ", ".join(log["utenti"])
        print(f"{i}. {utenti} - {log['data']} {log['ora_inizio']} → {log['ora_fine']} | {log['descrizione']}")
    print("")
    inquirer.text(
        qmark="👉",
        message="Premi invio per continuare..."
    ).execute()

def menu():
    while True:
        clear_console()
        scelta = inquirer.select(
            qmark="👉",
            message="Menu Principale - cosa vuoi fare?",
            choices=[
                {"name": "Aggiungi Log", "value": "add"},
                {"name": "Visualizza Logs", "value": "view"},
                {"name": "Esci", "value": "exit"}
            ],
            default="add"
        ).execute()

        if scelta == "add":
            add_log()
        elif scelta == "view":
            view_logs()
        elif scelta == "exit":
            break

if __name__ == "__main__":
    menu()
