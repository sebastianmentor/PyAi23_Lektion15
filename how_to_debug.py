def call_func() -> None:
    sträng = "hej"
    func(sträng)


def func(a) -> None:
    print(a)


def swapp(a,b) -> tuple:
    return b,a


if __name__ == "__main__":
    call_func()
    var1 = 10
    var2 = '10'

    var1, var2 = swapp(var1, var2)

    print(type(var1), type(var2))