from teatras_modelis import engine, Sale, Spektaklis, Rezisierius, Aktorius, Vaidmuo
from sqlalchemy.orm import sessionmaker
from datetime import *

session = sessionmaker(bind=engine)()

def ivesti_sale():
    print("--- Įveskite naują salę ---")
    pavadinimas = input("Įveskite salės pavadinimą: ")
    adresas = input("Įveskite salės adresą: ")
    sale = Sale(pavadinimas = pavadinimas, adresas = adresas)
    session.add(sale)
    session.commit()
    print(f"Salė: {sale} sėkmingai pridėta į duomenų bazę.")


def ivesti_rezisieriu():
    print("--- Įveskite naują režisierių ---")
    try:
        vardas = input("Įveskite režisieriaus vardą: ")
        pavarde = input("Įveskite režisieriaus pavardę: ")
        gimimo_data = datetime.strptime(input("Įveskite režisieriaus gimimo datą (YYYY-MM-DD): "), "%Y-%m-%d")
    except ValueError:
        print("\x1B[1mBlogai įvesta režisieriaus/ės gimimo data.\x1B[0m")
        return ivesti_rezisieriu()
    else:
        rezisierius = Rezisierius(vardas = vardas, pavarde = pavarde, gimimo_data = gimimo_data)
        session.add(rezisierius)
        session.commit()
        print(f"Režisierius/ė: {rezisierius} sėkmingai pridėtas/a į duomenų bazę.")


def ivesti_aktoriu():
    print("--- Įveskite naują aktorių/aktorę ---")
    try:
        vardas = input("Įveskite aktoriaus/ės vardą: ")
        pavarde = input("Įveskite aktoriaus/ės pavardę: ")
        gimimo_data = datetime.strptime(input("Įveskite aktoriaus/ės gimimo datą (YYYY-MM-DD): "), "%Y-%m-%d")
    except ValueError:
        print("\x1B[1mBlogai įvesta aktoriaus/ės gimimo data.\x1B[0m")
        return ivesti_aktoriu()
    else:
        aktorius = Aktorius(vardas = vardas, pavarde = pavarde, gimimo_data = gimimo_data)
        session.add(aktorius)
        session.commit()
        print(f"Aktorius/ė: {aktorius} sėkmingai pridėtas/a į duomenų bazę.")

def ivesti_spektakli():
    print("--- Įveskite naują spektaklį ---")
    try:
        pavadinimas = input("Įveskite spektaklio pavadinimą: ")
        sales = session.query(Sale).all()
        if len(sales) == 0:
            print("\x1B[1mSalių duomenų bazė tuščia\x1B[0m")
            return ivesti_spektakli()
        else:
            print("Salės: ")
            for sale in sales:
                print("\t-", sale)
        sales_id = int(input("Įveskite salės ID: "))
    except ValueError:
        print("\x1B[1mSalės ID negali būti raidė.\x1B[0m")
        return ivesti_spektakli()
    sales_choice = session.query(Sale).get(sales_id)
    if sales_choice:
        session.commit()
    else:
        print("\x1B[1mTokio salės ID nėra.\x1B[0m")
        return ivesti_spektakli()
    rezisieriai = session.query(Rezisierius).all()
    if len(rezisieriai) == 0:
        print("\x1B[1mRežisierių duomenų bazė tuščia.\x1B[0m")
        return ivesti_spektakli()
    else:
        print("Režisieriai: ")
        for rezisierius in rezisieriai:
            print("\t-", rezisierius)
    try:
        rezisierius_id = int(input("Įveskite režisieriaus ID: "))  
    except ValueError:
        print("\x1B[1mRežisieriaus ID negali būti raidė.\x1B[0m")
        return ivesti_spektakli()
    rezisierius_choice = session.query(Rezisierius).get(rezisierius_id)
    if rezisierius_choice:
        session.commit()
    else:
        print("\x1B[1mTokio režisieriaus ID nėra.\x1B[0m")
        return ivesti_spektakli()
    spektaklis = Spektaklis(pavadinimas = pavadinimas, sale_id = sales_id, rezisierius_id = rezisierius_id)
    session.add(spektaklis)
    session.commit()
    print(f"Spektaklis: {spektaklis} sėkmingai pridėtas į duomenų bazę.")


def ivesti_vaidmeni():
    print("--- Įveskite naują vaidmenį ---")
    try:
        vaidmuo = input("Įveskite personažo vardą: ")
        aktoriai = session.query(Aktorius).all()
        if len(aktoriai) == 0:
            print("\x1B[1mAktorių duomenų bazė tuščia\x1B[0m")
            return ivesti_vaidmeni()
        else:
            print("Aktoriai: ")
            for aktorius in aktoriai:
                print("\t-", aktorius)
        aktorius_id = int(input("Įveskite aktoriaus/ės ID: "))
    except ValueError:
        print("\x1B[1mAktoriaus/ės ID negali būti raidė.\x1B[0m")
        return ivesti_vaidmeni()
    aktorius_choice = session.query(Aktorius).get(aktorius_id)
    if aktorius_choice:
        session.commit()
    else:
        print("\x1B[1mTokio aktoriaus ID nėra.\x1B[0m")
        return ivesti_vaidmeni()
    spektakliai = session.query(Spektaklis).all()
    if len(spektakliai) == 0:
        print("\x1B[1mSpektaklių duomenų bazė tuščia.\x1B[0m")
        return ivesti_vaidmeni()
    else:
        print("Spektakliai: ")
        for spektaklis in spektakliai:
            print("\t-", spektaklis)
    try:
        spektaklis_id = int(input("Įveskite spektaklio ID: "))  
    except ValueError:
        print("\x1B[1mSpektaklio ID negali būti raidė.\x1B[0m")
        return ivesti_vaidmeni()
    spektaklis_choice = session.query(Spektaklis).get(spektaklis_id)
    if spektaklis_choice:
        session.commit()
    else:
        print("\x1B[1mTokio spektkalio ID nėra.\x1B[0m")
        return ivesti_vaidmeni()
    spektaklis_choice.aktoriai.append(aktorius_choice)
    vaidmuo = Vaidmuo(vaidmuo = vaidmuo, aktorius_id = aktorius_id, spektaklis_id = spektaklis_id)
    session.add(vaidmuo)
    session.commit()
    print(f"Vaidmuo: {vaidmuo} sėkmingai pridėtas į duomenų bazę.")


def saliu_perziura():
    sales = session.query(Sale).all()
    if len(sales) == 0:
        print("\x1B[1mTeatro salių duomenų bazė tuščia.\x1B[0m")
    else:
        print("Salės:")
        for sale in sales:
            print("\t-", sale)

def rezisieriu_perziura():
    rezisiariai = session.query(Rezisierius).all()
    if len(rezisiariai) == 0:
        print("\x1B[1mTeatro režisierių duomenų bazė tuščia.\x1B[0m")
    else:
        print("Režisieriai:")
        for rezisierius in rezisiariai:
            print("\t-", rezisierius)

def aktoriu_perziura():
    aktoriai = session.query(Aktorius).all()
    if len(aktoriai) == 0:
        print("\x1B[1mTeatro aktorių duomenų bazė tuščia.\x1B[0m")
    else:
        print("Aktoriai:")
        for aktorius in aktoriai:
            print("\t-", aktorius)

def spektakliu_perziura():
    spektakliai = session.query(Spektaklis).all()
    if len(spektakliai) == 0:
        print("\x1B[1mTeatro spektaklių duomenų bazė tuščia.\x1B[0m")
    else:
        print("Spektakliai:")
        for spektaklis in spektakliai:
            print("\t-", spektaklis)

def vaidmenu_perziura():
    vaidmenys = session.query(Vaidmuo).all()
    if len(vaidmenys) == 0:
        print("\x1B[1mSpektaklių vaidmenų duomenų bazė tuščia.\x1B[0m")
    else:
        print("Vaidmenys:")
        for vaidmuo in vaidmenys:
            print("\t-", vaidmuo)


def pasirinkti_sale():
    saliu_perziura()
    try:
        sales_id = int(input("Įveskite salės ID: "))
    except ValueError:
        print("\x1B[1mSalės ID turi būti skaičius.\x1B[0m")
        return pasirinkti_sale()
    else:
        if sales_id:
            sale = session.query(Sale).get(sales_id)
            if sale:
                return sale
            else:
                print(f"Tokio ID ({sales_id}) duomenų bazėje nėra.")
                return pasirinkti_sale()

def pasirinkti_rezisieriu():
    rezisieriu_perziura()
    try:
        rezisieriaus_id = int(input("Įveskite režisieriaus ID: "))
    except ValueError:
        print("\x1B[1mRežisieriaus ID turi būti skaičius.\x1B[0m")
        return pasirinkti_rezisieriu()
    else:
        if rezisieriaus_id:
            rezisierius = session.query(Rezisierius).get(rezisieriaus_id)
            if rezisierius:
                return rezisierius
            else:
                print(f"Tokio ID ({rezisieriaus_id}) duomenų bazėje nėra.")
                return pasirinkti_rezisieriu()

def pasirinkti_aktoriu():
    aktoriu_perziura()
    try:
        aktoriaus_id = int(input("Įveskite aktoriaus/ės ID: "))
    except ValueError:
        print("\x1B[1mAktoriaus/ės ID turi būti skaičius.\x1B[0m")
        return pasirinkti_aktoriu()
    else:
        if aktoriaus_id:
            aktorius = session.query(Aktorius).get(aktoriaus_id)
            if aktorius:
                return aktorius
            else:
                print(f"Tokio ID ({aktoriaus_id}) duomenų bazėje nėra.")
                return pasirinkti_aktoriu()

def pasirinkti_spektakli():
    spektakliu_perziura()
    try:
        spektaklio_id = int(input("Įveskite spektaklio ID: "))
    except ValueError:
        print("\x1B[1mSpektaklio ID turi būti skaičius.\x1B[0m")
        return pasirinkti_spektakli()
    else:
        if spektaklio_id:
            spektaklis = session.query(Spektaklis).get(spektaklio_id)
            if spektaklis:
                return spektaklis
            else:
                print(f"Tokio ID ({spektaklio_id}) duomenų bazėje nėra.")
                return pasirinkti_spektakli()


def pasirinkti_vaidmeni():
    vaidmenu_perziura()
    try:
        vaidmens_id = int(input("Įveskite vaidmens ID: "))
    except ValueError:
        print("\x1B[1mVaidmens ID turi būti skaičius.\x1B[0m")
        return pasirinkti_vaidmeni()
    else:
        if vaidmens_id:
            vaidmuo = session.query(Vaidmuo).get(vaidmens_id)
            if vaidmuo:
                return vaidmuo
            else:
                print(f"Tokio ID ({vaidmens_id}) duomenų bazėje nėra.")
                return pasirinkti_vaidmeni()

def atnaujinti_sale():
    sale = pasirinkti_sale()
    if sale:
        pavadinimas = input("Įveskite salės pavadinimą: ")
        adresas = input("Įveskite salės adresą: ")
        if len(pavadinimas) > 0:
            sale.pavadinimas = pavadinimas
        if len(adresas) > 0:
            sale.adresas = adresas
        session.commit()
        print(f"Salės duomenys {sale} atnaujinti sėkmingai.")

def atnaujinti_rezisieriu():
    rezisierius = pasirinkti_rezisieriu()
    if rezisierius:
        try:
            vardas = input("Įveskite režisieriaus vardą: ")
            pavarde = input("Įveskite režisieriaus pavardę: ")
            gimimo_data = datetime.strptime(input("Įveskite režisieriaus gimimo datą (YYYY-MM-DD): "), "%Y-%m-%d")
        except ValueError:
            gimimo_data = rezisierius.gimimo_data
        if len(vardas) > 0:
            rezisierius.vardas = vardas
        if len(pavarde) > 0:
            rezisierius.pavarde = pavarde
        if gimimo_data:
            rezisierius.gimimo_data = gimimo_data
        session.commit()
        print(f"Režisieriaus duomenys {rezisierius} atnaujinti sėkmingai.")

def atnaujinti_aktoriu():
    aktorius = pasirinkti_aktoriu()
    if aktorius:
        try:
            vardas = input("Įveskite aktoriaus/ės vardą: ")
            pavarde = input("Įveskite aktoriaus/ės pavardę: ")
            gimimo_data = datetime.strptime(input("Įveskite aktoriaus gimimo datą (YYYY-MM-DD): "), "%Y-%m-%d")
        except ValueError:
            gimimo_data = aktorius.gimimo_data
        if len(vardas) > 0:
            aktorius.vardas = vardas
        if len(pavarde) > 0:
            aktorius.pavarde = pavarde
        if gimimo_data:
            aktorius.gimimo_data = gimimo_data
        session.commit()
        print(f"Aktoriaus duomenys {aktorius} atnaujinti sėkmingai.")

def atnaujinti_spektakli():
    spektaklis = pasirinkti_spektakli()
    if spektaklis:
        try:
            pavadinimas = input("Įveskite spektaklio pavadinimą: ")
            sales = session.query(Sale).all()
            if len(sales) == 0:
                print("\x1B[1mSalių duomenų bazė tuščia\x1B[0m")
                return atnaujinti_spektakli()
            else:
                print("Salės: ")
                for sale in sales:
                    print("\t-", sale)
            sale_id = int(input("Įveskite salės ID: "))
        except ValueError:
            print("\x1B[1mBlogas pasirinkimas\x1B[0m")
            return atnaujinti_spektakli()
    sales_choice = session.query(Sale).get(sale_id)
    if sales_choice:
        session.commit()
    else:
        print("\x1B[1mTokio salės ID nėra.\x1B[0m")
        return ivesti_spektakli()
    rezisieriai = session.query(Rezisierius).all()
    if len(rezisieriai) == 0:
        print("\x1B[1mRežisierių duomenų bazė tuščia.\x1B[0m")
        return ivesti_spektakli()
    else:
        print("Režisieriai: ")
        for rezisierius in rezisieriai:
            print("\t-", rezisierius)
    try:
        rezisierius_id = int(input("Įveskite režisieriaus ID: "))  
    except ValueError:
        print("\x1B[1mBlogas režisieriaus ID, bandykite dar kartą.\x1B[0m")
        return atnaujinti_spektakli()
    rezisierius_choice = session.query(Rezisierius).get(rezisierius_id)
    if rezisierius_choice:
        session.commit()
    else:
        print("\x1B[1mTokio režisieriaus ID nėra.\x1B[0m")
        return atnaujinti_spektakli()
    if len(pavadinimas) > 0:
        spektaklis.pavadinimas = pavadinimas
    if sale_id:
        spektaklis.sale_id = sale_id
    if rezisierius_id:
        spektaklis.rezisierius_id = rezisierius_id
        session.commit()
        print(f"Spektaklio duomenys {spektaklis} atnaujinti sėkmingai.")



def atnaujinti_vaidmeni():
    role = pasirinkti_vaidmeni()
    if role:
        try:
            vaidmuo = input("Įveskite personažo vardą: ")
            aktoriai = session.query(Aktorius).all()
            if len(aktoriai) == 0:
                print("Aktorių duomenų bazė tuščia")
                return atnaujinti_vaidmeni()
            else:
                print("Aktoriai: ")
                for aktorius in aktoriai:
                    print("\t-", aktorius)
            aktorius_id = int(input("Įveskite aktoriaus ID: "))
        except ValueError:
            print("Blogas aktoriaus ID, bandykite dar kartą.")
            return atnaujinti_vaidmeni()
        aktorius_choice = session.query(Aktorius).get(aktorius_id)
        if aktorius_choice:
            session.commit()
        else:
            print("Tokio aktoriaus ID nėra.")
            return atnaujinti_vaidmeni()
        spektakliai = session.query(Spektaklis).all()
        if len(spektakliai) == 0:
            print("Spektaklių duomenų bazė tuščia.")
            return atnaujinti_vaidmeni()
        else:
            print("Spektakliai: ")
            for spektaklis in spektakliai:
                print("\t-", spektaklis)
        try:
            spektaklis_id = int(input("Įveskite spektaklio ID: "))  
        except ValueError:
            print("Blogas spektaklio ID, bandykite dar kartą.")
            return atnaujinti_vaidmeni()
        spektaklis_choice = session.query(Spektaklis).get(spektaklis_id)
        if spektaklis_choice:
            session.commit()
        else:
            print("Tokio spektkalio ID nėra.")
            return atnaujinti_vaidmeni()
        if len(vaidmuo) > 0:
            role.vaidmuo = vaidmuo
        if spektaklis_id:
            role.spektaklis_id = spektaklis_id

        if aktorius_id:
            role.aktorius_id = aktorius_id

            # aktorius = session.query(Aktorius).get(aktorius_id)
            # spektaklis = session.query(Spektaklis).get(spektaklis_id)
            # for spektaklis in aktorius.spektakliai:
            #     if spektaklis.id != role.spektaklis_id:
            #         aktorius.spektakliai[spektaklis_choice.id] = role.spektaklis_id
            # for aktorius in spektaklis.aktoriai:
            #     if aktorius.id != role.aktorius_id:
            #         spektaklis.aktoriai[aktorius_choice.id] = role.aktorius_id
    
            session.commit()
            print(f"Vaidmens duomenys {role} atnaujinti sėkmingai.")

def delete():
    print("Kuriuos Teatro duomenis norite ištrinti?")
    print("\t1 - salės.")
    print("\t2 - režisieriaus.")
    print("\t3 - aktoriaus.")
    print("\t4 - spektaklio.")
    print("\t5 - vaidmens.")
    try:
        choice = int(input("Pasirinkite: "))
        if choice > 5 or choice == 0:
            print("Tokio pasirinkimo nėra.")
            return delete()
        else:
            if choice == 1:
                sales = session.query(Sale).all()
                if len(sales) == 0:
                    print("Teatro salių duomenų bazė tuščia")
                else:
                    print("Salės: ")
                    for sale in sales:
                        print("\t-", sale)
                try:
                    sale_pasirinkimas = int(input("Įveskite salės ID:"))
                    trinama_sale = session.query(Sale).get(sale_pasirinkimas)
                    if trinama_sale:
                        session.delete(trinama_sale)
                        session.commit()
                        print(f"Salė {trinama_sale} -- sėkmingai ištrinta.")
                    else:
                        print("\x1B[1mTokio salės ID duomenų bazėje nėra.\x1B[0m")
                        return delete()
                except ValueError:
                    print("Salės ID gali būti tik \x1B[1mSKAIČIUS\x1B[0m.")
                    return delete()
            if choice == 2:
                rezisieriai = session.query(Rezisierius).all()
                if len(rezisieriai) == 0:
                    print("Režisierių duomenų bazė tuščia.")
                else:
                    print("Režisieriai/ės: ")
                    for rezisierius in rezisieriai:
                        print("\t-", rezisierius)
                try:
                    rezisierius_pasirinkimas = int(input("Įveskite režisieriaus/ės ID: "))
                    trinamas_rezisierius = session.query(Rezisierius).get(rezisierius_pasirinkimas)
                    if trinamas_rezisierius:
                        session.delete(trinamas_rezisierius)
                        session.commit()
                        print(f"Režisierius {trinamas_rezisierius} -- sėkmingai ištrintas/a.")
                    else:
                        print("\x1B[1mTokio režisieriaus ID duomenų bazėje nėra.\x1B[0m")
                        return delete()
                except ValueError:
                    print("Režisieriaus ID gali būti tik \x1B[1mSKAIČIUS\x1B[0m.")
                    return delete()
            if choice == 3:
                aktoriai = session.query(Aktorius).all()
                if len(aktoriai) == 0:
                    print("Aktorių duomenų bazė tuščia.")
                else:
                    print("Aktoriai/ės: ")
                    for aktorius in aktoriai:
                        print("\t-", aktorius)
                try:
                    aktorius_pasirinkimas = int(input("Įveskite aktoriaus/ės ID: "))
                    trinamas_aktorius = session.query(Aktorius).get(aktorius_pasirinkimas)
                    if trinamas_aktorius:
                        for spektaklis in trinamas_aktorius.spektakliai:
                            trinamas_aktorius.spektakliai.remove(spektaklis)
                        session.delete(trinamas_aktorius)
                        session.commit()
                        print(f"Aktorius/ė {trinamas_aktorius} -- sėkmingai ištrintas/a.")
                    else:
                        print("\x1B[1mTokio aktoriaus/ės ID duomenų bazėje nėra.\x1B[0m")
                        return delete()
                except ValueError:
                    print("Aktoriaus ID gali būti tik \x1B[1mSKAIČIUS\x1B[0m.")
                    return delete()

            if choice == 4:
                spektakliai = session.query(Spektaklis).all()
                if len(spektakliai) == 0:
                    print("Spektaklių duomenų bazė tuščia.")
                else:
                    print("Spektakliai: ")
                    for spektaklis in spektakliai:
                        print("\t-", spektaklis)
                try:
                    spektaklis_pasirinkimas = int(input("Įveskite spektaklio ID: "))
                    trinamas_spektkalis = session.query(Spektaklis).get(spektaklis_pasirinkimas)
                    if trinamas_spektkalis:
                        for aktorius in trinamas_spektkalis.aktoriai:
                            trinamas_spektkalis.aktoriai.remove(aktorius)
                        session.delete(trinamas_spektkalis)
                        session.commit()
                        print(f"Spektaklis {trinamas_spektkalis} -- sėkmingai ištrintas/a.")
                    else:
                        print("\x1B[1mTokio spektaklio ID duomenų bazėje nėra.\x1B[0m")
                        return delete()
                except ValueError:
                    print("Spektaklio ID gali būti tik \x1B[1mSKAIČIUS\x1B[0m.")
                    return delete()
            
            if choice == 5:
                vaidmenys = session.query(Vaidmuo).all()
                if len(vaidmenys) == 0:
                    print("Vaidmenų duomenų bazė tuščia.")
                else:
                    print("Vaidmenys: ")
                    for vaidmuo in vaidmenys:
                        print("\t-", vaidmuo)
                try:
                    vaidmuo_pasirinkimas = int(input("Įveskite vaidmenio ID: "))
                    trinamas_vaidmuo = session.query(Vaidmuo).get(vaidmuo_pasirinkimas)
                    if trinamas_vaidmuo:
                        aktorius = session.query(Aktorius).get(trinamas_vaidmuo.aktorius_id)
                        spektaklis = session.query(Spektaklis).get(trinamas_vaidmuo.spektaklis_id)
                        for spektaklis in aktorius.spektakliai:
                            if spektaklis.id == trinamas_vaidmuo.spektaklis_id:
                                aktorius.spektakliai.remove(spektaklis)
                        for aktorius in spektaklis.aktoriai:
                            if aktorius.id == trinamas_vaidmuo.aktorius_id:
                                spektaklis.aktoriai.remove(aktorius)
                        session.delete(trinamas_vaidmuo)
                        session.commit()
                        print(f"Vaidmuo {trinamas_vaidmuo} -- sėkmingai ištrintas/a.")
                    else:
                        print("\x1B[1mTokio vaidmens ID duomenų bazėje nėra.\x1B[0m")
                        return delete()
                except ValueError:
                    print("Vaidmens ID gali būti tik \x1B[1mSKAIČIUS\x1B[0m.")
                    return delete()          
    except ValueError:
        print("Įveskite 1/2/3. Įvedėte tai, ko nėra pasirinkime.")

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
                    atnaujinti_sale()
                if pasirinkimas3 == 2:
                    atnaujinti_rezisieriu()
                if pasirinkimas3 == 3:
                    atnaujinti_aktoriu()
                if pasirinkimas3 == 4:
                    atnaujinti_spektakli()
                if pasirinkimas3 == 5:
                    atnaujinti_vaidmeni()
            except ValueError:
                print("Įveskite 1/2/3/4/5. Įvedėte tai, ko nėra pasirinkime.")
        if choice == 4:
            delete()
        if choice == 0:
            print("Išėjote")
            break
    except ValueError:
        print("Įveskite 0/1/2/3/4. Įvedėte tai, ko nėra pasirinkime.")