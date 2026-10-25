# Jak pomóc

Dziękujemy za każdą poprawkę. Małe, konkretne pull requesty najłatwiej przejrzeć.

1. Przy większej zmianie najpierw otwórz issue, żebyśmy uzgodnili kształt.
2. Pisz prostą, poprawną polszczyzną, z polskimi znakami, bez półpauz i pauz
   (zamiast nich przecinek, dwukropek albo kropka). Testy to sprawdzają.
3. Nie dodawaj do przykładów ani testów profili, cytatów ani danych prawdziwych
   osób. Używaj fikcyjnych person. Instytucje w `references/rynek.md` mogą być
   prawdziwe, bo są publiczne i służą tylko jako przykłady miejsc pracy person.
4. Przed pull requestem uruchom testy:

   ```bash
   python -m unittest discover -s tests -v
   ```

5. Dopisz zmianę do `CHANGELOG.md` w sekcji „Unreleased”.

Wysyłając zmianę, zgadzasz się na jej udostępnienie na licencji MIT tego
repozytorium.
