# Better to ask for forgivness the premision!

while True:
    tal = input("Vänligen mata in ett positivt tal: ")

    try:
        heltal = int(tal)

    except ValueError:
        print("Inte ett giltligt heltal!")

    else:
        if heltal < 0:
            print("Det där var ett negativt tal")
            
        else:
            print("Korrekt inmatat")
            break