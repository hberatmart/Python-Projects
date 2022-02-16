dimension = int(input("bir değer giriniz: "))

def number_of_square(dmn):
    a = dmn
    while a > 0:
        print("*" * dmn)
        a -= 1
number_of_square(dimension)