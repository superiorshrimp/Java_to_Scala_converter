# Java to Scala compiler

Projekt z przedmiotu Metody i Algorytmy Kompilacji

Wymagania:<br />
&nbsp;&nbsp;&nbsp;&nbsp;-> ANTLR 4.11.1<br />
&nbsp;&nbsp;&nbsp;&nbsp;-> Python 3.9 oraz biblioteki:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> antlr python runtime: `pip install antlr4-python3-runtime`<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> inspect: `pip install inspect`<br />

Jak włączyć?<br />
1. Wejść do folderu /main<br />
2. Wpisać komendę uruchamiającą plik run.py (`python run.py`)
3. Wygenerowany zostanie plik w Scali result.scala. Działanie wygenerowanego kodu można sprawdzić na stronie https://scastie.scala-lang.org/, (trzeba się upewnić, że w "Build Settings" została wybrana wesja Scali 2.13.10 dla na która kompilowany jest kod z Javy). 

Aby wybrać źródłowy kod w Javie do przekonwertowania należy dodać jego lokalizację w stosunku do folderu /main do komendy pythonowej (`python run.py ./folder1/folder2/folder3/kod_w_javie.java`)

Uwagi: <br />
&nbsp;&nbsp;&nbsp;&nbsp;-> lexer i parser obsługują duży podzbiór Javy (wszystkie przykładowe pliki z /main/java_examples)<br />
&nbsp;&nbsp;&nbsp;&nbsp;-> sama konwersja obsługuje mały podzbiór Javy (tworzenie zmiennych, działania na zmiennych, wypisywanie ich oraz deklarowanie klas)<br />
&nbsp;&nbsp;&nbsp;&nbsp;-> po konwersji plik w Scali można sformatować dowolnym internetowym lub wbudowanych w IDE formatterem, aby kod ładnie wyglądał (dodanie odpowiednich wcięć itd.)<br />
