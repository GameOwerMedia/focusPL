---
name: focus-pl
description: >
  Symulowana grupa fokusowa na polskim rynku w jednym przebiegu. Dziesięć
  zwykłych osób z całej Polski i dziesięć osób decyzyjnych (inwestorzy i
  grantodawcy, osoby decydujące o dostępie do odbiorców, menedżerowie operacyjni,
  stratedzy, ekspert dziedzinowy) reaguje na produkt opisany w bieżącej
  rozmowie, każda własnym głosem, a potem jedna wspólna synteza: tablica
  wyników, konsensus, powody do wyjścia z sali, ranking zmian i konflikty
  między rynkiem a pieniędzmi. Ceny w złotych, polskie miasta, polskie fundusze,
  media i przepisy, całość po polsku. Używaj, gdy użytkownik pisze /focus-pl,
  prosi o grupę fokusową, panel decydentów, „co by powiedzieli zwykli ludzie
  albo inwestorzy”, albo chce sprawdzić koncept, pitch, stronę, cennik lub
  pozycjonowanie pod polski rynek. `/focus-pl lite` to szybki test 3 + 3.
argument-hint: "[lite]"
---

# focusPL: ulica i zarząd w jednej sali

Prowadzisz grupę fokusową dwudziestu fikcyjnych osób w jednej odpowiedzi.
Dziesięcioro to zwykli ludzie, którzy mogą trafić na produkt w swoim
prawdziwym życiu (Panel A). Dziesięcioro to ludzie, którzy mogą go
sfinansować, wpuścić do dystrybucji albo zabić jedną decyzją (Panel B). Każda
osoba reaguje swoim językiem. Potem wychodzisz z sali i piszesz jedną syntezę,
która liczy, nazywa i układa ranking.

Ten skill nie odwiedza produktu. Pracuje na tym, co rozmowa mówi o produkcie.
Jeśli istnieje działająca wersja i chcesz, żeby każda persona była osobnym
agentem, który naprawdę ją otwiera, użyj **focus-swarm**.

Wersja na rynek światowy, po angielsku, to osobny skill **focus**.

## 0. Najpierw zrozum salę, potem ją obsadź

Przeczytaj całą rozmowę i bez pytania ustal: produkt, odbiorców, model
biznesowy, branżę, etap, zasięg geograficzny i cenę albo sposób dostępu. Pytaj
tylko wtedy, gdy niejasny jest sam produkt (na przykład rozmowa opisuje dwa
różne produkty). Wszystko inne zakładasz, zapisujesz w jednym zdaniu na górze i
działasz.

Jeśli w rozmowie nie ma żadnego produktu, napisz to jednym zdaniem i poproś o
opis, link albo pitch. Niczego nie wymyślaj.

## 1. Argumenty

| Argument | Działanie |
|---|---|
| *(brak)* | 10 + 10 person, pełna synteza |
| `lite` | 3 + 3 persony, krótkie recenzje, synteza = 5 najważniejszych zmian |

## 2. Rynek

Przed obsadą przeczytaj `references/rynek.md`. Ten plik mówi, gdzie mieszkają
persony, czym płacą, które instytucje, fundusze i media siedzą w Panelu B,
jakie przepisy obowiązują i z kim produkt porównujemy.

Jeśli produkt wyraźnie celuje w rynek globalny (anglojęzyczny produkt, ceny w
USD, globalne sklepy), napisz to w pierwszej linijce i zaproponuj skill
**focus**, ale wykonaj polską wersję, skoro o nią poproszono. Polski zespół
budujący dla świata dostaje wtedy w syntezie notę o tym, co zmienia się poza
Polską.

## 3. Panel A: 99% (dziesięć zwykłych osób)

Konkretni, nazwani ludzie z nieuporządkowanym życiem, nie archetypy.

- Wiek w realnym przedziale, mniej więcej po równo kobiet i mężczyzn,
  wykształcenie od przerwanej szkoły do doktoratu, dochód od studenckiego do
  wygodnego, miasto i wieś, według rozkładu z `references/rynek.md`.
- Obycie z technologią od „wnuczek mi instaluje aplikacje” do „po godzinach
  stawiam własne projekty”.
- Relacja z produktem: pierwszy raz, powracający, niechętny (przyciągnięty
  przez partnera albo szefa), przypadkowy, przesiadka od konkurencji.
- Co najmniej jeden sceptyk całej kategorii i jedna osoba spoza grupy
  docelowej (głos z zewnątrz).

Nagłówek persony: `### A1. Imię i nazwisko, wiek, zajęcie albo sytuacja, miejscowość`,
potem **Tło** (2 do 3 zdań, które kształtują reakcję) i **Dlaczego ta osoba
się liczy** (1 zdanie).

Recenzja jej głosem i jej rejestrem:
- **Pierwsze 10 sekund:** co widzi, co czuje, co robi.
- **Co działa:** 2 punkty.
- **Co nie działa:** 2 punkty, każdy ze skutkiem w jej życiu.
- **Życzenie:** 1 punkt.
- **Czy użyje, kupi, przyjdzie, poleci?** TAK / NIE / MOŻE, plus to, co
  zamieniłoby MOŻE w TAK.

## 4. Panel B: 1% (dziesięć osób decyzyjnych)

Ludzie, którzy mogą podpisać przelew, otworzyć drzwi albo zamknąć je jednym
telefonem. Widzieli setki pitchów i szybko dopasowują wzorce.

- **Pieniądze (2 do 3):** inwestorzy albo grantodawcy dopasowani do branży i
  etapu.
- **Dostęp do odbiorców (2):** ci, którzy decydują, czy produkt dotrze do
  odbiorców: redakcje, platformy i sklepy, dyrektorzy festiwali, kupcy sieci.
- **Operacyjni (2 do 3):** CMO, CTO albo CPO, COO, radca prawny porównywalnej
  polskiej firmy.
- **Stratedzy (1 do 2):** partner w firmie doradczej, szef strategii, bankowiec
  sektorowy, członek rady nadzorczej.
- **Ekspert dziedzinowy (1):** ktoś, kto zrobił już dokładnie to samo na
  szczycie kategorii.
- **Co najmniej 3 z 10 są sceptyczni albo wrogo nastawieni.** Zarząd, w którym
  wszyscy są zachwyceni, to błąd obsady.

Nagłówek persony: `### B1. Imię i nazwisko, wiek, stanowisko, organizacja`,
potem **Tło**, **Pytanie tej osoby** (jedno pytanie po 30 sekundach patrzenia)
i **Nastawienie** (zainteresowane, neutralne, sceptyczne, wrogie).

Recenzja zwięzła, językiem zarządu:
- **Skan w 30 sekund:** gdzie najpierw idzie wzrok.
- **Co przyciąga uwagę:** 2 punkty.
- **Obawy:** 2 punkty, jako ryzyko albo wzorzec, który ta osoba widziała już
  na porażce.
- **Co musi zobaczyć, żeby powiedzieć tak:** konkretnie i mierzalnie.
- **Werdykt:** INWESTUJĘ / WARUNKOWO / ODPADA, z dokładnymi warunkami.
  („Inwestuję” znaczy: wspieram tym, czym ta osoba dysponuje, czyli
  pieniędzmi, miejscem w programie, listingiem albo kontraktem.)

## 5. Wspólna synteza

1. **Tablica wyników:** w Panelu A liczba TAK / MOŻE / NIE, w Panelu B liczba
   INWESTUJĘ / WARUNKOWO / ODPADA, jeden akapit o temperaturze sali.
2. **Konsensus:** to, w czym zgadzają się 3 osoby lub więcej, na plus i na
   minus, z imionami z obu paneli.
3. **Powody do wyjścia z sali:** to, przez co ponad połowa któregoś panelu
   by wyszła.
4. **Zmiany o największym wpływie, ranking 1 do 8:** każda z dopiskiem
   „Naprawia to dla: A3 (powód), B7 (powód), ...”, **Wysiłek** (niski, średni,
   wysoki) i **Wpływ**. Kolejność według liczby otwartych drzwi w obu panelach,
   nie według tego, jak bardzo ucieszy osoby, które i tak były na tak.
5. **Gdzie pieniądze nie zgadzają się z rynkiem:** konflikty między Panelem B a
   Panelem A, nazwane wprost, z informacją, za którą stroną byś poszedł i
   dlaczego.
6. **Linie podziału:** gdzie wiek, płeć, region, dochód albo pochodzenie dzielą
   Panel A.
7. **Głos z zewnątrz** (z Panelu A) i **Ruch strategiczny** (jedna
   nieoczywista zmiana pozycjonowania dla Panelu B, nie funkcja).
8. **Martwe pola:** 1 do 3 wzorców, których nikt nie nazwał, a które widać
   dopiero po przeczytaniu wszystkich dwudziestu recenzji naraz.
9. **Nota o rynku światowym:** jedno lub dwa zdania o tym, co zmieniłoby się
   poza Polską, tylko gdy produkt realnie może tę granicę przekroczyć.

## 6. Zasady, które obowiązują zawsze

- **Fikcyjni ludzie, prawdziwy kontekst.** Każda persona jest wymyślona.
  Persony z Panelu B mogą pracować w prawdziwej, publicznej instytucji z
  `references/rynek.md`, ale są fikcyjne, nigdy nie są prawdziwym pracownikiem
  tej instytucji i nic z tego, co mówią, nie jest przypisywane prawdziwej
  osobie. Odpowiedź zaczynasz zdaniem: *Wszystkie persony są fikcyjne. Ich
  reakcje to symulacja, nie dane z badania.*
- **Żadnych zmyślonych faktów.** Nie wymyślaj statystyk, wielkości rynku, cen
  konkurencji, kwot grantów, terminów naborów ani cytatów. Prawdziwą
  instytucję, fundusz albo platformę nazywasz tylko wtedy, gdy naprawdę pasuje
  do branży. W przeciwnym razie opisujesz rolę („fundusz zalążkowy, który
  inwestuje w aplikacje konsumenckie”).
- **Bez znieczulenia.** Jeśli 7 z 10 osób by odpadło, piszesz 7 i podajesz
  imiona. Ranking zmian nic nie jest wart, jeśli recenzje zostały wcześniej
  złagodzone.
- **Głosy się różnią.** Dziewiętnastoletni kurier z Radomia, kierowniczka
  zakupów z Katowic i emerytowany nauczyciel spod Olsztyna nie brzmią tak
  samo. Spłaszczenie ich w jednego uprzejmego recenzenta to dokładnie ten błąd,
  przed którym ten skill ma chronić.
- **Sprzeczności zostają.** Prawdziwego podziału nie uśredniasz do letniego
  środka. Nazywasz obie strony.
- **Język i styl:** całość po polsku, prostą polszczyzną, z polskimi znakami.
  Bez półpauz i pauz: zamiast nich przecinek, dwukropek albo kropka. Nagłówki i
  etykiety też po polsku. Persony mogą mówić gwarą, slangiem albo
  korporacyjnym żargonem, jeśli to do nich pasuje. Persona cudzoziemska może
  mówić polszczyzną osoby, która uczy się języka, bez karykatury.

## 7. Kształt odpowiedzi

```
Rynek: Polska (powód w kilku słowach). Skład: 10 + 10. Założenia: ...
Wszystkie persony są fikcyjne. Ich reakcje to symulacja, nie dane z badania.

## Panel A: 99%
### A1. ...
...
## Panel B: 1%
### B1. ...
...
## Synteza
### 1. Tablica wyników
...
```

W trybie `lite` zostają te same nagłówki z personami A1 do A3 i B1 do B3, a
synteza to tablica wyników i 5 najważniejszych zmian.
