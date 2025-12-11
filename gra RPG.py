
import random
import time



def pauza():
    time.sleep(1)

def linia():
    print("-" * 50)

def wybor_opcji(ile):
    while True:
        try:
            x = int(input("> "))
            if 1 <= x <= ile:
                return x
        except:
            pass
        print("Wpisz numer od 1 do", ile)


def stworz_postac():
    linia()
    print("Witaj w PROSTEJ GRZE RPG!")
    imie = input("Podaj imię postaci: ")

    linia()
    print("Wybierz klasę:")
    print("1. Wojownik")
    print("2. Mag")

    wybor = wybor_opcji(2)

    postac = {
        "imie": imie,
        "poziom": 1,
        "exp": 0,
        "zloto": 0
    }

    if wybor == 1:
        postac["klasa"] = "Wojownik"
        postac["max_hp"] = 30
        postac["hp"] = 30
        postac["sila"] = 6
        postac["zrecznosc"] = 4
        postac["mana"] = 0
        postac["max_mana"] = 0

    else:
        postac["klasa"] = "Mag"
        postac["max_hp"] = 18
        postac["hp"] = 18
        postac["sila"] = 3
        postac["zrecznosc"] = 3
        postac["mana"] = 20
        postac["max_mana"] = 20

    print(f"Rozpoczynasz przygodę jako {postac['imie']} ({postac['klasa']})!")
    pauza()

    return postac


def pokaz_statystyki(postac):
    linia()
    print(f"Statystyki postaci: {postac['imie']}")
    print("Klasa:", postac["klasa"])
    print("Poziom:", postac["poziom"])
    print("HP:", postac["hp"], "/", postac["max_hp"])
    print("Mana:", postac["mana"], "/", postac["max_mana"])
    print("Siła:", postac["sila"])
    print("Zręczność:", postac["zrecznosc"])
    print("Doświadczenie:", postac["exp"])
    print("Złoto:", postac["zloto"])
    linia()



def dodaj_exp(postac, ile):
    print(f"+{ile} EXP!")
    postac["exp"] += ile

    if postac["exp"] >= postac["poziom"] * 20:
        postac["poziom"] += 1
        postac["exp"] = 0
        postac["max_hp"] += 5
        postac["hp"] = postac["max_hp"]
        postac["sila"] += 1
        postac["zrecznosc"] += 1
        postac["max_mana"] += 2
        postac["mana"] = postac["max_mana"]
        print("AWANS NA WYŻSZY POZIOM!")
        pauza()


def atak_postaci(postac):
    return random.randint(postac["sila"], postac["sila"] + 4)

def unik_postaci(postac):
    return random.randint(0, postac["zrecznosc"])



def losowy_przeciwnik():
    lista = [
        ("Goblin", 10, 4, 5, 10),
        ("Wilk", 12, 5, 6, 12),
        ("Bandzior", 15, 6, 8, 14),
        ("Szkielet", 14, 5, 10, 15)
    ]

    w = random.choice(lista)

    przeciwnik = {
        "nazwa": w[0],
        "hp": w[1],
        "max_hp": w[1],
        "sila": w[2],
        "zloto": w[3],
        "exp": w[4]
    }

    return przeciwnik

def atak_przeciwnika(przeciwnik):
    return random.randint(przeciwnik["sila"] - 1, przeciwnik["sila"] + 2)



def walka(postac, przeciwnik):
    linia()
    print(f"Napotkałeś przeciwnika: {przeciwnik['nazwa']}")
    pauza()

    while postac["hp"] > 0 and przeciwnik["hp"] > 0:
        linia()
        print(f"{postac['imie']}: {postac['hp']}/{postac['max_hp']} HP")
        print(f"{przeciwnik['nazwa']}: {przeciwnik['hp']}/{przeciwnik['max_hp']} HP")
        linia()

        print("1. Atak")
        print("2. Unik")
        print("3. Leczenie (tylko Mag)")
        print("4. Ucieczka")

        wybor = wybor_opcji(4)

        if wybor == 1:
            dmg = atak_postaci(postac)
            przeciwnik["hp"] -= dmg
            print(f"Zadałeś {dmg} obrażeń!")

        elif wybor == 2:
            if unik_postaci(postac) > random.randint(2,6):
                print("Uniknięto ataku!")
                continue
            else:
                print("Nie udało się uniknąć!")

        elif wybor == 3:
            if postac["klasa"] == "Mag" and postac["mana"] >= 5:
                postac["mana"] -= 5
                leczenie = random.randint(6,12)
                postac["hp"] = min(postac["max_hp"], postac["hp"] + leczenie)
                print("Wyleczono:", leczenie)
            else:
                print("Nie możesz się leczyć.")
                continue

        elif wybor == 4:
            if random.random() < 0.5:
                print("Uciekłeś!")
                return
            else:
                print("Nie udało się uciec!")

        if przeciwnik["hp"] > 0:
            dmg = atak_przeciwnika(przeciwnik)
            postac["hp"] -= dmg
            print("Przeciwnik zadał ci", dmg, "obrażeń.")

        pauza()

    if postac["hp"] <= 0:
        print("Zostałeś pokonany...")
        exit()

    print(f"Pokonałeś {przeciwnik['nazwa']}!")
    postac["zloto"] += przeciwnik["zloto"]
    dodaj_exp(postac, przeciwnik["exp"])
    pauza()


def sklep(postac):
    linia()
    print("Witaj w sklepie!")
    print("Złoto:", postac["zloto"])
    print("1. Mikstura życia (+10 HP) — 5 złota")
    print("2. Mikstura many (+5 many) — 5 złota")
    print("3. Wyjdź")

    wybor = wybor_opcji(3)

    if wybor == 1:
        if postac["zloto"] >= 5:
            postac["zloto"] -= 5
            postac["hp"] = min(postac["max_hp"], postac["hp"] + 10)
            print("Kupiono miksturę życia.")
        else:
            print("Za mało złota.")

    elif wybor == 2:
        if postac["zloto"] >= 5 and postac["klasa"] == "Mag":
            postac["zloto"] -= 5
            postac["mana"] = min(postac["max_mana"], postac["mana"] + 5)
            print("Kupiono miksturę many.")
        else:
            print("Nie możesz kupić.")

    elif wybor == 3:
        return

    pauza()



def miasto(postac):
    while True:
        linia()
        print("== MIASTO ==")
        print("1. Sklep")
        print("2. Odpocznij (pełne HP i mana)")
        print("3. Statystyki")
        print("4. Wyjście z miasta")

        wybor = wybor_opcji(4)

        if wybor == 1:
            sklep(postac)
        elif wybor == 2:
            postac["hp"] = postac["max_hp"]
            postac["mana"] = postac["max_mana"]
            print("Wypocząłeś!")
            pauza()
        elif wybor == 3:
            pokaz_statystyki(postac)
        else:
            return


def gra():
    postac = stworz_postac()

    while True:
        linia()
        print("== MENU GŁÓWNE ==")
        print("1. Wyrusz na przygodę")
        print("2. Idź do miasta")
        print("3. Statystyki")
        print("4. Zakończ grę")

        wybor = wybor_opcji(4)

        if wybor == 1:
            przeciwnik = losowy_przeciwnik()
            walka(postac, przeciwnik)
        elif wybor == 2:
            miasto(postac)
        elif wybor == 3:
            pokaz_statystyki(postac)
        else:
            print("Dzięki za grę!")
            break



gra()

