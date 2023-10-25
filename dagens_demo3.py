class Bankkonto:
    ...

def sätt_in_pengar(summa:int, bankkonto:Bankkonto) -> None:
    """Måste vara positivt!!!"""
    # if summa < 0:
    #     raise NegativNumberError
    
    bankkonto.konto = summa


class NegativNumberError(Exception):
    ...

while True:
    try:
        y = int(input('Mata in ett heltal: '))
        if y < 0:
            raise NegativNumberError
        else:
            x = 1/y
            break
    except ZeroDivisionError as messag:
        print('Vi försökte dela med noll!')
    except ValueError:
        print('Du använde inte siffror!')
    except NegativNumberError:
        print('Inga negativa tal tack!!')
    except KeyboardInterrupt:
        print('Okej, vi stänger ner!!!')
        break
    except EOFError:
        print('Du terminerade programmet')
        break
    except AssertionError:
        print('????')
    except TypeError:
        print('Något konstigt fel')
    # except:
    #     print('Något galet har skett!!!')
    # else:
    #     print('Vi kör else-blocket')
    # finally:
    #     print('Jag körs alltid oavsätt fel!!!')