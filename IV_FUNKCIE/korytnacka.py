"""
Na spustenie treba tento kod ulozit ako skript
napr. do suboru test.py v adresesári ktorý máte 
nastavený v Git Bash. Keď sa vytvorí kresliace okno , 
tak do terminálového okna za šípku treba zadavat 
jednotlivé kombinácie hodnôt (smer počet_bodov) 
kam sa má posunúť koryrnačka (šípka):
"""

import turtle   # import grafickeho modulu

def vykonaj():
    t = turtle.Turtle()  # vytvorenie grafickej plochy
    p = {'fd': t.fd, 'rt': t.rt, 'lt': t.lt} # pozicia sipky
    while True:
        prikaz, parameter = input('> ').split() # vstup smeru pohybu a hodnot o kolko napr. fd o 100 
        p[prikaz](int(parameter))

vykonaj()   # volanie funkcie bez parametrov

# Priklad vstupnych dvojic hodnot:
# > fd 100  kde fd je skrateny zapis posunuforward
# > lt 90   kde lt je skrateny zapis natocenia uhlu left
# > fd 50   
# > rt 60   kde fd je skrateny zapis natocenia uhlu right
# > fd 100  

