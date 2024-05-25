class Main:
    while True:
        try:
            value = float(input("Zadejte pouze číselnou hodnotu na převod: "))
            valueToPrint = str(value)
            break
        except:
            print("\n!! Špatně zadaná hodnota, prosím zadejte pouze číselnou hodnotu. !!\n")
    unit = str()

    while True:
        whichUnits = input("Do jakého systému si přejete převést hodnotu? [B]ritského/[M]etrického\n").upper()
        if whichUnits == "B":
            while not unit:
                unit = input("Zadejte, v jakých jednotkách je hodnota: [mm] [cm] [dm] [m] [km]").lower()
                match unit:
                    case "mm":
                        value /= 10
                    case "cm":
                        pass
                    case "dm":
                        value *= 10
                    case "m":
                        value *= 100
                    case "km":
                        value *= 100000
                    case _:
                        unit = str()
                        print(
                            "\n!! Zadejte prosím zkratku jednotek, ve kterých je hodnota [mm] [cm] [dm] [m] [km] !!\n")
            print(valueToPrint + " " + unit + " je " + str(round(value / 2.54, 2)) + " palců, " + str(
                round(value / 30.48, 2)) + " stop, " + str(round(value / 91.44, 2)) + " yardů a " + str(
                round(value / 160934, 5)) + " mil.")
            break
        elif whichUnits == "M":
            while not unit:
                unit = input("Zadejte, v jakých jednotkách je hodnota: [in] [ft] [yd] [mi]").lower()
                match unit:
                    case "in":
                        value /= 12
                    case "ft":
                        pass
                    case "yd":
                        value *= 3
                    case "mi":
                        value *= 5280
                    case _:
                        unit = str()
                        print("\n!! Zadejte prosím zkratku jednotek, ve kterých je hodnota [in] [ft] [yd] [mi] !!\n")
            print(valueToPrint + " " + unit + " je " + str(round(value * 304.8, 2)) + " milimetrů, " + str(
                round(value * 30.48, 2)) + " centimetrů, " + str(
                round(value * 3.048, 2)) + " decimetrů, " + str(
                round(value * 0.3048, 5)) + " metrů a " + str(
                round(value * 0.0003048, 5)) + " kilometrů.")
            break
        else:
            print("\n!! Špatně zadaný indikátor pro výběr systému. Zadejte prosím buď [B]ritský nebo [M]etrický "
                  "systém. !!\n")
