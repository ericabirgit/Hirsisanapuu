def hirsipuu():
    sana = "kultainennoutaja"
    arvattu = []
    yritykset = 10

    print("Tervetuloa hirsipuupeliin!")
    print("_ " * len(sana))
// dasdasd
    while yritykset > 0:
        arvaus = input("Arvaa kirjain: ").lower()

        if not arvaus.isalpha() or len(arvaus) != 1:
            print("Anna yksi kirjain.")
            continue

        if arvaus in arvattu:
            print("Olet jo arvannut tämän kirjaimen.")
            continue

        arvattu.append(arvaus)

        if arvaus in sana:
            print("Oikein!")
        else:
            yritykset -= 1
            print(f"Väärin! Yrityksiä jäljellä: {yritykset}")

        tulos = ""
        for kirjain in sana:
            if kirjain in arvattu:
                tulos += kirjain + " "
            else:
                tulos += "_ "

        print(tulos)

        if "_" not in tulos:
            print("Onneksi olkoon! Arvasit sanan.")
            break
    else:
        print(f"Hävisit! Oikea sana oli: {sana}")

if __name__ == "__main__":
    hirsipuu()
