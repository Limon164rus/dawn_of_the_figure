import math
a=str(input('Введите название фигуры:'))
if a=='Треугольник':
    a=float(input('Введите сторону a:'))
    b=float(input('Введите сторону b:'))
    c=float(input('Введите сторону c:'))
    P=(a+b+c)/2
    print(P)
elif a=='Прямоугольник':
    a=float(input('Введите сторону a:'))
    b=float(input('Введите сторону b:'))
    S=a*b
    print(S)
elif a=='Круг':
    r=float(input('Введите градиус:'))
    S=math.pi*pow(r,2)
    print(S)
