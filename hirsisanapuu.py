def hirsipuu():
    sana = "kultainennoutaja"
    arvattu = []
    yritykset = 10

    print("Tervetuloa hirsipuupeliin!")
    print("_ " * len(sana))

    while yritykset > 0:
        arvaus = input("Arvaa kirjain: ").lower()
# Tarkistetaan, että syöte on yksi kirjain
        if not arvaus.isalpha() or len(arvaus) != 1:
            print("Anna yksi kirjain.")
            continue
# Tarkistetaan, onko kirjain jo arvattu
        if arvaus in arvattu:
            print("Olet jo arvannut tämän kirjaimen.")
            continue

        arvattu.append(arvaus) # Lisätään arvaus listaan
# Tarkistetaan, onko arvaus sanassa
        if arvaus in sana:
            print("Oikein!")
        else:
            yritykset -= 1 # Vähennetään yrityksiä, jos väärä arvaus
            print(f"Väärin! Yrityksiä jäljellä: {yritykset}")
# Rakennetaan tulostettava sana arvattujen kirjainten perusteella
        tulos = ""
        for kirjain in sana:
            if kirjain in arvattu:
                tulos += kirjain + " " # Näytetään arvattu kirjain
            else:
                tulos += "_ " # Muuten näytetään alaviiva

        print(tulos) # Tulostetaan nykyinen sanan tila
# Tarkistetaan, onko pelaaja arvannut koko sanan
        if "_" not in tulos:
            print("Onneksi olkoon! Arvasit sanan.")
            break # Lopetetaan peli
    else:
        # Tämä else-haara suoritetaan, jos while-silmukka päättyy ilman break:ia
        print(f"Hävisit! Oikea sana oli: {sana}")
# Suoritetaan peli vain jos tiedosto suoritetaan suoraan
if __name__ == "__main__":
    hirsipuu()
