W naszym interfejsie Agent-Środowisko:
  * mamy agenta, który jest naszym podmiotem decyzyjnym,
  * środowisko na które agent może wpływać tworząc nowe środowisko z nowymi nagrodami.

Wykonujemy te czynności w dyskretnym okresie czasu (T),
a stany są oznaczone przez ![SsubT]( http://latex.codecogs.com/png.latex?S_%7BT%7D),
który jest zbiorem wszystkich możliwych stanów.

Akcje są oznaczone przez A, które są wszystkimi możliwymi akcjami w danym czasie.
I mamy nasze nagrody, ![RsubT]( http://latex.codecogs.com/png.latex?R_%7BT%7D), Zbiór wszystkich nagród.
I politykę oznaczoną przez ![pi]( http://latex.codecogs.com/png.latex?%5Cpi).

Agent wykonuje akcje, środowisko to akceptuje określa nowy stan i nagrodę. Agent to analizuje i decyduje o następnej akcji i tak dalej aż do osiągnięcia pożądanych rezultatów.


Do projektowania modelu musimy określić zbiór stanów, nagród, akcji oraz prawdopodobieństwo przejścia przez dany stan.

W przypadku robota może to wyglądać tak:
- ciało robota jest częścią środowiska
- agent uczy się operowanie nad ciałem 
- pozwala na zdefiniowanie problemu RL jeśli określimy cele i nagrody

Nagroda naszyb celem nie ważne jak złozona ona może być, to przedstawienie jej jako pojedyńczej liczby rzeczywistej.
Returns to suma wszystkich nagród od czasu T, ![returns](http://latex.codecogs.com/png.latex?G_%7Bt%7D%20%3D%20R_%7Bt&plus;1%7D&plus;R_%7Bt&plus;2%7D&plus;%20...%20&plus;%20R_%7BT%7D)
