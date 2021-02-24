from jedzonko.views import Plan, Recipe

old_recipes = Recipe.objects.all()
old_recipes.delete()

r1 = Recipe.objects.create(name="Zupa meksykańska z ogórkiem i papryką ",
                           ingredients=""" czerwona fasola - 1 puszka
ogórki konserwowe - 5 sztuk
papryka konserwowa czerwona - 4 sztuki
kukurydza - 1 puszka
Fix Chili con carne Knorr - 1 opakowanie
cebula czerwona - 1 sztuka
przecier pomidorowy - 2 łyżki
Kmin rzymski z Indii mielony Knorr - 1 łyżeczka
ząbki czosnku - 2 sztuki
kolendra - 1 pęczek
woda - 1.5 litra """,
                           description="Pikantna zupa meksykańska.",
                           preparation_time=40,
                           preparation_method="""Krok 1
W dużym garnku podsmaż na oleju posiekaną cebulę i czosnek.
Zupa meksykańska z ogórkiem i papryką - Krok 1
Krok 2
Po chwili smażenia dodaj mielony kumin oraz koncentrat pomidorowy. Całość smaż jeszcze 3-4 minuty.
Zupa meksykańska z ogórkiem i papryką - Krok 2
Krok 3
Fix Knorr wymieszaj z wodą. Zalej podsmażone składniki płynem i zagotuj.
Zupa meksykańska z ogórkiem i papryką - Krok 3
Krok 4
Kukurydzę i fasolkę odcedź. Ogórki i paprykę pokrój w drobną kostkę i dodaj wszystkie warzywa do zupy.
Zupa meksykańska z ogórkiem i papryką - Krok 4
Krok 5
Zupę gotuj około 15-20 minut. Na końcu dodaj posiekaną kolendrę i podawaj. """
)

r2 = Recipe.objects.create(name="Zupa kapuśniak",
                           ingredients="""porcja rosołowa - 500 gramów
Bulionetka drobiowa Knorr - 2 sztuki
wędzony boczek - 150 gramów
kiszona kapusta - 300 gramów
marchewki - 2 sztuki
pietruszka - 1 sztuka
pokrojone ziemniaki - 200 gramów
średniej wielkości cebula - 2 sztuki
Kminek z Polski Knorr - 0.5 łyżki
Majeranek z krajów śródziemnomorskich Knorr - 1 łyżka
Pieprz czarny z Wietnamu mielony Knorr - 1 szczypta
woda - 2 litry
mąka pszenna - 2 łyżki
masło - 50 gramów """,
                           description="Ciepła i sycąca zupa",
                           preparation_time=60,
                           preparation_method="""Krok 1
Z porcji rosołowej i bulionetek Knorr przygotuj wywar.
Zupa kapuśniak - Krok 1
Krok 2
Dodaj pokrojone ziemniaki, marchewki i gotuj przez 15 minut.
Zupa kapuśniak - Krok 2
Krok 3
Dopraw zupę majerankiem, kminkiem oraz pieprzem do smaku.
Zupa kapuśniak - Krok 3
Krok 4
Pokrój boczek w kostkę i podsmaż na patelni. Dodaj do niego poszatkowaną kapustę. Całość duś około 10 minut na małym ogniu, po czym dodaj do zupy.
Zupa kapuśniak - Krok 4
Krok 5
Pokrój cebulę w kostkę i zeszklij ją na maśle. Następnie dodaj mąkę i tak przygotowaną zasmażką zapraw zupę. Należy uważać, aby masło nie przypaliło się, inaczej potrawa będzie niesmaczna i niezdrowa. """
)

r3 = Recipe.objects.create(name='Zapiekanka makaronowa "PYCHOTKA" z kurczakiem i serem',
                           ingredients="""makaron świderki - 100 gramów
Rosół z kury Knorr - 1 sztuka
filet z kurczaka - 1 sztuka
cebula - 1 sztuka
papryka - 1 sztuka
pomidor - 1 sztuka
przecier pomidorowy - 2 łyżki
ząbek czosnku - 1 sztuka
mozarella light - 20 dekagramów
olej - 4 łyżki
woda - 1 szklanka """,
                           description="Szukasz szybkiego i łatwego przepisu na smaczny obiad? Zapiekanka makaronowa będzie dobrym pomysłem!",
                           preparation_time=45,
                           preparation_method="""Krok 1
Cebulę pokrój w piórka, czosnek przeciśnij przez praskę. Podsmaż je na oleju.
Zapiekanka makaronowa "PYCHOTKA" - Krok 1
Krok 2
Ugotuj makaron na sposób al dente.
Zapiekanka makaronowa "PYCHOTKA" - Krok 2
Krok 3
Warzywa pokrój w paski i wraz z kurczakiem dodaj do całości. Duś około 15 minut. Następnie podlej szklanką wody i dodaj kostkę Rosołu z kury Knorr oraz przecier pomidorowy.
Zapiekanka makaronowa "PYCHOTKA" - Krok 3
Krok 4
Makaron wyłóż do naczynia żaroodpornego, zalej sosem i posyp startym serem. Włóż do piekarnika nagrzanego do 180 stopni na 20 minut. Następnie podawaj."""
)

r4 = Recipe.objects.create(name="Naleśniki z kurczakiem w sosie bolognese",
                           ingredients="""gotowe naleśniki - 5 sztuk
Naturalnie smaczne Spaghetti Bolognese Knorr - 1 opakowanie
filet z piersi kurczaka - 200 gramów
marchewka - 1 sztuka
ser żółty ementaler - 100 gramów
kwaśna śmietana 18% - 100 mililitrów""",
                           description="Delikatne naleśniki wypełnione kurczakiem z aromatycznym, gęstym sosem Bolognese smakują wwspaniale!",
                           preparation_time=30,
                           preparation_method="""Krok 1
Rozgrzej piekarnik do 200°C. Pokrój w kostkę mięso i marchewkę. Zetrzyj ser na grubej tarce. Przesmaż mięso na złoto w 1 łyżce oleju. Dodaj 200 ml wody i zawartość opakowania Knorr Naturalnie smaczne - Spaghetti Bolognese.
Krok 2
Wymieszaj, doprowadź do wrzenia i gotuj przez ok. 5 minut. Ochłodź. Wypełnij naleśniki farszem mięsnym i zroluj.
Krok 3
Ułóż naleśniki w dobrze natłuszczonym naczyniu do zapiekania. Rozprowadź na nich śmietanę i posyp serem. Piecz przez ok. 10 minut, do momentu gdy ser roztopi się i lekko zrumieni na złoto. """
)

r5 = Recipe.objects.create(name="Sznycelki drobiowe po francusku",
                           ingredients="""piersi z kurczaka - 400 gramów
Francuska zupa cebulowa Knorr - 1 opakowanie
mąka pszenna - 3 łyżki
jajko - 1 sztuka
olej roślinny - 3 łyżki
mleko - 100 mililitrów
starty żółty ser - 100 gramów """,
                           description="Jeśli masz ochotę przygotować na obiad coś, czego twoi bliscy nie mieli jeszcze do tej pory na talerzu, to spróbuj sznycelków drobiowych po francusku",
                           preparation_time=30,
                           preparation_method="""Krok 1
Przygotuj ciasto, mieszając ze sobą jajko, zupę cebulową, mąkę, mleko i żółty ser. Możesz dodać do panierki pokruszone orzechy lub ziarna słonecznika. Sznycle będą wtedy bardziej chrupiące.
Sznycelki drobiowe po francusku - Krok 1
Krok 2
Piersi pokrój pod skosem w cienkie plastry.
Sznycelki drobiowe po francusku - Krok 2
Krok 3
Mięso zanurz w cieście i smaż na rozgrzanym tłuszczu przez 3-4 minuty z każdej strony. Kotleciki ułóż na papierowym ręczniku, aby odsączyć nadmiar tłuszczu. """
)

r6 = Recipe.objects.create(name="Tost z kurczakiem i jajkiem (club sandwich) ",
                           ingredients=""" pierś z kurczaka - 10 dekagramów
Przyprawa do złotego kurczaka Knorr - 5 gramów
kromka pieczywa tostowego - 3 sztuki
sałata lodowa - 50 gramów
Majonez Hellmann's Babuni - 2 łyżki
bekon - 5 dekagramów
ogórek konserwowy - 5 plastrów
pomidor - 1 sztuka
jajo - 1 sztuka
olej - 80 mililitrów """,
                           description="Club sandwich, czyli kanapka klubowa, to nic innego jak jasne pieczywo pszenne, przełożone mięsem i innymi składnikami.",
                           preparation_time=30,
                           preparation_method="""Krok 1
Tosty lekko podpiecz w opiekaczu lub na suchej paleni.
Tost z kurczakiem i jajkiem (club sandwich) - Krok 1
Krok 2
Pierś kurczaka polej połową oleju i posyp przyprawą Knorr. Upiecz na grillu lub podsmaż na patelni.
Tost z kurczakiem i jajkiem (club sandwich) - Krok 2
Krok 3
Na pozostałym tłuszczu usmaż z obu stron jajko sadzone.
Tost z kurczakiem i jajkiem (club sandwich) - Krok 3
Krok 4
Następnie posmaruj majonezem chleb, ułóż na kromkach porwaną sałatę, plastry pomidora i kurczaka.
Tost z kurczakiem i jajkiem (club sandwich) - Krok 4
Krok 5
Plasterki ogórka wraz z jajkiem ułóż na jednej z kromek.
Tost z kurczakiem i jajkiem (club sandwich) - Krok 5
Krok 6
Podsmaż bekon i ułóż go na drugiej kromce.
Tost z kurczakiem i jajkiem (club sandwich) - Krok 6
Krok 7
Kromki ułóż jedną na drugiej i przykryj trzecim tostem. Gotową kanapkę przekłuj dwiema wykałaczkami. Przekrój na dwa trójkąty. Podawaj z frytkami."""
)
