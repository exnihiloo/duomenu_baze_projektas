from teatras_modelis import engine, Sale, Spektaklis, Rezisierius, Aktorius, Vaidmuo
from sqlalchemy.orm import sessionmaker


session = sessionmaker(bind=engine)()

def ivesti_sale():
    print("--- Įveskite naują salę ---")
    pavadinimas = input("Įveskite salės pavadinimą: ")
    sale = Sale(pavadinimas = pavadinimas)
    session.add(sale)
    session.commit()
    print(f"Salė: s{sale} sėkmingai pridėta į duomenų bazę.")



while True:
    print('Teatro duomenų bazė, pasirinimai:')
    print('\t1 - teatro duomenų įvestis')
    print('\t2 - teatro duomenų peržiūra')
    print('\t3 - teatro duomenų atnaujinimas')
    print('\t4 - teatro duomenų trynimas')
    print('\t0 - išeiti iš programos')
    try:
        choice = int(input("Pasirinkite: "))
        if choice == 0 or choice > 4:
            print("Tokio pasirinkimo nėra.")
        if choice == 1:
            print("Kokius duomenis norite įrašyti?")
            print("\t1 - salės.")
            print("\t2 - režisieriaus.")
            print("\t3 - aktoriaus.")
            print("\t4 - spektaklio.")
            print("\t5 - vaidmens.")
            try:
                pasirinkimas = int(input("Pasirinkite: "))
                if pasirinkimas == 0 or pasirinkimas > 6:
                    print("Tokio pasirinkimo nėra.")
                if pasirinkimas == 1:
                    ivesti_sale()
                if pasirinkimas == 2:
                    pass
                if pasirinkimas == 3:
                    pass
                if pasirinkimas == 4:
                    pass
                if pasirinkimas == 5:
                    pass
            except ValueError:
                print("Įveskite 1/2/3/4/5. Įvedėte tai, ko nėra pasirinkime.")

        if choice == 2:
            print("Kokius duomenis norite peržiūrėti?")
            print("\t1 - salių.")
            print("\t2 - režisierių.")
            print("\t3 - aktorių.")
            print("\t4 - spektaklių.")
            print("\t5 - vaidmenų.")
            try:
                pasirinkimas2 = int(input("Pasirinkite: "))
                if pasirinkimas2 == 0 or pasirinkimas2 > 6:
                    print("Tokio pasirinkimo nėra.")
                if pasirinkimas2 == 1:
                    pass
                if pasirinkimas2 == 2:
                    pass
                if pasirinkimas2 == 3:
                    pass
                if pasirinkimas2 == 4:
                    pass
                if pasirinkimas2 == 5:
                    pass
            except ValueError:
                print("Įveskite 1/2/3/4/5. Įvedėte tai, ko nėra pasirinkime.")
        if choice == 3:
            print("Kokius duomenis norite atnaujinti?")
            print("\t1 - salių.")
            print("\t2 - režisierių.")
            print("\t3 - aktorių.")
            print("\t4 - spektaklių.")
            print("\t5 - vaidmenų.")
            try:
                pasirinkimas3 = int(input("Pasirinkite: "))
                if pasirinkimas3 == 0 or pasirinkimas3 > 6:
                    print("Tokio pasirinkimo nėra.")
                if pasirinkimas3 == 1:
                    pass
                if pasirinkimas3 == 2:
                    pass
                if pasirinkimas3 == 3:
                    pass
                if pasirinkimas3 == 4:
                    pass
                if pasirinkimas3 == 5:
                    pass
            except ValueError:
                print("Įveskite 1/2/3/4/5. Įvedėte tai, ko nėra pasirinkime.")
        if choice == 4:
            pass
        if choice == 0:
            print("Išėjote")
            break
    except ValueError:
        print("Įveskite 0/1/2/3/4. Įvedėte tai, ko nėra pasirinkime.")