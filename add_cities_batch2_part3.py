import psycopg2
import json

conn = psycopg2.connect("dbname=viajeramente user=tenant")
cur = conn.cursor()

cities = [
# AMÉRICAS
{
    "slug": "seattle", "name": "Seattle", "country": "Estados Unidos", "continent": "América", "type": "city",
    "coordinates": {"lat": 47.6062, "lng": -122.3321},
    "tagline": "Coffee culture, grunge, el Monte Rainier y el inicio de la ruta de los parques del noroeste",
    "intro": "Seattle es la ciudad americana que mejor combina naturaleza salvaje y urbanismo de calidad: el Monte Rainier (4.392m con glaciares) se ve desde el centro en días despejados, el sonido de Puget Sound separa la ciudad del Olympic Peninsula, y los parques de los Cascades están a menos de dos horas. La ciudad inventó el concepto moderno de café de especialidad (Starbucks empezó aquí, pero Pike Place Roast y Victrola Coffee son el nivel real).\n\nEl barrio de Capitol Hill es el epicentro cultural — librerías independientes, bares de todo tipo, el mejor mercado de segunda mano de la ciudad y la escena LGBTQ+ más activa del noroeste. El mercado de Pike Place Market no es solo un atractivo turístico — es donde los restaurantes de la ciudad compran el pescado del día.\n\nSeattle fue también el epicentro del grunge (Nirvana, Pearl Jam, Soundgarden son de aquí) y hay un museo extraordinario dedicado a la música de la región.",
    "when_to_go": "Julio-septiembre: el único período fiable de sol, temperaturas de 20-26°C y toda la actividad al aire libre. El resto del año llueve frecuentemente (es la ciudad más lluviosa de EEUU después de Miami). El invierno permite esquiar en Summit at Snoqualmie (90 min).",
    "how_to_get_there": "Aeropuerto Internacional de Seattle-Tacoma (SEA) con conexiones globales. Link Light Rail al centro en 40 min (3$). Ferries a Bainbridge Island y la Península Olímpica desde el terminal del centro.",
    "where_to_sleep": [
        {"name": "Capitol Hill", "description": "El barrio más animado y diverso, con los mejores bares y restaurantes. Hoteles boutique desde 100$, hostels desde 35$."},
        {"name": "Belltown / Pike Place", "description": "Junto al mercado y el waterfront. Práctico para visitas pero turístico. Hoteles desde 110$."},
        {"name": "University District", "description": "El barrio universitario, más económico y con ambiente joven. Apartamentos desde 75$/noche."}
    ],
    "what_to_do": [
        {"title": "Pike Place Market", "description": "El mercado más antiguo de EEUU (1907) con fishmongers que lanzan el salmón en el aire, floristas, productores y el primer Starbucks original (la cola vale el rato). Llega antes de las 9h."},
        {"title": "Space Needle y Seattle Center", "description": "La torre del 62 de 184m con el anillo de vidrio inclinado a 160m. Vista de 360° del Monte Rainier, Puget Sound y los Cascades (35$). El MoPOP (museo de la cultura pop) al lado es imprescindible."},
        {"title": "Capitol Hill y los bares independientes", "description": "La calle Broadway y las calles adyacentes concentran las mejores librerías, cafés de especialidad y bares de craft beer. La escena más auténtica de Seattle."},
        {"title": "Excursión al Parque Nacional del Monte Rainier", "description": "A 90 min en coche, el volcán nevado más grande del sistema de los Cascades tiene rutas de senderismo extraordinarias y vistas de glaciares desde el Paradise Visitor Center (35$ coche/entrada)."},
        {"title": "Ferry a Bainbridge Island", "description": "El ferry más barato de EEUU (9$) cruza el Puget Sound en 35 min. Bainbridge tiene bodegas, restaurantes y las mejores vistas de vuelta a Seattle desde el agua."},
        {"title": "Seattle Art Museum y Chihulyhaus", "description": "El SAM tiene colecciones de arte nativo del noroeste y arte contemporáneo. El Garden and Glass de Dale Chihuly (experto en cristal soplado) es visualmente espectacular (30$)."}
    ],
    "food_and_drink": "El salmón del Pacífico (especialmente el king salmon y el sockeye), los Dungeness crab (cangrejos del noroeste), los ostiones de Puget Sound y el teriyaki de la ciudad (influencia japonesa-americana) definen la cocina local. Los food trucks de Capitol Hill tienen la mejor relación calidad-precio. Cena de marisco 25-45$. Café de especialidad: 5-7$.",
    "safety": "Seattle es segura en barrios turísticos. El Downtown y Belltown tienen zonas de fentanilo y personas sin hogar que pueden incomodar pero raramente presentan peligro real. Capitol Hill es muy seguro. Coche: riesgo de rotura de ventanilla — no dejes nada visible.",
    "visa_info": "Españoles necesitan ESTA (Sistemas de Autorización Electrónica de Viaje, 21$, solicitar online antes del viaje). No se requiere visa para estancias hasta 90 días.",
    "local_tips": ["El Light Rail del aeropuerto es la forma más eficiente de llegar al centro — evita el taxi", "El Orca Card es la tarjeta recargable de transporte, incluye buses, trenes y ferries de Sound Transit", "Los museos tienen 'first thursday free' algunos meses — revisa el calendario", "En Pike Place, el puesto de bouquets de flores frescos cuesta la mitad que en cualquier floristería", "El Mount Rainier requiere reserva de aparcamiento en temporada alta — haz la reserva online"],
    "travel_styles": ["naturaleza", "cultura", "gastronomía", "outdoor"],
    "vibes": ["pacific northwest", "grunge", "coffee", "rainy"],
    "climate": ["oceanic", "rainy"],
    "best_months": ["July", "August", "September"],
    "budget_daily_low": 80, "budget_daily_mid": 160, "budget_daily_high": 380, "guide_quality": 8
},
{
    "slug": "boston", "name": "Boston", "country": "Estados Unidos", "continent": "América", "type": "city",
    "coordinates": {"lat": 42.3601, "lng": -71.0589},
    "tagline": "La cuna de la independencia americana, con universidades legendarias y el mejor marisco del Atlántico",
    "intro": "Boston es la ciudad americana con más historia por metro cuadrado: el Freedom Trail conecta 16 lugares de la Revolución Americana a lo largo de un kilómetro y medio de línea roja pintada en el suelo. Harvard y el MIT están a 20 minutos en metro, Fenway Park lleva 110 años siendo el estadio más antiguo de las Grandes Ligas y el barrio de Beacon Hill tiene las únicas calles adoquinadas y las casas de ladrillo rojo más bonitas de EEUU.\n\nLo que hace diferente a Boston de otras ciudades del noreste es su escala humana — se puede recorrer completamente a pie. El Harbor de Boston, los barrios de Cambridge (MIT y Harvard Square), el South End y el distrito de Back Bay forman un conjunto urbano donde el pasado colonial y el presente universitario conviven naturalmente.\n\nLas langostas de Maine y el chowder de almejas de Nueva Inglaterra son aquí una forma de vida.",
    "when_to_go": "Septiembre-octubre: el otoño americano con los colores de los arces es el momento más espectacular — uno de los colores de otoño más bonitos de EEUU. Primavera (abril-mayo) es agradable. El invierno (dic-feb) es frío con posibilidad de nieve pero los precios bajan.",
    "how_to_get_there": "Aeropuerto Logan con conexiones globales. Silver Line (bus gratuito) o Blue Line del metro al centro en 20-30 min. Amtrak desde Nueva York en 4h (desde 40$).",
    "where_to_sleep": [
        {"name": "Back Bay / Newbury Street", "description": "El barrio más elegante con las mejores tiendas y acceso al jardín público. Hoteles desde 120$."},
        {"name": "South End", "description": "El barrio más animado gastronómicamente, con excelentes restaurantes. Apartamentos desde 100$/noche."},
        {"name": "Cambridge / Harvard Square", "description": "Al otro lado del río Charles, ambiente universitario incomparable. Hostels desde 45$, hoteles desde 95$."}
    ],
    "what_to_do": [
        {"title": "Freedom Trail", "description": "Los 4km de línea roja en el suelo conectan el Boston Common, Paul Revere's House, la Old North Church y el Bunker Hill Monument. Guía gratuita disponible, visita guiada recomendada (15$)."},
        {"title": "Harvard Square y campus del MIT", "description": "La plaza de Harvard Square con sus librerías, cafés y el famoso campus. El MIT tiene un campus abierto con arquitectura de Gehry y Pei. Ambos gratuitos para pasear."},
        {"title": "Quincy Market y Faneuil Hall", "description": "El mercado histórico del siglo XVIII y el centro de food court más concurrido de Boston. Para langosta, clam chowder y cannoli — más turístico pero de calidad."},
        {"title": "Museum of Fine Arts", "description": "Una de las mejores colecciones de arte de EEUU: arte americano, impresionismo francés, arte antiguo egipcio y griego. Miércoles 4-9pm pago voluntario (25$ normalmente)."},
        {"title": "Excursión a Cape Cod", "description": "A 90 min en ferry o coche, las playas de la lengua arenosa de Cape Cod son las mejores de Nueva Inglaterra. Provincetown en el extremo tiene el ambiente más animado."},
        {"title": "Partidos de los Red Sox en Fenway Park", "description": "Una visita al estadio más antiguo de las Grandes Ligas (1912) es una experiencia cultural americana. Entradas desde 25$, visita guiada cuando no hay partido (22$)."}
    ],
    "food_and_drink": "Boston es la capital mundial del clam chowder (sopa de almejas con patata y nata — la blanca, no la de Manhattan) y la langosta de Maine. Neptune Oyster en North End, Legal Sea Foods y las puestos del Quincy Market son los referentes. Los cannoli del North End (barrio italiano) de Modern Pastry son legendarios. Cena de marisco 35-60$.",
    "safety": "Boston es segura para turistas. Precaución estándar en zonas de transporte. Los barrios históricos son muy seguros. Conducir en Boston es difícil — el 'Masshole' (conductor de Massachusetts) es un estereotipo con base real.",
    "visa_info": "Españoles necesitan ESTA (21$, solicitar online antes del viaje). Estancias hasta 90 días sin visa.",
    "local_tips": ["El metro (T) es el más antiguo de EEUU y tiene sus peculiaridades — descarga la app MBTA", "El Freedom Trail es autoguiado y gratuito — descarga el mapa oficial", "Los cannoli de Modern Pastry en el North End cuestan 3$ y son mejores que los de Mike's Pastry (que tiene más fama)", "Cape Cod en temporada alta (julio-agosto) tiene mucho tráfico — ve en septiembre", "El pase American Museum Alliance da entrada reducida en muchos museos si ya tienes uno de otra ciudad"],
    "travel_styles": ["historia", "cultura", "gastronomía", "universitario"],
    "vibes": ["colonial", "ivy league", "seafood", "autumn"],
    "climate": ["humid continental"],
    "best_months": ["September", "October", "May", "June"],
    "budget_daily_low": 85, "budget_daily_mid": 170, "budget_daily_high": 380, "guide_quality": 8
},
{
    "slug": "washington-dc", "name": "Washington DC", "country": "Estados Unidos", "continent": "América", "type": "city",
    "coordinates": {"lat": 38.9072, "lng": -77.0369},
    "tagline": "Los mejores museos gratuitos del mundo y el poder americano en cada esquina",
    "intro": "Washington DC tiene la concentración más alta de museos gratuitos de clase mundial del planeta — el Smithsonian Institution controla 19 museos de acceso libre en el Mall, incluyendo el Museo Nacional del Aire y el Espacio, el de Historia Natural y la Galería Nacional de Arte. Es literalmente la ciudad donde puedes pasar una semana entrando a museos sin pagar un centavo.\n\nEl Mall — el paseo central entre el Lincoln Memorial y el Capitolio — es uno de los espacios públicos más cargados de simbolismo del mundo. La Casa Blanca, el Pentágono (visitable con reserva), la Biblioteca del Congreso y la Corte Suprema rodean a los ciudadanos con las instituciones del poder americano de forma casi teatral.\n\nEl barrio de Adams Morgan, el Columbia Heights y el barrio de Georgetown tienen la mejor escena gastronómica y de bares — lejos del turismo institucional del Mall.",
    "when_to_go": "Marzo-mayo: los cerezos japoneses en flor del Mall (especialmente en abril) son uno de los espectáculos más conocidos de EEUU. Septiembre-octubre tiene el mejor clima (20-25°C). El verano (junio-agosto) es caluroso y húmedo (35°C+) pero los museos son el refugio perfecto.",
    "how_to_get_there": "Aeropuerto Reagan National (el más cercano al centro, Metro directo en 20 min) o Dulles Internacional. El Metro de DC es eficiente y cubre todos los atractivos principales.",
    "where_to_sleep": [
        {"name": "Dupont Circle", "description": "El barrio más animado con la mejor vida nocturna y restaurantes. Hoteles boutique desde 100$, hostels desde 40$."},
        {"name": "Capitol Hill", "description": "El barrio histórico junto al Capitolio, tranquilo y con carácter. Hoteles desde 110$."},
        {"name": "Adams Morgan", "description": "El barrio multicultural con la mejor gastronomía étnica y los precios más razonables. Apartamentos desde 85$/noche."}
    ],
    "what_to_do": [
        {"title": "Museos Smithsonian (gratuitos)", "description": "El Museo del Aire y el Espacio (cohete Saturn V, naves Apollo), el de Historia Natural (diamante Hope) y la Galería Nacional de Arte (Vermeer, Da Vinci, Monet) son GRATUITOS. Reserva entrada online en temporada alta."},
        {"title": "El Mall y los Memoriales", "description": "El paseo desde el Lincoln Memorial (donde Luther King pronunció 'I Have a Dream') hasta el Capitolio, con el reflejo pool, el Vietnam Veterans Memorial y el Washington Monument. Todo gratuito."},
        {"title": "Capitol Tour", "description": "El Capitolio, residencia del Congreso, tiene visitas gratuitas con reserva online previa. La sala de la Rotonda y la Cámara de Representantes son accesibles."},
        {"title": "Georgetown", "description": "El barrio universitario más elegante de DC, con la mejor concentración de restaurantes y el canal C&O para caminar o montar en bici junto al agua."},
        {"title": "Biblioteca del Congreso", "description": "La mayor biblioteca del mundo con una sala de lectura principal que es una de las más bonitas de EEUU. Gratuita, accesible a civiles."},
        {"title": "Museo Nacional de Arte Africano y Freer Gallery", "description": "Dos museos Smithsonian infravalorados con colecciones extraordinarias de arte africano y asiático. Siempre menos concurridos que el de Historia Natural."}
    ],
    "food_and_drink": "DC tiene una escena culinaria sorprendentemente buena dada su imagen política: José Andrés (chef español) tiene varios restaurantes de referencia (Jaleo, Oyamel, minibar). El barrio de Adams Morgan tiene la mayor diversidad de comida étnica. El Ben's Chili Bowl (U Street) con su chili half-smoke es un clásico de la cultura afroamericana. Cena 25-45$.",
    "safety": "DC es segura en zonas turísticas. El barrio del Mall, Capitol Hill, Georgetown y Dupont Circle son muy seguros. Evita las zonas al este del río Anacostia de noche.",
    "visa_info": "Españoles necesitan ESTA (21$, online antes del viaje). Estancias hasta 90 días sin visa.",
    "local_tips": ["TODOS los museos Smithsonian son gratuitos — reserva entrada online para los más populares (Aire y Espacio, Historia Natural)", "La tarjeta SmarTrip del metro es recargable y más barata que pagar en efectivo", "El Jefferson Memorial al atardecer con el reflejo en el Tidal Basin es la mejor foto de DC", "Los cafés del barrio de Logan Circle tienen la mejor tercera ola del café de la ciudad", "El Cherry Blossom Festival en abril requiere reservar alojamiento con meses de antelación"],
    "travel_styles": ["historia", "cultura", "museos", "política"],
    "vibes": ["capital", "monumental", "free museums", "power"],
    "climate": ["humid subtropical"],
    "best_months": ["March", "April", "May", "September", "October"],
    "budget_daily_low": 80, "budget_daily_mid": 160, "budget_daily_high": 380, "guide_quality": 8
},
{
    "slug": "las-vegas", "name": "Las Vegas", "country": "Estados Unidos", "continent": "América", "type": "city",
    "coordinates": {"lat": 36.1699, "lng": -115.1398},
    "tagline": "El mayor espectáculo sobre la Tierra, puerta al Gran Cañón y Monument Valley",
    "intro": "Las Vegas es exactamente lo que parece y aún así sorprende. El Strip — los 7km de casinos y hoteles monumentales con réplicas del Coliseo, la Torre Eiffel y la Estatua de la Libertad — es una de las experiencias urbanas más surrealistas del mundo. La ciudad no duerme, los bufés sirven a las 4am y todo está diseñado para mantener al visitante desorientado del tiempo real.\n\nLo que menos espera el viajero es que a 45 minutos en coche del Strip empiezan algunas de las naturalezas más extraordinarias de EEUU: el Gran Cañón del Colorado está a 4 horas, Monument Valley a 5 horas, el Parque Nacional de Zion a 2,5 horas y Valley of Fire a 1 hora. Las Vegas es la base perfecta para explorar el suroeste americano.\n\nPara el viajero presupuestado: los bufés (15-25$) son la solución gastronómica, los shows gratuitos del exterior (Bellagio fountain, Fremont Street Experience) son los mejores del strip y los casinos locales (fuera del Strip) ofrecen más valor.",
    "when_to_go": "Marzo-mayo y octubre-noviembre: temperaturas perfectas (20-28°C) para el Strip y las excursiones al desierto. El verano (junio-agosto) tiene temperaturas de 40-45°C — solo viable si permaneces en los casinos con aire acondicionado. El invierno es agradable (10-20°C) y con muchos menos turistas.",
    "how_to_get_there": "Aeropuerto Internacional Harry Reid directamente junto al Strip. Taxi al Strip: 18-25$. Monorail del aeropuerto inaugurado en 2021 (3$). Muchos vuelos desde ciudades europeas.",
    "where_to_sleep": [
        {"name": "The Strip (Centro)", "description": "Los grandes casinos-hotel (MGM, Bellagio, Caesars) son la experiencia, pero caros (80-200$/noche en fin de semana). Busca precios entre semana."},
        {"name": "Off-Strip", "description": "A 10 min del Strip los hoteles cuestan la mitad. El Rio, el Palms y el Stratosphere son buenas opciones."},
        {"name": "Downtown (Fremont Street)", "description": "El Vegas original, más económico y con el Fremont Street Experience (show de luz gratuito). Hoteles desde 40$/noche."}
    ],
    "what_to_do": [
        {"title": "The Strip de noche", "description": "El paseo nocturno entre el Bellagio y el MGM Grand es el mejor show gratuito de Las Vegas. Las fuentes del Bellagio cada 15-30 min, la Estatua de la Libertad de New York-New York y el Coliseo de Caesars."},
        {"title": "Fremont Street Experience", "description": "El Vegas original con el mayor techo de LED del mundo (460m de pantalla) con shows de luz y sonido gratuitos cada hora. Más auténtico y menos caro que el Strip."},
        {"title": "Gran Cañón (excursión de día o dos días)", "description": "A 4h en coche (South Rim) o 2,5h al West Rim. El helicóptero desde Las Vegas al fondo del cañón es una experiencia extraordinaria (200-300$). Con coche propio, el South Rim es imprescindible."},
        {"title": "Parque Nacional Zion", "description": "A 2,5h, uno de los parques nacionales más espectaculares de EEUU con el Narrows (senderismo por el río en un desfiladero) y el Angel's Landing. Entrada 35$/coche."},
        {"title": "Valley of Fire State Park", "description": "A 1h, un parque de roca roja de 150 millones de años con petroglifos nativos americanos y formaciones que parecen de Marte. Solo 15$ de entrada."},
        {"title": "Bufé de Wicked Spoon o ARIA", "description": "Los bufés de Las Vegas son una institución — decenas de estaciones de comida diferente en un mismo sitio. Wicked Spoon es el mejor precio-calidad del Strip (30-40$)."}
    ],
    "food_and_drink": "Las Vegas tiene los restaurantes más baratos y los más caros de EEUU simultáneamente. Los bufés (15-45$) son la solución económica. Cada gran casino tiene restaurantes de chef con Michelin (Joel Robuchon, Gordon Ramsay, Guy Savoy) a precios de 60-150$/persona. Los happy hours de casinos locales ofrecen las mejores cervezas baratas de la ciudad.",
    "safety": "El Strip y el Downtown son seguros para turistas. Las zonas residenciales al este del Strip tienen mayor criminalidad — no te salgas de las áreas turísticas. Los casinos tienen seguridad interna excelente.",
    "visa_info": "Españoles necesitan ESTA (21$, online antes del viaje). Estancias hasta 90 días sin visa.",
    "local_tips": ["Las Vegas entre semana puede ser el doble de barata que el fin de semana en alojamiento", "La mayoría de shows gratuitos del Strip no requieren consumición — solo paciencia para ver las fuentes del Bellagio", "Alquila coche para los parques — las excursiones organizadas son más caras y menos flexibles", "El bono del casino (free play) viene con el registro en cualquier loyalty card — recoge las de cada casino que visites", "El Fremont Street Experience es el mejor show de Las Vegas por 0€"],
    "travel_styles": ["entretenimiento", "naturaleza", "cultura", "aventura"],
    "vibes": ["neon", "casino", "desert gateway", "over the top"],
    "climate": ["hot desert"],
    "best_months": ["March", "April", "October", "November"],
    "budget_daily_low": 70, "budget_daily_mid": 150, "budget_daily_high": 500, "guide_quality": 8
},
{
    "slug": "denver", "name": "Denver", "country": "Estados Unidos", "continent": "América", "type": "city",
    "coordinates": {"lat": 39.7392, "lng": -104.9903},
    "tagline": "La ciudad a 1.600m donde las Rocosas empiezan y el craft beer no para",
    "intro": "Denver se llama la 'Mile High City' porque está literalmente a una milla de altitud (1.609m). No es tan alto como para notar el mal de altura, pero es suficiente para que la cerveza te golpee más rápido — algo que los habitantes de la ciudad con más cervecerías artesanales per cápita de EEUU han convertido en un argumento turístico.\n\nEl Downtown de Denver tiene el parque de arte urbano más grande de EEUU (Sculpture Park), el Denver Art Museum con una de las mejores colecciones de arte nativo americano del mundo y el Red Rocks Amphitheatre — el anfiteatro natural de roca roja a 40 minutos donde los conciertos bajo las estrellas son una experiencia única.\n\nLo que realmente define Denver es que es la puerta a las Rocosas: el Rocky Mountain National Park está a 90 minutos, Vail y Breckenridge a 2 horas, y el desierto de Moab (Utah) a 4,5 horas.",
    "when_to_go": "Junio-agosto para senderismo y parques. Diciembre-marzo para esquí (los mejores resorts de EEUU están a 2h). El otoño (sept-oct) tiene los colores del aspen (álamo temblón) más espectaculares de EEUU. La ciudad recibe 300 días de sol al año.",
    "how_to_get_there": "Aeropuerto Internacional de Denver, el más grande en área de EEUU. Tren A-Line al centro en 37 min (11$). Buen hub con conexiones directas de Europa.",
    "where_to_sleep": [
        {"name": "LoDo (Lower Downtown)", "description": "El barrio histórico con los mejores bares y restaurantes. Hoteles boutique desde 100$, hostels desde 38$."},
        {"name": "Capitol Hill", "description": "El barrio artístico y bohemio, más económico y auténtico. Apartamentos desde 85$/noche."},
        {"name": "RiNo (River North)", "description": "El barrio de galerías y cervecerías artesanales, el más creativo de Denver. Hoteles boutique desde 120$."}
    ],
    "what_to_do": [
        {"title": "Red Rocks Amphitheatre", "description": "El anfiteatro natural de rocas rojas de 300 millones de años a 40 min del centro. Impresionante aunque no haya concierto — hay senderos y yoga matutino gratuito. Con concierto: una experiencia única."},
        {"title": "Denver Art Museum", "description": "Una de las mejores colecciones de arte nativo americano del mundo, más arte contemporáneo en un edificio de Daniel Libeskind. Sábados hay entrada gratuita con descuentos."},
        {"title": "Rocky Mountain National Park", "description": "A 90 min, uno de los parques más visitados de EEUU con más de 150 picos por encima de 3.000m. Trail Ridge Road (abierta en verano) llega a 3.713m en coche (35$/coche)."},
        {"title": "Barrio RiNo y craft beer trail", "description": "River North tiene la mayor concentración de cervecerías artesanales de Denver. Great Divide, Breckenridge Brewery y Odell son los más conocidos — el tour de cervecería es gratuito."},
        {"title": "Union Station y LoDo", "description": "La estación histórica de trenes reconvertida en epicentro social con restaurantes, una cervecería y un hotel boutique. El punto de encuentro del Denver moderno."},
        {"title": "Excursión a Breckenridge o Vail", "description": "A 2h en coche, los mejores resorts de esquí de EEUU. En verano funcionan como resorts de mountain biking y senderismo de alta montaña."}
    ],
    "food_and_drink": "Denver tiene una escena gastronómica emergente con mucha influencia del suroeste americano: green chile (salsa de chile verde sobre huevos, burritos o hamburguesas), bison burgers, steaks de Colorado y la mejor craft beer del país. Los mercados de Union Station y el Source Market Hall tienen la mejor selección.",
    "safety": "Denver es segura en barrios turísticos. El Downtown (especialmente el área 16th Street Mall) tiene zonas de personas sin hogar con problemas de fentanilo — el mismo perfil que otras ciudades americanas. LoDo y RiNo son muy seguros.",
    "visa_info": "Españoles necesitan ESTA (21$, online antes del viaje). Estancias hasta 90 días sin visa.",
    "local_tips": ["La altitud afecta más de lo esperado en las primeras 24h — hidratación y cuidado con el alcohol", "El A-Line del aeropuerto al centro es la mejor inversión de 11$ — puntual y directo", "El RTD bus y tren cubren bien el centro — compra la MyDenver Pass de 24h (6$)", "Red Rocks es espectacular de noche para conciertos — reserva entradas con meses de antelación", "Los mercados de productores del Colorado del sábado en Union Station tienen los mejores melocotones del mundo (en agosto)"],
    "travel_styles": ["naturaleza", "outdoor", "cultura", "esquí"],
    "vibes": ["rocky mountains", "craft beer", "outdoor", "mile high"],
    "climate": ["semi-arid", "sunny", "snowy winters"],
    "best_months": ["June", "July", "August", "September"],
    "budget_daily_low": 75, "budget_daily_mid": 150, "budget_daily_high": 350, "guide_quality": 8
},
{
    "slug": "cancun", "name": "Cancún", "country": "México", "continent": "América", "type": "city",
    "coordinates": {"lat": 21.1619, "lng": -86.8515},
    "tagline": "El Caribe mexicano: cenotes, arrecifes de coral, ruinas mayas y la Riviera Maya a la puerta",
    "intro": "Cancún tiene mala fama como destino de turismo de masas y algo de razón hay en ello — la Zona Hotelera con sus 26km de hoteles todo-incluido puede ser abrumadora. Pero Cancún es también la puerta a una de las regiones más ricas de México: las ruinas mayas de Chichén Itzá y Tulum, los cenotes (pozos naturales de agua dulce de la selva) de la Riviera Maya, el segundo arrecife de coral más grande del mundo y la Isla Mujeres.\n\nEl centro de Cancún (El Centro, o Downtown Cancún) es donde viven los locales y donde los precios vuelven a la realidad: tacos por 1€, mercados de artesanías y el ambiente de ciudad mexicana real lejos de los resorts.\n\nCancún funciona mejor como base de operaciones que como destino final — con acceso en autobús económico a Tulum (2h), Playa del Carmen (1h), Chichén Itzá (3h) y las cenotes más espectaculares de la Península de Yucatán.",
    "when_to_go": "Diciembre-abril: clima perfecto (25-30°C), mares calmados y la temporada alta del turismo. Mayo-junio es más tranquilo y económico antes del huracán. Junio-octubre es la temporada de huracanes — riesgo real aunque no siempre impactan directamente.",
    "how_to_get_there": "Aeropuerto Internacional de Cancún, el más concurrido de México. Muchos vuelos directos desde Europa (Iberia, Air Europa, Condor). Bus ADO al centro en 20 min (70 pesos). A la Zona Hotelera: bus R1 (10 pesos) o taxi (200-300 pesos).",
    "where_to_sleep": [
        {"name": "Downtown Cancún (El Centro)", "description": "Donde viven los locales, precios reales: hostels desde 12$, hoteles desde 40$. Auténtico y económico."},
        {"name": "Zona Hotelera (km 9-14)", "description": "El Caribe a la puerta y acceso a playas de resort. Todo-incluido desde 100$/noche, hoteles independientes desde 80$."},
        {"name": "Playa del Carmen (base alternativa)", "description": "A 1h en bus, más auténtica que la Zona Hotelera y con la misma accesibilidad a todo."}
    ],
    "what_to_do": [
        {"title": "Chichén Itzá (excursión de día)", "description": "La pirámide maya más famosa del mundo, a 3h en bus (ADO desde Cancún, 300 pesos). Madruga para llegar antes de los tours en grupo (8am, antes del calor y las masas). Entrada: 600 pesos."},
        {"title": "Cenotes de la Riviera Maya", "description": "Los pozos naturales de agua dulce con estalactitas son únicos en el mundo. El Gran Cenote y Dos Ojos en Tulum son los más espectaculares. Snorkel incluido en la mayoría (200-400 pesos)."},
        {"title": "Isla Mujeres", "description": "A 20 min en ferry (200 pesos), la isla con las mejores playas del Caribe mexicano y el pueblo más auténtico del área. Alquila golf cart (400 pesos/día) para dar la vuelta."},
        {"title": "Ruinas de Tulum sobre el Caribe", "description": "A 2h en bus, las únicas ruinas mayas frente al Caribe — el postal más icónico de Yucatán. Llega antes de las 9am. Entrada: 90 pesos."},
        {"title": "Snorkel en el arrecife de Mesoamérica", "description": "El segundo arrecife de coral más grande del mundo pasa frente a Cancún e Isla Mujeres. Tours de snorkel desde el Embarcadero: 50-80$ con almuerzo y bebidas."},
        {"title": "Mercados de El Centro", "description": "El Mercado 23 y el Mercado 28 tienen la mejor comida local: tacos de cochinita pibil (1,5€/taco), poc chuc, marquesitas y la mejor fruta tropical de México por precios de mercado local."}
    ],
    "food_and_drink": "La cocina yucateca es una de las más complejas de México: cochinita pibil (cerdo marinado en achiote asado en hojas de banana), poc chuc (carne asada con naranja agria), panuchos y salbutes (antojitos con frijoles y pavo), tikinxic (pescado a la brasa con chile). Los mercados del Centro son la mejor opción económica (2-4€ por plato). Zona Hotelera: 15-30$/plato.",
    "safety": "Cancún tuvo problemas de seguridad en años anteriores pero la Zona Hotelera y El Centro turístico son seguros. Evita ir solo de noche a zonas residenciales desconocidas. El transporte público (bus R1/R2) es seguro durante el día.",
    "visa_info": "Españoles entran sin visado hasta 180 días. Paga la tarjeta de turista incluida en el billete de avión. Moneda: peso mexicano (MXN). 1€ ≈ 19-20 MXN.",
    "local_tips": ["El bus ADO es la forma más cómoda de moverse entre ciudades — puntual y con aire acondicionado", "Los cenotes cierran temprano (5pm) — organiza el día para llegar a primera hora", "El Chichén Itzá se visita mejor llegando antes de las 9am para evitar calor y grupos", "Negocia el precio del taxi siempre o usa InDriver/Cabify", "La tarjeta bancaria funciona en todos lados pero las comisiones pueden ser altas — saca efectivo en cajeros bancarios"],
    "travel_styles": ["playa", "cultura", "naturaleza", "aventura"],
    "vibes": ["caribbean", "mayan", "beach", "cenotes"],
    "climate": ["tropical"],
    "best_months": ["December", "January", "February", "March", "April"],
    "budget_daily_low": 40, "budget_daily_mid": 85, "budget_daily_high": 280, "guide_quality": 8
},
{
    "slug": "guadalajara", "name": "Guadalajara", "country": "México", "continent": "América", "type": "city",
    "coordinates": {"lat": 20.6597, "lng": -103.3496},
    "tagline": "La segunda ciudad de México: cuna del mariachi, el tequila y la torta ahogada",
    "intro": "Guadalajara es la segunda ciudad de México y la más mexicana de todas — aquí nacieron el mariachi, el tequila, la charrería (rodeo mexicano) y el jarabe tapatío (el jarabe nacional). Tiene el carácter que Ciudad de México ha perdido parcialmente con su hiperglobalización: mercados de barrio, fiestas patronales en cada colonia y un orgullo cultural que se nota en cada cantina.\n\nEl centro histórico de Guadalajara, con la catedral doble-torre, el Teatro Degollado y los jardines es uno de los más bonitos de México. El barrio de Tlaquepaque (literalmente 'encima del barro') a 7 km del centro es el centro artesanal más importante del país con cerámica talavera, vidrio soplado y muebles de madera.\n\nDesde Guadalajara se puede llegar en 2 horas al Lago de Chapala (el mayor lago de México) y a la ciudad de Tequila para la experiencia de destilería original.",
    "when_to_go": "Octubre-mayo: la mejor temporada. Guadalajara tiene un clima casi perfecto todo el año gracias a su altitud (1.566m) pero el verano (junio-septiembre) trae el monzón del Pacífico con lluvias fuertes. Temperaturas siempre entre 15-28°C.",
    "how_to_get_there": "Aeropuerto Internacional de Guadalajara con conexiones directas de EEUU, México y vuelos internacionales. Tren Suburbano o taxis al centro. Autobuses de larga distancia desde Ciudad de México (6h) y la costa.",
    "where_to_sleep": [
        {"name": "Centro Histórico", "description": "El corazón de Guadalajara, animado y con todos los atractivos a pie. Hostels desde 12$, hoteles boutique desde 50$."},
        {"name": "Chapultepec / Americana", "description": "El barrio más trendy con los mejores cafés y restaurantes de la ciudad. Apartamentos desde 40$/noche."},
        {"name": "Tlaquepaque", "description": "El pueblo artesanal a 7km del centro. Hoteles boutique en casas coloniales desde 60$. Ideal para estancias más largas."}
    ],
    "what_to_do": [
        {"title": "Centro Histórico y Catedral", "description": "El conjunto catedral-palacio de gobierno-museo regional forma uno de los centros históricos más completos de México. Los murales de Orozco en el Hospicio Cabañas (UNESCO) son de la mayor calidad en México."},
        {"title": "Tlaquepaque — pueblo artesanal", "description": "El centro artesanal más importante de México: cerámica talavera, vidrio soplado y Huichol. La calle Independencia con sus galerías y restaurantes es perfecta para una tarde."},
        {"title": "Excursión a la ciudad de Tequila", "description": "A 60 km, el Pueblo Mágico donde se produce el tequila auténtico. Tours de destilería en Casa Herradura o Cazadores (100-200 pesos, con catado incluido)."},
        {"title": "Mercado de San Juan de Dios", "description": "El mercado cubierto más grande de América Latina (3 pisos, 3.000 puestos). El nivel gastronómico (birria, tortas ahogadas, jugos) del sótano es la mejor comida callejera de la ciudad."},
        {"title": "Lago de Chapala", "description": "A 45 km, el mayor lago de México con el pueblo colonial de Ajijic a orillas del agua. La comunidad de expatriados americanos y canadienses le da un ambiente peculiar."},
        {"title": "Zona Rosa / Chapultepec de noche", "description": "La avenida Chapultepec concentra los mejores bares y restaurantes de la nueva Guadalajara. La escena de los jueves y viernes es la más animada de la ciudad."}
    ],
    "food_and_drink": "La cocina tapatía (de Guadalajara) es de las más ricas de México: la torta ahogada (sándwich de cerdo bañado en salsa picante de chile de árbol) es el plato más icónico. La birria (estofado de cabra o ternera con chile), los pozoles de cerdo y los tamales jalicienses completan el repertorio. Las cantinas de barrio (La Fonda de San Miguel, Los Famosos Equipales) son el lugar más auténtico.",
    "safety": "Guadalajara es relativamente segura en zonas turísticas. El Centro Histórico y Chapultepec son seguros de día y noche. Evita el estadio Jalisco y las colonias periféricas de noche. Usa Uber en lugar de taxis.",
    "visa_info": "Españoles entran sin visado hasta 180 días. Moneda: peso mexicano (MXN). 1€ ≈ 19-20 MXN.",
    "local_tips": ["La torta ahogada es el plato que debes pedir en Guadalajara — en El Abajeño o cualquier puesto del mercado", "El tequila auténtico en la ciudad de Tequila es completamente diferente al que se exporta", "Uber funciona perfectamente en Guadalajara y es mucho más seguro que los taxis de calle", "El Hospicio Cabañas (murales de Orozco) es tan bueno como cualquier mural de Rivera en CDMX", "Tlaquepaque de tarde-noche tiene ambiente de plaza animada — quédate para la cena"],
    "travel_styles": ["cultura", "gastronomía", "historia", "artesanía"],
    "vibes": ["mexican", "traditional", "mariachi", "colonial"],
    "climate": ["subtropical highland"],
    "best_months": ["October", "November", "December", "January", "February", "March", "April", "May"],
    "budget_daily_low": 30, "budget_daily_mid": 65, "budget_daily_high": 160, "guide_quality": 8
},
{
    "slug": "montevideo", "name": "Montevideo", "country": "Uruguay", "continent": "América", "type": "city",
    "coordinates": {"lat": -34.9011, "lng": -56.1645},
    "tagline": "La capital más liveable de América del Sur: sin prisa, con ramblas, mate y la mejor carne del mundo",
    "intro": "Montevideo tiene fama de ser la ciudad más aburrida de América del Sur y eso es exactamente lo que la hace especial. Sin los extremos de Buenos Aires ni los peligros de Rio, Montevideo es la capital latinoamericana donde el viajero puede relajarse: la rambla de 22km que bordea el Río de la Plata es el paseo urbano más largo de América, el mercado del Puerto tiene los asados de carne más honestos del continente y el barrio histórico Ciudad Vieja guarda una arquitectura art déco que sorprende.\n\nUruguay es el país más estable, progresista y seguro de Sudamérica — fue el primer país del mundo en legalizar la marihuana (2013), tiene el sistema de salud público más completo del continente y una igualdad social que se nota en la calle.\n\nLa vida gira alrededor del mate — el termo con agua caliente y el mate de hierba son el accesorio universal de todo uruguayo en todo momento. Que te ofrezcan un mate es la señal de bienvenida más genuina.",
    "when_to_go": "Diciembre-marzo: verano austral con temperaturas de 24-28°C y la rambla en su máximo esplendor. El otoño (abril-mayo) tiene los mejores colores y menos turistas. El invierno (junio-agosto) es frío (8-12°C) y gris, pero la ciudad interior sigue siendo completamente funcional.",
    "how_to_get_there": "Aeropuerto Internacional de Carrasco con conexiones de Argentina, Brasil, España y Chile. Buquebús (ferry) desde Buenos Aires en 2,5h por el Río de la Plata (desde 80$, la opción más bonita). Bus desde Buenos Aires: 8h por tierra más el ferry.",
    "where_to_sleep": [
        {"name": "Ciudad Vieja", "description": "El barrio histórico en la punta de la península, con los mejores hostels (desde 12$) y hoteles boutique (desde 60$)."},
        {"name": "Centro / Cordón", "description": "El barrio universitario más animado. Apartamentos desde 40$/noche, cafés y librerías."},
        {"name": "Pocitos", "description": "El barrio residencial con las mejores playas urbanas. Hoteles desde 55$, ambiente más tranquilo."}
    ],
    "what_to_do": [
        {"title": "Mercado del Puerto", "description": "El mercado de hierro del siglo XIX donde los parrilleros cocinan frente a ti enormes costillas de carne uruguaya. El chivito (sándwich de carne con huevo, jamón y lechuga) es el plato nacional. Precio parrillada: 25-40$."},
        {"title": "Rambla de Montevideo (22km)", "description": "El paseo marítimo más largo de América del Sur, desde el Puerto hasta el Parque Rodó y más allá. Idealmente en bicicleta (alquiler desde 8$/día). Los atardeceres sobre el Río de la Plata son memorables."},
        {"title": "Ciudad Vieja y Plaza Zabala", "description": "El casco histórico con el mejor art déco de Uruguay, el Palacio Salvo (el rascacielos más alto de Sudamérica cuando se construyó en 1928) y la Plaza Independencia con el mausoleo de Artigas."},
        {"title": "Feria de Tristán Narvaja (domingos)", "description": "El mercado de pulgas más completo de Uruguay: libros usados, vinilos, antigüedades y artesanías. El mejor domingo en Montevideo."},
        {"title": "Estadio Centenario y Museo del Fútbol", "description": "El estadio donde se jugó el primer Mundial de Fútbol en 1930 (y Uruguay lo ganó) tiene un museo extraordinario para los amantes del deporte (5$)."},
        {"title": "Colonia del Sacramento (excursión de día)", "description": "A 2,5h en bus, el barrio histórico colonial portugués del siglo XVII (UNESCO) a orillas del Río de la Plata es uno de los más bonitos de Sudamérica."}
    ],
    "food_and_drink": "Uruguay tiene la mejor carne del mundo por habitante — el asado de tira, el vacío y el chivito (el sándwich nacional con carne, huevo frito y ensalada) son incomparables. El chivito más auténtico de Montevideo es en El Uruguayo. El dulce de leche es la obsesión nacional. Vino Tannat uruguayo (la uva autóctona): excelente y barato. Cena completa 20-35$.",
    "safety": "Montevideo es la capital más segura de Sudamérica. El centro y Ciudad Vieja tienen algo de carterismo pero raramente agresividad. Muy segura para familias y viajeros solitarios.",
    "visa_info": "Españoles entran sin visado hasta 90 días. Moneda: peso uruguayo (UYU). 1€ ≈ 42 UYU.",
    "local_tips": ["El mate se acepta con la mano derecha y sin decir 'gracias' hasta que quieras parar", "El Mercado del Puerto es carísimo para comer — es la experiencia, no el precio", "Alquila una bici para la Rambla — sin coche el paseo de 22km se puede hacer en 2h tranquilamente", "La feria de Tristán Narvaja los domingos tiene los mejores vinilos de segunda mano de Sudamérica", "El ferry al anochecer desde Buenos Aires a Montevideo tiene las mejores vistas de ambas ciudades"],
    "travel_styles": ["gastronomía", "cultura", "naturaleza", "relajado"],
    "vibes": ["laid-back", "river plate", "steak", "mate"],
    "climate": ["humid subtropical"],
    "best_months": ["December", "January", "February", "March"],
    "budget_daily_low": 40, "budget_daily_mid": 80, "budget_daily_high": 180, "guide_quality": 8
},
{
    "slug": "quito", "name": "Quito", "country": "Ecuador", "continent": "América", "type": "city",
    "coordinates": {"lat": -0.1807, "lng": -78.4678},
    "tagline": "La capital más alta del mundo, con el casco histórico mejor conservado de América y la mitad del mundo a 30 minutos",
    "intro": "Quito es la segunda capital más alta del mundo (2.850m) y tiene el centro histórico colonial mejor conservado de toda América Latina — fue la primera ciudad declarada Patrimonio de la Humanidad por la UNESCO en 1978. Las iglesias barrocas del siglo XVII con interiores completamente cubiertos de oro, los conventos, los mercados y las plazas son de una calidad y escala que sorprende incluso a viajeros experimentados.\n\nLo que hace única a Quito es su geografía: está construida en un valle entre volcanes activos. El Pichincha (4.784m) domina la ciudad por el oeste. El teleférico (TelefériQo) sube a 4.100m desde el centro en 15 minutos, desde donde se ve toda la ciudad y el Chimborazo en días despejados.\n\nA 30 km del centro está la Mitad del Mundo — la línea del Ecuador — aunque el verdadero punto del Ecuador está en el museo Intiñan, a 200m del monumento oficial.",
    "when_to_go": "Ecuador tiene dos estaciones: la seca (junio-septiembre, diciembre-enero) con días soleados perfectos y la húmeda (febrero-mayo) con más lluvia pero paisajes más verdes. Quito a 2.850m tiene temperatura de primavera permanente (15-22°C), nunca hace calor ni frío extremo.",
    "how_to_get_there": "Aeropuerto Internacional Mariscal Sucre con conexiones de toda América y vuelos directos de Madrid (Iberia). Bus municipal al centro (0,25$). Taxi o Cabify: 5-8$.",
    "where_to_sleep": [
        {"name": "Centro Histórico", "description": "La experiencia más auténtica pero más transitada. Hostels desde 10$, hoteles boutique desde 40$ (algunos en conventos históricos)."},
        {"name": "La Mariscal (Gringolandia)", "description": "El barrio turístico con los mejores hostels y más oferta de tours. Hostels desde 8$, hoteles desde 30$."},
        {"name": "La Floresta / González Suárez", "description": "El barrio residencial más seguro y con mejor gastronomía. Apartamentos desde 30$/noche."}
    ],
    "what_to_do": [
        {"title": "Centro Histórico colonial", "description": "La Compañía de Jesús (el interior más dorado de América Latina), el convento de San Francisco (el más grande de América del Sur) y la Plaza Grande forman el conjunto histórico más extraordinario de la región. Gratis desde el exterior, 4-6$ los interiores."},
        {"title": "TelefériQo al Pichincha", "description": "El teleférico sube desde 2.950m a 4.100m en 8 minutos, con vistas de Quito y los volcanes. Desde la cima se puede hacer senderismo a 4.600m (8$ el teleférico, aguante a la altitud necesario)."},
        {"title": "Mitad del Mundo e Intiñan", "description": "A 30 km del centro. El Museo Intiñan (10$) tiene el verdadero punto del Ecuador con el experimento del huevo en pie y la dirección del agua en el desagüe. Más científicamente correcto que el monumento oficial."},
        {"title": "Mercado Central y Mercado de San Francisco", "description": "El mercado central del centro histórico tiene el almuerzo más barato y auténtico de Quito: sopa + plato fuerte + jugo por 2,50$. El mercado artesanal de la plaza San Francisco tiene los mejores souvenirs."},
        {"title": "Excursión al Cotopaxi", "description": "El volcán activo más alto del mundo con un glaciar activo, a 90 minutos de Quito. El refugio a 4.800m está accesible con 4x4. Tours desde 35$."},
        {"title": "Barrio La Floresta", "description": "El barrio bohemio con los mejores restaurantes creativos de Quito, galerías y el ambiente más relajado de la ciudad. El parque La Floresta los fines de semana tiene el mejor ambiente local."}
    ],
    "food_and_drink": "La cocina quiteña mezcla influencias andinas con influencias españolas: ceviche de camarones (diferente al peruano, con patacones), locro de papas (sopa de patata andina con queso y aguacate), seco de pollo (estofado de pollo), hornado (cerdo asado entero en horno de barro) y las empanadas de viento. El almuerzo completo en el mercado cuesta 2-3$.",
    "safety": "Quito ha tenido episodios de inseguridad en los últimos años. El Centro Histórico es seguro de día pero requiere más cuidado de noche. La Mariscal: cuidado de madrugada. Usa Cabify o InDriver en lugar de taxis de calle.",
    "visa_info": "Españoles entran sin visado hasta 90 días. Moneda: dólar estadounidense (Ecuador dolarizó en 2000). 1€ ≈ 1,08$.",
    "local_tips": ["La altitud de Quito (2.850m) afecta los primeros días — hidratación y actividad física moderada las primeras 48h", "Cabify funciona bien en Quito — más seguro que taxis de calle", "El almuerzo en el Mercado Central (2,50$) es la mejor comida auténtica y más económica de la ciudad", "El TelefériQo cierra con mal tiempo — llama antes de ir", "El ceviche ecuatoriano (con tomate y ketchup) es completamente diferente al peruano — prueba ambos sin prejuicios"],
    "travel_styles": ["historia", "cultura", "naturaleza", "aventura"],
    "vibes": ["andes", "colonial", "volcanic", "indigenous"],
    "climate": ["subtropical highland", "spring-like year round"],
    "best_months": ["June", "July", "August", "September", "December", "January"],
    "budget_daily_low": 25, "budget_daily_mid": 55, "budget_daily_high": 140, "guide_quality": 8
},
{
    "slug": "san-jose-cr", "name": "San José", "country": "Costa Rica", "continent": "América", "type": "city",
    "coordinates": {"lat": 9.9281, "lng": -84.0907},
    "tagline": "La puerta a los volcanes, el cloud forest y las mejores playas de Centroamérica",
    "intro": "San José no es la razón de visitar Costa Rica — los volcanes, los bosques nubosos y las playas del Pacífico y el Caribe son las razones. Pero San José es el hub inevitable y, bien usado, tiene más de lo que parece: el Mercado Central más completo de Centroamérica, el Teatro Nacional (una de las mejores salas de ópera de América Latina) y los barrios de Barrio Amón y Escalante con cafés de especialidad, galerías y los mejores restaurantes del país.\n\nCosta Rica lleva décadas siendo ejemplo de sostenibilidad y biodiversidad: el 25% del territorio es parque nacional, tiene más especies de aves que toda América del Norte y el 99% de la electricidad es renovable. Desde San José se puede llegar al volcán Arenal (3h), al cloud forest de Monteverde (3h) y a las playas del Pacífico central (2h).\n\nPura vida — el mantra nacional — no es un saludo vacío sino una filosofía real que se nota en el trato local.",
    "when_to_go": "Diciembre-abril: la estación seca en el Pacífico (la favorita de la mayoría). Mayo-noviembre es la temporada verde/húmeda con más lluvia pero menos turistas y precios más bajos. El Caribe (Puerto Viejo, Tortuguero) tiene su propia meteorología — puede estar seco cuando el Pacífico llueve.",
    "how_to_get_there": "Aeropuerto Internacional Juan Santamaría con conexiones de toda América y vuelos directos de Madrid. Bus express al centro (700 colones). Taxi: 8-12$. El aeropuerto está a 20 km del centro.",
    "where_to_sleep": [
        {"name": "Barrio Amón / Otoya", "description": "El barrio histórico con los mejores hoteles boutique en mansiones victorianas (desde 60$). El más agradable de la ciudad."},
        {"name": "Escalante", "description": "El barrio gastronómico más trendy, con los mejores restaurantes y cafés. Apartamentos desde 50$/noche."},
        {"name": "La Sabana / Paseo Colón", "description": "Junto al mayor parque urbano, práctico para moverse. Hoteles desde 45$."}
    ],
    "what_to_do": [
        {"title": "Mercado Central de San José", "description": "El mercado cubierto de 1881 con toda la vida tica concentrada: mariscos frescos, casados completos (el plato nacional), sodas locales, especias, flores y artesanías. El almuerzo aquí cuesta 3-5$."},
        {"title": "Teatro Nacional de Costa Rica", "description": "La sala de ópera del siglo XIX financiada con un impuesto al café es la más bonita de Centroamérica. Visita guiada (10$) o asistir a un espectáculo (8-25$)."},
        {"title": "Parque Nacional Manuel Antonio", "description": "A 3h, el parque más visitado de Costa Rica con la mayor densidad de monos Tití en el mundo y playas de selva. Entrada limitada — reserva online (19$)."},
        {"title": "Volcán Arenal y aguas termales", "description": "A 3h, el volcán más activo de Centroamérica con las mejores aguas termales gratuitas (junto al río) o de pago (resorts). La zona de La Fortuna es base excelente."},
        {"title": "Cloud Forest de Monteverde", "description": "A 3h (carretera de tierra), el bosque nuboso más famoso de América Central con quetzales, puentes colgantes y una biodiversidad sin parangón. Ideal combinarlo con Arenal."},
        {"title": "Puerto Viejo de Talamanca (Caribe)", "description": "A 4h en bus, el Caribe costarricense con playas de Cocles y Punta Uva, la cultura afrocaribeña y el surf de Salsa Brava."}
    ],
    "food_and_drink": "El gallo pinto (arroz y frijoles, el desayuno nacional) con huevos y plátano, el casado (arroz, frijoles, ensalada, proteína y plátano), el ceviche tico y los tamales navideños son la cocina local. Las sodas (restaurantes locales informales) son la mejor opción: casado completo 5-8$. El café de altura costarricense está entre los mejores del mundo.",
    "safety": "San José tiene zonas de alta inseguridad (alrededores del Mercado Central de noche, Barrio Cuba). Los barrios turísticos (Amón, Escalante) son seguros. Usa Uber o Rideshare Bolt en lugar de taxis.",
    "visa_info": "Españoles entran sin visado hasta 90 días. Moneda: colón costarricense (CRC). 1€ ≈ 580 CRC. También se acepta dólar ampliamente.",
    "local_tips": ["San José no es el destino — es el hub. Planifica las salidas a parques desde el primer día", "Uber es más seguro y barato que los taxis de calle en San José", "Las sodas locales tienen la mejor comida por menos dinero — pide el casado del día", "El Mercado Central tiene carteristas — cuida la mochila especialmente en la entrada", "El café costarricense se compra mejor en la cooperativa Coopeatarrazu o en tiendas de productores"],
    "travel_styles": ["naturaleza", "aventura", "wildlife", "sostenibilidad"],
    "vibes": ["pura vida", "tropical", "biodiversity", "gateway"],
    "climate": ["tropical", "rainy season May-November"],
    "best_months": ["December", "January", "February", "March", "April"],
    "budget_daily_low": 40, "budget_daily_mid": 85, "budget_daily_high": 220, "guide_quality": 8
},
{
    "slug": "la-habana-cuba", "name": "La Habana", "country": "Cuba", "continent": "América", "type": "city",
    "coordinates": {"lat": 23.1136, "lng": -82.3666},
    "tagline": "El tiempo suspendido, el son cubano y la arquitectura colonial más espectacular del Caribe",
    "intro": "La Habana es como viajar al pasado y al futuro simultáneamente — la arquitectura colonial española del siglo XVII y XVIII está perfectamente preservada en La Habana Vieja (UNESCO) pero también en ruinas parciales que le dan un romanticismo único. Los coches americanos de los años 50 circulan por las mismas calles donde los jóvenes se conectan a internet con los celulares más nuevos.\n\nEl son cubano, la salsa, el danzón y la trova son omnipresentes — la música sale de cada bar, cada paladar y cada esquina de La Habana. El Malecón al atardecer, el mojito en La Bodeguita del Medio (el bar de Hemingway), el daiquiri en El Floridita y el habano en la Fábrica del Tabaco son los rituales ineludibles.\n\nNOTA: La situación económica de Cuba es severa. La escasez de bienes básicos, los cortes de electricidad y las dificultades para usar tarjetas internacionales son realidad. Viaja con efectivo en euros (se cambia mejor que el dólar) y con expectativas ajustadas.",
    "when_to_go": "Noviembre-abril: la temporada seca con 24-28°C, ideal. Junio-octubre es la temporada de huracanes — riesgo real y alta humedad. Diciembre y enero son los mejores meses combinando clima y oferta cultural.",
    "how_to_get_there": "Aeropuerto Internacional José Martí. Vuelos directos desde Madrid (Iberia), Barcelona y otras ciudades europeas. Los taxis hasta el centro están regulados (~25 CUP en moneda nacional, confirma precio antes). La situación del transporte puede cambiar — verifica antes de viajar.",
    "where_to_sleep": [
        {"name": "La Habana Vieja", "description": "El barrio histórico UNESCO, a pie de todos los atractivos. Casas particulares (B&B cubano) desde 25-40$ la noche. La experiencia más auténtica."},
        {"name": "Vedado", "description": "El barrio residencial más agradable, con los mejores restaurantes privados (paladares). Casas particulares desde 30$, hoteles desde 50$."},
        {"name": "Miramar", "description": "El barrio diplomático y más tranquilo. Casas coloniales desde 35$."}
    ],
    "what_to_do": [
        {"title": "La Habana Vieja — paseo colonial", "description": "Las cuatro plazas históricas (Armas, Vieja, San Francisco, Catedral) y las calles entre ellas forman el conjunto colonial más completo del Caribe. Gratuito pasear, museos desde 1-5$."},
        {"title": "Malecón al atardecer", "description": "El paseo marítimo de 8km es el salón de la ciudad — familias, músicos, pescadores, parejas y turistas convergen aquí al caer el sol. El mejor espectáculo gratuito de La Habana."},
        {"title": "Museo de la Revolución (ex-Palacio Presidencial)", "description": "El palacio presidencial donde Batista gobernó y donde hoy se documenta la revolución cubana desde la perspectiva oficial. El granma (barco de Fidel) en el jardín exterior es icónico."},
        {"title": "Real Fábrica de Tabacos Partagás", "description": "La fábrica de habanos más famosa del mundo con visitas guiadas (10$). Ver a los torcedores enrollar los puros a mano es una artesanía en extinción."},
        {"title": "Son cubano en Casa de la Trova", "description": "Las casas de la trova (La Trova de Santiago está en la capital como El Hurón Azul) tienen los mejores músicos locales. Entrada 5$, las mejores noches son los viernes y sábados."},
        {"title": "Excursión a Trinidad y Valle de los Ingenios", "description": "A 4,5h en coche, Trinidad es la ciudad colonial más bella y mejor conservada de Cuba. El valle de Los Ingenios (UNESCO) tiene las ruinas de las plantaciones de caña del siglo XIX."}
    ],
    "food_and_drink": "La gastronomía cubana estatal es básica — los mejores restaurantes son los paladares (privados): comida cubana criolla con cerdo asado, arroz y frijoles negros, ropa vieja (carne deshilachada) y yuca con mojo. El mojito auténtico lleva ron blanco, lima, azúcar, hierbabuena y agua con gas. Paladar: 15-25$. El ron Havana Club Añejo Especial (local): 5-8$ la botella en tiendas.",
    "safety": "La Habana es relativamente segura para turistas — el delito más común es el timo y la estafa (jineteo), no la violencia. Los jinetes (vendedores, guías no oficiales) pueden ser insistentes pero raramente agresivos. Por la noche, el Malecón y el Centro tienen más actividad — acompañado no hay problema.",
    "visa_info": "Españoles necesitan tarjeta de turismo (25€, compra en el aeropuerto o con la aerolínea). Pasaporte válido. Seguro médico obligatorio (puede incluirlo la aerolínea). Las tarjetas de banco europeas SÍ funcionan en Cuba (diferente a los bancos americanos).",
    "local_tips": ["Las casas particulares son la mejor opción de alojamiento — más auténticas y directamente ayudan a familias cubanas", "Viaja con efectivo en euros — se cambia mejor que dólares y las tarjetas pueden fallar", "El Malecón al atardecer es la mejor experiencia gratuita de Cuba", "Evita cambiar dinero en la calle — usa las CADECA (casas de cambio oficiales)", "El ron cubano se compra en tiendas de Estado mucho más barato que en bares de hotel"],
    "travel_styles": ["cultura", "historia", "música", "arquitectura"],
    "vibes": ["retro", "music", "colonial", "caribbean"],
    "climate": ["tropical"],
    "best_months": ["November", "December", "January", "February", "March"],
    "budget_daily_low": 35, "budget_daily_mid": 75, "budget_daily_high": 180, "guide_quality": 8
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
