import sys
import os

ALFABETO_ESTESO = "abcdefghijklmnopqrstuvwxyz0123456789"

def cifrario(testo, chiave, modalità):
    risultato = []

    for char in testo:
        lower = char.lower()
        if lower in ALFABETO_ESTESO:
            indice = ALFABETO_ESTESO.index(lower)
            if modalità == "cript":
                nuovo_indice = (indice + chiave) % len(ALFABETO_ESTESO)
            elif modalità == "decript":
                nuovo_indice = (indice - chiave) % len(ALFABETO_ESTESO)
            nuovo_char = ALFABETO_ESTESO[nuovo_indice]
            if char.isupper():
                nuovo_char = nuovo_char.upper()
            risultato.append(nuovo_char)
        else:
            risultato.append(char)

    return "".join(risultato)



def elabora_testo(testo: str, chiave: int, modalità: str, passaggi: int) -> str:
    """Esegue più passaggi di cifratura o decifratura."""
    risultato = testo
    for _ in range(passaggi):
        risultato = cifrario(risultato, chiave, modalità)
    return risultato


def chiedi_input(prompt: str, tipo=int, condizione=None, messaggio_errore="Valore non valido."):
    """Gestisce input sicuro da terminale."""
    while True:
        try:
            valore = tipo(input(prompt))
            if condizione and not condizione(valore):
                raise ValueError
            return valore
        except ValueError:
            print(messaggio_errore)


def main():
    print("=== Cifrario di Cesare Avanzato ===")

    while True:
        print("\nScegli un'opzione:")
        print("1. Inserisci testo manualmente")
        print("2. Leggi testo da file")
        print("3. Esci")

        scelta = input("→ ").strip()

        if scelta == "3":
            print("Uscita dal programma.")
            break

        if scelta == "1":
            testo = input("\nInserisci il testo: ")
        elif scelta == "2":
            percorso = input("\nPercorso del file da leggere: ")
            if not os.path.exists(percorso):
                print(" File non trovato.")
                continue
            with open(percorso, "r", encoding="utf-8") as f:
                testo = f.read()
            print("Testo caricato dal file.")
        else:
            print("Scelta non valida.")
            continue

        modalità = input("\nScrivi 'cript' o 'decript': ").lower()
        while modalità not in ["cript", "decript"]:
            modalità = input("Modalità non valida. Scrivi 'cript' o 'decript': ").lower()

        chiave = chiedi_input("Inserisci la chiave (numero intero): ", int)
        passaggi = chiedi_input("Quanti passaggi vuoi eseguire (>=1)? ", int, lambda x: x >= 1)

        risultato = elabora_testo(testo, chiave, modalità, passaggi)

        print(f"\nRisultato finale ({modalità} con {passaggi} passaggi):\n")
        print(risultato)

        # Opzione di salvataggio
        salva = input("\nVuoi salvare il risultato su file? (s/n): ").lower()
        if salva == "s":
            out_file = input("Nome del file di output (es. output.txt): ")
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(risultato)
            print(f"Risultato salvato in '{out_file}'.")

        continua = input("\nVuoi eseguire un'altra operazione? (s/n): ").lower()
        if continua != "s":
            print("Fine del programma.")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterruzione da tastiera. Uscita dal programma.")
        sys.exit(0)
