def Hipotenusa(a, b):
    hipotenusa = a*a + b*b
    return hipotenusa

def soma_hipotenusas(n):
    c = 1
    soma = 0
    while c <= n:
        c2 = c*c       
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (c2 == Hipotenusa(a, b)):
                    soma = soma + c
                    a = n
                    break
                b = b + 1
            a = a + 1
            b = a
        c = c + 1   
    return soma

