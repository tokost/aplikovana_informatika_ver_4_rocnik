>>## Moduly

Na volanie funkcii ktoré sú definované v iných súboroch nám slúži funkcia **main()**. Ponúka sa nám takto vhodný nástroj pre štrukurovanie kódu našej aplikácie. Robí sa to pomocou príkazu **import** prostredníctvom ktorého sa do main() prenášajú moduly funkcie z iných pythonovských súborov. Tým je aj daná **súvislosť medzi hlavnou funkciou main() a jej modulmi**.

Všeobecne povedané **modul** v Pythone je niečo, z čoho můžeš importovat nejakú funkciu. Má svoj názov a ako bolo vidieť v predchádzajúcom príklade z modulu pyplot bola importovaná funkcia plot. Alebo napr. z iného modulu math môžes importovat funkci sqrt ktorá j ev tomto module zahrnutá:
~~~
from math import sqrt

print(sqrt(2))
~~~
Tentokrát sme pre získanie funkcie z modulu nepoužili zápis 
~~~
import meno_knižnice.modul as nazov_priradenia
~~~
kedy funkciu používam cez bodkovú konvenciu
~~~
nazov_priradenia.funkcia(parametre)
~~~
ale inú formu zápisu
~~~
from modul import funkcia
~~~
Okrem importovania jednotlivých funkcii z modulu, môžeš modul importovať aj celý naraz. Aj v takomto prípade platí spomínaný bodkový zápis aby si sa dostal k tomu čo modul ponúka (aké metódy). Táto konvencia neplatí iba v prípade modulov ale môžeme sa s ňou stretnú aj inde ako napr. pri funckii na premenu reťazca na veľké písmená "Ahoj".upper. Met=oda upper je však vstavanou funkciou (build-in) a preto ju nemusíme importovať 
~~~
message = 'python is fun'

# convert message to uppercase
print(message.upper())

# Output: PYTHON IS FUN
~~~
**Vstavané metódy v Pythone nemusíme importovať** sú vstavané priamo v interpreteri Pythonu. Ale neplatí to napr. pre funkciu turtle:
~~~
import turtle

turtle.left(90)
turtle.color('red')
turtle.forward(100)
turtle.exitonclick()
~~~
~~~
import math

print(math.cos(math.pi))
~~~

**Hvězdičky nechceme**
Občas sa pri používaní príkazu **import** používa hviezdička ktorá chce povedať že všetko. Je však lepšie v tejto súvislosti na to zabudnúť a treba importovať celý modul prostredníctvom jeho mena. Pri väčších programoch sa zvzšuje ich prehladnosť a zjednodušuje hľadanie chýb.

>## Vlastné moduly

A teraz to hlavné k čomu sme sa chceli dostať. Vedieť si vytvoriť svoj vlastný modul a takým spôsobom že sa vytvorí pythonovský súbor. Funkcie ktoré v ňom nadefinuješ a globálne premenné ktoré v ňom nastavíš potom bude možné použiť všade tam kam tento modul naiportuješ.

Vyskúšame si to na príklade v ktorom vytvoríme súbor soubor luka.py a do neho napíšeme:
~~~
barva_travy = 'zelená'
pocet_kotatek = 28

def popis_stav():
    return f'Tráva je {barva_travy}. Prohání se po ní {pocet_kotatek} koťátek'
~~~
A potom do ďalšieho súboru s menom vypis.py, napíš:
~~~
import luka

print(luka.popis_stav())
~~~
A nakoniec spustíme program vypis.py cez git shell:
~~~
$ python vypis.py
~~~

Príkaz import hladá súbory okrem iného aj v adresári v ktorom je hlavný modul programu - teda súbor ktorý sme spustili (vypis.py). **Oba súbory (aj luka.py) by preto mali byť v rovnakom adresári**.

>#### Vedlajšie efekty 

Čo presne vlastne príkaz **import luka** vykonáva.

Python nájde príslušný súbor (luka.py) a vykoná v ňom všetky príkazy od zhora dole ako v normálnom pythonovskom programe. Všetky globálne premenné vrátane nadefinovaných funkcii potom dá k dispozícii kódu ktory ho importoval.

Ak ten istý modul importujeme druhý krát, už sa nevykonáva celý postup odznova. Druhý import iba sprístupní rovnakú sadu premenných a funkcii ako to bolo v prvom importe. Možeme to vidieť ak do súboru luka.py na koniec dopíšeme:
~~~
print('Luka je zelená!')
~~~
Spusťime python (ak je už sputený ukončime ho a znovu spustime) a zadajme v ňom:
~~~
print('Prvý import:')
import luka
print('Druhý import:')
import luka
~~~

Výpis sa objaví len po prvý krát. Čo ale urobiť, keď súbore luka.py niečo zmeníme. Zmeny sa totiž v takomto opakovanom volaní do naimportovaného modulu nepremietnú. Aby sa ale premietli, musíme Python zatvoriť a znovu spustiť. (Aj preto je dobré spoúštať programy zo souborov a nie cez príkaz interpreta. Pri každom spustení sa totiž znovu načíta aktuálná verzia modulov.)

Ale späť k volaniu print. Príde Vám trochu divné že príkaz import luka niečo vypíše na obrazovku ?

Keď **modul pri importe** „robí“ niečo naviac ako nastavenie premenných a funkcii, tak sa hovorí že má 
**vedlajší efekt** (angl. side effect). Vedlajší efekt môže byť napr. vypísanie niečoho na obrazovkusání něčeho na obrazovku alebo do súboru, vykreslenie okna na obrazovku, vypísanie otázky na užívateľa pomocou input, a pod.

V moduloch pripravených na importovanie sa ale **vedlajším efektom radšej vyhýbajte**: úloha modulov je dať k dispozícii funkcie, ktoré niečo robia, a nie to urobiť priamo. Všimnime si napríklad, že import turtle neukáže okno – to sa objaví až po zavolaní turtle.forward(). 

>### Importom si programátor pripravuje nástroje a až  zavolaním funkcie ich používa.

Preto príkaz print radšej z modulu zase vymažme a presunme ho do volajúceho programu.

>## Samoistatný adresár pre každý projekt

Od teraz keď už poznáme na čo slúžia knižnice, moduly a funkcie **môžeme písať väčšie programy a pracovať na týmových projektoch**. Projekty a rozsiahlejšie programy totiž obsahujú viacero súvisiacich súborov ktoré sú viac alebo menej navzájom previazané a prepojené práve cez knižnice, moduly a funkcie ktoré obsahujú a ktoré súčasne používajú. Je vhodné aby sa pre každý takýto projekt vytvoril samostatný adresár. Na základe toho je možné sa lepšie orientovať v tom ku ktorému ten ktorý súbor patrí.

>### Mechanizmus spracovania modulov

Moduly môžu obsahovať ľubovolný kód a ich použitie sa teda neobmedzuje iba na púhe vlastné definovanie celej rady funkcii. Pred prvým nájdením modulu interpreter nájde súbor ktorý obsahuje modul, načíta ho a spustí všetky príkazy ktoré obsahuje. tento proces sa nazýva
**inicializácia modulu**. Pri inicializácii vznikajú objekty ktoré reprezentujú funkcie vo vnútri modulu a počas nej je možné nastaviť do určitého stavu aj globálne premenné. Ak chce program importovať modul ktorý už ból inicializovaný, nepríde k opakovanému spusteniu kódu, ale sa použijú objekty modulu ktoré boli vytvorené pri prvej inicializácii.

Zavedením modulu vznikne nový priestor mien (pamäť mien) ktorý je určený pre globálne premenné tohoto modulu. Vďaka tomuto mechanizmu môž eautor modulu používať ľubovolné názvy premenných s napriek tomu nepríde ku kolízii s premennými iného modulu. **Premenné v tomto priestore mien sú dostupné len v prípade, ak bude dostupný t.j. importovaný aj modul !!!** Okrem príkazu import sa to uskutoční zadaním mena mmodulu.

Nedoporučuje s avšak ľubovolne modifikovať súkromné premenné (použité pri definícii funkcie) modulu, mohla by sa tým totiž  narušiť konzistencia (vezby) údajov modulu a na základe toho by mohol chybne pracovať a dávať zlé výsledky.

Je len samozrejmé, že **moduly môžu importovať ďalšie moduly**. V pythone je zvykom umiestniť všetky príkazy **import** na začiatok modulu alebo kódu (skriptu - viacerých príkazov). Podmienky jazyka to ale nevyžadujú a príkaz import môžeme použiť kdekoľvek napr. aj vo vetve pod príkazom if, alebo vo vnútri funkcie.

Ako sme spomenuli vyššie, príkaz zavedie do lokálneho priestoru pamäti mien objekt modulu. Existuje ale aj variant príkazu import ktorý priamo zavedie niektoré alebo všetky objekty z určitého. Majme teda funkcie
fib() a fib2() v module fibo.py:
~~~
# modul Fibonacciho postupnosti

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
~~~

Nemusíme teda používat priradenie pre vytvorenie lokálneho mena:
~~~
fibo.fib(1000)
# Vysledok je : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
fibo.fib2(100)
# Vysledok je :[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fibo.__name__
# Vysledok je : 'fibo'py
~~~
Toto použitie príkazu import nevytvorí meno odkazujúce na objekt modulu a v príklade vyššie nie je teda premenná fibo ktorá reprezentuje modul fibo definovaná.

Pre **zavedenie všetkých mien z modulu** tu je ďalší variant príkazu import:
~~~
>>> from fibo import *
>>> fib(500)
# Vysledok je : 1 1 2 3 5 8 13 21 34 55 89 144 233 377
~~~

Tento príkaz zavedie z modulu všetky mená s výnimkou tých ktoré začínajú znakom podtžníka. Je potrebné ale podotknúť že tento spôsob používani amodulov je veľmi zradný. Je to preto ž ejednak nie je známe na ktorom mieste je príslušná premenná definovaná a jednak môže dojisť ku kolízii mien. Preto je u niektorých moduloch výslovne **zakázané používanie zápisu** 
~~~
from ... import *
~~~

>### Vyhľadávanie modulov

Čo sa stane keď importujeme modul fibo prvý krát ?
Kde všade interpreter hľadá súbory obsahujúce definíciu tohoto modulu? Predovšetkým sa interpréter pozrie do pracovného adresára a keď tu nájde súbor fibo.py všetká jeho práca končí a pokusí sa zavieť tento modul do súboru ktorý ho volá.

Keď však tento súbor v tomto adresári nenájde, začne ho hľadať podľa presných pravidiel ktoré sú špecifikované v definíciach jazyka. Takže: 
* najprv sa pozrie na premennou prostredia , ktorá by mala mať rovnakú syntax ako premenná prostredia PATH.
* Ak neni premenná PYTHONPATH nastavená, alebo v adresároch ktoré špecifikuje nie je požadovaný súbor najdený pokračuje vyhladávanoie v implicitnej (predvolenej) ceste.
* tu špecifikuje premenná sys.path ktorý obsahuje zoznam reťazcov reprezentujúcich ostatné adresáre. Obsah téjto promennej je závislý na inštalácii interpretru a jeho nastavenie v modulu siete. Môže vyzerať napr. takto: ['/usr/lib/python2.2', '/usr/lib/python2.2/plat-linux2'].

Je potrebné dôsledne **dbať na to, aby nejaký súbor v pracovnom adresári nemal rovnaké mená ako nejaký standardný modul** resp. aby sa pod menom skutočne skrývali vyhladávané definované funkcie. Ak by tak nebolo nemali by sme cestu k hľadanému modulu a pri pokuse o zavedenie modulu by sme obdržali súbor v pracovnom adresári kde sa funkcie ktoré chceme použiť nachádzať nebudú.

Ak **interpreter požadovaný modul nenájde**, dojde k [výnimke](https://macek.sandbox.cz/texty/python-tutorial-cz/tut/node10.html#SECTION0010200000000000000000) ktorá sa odvodí z príkazu import. Reakcie na výnimky predstavuje samostatnú problematiku spadajúcu do vyššej školy a preto sa s ňou n atomto mieste zaoberať nebudeme. Jednou z najznámejších spôsobov reakcie na problém miesto riešenia vynimky je napr. zobrazenie chybového hlásenia 404.

Obdobne j eto aj v prípade ak sa požadovaný modul podarilo nájisť, ale pri jeho inicializácii došlo k potrebe riešiť výnimku. Tu je treba dávať pozor na to, že modul nebol pri prvom volaní korektne inicializovný a tak pri ďalšom volaní sa jeho inicializáci aopakovať nebude lebo systém má zaregistrované iba prvé inicializovanie bez výsledku ako dopadlo. Môže sa teda stať že modul bude možné používat nezinicializovaný aj s dôsledkami.

>### Standardné moduly

Základná distribúcia Pythonu obsahuje velké množstvo modulov (sú popísané v samostatnom dokumente [**Python Library Reference**](https://docs.python.org/3/library/index.html)). Vďaka nim je možné realizovať množstvo úloh spojených s internetom, unixovými databázami dbm, prácami so soúbormi, operačným systémom a mnoho a mnoho ďalších.

Niektoré moduly sú priamo súčsťou interpretru, umožňujú totiž prístup k operáciam, ktoré nie sú priamo súčasťou jadra prostredia, ale sú mu veľmi blízké (napr. v danej aplikácii závisia na rýchlosti vykonávania alebo je potrebné volať funkcie operačného systému či ďalších knižníc). Zahrnutie týchto modulov je závislé na konfiguracii a prekladu interpretra. (Napríklad modul Tkinter určený ako rozhranie ku grafickej knižnice Tk je prítomný len na systémoch s knižnicou Tk).

Mezi všetkými modulmi nájdeme jeden, ktorý ponúka samotné jádro operačného systému. Modul **sys**  obsahuje každý interpretr. Jeho premenné **sys.ps1 a sys.ps2 umožňujú v interaktívnom móde nastavenie primárnej a sekundárnej výzvy smerom k interpreteru:
~~~
>>> import sys
>>> sys.ps1
# Vystupom je : '>>> '
>>> sys.ps2
# Vystupom je : '... '
>>> sys.ps1 = 'C> '
# Vystupom je : C> 
print ('Ahoj!')
# Vystupom je :Ahoj!
# C>
~~~

Premenná **sys.path** je zoznam reťazcov ktorý určuje cesty v ktorých interpréter vyhľadáva moduly. Je inicializována z premennej prostredia PYTHONPATH prípadne je nastavená v module siete. Ide o klasický zoznam, ktorý môžete meniť a prídávať do neho běžnými operáciami definovanými nad zoznamami:
~~~
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
~~~

>### Funkcia dir()

Internú funkciu dir() používame v prípade ak chceme zistiť všetky mená ktoré sú definované vo vnútri nejakého objektu. Táto funkcia vracia zoznam reťazcov zotriedený podľa abecedy a jeho používanie reprezentuje následujúcí príklad:

>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__stderr__',
 '__stdin__', '__stdout__', '_getframe', 'argv', 'builtin_module_names',
 'byteorder', 'copyright', 'displayhook', 'exc_info', 'exc_type',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'getdefaultencoding',
 'getdlopenflags', 'getrecursionlimit', 'getrefcount', 'hexversion',
 'maxint', 'maxunicode', 'modules', 'path', 'platform', 'prefix', 'ps1',
 'ps2', 'setcheckinterval', 'setdlopenflags', 'setprofile',
 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'version',
 'version_info', 'warnoptions']
Bez argumentů vrátí seznam jmen, které jsou definovány v aktuálním prostoru jmen:

>>> a = [1, 2, 3, 4, 5]
>>> import fibo, sys
>>> fib = fibo.fib
>>> dir()
['__name__', 'a', 'fib', 'fibo', 'sys']
Seznam vrácený funkcí dir() zahrnuje všechna jména definovaná v objektu, nejde tudíž pouze o proměnné, ale i o funkce, moduly, třídy apod. Do tohoto seznamu nejsou zahrnuta jména interních funkcí a proměnných (tj. těch definovaných modulem __builtin__). Pokud potřebujete seznam interních funkcí použijte

>>> import __builtin__
>>> dir(__builtin__)
['ArithmeticError', 'AssertionError', 'AttributeError',
 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError',
 'Exception', 'FloatingPointError', 'IOError', 'ImportError',
 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt',
 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError', 'OverflowWarning',
 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TypeError', 'UnboundLocalError',
 'UnicodeError', 'UserWarning', 'ValueError', 'Warning',
 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__',
 '__name__', 'abs', 'apply', 'buffer', 'callable', 'chr', 'classmethod',
 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr',
 'dict', 'dir', 'divmod', 'eval', 'execfile', 'exit', 'file', 'filter',
 'float', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id',
 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len',
 'license', 'list', 'locals', 'long', 'map', 'max', 'min', 'object',
 'oct', 'open', 'ord', 'pow', 'property', 'quit', 'range', 'raw_input',
 'reduce', 'reload', 'repr', 'round', 'setattr', 'slice', 'staticmethod',
 'str', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange',
 'zip']

>### Programové balíky

Balíky sú logickým rozšírením mechanizmov Pythonových modulov. V Pythonu je totiž veˇmi rozšírená "bodková notácia" a práve balíky umožňujú hiearchickú organizáciu modulov.

Napríklad modul s menom A.B znamená že modul pomenovaný "B" je umiestnený v balíku "A". **Balíky umožňujú dekompozíciu (rozloženie) rozsiahlých knižníc do menších celkov - modulov**. Autori jednotlivých modulov sa nemusia zajímať o mená globálných premenných ich modulov v tom istom balíku. Programovací jazyk tu zaisťuje vzájomnú "izoláciu" balíkov mezi sebou. Preto sa napríklad autori jednotlivých modulov rozsiahlých balíkov (ako např. NumPy alebo Python Imaging Library) nemusia obávať stretu mien svojich globálných premenných s premennými iného autora.

Predstavte si modelovú situáciu: chcete navrhnúť balík (kolekciu modulov) pre manipuláciu so zvukovými súubormi a zvukovými údajmi obecne. Keďže existuje mnoho rôzných zvukových formátov, potrebujeme vytvoriť a spravovať kolekciu modulov pre konverziu mezi týmito rôznymi formátmi. Také si môžeme predstaviť mnoho operácii, ktoré je možné zo zvukovými údajmi vykonávať (napr. mixovanie stop, pridávanie ozveny, aplikovanie ekvalizéra ...). Postupom času si vytvoríme mnoho modulov pre tieto činnosti. Pre ich organizáciu je mechanizmus balíkov naprosto ideálny. Tu možný štruktúra nášho balíku (zobrazená ako hiearchický súborový systém):
~~~
Sound/                          Hlavný balík
      __init__.py               Inicializýcia balíku
      Formats/                  Balík pre konverziu souborových formátov
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      Effects/                  Balík pre zvukové efekty
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      Filters/                  Balík filtrov
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
~~~

Ak sa pýtate čo znamenajú súbory s podtržníkmi ako napr. __init__.py, tak vedzte že python podľa nich rozpoznáva balíky. A to práve zabraňuje nedorozumeniam aby pzthon nepovažoval ľubovalný adresár nachádzajúci sa v jeho ceste za balík. V najjednoduchšom prípade môže byť napr. súbor __init__.py iba obyčajný prázdny súbor. Môže tu byť ale umiestnený inicializačný kód balíku alebo nastavenie premennej __all__ ktorej význam popíšeme neskôr.

Uživatelia balíkov z nej môžu priamo importovať  jednotlivé moduly:
~~~
import Sound.Effects.echo
~~~
Tento príkaz načíta modul **Sound.Effects.echo**. Jeho premenné a funkcie však musia byť odkazované plným ménom:
~~~
Sound.Effects.echo.echofilter(input, output, delay=0.7, atten=4)
~~~
Inou možnosťou je priame importovanie modulu z balíku: 
~~~
from Sound.Effects import echo
~~~
Tento príkaz tiež načíta modul *echo* a urobí ho  prístupným použitím jeho mena. Funkciu ktorá je v ňom definovaná môžete používať napr.nasledovne:
~~~
echo.echofilter(input, output, delay=0.7, atten=4)
~~~
Ďalšou možnosťou je importovanie určitej funkcie alebo premennej priamo:
~~~
from Sound.Effects.echo import echofilter
~~~
Tento príkaz opäť načíta modul echo, ale urobí jeho funkciu *echofilter()* prístupnú priamo:
~~~
echofilter(input, output, delay=0.7, atten=4)
~~~

Na záver podotknime, že pri importovaní nejakých mien premenný, modulov a pod. s použitím príkazu import môžeme namiesto objektu z ktorého chceme vykonať uviesť iba balík alebo modul. Príkaz 
~~~
from objekt_rôzny_od_modulu_či_balíku import jeho_atribut
~~~
je považovaný za výpočtovú chybu a od tohoto miesta alebo okamihu vstúpi v platnosť výnimka. Ako náhradu takejto konštrukcie môžeme použiť nasledovné:
~~~
jeho_atribut = objekt_rôzny_od_modulu_či_balíku.jeho_atribut
~~~

>### Odkazovanie sa na moduly vo vnútri programového balíka

Často potrebuje jeden modul odkazovať na iný modul toho istého balíku.
Ak výjdeme z nášho modelového príkladu tak modul *surround* bude potrebovať nejakú funkciu z modulu *echo*. V tomto prípade platí nasledujúce: príkaz *import* sa najprv pozrie do aktuálneho balíku a až potom prehľadástandardnú cestu (určenú premennou sys.path). Preto môže modul *surround* jednoducho použiť zápis *import echo*. Keby ale modul nebol súčasťou aktuálneho balíka, tak by prišli na radu štandardné pravidlá pre vyhľadávanie modulu.

Ak je ale balík štruktúrovaný na podriadené balíky (v našom príklade napr. balík *Sound*), neexistuje žiadny spôsob ako sa odkazovať na modul z rodičovského balíku. V takom prípade musíme použiť iné meno. Ak napr. modul *Sound.Filters.vocoder* potrebuje modul *echo* z balíku *Sound.Effect* musí použiť príkaz
~~~
from Sound.Effects import echo
~~~

>### Zásada

**Sila programovacieho jazyka** nie je iba v jeho syntyxi, ale **je predovšetkým v jeho funkciách** ktoré niekto naprogramoval pred Vami a Vám stačí ich iba používať.

Pyton v tejto súvislosti obsahuje sýstém modulov - v podstate sa jedná o súbory v ktorých sú uložené funkcie a do Vášho programu ich musíte iba naimportovať. **Heslo Pythonu je „batterries included“ čo znamená že naozaj veľa vecí je už hotových a dostupných**.

**Čím viac modulov** budete importovať, **tým viac miesta v pamäti** vám bude berať váš program a jeho spustenie a **beh bude o niečo pomalší*. Preto **neimportujte** niečo **čo nepotrebujete**.

Vyskúšame si napr. niektoré funkcie z modulu math

~~~
import math

print(math.sqrt(10))
~~~

Funkcia sqrt() nie je štandardne v základnej inštalácii Pythonu prítomná. Program by v takomto prípade skončil výnimkou (chybou ktorú by trebalo ošetriť výnimkou)
~~~
NameError: name 'math' is not defined
~~~

Modul math obsahuje celú radu zaujímavých vecí ako, např. číslo PI
~~~
print(math.pi)
print(math.e)
~~~

**Importovať môžeme alebo celé moduly, ako to bolo v predchádzajúcom príklade, alebo iba jednotlivé fukcie**, napr. sin().
~~~
from math import sin

print(sin(math.pi/2))
~~~
Ešte niečo zo sveta priestorových a tvarových údajov. Pred tým však treba nainštalovať knižnicu shapley príkazom *pip install shapely*:
~~~
from shapely.geometry import Point

centroid = Point(0.0, 0.0) # vytvoríme nový objekt triedy "Point"
patch = centroid.buffer(10.0) # zavoláme jeho metódu buffer
print(patch.area) # a vytlačíme jeho plochu
~~~
V predchádzajúcom príklade sme z modulu shapely kotrý nám umožňuje pracovať s vektorovými geometriami naimportovali triedu Point a vytvorili sme nový bod. Okolo neho sme vytvorili buffer (dočasné krátkodobé pamäťové miesto) o veľkosti 10-ich jednotiek a vytlačili sme plochu výslednej obalovej zóny.

Trochu sme tým nakukli do sveta objektovo-orientovaného programovania, s ktorým sa blížšie zoznámíme v druhom polroku.

Teraz ešte skúsime obsah vytvoreného buffra vytlačiť vo formáte GeoJSON:
~~~
import json
from shapely.geometry import mapping
from shapely.geometry import Point

centroid = Point(0.0, 0.0) # vytvoríme nový objekt triedy "Point"
patch = centroid.buffer(10.0) # zavoláme jeho metódu buffer
print(json.dumps(mapping(patch)))
~~~

V predchádzajúcom príklade sme na poslednom riadku použili ako vstup pre funkciu print() výstup z funkcie json.dumps() ktorá zase dostala výstup z funkcie mapping(). Nie je to príliž prehľadné, ale takéto konštrukcie sa používajú často.

### Dokumentácia k modulom

Je na čase, aby sme sa zoznámili s príkazom **pydoc** (alebo pydoc3), ktorý ako parameter dostane modul a prevedie vás po jeho dokumentácii Napr. pre modul shapely by to vyzeralo takto :
~~~
$ pydoc shapely
~~~
~~~
Help on package shapely.geometry in shapely:

NAME
    shapely.geometry - Geometry classes and factories

FILE
    /home/jachym/.local/lib/python2.7/site-packages/shapely/geometry/__init__.py

PACKAGE CONTENTS
    base
    collection
    geo
    linestring
    multilinestring
    multipoint
    multipolygon

...
~~~

Google nám tiež vždycky dobre poradí ak správne hľadáte a zoznam modulov distribuovaných spolu s jazykom Python nájdete na dokumentačnej stránke jazyka Python.

### Vlastné moduly

Ak uložíme program do súboru, tak sa týmto váš súbor stáva modulom ktorý je možné použíť a naimportovať.

Vytvoríme súbor buffer.py s následujúcim obsahom:
~~~
from shapely.geometry import Point
from shapely.geometry import mapping, shape

def udelej_buffer(geometry, velikost):
    """Vrátí buffer ve formátu GeoJSON pro zadanou geometrii
    """

    geometrie = shape(geometry)
    buffer = geometrie.buffer(velikost)
    return  mapping(buffer)
~~~
Teraz môžeme v inom programe (alebo priamo v interpreteru) naš modul použiť:
~~~
>>> import buffer
>>> moj_bod = {"type": "Point", "coordinates": [0.0, 0.0]}
>>> buffer.udelej_buffer(moj_bod, 3)
{
    'type': 'Polygon',
    'coordinates': ((
        (3.0, 0.0),
        (2.9855541800165906, -0.29405142098868153),
        (2.9423558412096917, -0.5852709660483842),
        (2.8708210071966267, -0.8708540317633864),
        (2.771638597533861, -1.1480502970952682),
        (2.6457637930450657, -1.4141902104779915),
        (2.4944088369076365, -1.6667106990588052),
        (2.3190313600882124, -1.903179852490935),
        (2.1213203435596446, -2.1213203435596406),
        (1.903179852490939, -2.319031360088209),
        (1.6667106990588092, -2.4944088369),
        ...
    ))
}
~~~

Moduly nám teda umožňujú usporiadať časti programu ktoré spolu súvisia do do logických celkov a rozsekať rozsiahlé programy do menších súborov a štrukturovať tak kód aby bol prehľadnejší pri používaní.

[Abecedný zoznam Pythonových modulov](https://docs.python.org/3/py-modindex.html)

### Dva typy modulov: programy a knižnice

Všetko sú súbory .py a v tomto rozdiel nie je. **Programy (skripty)** sú primárne **určené k spúšťaniu** a predstavujú často vstupný bod nejakej aplikácie.

**Knižnice** sú určené **k importu** do iných knižníc a programov.

Často ale môžeme ten istý modul využiť aj ako skript (môžeme ho spustiť a on urobí niečo užitečného) aj ako knižnicu (môžeme ho importovať do iných modulov)

K téme **Vlastne moduly** najdeme kvalitné video od Miša Hucka
https://www.youtube.com/watch?v=ea6R0ZygfLM 

>### Pridanie modulu do cesty Python

Druhou možnosťou, ktorú máme, je **pridať modul na cestu**, kde Python kontroluje moduly a balíky. Toto je trvanlivejšie riešenie pre náš modul, vďaka ktorému **je modul dostupný v celom prostredí alebo v celom systéme**, vďaka čomu je táto metóda prenosnejšia. Naviac knižnice ktoré si sťahujeme prechádzajú prirodzeným vývojom a aktualizáciou ktorá môže spôsobiť pre staršie programy so staršími verziami knižníc problémy. Preto **je veľmi dôležité viesť** ku každej aplikácii zoznam použitých knižníc v súbore **requirements.txt** a tento zoznam si pozrieť aj pri preberaní kódu od cudzích autorov!

Ak chcete **zistiť, akú cestu Python kontroluje**, spustite interpret Pythonu z vášho programovacieho prostredia príkazom:
~~~
$ python3 resp. iba python
~~~
Ďalej importujte modul sys:
~~~
>>> import sys
~~~
A potom nechajte Python vytlačiť systémovú cestu:
~~~
>>> print(sys.path)
~~~

Tak dostanete nejaký výstup s aspoň jednou systémovú cestu. V programovacom prostredí môžete získať aj niekoľko takýchto ciest. Vás zaujíma predovšetkým cesta kde sa nachádza príslušný modul t.j. chcete hľada+t cestu pre modul, ktorý sa nachádza v prostredí (adresár), ktoré práve používate. Ale možno budete chcieť pridať modul aj do hlavnej cesty systému Python. Tak to, čo hľadáte, bude podobné tomuto a okrem /site-packages môžu byť v ostatných častiach zmeny ako napr. nie *python3.5* ale *Python311* apod.:
~~~
'/usr/sammy/my_env/lib/python3.5/site-packages'
~~~

Teraz môžete presunúť svoj súbor *hello.py* ktorý chcete používať ako modul do tohto adresára a bude zovšadiaľ prístupný. Po dokončení môžete importovať *modul ahoj* ako zvyčajne:
~~~
import hello
...
~~~
a keď spustíte program, mal by sa dokončiť bez ohlásenia chyby že mu chýba modul ahoj.

Úprava cesty k vášmu modulu môže zabezpečiť, že budete mať prístup k modulu bez ohľadu na to, v ktorom adresári sa nachádzate. **Je to užitočné najmä vtedy, ak máte viac ako jeden projekt odkazujúci na konkrétny modul**.

[SPÄŤ](../../Obsah.md)
