def carica_da_file(file_path):
    try:
        with open (file_path, 'r', encoding='utf-8') as infile:
            from csv import reader
            csv_reader = reader(infile)
            biblioteca = {}
            for row in csv_reader:
                if len(row)<5:
                    continue
                titolo = row[0]
                autore = row[1]
                anno = int(row[2])
                pagine = int(row[3])
                sezione = int(row[4])
                libro = {"titolo":titolo,
                        "autore":autore,
                        "anno":anno,
                        "pagine":pagine
                         }

                if sezione not in biblioteca:
                    biblioteca[sezione] = [libro]
                else:
                    biblioteca[sezione].append(libro)
            return biblioteca

    except FileNotFoundError:
        return None
    """Carica i libri dal file"""
    # TODO


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    if sezione not in biblioteca:
        print("La sezione non è valida")
        return None

    for libro in biblioteca[sezione]:
        if libro["titolo"].lower() == titolo.lower():
            print("Il libro è già presente nella biblioteca")
            return None


    nuovoLibro = {"titolo":titolo,
                  "autore":autore,
                  "anno":anno,
                  "pagine":pagine
                  }
    biblioteca[sezione].append(nuovoLibro)

    try:
        with open(file_path, 'a', encoding='utf-8') as outfile:
            import csv
            outfile.write(f'\n{titolo},{autore},{anno},{pagine},{sezione}')

    except FileNotFoundError:
        print("Errore")
        return None

    return nuovoLibro

    """Aggiunge un libro nella biblioteca"""
    # TODO


def cerca_libro(biblioteca, titolo):
    for sezione,libri in biblioteca.items():
        for libro in libri:
            if libro["titolo"].lower() == titolo.lower():
                return f'{libro["titolo"]},{libro["autore"]},{libro["anno"]},{libro["pagine"]},{sezione}'

    return None

    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    if sezione in biblioteca:
        titoli =[]
        for libro in biblioteca[sezione]:
            titoli.append(libro["titolo"])
            titoliOrdinati=sorted(titoli)
        return titoliOrdinati
    else:
        print("Sezione non valida")
        return None

    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

