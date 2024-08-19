This project is from exercises by M.Sroczyñska.

Full original task command is below, in Polish language.

tldr: We have a garden with 3 cats' types, and one type of mice.
Each animal type has its own move pattern and reaction between cat and mouse.
The program ends with showing where our animals were during all day (prined on the map).




Task:
W du¿ym kwadratowym ogrodzie ¿yje gromadka kotów i sporo myszy. 
Od rana koty uganiaj¹ siê za myszami i wydeptuj¹ œcie¿ki. 
Czasem kot i mysz mog¹ spotkaæ siê w jednym miejscu. 
Jak koñczy siê taka sytuacja? To zale¿y (opis mo¿liwych scenariuszy poni¿ej). 
Wieczorem na trawie widaæ œcie¿ki wydeptane przez zwierzêta. 
Na pocz¹tku symulacji umieszczamy koty i myszy w ogródku. 
Lista po³o¿eñ pocz¹tkowych (czyli po³o¿eñ kocich pude³ek/mysich norek) 
wszystkich kotów i myszy wczytywana jest z plików, 
których opis znajduje siê nieco dalej. 
Na jej podstawie nale¿y stworzyæ wszystkie obiekty reprezentuj¹ce zwierzêta. 
Wci¹gu dnia zarówno koty, jak i myszy poruszaj¹ siê po ogrodzie, 
ka¿dy na swój sposób: 
	Myszy s¹ ma³e, wiêc robi¹ ma³e kroczki. 
	W jednym momencie mog¹ co najwy¿ej zmieniæ swoj¹ pozycjê (x, y) o 1 
	(lub nie zmieniæ wcale) w ka¿dym kierunku. 
	Wyj¹tek stanowi ucieczka, wtedy mysz nabiera supermocy i teleportuje siê 
	do swojego schronienia, niezale¿nie jak to daleko. 

	Koty Przeciêtniaki oraz Koty Leniuchy poruszaj¹ siê w losowym kierunku 
	zmieniaj¹c po³o¿enie o co najwy¿ej 10, zarówno w kierunku x, jak i y. 

	Kociaki poruszaj¹ siê w losowym kierunku, zmieniaj¹ swoj¹ pozycjê 
	(ka¿d¹ wspó³rzêdn¹) o co najwy¿ej 5, ale nigdy nie oddalaj¹ siê 
	od swojego domu o odleg³oœæ wiêksz¹ ni¿ 100. 
	Jeœli nowe po³o¿enie sprawi³oby, ¿e kociak oddali siê od domu o ponad 100, 
	to zamiast tego wraca do poprzedniego po³o¿enia. 

Uwaga: Ka¿dy zwierzak pamiêta wszystkie swoje po³o¿enia. 
Jeœli mysz znajdzie siê w odleg³oœci mniejszej ni¿ 4 od kota, 
to nastêpuje ich spotkanie. Spotkanie kota i myszy mo¿e przebiegaæ ró¿nie: 
	Koty Przeciêtniaki, których jest najwiêcej, 
	po prostu zawsze tr¹caj¹ mysz ³apk¹, ona teleportuje siê do swojego domku, 
	a kot jest zadowolony. 

	Kociaki s¹ bardzo m³ode i praktycznie zawsze boj¹ siê myszy, 
	a gdy j¹ spotkaj¹, natychmiast teleportuj¹ siê do swojego pud³a. 
	Mysz nadal normalnie spaceruje sobie po ogródku. 
	Jednak je¿eli jakimœ cudem spotkaj¹ mysz w pobli¿u 
	swojego pude³ka (w promieniu 50), wtedy staj¹ siê odwa¿ne 
	i potrafi¹ przestraszyæ gryzonia na tyle, ¿e tym razem to on teleportuje siê 
	natychmiast do swojej kryjówki. 

	Koty Leniuchy s¹ wzglêdnie niegroŸne. 
	Gdy spotkaj¹ mysz, nawet w swoim mieszkanku, 
	czêsto zupe³nie siê ni¹ nie przejmuj¹ i po spotkaniu ka¿de z nich 
	idzie w swoj¹ stronê jak gdyby nic siê nie sta³o. 
	Czasem jednak kot tr¹ca mysz ³apk¹, ta ucieka (teleportuje siê) do kryjówki, 
	a kot jest zadowolony, ¿e pogoni³ gryzonia. 
	To, czy kot jest akurat zainteresowany mysz¹, jest losowe. 
	Zale¿y jednak od liczby przegonionych ju¿ myszy. 
	Im jest ich wiêcej, tym kotu jednak bardziej siê chce. 
	Prawdopodobieñstwo zainteresowania wynosi 1 1+e-0.1n , 
	gdzie n to liczba dotychczas przegonionych myszy. 

Ca³y dzieñ trwa kilkaset iteracji, a ca³a symulacja to jeden dzieñ. 
Po zakoñczeniu symulacji chcemy zobaczyæ wszystkie œcie¿ki 
wydeptane w trawie przez koty i myszy. 

Pliki z danymi. 
Za pomoc¹ dowolnego programu (lub rêcznie) nale¿y stworzyæ pliki tekstowy, 
który w ka¿dej linijce zawiera dwie liczby oddzielone spacj¹- 
po³o¿enia pocz¹tkowe x i y jednego zwierzaka. 
Dane dla ka¿dego typu zwierz¹t powinny znaleŸæ siê w osobnym pliku 
(3 typy kotów + myszy › w sumie 4 pliki). 
Po³o¿enia powinny byæ liczbami ca³kowitymi nieujemnymi, 
¿aden zwierzak nie powinien te¿ znajdowaæ poza ogrodem. 
Nale¿y stworzyæ po kilka zwierz¹t ka¿dego typu. 
Po zakoñczeniu symulacji chcemy zobaczyæ œcie¿ki wydeptane 
przez wszystkie zwierzêta. Jako ¿e ka¿de zwierzê pamiêta 
wszystkie swoje po³o¿enia, wystarczy narysowaæ wykres 
przedstawiaj¹cy kolejno po³¹czone punkty. 
Mo¿na to zrobiæ u¿ywaj¹c Matplotlib i polecenia plot.