# x = 1/0
# print(x)

while True:
    try:
        y = int(input('Mata in ett heltal: '))
        if y <= 0:
            print('Du skrev inte in ett positivt tal!')
        else:
            x = 1/y
            print(x)
            break
    # except ZeroDivisionError:
    #     print('Vi försökte dela med noll!')
    except ValueError:
        print('Du använde inte siffror!')
    else:
        print('Vi kör else-blocket')
    finally:
        print('Jag körs alltid oavsätt fel!!!')