# Množiny (set)
Množiny sa používajú na uloženie viacerých položiek do jednej premennej. Set je kolekcia, ktorá je neusporiadaná , nemeniteľná t.j. neindexovaná a iterovatelná. Je to druh kolekcie ktorá opäť vychádza zo zoznamu (list) s tým rozdielom, že môže obsahovať iba unikátné (neopakujúce sa) položky t.j. **každá položka môže byť v množine zastúpená iba jeden krát**. Hlavnou výhodou použitia množiny na rozdiel od zoznamu je to, že má vysoko optimalizovanú metódu na kontrolu, **či je v množine obsiahnutý konkrétny prvok ktorý nás zaujíma**.Kedže táto vlastosť zodpovedá matematickéj definicii množiny, tak táto kolekcia aj v Pythone dostala názov množiny. V súvislosti so set-om tiež hovoríme že **položky nie sú zotriedené** - sú neusporiadané, čo znamená to, že položka bude pridaná svojvolne na ľubovolné miesto do množiny a položky nemajú definované poradie t.j. nie sú indexované a teda nie je možné na ne odkazovať podľa indexu alebo definovaného kľuča. Pojem **immutable** resp. nemenné znamená, že po ich vytvorení ich už nemôžeme meniť. Môžeme ich však zmazať alebo pridať ako nové v požadovanej podobe. Výraz **neopakujúce sa** zase znamená, že ak zadáme príkaz na pridanie hodnoty do množiny, bude táto hodnota vložená do množiny, len vtedy ak sa v nej ešte nevyskytuje. Pojem **iterovatelnosti** znamená že môžeme prechádzať prvkami kolekcie pomocou cyklu (napr. for a pod). Cyklami sa budeme zaoberať neskôr avšak na tomto mieste uvedieme kvôli názornosti iba malú ukážku:
~~~
pole = [2, 3, 5, 7, 11, 13, 17]
for i in pole:
    print(i, i*i)
~~~


Množinu môžeme vytvoriť aj manuálne a to tak že nejakej premennej ktorej dáme napr. názov a_set priradíme hodnoty ktoré sú v zložených zátvorkách oddelené čiarkami.
~~~
a_set = {1}         #   ①
print(a_set)
{1}

print(type(a_set))  #   ②
<class 'set'>

a_set = {1, 'Stevo', 10.5, True}      #   ③
print(a_set)
{1, 'Stevo', 10.5, True}

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums) 
{1, 2, 3, 4, 5}


~~~
①	Zápis množiny keď chceme vytvoriť množinu s jednou hodnotou. Vtedy uzatvoríme túto hodnotu do zložených zátvoriek { }.
②	Množiny sú v skutočnosti implementované ako triedy, ale týmto sa teraz zaoberať nebudeme.
③	Ak chceme vytvoriť množinu s viacerými hodnotami, oddelíme hodnoty čiarkami a všetko uzatvoríme do zložených zátvoriek. Pritom možno použiť aj rôzne údajové typy.

Súčasťou vytvoreného objektu môžu byť iba nemenné (a hašovateľné) prvky. Čísla (celé čísla, pohyblivé čísla, ako aj komplexné), reťazce a objekty tuple sú akceptované, ale objekty množiny, zoznamu a slovníka nie. Aj keď meniteľné prvky nemôžu byť uložené v množine, množina samotná je meniteľným objektom.
~~~
myset = {(10,10), 10, 20}
print(myset)

myset = {[10, 10], 10, 20}  #TypeError can't add a list

myset = { {10, 10}, 10, 20} #TypeError can't add a set
~~~
Vo vyššie uvedenom príklade (10,10)je to n-tica, a preto sa stáva súčasťou sady. Ide však [10,10]o zoznam, preto sa zobrazí chybové hlásenie, že zoznam je nehašovateľný. ( [Hashovanie](https://en.wikipedia.org/wiki/Hash_function) je mechanizmus v informatike, ktorý umožňuje rýchlejšie vyhľadávanie objektov v pamäti počítača.)

Pre množiny **neexistuje žiadná zvláštna syntax** ako to bolo v prípade zoznamov či n-tic, vytvárame ich jednoducho použitím globálnej funkcie set(), ku ktorej môžeme napr. použitím funkcie add() priložiť novú hodnotu, ktorá sa nachádza v jej parametri. To je príklad jednej z viacerých funkcii resp. metód ktoré môžeme použiť nad danou množinou:
~~~
planety = set(("Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun"))
print(planety)

planety.add("Pluto")
print(planety)

planety.add("Neptun")
print(planety)

Výsledok:
{'Jupiter', 'Uran', 'Saturn', 'Mars', 'Neptun', 'Země'}
{'Jupiter', 'Uran', 'Saturn', 'Mars', 'Neptun', 'Země', 'Pluto'}
{'Jupiter', 'Uran', 'Saturn', 'Mars', 'Neptun', 'Země', 'Pluto'}
~~~
V príklade výššie sme vytvorili množinu šiestich mien planet. Dvojité zátvorky na riadku s funkciou set() znamenajú, že sme odovzdali názvy planet formou n-tice ako parameter tejto
funkcie. Poradie položiek není zoradené podľa abecedy, a nezmení sa ani po pridaní novej položky. To ale nie je žiadná chyba, lebo položky sú evidované v danom poradí, čo nám pomáha na množine určiť pozíciu každej položky.

>**Množinu môžeme vytvoriť aj zo zoznamu (list).**
~~~
a_list = ['a', 'b', 'mpilgrim', True, False, 42]    # toto je zoznam, viete preco

a_set = set(a_list)                           #      ①
print(a_set)                                   
{'a', False, 'b', True, 'mpilgrim', 42}       #      ②

print(a_list)                                  
['a', 'b', 'mpilgrim', True, False, 42]       #      ③
~~~
①	K vytvoreniu množiny zo zoznamu sme použili funkciu set(). (Odborníci na Python vedia ako sú množiny implementované. Vedia teda že aj to že v skutočnosti nejde o volanie funkcie, ale o vytváranie tzv. inštancie triedy. Táto problematika spadá do vlastného OOP ktorou sa budeme zaoberať v ďalšom ročníku lebo teraz našu pozornosť sústreďujeme hlavne na základy Pythonu. Preto nám yzatiaľ bude stačit vedieť, že set() sa chová ako funkcia a že vracia množinu.)\
②	Ako sme sa už zmienili skôr, jedna množina môže obsahovať hodnoty ľubovolného datového typu. A tiež sme už spoznali, že množiny sú neusporiadané. Táto množina si nepamätuje pôvodné poradie prvkov v zozname, ktorý ból použitý k jej vytvoreniu. Ak by sme do množiny pridávali ďalšie prvky, nebude si množina pamätovať poradie, v akom ste ich vkladali.\
③	Pôvodný zoznam zostáva nezmenený.

**Poznámka:** Hodnoty Truea 1sa v súboroch považujú za rovnakú hodnotu a zaobchádza sa s nimi ako s duplikátmi.

>**Vytvorenie prázdnej množiny**

Ak nemáme k dispozícii žiadne hodnoty (s tým že budú vytvorené resp. načítané podľa nejakého kritéria neskôr) nie je to žiadny problém. Môžeme totiž vytvoriť tzv. prázdnu množinu čím si vyčleníme (alokujeme) priestor a názov množiny pre neskoršiu aktualizáciu.
~~~
a_set = set()          #  ①
a_set                  #  ②
print(set())
# set()

>>> type(a_set)        #  ③
<class 'set'>

print(len(a_set))      #  ④
# 0

>>> not_sure = {}      #  ⑤
>>> type(not_sure)
<class 'dict'>
~~~
①	K vytvoreniu prázdnej množiny zavoláme set() bez argumentov.\
②	Zobrazená reprezentácia prázdnej množiny vypadá trochu divne. Asi sme očakávali niečo ako { } . Týmto spôsobom sa ale vyjadruje prázdny slovník (dictionary) a nie množina. O slovníkoch se dozvieme v nasledujúcej časti.\
③	Navzdory podivnosti zobrazenej reprezentácie to skutočne je množina...\
④	...a táto množina neobsahuje žiadné prvky.\
⑤	Prázdnu množinu nie je možné vytvoriť zápisom dvoch zložených zátvoriek kvôli histórii vývoja verzii (z Pythonu ver. 2). Týmto spôsobom sa vyjadruje prázdny slovník a nie množina.
>## Pridávanie hodnôt do množiny

# Operácie nad množinami (set-mi)
>## Zistenie počtu položiek množiny
Ak chcete zistiť, koľko položiek má sada, použite len()funkciu.
~~~
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
~~~

Do existující množiny můžeme přidávat hodnoty dvěma různými způsoby: metodou add() a metodou update().
~~~
>>> a_set = {1, 2}
>>> a_set.add(4)  ①
>>> a_set
{1, 2, 4}
>>> len(a_set)    ②
3
>>> a_set.add(1)  ③
>>> a_set
{1, 2, 4}
>>> len(a_set)    ④
3
~~~
①	Metoda add() přebírá jeden argument, který může být libovolného datového typu, a přidává zadanou hodnotu do množiny.
②	Množina teď má tři členy.
③	Množiny jsou kolekcemi jedinečných hodnot. Pokud do množiny zkusíme přidat hodnotu, která se v ní již nachází, neudělá to nic. Nevznikne chyba. Jde zkrátka o prázdnou operaci.
④	Množina má pořád jen tři členy.
~~~
>>> a_set = {1, 2, 3}
>>> a_set
{1, 2, 3}
>>> a_set.update({2, 4, 6})                       ①
>>> a_set                                         ②
{1, 2, 3, 4, 6}
>>> a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})  ③
>>> a_set
{1, 2, 3, 4, 5, 6, 8, 9, 13}
>>> a_set.update([10, 20, 30])                    ④
>>> a_set
{1, 2, 3, 4, 5, 6, 8, 9, 10, 13, 20, 30}
~~~
①	Metoda update() přebírá jeden argument, rovněž množinu, a přidá všechny její členy do původní množiny. Je to, jako kdybychom volali metodu add() pro všechny členy množiny předané argumentem.
②	Protože cílová množina nemůže obsahovat jednu hodnotu dvakrát, duplicitní hodnoty se ignorují.
③	Ve skutečnosti můžete metodu update() volat s libovolným počtem argumentů. Pokud ji zavoláte s dvěma množinami, metoda update() přidá všechny členy z každé z předaných množin do původní množiny (duplicitní hodnoty se přeskočí).
④	Metoda update() umí zpracovat objekty různých datových typů, včetně seznamů. Pokud jí předáte seznam, pak metoda update() přidá do původní množiny všechny členy seznamu.

>## Odstraňovanie položiek z množiny
ednotlivé hodnoty lze z množiny odstranit třemi způsoby. První dva, discard() a remove(), se liší v jedné malé drobnosti.
~~~
>>> a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
>>> a_set
{1, 3, 36, 6, 10, 45, 15, 21, 28}
>>> a_set.discard(10)                        ①
>>> a_set
{1, 3, 36, 6, 45, 15, 21, 28}
>>> a_set.discard(10)                        ②
>>> a_set
{1, 3, 36, 6, 45, 15, 21, 28}
>>> a_set.remove(21)                         ③
>>> a_set
{1, 3, 36, 6, 45, 15, 28}
>>> a_set.remove(21)                         ④
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 21
~~~
①	Metoda discard() přebírá jeden argument a zadanou hodnotu odebere z množiny.\
②	Pokud metodu discard() voláme s hodnotou, která v množině neexistuje, neprovede se nic. Nevznikne chyba. Jde o prázdnou operaci.\
③	Metoda remove() také přebírá hodnotu jediného argumentu a také odstraňuje hodnotu z množiny.\
④	Odlišnost se projeví v případě, kdy se zadaná hodnota v množině nenachází. V takovém případě metoda remove() vyvolá výjimku KeyError.

Funkcia set() sa tiež používa na konverziu objektu typu reťazec, n-tica alebo slovník na objekt množiny, ako je znázornené nižšie.
~~~
s = set('Hello') # converts string to set
print(s)
{'l', 'H', 'o', 'e'}

s = set((1,2,3,4,5)) # converts tuple to set
print(s)
{1, 2, 3, 4, 5}

d = {1:'One', 2: 'Two'} 
s = set(d)   # converts dict to set
print(s) 
{1, 2}
~~~

>### Použitie metódy pop()
Na odstraňovanie prvkov z množiny, tak ako tomu bolo pri zoznamoch aj tu možno použiť funkciu či metódu pop().
~~~
>>> a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
>>> a_set.pop()                                ①
1
>>> a_set.pop()
3
>>> a_set.pop()
36
>>> a_set
{6, 10, 45, 15, 21, 28}
>>> a_set.clear()                              ②
>>> a_set
set()
>>> a_set.pop()                                ③
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
~~~
①	Metoda pop() odstraní jeden prvek z množiny a vrátí jeho hodnotu. Ale množiny jsou neuspořádané a neexistuje u nich nic takového jako „poslední“ hodnota. Proto také neexistuje možnost ovlivnit, která hodnota bude odstraněna. Je to zcela náhodné.\
②	Metoda clear() odstraní všechny prvky množiny a množina se stane prázdnou. Ve výsledku je to stejné jako provedení příkazu a_set = set(), který vytvoří novou prázdnou množinu a přepíše původní hodnotu proměnné a_set.\
③	Pokus o volání metody pop() pro prázdnou množinu vede k vyvolání výjimky KeyError.

# Ďalšie funkcie nad množinami (set-mi)

>## Bežné množinové funkcie (metódy)
Pythonovský datový typ **set podporuje niekoľko bežných množinových funkcii (metód)** či operácií.

~~~
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
30 in a_set                        ①        
True

31 in a_set
False

b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set.union(b_set)                 ②

{1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}

a_set.intersection(b_set)          ③
{9, 2, 12, 5, 21}

a_set.difference(b_set)            ④
{195, 4, 76, 51, 30, 127}

a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set.symmetric_difference(b_set)  ⑤
{1, 3, 4, 6, 8, 76, 15, 17, 18, 195, 127, 30, 51}
~~~
①	Ak chceme otestovať, či je daná hodnota prvkom množiny, použijeme operátor **in**. Funguje rovnakým spôsobom ako u je to u zoznamov.\
②	Metóda union() (zjednotenie) vracia novú množinu, ktorá obsahuje všetky prvky ako z jednej, tak aj z druhej množiny.\
③	Metoda intersection() (prienik) vracia novú množinu, ktorá obsahuje všetky prvky ktoré sa nachádzajú se v oboch množinách súčasne.\
④	Metoda difference() (rozdíl) vrací novou množinu obsahující všechny prvky, které se nacházejí v množině a_set, ale nenacházejí se v množině b_set.\
⑤	Metoda symmetric_difference() (symetrický rozdiel) vracia novú množinu obsahujúcu všetky prvky, ktoré se nachádzajú práve v jednej z množín.\

Tri z týchto funkcii (metód) sú tzv. symetrické čo znamená súmernosť z hladiska. V náväznosti na predchádzajúci príklad sú to tieto funkcie:
~~~
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set.symmetric_difference(a_set)  ①
{3, 1, 195, 4, 6, 8, 76, 15, 17, 18, 51, 30, 127}

b_set.symmetric_difference(a_set) == a_set.symmetric_difference(b_set)  ②
True


b_set.union(a_set) == a_set.union(b_set)  ③
True

b_set.intersection(a_set) == a_set.intersection(b_set)  ④
True

b_set.difference(a_set) == a_set.difference(b_set)  ⑤
False
~~~
①	Symetrický rozdiel množín a_set od b_set vypadá inak ako symetrický rozdiel množín b_set od a_set. Ale pamätujme na to, že množiny sú neusporiadané. Akékoľvek dve množiny, ktorých všetky hodnoty sa zhodujú (žiadna nesmie byť vynechaná), sa považujú za zhodné.\
②	A presně tento prípad nastal tu. Nenechajme sa zmiať reprezentáciami týchto množín ktoré zobrazené v pythonovskom shelle. Obsahujú rovnaké hodnoty, takže sú zhodné.\
③	Zjednocenie dvoch množín je tiež symetrické.\
④	Prienik dvoch množín je taktiež symetrický.\
⑤	Rozdiel dvoch množín symetrický neni. Ono to dáva zmysel. Podobá sa to na odčítanie jedného čísla od druhého. Na poradí operandov tu ale záleží !

A nakoniec tu máme niekoľk funkcii ktoré vyhodnocujú zadané otázky vztiahnuté na množiny. 
~~~
a_set = {1, 2, 3}
b_set = {1, 2, 3, 4}
a_set.issubset(b_set)    ①
True

b_set.issuperset(a_set)  ②
True

a_set.add(5)             ③
a_set.issubset(b_set)
False

b_set.issuperset(a_set)
False
~~~
①	Množina a_set je podmnožinou množiny b_set — všechny prvky množiny a_set jsou současně prvky množiny b_set.\
②	Stejnou otázku můžeme položit obráceně. Množina b_set je nadmnožinou množiny a_set, protože všechny prvky množiny a_set jsou současně prvky množiny b_set.\
③	Jakmile do množiny a_set přidáme hodnotu, která se v množině b_set nenachází, oba testy vrátí hodnotu False.

>## Množiny v booleovském kontextu

Množiny můžeme použít v booleovském kontextu, například v příkazu if.
~~~
>>> def is_it_true(anything):
...   if anything:
...     print("yes, it's true")
...   else:
...     print("no, it's false")
...
>>> is_it_true(set())          ①
no, it's false
>>> is_it_true({'a'})          ②
yes, it's true
>>> is_it_true({False})        ③
yes, it's true
~~~
①	Prázdná množina se v booleovském kontextu vyhodnocuje jako false.
②	Ľubovolná množina s alespoň jedním prvkem se vyhodnocuje jako true.
③	Ľubovolná množina s alespoň jedním prvkem se vyhodnocuje jako true. Hodnota prvků je nepodstatná.

Nasledujúca tabuľka uvádza vstavané metódy funkcie nad množinou (set) s odkazom na príklady:

| Metóda    | Popis                                                                     |
|-----------|---------------------------------------------------------------------------|
| [set.add()](https://www.tutorialsteacher.com/python/set-add) | Pridá prvok do set-u. Ak prvok už v množine existuje, nepridá tento prvok.
|[set.clear()](https://www.tutorialsteacher.com/python/set-clear)| Odstráni všetky prvky zo set-u.
|[set.copy()](https://www.tutorialsteacher.com/python/set-copy)|Vráti plytkú kópiu set-u t.j. skopírujú sa iba atribúty objektov. [Hlboká kópia predstavuje úplnú kópiu objektu.](https://sk.wiki-base.com/7779662-python-shallow-copy-and-deep-copy)
|[set.difference()](https://www.tutorialsteacher.com/python/set-difference)|Vráti novú množinu s jedinečnými prvkami, ktoré nie sú v inej množine odovzdanej ako parameter.
|[set.difference_update()](https://www.tutorialsteacher.com/python/set-difference-update)|Aktualizuje množinu, v ktorej sa metóda volá, prvkami, ktoré sú spoločné v inej množine odovzdané ako argument.
|[set.discard()](https://www.tutorialsteacher.com/python/set-discard)| Odstráni konkrétny prvok zo sady.
|[set.intersection()](https://www.tutorialsteacher.com/python/set-intersection)|Vráti novú množinu s prvkami, ktoré sú v daných množinách spoločné.
|[set.intersection_update()](https://www.tutorialsteacher.com/python/set-intersection-update) | Aktualizuje množinu, na ktorej sa volá metóda instersection_update(), o spoločné prvky medzi špecifikovanými množinami.
|[set.isdisjoint()](https://www.tutorialsteacher.com/python/set-isdisjoint)|Vráti hodnotu true, ak dané množiny nemajú žiadne spoločné prvky. Množiny sú disjunktné vtedy a len vtedy, ak je ich priesečník prázdna množina.
|[set.issubset()](https://www.tutorialsteacher.com/python/set-issubset)|Vráti hodnotu true, ak množina (na ktorej sa volá issubset()) obsahuje každý prvok druhej množiny odovzdaný ako argument.
|[set.pop()](https://www.tutorialsteacher.com/python/set-pop)|Odstráni a vráti náhodný prvok zo sady.
|[set.remove()](https://www.tutorialsteacher.com/python/set-remove) | Odstráni zadaný prvok zo sady. Ak sa zadaný prvok nenašiel, vyhláste chybu.
|[set.symmetric_difference()](https://www.tutorialsteacher.com/python/set-symmetric-difference)| Vráti novú množinu s odlišnými prvkami nachádzajúcimi sa v oboch množinách. 
|[set.symmetric_difference_update()](https://www.tutorialsteacher.com/python/set-symmetric-difference-update) |Aktualizuje množinu, na ktorú sa volala metóda instersection_update(), o prvky, ktoré sú spoločné medzi špecifikovanými sadami.
|[set.union()](https://www.tutorialsteacher.com/python/set-union)| Vráti novú množinu s odlišnými prvkami zo všetkých daných množín.
|[set.update()](https://www.tutorialsteacher.com/python/set-update)|Aktualizuje množinu pridaním odlišných prvkov z odovzdanej jednej alebo viacerých iterovateľných položiek.

>### Operácie vs. vstavané funkcie
Ako už bolo spomenuté, dátový typ množiny v Pythone sa implementuje ako množina definovaná v matematike. Preto je aj tu možné vykonávať rôzne známe operácie. Operátory |, &, - a ^ vykonávajú operácie zjednotenia, prieniku, rozdielu a symetrického rozdielu. Každý z týchto operátorov má zodpovedajúcu metódu spojenú so vstavanou triedou množín.
	
| Operácie nad set-mi                                                                                                                                                | Príklady                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Zjednotenie** : Vráti novú množinu s prvkami z oboch množín.<br><br>**Operátor** :<br>**Metóda** : [set.union()](https://www-tutorialsteacher-com.translate.goog/python/set-union?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                                                                     | s1={1,2,3,4,5}<br>s2={4,5,6,7,8}<br>s1 s2 #{1, 2, 3, 4, 5, 6, 7, 8}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)<br><br>s1={1,2,3,4,5}<br>s2={4,5,6,7,8}<br>s1.union(s2) #{1, 2, 3, 4, 5, 6, 7, 8}<br>s2.union(s1) #{1, 2, 3, 4, 5, 6, 7, 8}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                                                                                                              |
| **Prienik** : Vráti novú množinu obsahujúcu prvky spoločné pre obe množiny.<br><br>**Operátor**: &<br>**Metóda**: [set.intersection()](https://www-tutorialsteacher-com.translate.goog/python/set-intersection?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                                       | s1={1,2,3,4,5} <br>s2={4,5,6,7,8} <br>s1&s2 #{4, 5}                       <br>s2&s1 #{4, 5}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)<br><br>s1={1,2,3,4,5}           <br>s2={4,5,6,7,8}           <br>s1.intersection(s2) #{4, 5}                                <br>s2.intersection(s1) #{4, 5}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                                                      |
| **Rozdiel**: Vráti množinu obsahujúcu prvky iba v prvej množine, ale nie v druhej množine.<br><br>**Operátor** : -<br>**Metóda**: [set.difference()](https://www-tutorialsteacher-com.translate.goog/python/set-difference?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                             | s1={1,2,3,4,5} <br>s2={4,5,6,7,8} <br>s1-s2 #{1, 2, 3}                    <br>s2-s1 #{8, 6, 7}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)<br><br>s1={1,2,3,4,5}      <br>s2={4,5,6,7,8}      <br>s1.rozdiel(s2) #{1, 2, 3}                        <br>s2.rozdiel(s1) #{8, 6, 7}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)                                                                         |
| **Symetrický rozdiel**: Vráti množinu pozostávajúcu z prvkov v oboch množinách, s výnimkou spoločných prvkov.<br><br>**Operátor**: ^<br>Metóda: [set.symmetric_difference()](https://www-tutorialsteacher-com.translate.goog/python/set-symmetric-difference?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) | s1={1,2,3,4,5} <br>s2={4,5,6,7,8} <br>s1^s2 #{1, 2, 3, 6, 7, 8}           <br>s2^s1 #{1, 2, 3, 6, 7, 8}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp)<br><br>s1={1,2,3,4,5}               <br>s2={4,5,6,7,8}               <br>s1.symmetric_difference(s2) #{1, 2, 3, 6, 7, 8}                        <br>s2.symmetric_difference( s1) #{1, 2, 3, 6, 7, 8}<br>[Kód](https://www-tutorialsteacher-com.translate.goog/codeeditor?cid=python-3z7undc5a&_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp) |

[SPÄŤ](../../Obsah.md)