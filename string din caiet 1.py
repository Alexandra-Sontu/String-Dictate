"""se citeste un cuvant si o litera
sa se afiseze:
cuvintul inlocuit prin inlocuirea fiecarui caracter al cuvantului cu litera data."""
x=str(input("introdu cuvantul:"))
y=str(input("introdu litera:"))
for i in x:
    z=x.replace(i,y)
    print(z)