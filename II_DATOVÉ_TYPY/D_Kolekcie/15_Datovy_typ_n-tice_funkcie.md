# n-tice (tuple)
Sú to vlastne len nemeniteľné (**immutable**) zoznamy. 

Pythonovský typ tuple dokáže robiť skoro všetko to isté ako list okrem mutable operácií. Takže to najprv zhrňme a potom si ukážeme, ako to pracuje:

* operácia + na zreťazovanie (spájanie dvoch n-tíc)

* operácia * na viacnásobné zreťazovanie (viacnásobné spájanie jednej n-tice)

* operácia in na zisťovanie, či sa nejaká hodnota nachádza v n-tici

* operácia indexovania [i] na zistenie hodnoty prvku na zadanom indexe

* operácia rezu [i:j:k] na zistenie hodnoty nejakej podčasti n-tice

* relačné operácie ==, !=, <, <=, >, >= na porovnávanie obsahu dvoch n-tíc

* metódy count() a index() na zisťovanie počtu výskytov, resp. indexu prvého výskytu

* prechádzanie n-tice pomocou for-cyklu (iterovanie)

* štandardné funkcie len(), sum(), min(), max() ktoré zisťujú niečo o prvkoch n-tice

Takže n-tice, tak ako aj zoznamy sú štruktúrované typy, t.j. sú to typy, ktoré obsahujú hodnoty nejakých (možno rôznych) typov (sú to tzv. kolekcie):

* konštanty typu n-tica uzatvárame do okrúhlych zátvoriek a navzájom oddeľujeme čiarkami

* funkcia len() vráti počet prvkov n-tice, napríklad:

~~~
stred = (150, 100)
zviera = ('slon', 2013, 'gray')

print(stred)
    (150, 100)

print(zviera)
    ('slon', 2013, 'gray')

nic = ()
print(nic)
    ()

len(stred)
    2

len(zviera)
    3

len(nic)
    0

type(stred)
    <class 'tuple'>
~~~
Vidíte, že n-tica môže byť aj prázdna, označujeme ju **()** a vtedy má počet prvkov 0 (teda len(()) je 0). Ak n-tica nie je prázdna, hodnoty sú navzájom oddelené čiarkami.

> ## n-tica s jednou hodnotou
Pre jednoprvkovú n-ticu musíme do zátvoriek zapísať aj čiarku:
~~~
p = (12,)

print(p)
    (12,)

len(p)
    1

type(p)
    <class 'tuple'>
~~~
n-ticu s jednou hodnotou teda nemôžeme zapísať takto:
~~~
p = (12)

print(p)
    12

type(p)
    <class 'int'>
~~~
**Ak zapíšeme ľubovoľnú hodnotu do zátvoriek, nie je to n-tica (v našom prípade je to len jedno celé číslo).**

> ## Pre Python sú dôležitejšie čiarky ako zátvorky. V mnohých prípadoch si Python zátvorky domyslí (čiarky si nedomyslí nikdy):
~~~
stred = 150, 100
zviera = 'slon', 2013, 'gray'
p = 12,

print(stred)
(150, 100)

print(zviera)
('slon', 2013, 'gray')

print(p)
(12,)
~~~
Aj na tomto príklade vidíme význam a funkciu čiarok. Našli ste ste rozdiel medzi premennými **a** a **b** ?
~~~
a = 3.14
b = 3,14

print(a, type(a))
    3.14 <class 'float'>

print(b, type(b))
    (3, 14) <class 'tuple'>
~~~


> ## Funkcia tuple()
Vyrobí n-ticu z ľubovoľnej postupnosti (z iterovateľného objektu, t.j. takého objektu, ktorý sa dá prechádzať for-cyklom), napríklad zo znakového reťazca, zo zoznamu, vygenerovanej postupnosti celých čísel pomocou range(), ale iterovateľný je aj otvorený textový súbor. Znakový reťazec funkcia tuple() rozoberie na znaky:
~~~
tuple = tuple('Python')
print(tuple)

('P', 'y', 't', 'h', 'o', 'n')
~~~
n-tice môžeme vytvoriť aj pomocou funkcie range():
~~~
rozsah = tuple(range(1, 16))
print(rozsah)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

a = tuple(range(1000000))
print(len(a))
1000000
~~~
Podobne môžeme skonštruovať n-ticu z textového súboru. Predpokladajme, že súbor styri_riadky.txt obsahuje tieto 4 riadky:
~~~
prvy
druhy
treti
stvrty

potom
with open('C:\\Users\\tomast\\Documents\\sss-trencin\\Vyuka\Aplikovana_Informatika\\11_hodina\\styri_riadky.txt', encoding="utf-8") as t:
    obsah = tuple(t)
print(obsah)

('prvy\n', 'druhy\n', 'treti\n', 'stvrty\n')
~~~
Kedy riadky súboru styri_riadky.txt sa postupne stanú prvkami n-tice.

> ## for-cyklus s n-ticami
for-cyklus je programová konštrukcia, ktorá postupne prechádza všetky prvky nejakého **iterovateľného** objektu. Doteraz sme sa stretli s iterovaním pomocou funkcie range(), prechádzaním prvkov reťazca str a zoznamu list, aj celých riadkov textového súboru. Ale už sme sa tiež možno stretli aj s takýmto zápisom:
~~~
for i in 2, 3, 5, 7, 11, 13:
    print('prvocislo', i)
~~~
V tomto zápise už teraz vidíme n-ticu (tuple): 2, 3, 5, 7, 11, 13. Len sme tomu nemuseli dávať zátvorky. Keďže aj n-tica je iterovateľný objekt, Môžeme ju používať vo for-cykle rovnako ako iné iterovateľné typy. To isté, ako v predchádzajúcom príklade, by sme mohli zapísať napríklad aj takto:
~~~
cisla = (2, 3, 5, 7, 11, 13)
for i in cisla:
    print('prvocislo', i)
~~~
Keď sa naučíme manipulovať s n-ticami a používať funkciu cyklu (opakovania), môžeme zapísať aj takýto príklad:
~~~
rozne = ('retazec', (100, 200), 3.14, len)
for prvok in rozne:
        print(prvok, type(prvok))
    retazec <class 'str'>
    (100, 200) <class 'tuple'>
    3.14 <class 'float'>
    <built-in function len> <class 'builtin_function_or_method'>
~~~
Na ktorom vidíme, že **prvkami n-tice môžu byť najrôznejšie objekty a aj funkcie** (tu je to štandardná funkcia len).

Pomocou operácií s n-ticami vieme zapísať aj zaujímavejšie postupnosti čísel, napríklad:
~~~
for i in 10 * (1,):
    print(i, end=' ')

1 1 1 1 1 1 1 1 1 1

for i in 10 * (1, 2):
    print(i, end=' ')

1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2

for i in 10 * tuple(range(10)):
    print(i, end=' ')

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2
3 4 5 6 7 8 9

for z in 'Python':
    print(z, end=' ')

P y t h o n

for z in 'Python',:
    print(z, end=' ')

Python
~~~
Ďalej pomocou for-cyklu vieme n-tice skladať podobne, ako sme to robili so zoznamami. V nasledovnom príklade vytvoríme n-ticu zo všetkých deliteľov nejakého čísla:
~~~
cislo = int(input('zadaj cislo: '))
delitele = ()
for i in range(1, cislo+1):
    if cislo % i == 0:
        delitele = delitele + (i,)  # pridanie jeneho prvku
print('delitele', cislo, 'su', delitele)
~~~
a po spustení tohoto kódu dostaneme
~~~
zadaj cislo: 124  # po stlaceni Enter dostaneme vysledok

delitele 124 su (1, 2, 4, 31, 62, 124)
~~~
Všimnite si, ako sme pridali jeden prvok na koniec n-tice: delitele = delitele + (i,). Museli, sme vytvoriť jednoprvkovú n-ticu (i,) a tú sme zreťazili s pôvodnou n-ticou delitele. Mohli sme to zapísať aj takto: delitele += (i,). Keby sme ale túto úlohu riešili pomocou zoznamov, použili by sme metódu append().

> ## Funkcia enumerate()

Funkcie enumerate() už poznáme zo zoznamov a keďže sme povedali že tuple je inmutable zoznam tak použitie tejto funkcie aj v tomto prípade je logické. Pre n-tice ju opäť s pomocou cyklu využijeme napr. takto:
~~~
zoz = (2, 3, 5, 7, 9, 11, 13, 17, 19)
for ix, pr in enumerate(zoz):
    print(f'{ix}. prvocislo je {pr}') # novy prvok syntaxe - formatovanie vypysu s pouzitim hodnot parametrov

Vysledok:
0. prvocislo je 2
1. prvocislo je 3
2. prvocislo je 5
3. prvocislo je 7
4. prvocislo je 9
5. prvocislo je 11
6. prvocislo je 13
7. prvocislo je 17
8. prvocislo je 19
~~~
Funkcia enumerate() v skutočnosti z jednej ľubovoľnej postupnosti vygeneruje postupnosť dvojíc (ktoré sú už typu tuple). Túto postupnosť ďalej preliezame for-cyklom. Mohli by sme to zapísať aj takto:
~~~
zoz = (2, 3, 5, 7, 9, 11, 13, 17, 19)
for dvojica in enumerate(zoz):
    ix, pr = dvojica
    print(f'{ix}. prvocislo je {pr} ... dvojica = {dvojica}')

Vysledok:   
0. prvocislo je 2 ... dvojica = (0, 2)
1. prvocislo je 3 ... dvojica = (1, 3)
2. prvocislo je 5 ... dvojica = (2, 5)
3. prvocislo je 7 ... dvojica = (3, 7)
4. prvocislo je 9 ... dvojica = (4, 9)
5. prvocislo je 11 ... dvojica = (5, 11)
6. prvocislo je 13 ... dvojica = (6, 13)
7. prvocislo je 17 ... dvojica = (7, 17)
8. prvocislo je 19 ... dvojica = (8, 19) 
~~~
Ak by sme skúmali výsledok z tejto funkcie, dozvedeli by sme sa že ide o postupnosti skutočných dvojíc:
~~~
enumerate(zoz)
<enumerate object at 0x02F59B48>

list(enumerate(zoz))
[(0, 2), (1, 3), (2, 5), (3, 7), (4, 9), (5, 11), (6, 13), (7, 17), (8, 19)]

tuple(enumerate(zoz))
((0, 2), (1, 3), (2, 5), (3, 7), (4, 9), (5, 11), (6, 13), (7, 17), (8, 19))
~~~

[SPÄŤ](../../Obsah.md)