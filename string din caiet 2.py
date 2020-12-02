"""Un sir de caractere introdus de la tastura trebuie
  sa reprezinte numele si prenumele unei persoane, initialele 
 scrise cu majuscule, celelalte caractere fiind litere mici. 
 Stabiliti daca sirul dat este un nume corect de persoana"""
import string
x=str(input("dati un nume:"))
y=x.title()
if x==y:
print("poate fi un nume")
else:
    print("nu poate fi un nume")