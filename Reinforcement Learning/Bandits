Podstawowe wyzwania dla RL:
	•	Reprezentacja stanów środowiska.
	•	Generalizacja od szkolenia do innych możliwych stanów środowiska.
	•	Eksploracja stanów lub akcji, które nie są optymalne.
	•	Szacowanie w ograniczonym czasie celem znalezienia optymalnej polityki

Pojęcie jednoręcznych bandytów jako sposób badania problemu eksploracji i eksploatacji.

Bandits 
stałe ograniczony zestaw zasobów musi być rozdzielona między alternatywne/konkurencyjne wybory w sposób, który maksymalizuje ich oczekiwany zysk, gdy właściwości każdego wyboru są tylko częściowo znane w danym momencie, i mogą stać się lepiej rozumiane wraz z upływem czasu lub poprzez przydzielanie zasobów.
	•	Epsilon-greedy
		Chciwie wykorzystujemy czas na eksploatacje a pozostałą cześć czasu eksplorujemy albo wykonujemy losowe akcje.
	•	Regret
		Czekamy aż algorytm zwróci wszystkie optymalne akcje w obecnym stanie.
	•	UCB
		Rozwiązanie Regret z naszą polityką.
	•	Thompson Sampling
		Szacujemy optymalną politykę po przez próbkowanie.

Agent, który podejmuje pewne kroki eksploracyjne wraz z chciwą strategii, zbiegnie się do optymalnej polityki przy jednoczesnym zdobyciu informacji w celu ulepszenia polityki.
Dlaczego generalizacja jest ważne w RL?
Agent, który generalizuje:
	•	będzie w stanie zapewnić dobre rozwiązania w obliczu stanów i opcji działania, których wcześniej nie spotkałem.
	•	będzie w stanie rozwiązywać złożone problemy, w których liczba stanów jest bardzo duża.
	•	będzie mógł wybierać akcje z dużej liczby możliwości.

Algorytm UCB wybiera akcję z największą niepewnością dla nagrody, celem jej zmniejszenia. 
Uczenie kontekstowe a RL?
Konkretny bandyta podejmuje działania i otrzymuje nagrody, które mogą zależeć od stanu, podczas gdy agent RL podejmuje działania w celu zmiany stanu i otrzymania nagrody. 
