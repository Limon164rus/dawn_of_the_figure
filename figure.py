import math
a=str(input('������� �������� ������:'))
if a=='�����������':
    a=float(input('������� ������� a:'))
    b=float(input('������� ������� b:'))
    c=float(input('������� ������� c:'))
    P=(a+b+c)/2
    print(P)
elif a=='�������������':
    a=float(input('������� ������� a:'))
    b=float(input('������� ������� b:'))
    S=a*b
    print(S)
elif a=='����':
    r=float(input('������� ������:'))
    S=math.pi*pow(r,2)
    print(S)