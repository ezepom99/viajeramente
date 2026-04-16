import psycopg2
import json

conn = psycopg2.connect("dbname=viajeramente user=tenant")
cur = conn.cursor()

cities = [
# ÁFRICA
{
    "slug": "tunis", "name": "Túnez", "country": "Túnez", "continent": "África", "type": "city",
    "coordinates": {"lat": 36.8065, "lng": 10.1815},
    "tagline": "La medina de oro, Cartago y el Norte de África más accesible del Mediterráneo",
    "intro": "Túnez es la capital de uno de los países más abiertos del Magreb — la medina histórica de Túnez (Patrimonio UNESCO) es un laberinto de zocos, mezquitas y palacios que funciona exactamente igual que en el siglo XIII. La Gran Mezquita de Zitouna con sus 160 columnas de mármol del siglo VII, el barrio de los tintoreros y las puertas monumentales de Bab Bhar son el corazón de la ciudad más auténtica del norte de África.\n\nA 15 km del centro están las ruinas de Cartago, la gran rival de Roma, y a 20 km el pueblo colonial de Sidi Bou Saïd — casas blancas y azules sobre el Mediterráneo en un acantilado — que es la postal más icónica de Túnez.\n\nTúnez tiene una rica historia arqueológica que culmina en el Museo del Bardo: la mayor colección de mosaicos romanos del mundo, incluyendo el mosaico de la batalla de Thapsus más grande jamás encontrado.",
    "when_to_go": "Marzo-mayo y octubre-noviembre: temperaturas perfectas (20-26°C) sin el agobio del verano. El verano (junio-agosto) alcanza 35-40°C en el interior pero la costa tiene brisa agradable. El invierno es suave (12-18°C).",
    "how_to_get_there": "Aeropuerto de Túnez-Cartago con vuelos directos de Madrid, Barcelona y otras ciudades europeas. Taxi al centro en 20 min (6-8 dinares). Ferries desde Génova, Palermo y Civitavecchia.",
    "where_to_sleep": [
        {"name": "Medina histórica", "description": "Alojarse dentro de las murallas en un riad (casa árabe con patio) es la experiencia más auténtica. Desde 30 dinares/noche."},
        {"name": "Avenue Habib Bourguiba", "description": "El centro moderno colonial francés, con los mejores hoteles desde 80 dinares."},
        {"name": "Sidi Bou Saïd", "description": "El pueblo blanco y azul a 20km del centro, con hoteles boutique desde 100 dinares. Para estancias más relajadas."}
    ],
    "what_to_do": [
        {"title": "Medina histórica de Túnez (UNESCO)", "description": "El laberinto medieval con más de 700 monumentos históricos. La Gran Mezquita de Zitouna (900 pilares), la madraza de las Palmeras y los zocos de los perfumistas, tintoreros y libreros."},
        {"title": "Museo del Bardo", "description": "La mayor colección de mosaicos romanos del mundo en un palacio beylical del siglo XIX. Los mosaicos de Virgilio, de Odiseo y de la caza son extraordinarios (11 dinares)."},
        {"title": "Ruinas de Cartago", "description": "A 15 km, las ruinas de la gran ciudad fenicia rival de Roma: las termas de Antonino, el tophet (santuario) y el Museo Nacional de Cartago en la colina de Byrsa (12 dinares)."},
        {"title": "Sidi Bou Saïd", "description": "El pueblo blanco y azul del acantilado, inspiración de Klee y Macke en 1914. Las casas de jazmín y las vistas al Mediterráneo son una visita imprescindible (20 min en TGM tren)."},
        {"title": "Zocos de la medina", "description": "El zoco de los perfumistas (Souk el Attarine), el de los tintoreros (Souk des Teinturiers) con lana teñida colgando y el de los joyeros son los más pintorescos. Regateo obligatorio."},
        {"title": "Anfiteatro de El Djem (excursión)", "description": "A 200 km al sur, el Coliseo africano con capacidad para 35.000 espectadores, mejor conservado que el de Roma. Merece un día completo."}
    ],
    "food_and_drink": "La cocina tunecina es la más especiada del Magreb: el shakshuka (huevos en salsa de tomate y harissa), la brik (hojaldre relleno con huevo frito), el mechouia (ensalada de pimientos y tomates asados), el couscous con cordero y la harissa (pasta de chile) en todas partes. El té de menta con piñones en Sidi Bou Saïd es un ritual obligatorio (1,5-3 dinares). Cena completa 15-25 dinares.",
    "safety": "Túnez ha reforzado enormemente la seguridad turística desde los atentados de 2015. Los sitios turísticos tienen controles de seguridad. El norte del país (Túnez, Hammamet, Djerba) es seguro. Evita las zonas fronterizas con Libia y Argelia.",
    "visa_info": "Españoles entran sin visado hasta 90 días con pasaporte. La tarjeta de turista se rellena a la llegada. Moneda: dinar tunecino (TND). 1€ ≈ 3,30 TND.",
    "local_tips": ["El tren TGM desde el centro hasta Sidi Bou Saïd y Cartago cuesta menos de 1 dinar y es completamente fiable", "El regateo es obligatorio en los zocos — nunca pagues el primer precio", "La harissa tunecina es más picante que cualquier chile europeo — empieza poco a poco", "El té con piñones en la terraza del café de Sidi Bou Saïd con vistas al Mediterráneo es una de las mejores experiencias de viaje del norte de África", "El museo del Bardo está en el extrarradio — toma un taxi o un Bolt"],
    "travel_styles": ["historia", "cultura", "gastronomía", "arqueología"],
    "vibes": ["maghreb", "mediterranean", "ancient", "medina"],
    "climate": ["mediterranean", "hot summers"],
    "best_months": ["March", "April", "May", "October", "November"],
    "budget_daily_low": 30, "budget_daily_mid": 60, "budget_daily_high": 140, "guide_quality": 8
},
{
    "slug": "dakar", "name": "Dakar", "country": "Senegal", "continent": "África", "type": "city",
    "coordinates": {"lat": 14.6928, "lng": -17.4467},
    "tagline": "El África del Atlántico: teranga, música mbalax y la puerta al continente más infraesitmado",
    "intro": "Dakar está en la punta más occidental de África continental, sobre una península que mira al Atlántico como un barco que no puede zarpar. La capital senegalesa tiene una energía y vitalidad que sorprende: el barrio de Plateau con su arquitectura colonial francesa, los mercados de Sandaga y Kermel, el núcleo artístico de Point E y el barrio pescador de Soumbédioune forman una ciudad de capas que se descubre poco a poco.\n\nEl concepto de teranga — la hospitalidad senegalesa — es real. Invitarte a tomar té tres veces (el ritual del ataya) o a compartir un plato de thiéboudienne es una constante que ningún viajero con tiempo de sentarse puede evitar. Senegal es el país más estable del África subsahariana occidental y Dakar es su embajadora más accesible.\n\nLa música mbalax (con Youssou N'Dour como máximo exponente) llena cada bar, terraza y ocasión festiva.",
    "when_to_go": "Noviembre-mayo: la estación seca con temperaturas de 22-30°C y brisas atlánticas. La harmattan (viento seco del Sahara) puede traer polvo en enero-febrero. El verano (junio-octubre) es la estación húmeda con alta humedad aunque temperaturas similares.",
    "how_to_get_there": "Aeropuerto Internacional Blaise Diagne (abierto en 2017, a 47 km del centro). Bus DDD al centro (2.000 CFA) o taxi (15.000-20.000 CFA). Vuelos directos de Air Senegal y Air France desde París, y desde Madrid.",
    "where_to_sleep": [
        {"name": "Plateau", "description": "El centro colonial con los mejores hoteles desde 40$ y acceso a pie al mercado Sandaga y la Grande Mosquée."},
        {"name": "Almadies / Ngor", "description": "El barrio más agradable junto al Atlántico, con los mejores restaurantes y acceso a la Île de Gorée. Desde 55$."},
        {"name": "Point E", "description": "El barrio residencial intelectual y artístico. Apartamentos desde 35$/noche, ambiente más local."}
    ],
    "what_to_do": [
        {"title": "Île de Gorée", "description": "La isla Patrimonio UNESCO a 20 min en ferry (7.500 CFA) fue el mayor centro de comercio de esclavos del Atlántico. La Maison des Esclaves es el memorial más visitado de África occidental. Emocionalmente imprescindible."},
        {"title": "Mercado de Sandaga y Kermel", "description": "Sandaga es el mercado más caótico y auténtico de Dakar: tejidos, especias, artesanías y la vida cotidiana senegalesa. Kermel es el mercado cubierto más organizado con flores y verduras."},
        {"title": "Monument de la Renaissance Africaine", "description": "La estatua más alta de África (49m, más alta que la Estatua de la Libertad) con vistas de Dakar y el Atlántico desde la cima. Controvertido pero impresionante (2.000 CFA)."},
        {"title": "Restaurante y música mbalax en Almadies", "description": "Los bares y restaurantes del barrio de Almadies tienen sesiones de mbalax en vivo los fines de semana — la música senegalesa es un elemento cultural tan central como el thiéboudienne."},
        {"title": "Thiès y el arte de la tapicería (excursión)", "description": "A 70 km, la Manufacture Sénégalaise des Arts Décoratifs produce las mejores tapicerías africanas del continente. Las visitas están disponibles con reserva."},
        {"title": "Lago Rosa (Retba)", "description": "A 35 km, el lago de agua salada con bacterias que lo tiñen de rosa (similar al de Las Maras en Perú) donde se extrae sal artesanalmente. Tours desde 20$."}
    ],
    "food_and_drink": "El thiéboudienne (arroz con pescado y verduras en salsa de tomate) es el plato nacional senegalés y uno de los mejores platos de África. El yassa poulet (pollo marinado con cebolla y limón), el mafé (estofado de cacahuete) y el ceebu yapp (arroz con carne) son igual de imprescindibles. El ataya (té verde con menta muy dulce servido tres veces, cada vez más dulce) es el ritual social central.",
    "safety": "Dakar es relativamente segura pero requiere atención. Los mercados tienen carteristas. Usa taxis acordados por precio o la app Yango (Uber local). Las playas de noche, especialmente Corniche, requieren más precaución.",
    "visa_info": "Españoles entran sin visado hasta 90 días con pasaporte válido. Moneda: franco CFA (XOF). 1€ = 655,957 CFA (tipo fijo con el euro).",
    "local_tips": ["El ritual del ataya (tres rondas de té verde) es un acto de hospitalidad — rechazarlo es descortés", "El franco CFA tiene tipo fijo con el euro (655 CFA = 1€) — fácil de calcular", "Yango funciona como Uber en Dakar — mucho más seguro que taxis de calle para trayectos de noche", "El thiéboudienne está en todas partes pero el mejor es el que te hace una familia senegalesa en casa", "La Île de Gorée es la visita más importante de Dakar — reserva el ferry el día anterior en temporada alta"],
    "travel_styles": ["cultura", "historia", "gastronomía", "música"],
    "vibes": ["west africa", "atlantic", "vibrant", "hospitality"],
    "climate": ["hot semi-arid", "saharan"],
    "best_months": ["November", "December", "January", "February", "March"],
    "budget_daily_low": 25, "budget_daily_mid": 60, "budget_daily_high": 160, "guide_quality": 8
},
{
    "slug": "lagos-nigeria", "name": "Lagos", "country": "Nigeria", "continent": "África", "type": "city",
    "coordinates": {"lat": 6.5244, "lng": 3.3792},
    "tagline": "La megaciudad más vibrante de África: 22 millones de personas y una energía imparable",
    "intro": "Lagos es la ciudad más grande de África y uno de los centros económicos y culturales más importantes del continente. Con más de 22 millones de habitantes, puede ser caótica, ruidosa e intensa — pero también tiene una energía creativa que ninguna otra ciudad africana iguala. La escena musical (afrobeats, afropop, juju), el arte contemporáneo (el barrio de Lekki concentra las mejores galerías del continente), la gastronomía y el emprendimiento tecnológico hacen de Lagos la ciudad más dinámica del África subsahariana.\n\nLa ciudad se extiende sobre una serie de islas y tierras firmes: Lagos Island (el centro histórico colonial), Lekki (el barrio moderno y seguro para turistas), Victoria Island (los restaurantes y vida nocturna) y el Continente donde vive la mayoría de la población real.\n\nLagos no es fácil, pero los viajeros que la abordan con paciencia y un buen guía local vuelven fascinados.",
    "when_to_go": "Noviembre-marzo: la estación seca con temperaturas de 26-32°C y menos humedad. El verano (mayo-septiembre) es la estación lluviosa con aguaceros intensos que empeoran el tráfico (que ya es legendariamente malo).",
    "how_to_get_there": "Aeropuerto Internacional Murtala Muhammed con conexiones de Europa (British Airways, Air France, Ethiopian) y toda África. Taxis del aeropuerto al centro: negociar (5.000-10.000 nairas). Uber funciona en Lagos.",
    "where_to_sleep": [
        {"name": "Victoria Island", "description": "El distrito financiero y de entretenimiento, el más seguro para turistas. Hoteles desde 80$."},
        {"name": "Lekki Phase 1", "description": "El barrio residencial más agradable con buenas opciones de alojamiento desde 60$ y los mejores restaurantes modernos."},
        {"name": "Ikoyi", "description": "El barrio más exclusivo y seguro, tradicional para embajadas y expatriados. Hoteles desde 100$."}
    ],
    "what_to_do": [
        {"title": "Nike Art Gallery", "description": "Cuatro plantas de arte contemporáneo y tradicional nigeriano en la galería más grande de África. El trabajo de tela adire (teñido en reserva) y las esculturas en bronce de Benin son extraordinarios (entrada gratuita)."},
        {"title": "Mercado de Balogun (Lagos Island)", "description": "El mercado más grande de África occidental: tejidos ankara, electrónica, especias, calzado y todo lo imaginable. Una inmersión total en la economía informal de Nigeria."},
        {"title": "Bar Beach y Lekki Beach", "description": "Las playas del Atlántico de Lagos son populares entre los locales los fines de semana. Lekki Conservation Centre tiene un paseo de canopié sobre los árboles."},
        {"title": "Concierto de afrobeats en el New Afrika Shrine", "description": "El santuario del afrobeats fundado por Fela Kuti tiene conciertos cada martes y viernes noche. La música en vivo de Lagos es una de las mejores experiencias culturales de África."},
        {"title": "Terra Kulture Museum", "description": "El museo y teatro que mejor documenta la cultura yoruba y las artes escénicas de Nigeria. Obras de teatro en inglés y yoruba regularmente."},
        {"title": "Eat Lagos food tour", "description": "Los tours de comida por el Lagos Island y el continente muestran la gastronomía nigeriana real: suya (brochetas de carne), egusi soup, amala y ewedu. La mejor inversión de 40$ en Lagos."}
    ],
    "food_and_drink": "La cocina nigeriana yoruba es contundente y rica: jollof rice (el plato nacional de África occidental, siempre en debate cuál es el mejor — el nigeriano gana), egusi soup (sopa de semillas de melón con verduras), suya (brochetas de carne especiada), akara (buñuelos de judías) y el puff puff (rosquillas dulces). Un almuerzo en buka (restaurante local informal): 3-5$.",
    "safety": "Lagos requiere más precaución que otras capitales africanas. Victoria Island y Lekki son los barrios más seguros para turistas. Uber es esencial — los taxis de calle tienen riesgo de timo. No saques el teléfono en la calle. Evita el transporte público (danfos, buses amarillos).",
    "visa_info": "Los españoles necesitan visa de Nigeria. Solicita e-visa online (visa on arrival disponible para algunos países, verificar). Proceso puede ser burocrático — inicia con 4-6 semanas de antelación. Moneda: naira (NGN). 1€ ≈ 1.700 NGN.",
    "local_tips": ["Contrata un guía local desde el primer día — Lagos sin alguien que la conozca es muy dura", "El tráfico de Lagos (go-slow) puede paralizar la ciudad durante horas — planifica con mucho margen", "Uber es la única forma segura de moverse como turista", "El New Afrika Shrine los martes o viernes es la mejor noche de música en vivo de toda África", "El jollof rice nigeriano para probar cuál es el mejor de Lagos es una búsqueda gastronómica en sí misma"],
    "travel_styles": ["cultura", "música", "gastronomía", "arte"],
    "vibes": ["west africa", "megacity", "afrobeats", "hustle"],
    "climate": ["tropical monsoon"],
    "best_months": ["November", "December", "January", "February", "March"],
    "budget_daily_low": 40, "budget_daily_mid": 90, "budget_daily_high": 250, "guide_quality": 8
},
{
    "slug": "dar-es-salaam", "name": "Dar es Salaam", "country": "Tanzania", "continent": "África", "type": "city",
    "coordinates": {"lat": -6.7924, "lng": 39.2083},
    "tagline": "El puerto del paz, puerta al Serengeti, el Kilimanjaro y las playas de Zanzíbar",
    "intro": "Dar es Salaam — 'el puerto de la paz' en árabe — es la mayor ciudad de Tanzania y el hub de la región del África oriental. No tiene los atractivos turísticos icónicos del país (esos están en el Serengeti, el Kilimanjaro y Zanzíbar) pero tiene algo que las ciudades del safari no tienen: la vida urbana africana oriental auténtica, la cocina swahili de la costa y el carácter portuario de una ciudad donde el Índico llega hasta los pies del mercado de Kariakoo.\n\nEl barrio de Oyster Bay tiene los mejores restaurantes y la vida de expatriados y turistas. El centro histórico con el Askari Monument y los edificios coloniales alemanes y británicos cuenta la historia colonial en ladrillo. El mercado de Kariakoo es el mayor mercado cubierto de África oriental.\n\nLa mayoría de viajeros usan Dar como puente hacia Zanzíbar (ferry, 2h) y el safari, pero la ciudad merece al menos una o dos noches propias.",
    "when_to_go": "Junio-octubre (estación seca corta) y diciembre-marzo (estación seca larga): las mejores épocas con temperaturas de 25-32°C. Evita el largo rains (abril-mayo) y el short rains (noviembre). Zanzíbar tiene su mejor clima en junio-octubre.",
    "how_to_get_there": "Aeropuerto Internacional Julius Nyerere con conexiones de Europa (KLM, Ethiopian, Qatar Airways) y toda África. Taxis al centro (25.000-40.000 TZS). Ferry a Zanzíbar desde el terminal del puerto (35-40$ turistas).",
    "where_to_sleep": [
        {"name": "Oyster Bay / Masaki", "description": "El barrio más seguro y agradable para turistas, junto al mar. Hoteles desde 60$, restaurantes excelentes."},
        {"name": "Msasani Peninsula", "description": "La península residencial con los mejores bares y restaurantes. Apartamentos desde 50$/noche."},
        {"name": "Centro / Kariakoo", "description": "El centro histórico, más económico pero ruidoso. Hoteles locales desde 20$."}
    ],
    "what_to_do": [
        {"title": "Ferry y playa en Zanzíbar", "description": "La isla de Zanzíbar (Unguja) con Stone Town (UNESCO), las playas de Nungwi y Kendwa y los arrecifes de coral está a 2h en fast ferry (35-40$). La excursión más obvia y la más recompensada."},
        {"title": "Mercado de Kariakoo", "description": "El mayor mercado cubierto de África oriental: especias, frutas tropicales, telas ankara, artesanías swahili y la mejor comida callejera de la ciudad (mishkaki, samosas, jugos de caña)."},
        {"title": "Makumbusho Village Museum", "description": "El museo de la vida cultural tanzana con 16 casas tradicionales de distintas etnias y danzas folclóricas en vivo los fines de semana. Fuera del centro (12 km), imprescindible."},
        {"title": "Playa de Coco Beach", "description": "La playa más popular de la ciudad, junto al barrio de Oyster Bay. Los fines de semana los locales se reúnen aquí. No apta para nadar pero perfecta para la atmósfera."},
        {"title": "Nightlife de Oyster Bay", "description": "Los bares de Junction Mall y las terrazas de Oyster Bay tienen la mejor vida nocturna de Dar — música bongo flava (hip-hop tanzano), cerveza Safari y mariscos a la brasa."},
        {"title": "Excursión al Parque Nacional Mikumi", "description": "A 280 km (4h en bus o coche), el parque nacional más accesible desde Dar con elefantes, leones y jirafas. Alternativa más económica al Serengeti para un primer safari."}
    ],
    "food_and_drink": "La cocina swahili es una mezcla de árabe, india y africana: mishkaki (brochetas de carne o marisco), chips mayai (tortilla de patatas fritas), pilau (arroz especiado con carne), urojo (sopa de coco con frituras) y el biryani swahili. El mercado de Kariakoo tiene la mejor comida local por menos de 5$. Los restaurantes de mariscos de Oyster Bay: 15-25$.",
    "safety": "Dar es Salaam es moderadamente segura. El centro histórico y Kariakoo de noche requieren atención. Oyster Bay y Masaki son los barrios más seguros. No uses teléfono en la calle en zonas concurridas. Taxis: Uber y Bolt funcionan bien.",
    "visa_info": "Los españoles necesitan visa de Tanzania. Solicita e-visa online antes de viajar (50$, 50$ también a la llegada). El East Africa Tourist Visa (100$) incluye Tanzania, Uganda y Kenya en una sola visa — conveniente si visitas los tres países. Moneda: shilling tanzano (TZS). 1€ ≈ 2.700 TZS.",
    "local_tips": ["El ferry a Zanzíbar reserva online — en temporada alta se llena y los precios suben", "La East Africa Tourist Visa vale la pena si combinas Tanzania con Kenya y Uganda", "Bolt funciona en Dar es Salaam y es más fiable que taxis de calle", "El mercado de Kariakoo está en su mejor momento a primera hora de la mañana (7-10am)", "El bongo flava (música tanzana) es el mejor souvenir cultural de la ciudad — descarga una playlist local"],
    "travel_styles": ["naturaleza", "cultura", "playa", "safari"],
    "vibes": ["east africa", "swahili", "port city", "gateway"],
    "climate": ["tropical", "hot and humid"],
    "best_months": ["June", "July", "August", "September", "December", "January", "February"],
    "budget_daily_low": 30, "budget_daily_mid": 70, "budget_daily_high": 180, "guide_quality": 8
},
{
    "slug": "zanzibar-ciudad", "name": "Zanzíbar (Stone Town)", "country": "Tanzania", "continent": "África", "type": "city",
    "coordinates": {"lat": -6.1630, "lng": 39.1980},
    "tagline": "La ciudad de las especias: aromas de clavo, historia árabe y el océano Índico más turquesa",
    "intro": "Stone Town es el corazón histórico de la isla de Zanzíbar — un laberinto de calles tan estrechas que dos burros no pueden cruzarse, con puertas talladas en madera que son obras de arte por sí solas, mercados de especias que llevan siglos funcionando y una mezcla de culturas árabes, indias, africanas y coloniales europeas que solo tiene sentido en un cruce de rutas de comercio marítimo.\n\nZanzíbar fue durante siglos el mayor centro del comercio de esclavos y especias del Océano Índico, y es Patrimonio UNESCO precisamente por esa complejidad histórica que todavía se lee en cada rincón. Las playas de la isla son independientemente espectaculares: Nungwi al norte tiene las mejores para nadar, Paje al este es la capital del kitesurf y Matemwe al nordeste tiene los arrecifes más tranquilos.\n\nFreddie Mercury nació en Stone Town en 1946 — la casa donde vivió de niño es hoy museo.",
    "when_to_go": "Junio-octubre y diciembre-febrero son la temporada seca con el agua más calma. Los meses de la larga lluvia (abril-mayo) hacen el snorkel y kitesurf imposibles. Junio-agosto tiene los precios más altos pero el mejor clima.",
    "how_to_get_there": "Ferry desde Dar es Salaam (2h, 35-40$ turistas) o vuelo directo (30 min) desde Kilimanjaro o Nairobi. El aeropuerto de Zanzíbar tiene conexiones directas de algunos destinos europeos (Milán, Londres). Dala-dala (furgoneta local) desde el puerto al centro: 500 TZS.",
    "where_to_sleep": [
        {"name": "Stone Town", "description": "Dormir dentro del laberinto histórico es la experiencia más auténtica. Riads y guesthouses desde 40$, hoteles boutique desde 80$."},
        {"name": "Nungwi (norte)", "description": "Las mejores playas para nadar, animadas y con el mejor ambiente nocturno. Hoteles de playa desde 80$."},
        {"name": "Paje (este)", "description": "La capital del kitesurf, con bungalows frente al mar desde 50$ y atmósfera más relajada."}
    ],
    "what_to_do": [
        {"title": "Calles de Stone Town de noche", "description": "El laberinto de Stone Town al anochecer, cuando la luz de los mercados y el olor de los cloves llenan las callejuelas, es la experiencia más única de África oriental. El mercado nocturno Forodhani Gardens es el mejor lugar para cenar (3-8$)."},
        {"title": "Tour de especias", "description": "Los tours por las plantaciones de especias (clavo, vainilla, cardamomo, cúrcuma, pimienta) muestran de dónde viene el aroma que permea toda la isla. 3-4 horas, 10-15$."},
        {"title": "Snorkel en Mnemba Atoll", "description": "El mejor arrecife de coral de Zanzíbar, con tortugas marinas, delfines y una visibilidad de hasta 20m. Tours desde Stone Town: 40-60$."},
        {"title": "Playa de Nungwi al atardecer", "description": "El lado norte de la isla tiene las mejores puestas de sol de Zanzíbar — las playas de arena blanca miran al Índico sin mareas extremas que lo alejen."},
        {"title": "Casa natal de Freddie Mercury", "description": "El frontman de Queen nació aquí en 1946. La casa es hoy restaurante y pequeño museo con memorabilia. Para los fans, una peregrinación."},
        {"title": "Bosque de Jozani y monos Colobus Rojos", "description": "El único bosque primario de Zanzíbar tiene la única colonia de monos Colobus Rojos del mundo, endémicos de la isla. Entrada 10$, guía incluido."}
    ],
    "food_and_drink": "La cocina zanzibarí mezcla árabe, india y swahili: el pilau (arroz especiado con cardamomo, clavo y canela), el biryani de marisco, el urojo (sopa mixta) y el mkate wa kumimina (pan de coco). El mercado nocturno de Forodhani Gardens tiene la mejor opción: langosta fresca a la plancha por 10-15$, brochetas de pulpo y zumo de caña de azúcar por 0,50$.",
    "safety": "Zanzíbar es generalmente segura para turistas. La zona de Stone Town de noche puede tener acoso sexual ocasional a mujeres solas. Las playas requieren atención al oscurecer. Usa ropa respetuosa en Stone Town (es mayoritariamente musulmán).",
    "visa_info": "Zanzíbar es parte de Tanzania — misma visa. E-visa online antes del viaje (50$). El East Africa Tourist Visa cubre Tanzania. Los ciudadanos de Zanzíbar tienen pasaporte tanzano.",
    "local_tips": ["El mercado nocturno de Forodhani Gardens es el mejor valor-precio de toda Zanzíbar — llega a las 18:30 cuando está más fresco", "El tour de especias incluye frutas exóticas que nunca has probado — merece los 10$", "Viste conservadoramente en Stone Town — la isla es mayoritariamente musulmana", "El ferry de noche de Dar a Zanzíbar no es recomendable — viaja de día", "Las medusas son frecuentes en Paje — consulta antes de nadar sin protección"],
    "travel_styles": ["playa", "cultura", "historia", "snorkel"],
    "vibes": ["spice island", "arabic", "indian ocean", "tropical"],
    "climate": ["tropical"],
    "best_months": ["June", "July", "August", "September", "January", "February"],
    "budget_daily_low": 35, "budget_daily_mid": 80, "budget_daily_high": 250, "guide_quality": 8
},
{
    "slug": "kigali", "name": "Kigali", "country": "Ruanda", "continent": "África", "type": "city",
    "coordinates": {"lat": -1.9441, "lng": 30.0619},
    "tagline": "La capital más limpia de África, puerta a los gorilas de montaña y un milagro de reconciliación",
    "intro": "Kigali es la capital más limpia y ordenada de África — literalmente, sin bolsas de plástico (prohibidas en 2008), con calles barridas y una eficiencia administrativa que sorprende. Treinta años después del genocidio de 1994 que mató a 800.000 personas en 100 días, Ruanda es el país africano que mejor demuestra que la reconstrucción post-genocidio es posible.\n\nEl Museo del Genocidio de Kigali es obligatorio — doloroso pero imprescindible para entender el país y el continente. Pero Kigali de 2024 también tiene los mejores restaurantes de café de especialidad de África, barrios de galerías de arte contemporáneo, hoteles boutique de alto nivel y, a 2-3 horas, los gorilas de montaña del Parque Volcanes — el safari más exclusivo y emocionante del continente.\n\nRuanda es seguro, limpio y organizado — las cualidades más insólitas de África y también las que más se agradecen.",
    "when_to_go": "Junio-septiembre y diciembre-febrero son las estaciones secas — perfectas para los gorilas y el trekking. Las temporadas húmedas (marzo-mayo y octubre-noviembre) reducen visibilidad pero los precios bajan y los paisajes son más verdes.",
    "how_to_get_there": "Aeropuerto Internacional de Kigali con conexiones directas de Nairobi, Addis Abeba, Dubai, Bruselas, Londres y otras. RwandAir vuela directamente a Barcelona. Mototaxi (moto-taxi con casco) al centro: 1-2$. Taxis: 5-10$.",
    "where_to_sleep": [
        {"name": "Kiyovu / Downtown", "description": "El centro de la ciudad con los mejores hoteles boutique (desde 70$) y acceso a pie a los atractivos principales."},
        {"name": "Kimihurura", "description": "El barrio diplomático y residencial más agradable. Apartamentos desde 60$/noche."},
        {"name": "Nyamirambo", "description": "El barrio más auténtico y animado, con la mejor comida local y mercados. Guesthouses desde 25$."}
    ],
    "what_to_do": [
        {"title": "Museo del Genocidio de Kigali (Gisozi)", "description": "El memorial donde 250.000 víctimas del genocidio están enterradas y donde la historia de los 100 días de 1994 se documenta con rigor y respeto. Entrada gratuita, guía disponible. Emocionalmente devastador e imprescindible."},
        {"title": "Trekking de gorilas en el Parque Volcanes", "description": "A 2,5h de Kigali, el encuentro de una hora con gorilas de montaña en su hábitat natural es posiblemente la experiencia de safari más intensa del mundo. El permiso cuesta 1.500$ (incluye guías y conservación) — el dinero más justificado de África."},
        {"title": "Kimironko Market", "description": "El mercado cubierto más grande de Kigali: tejidos kitenge, artesanías de madera y cestas de Ruanda (de las más elaboradas de África). Sin regateo agresivo — los precios son más fijos que en otros mercados africanos."},
        {"title": "Inema Art Center", "description": "El centro de arte contemporáneo más importante de África oriental, con artistas residentes, exposiciones y talleres. Una ventana al Ruanda creativo post-genocidio."},
        {"title": "Coffee tour en las cooperativas", "description": "El café de altura ruandés (varietales bourbon lavado) está entre los mejores del mundo. Tours de procesado en cooperativas a las afueras de Kigali (15-25$) con cata incluida."},
        {"title": "Kandt House Museum", "description": "La residencia del primer gobernador colonial alemán de Ruanda, convertida en museo de la historia natural y cultural del país. El único museo de historia natural de Kigali."}
    ],
    "food_and_drink": "La cocina ruandesa mezcla ingredientes africanos con técnicas coloniales: isombe (hojas de yuca con berenjenas), ibirayi (patatas fritas con frijoles), brochetas de cabra (nyama choma) y el ubwiru (cerveza de plátano fermentada). La escena de cafés de especialidad de Kigali (Question Coffee, Bourbon Coffee) es la mejor de África. Cena local 5-10$.",
    "safety": "Kigali es una de las ciudades más seguras de África — la policía y la seguridad son muy visibles y efectivas. Prácticamente sin delincuencia para turistas. Las mototaxis tienen licencia y casco obligatorio.",
    "visa_info": "Los españoles pueden obtener e-visa online (50$, 30 días) o la East Africa Tourist Visa (100$) que incluye Kenya, Uganda y Tanzania. A la llegada también disponible. Moneda: franco ruandés (RWF). 1€ ≈ 1.200 RWF.",
    "local_tips": ["El permiso de gorilas (1.500$) hay que reservarlo con meses de antelación — hay cupos muy limitados por grupo de gorillas", "Kigali es la más limpia de África — el 'Umuganda' (día de limpieza comunitaria el último sábado del mes) explica parcialmente por qué", "Los cafés de especialidad de Kigali sirven algunos de los mejores cafés de origen del mundo por 2-3$", "Las mototaxis son el transporte más rápido y tienen helmets obligatorios — úsalas sin miedo", "La prohibición de bolsas de plástico es total — lleva bolsas reutilizables"],
    "travel_styles": ["historia", "naturaleza", "cultura", "safari"],
    "vibes": ["east africa", "genocide memorial", "gorillas", "clean"],
    "climate": ["tropical highland", "mild year-round"],
    "best_months": ["June", "July", "August", "September", "December", "January", "February"],
    "budget_daily_low": 35, "budget_daily_mid": 80, "budget_daily_high": 250, "guide_quality": 8
},
{
    "slug": "kampala", "name": "Kampala", "country": "Uganda", "continent": "África", "type": "city",
    "coordinates": {"lat": 0.3476, "lng": 32.5825},
    "tagline": "La ciudad de las siete colinas, puerta a los gorilas y a la fuente del Nilo",
    "intro": "Kampala tiene exactamente la energía que la mayoría asocia con el África profunda y real: mercados abarrotados, matatus (minibuses) que van al límite de su capacidad, comida callejera de rollex (huevo con chapati enrollado) y una hospitalidad ugandesa genuina que hace difícil estar solo más de cinco minutos. Construida sobre siete colinas junto al lago Victoria, la ciudad tiene una topografía dramática que se disfruta mejor desde la Colina del Parlamento al atardecer.\n\nUganda es el país con más gorilas de montaña del mundo (más de la mitad de la población mundial) y con los mejores chimpancés. Pero Kampala tiene también sus propias atracciones: los mercados de Owino y Nakasero, el Lubiri (Palacio del Rey Buganda), la mezquita más grande de África Subsahariana y la fuente del Nilo a 80 km en Jinja.\n\nLa comida ugandesa — especialmente el rolex callejero — es probablemente el mejor street food de África oriental.",
    "when_to_go": "Junio-agosto y diciembre-febrero son las estaciones más secas. Uganda es relativamente verde todo el año gracias a las lluvias distribuidas — incluso en la 'estación seca' puede llover. Las temporadas húmedas (marzo-mayo, septiembre-noviembre) no impiden los safaris pero pueden complicar algunos caminos.",
    "how_to_get_there": "Aeropuerto Internacional de Entebbe (40 km del centro). Taxis al centro: 60.000-80.000 UGX. Matatu económico desde Entebbe a Kampala (3.000 UGX). Entebbe tiene buenas conexiones con Europa vía Nairobi, Addis Abeba y Dubái.",
    "where_to_sleep": [
        {"name": "Kololo", "description": "El barrio diplomático más seguro y agradable, con buenos restaurantes y hoteles boutique desde 60$."},
        {"name": "Ntinda", "description": "El barrio más animado y económico con la mejor comida local. Guesthouses desde 20$, apartamentos desde 35$."},
        {"name": "Nakasero", "description": "Junto al mercado principal, el más céntrico. Hoteles desde 40$. Mucho tráfico durante el día."}
    ],
    "what_to_do": [
        {"title": "Mercado de Owino (St. Balikuddembe)", "description": "El mercado más grande de África oriental: 60.000 comerciantes en más de 5 hectáreas. Telas, electrónica, ropa de segunda mano occidental y todo lo imaginable. Intenso e imprescindible."},
        {"title": "Fuente del Nilo en Jinja", "description": "A 80 km, el punto donde el Nilo Blanco nace del lago Victoria es accesible en kayak o barca de remos. El mejor rafting de aguas bravas de África también está en el Nilo de Jinja."},
        {"title": "Lubiri — Palacio del Rey Buganda", "description": "El palacio del rey Mutesa II, líder del reino precolonial más importante de Uganda. Las tumbas de los reyes (Kasubi Tombs, UNESCO) están a 3 km."},
        {"title": "Mezquita Nacional de Uganda (Old Kampala)", "description": "La mezquita más grande del África Subsahariana, construida con fondos libios, en la colina más alta de Kampala. Las vistas de la ciudad desde el minarete son las mejores disponibles."},
        {"title": "Rafting en el Nilo / Tracking gorilas / Chimpancés", "description": "Uganda concentra los mejores safaris de primates: gorilas en Bwindi (700$, hay que reservar con meses), chimpancés en Kibale (150$) y rafting en el Nilo en Jinja (120$)."},
        {"title": "Mercado de Nakasero (comida y artesanías)", "description": "El mercado más organizado de Kampala, con productos frescos del lago Victoria y artesanías ugandesas. Los peces viktoria frescas (Nile perch) son la mejor compra gastronómica."}
    ],
    "food_and_drink": "Uganda tiene el mejor street food de África oriental: el rolex (huevo revuelto con cebolla y tomate enrollado en chapati) es probablemente el mejor bocado callejero del continente por 1$. El matoke (plátano verde cocido al vapor) con stew de cacahuete, el posho (ugali de maíz) y el muchomo (brochetas de cerdo a la brasa) son los platos de referencia.",
    "safety": "Kampala es moderadamente segura. El centro (Nakasero, Owino) requiere atención con los bolsillos. De noche, Kololo y los restaurantes de Bugolobi son seguros. Evita caminar solo de madrugada. Usa boda-bodas (mototaxis) con confianza de día.",
    "visa_info": "Los españoles necesitan visa de Uganda. E-visa online (50$, 30 días) o East Africa Tourist Visa (100$ con Kenya y Tanzania). Moneda: shilling ugandés (UGX). 1€ ≈ 4.000 UGX.",
    "local_tips": ["El rolex ugandés (1$) es el mejor bocadillo de África oriental — pruébalo en el primer día", "Los permisos de gorilas de Bwindi se reservan con 3-6 meses de antelación — planifica con tiempo", "Las boda-bodas (mototaxis) son la forma más rápida de moverse en Kampala — negocia precio y lleva casco", "El lago Victoria pez Nile perch cocinado en el Puerto de Entebbe es el mejor pescado de agua dulce de África", "Combina Kampala con Jinja (2 noches) para el Nilo y con Bwindi (3 noches) para los gorilas"],
    "travel_styles": ["naturaleza", "cultura", "safari", "aventura"],
    "vibes": ["east africa", "gorillas", "nile", "authentic"],
    "climate": ["tropical highland", "rainy seasons"],
    "best_months": ["June", "July", "August", "December", "January", "February"],
    "budget_daily_low": 25, "budget_daily_mid": 60, "budget_daily_high": 180, "guide_quality": 8
},
# OCEANÍA
{
    "slug": "wellington", "name": "Wellington", "country": "Nueva Zelanda", "continent": "Oceanía", "type": "city",
    "coordinates": {"lat": -41.2865, "lng": 174.7762},
    "tagline": "La capital más ventosa del mundo: café de especialidad, Te Papa y la puerta a los fiordos",
    "intro": "Wellington es la capital más compacta y agradable de Oceanía — se puede recorrer a pie en un día y tiene una concentración de cafés de especialidad, restaurantes y galerías por habitante que avergüenza a ciudades tres veces su tamaño. La bahía de Wellington y los barrios de colores sobre las colinas tienen un carácter único en el Pacífico.\n\nEl Te Papa Tongarewa es el mejor museo de Nueva Zelanda — la historia maorí, la geología volcánica y la fauna del Pacífico están narradas de forma que ningun otro museo de la región iguala. El barrio de Te Aro tiene el mejor café de especialidad del hemisferio sur (sin exagerar) y los mejores restaurantes del país según los locales.\n\nWellington es también la base del ferry a la Isla Sur y la puerta a los fiordos, Kaikōura (ballenas y delfines) y los glaciares de la costa oeste.",
    "when_to_go": "Diciembre-marzo es el verano del hemisferio sur: temperaturas de 18-24°C, días largos y el ambiente más animado. Wellington vive uno de los climas más variables del mundo — 'si no te gusta el tiempo, espera 10 minutos' es su lema. El invierno (junio-agosto) es frío y ventoso (8-14°C) pero funcional.",
    "how_to_get_there": "Aeropuerto Internacional de Wellington con conexiones de Australia, las islas del Pacífico y vuelos internacionales vía Auckland o Sydney. Bus al centro (7 NZD). Ferry al Sur (Interislander/Bluebridge, 3h, desde 50 NZD).",
    "where_to_sleep": [
        {"name": "Te Aro", "description": "El corazón del barrio creativo, con los mejores cafés y restaurantes. Hostels desde 25 NZD, hoteles boutique desde 100 NZD."},
        {"name": "Thorndon", "description": "El barrio histórico junto al Parlamento. Hoteles desde 90 NZD, más tranquilo."},
        {"name": "Newtown", "description": "El barrio multicultural más económico, a 15 min del centro. Apartamentos desde 70 NZD/noche."}
    ],
    "what_to_do": [
        {"title": "Te Papa Tongarewa (Museo de Nueva Zelanda)", "description": "El mejor museo del país: historia maorí con su cultura material, las colecciones de fauna neozelandesa (kiwi, moa, weta gigante) y las exposiciones geológicas. Gratuito, 6 plantas."},
        {"title": "Cable Car a Kelburn y jardines botánicos", "description": "El funicular histórico (9 NZD ida y vuelta) sube desde Lambton Quay a Kelburn con las mejores vistas de Wellington y el puerto. Los jardines botánicos son gratuitos."},
        {"title": "Barrio de Te Aro y cafés de especialidad", "description": "Wellington tiene la mayor concentración de cafés de especialidad de Oceanía. Flight Coffee Hangar, Fidel's y Havana son los míticos. El flat white neozelandés es aquí donde se inventó."},
        {"title": "Zealandia Eco-Sanctuary", "description": "La reserva natural dentro de la ciudad donde se reintrodujeron tuataras, kiwis y petrels de antifaz. Visita nocturna (100 NZD) para ver kiwis en libertad — una experiencia extraordinaria."},
        {"title": "Ferry a la Isla Sur (Picton/Marlborough)", "description": "El ferry de 3h a través del estrecho de Cook es uno de los viajes en barco más bonitos del mundo. Picton es la puerta a la Marlborough Sounds y la Ruta de la Reina Charlotte."},
        {"title": "Wellington Writers Walk y esculturas costeras", "description": "El paseo marítimo de la bahía tiene esculturas con citas de los mejores escritores neozelandeses. El tramo desde Te Papa hasta el barrio de Chaffers Marina es el más bonito."}
    ],
    "food_and_drink": "Wellington tiene la mejor escena culinaria de Nueva Zelanda — el lamb (cordero de Canterbury), el verde mussel (mejillón verde de Marlborough), el manuka honey y los dairy products de Southland son los mejores ingredientes del país. Los mercados de productores del sábado en Capital E o Harbourside Market tienen lo mejor de la temporada. Café flat white: 4-5 NZD.",
    "safety": "Wellington es extremadamente segura. Sin precauciones especiales para turistas.",
    "visa_info": "Españoles necesitan NZeTA (Electronic Travel Authority, 23 NZD, solicitar online) para entrar a Nueva Zelanda. El IVL (International Visitor Conservation and Tourism Levy, 35 NZD) se paga junto al NZeTA. Moneda: dólar neozelandés (NZD). 1€ ≈ 1,75 NZD.",
    "local_tips": ["El flat white neozelandés es el mejor café del mundo (junto al australiano) — prueba el de Wellington para empezar", "El NZeTA hay que tramitarlo online antes de viajar — no es visa en el sentido tradicional pero es obligatorio", "Zealandia de noche (visita guiada) para ver kiwis silvestres es una experiencia que no existe igual en ningún otro lugar", "El ferry a la Isla Sur es uno de los viajes más bonitos de Oceanía — reserva con antelación", "Wellington se llama 'Windy Wellington' por razón — lleva ropa de abrigo aunque sea verano"],
    "travel_styles": ["cultura", "naturaleza", "café", "outdoor"],
    "vibes": ["pacific", "kiwi", "windy", "creative"],
    "climate": ["oceanic", "windy"],
    "best_months": ["December", "January", "February", "March"],
    "budget_daily_low": 75, "budget_daily_mid": 150, "budget_daily_high": 340, "guide_quality": 8
},
{
    "slug": "brisbane", "name": "Brisbane", "country": "Australia", "continent": "Oceanía", "type": "city",
    "coordinates": {"lat": -27.4698, "lng": 153.0251},
    "tagline": "El sol más generoso de Australia, la Great Barrier Reef al norte y un barrio creativo sin complejos",
    "intro": "Brisbane ha pasado de ser la capital australiana menos visitada a convertirse en una de las más interesantes. La reconversión del South Bank (antigua Exposición Universal de 1988) en un parque fluvial con playa artificial, el barrio de Fortitude Valley con la mejor escena nocturna del país, el mercado de Jan Powers y la proximidad a la Gold Coast y Sunshine Coast la hacen una base perfecta para el sur de Queensland.\n\nBreda tiene un carácter más relajado que Sydney y Melbourne — la luz subtropical es diferente, los ciclorricarros en el puente de Story Bridge son una constante y el grano de café tiene otra calidad cuando lo tuestan locales de West End. La sede de los Juegos Olímpicos de 2032 está en proceso de transformación urbana acelerada.\n\nDesde Brisbane, la Great Barrier Reef accesible (Whitsundays, Port Douglas) está a 2h en avión y los koalas del Lone Pine Koala Sanctuary a 30 minutos.",
    "when_to_go": "Mayo-octubre: el invierno subtropical de Brisbane es el mejor clima de Australia (20-25°C, seco y soleado). El verano (noviembre-marzo) es caluroso y húmedo (28-35°C) con tormentas eléctricas intensas pero impresionantes.",
    "how_to_get_there": "Aeropuerto Internacional de Brisbane con conexiones globales. Airtrain al centro en 22 min (20 AUD). Cruceros internacionales en el puerto de Brisbane.",
    "where_to_sleep": [
        {"name": "South Bank / West End", "description": "El barrio cultural junto al río, con el mejor parque y acceso a pie a los atractivos. Hostels desde 30 AUD, hoteles boutique desde 120 AUD."},
        {"name": "Fortitude Valley", "description": "El barrio nocturno más animado de Queensland, con bares, galerías y el mejor ambiente. Apartamentos desde 90 AUD/noche."},
        {"name": "CBD (Centro)", "description": "El corazón financiero con los mejores hoteles desde 100 AUD y acceso a todo."}
    ],
    "what_to_do": [
        {"title": "South Bank Parklands y Streets Beach", "description": "El parque fluvial con la única playa artificial de agua templada de una capital australiana. Gratuito, perfecto para un domingo con los locales."},
        {"title": "Lone Pine Koala Sanctuary", "description": "El santuario de koalas más grande del mundo, con más de 130 ejemplares, canguros y fauna autóctona. Se puede abrazar un koala para foto (40 AUD la foto). Entrada: 45 AUD."},
        {"title": "Story Bridge Climb", "description": "Escalar los arcos del puente más icónico de Brisbane con vistas de la ciudad, el río y hasta las montañas Glasshouse al fondo. Desde 120 AUD."},
        {"title": "South Bank Gallery of Modern Art (QAGOMA)", "description": "Una de las mejores galerías de arte moderno de Australia, con la mayor colección de arte asiático-pacífico del mundo. Gratuita."},
        {"title": "Excursión a Noosa o Gold Coast", "description": "La Gold Coast (75 km, 1h) tiene el mejor surf de Australia. Noosa Heads (140 km, 2h) tiene un parque nacional con surf tranquilo, koalas y el barrio Hastings Street. Ambas son perfectas para una noche."},
        {"title": "Mercado de Farmer's Market en Jan Powers", "description": "El mercado de productores más auténtico de Brisbane: mango de Queensland, queso local, café de especialidad y macadamia fresca. Sábados por la mañana en Powerhouse."}
    ],
    "food_and_drink": "Brisbane tiene una escena gastronómica que la pandemia transformó — los mejores restaurantes de West End y Fortitude Valley compiten con Sydney. El mud crab (cangrejo de pantano), las ostras de Coffin Bay, el beef de Queensland (el mejor del país) y las frutas tropicales (mango, papaya) son los ingredientes locales. Los mercados de granjeros y el barrio de West End concentran la mejor oferta asequible.",
    "safety": "Brisbane es muy segura. Fortitude Valley de noche puede ser ruidosa con bares — precaución estándar de ciudad. Calor extremo en verano requiere protección solar muy alta.",
    "visa_info": "Españoles necesitan ETA (Electronic Travel Authority, 20 AUD, solicitar online antes del viaje). Estancias hasta 90 días. Moneda: dólar australiano (AUD). 1€ ≈ 1,65 AUD.",
    "local_tips": ["El Airtrain del aeropuerto es caro (20 AUD) pero puntual — las alternativas en autobús son más lentas", "El ETA se tramita online antes de viajar — no necesitas visa tradicional", "La Opal Card (en NSW) / Go Card (en Queensland) es la tarjeta de transporte recargable imprescindible", "El Lone Pine Koala Sanctuary es la mejor forma de ver koalas sin depender de la suerte en el campo", "La Gold Coast y Noosa son las playas más accesibles — decide según si prefieres surf activo (GC) o tranquilo (Noosa)"],
    "travel_styles": ["naturaleza", "playa", "outdoor", "cultura"],
    "vibes": ["subtropical", "outdoors", "coastal", "laid-back"],
    "climate": ["humid subtropical", "hot summers"],
    "best_months": ["May", "June", "July", "August", "September", "October"],
    "budget_daily_low": 80, "budget_daily_mid": 160, "budget_daily_high": 380, "guide_quality": 8
},
{
    "slug": "perth", "name": "Perth", "country": "Australia", "continent": "Oceanía", "type": "city",
    "coordinates": {"lat": -31.9505, "lng": 115.8605},
    "tagline": "La ciudad más aislada del mundo: playas perfectas, vino de Margaret River y la naturaleza más extrema de Australia",
    "intro": "Perth tiene el honor dudoso de ser la ciudad más aislada del mundo — la ciudad de más de un millón de habitantes más cercana está a 2.700 km. Esa lejanía ha forjado un carácter propio: más relajada que Sydney, con mejores playas que Melbourne y un sol que promedia 300 días al año. Los surfistas de Cottesloe Beach, los pescadores de Fremantle y los locales en el Kings Park cualquier domingo son la imagen real de Perth.\n\nLo que pocos esperan es la calidad de vida: las playas de Cottesloe, City Beach y Scarborough son de las mejores de Australia sin la masificación del este. El puerto de Fremantle (a 30 min en tren) tiene los mercados más auténticos de Australia occidental, la cervecería artesanal Little Creatures y una historia carcelaria victoriana fascinante.\n\nMargaret River, a 3h al sur, tiene el mejor vino de Australia occidental (cabernet sauvignon y chardonnay de clase mundial) y algunas de las mejores olas de surf del hemisferio sur.",
    "when_to_go": "Septiembre-noviembre: el mejor período — temperatura perfecta (20-26°C), flores salvajes (wildflowers) y los pingüinos de la isla Penguin (Little Penguins) en Fremantle. Diciembre-febrero es caluroso (32-40°C). El invierno (junio-agosto) es suave (12-18°C) y el ideal para Margaret River.",
    "how_to_get_there": "Aeropuerto Internacional de Perth con conexiones globales (más desde Singapur, Dubai y Doha). Tren al centro en 20 min (3,70 AUD). Perth está en una zona horaria diferente al este de Australia.",
    "where_to_sleep": [
        {"name": "CBD / Northbridge", "description": "El centro con los mejores hostels (desde 28 AUD) y la vida nocturna. Hoteles desde 100 AUD."},
        {"name": "Fremantle", "description": "El puerto histórico más auténtico, a 30 min en tren. Guesthouses desde 60 AUD, el ambiente más relajado."},
        {"name": "Cottesloe / Claremont", "description": "Los barrios de playa más elegantes, con los mejores restaurantes de marisco. Hoteles desde 130 AUD."}
    ],
    "what_to_do": [
        {"title": "Playa de Cottesloe", "description": "La playa más elegante de Perth, con el Cottesloe Beach Hotel y vistas de las puestas de sol sobre el Índico (las mejores de Australia). El snorkel en las rocas es gratuito."},
        {"title": "Fremantle Markets y Puerto", "description": "Los mercados cubiertos de 1897 tienen los mejores productores de Australia occidental. La Little Creatures Brewery junto al puerto hace una de las mejores cervezas artesanales del país."},
        {"title": "Kings Park y Jardín Botánico", "description": "El parque en la colina sobre el río Swan con las mejores vistas de la ciudad. Las wildflowers en primavera (sept-oct) son un espectáculo único. Gratuito."},
        {"title": "Isla Rottnest y los quokkas", "description": "A 30 min en ferry, la isla reserva de naturaleza tiene las playas más bonitas de Australia occidental y los quokkas — los animales más sonrientes del mundo (no se pueden tocar). Ferry desde 65 AUD."},
        {"title": "Margaret River (excursión de 2 días)", "description": "A 3h, la región vinícola con las mejores olas de surf del hemisferio sur. Wineries de clase mundial (Vasse Felix, Leeuwin Estate), queso artesanal y cuevas de caliza."},
        {"title": "Pinnacles Desert (excursión de día)", "description": "A 250 km al norte, el desierto de piedras calcáreas en forma de agujas en medio de la arena es uno de los paisajes más extraordinarios de Australia. Tour de día desde 90 AUD."}
    ],
    "food_and_drink": "Los mariscos de Australia occidental son los mejores del país: langostas de roca (rock lobster), ostras de Albany, gambas de Shark Bay y el barramundi a la plancha. El mercado de Fremantle tiene la mejor selección. La escena de cafés (Perth tiene el flat white perfecto de la costa oeste) y el vino de Margaret River son el mejor argumento gastronómico. Cena de marisco: 35-60 AUD.",
    "safety": "Perth es muy segura. Northbridge de noche puede ser ruidoso con bares. Cottesloe y Fremantle son tranquilas. El sol es peligroso — SPF 50+ obligatorio.",
    "visa_info": "Españoles necesitan ETA (Electronic Travel Authority, 20 AUD, online antes del viaje). Estancias hasta 90 días. Moneda: dólar australiano (AUD).",
    "local_tips": ["La isla Rottnest en kayak o bicicleta (alquiler 30 AUD/día) es la mejor forma de explorar las calas", "Las wildflowers de agosto-octubre hacen que todo el suroeste de Australia florezca — un espectáculo sin igual", "El ferry a Rottnest reserva online en temporada alta (sept-feb) — se llena los fines de semana", "El flat white de Perth tiene la reputación de ser el mejor de Australia occidental — prueba en el barrio de Subiaco", "Perth está 2h detrás del este de Australia (AWST) — ten cuidado con las conexiones de vuelo"],
    "travel_styles": ["playa", "naturaleza", "vino", "outdoor"],
    "vibes": ["isolated", "sunny", "beach", "indian ocean"],
    "climate": ["mediterranean"],
    "best_months": ["September", "October", "November", "March", "April"],
    "budget_daily_low": 80, "budget_daily_mid": 160, "budget_daily_high": 380, "guide_quality": 8
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
