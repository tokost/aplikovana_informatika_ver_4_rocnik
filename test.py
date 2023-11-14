import turtle

def vykonaj():
    t = turtle.Turtle()
    p = {'fd': t.fd, 'rt': t.rt, 'lt': t.lt}
    while True:
        prikaz, parameter = input('> ').split()
        p[prikaz](int(parameter))


vykonaj()


# Vysledok je :
# > fd 100  kde fd je skrateny zapis forward
# > lt 90   kde lt je skrateny zapis left
# > fd 50   kde fd je skrateny zapis forward
# > rt 60   kde fd je skrateny zapis right
# > fd 100  kde fd je skrateny zapis forward

