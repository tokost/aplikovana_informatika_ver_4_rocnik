> ## Indexovanie

**Indexovanie** pomocou hranatých zátvoriek [ ] - **je úplne rovnaké ako pri reťazcoch**: indexom je celé číslo od 0 do počet prvkov zoznamu - 1, alebo je to záporné číslo, napríklad:
~~~
>>> teploty = [10, 13, 15, 18, 17, 12, 12]
>>> nakup = ['chlieb', 'mlieko', 'rozky', 'jablka']
>>> studenti = ['Juraj Janosik', 'Emma Drobna', 'Ludovit Stur', 'Pavol Habera', 'Margita Figuli']
>>> zviera = ['pes', 'Dunco', 2011, 35.7, 'hneda']
>>> prazdny = []      # prázdny zoznam


>>> zviera[0]
    'pes'
nakup[1]
    'mlieko'
studenti[-1]
    'Margita Figuli'


>>> ['red', 'blue', 'yellow', 'green'][1]
    'blue'
>>> ['red', 'blue', 'yellow'][2][4]
    'o'
~~~

> ## Zreťazenie 
Zreťazenie pomocou operácie + označuje, že vytvoríme nový väčší zoznam, ktorý bude obsahovať najprv prvky prvého zoznamu a **za tým** všetky prvky druhého zoznamu, napríklad:
~~~
>>> nakup = ['chlieb', 'mlieko', 'rozky', 'jablka']
>>> nakup2 = ['zosity', 'pero', 'vreckovky']
>>> nakup + nakup2
    ['chlieb', 'mlieko', 'rozky', 'jablka', 'zosity', 'pero', 'vreckovky']

>>> studenti = ['Juraj Janosik', 'Emma Drobna', 'Ludovit Stur', 'Pavol Habera', 'Margita Figuli']
>>> studenti = studenti + ['Karel Capek']
>>>> studenti
    ['Juraj Janosik', 'Emma Drobna', 'Ludovit Stur', 'Pavol Habera', 'Margita Figuli', 'Karel Capek']

>>> prazdny = []      # prázdny zoznam
>>> prazdny + prazdny
    []

>>> [1] + [2] + [3, 4] + [] + [5]
    [1, 2, 3, 4, 5]
~~~

> ## Viacnásobné zreťazenie
Viacnásobné zreťazenie pomocou operácie * označuje, že daný zoznam sa navzájom zreťazí určený počet krát, napríklad:
~~~
>>> jazyky = ['Python', 'Pascal', 'C++', 'Java', 'C#']
>>> vela = 3 * jazyky
vela
    ['Python', 'Pascal', 'C++', 'Java', 'C#', 'Python', 'Pascal', 'C++', 'Java', 'C#', 'Python',
     'Pascal', 'C++', 'Java', 'C#']

>>> sto_krat_nic = 100 * [None]
>>> sto_krat_nic
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None]

>>> prazdny = []      # prázdny zoznam
>>> prazdny * 1000
    []
~~~

## Zisťovanie existencie prvku
Zisťovanie prvku sa uskutočňuje pomocou funkcie **in** označuje, či sa nejaká hodnota nachádza v danom zozname, napríklad:
~~~
>>> studenti = ['Juraj Janosik', 'Emma Drobna', 'Ludovit Stur', 'Pavol Habera', 'Margita Figuli']
>>> 'Pavol Habera' in studenti
    True

>>> nakup = ['chlieb', 'mlieko', 'rozky', 'jablka']
>>> 'pero' in nakup
    False
>
>> jazyky = ['Python', 'Pascal', 'C++', 'Java', 'C#']
>>> 'pascal' in jazyky
    False   # kvoli malemu p v slove pascal

>>> sto_krat_nic = 100 * [None]
>>> prazdny in sto_krat_nic
    False

>>> teploty = [10, 13, 15, 18, 17, 12, 12]
>>> 18 in teploty
    True

>>> teploty = [10, 13, 15, 18, 17, 12, 12]
>>> [18, 17] in teploty     # zoznam v zozname nevie
    False
~~~
V poslednom príklade testujeme, či sa dvojprvkový zoznam [18, 17] nachádza niekde v zozname teploty. Lenže tento zoznam obsahuje len celé čísla a žiaden prvok nie je typu zoznam. Hoci pre znakové reťazce fungovalo hľadanie podreťazca, napríklad:
~~~
>>> 'th' in 'Python'
    True
~~~
pre zoznamy táto analógia nefunguje.

Ešte si pripomeňte zápis negácie takéhoto testu, ktorý analogicky funguje pre reťazce aj zoznamy:
~~~
>>> not 'Y' in 'Python'
    True

>>> 'Y' not in 'Python'
    True

>>> 'str' not in ['pon', 'uto', 'str', 'stv', 'pia', 'sob', 'ned']
    False

>>> 'štv' not in ['pon', 'uto', 'str', 'stv', 'pia', 'sob', 'ned']
    True
~~~
> **Pripomeňme si, ako vyzerajú premenné a ich hodnoty v pamäti Pythonu.**

 Urobme toto priradenie:
 ~~~
 ab = [2, 3, 5, 7, 11]
 ~~~
 Do pamäti mien (globálny menný priestor) pribudne jeden identifikátor premennej ab a tiež referencia (odkaz) na päťprvkový zoznam [2, 3, 5, 7, 11]. Tento zoznam môžeme v pamäti hodnôt vizualizovať ako päť vedľa seba položených škatuliek, pričom v každej je referencia na príslušnú hodnotu:

 ![](./Tahaky_dokumenty_obrazky/Zoznam_v_pamati.png)

 Je dobre si uvedomiť, že momentálne máme v pamäti 6 premenných, jedna z nich je ab (je typu list) a zvyšných päť je ab[0], ab[1], ab[2], ab[3] a ab[4] (všetky sú typu int).

> ## Prechádzanie prvkov zoznamu

## Iterovanie zoznamu
**Iterovanie - opakovanie** sa najčastejšie vykonáva pomocou for-cyklu t.j opakovanému vykonávaniu rovnakých operácii (v našom prípade zobrazovania formátovaných údajov) pri ktorých sa menia parametre premennej i vystupujúcej najprv ako hodnota poradového čísla typu integer a neskôr ako index zoznamu. Napríklad:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for i in range(7):
        print(f'{i}. deň', teploty[i])

 Zobrazenie výsledku :      
    0. deň 10
    1. deň 13
    2. deň 15
    3. deň 18
    4. deň 17
    5. deň 12
    6. deň 12
~~~

Využili sme indexovanie prvkov zoznamu indexmi od 0 do 6 a použili sme funkciu range() ktorá obmedzuje parameter i na 7 iterácii. Ak nepotrebujeme pracovať s indexmi, ale stačia nám samotné hodnoty, zapíšeme:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for prvok in teploty:
        print(prvok, end=', ')

Zobrazenie výsledku : 
    10, 13, 15, 18, 17, 12, 12,
~~~
## Enumerate zoznamu
Ďalšou vstavanou funkciou je **enumerate - odpočítavanie** ktorá nám umožňuje sledovať **počet iterácii (opakovaní)** v slučke:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for i, prvok in enumerate(teploty):
        print(f'{i+1}. deň', prvok)

Zobrazenie výsledku :
    1. deň 10
    2. deň 13
    3. deň 15
    4. deň 18
    5. deň 17
    6. deň 12
    7. deň 12
~~~

## Výpočet priemernej hodnoty zoznamu
Takto môžeme napr. zapísať **výpočet priemernej hodnoty** - teploty:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]

sucet = 0
for prvok in teploty:   # premenna prvok je parameter ako i ktory iteruje od 1 az po zastavenie ktore musime zabezpecit my aby sa to nezacyklilo
    sucet += prvok
priemer = sucet / 7
print(f'priemerná teplota je {priemer:.1f}')    # formátovanie desatinného čísla na jedno miesto

Zobrazenie výsledku :
priemerná teplota je 13.9
~~~
## Výpočet maximálnej hodnoty zoznamu
Podobne vieme zistiť, napríklad **maximálnu hodnotu v zozname**:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
mx = teploty[0]
for prvok in teploty:
    if mx < prvok:
        mx = prvok
print('najteplejšie bolo', mx, 'stupňov')

Zobrazenie výsledku :
najteplejšie bolo 18 stupňov
~~~
## Výpočet odchylok napr. nadpriemerne teplých dní zoznamu
Alebo zistenie počtu nadpriemerne teplých dní. Prečítaj kód s porozumením resp. pozri si to v online pythone https://pythontutor.com/ :
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]

sucet = 0
for prvok in teploty:   # Pozor on iteruje cez poziciu zoznamu t.j. index ale do premennej prvok vklada hodnotu prvku !!!
    sucet += prvok
priemer = sucet / 7
pocet = 0
for prvok in teploty:
    if prvok > priemer:
        pocet += 1
print('počet nadpriemerne teplých dní', pocet)

Zobrazenie výsledku :
počet nadpriemerne teplých dní 3    # pricom priemerna hodnota je 13.8571
~~~

## Zhrnutie operácii prechodu zoznamom
Z týchto jednoduchých príkladov môžeme vytvoriť šablóny, ktoré niečo zisťujú o prvkoch zoznamu.
> ### Šablóna na zisťovanie hodnôt v zozname
Táto šablóna spočíta hodnoty prvkov (prvky by sme mohli, napríklad aj násobiť, alebo zreťazovať):
~~~
sucet = 0
for prvok in zoznam:
    sucet = sucet + prvok
print(sucet)
~~~

> ### Šablóna na zisťovanie zisťovanie nejakých informácii o zozname
Šablóna budeme zisťovať nejakú informáciu o prvkoch zoznamu, napríklad minimálny prvok. Pri+com podmienka aj priradenie budú závisieť od konkrétnej úlohy.:
~~~
mn = zoznam[0]
for prvok in zoznam:
    if prvok < mn:
        mn = prvok
print(mn)
~~~
### Šablóna na vypísanie prvkov zoznamu do jedného riadku
~~~
zoznam = [47, 'ab', -13, 22, 9, 25]
print('prvky zoznamu:', end=' ')
for prvok in zoznam:
    print(prvok, end=' ')
print()

Zobrazenie výsledku :
prvky zoznamu: 47 ab -13 22 9 25
~~~

### Šablóna keď pristupujeme k niektorým prvkom viackrát
~~~
for i in range(10):
    index = i % 4
    farba = ['red', 'blue', 'yellow', 'green'][index]
    print(farba)

Zobrazenie výsledku :
red
blue
yellow
green
red
blue
yellow
green
red
blue
~~~

> ## Zmena hodnoty prvku zoznamu

Dátová štruktúra zoznam je **meniteľný typ (tzv. mutable)** - môžeme meniť hodnoty prvkov zoznamu, napríklad takto:
~~~
studenti = ['Juraj Janosik', 'Emma Drobna', 'Ludovit Stur', 'Pavol Habera', 'Margita Figuli']
studenti[3]

Zobrazenie výsledku :
    'Pavol Habera'

studenti[3] = 'Janko Hrasko'
studenti[2] = 'Guido van Rossum'

Zobrazenie výsledku :
studenti
    ['Juraj Janosik', 'Emma Drobna', 'Guido van Rossum', 'Janko Hrasko', 'Margita Figuli', 'Karel Capek']
~~~
Hodnoty prvkov zoznamu môžeme zmeniť aj v cykle, ale k prvkom musíme pristupovať pomocou indexov, napríklad sme zistili, že náš teplomer ukazuje o 2 stupne menej ako je reálna teplota, preto opravíme t.j. zmen=ime všetky prvky zoznamu nasledovne:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for i in range(7):
    teploty[i] = teploty[i] + 2
print(teploty)

Zobrazenie výsledku :
[12, 15, 17, 20, 19, 14, 14]
~~~
Dá sa to tiež zapísať využitím štandardnej funkcie len(), ktorá vráti počet prvkov zoznamu:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for i in range(len(teploty)):
    teploty[i] += 2
print(teploty)
~~~
Pri tejto príležitosti si treba uvedomiť, že ak by sme prvky zoznamu neindexovali, ale prechádzali by sme ich priamo cez premennú cyklu prvok, tak náš zámer nedosiahneme:
~~~
teploty = [10, 13, 15, 18, 17, 12, 12]
for prvok in teploty:
    prvok += 2
print(teploty)

Zobrazenie výsledku :
[10, 13, 15, 18, 17, 12, 12]
~~~
Je to preto, lebo samotný zoznam sa tým nemení: **menili sme iba obsah premennej cyklu prvok** a obsah zoznamu zostal nezmenený. Preto je dobré si predstaviť, čo sa vlastne deje v pamäti pri zmene hodnoty prvku zoznamu. Zoberme si pôvodný päť prvkový zoznam prvočísel:
~~~
ab = [2, 3, 5, 7, 11]
~~~
Zmenou obsahu jedného prvku zoznamu sa zmení jediná referencia, všetko ostatné zostáva bez zmeny:
~~~
ab[2] = 55
~~~

![](./Tahaky_dokumenty_obrazky/Priradenie_do%20_jedneho_prvku.png)


Priraďovaním do jedného prvku zoznamu sa tento zoznam modifikuje, hovoríme, že priradenie do prvku je **mutable** operácia. Ukážme šablónu, pomocou ktorej vieme v cykle priradiť do rôznych prvkov rôzne hodnoty.

> ### Šablóna na vytváranie zoznamu
Táto šablóna umožňuje v cykle priradiť do prvkov zoznamu rôzne hodnoty bez toho aby vzniklo opakované prepísanie iba jednej hodnoty. **Príslušné indexy zoznamu však už musia existovať**. Najlepšie takýto zoznam pripravíme jedným priradením a viacnásobným zreťazením, napríklad pre n prvkov:
~~~
zoznam = [None] * n
for i in range(n):
    zoznam[i] = ... výpočet hodnoty
print(zoznam)
~~~
Ako príklad použitia tejto šablóny vytvoríme zoznamu prvých n druhých mocnín čísel od 0 do n-1 : kedy hodnotu premennej n načítame z klávesnice pomocou vstavanej funkcie input():
~~~
n = int(input('zadaj n: '))
mocniny = [None] * n
for i in range(n):
    mocniny[i] = i * i
print(mocniny)
~~~
Kedy hodnotu premennej n načítame z klávesnice pomocou novej vstavanej vstupnej funkcie **input()** ktorá po zadaní hodnoty čaká na stlačenie klávesy Enter:
~~~
zadaj n: 14
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
~~~

> ## Rezy
Keď sme v znakovom reťazci potrebovali zmeniť nejaký znak, zakaždým sme museli vyrobiť kópiu reťazca, napríklad:
~~~
retazec = 'Monty Python'
retazec[4] = 'X'     # takto sa to nedá
 
    ...
    TypeError: 'str' object does not support item assignment

retazec = retazec[:4] + 'X' + retazec[5:]
retazec

    'MontX Python'
~~~
Využili sme tu rezy (slice), t.j. získavanie podreťazcov. To isté sa dá použiť aj pri práci so zoznamami, lebo aj s nimi fungujú rezy, napríklad:
~~~
jazyky = ['Python', 'Pascal', 'C++', 'Java', 'C#']
print(jazyky)
    ['Python', 'Pascal', 'C++', 'Java', 'C#']

print(jazyky[1:3])
    ['Pascal', 'C++']

print(jazyky[-3:])
    ['C++', 'Java', 'C#']

print(jazyky[:-1])
    ['Python', 'Pascal', 'C++', 'Java']
~~~
Samozrejme, že pritom funguje aj určovanie kroku, napríklad:
~~~
print(jazyky[1::2])
    ['Pascal', 'Java']

print(jazyky[::-1])
    ['C#', 'Java', 'C++', 'Pascal', 'Python']
~~~
> #### Rezy **nemenia obsah** samotného zoznamu a preto hovoríme, že sú **immutable**.


> ### ***Priraďovanie do rezu***
Keď iba vyberáme nejaký podzoznam pomocou rezu, napríklad zoznam[od:do:krok], takáto operácia s pôvodným zoznamom nič nerobí (len vyrobí úplne nový zoznam). Lenže my môžeme obsah zoznamu meniť aj takým spôsobom, že **zmeníme len nejakú časť zoznamu**.

Takže **rez zoznamu** môže byť ***na ľavej strane*** priraďovacieho príkazu a potom ***na pravej strane*** priraďovacieho príkazu musí byť **nejaká postupnosť** (nemusí to byť zoznam). 

Priraďovací príkaz teraz túto postupnosť prejde, zostrojí z nej zoznam a ten vloží namiesto udaného rezu.

Príklady priraďovania rezu v ktorých sa modifikuje pôvodný zoznam, teda priraďovanie do rezu je **mutable** operácia.:
~~~
zoz = list(range(0, 110, 10))
print(zoz)
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

zoz[3:6] = ['begin', 'end']   # tri prvky sa nahradili dvomi
print(zoz)
    [0, 10, 20, 'begin', 'end', 60, 70, 80, 90, 100]
~~~
~~~
zoz[6:7] = [111, 222, 333]   # jeden prvok sa nahradil tromi
print(zoz)
    [0, 10, 20, 'begin', 'end', 60, 111, 222, 333, 80, 90, 100]
~~~
~~~
abc = list('Python')
print(abc)
    ['P', 'y', 't', 'h', 'o', 'n']

print(abc[2:2])              # rez dĺžky 0
    []

print(abc[2:2] = ['dve', 'slova'])  # rez dĺžky 0 sa nahradí dvomi prvkami

print(abc)
    ['P', 'y', 'dve', 'slova', 't', 'h', 'o', 'n']
~~~
~~~
prvo = [2, 3, 5, 7, 11]
print(prvo[1:-1])
    [3, 5, 7]

prvo[1:-1] = []           # rez dĺžky 3 sa nahradí žiadnymi prvkami
print(prvo)                      # prvky sa takto vyhodili
    [2, 11]
~~~

> ## Porovnávanie zoznamov
Zoznamy môžeme navzájom **porovnávať (na rovnosť, alebo menší/väčší)**. Funguje to na rovnakom princípe ako porovnávanie znakových reťazcov:

* postupne sa prechádzajú prvky jedného aj druhého zoznamu, kým sú rovnaké

* ak je jeden so zoznamov kratší, tak ten sa považuje za menší ako ten druhý

* ak pri postupnom porovnávaní prvkov nájde rôzne hodnoty, výsledok porovnania týchto dvoch rôznych hodnôt je výsledkom porovnania celých zoznamov

* každé dva porovnávané prvky musí Python vedieť porovnať: na rovnosť je to bez problémov, ale **relačné operácie < a > nebudú fungovať** napríklad pre porovnávanie čísel a reťazcov

~~~
[1, 2, 5, 3, 4] > [1, 2, 4, 8, 1000]
    True

[1000, 2000, 3000] < [1000, 2000, 3000, 0, 0]
    True

[1, 'ahoj'] == ['ahoj', 1]
    False

[1, 'ahoj'] < ['ahoj', 1]
    ...
    TypeError: '<' not supported between instances of 'int' and 'str'
~~~
> ## Dve premenné referencujú (odkazujú) na ten istý zoznam
Už sme získali predstavu o tom, že priradenie zoznamu do premennej označuje, že sme v skutočnosti do premennej priradili referenciu na zoznam. Lenže na ten istý zoznam v pamäti môžeme mať viac referencií, napríklad:
~~~
a = [2, 3, 5, 7, 11]
b = a
b[3] = 'kuk'
print(a)
    [2, 3, 5, 'kuk', 11]
~~~
Menili sme obsah premennej **b** (zmenili sme jej prvok s indexom 3), ale tým sa zmenil aj obsah premennej **a**. Totiž obe premenné referencujú na ten istý zoznam:

![](./Tahaky_dokumenty_obrazky/Referencia_na_rovnaky_zoznam01.png)

Keď teraz meníme obsah premennej **b** ( ale len **pomocou mutable operácií !** ), zmení sa aj obsah premennej a:

![](./Tahaky_dokumenty_obrazky/Referencia_na_rovnaky_zoznam02.png)

> ## Nasleduje časť ktorá sa zaoberá :

* Zoznam ako parameter funkcie
* Metódy nad zoznamom
* Zoznam ako výsledok funkcie
  
Ktorými sa budeme zaoberať neskôr keď budeme preberať funkcie a metódy https://python.input.sk/z/08.html#zoznamy 


[SPÄŤ](../../Obsah.md)