This project is from exercises by M.Sroczy�ska.

Full original task command is below, in Polish language.

tldr: We have a garden with 3 cats' types, and one type of mice.
Each animal type has its own move pattern and reaction between cat and mouse.
The program ends with showing where our animals were during all day (prined on the map).




Task:
W du�ym kwadratowym ogrodzie �yje gromadka kot�w i sporo myszy. 
Od rana koty uganiaj� si� za myszami i wydeptuj� �cie�ki. 
Czasem kot i mysz mog� spotka� si� w jednym miejscu. 
Jak ko�czy si� taka sytuacja? To zale�y (opis mo�liwych scenariuszy poni�ej). 
Wieczorem na trawie wida� �cie�ki wydeptane przez zwierz�ta. 
Na pocz�tku symulacji umieszczamy koty i myszy w ogr�dku. 
Lista po�o�e� pocz�tkowych (czyli po�o�e� kocich pude�ek/mysich norek) 
wszystkich kot�w i myszy wczytywana jest z plik�w, 
kt�rych opis znajduje si� nieco dalej. 
Na jej podstawie nale�y stworzy� wszystkie obiekty reprezentuj�ce zwierz�ta. 
Wci�gu dnia zar�wno koty, jak i myszy poruszaj� si� po ogrodzie, 
ka�dy na sw�j spos�b: 
	Myszy s� ma�e, wi�c robi� ma�e kroczki. 
	W jednym momencie mog� co najwy�ej zmieni� swoj� pozycj� (x, y) o 1 
	(lub nie zmieni� wcale) w ka�dym kierunku. 
	Wyj�tek stanowi ucieczka, wtedy mysz nabiera supermocy i teleportuje si� 
	do swojego schronienia, niezale�nie jak to daleko. 

	Koty Przeci�tniaki oraz Koty Leniuchy poruszaj� si� w losowym kierunku 
	zmieniaj�c po�o�enie o co najwy�ej 10, zar�wno w kierunku x, jak i y. 

	Kociaki poruszaj� si� w losowym kierunku, zmieniaj� swoj� pozycj� 
	(ka�d� wsp�rz�dn�) o co najwy�ej 5, ale nigdy nie oddalaj� si� 
	od swojego domu o odleg�o�� wi�ksz� ni� 100. 
	Je�li nowe po�o�enie sprawi�oby, �e kociak oddali si� od domu o ponad 100, 
	to zamiast tego wraca do poprzedniego po�o�enia. 

Uwaga: Ka�dy zwierzak pami�ta wszystkie swoje po�o�enia. 
Je�li mysz znajdzie si� w odleg�o�ci mniejszej ni� 4 od kota, 
to nast�puje ich spotkanie. Spotkanie kota i myszy mo�e przebiega� r�nie: 
	Koty Przeci�tniaki, kt�rych jest najwi�cej, 
	po prostu zawsze tr�caj� mysz �apk�, ona teleportuje si� do swojego domku, 
	a kot jest zadowolony. 

	Kociaki s� bardzo m�ode i praktycznie zawsze boj� si� myszy, 
	a gdy j� spotkaj�, natychmiast teleportuj� si� do swojego pud�a. 
	Mysz nadal normalnie spaceruje sobie po ogr�dku. 
	Jednak je�eli jakim� cudem spotkaj� mysz w pobli�u 
	swojego pude�ka (w promieniu 50), wtedy staj� si� odwa�ne 
	i potrafi� przestraszy� gryzonia na tyle, �e tym razem to on teleportuje si� 
	natychmiast do swojej kryj�wki. 

	Koty Leniuchy s� wzgl�dnie niegro�ne. 
	Gdy spotkaj� mysz, nawet w swoim mieszkanku, 
	cz�sto zupe�nie si� ni� nie przejmuj� i po spotkaniu ka�de z nich 
	idzie w swoj� stron� jak gdyby nic si� nie sta�o. 
	Czasem jednak kot tr�ca mysz �apk�, ta ucieka (teleportuje si�) do kryj�wki, 
	a kot jest zadowolony, �e pogoni� gryzonia. 
	To, czy kot jest akurat zainteresowany mysz�, jest losowe. 
	Zale�y jednak od liczby przegonionych ju� myszy. 
	Im jest ich wi�cej, tym kotu jednak bardziej si� chce. 
	Prawdopodobie�stwo zainteresowania wynosi 1 1+e-0.1n , 
	gdzie n to liczba dotychczas przegonionych myszy. 

Ca�y dzie� trwa kilkaset iteracji, a ca�a symulacja to jeden dzie�. 
Po zako�czeniu symulacji chcemy zobaczy� wszystkie �cie�ki 
wydeptane w trawie przez koty i myszy. 

Pliki z danymi. 
Za pomoc� dowolnego programu (lub r�cznie) nale�y stworzy� pliki tekstowy, 
kt�ry w ka�dej linijce zawiera dwie liczby oddzielone spacj�- 
po�o�enia pocz�tkowe x i y jednego zwierzaka. 
Dane dla ka�dego typu zwierz�t powinny znale�� si� w osobnym pliku 
(3 typy kot�w + myszy � w sumie 4 pliki). 
Po�o�enia powinny by� liczbami ca�kowitymi nieujemnymi, 
�aden zwierzak nie powinien te� znajdowa� poza ogrodem. 
Nale�y stworzy� po kilka zwierz�t ka�dego typu. 
Po zako�czeniu symulacji chcemy zobaczy� �cie�ki wydeptane 
przez wszystkie zwierz�ta. Jako �e ka�de zwierz� pami�ta 
wszystkie swoje po�o�enia, wystarczy narysowa� wykres 
przedstawiaj�cy kolejno po��czone punkty. 
Mo�na to zrobi� u�ywaj�c Matplotlib i polecenia plot.