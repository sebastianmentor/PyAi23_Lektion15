class ZeroValueError(Exception):
    ...


def divide_a_by_b(a:float, b:float) -> float:
    return a/b

if __name__ == "__main__":
    while True:
        
        print('Dela 2 tal')
        try:
            a = float(input('Välj tal att dela: '))
            b = float(input('Välj tal att dela med: '))
            # if b == 0:
            #     raise ZeroValueError

        except ValueError:
            print('Måste va en float!! ex 2.523 eller 34')

        except ZeroValueError:
            print('Nu skulle du dela med noll och universum skulle explodera!!')

        else:
            # try:
            #     print(divide_a_by_b(a,b))
            # except ZeroDivisionError:
            #     print('Går inte att dela med noll!!!')

            if b == 0:
                print('Du försöker dela med noll!!')
                continue

            print(divide_a_by_b(a,b))

        finally:
            # print('Kommer alltid att köras oavsätt vad som händer!!!')
            q = input('Är du färdig? Skriv q i sådana fall!!! >>>')
            if q =='q':break