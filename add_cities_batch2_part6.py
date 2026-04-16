import psycopg2
import json

conn = psycopg2.connect("dbname=viajeramente user=tenant")
cur = conn.cursor()

cities = [
# More Oceania
{
    "slug": "christchurch", "name": "Christchurch", "country": "Nueva Zelanda", "continent": "Oceanía", "type": "city",
    "coordinates": {"lat": -43.5320, "lng": 172.6306},
    "tagline": "La ciudad que renació de los terremotos: arte urbano, los Alpes a la vista y la Antártida a 3.800 km",
    "intro": "Christchurch era la ciudad más inglesa de Nueva Zelanda — catedrales de piedra, jardines botánicos victorianos y cricket en el Hagley Park. Los terremotos de 2010-2011 destruyeron el 80% del centro histórico. Lo que surgió de las ruinas es una ciudad experimental: arte urbano en contenedores de carga, arquitectura de cartón (la Cardboard Cathedral del arquitecto Shigeru Ban) y espacios de pop-up que hacen de la reconstrucción un experimento urbano único en el mundo.\n\nChristchurch es la puerta a la Isla Sur de Nueva Zelanda — los Alpes del Sur con sus glaciares están a 2 horas, Kaikōura (ballenas y lobos marinos) a 2,5 horas y el Parque Nacional Arthur's Pass a 1,5 horas. La ciudad en sí tiene los mejores jardines botánicos de Oceanía y el barrio de Addington con la mejor escena de cafés del país.\n\nPara quien viene de visitar Wellington, Christchurch ofrece una perspectiva completamente diferente de Nueva Zelanda.",
    "when_to_go": "Diciembre-marzo: el verano del hemisferio sur con temperaturas de 18-24°C y los días más largos. Septiembre-noviembre (primavera) tiene los jardines en plena floración. El invierno (junio-agosto) es frío (5-12°C) pero permite esquiar en las estaciones de las cercanías.",
    "how_to_get_there": "Aeropuerto Internacional de Christchurch con conexiones de Australia, los principales hubs de Asia y conexiones domésticas de Auckland y Wellington. Bus al centro (8 NZD). Ferry desde Picton (3h, conexión con Wellington).",
    "where_to_sleep": [
        {"name": "Barrio Central (The Square)", "description": "El núcleo en reconstrucción con arte urbano y hostels desde 25 NZD, hoteles boutique desde 100 NZD."},
        {"name": "Addington", "description": "El barrio más animado con los mejores cafés. Apartamentos desde 80 NZD/noche."},
        {"name": "Sumner", "description": "El barrio costero a 15 km del centro, junto a la playa. Más tranquilo y con surf."}
    ],
    "what_to_do": [
        {"title": "Jardines Botánicos de Christchurch", "description": "Los mejores jardines de Oceanía: 21 hectáreas junto al río Avon con colecciones de rododendros, rosales y plantas nativas neozelandesas. Gratuitos."},
        {"title": "Cardboard Cathedral y arte urbano del CBD", "description": "La catedral temporal de cartón de Shigeru Ban (2013) y el arte de contenedores del Re:START Mall forman el experimento urbano de reconstrucción más interesante del mundo."},
        {"title": "Articulando en el Christchurch Art Gallery", "description": "La galería de arte moderna que sobrevivió a los terremotos tiene la mejor colección de arte contemporáneo neozelandés fuera de Auckland. Gratuita."},
        {"title": "Excursión a Kaikōura (ballenas y lobos marinos)", "description": "A 2,5h en coche, el tour en barco con sperm whales (cachalotes) garantizados 95% del tiempo. También delfines, leones marinos y albatros. Whale Watch Kaikōura: 165 NZD."},
        {"title": "Skiing en Mount Hutt o Porter Heights", "description": "A 90 min en coche, los ski fields de Canterbury tienen nieve de junio a octubre. Mount Hutt es el más grande, Porter Heights el más económico."},
        {"title": "Track en los Alpes del Sur (Arthur's Pass)", "description": "A 90 min, el Parque Nacional Arthur's Pass tiene trekking de nivel desde fácil hasta el multi-day Avalanche Peak. El viaje en tren TranzAlpine (155 NZD) hasta la costa oeste es uno de los mejores del mundo."}
    ],
    "food_and_drink": "Christchurch tiene la mejor escena de cafés de flat white de la Isla Sur. El barrio de Addington y Victoria Street concentran los mejores: C1 Espresso, Allpress y Coffee Culture. El mercado de productores del sábado en el Riccarton Market tiene los mejores productos de Canterbury: salmón, cordero, queso y vino de Marlborough. Cena: 25-45 NZD.",
    "safety": "Christchurch es muy segura. Sin precauciones especiales para turistas. El centro en reconstrucción tiene zonas acordonadas — sigue las señales.",
    "visa_info": "Españoles necesitan NZeTA (23 NZD, online antes del viaje) + IVL (35 NZD). Moneda: dólar neozelandés (NZD). 1€ ≈ 1,75 NZD.",
    "local_tips": ["El TranzAlpine (tren Christchurch-Greymouth a través de los Alpes) es uno de los viajes en tren más bonitos del mundo — reserva con antelación", "Los jardines botánicos están en su máximo esplendor en octubre-noviembre (primavera) y enero-febrero (verano)", "El NZeTA se tramita online — no es visa tradicional pero es obligatorio para españoles", "Kaikōura con lluvia también tiene cachalotes — no pospongas si el tiempo es dudoso", "Addington tiene mejores precios que el centro turístico — come ahí"],
    "travel_styles": ["naturaleza", "cultura", "outdoor", "arquitectura"],
    "vibes": ["rebuilt", "experimental", "alpine gateway", "kiwi"],
    "climate": ["oceanic", "four seasons"],
    "best_months": ["December", "January", "February", "March"],
    "budget_daily_low": 70, "budget_daily_mid": 140, "budget_daily_high": 320, "guide_quality": 8
},
{
    "slug": "adelaide", "name": "Adelaida", "country": "Australia", "continent": "Oceanía", "type": "city",
    "coordinates": {"lat": -34.9285, "lng": 138.6007},
    "tagline": "La ciudad del vino, los festivales y el mejor acceso al Outback y Kangaroo Island",
    "intro": "Adelaida tiene la fama de ser la ciudad más aburrida de Australia y eso es precisamente lo que la hace perfecta para cierto tipo de viajero: escala humana, sin las aglomeraciones de Sydney o Melbourne, con una escena gastronómica y vinícola que en algunas comparaciones los supera. El Barossa Valley (los mejores shiraz del mundo) y la McLaren Vale están a menos de una hora.\n\nLo que distingue a Adelaida es su programación cultural — el Festival de Adelaida, el Fringe y la Bienal de Arte son algunos de los mejores del hemisferio sur. El Adelaide Central Market tiene la mayor variedad de productores de Australia en un solo espacio. El barrio de Hahndorf, 30 km al este, es el pueblo alemán más antiguo de Australia.\n\nKangaroo Island — con koalas, canguros y leones marinos silvestres — está a 30 minutos en avión o 3 horas en ferry.",
    "when_to_go": "Marzo-mayo y septiembre-noviembre: otoño e primavera australes con 18-25°C son los momentos ideales. El verano (dic-feb) puede ser muy caluroso (40°C+) aunque las vendimias en el Barossa hacen de febrero-marzo la temporada más emocionante para los amantes del vino.",
    "how_to_get_there": "Aeropuerto Internacional de Adelaida con conexiones australianas e internacionales (Singapur, Doha, Malasia). Tren al centro en 23 min (10 AUD).",
    "where_to_sleep": [
        {"name": "CBD / North Adelaide", "description": "El centro histórico con los mejores hoteles boutique (desde 100 AUD) y acceso al mercado central."},
        {"name": "Glenelg", "description": "El barrio de playa a 30 min en tram desde el centro. Más económico y con ambiente playero. Desde 80 AUD."},
        {"name": "Norwood / Unley", "description": "Los barrios más agradables para estancias largas. Apartamentos desde 85 AUD/noche."}
    ],
    "what_to_do": [
        {"title": "Barossa Valley (excursión de día o fin de semana)", "description": "El valle productor de los mejores shiraz y grenache del mundo, a 70 km. Jacob's Creek, Penfolds (Grange se hace aquí) y Henschke son las bodegas de referencia. Tours de vino desde 80 AUD."},
        {"title": "Adelaide Central Market", "description": "El mercado cubierto más grande del hemisferio sur: queso australiano, ostras de Coffin Bay, vino del Barossa, mermeladas artesanales y la mejor charcutería de Australia del Sur. Los martes son el día más tranquilo."},
        {"title": "Kangaroo Island (2 días)", "description": "La tercera isla más grande de Australia con los mejores avistamientos de fauna salvaje: leones marinos, koalas en los árboles, canguros sin miedo y el Remarkable Rocks en acantilados sobre el Océano Austral."},
        {"title": "Hahndorf — pueblo alemán del siglo XIX", "description": "A 28 km en los Adelaide Hills, el pueblo fundado por inmigrantes luteranos alemanes en 1839 tiene las mejores salchichas, cerveza artesanal y el strudel más auténtico fuera de Bavaria."},
        {"title": "Costa de Coorong y Murray Mouth", "description": "A 80 km al sur, el Parque Nacional Coorong con su laguna de agua salada de 145 km de largo y los pelícanos es el paisaje más único de Australia del Sur."},
        {"title": "Fringe Festival (febrero-marzo)", "description": "El Festival Fringe de Adelaida es el segundo festival de artes más grande del mundo (después del Edimburgo Fringe) — 700 actuaciones en 3 semanas."}
    ],
    "food_and_drink": "Adelaida tiene la mejor cocina australiana fuera de Melbourne: las ostras de Coffin Bay (las más famosas de Australia), el shiraz del Barossa con carne de canguro, quesos de Mount Barker y los farmer's markets de los Adelaide Hills. El Central Market tiene la mejor selección de comida de Australia del Sur. El vino del Barossa es el mejor argumento gastronómico de Adelaida.",
    "safety": "Adelaida es la ciudad más segura de Australia. Sin precauciones especiales para turistas.",
    "visa_info": "Españoles necesitan ETA (20 AUD, online antes del viaje). Estancias hasta 90 días. Moneda: dólar australiano (AUD).",
    "local_tips": ["El Barossa + una noche en un bed and breakfast de la zona vale más que 3 días en el centro de Adelaida", "Kangaroo Island requiere ferry (KI Connect, 3h) o vuelo (Rex Airlines, 30 min) — ambos requieren reserva", "El Fringe de febrero-marzo (700 espectáculos) hace que sea el mejor momento para visitar la ciudad", "La Go Card de transporte cubre tren, bus y el tram a Glenelg", "Las ostras de Coffin Bay en el mercado central cuestan la mitad que en un restaurante"],
    "travel_styles": ["vino", "naturaleza", "cultura", "gastronomía"],
    "vibes": ["wine country", "festivals", "laid-back", "australian"],
    "climate": ["mediterranean"],
    "best_months": ["March", "April", "May", "September", "October", "November"],
    "budget_daily_low": 80, "budget_daily_mid": 155, "budget_daily_high": 360, "guide_quality": 8
},
# More Europe to fill gaps
{
    "slug": "tirana", "name": "Tirana", "country": "Albania", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 41.3275, "lng": 19.8187},
    "tagline": "El secreto de los Balcanes: la capital más animada de Europa que nadie visita todavía",
    "intro": "Tirana es el secreto mejor guardado de los Balcanes — una capital europea que aún no ha sido descubierta por el turismo de masas pero tiene todo lo necesario para ser la próxima ciudad de moda: el bulevar central con sus edificios pintados de colores vivos (proyecto del alcalde-artista Edi Rama), la montaña Dajti a 25 minutos en teleférico, el Blloku (barrio cerrado durante el comunismo, ahora el más animado de la ciudad) y precios que recuerdan a lo que costaba viajar a Europa del Este en los años 90.\n\nAlbania vivió el régimen comunista más estricto de Europa hasta 1992 — las 170.000 bunkers de hormigón distribuidos por todo el país son el legado más visible de la paranoia del dictador Enver Hoxha. Muchos han sido reconvertidos en bares, museos y galerías.\n\nTirana está a 30 minutos en coche de la costa del Adriático y a 2 horas del lago de Ohrid (UNESCO, compartido con Macedonia del Norte) — una base perfecta para explorar los Balcanes occidentales.",
    "when_to_go": "Abril-junio y septiembre-octubre: clima mediterráneo perfecto (20-28°C). El verano (julio-agosto) es caluroso (35°C+) pero la costa está llena de albaneses. El invierno (dic-feb) puede ser lluvioso y frío pero los precios son muy bajos.",
    "how_to_get_there": "Aeropuerto Internacional Madre Teresa con conexiones directas de Madrid, Roma, Milán, Londres, Turquía y toda la región. Vuelos muy económicos desde Europa occidental. Bus al centro: 200 LEK. Taxi: 1.500-2.000 LEK.",
    "where_to_sleep": [
        {"name": "Blloku", "description": "El barrio más animado de Tirana, antes reservado a la nomenklatura comunista, ahora lleno de bares y restaurantes. Hostels desde 10€, apartamentos desde 30€/noche."},
        {"name": "Centro (Skanderbeg Square)", "description": "El corazón histórico con el mejor acceso a pie. Hoteles boutique desde 45€."},
        {"name": "Barrio Laprake", "description": "Zona residencial más tranquila y económica, bien conectada al centro."}
    ],
    "what_to_do": [
        {"title": "Plaza Skanderbeg y Bulevar Central", "description": "El corazón de Tirana con la estatua del héroe nacional, la mezquita Et'hem Bey y los edificios pintados de colores vivos. El mejor paseo matutino de la ciudad."},
        {"title": "Blloku — barrio nocturno", "description": "El barrio que Hoxha reservó para sus oficiales comunistas es ahora el más animado de Tirana: bares, restaurantes, vida nocturna y la antigua villa de Hoxha convertida en museo."},
        {"title": "Museo Nacional de Historia", "description": "La historia de Albania desde los ilírios hasta el régimen comunista, con el mosaico más grande del país en la fachada. 200 LEK."},
        {"title": "Bunker del Arte (BunkArt)", "description": "Dos búnkeres convertidos en museos: BunkArt 1 (el búnker del dictador Hoxha en el monte Dajti) y BunkArt 2 (el búnker del interior de Tirana). Los mejores museos del horror comunista de Europa."},
        {"title": "Monte Dajti en teleférico", "description": "El teleférico de 15 minutos sube a 1.613m con vistas de Tirana y las montañas albanesas. El restaurante en la cima sirve comida albanesa con esas vistas."},
        {"title": "Lago de Ohrid (excursión de día o noche)", "description": "A 2h en coche o bus, el lago más antiguo de Europa (UNESCO, compartido con Macedonia del Norte) tiene el pueblo de Ohrid con la mayor concentración de iglesias medievales de los Balcanes."}
    ],
    "food_and_drink": "La cocina albanesa tiene influencias griegas, turcas y mediterráneas: tavë kosi (cordero horneado en yogur, el plato nacional), byrek (hojaldre de queso o espinacas), fëgesë (fritada de pimientos, tomates y queso), qofte (albóndigas), y el raki (aguardiente de uva, el más fuerte de los Balcanes). Un menú completo en un restaurante local: 5-10€. Cerveza Tirana o Korça: 1-2€.",
    "safety": "Tirana es segura para turistas. Sin precauciones especiales en el centro y el Blloku. El tráfico es el mayor riesgo — los conductores albaneses tienen fama en los Balcanes.",
    "visa_info": "Albania no es UE ni Schengen. Los ciudadanos españoles pueden entrar sin visado hasta 90 días con pasaporte o DNI. Moneda: lek albanés (LEK/ALL). 1€ ≈ 105 LEK.",
    "local_tips": ["El lek es la moneda local pero el euro se acepta en muchos lugares — comprueba el tipo de cambio", "El raki albanés es más fuerte que cualquier ouzo griego o rakija serbio — con cuidado", "Los búnkeres de Hoxha están literalmente en todas partes del país — hasta en los campos de cultivo", "El barrio Blloku de jueves a sábado tiene la vida nocturna más animada de los Balcanes por 2€ la cerveza", "Tirana + Riviera albanesa (Sarandë, Himara, Dhermi) es uno de los mejores itinerarios de los Balcanes"],
    "travel_styles": ["cultura", "historia", "nocturno", "budget"],
    "vibes": ["balkans", "emerging", "communist history", "colorful"],
    "climate": ["mediterranean"],
    "best_months": ["April", "May", "June", "September", "October"],
    "budget_daily_low": 25, "budget_daily_mid": 50, "budget_daily_high": 120, "guide_quality": 8
},
{
    "slug": "sarajevo", "name": "Sarajevo", "country": "Bosnia y Herzegovina", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 43.8476, "lng": 18.3564},
    "tagline": "Donde Oriente y Occidente se besan: el bazaar otomano más auténtico de los Balcanes y el inicio de la Primera Guerra Mundial",
    "intro": "Sarajevo es una de las ciudades más fascinantes y complejas de Europa: el lugar donde un archduke fue asesinado y comenzó la Primera Guerra Mundial, donde durante 44 meses (1992-1996) tuvo lugar el asedio más largo de una capital en la historia de la guerra moderna, y donde hoy una mezquita otomana, una catedral ortodoxa y una sinagoga medieval conviven a 50 metros de distancia.\n\nEl Baščaršija, el bazaar otomano del siglo XV, es el más auténtico de los Balcanes — más que los de Sarajevo se parecen al Estambul real que el Istanbul actual. Los puestos de cevapcici (salchichas a la brasa con pan y cebollas), el café bosnio espeso y los talleres de cobre a la vista de todos crean una atmósfera que Europa occidental perdió siglos atrás.\n\nLas cicatrices del asedio siguen visibles — los 'rosas de Sarajevo' (marcas de metralla rellenas de resina roja en el pavimento) están por toda la ciudad, pero Sarajevo mira hacia delante con una determinación que solo las ciudades que sobrevivieron lo más duro pueden tener.",
    "when_to_go": "Abril-junio y septiembre-octubre: temperatura perfecta (18-26°C). El verano es agradable en la ciudad pero las montañas circundantes (base de los JJOO de 1984) tienen excursiones perfectas. El invierno puede tener nieve y se puede esquiar en Bjelašnica y Jahorina.",
    "how_to_get_there": "Aeropuerto Internacional de Sarajevo con conexiones directas de Vienna, Frankfurt, Estambul, Zagreb y otras ciudades europeas. Ryanair tiene vuelos desde Londres y ciudades europeas. Taxi del aeropuerto: 25-35 BAM.",
    "where_to_sleep": [
        {"name": "Baščaršija (Casco Otomano)", "description": "La experiencia más auténtica, dentro del bazaar. Pansiones desde 15 BAM/persona, hoteles boutique desde 60 BAM."},
        {"name": "Marijin Dvor", "description": "El barrio austro-húngaro del siglo XIX, el más europeo de Sarajevo. Hoteles boutique desde 70 BAM."},
        {"name": "Grbavica", "description": "Barrio residencial tranquilo, más económico. Apartamentos desde 40 BAM/noche."}
    ],
    "what_to_do": [
        {"title": "Baščaršija — el bazaar otomano", "description": "El corazón histórico otomano del siglo XV con la mezquita Gazi Husrev-beg (la más grande de Bosnia), los talleres de cobre (Kazandžiluk), la fuente de Sebilj y la mejor concentración de cultura oriental de Europa. Gratuito pasear."},
        {"title": "Rosas de Sarajevo y tour del asedio", "description": "Las marcas de metralla rellenadas de resina roja en el pavimento señalan las zonas de bombardeo. El tour del asedio (con guía, 30 BAM) narra los 44 meses del sitio con testimonios directos."},
        {"title": "Tunel de la Esperanza", "description": "El túnel de 800 metros excavado bajo el aeropuerto para abastecer la ciudad durante el asedio (1993). Hoy museo, es la visita más emotiva de Sarajevo (3 BAM)."},
        {"title": "Montañas Olímpicas (Trebević, Bjelašnica)", "description": "Las pistas de los JJOO de 1984 están a 20 minutos en teleférico (rehabilitado en 2018). Las instalaciones de bobsleigh abandonadas con grafiti son un lugar fascinante. Senderismo libre."},
        {"title": "Café bosnio en el Baščaršija", "description": "El café bosnio (džezva de cobre + azúcar rahat lokum) es un ritual de hospitalidad. Tomarlo en la terraza de cualquier kafana del bazaar con las mezquitas al fondo es la pausa más auténtica de los Balcanes."},
        {"title": "Mostar (excursión de día)", "description": "A 2h en bus, el Stari Most (puente otomano del siglo XVI sobre el río Neretva) es el símbolo de la reconciliación bosnia. El casco histórico tiene la concentración más alta de ambiente mediterráneo-otomano de los Balcanes."}
    ],
    "food_and_drink": "La cocina bosnia mezcla otomana y balcánica: ćevapi (salchichas de ternera y cordero con pan somun y cebollas, el plato por excelencia), burek (hojaldre de carne, queso o espinacas), begova čorba (sopa de okra con ternera) y baklava bosnia (más gruesa y con nueces). El ćevapi de Sarajevo es el mejor de los Balcanes según los propios bosnios. Cena completa 15-25 BAM.",
    "safety": "Sarajevo es muy segura para turistas. Sin precauciones especiales. El centro histórico y los barrios de Marijin Dvor y Grbavica son totalmente tranquilos.",
    "visa_info": "Bosnia y Herzegovina no es UE ni Schengen. Los ciudadanos españoles pueden entrar sin visado hasta 90 días con pasaporte. Moneda: marco bosnio (BAM). 1€ = 1,956 BAM (tipo fijo al euro).",
    "local_tips": ["El BAM tiene tipo fijo con el euro (1,956 BAM = 1€) — fácil de calcular", "El ćevapi se come con las manos, dentro del pan somun, con cebolla cruda — sin cubiertos es la forma correcta", "El tour del asedio con guía que vivió el sitio es incomparablemente más rico que hacerlo solo", "Mostar en un día desde Sarajevo es posible pero una noche allí es mucho mejor", "Las montañas olímpicas abandonadas son de los lugares más fascinantes de Europa — el bobsleigh cubierto de grafiti y la naturaleza recuperando el espacio"],
    "travel_styles": ["historia", "cultura", "gastronomía", "arquitectura"],
    "vibes": ["ottoman", "war history", "multicultural", "resilient"],
    "climate": ["continental"],
    "best_months": ["April", "May", "June", "September", "October"],
    "budget_daily_low": 30, "budget_daily_mid": 60, "budget_daily_high": 140, "guide_quality": 8
},
{
    "slug": "skopje", "name": "Skopie", "country": "Macedonia del Norte", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 41.9981, "lng": 21.4254},
    "tagline": "El experimento arquitectónico más bizarro de Europa: estatuas neoclásicas, bazaar otomano y Madre Teresa",
    "intro": "Skopie es probablemente la capital más rara de Europa. El proyecto 'Skopje 2014' del gobierno anterior invirtió más de 500 millones de euros en llenar la plaza central con más de 20 estatuas ecuatres de tamaño monumental, arcos del triunfo, fuentes y fachadas neoclásicas que se construyeron sobre edificios modernistas brutalistas de los años 60. El resultado es surrealista, discutible artísticamente pero absolutamente único y fotográfico.\n\nA 10 minutos caminando del kitsch neoclásico está el Çarsi — el Bazaar otomano del siglo XIV, uno de los más grandes de los Balcanes, que no ha cambiado nada en el último siglo. Madre Teresa nació en Skopie en 1910 — hay un memorial en la casa donde nació.\n\nMacedonia del Norte es barata, poco turística y tiene acceso directo al lago de Ohrid (UNESCO) a 2,5 horas.",
    "when_to_go": "Abril-junio y septiembre-octubre: temperatura perfecta (18-26°C). El verano (julio-agosto) es caluroso (35°C+). El invierno puede ser frío y neblinoso.",
    "how_to_get_there": "Aeropuerto Internacional Alexander el Grande con vuelos baratos de Ryanair, easyJet y Wizz Air desde toda Europa. Bus al centro: 150 MKD. Taxis: 300-400 MKD.",
    "where_to_sleep": [
        {"name": "Centro / Macedonia Square", "description": "En el corazón del experimento neoclásico. Hoteles boutique desde 30€, hostels desde 10€."},
        {"name": "Çarsi (Bazaar Otomano)", "description": "El lado otomano histórico, más auténtico. Guesthouses desde 20€/noche."},
        {"name": "Debar Maalo", "description": "El barrio bohemio más agradable con los mejores cafés y galerías. Apartamentos desde 25€/noche."}
    ],
    "what_to_do": [
        {"title": "Macedonia Square y el experimento neoclásico", "description": "La plaza más surrealista de Europa: 20+ estatuas monumentales, el Arco de Macedonia, la fuente del Guerrero a Caballo (Alejandro Magno enorme) y el Puente de las Civilizaciones. Gratuito y obligatorio."},
        {"title": "Çarsi — el Bazaar otomano (siglo XIV)", "description": "El mercado otomano mejor preservado de Macedonia: la Mezquita Mustafá Pashá del siglo XV, los joyeros, los talleres de hojalata y los cafés de café turco espeso. El contraste con la plaza neoclásica es asombroso."},
        {"title": "Fortaleza de Kale", "description": "La fortaleza medieval en la colina sobre el Vardar con las mejores vistas de la ciudad y del contraste neoclásico vs otomano que define Skopie. Gratuita."},
        {"title": "Memorial de Madre Teresa", "description": "La casa donde nació Gonxhe Bojaxhiu (Madre Teresa de Calcuta) en 1910, reconvertida en pequeño museo y capilla. Gratuito."},
        {"title": "Lago de Ohrid (excursión de día o noche)", "description": "A 2,5h en bus o coche, el lago más antiguo de Europa con el pueblo de Ohrid (UNESCO) y 365 iglesias medievales es la mejor razón para ir a Macedonia. Hostels desde 12€/noche."},
        {"title": "Canyon de Matka", "description": "A 15 km del centro, el cañón fluvial con kayak, cueva de estalactitas y monasterios medievales colgados es el mejor half-day trip de Skopie."}
    ],
    "food_and_drink": "La cocina macedónica mezcla griega, turca y balcánica: tavče gravče (judías al horno, el plato nacional), ajvar (paté de pimiento asado), shopska salata (tomate, pepino, queso blanco), ćevapi y el vino de Tikveš (la mejor región vinícola de los Balcanes occidentales). La zona de restaurantes junto al río Vardar tiene los mejores precios. Cena completa: 8-15€.",
    "safety": "Skopie es segura para turistas. Sin precauciones especiales.",
    "visa_info": "Macedonia del Norte no es UE ni Schengen. Los ciudadanos españoles pueden entrar sin visado hasta 90 días con pasaporte. Moneda: denar macedónico (MKD). 1€ ≈ 62 MKD.",
    "local_tips": ["El contraste entre la plaza neoclásica y el bazaar otomano a 10 minutos a pie es el mejor resumen de la identidad macedónica", "El vino Tikveš (Vranec especialmente) es una de las grandes sorpresas vinícolas de los Balcanes", "El Canyon de Matka en kayak (10€/h) con las rocas calizas es más impresionante de lo que las fotos sugieren", "Ohrid merece mínimo una noche — los templos medievales al amanecer vacíos de turistas son extraordinarios", "El denar no se puede cambiar fuera de Macedonia — cambia lo justo para el viaje"],
    "travel_styles": ["cultura", "historia", "budget", "vino"],
    "vibes": ["balkans", "bizarre", "ottoman", "neoclassical"],
    "climate": ["continental"],
    "best_months": ["April", "May", "June", "September", "October"],
    "budget_daily_low": 22, "budget_daily_mid": 45, "budget_daily_high": 110, "guide_quality": 8
},
# More Americas
{
    "slug": "atlanta", "name": "Atlanta", "country": "Estados Unidos", "continent": "América", "type": "city",
    "coordinates": {"lat": 33.7490, "lng": -84.3880},
    "tagline": "La capital del sur americano: Martin Luther King, Coca-Cola y la escena de hip-hop más importante del mundo",
    "intro": "Atlanta es la ciudad que definió el New South americano — más diversa, más dinámica y más global que el cliché sureño que muchos esperan. Es la ciudad donde nació Martin Luther King, donde se inventó la Coca-Cola, donde se desarrolló el movimiento de derechos civiles y donde, en los últimos 20 años, surgió el trap music que dominó la cultura popular global (Outkast, Lil Jon, Young Jeezy, Migos, Cardi B).\n\nEl barrio histórico Sweet Auburn con la casa natal de MLK, el CNN Center, el Acuario del Georgia (el más grande del mundo fuera de Asia) y el barrio de Ponce City Market forman un itinerario que abarca desde la historia del siglo XX hasta la gentrificación del XXI. El Beltline — una antigua vía de tren reconvertida en parque lineal de 35km con arte mural — es el proyecto urbano más interesante del sur de EEUU.\n\nAtlanta también es el hub de vuelos más transitado del mundo (Aeropuerto Hartsfield-Jackson).",
    "when_to_go": "Marzo-mayo y septiembre-noviembre: la primavera (especialmente marzo-abril con las azaleas del Piedmont Park) y el otoño son perfectos (18-26°C). El verano (junio-agosto) es caluroso y húmedo (32-38°C) pero con muchos festivales.",
    "how_to_get_there": "Aeropuerto Internacional Hartsfield-Jackson, el más transitado del mundo. MARTA (metro) al centro en 20 min (2,50$). Hub perfecto para vuelos transatlánticos de toda Europa.",
    "where_to_sleep": [
        {"name": "Midtown / Ponce City Market", "description": "El barrio más agradable con el Beltline y los mejores restaurantes. Hoteles boutique desde 90$, hostels desde 35$."},
        {"name": "Old Fourth Ward", "description": "El barrio del Beltline y el mercado de Ponce, más creativo y cool. Apartamentos desde 70$/noche."},
        {"name": "Buckhead", "description": "El barrio más elegante para compras y hoteles de lujo. Desde 120$, más alejado del centro histórico."}
    ],
    "what_to_do": [
        {"title": "Martin Luther King Jr. National Historic Site", "description": "La casa natal de MLK, la Iglesia Bautista de Ebenezer (donde predicó), el mausoleo con la llama eterna y el museo del Centro Nacional de Derechos Civiles son gratuitos y forman el conjunto más importante de la historia americana del siglo XX."},
        {"title": "Georgia Aquarium", "description": "El mayor acuario del mundo occidental con tiburones ballena y mantas rayas en el tanque de Ocean Voyager (38,5 millones de litros). 45$."},
        {"title": "Atlanta Beltline", "description": "La antigua vía de tren reconvertida en parque lineal de 35km con arte mural, mercados, restaurantes y bares. El tramo de Ponce City Market a Inman Park es el más animado."},
        {"title": "World of Coca-Cola Museum", "description": "El museo de la bebida más consumida del mundo, con sala de catas de 100 sabores de Coca-Cola de todo el mundo y la historia completa de la empresa fundada en Atlanta en 1886. 22$."},
        {"title": "Piedmont Park y High Museum of Art", "description": "El parque más grande de Atlanta es hermoso en cualquier estación. El High Museum (el mejor museo de arte del sur de EEUU) tiene los mejores impresionistas fuera de NYC. 23$."},
        {"title": "Escena de música hip-hop y R&B", "description": "Atlanta es la capital mundial del trap y el hip-hop moderno. The Masquerade, City Winery y los clubs de Buckhead tienen las mejores noches con artistas locales y actuaciones en directo."}
    ],
    "food_and_drink": "Atlanta tiene la mejor cocina del sur: pollo frito (Chick-fil-A fue inventado aquí), BBQ de cerdo con pulled pork, peach cobbler (tarta de melocotón, el melocotón de Georgia es el mejor de EEUU), biscuits con gravy y el sweet tea (té dulce helado, omnipresente). Slutty Vegan y Staplehouse son los restaurantes más de moda. Cena en restaurante de BBQ: 20-35$.",
    "safety": "Atlanta es segura en barrios turísticos. El Downtown y Midtown son seguros de día. Cuidado con las zonas al sur del Estadio Mercedes-Benz de noche. Usa Uber.",
    "visa_info": "Españoles necesitan ESTA (21$, online antes del viaje). Estancias hasta 90 días sin visa.",
    "local_tips": ["El Martin Luther King Historic Site es gratuito — reserva los tours con antelación en temporada alta", "El Beltline en bicicleta (alquiler en las estaciones Relay Bikes) es la mejor forma de ver el street art y los barrios", "El sweet tea helado en Atlanta es un ritual — los restaurantes sureños lo dan free refills", "El aeropuerto de Atlanta es el más transitado del mundo — llega con 3h de antelación para vuelos internacionales", "El Ponce City Market de tarde-noche tiene el mejor ambiente del Midtown"],
    "travel_styles": ["historia", "cultura", "música", "gastronomía"],
    "vibes": ["new south", "hip-hop", "civil rights", "urban"],
    "climate": ["humid subtropical"],
    "best_months": ["March", "April", "May", "September", "October", "November"],
    "budget_daily_low": 75, "budget_daily_mid": 150, "budget_daily_high": 340, "guide_quality": 8
},
{
    "slug": "phoenix", "name": "Phoenix", "country": "Estados Unidos", "continent": "América", "type": "city",
    "coordinates": {"lat": 33.4484, "lng": -112.0740},
    "tagline": "El desierto americano: saguaros, sol garantizado y la puerta a Sedona, el Gran Cañón y Sonora",
    "intro": "Phoenix es la ciudad más calurosa de EEUU en verano (45°C+) y una de las más sorprendentes: el desierto del Sonora con sus cactus saguaros gigantes rodea directamente la ciudad, haciendo que el contraste entre resort de lujo y desierto salvaje sea de literalmente 5 kilómetros. El barrio de Scottsdale tiene los mejores spas y restaurantes del suroeste americano.\n\nLo que hace de Phoenix una base extraordinary es su proximidad: Sedona (la ciudad más fotogénica de EEUU, con formaciones de roca roja) está a 2h, el Gran Cañón a 4h, el desierto de Sonora (México) a 2h y los mejores campos de golf del mundo literalmente dentro de la ciudad.\n\nEn invierno (noviembre-marzo), Phoenix es perfecta — 20-25°C de media y sol garantizado. Es cuando los 'snowbirds' (americanos jubilados que escapan del frío del norte) llenan los resorts.",
    "when_to_go": "Octubre-abril: el único período viable para turismo activo. Noviembre-febrero es el mejor: 18-24°C, sin lluvia y todo abierto. El verano (mayo-septiembre) con 42-48°C solo es para residentes con acceso a piscinas y aire acondicionado.",
    "how_to_get_there": "Aeropuerto Internacional Sky Harbor, bien conectado con EEUU y algo con Europa. Tren light rail al centro (2$). Uber al centro: 15-20$.",
    "where_to_sleep": [
        {"name": "Scottsdale", "description": "El barrio más elegante con los mejores resorts (desde 120$), restaurantes y galerías de arte. El mejor ambiente de Phoenix."},
        {"name": "Downtown Phoenix", "description": "El centro revitalizado con el barrio Roosevelt Row de arte urbano. Hoteles boutique desde 90$, hostels desde 30$."},
        {"name": "Tempe / ASU", "description": "El barrio universitario de Arizona State University, más económico y animado. Desde 60$/noche."}
    ],
    "what_to_do": [
        {"title": "Camelback Mountain", "description": "El senderismo urbano más famoso de Phoenix: 2km de subida empinada entre cactus saguaros a 821m de altura, con vistas de toda la ciudad. Gratis, llega antes de las 7am para aparcar."},
        {"title": "Sedona (excursión de día)", "description": "A 2h, las formaciones de roca roja de Sedona son uno de los paisajes más fotogénicos de EEUU. El Airport Loop Trail (fácil, 5km) tiene las mejores vistas. El centro tiene demasiado turismo espiritual new-age pero los paisajes son reales."},
        {"title": "Desert Botanical Garden", "description": "El jardín botánico del desierto de Sonora con más de 50.000 plantas desérticas y la colección más completa de cactus del mundo. Nocturno en verano con instalaciones de luz (25$)."},
        {"title": "Scottsdale ArtWalk y Old Town", "description": "El centro histórico de Scottsdale con las mejores galerías de arte western del suroeste. El ArtWalk de los jueves noche (gratuito) es el evento cultural más animado de la zona."},
        {"title": "Tour en Jeep por el Salt River o Tonto National Forest", "description": "Los tours de jeep 4x4 por el desierto y los cañones rodeando Phoenix son la mejor forma de entender el paisaje del Sonora sin conducir. Desde 75$ con empresa local."},
        {"title": "Gran Cañón (excursión de 1-2 días)", "description": "A 4h, el South Rim del Gran Cañón tiene los mejores miradores (Mather Point, Desert View). Para bajar hasta el río (Inner Gorge) se necesita permit y buena condición física."}
    ],
    "food_and_drink": "Phoenix tiene la mejor cocina sonorense de EEUU: tamales de chile colorado, carne asada tacos, chile relleno al horno, menudo (sopa de callos para la resaca del domingo) y los mejores burritos de EEUU (del estilo 'Sonoran dog', hot dog en pan bolillo con frijoles fritos y mayonesa). Scottsdale tiene restaurantes de alta cocina con chefs con Michelin. Los mejores tacos: Los Sombreros, Tacos Chiwas. Cena de tacos: 10-15$.",
    "safety": "Phoenix es segura en zonas turísticas. Scottsdale y Tempe son muy seguros. El centro de Phoenix tiene zonas de personas sin hogar — rutina de precaución estándar de ciudad americana.",
    "visa_info": "Españoles necesitan ESTA (21$, online antes del viaje). Estancias hasta 90 días sin visa.",
    "local_tips": ["Camelback Mountain: llega ANTES de las 7am — el aparcamiento se llena a las 8am y el calor aprieta desde las 9am", "Un coche es imprescindible en Phoenix — la ciudad está diseñada para el automóvil sin excepciones", "La temporada de verano de los resorts tiene los precios más bajos del año — solo sopórtalo si tienes piscina disponible", "Sedona tiene mucho turismo new-age pero los senderos son genuinamente espectaculares — ignora las tiendas de cristales", "El cactus saguaro solo crece en el desierto del Sonora — una rareza geográfica única"],
    "travel_styles": ["naturaleza", "outdoor", "gastronomía", "golf"],
    "vibes": ["sonoran desert", "sun", "saguaro", "resort"],
    "climate": ["hot desert"],
    "best_months": ["November", "December", "January", "February", "March"],
    "budget_daily_low": 70, "budget_daily_mid": 140, "budget_daily_high": 380, "guide_quality": 8
},
# One more Africa
{
    "slug": "alexandria", "name": "Alejandría", "country": "Egipto", "continent": "África", "type": "city",
    "coordinates": {"lat": 31.2001, "lng": 29.9187},
    "tagline": "La ciudad de los Ptolomeos, la Biblioteca y el Mediterráneo más griego de África",
    "intro": "Alejandría fue durante siglos la ciudad más importante del mundo mediterráneo — la Biblioteca de Alejandría (el conocimiento de la humanidad) y el Faro (una de las 7 Maravillas) la hacían el centro del mundo conocido. De todo eso quedan los cimientos bajo la nueva Biblioteca (Bibliotheca Alexandrina, una obra arquitectónica contemporánea extraordinaria), las catacumbas romanas de Kom el-Shoqafa y el espíritu cosmopolita que la distingue de El Cairo.\n\nAlejandría tiene un carácter mediterráneo y greco-romano que El Cairo no tiene — más europeo, con la Corniche frente al mar, cafeterías de estilo europeo que sobreviven del siglo XX y un barrio histórico de mezcla griega, judía, italiana y árabe que Lawrence Durrell describió en el 'Cuarteto de Alejandría'.\n\nA 3h en tren de El Cairo, Alejandría es la alternativa perfecta para quien quiere Egipto sin las pirámides.",
    "when_to_go": "Octubre-mayo: las temperaturas mediterráneas de 15-25°C hacen la ciudad cómoda. El verano (junio-agosto) es caluroso y húmedo (30-35°C) pero los alejandrianos (y los cairotas que escapan del calor) llenan las playas.",
    "how_to_get_there": "Tren desde El Cairo en 2-2,5h (desde 50 EGP, 1-2€). Autobús desde El Cairo (3h). Alejandría tiene aeropuerto internacional (Borg El Arab, 40km del centro) con conexiones de la región.",
    "where_to_sleep": [
        {"name": "Raml Station / Corniche", "description": "El centro histórico más europeo, con los mejores hoteles desde 30$ y acceso a pie a la Bibliotheca y el anfiteatro romano."},
        {"name": "El Azarita", "description": "El barrio del mercado y la mezquita Al-Abbas, más local y económico. Hoteles desde 20$."},
        {"name": "Stanley / Sidi Bishr", "description": "Los barrios de playa más populares al este del centro. Buenos hostels desde 15$."}
    ],
    "what_to_do": [
        {"title": "Bibliotheca Alexandrina", "description": "La nueva Biblioteca de Alejandría (2002), diseñada por Snøhetta, con una fachada de granito cubierta de caracteres de todos los alfabetos del mundo. El interior con el espacio de lectura en cascada es impresionante. 70 EGP."},
        {"title": "Catacumbas de Kom el-Shoqafa", "description": "Las catacumbas más grandes de Egipto (siglo II d.C.) muestran la fusión única de arte greco-romano con iconografía egipcia. Una de las 7 Maravillas del Mundo Medieval. 180 EGP."},
        {"title": "Fuerte de Qaitbay (donde estuvo el Faro)", "description": "El fuerte mameluco del siglo XV construido sobre los cimientos exactos del Faro de Alejandría, una de las 7 Maravillas del Mundo Antiguo. Las vistas del Mediterráneo son las mejores de la ciudad. 180 EGP."},
        {"title": "Corniche al atardecer", "description": "El paseo marítimo de 26km es el alma de Alejandría — las familias, los pescadores con caña y los cafés con vistas al Mediterráneo al caer el sol crean el ambiente más mediterráneo de Egipto."},
        {"title": "Café Athineos y Pastroudis", "description": "Los cafés históricos de la época cosmopolita del siglo XX (algunos abiertos desde 1928) sirven café griego, pastelería vienesa y el ambiente de la Alejandría de Durrell. Experiencia única."},
        {"title": "Anfiteatro Romano de Kom el-Dikka", "description": "El único anfiteatro romano descubierto en Egipto, con 13 filas de mármol blanco perfectamente conservado y una villa romana con mosaicos en el mismo recinto. 180 EGP."}
    ],
    "food_and_drink": "Alejandría tiene la mejor gastronomía de mariscos de Egipto: gambas y calamares fritos del Mediterráneo, sayyadiya (arroz con pescado y cebolla caramelizada), el sandwichería de hawawshi (carne especiada en pan) y los pasteles de la era griega que sobreviven en los cafés históricos. Los restaurantes de la Corniche tienen marisco por 10-20$. Un kilo de gambas frescas en el puerto: 3-5$.",
    "safety": "Alejandría es más relajada que El Cairo para turistas. Los barrios históricos y la Corniche son seguros. Cuidado con los timos de taxi — negocia precio siempre.",
    "visa_info": "Los españoles pueden obtener visa a la llegada en Egipto (25$) o e-visa online. Si ya tienes visa de Egipto para El Cairo, cubre también Alejandría. Moneda: libra egipcia (EGP). 1€ ≈ 55 EGP.",
    "local_tips": ["El tren desde El Cairo a Alejandría es cómodo, económico y con vistas del Delta del Nilo", "Los cafés históricos de la época cosmopolita (Athineos, Pastroudis) sirven el mejor café griego de África", "La Bibliotheca Alexandrina tiene una terraza en la planta superior con vistas del Mediterráneo — entra aunque no leas", "El hawawshi (pan con carne) del barrio de Muharram Bey es el mejor street food de Alejandría", "Negocia los taxis siempre — la app Uber/Careem funciona en Alejandría y es más transparente"],
    "travel_styles": ["historia", "cultura", "gastronomía", "mediterráneo"],
    "vibes": ["mediterranean", "greek-roman", "cosmopolitan", "sea"],
    "climate": ["mediterranean"],
    "best_months": ["October", "November", "December", "January", "February", "March", "April"],
    "budget_daily_low": 25, "budget_daily_mid": 55, "budget_daily_high": 140, "guide_quality": 8
},
]

inserted = 0
skipped = 0
for city in cities:
    cur.execute("SELECT slug FROM destinations WHERE slug = %s", (city["slug"],))
    if cur.fetchone():
        print(f"SKIP (exists): {city['slug']}")
        skipped += 1
        continue
    
    cur.execute("""
        INSERT INTO destinations (
            slug, name, country, continent, type, coordinates, tagline, intro,
            when_to_go, how_to_get_there, where_to_sleep, what_to_do,
            food_and_drink, safety, visa_info, local_tips,
            travel_styles, vibes, climate, best_months,
            budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality
        ) VALUES (
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        )
    """, (
        city["slug"], city["name"], city["country"], city["continent"], city["type"],
        json.dumps(city["coordinates"]), city["tagline"], city["intro"],
        city["when_to_go"], city["how_to_get_there"],
        json.dumps(city["where_to_sleep"]), json.dumps(city["what_to_do"]),
        city["food_and_drink"], city["safety"], city["visa_info"],
        city["local_tips"], city["travel_styles"], city["vibes"],
        city["climate"], city["best_months"],
        city["budget_daily_low"], city["budget_daily_mid"], city["budget_daily_high"],
        city["guide_quality"]
    ))
    print(f"INSERT: {city['slug']}")
    inserted += 1

conn.commit()
cur.close()
conn.close()
print(f"\nDone: {inserted} inserted, {skipped} skipped")
