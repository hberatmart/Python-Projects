boyut = int(input("bir değer giriniz: "))
def func(out):
    bs = boyut // 2
    inn = 1
    while inn <= out:
        print(" " * bs + "*" * inn )
        bs -= 1
        inn += 2
    inn = out - 2
    bs = 1
    while inn > 0 :
        print(" " * bs + "*" * inn)
        bs += 1
        inn -= 2
func(boyut)