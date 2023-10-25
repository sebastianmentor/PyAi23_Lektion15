
def är_heltal(tal:str) -> bool:
    if len(tal)>=2 and tal[0] == '-' and tal[1:].isdigit():
        return True
    if tal.isdigit(): 
        return True
        
    return False



while True:
    y = input('Mata in ett positivt heltal: ')
    if är_heltal(y):
        y = int(y)
        if y <= 0:
            print('Du skrev inte in ett positivt tal!')
        else:
            x = 1/y
            print(x)
            break
    else:
        print('Du skrev inte in ett tal!!')