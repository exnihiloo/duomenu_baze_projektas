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


def ivesti_rezisieriu():
    print("--- Įveskite naują režisierių ---")
    vardas = input("Įveskite režisieriaus vardą: ")
    pavarde = input("Įveskite režisieriaus pavardę: ")
    rezisierius = Rezisierius(vardas = vardas, pavarde = pavarde)
    session.add(rezisierius)
    session.commit()
    print(f"Režisierius/ė: {rezisierius} sėkmingai pridėtas/a į duomenų bazę.")


def ivesti_aktoriu():
    print("--- Įveskite naują aktorių/aktorę ---")
    vardas = input("Įveskite aktoriaus/ės vardą: ")
    pavarde = input("Įveskite aktoriaus/ės pavardę: ")
    aktorius = Aktorius(vardas = vardas, pavarde = pavarde)
    session.add(aktorius)
    session.commit()
    print(f"Aktorius/ė: {aktorius} sėkmingai pridėtas/a į duomenų bazę.")

def ivesti_spektakli():
    print("--- Įveskite naują spektaklį ---")
    try:
        pavadinimas = input("Įveskite spektaklio pavadinimą: ")
        sales = session.query(Sale).all()
        if len(sales) == 0:
            print("Salių duomenų bazė tuščia")
            return ivesti_spektakli()
        else:
            print("Salės: ")
            for sale in sales:
                print("\t-", sale)
        sales_id = int(input("Įveskite salės ID: "))
    except ValueError:
        print("Salės ID negali būti raidė.")
        return ivesti_spektakli()
    sales_choice = session.query(Sale).get(sales_id)
    if sales_choice:
        session.commit()
    else:
        print("Tokio salės ID nėra.")
        return ivesti_spektakli()
    rezisieriai = session.query(Rezisierius).all()
    if len(rezisieriai) == 0:
        print("Režisierių duomenų bazė tuščia.")
        return ivesti_spektakli()
    else:
        print("Režisieriai: ")
        for rezisierius in rezisieriai:
            print("\t-", rezisierius)
    try:
        rezisierius_id = int(input("Įveskite režisieriaus ID: "))  
    except ValueError:
        print("Režisieriaus ID negali būti raidė.")
        return ivesti_spektakli()
    rezisierius_choice = session.query(Rezisierius).get(rezisierius_id)
    if rezisierius_choice:
        session.commit()
    else:
        print("Tokio režisieriaus ID nėra.")
        return ivesti_spektakli()
    spektaklis = Spektaklis(pavadinimas = pavadinimas, sale_id = sales_id, rezisierius_id = rezisierius_id)
    session.add(spektaklis)
    session.commit()
    print(f"Spektaklis: [{spektaklis}] sėkmingai pridėtas į duomenų bazę.")


def ivesti_vaidmeni():
    print("--- Įveskite naują vaidmenį ---")
    try:
        vaidmuo = input("Įveskite personažo vardą: ")
        aktoriai = session.query(Aktorius).all()
        if len(aktoriai) == 0:
            print("Aktorių duomenų bazė tuščia")
            return ivesti_vaidmeni()
        else:
            print("Aktoriai: ")
            for aktorius in aktoriai:
                print("\t-", aktorius)
        aktorius_id = int(input("Įveskite aktoriaus ID: "))
    except ValueError:
        print("Aktoriaus ID negali būti raidė.")
        return ivesti_vaidmeni()
    aktorius_choice = session.query(Aktorius).get(aktorius_id)
    if aktorius_choice:
        session.commit()
    else:
        print("Tokio aktoriaus ID nėra.")
        return ivesti_vaidmeni()
    spektakliai = session.query(Spektaklis).all()
    if len(spektakliai) == 0:
        print("Spektaklių duomenų bazė tuščia.")
        return ivesti_vaidmeni()
    else:
        print("Spektakliai: ")
        for spektaklis in spektakliai:
            print("\t-", spektaklis)
    try:
        spektaklis_id = int(input("Įveskite spektaklio ID: "))  
    except ValueError:
        print("Spektaklio ID negali būti raidė.")
        return ivesti_vaidmeni()
    spektaklis_choice = session.query(Spektaklis).get(spektaklis_id)
    if spektaklis_choice:
        session.commit()
    else:
        print("Tokio spektkalio ID nėra.")
        return ivesti_vaidmeni()
    vaidmuo = Vaidmuo(vaidmuo = vaidmuo, aktorius_id = aktorius_id, spektaklis_id = spektaklis_id)
    session.add(vaidmuo)
    session.commit()
    print(f"Vaidmuo: ({vaidmuo}) sėkmingai pridėtas į duomenų bazę.")


def saliu_perziura():
    sales = session.query(Sale).all()
    if len(sales) == 0:
        print("Teatro salių duomenų bazė tuščia.")
    else:
        print("Salės:")
        for sale in sales:
            print("\t-", sale)

def rezisieriu_perziura():
    rezisiariai = session.query(Rezisierius).all()
    if len(rezisiariai) == 0:
        print("Teatro režisierių duomenų bazė tuščia.")
    else:
        print("Režisieriai:")
        for rezisierius in rezisiariai:
            print("\t-", rezisierius)

def aktoriu_perziura():
    aktoriai = session.query(Aktorius).all()
    if len(aktoriai) == 0:
        print("Teatro aktorių duomenų bazė tuščia.")
    else:
        print("Aktoriai:")
        for aktorius in aktoriai:
            print("\t-", aktorius)

def spektakliu_perziura():
    spektakliai = session.query(Spektaklis).all()
    if len(spektakliai) == 0:
        print("Teatro spektaklių duomenų bazė tuščia.")
    else:
        print("Spektakliai:")
        for spektaklis in spektakliai:
            print("\t-", spektaklis)

def vaidmenu_perziura():
    vaidmenys = session.query(Vaidmuo).all()
    if len(vaidmenys) == 0:
        print("Spektaklių vaidmenų duomenų bazė tuščia.")
    else:
        print("Vaidmenys:")
        for vaidmuo in vaidmenys:
            print("\t-", vaidmuo)


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
                    ivesti_rezisieriu()
                if pasirinkimas == 3:
                    ivesti_aktoriu()
                if pasirinkimas == 4:
                    ivesti_spektakli()
                if pasirinkimas == 5:
                    ivesti_vaidmeni()
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
                    saliu_perziura()
                if pasirinkimas2 == 2:
                    rezisieriu_perziura()
                if pasirinkimas2 == 3:
                    aktoriu_perziura()
                if pasirinkimas2 == 4:
                    spektakliu_perziura()
                if pasirinkimas2 == 5:
                    vaidmenu_perziura()
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