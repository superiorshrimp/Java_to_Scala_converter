# Java to Scala converter

Projekt z przedmiotu Metod i Algorytmów Kompilacji

Wymagania:<br />
&nbsp;&nbsp;&nbsp;&nbsp;-> ANTLR 4.11.1<br />
&nbsp;&nbsp;&nbsp;&nbsp;-> Python 3.9 (oraz biblioteki:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> antlr python runtime: `pip install antlr4-python3-runtime`<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> inspect: `pip install inspect`<br />

Jak włączyć?<br />
1. Wejść do folderu /main<br />
2. Wpisać komendę uruchamiającą plik run.py (`python run.py`)
3. Wygenerowany zostanie plik w Scali result.scala. Działanie wygenerowanego kodu można sprawdzić na stronie https://scastie.scala-lang.org/, (trzeba się upewnić, że w "Build Settings" została wybrana wesja Scali 2.13.10 dla na która kompilowany jest kod z Javy). 

Aby wybrać źródłowy kod w Javie do przekonwertowania należy dodać jego lokalizację w stosunku do folderu /main do komendy pythonowej (`python run.py ./folder1/folder2/folder3/kod_w_javie.java`)
