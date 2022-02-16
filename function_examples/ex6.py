berat = int(input("bir değer giriniz: "))
def func(brt):
    a = 1
    while a <= brt:
        print("*" * a)
        a += 1
    a = brt-1
    while a > 0:
        print("*" * a)
        a -= 1
func(berat)