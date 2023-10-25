

while True:

    try:
        inp = input('Mata in något!')
        float(inp)

    except:
        print('Fånga felet!!')

    if inp == 'q':break
