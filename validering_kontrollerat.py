# Ett program som kontrollerar att användaren matar in korrekt

print("********Meny*********")
print("* 1. Gör något      *")
print("* 2. Gör något annat*")
print("* 3. Avsluta        *")
print("*********************")
val = input(">>>")

if val == "1" or val == "2" or val == "3":
    print("Vi kontrollerade varje fall individuellt")

if "1"<= val <="3":
    print("Vi kontrollera ett span!")

giltligt_menyval = {"1","2","3"}

if val in giltligt_menyval:
    print("Vi kontrollerade att det fanns i en mängd")