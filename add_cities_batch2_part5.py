import psycopg2
import json

conn = psycopg2.connect("dbname=viajeramente user=tenant")
cur = conn.cursor()

cities = [
# More Americas
{
    "slug": "asuncion", "name": "Asunción", "country": "Paraguay", "continent": "América", "type": "city",
    "coordinates": {"lat": -25.2867, "lng": -57.6470},
    "tagline": "La capital más olvidada de Sudamérica y la más auténtica de la cuenca del Plata",
    "intro": "Asunción es la capital de uno de los países menos visitados de Sudamérica y esa invisibilidad le ha permitido conservar una autenticidad que Argentina y Brasil perdieron hace décadas. El barrio histórico de La Encarnación con sus edificios coloniales en distintos estados de conservación (desde restaurados hasta ruinosos) tiene el encanto irregular de una ciudad que nunca intentó ser turística.\n\nParaguay es el único país bilingüe de América del Sur donde dos idiomas (español y guaraní) tienen igual estatus oficial — y en Asunción se escucha el jopará (mezcla de ambos) en cada conversación. El tereré (mate frío con hierbas medicinales) es el ritual social por excelencia.\n\nLos precios de Paraguay son de los más bajos de Sudamérica y la hospitalidad paraguaya con los pocos turistas que llegan es genuinamente entusiasta.",
    "when_to_go": "Mayo-septiembre: el invierno austral suave (15-24°C) es la mejor época. El verano (dic-feb) es caluroso y húmedo (34°C+). La Semana Santa tiene las tradiciones más preservadas del continente.",
    "how_to_get_there": "Aeropuerto Internacional Silvio Pettirossi con conexiones de Buenos Aires, São Paulo, Lima y Santiago. Bus al centro (5.000 guaraníes). Buses internacionales de larga distancia desde Buenos Aires (18h), Montevideo y São Paulo.",
    "where_to_sleep": [
        {"name": "Centro Histórico", "description": "El núcleo colonial con los mejores hoteles boutique (desde 40$) y acceso a pie a todo."},
        {"name": "Villa Morra", "description": "El barrio más moderno y seguro con buenos restaurantes. Apartamentos desde 35$/noche."},
        {"name": "Trinidad", "description": "Barrio residencial tranquilo con los mejores precios. Guesthouses desde 20$."}
    ],
    "what_to_do": [
        {"title": "Barrio Histórico y Palacio de los López", "description": "El palacio presidencial del siglo XIX en estilo renacentista italiano frente a la bahía del río Paraguay. Los jardines son accesibles. El casco histórico alrededor mezcla colonial y republicano."},
        {"title": "Museo del Barro", "description": "La mejor colección de arte indígena guaraní del mundo, cerámica precolombina y arte popular paraguayo contemporáneo. Una de las colecciones más subestimadas de Sudamérica."},
        {"title": "Mercado 4 y Mercado Pettirossi", "description": "Los dos mercados más auténticos de Asunción donde los guaraníes y los brasileños y argentinos vienen a comprar electrónica y ropa. El caos y el regateo son parte de la experiencia."},
        {"title": "Costanera del río Paraguay al atardecer", "description": "El paseo a orillas del Río Paraguay al caer el sol es el momento más agradable de Asunción — botes, pescadores y el skyline modesto de la capital con el sol naranja."},
        {"title": "Excursión a las Ruinas Jesuitas de Trinidad", "description": "A 260 km, las ruinas de la misión jesuita del siglo XVIII (UNESCO) son las más completas de Sudamérica — más espectaculares que las argentinas de San Ignacio."},
        {"title": "Tereré con familia paraguaya", "description": "El mate frío con hierbas medicinales servido en rondas es la experiencia social más auténtica de Paraguay — más frecuente que en Argentina y con su propio ritual."}
    ],
    "food_and_drink": "La cocina paraguaya tiene identidad guaraní: sopa paraguaya (pastel de harina de maíz con queso y leche, NO es sopa líquida), chipa (rosquilla de almidón de mandioca con queso), bori-bori (sopa de bolas de maíz y queso) y el asado paraguayo (carne a la brasa con mandioca). Los precios son los más bajos de Sudamérica. Cena completa: 5-10$.",
    "safety": "Asunción tiene zonas de diferente seguridad. El centro histórico y Villa Morra son seguros. Evita el barrio de El Bañado y zonas al este del centro de noche. Usa taxis con contador.",
    "visa_info": "Españoles entran sin visado hasta 90 días. Moneda: guaraní (PYG). 1€ ≈ 7.800 PYG.",
    "local_tips": ["El tereré se toma con la mano derecha y se devuelve sin decir gracias hasta que quieras parar (igual que el mate)", "La sopa paraguaya NO es sopa líquida — es un pastel de maíz. Si la pides esperando algo líquido te vas a sorprender", "Paraguay tiene los mejores precios de electrónica de Sudamérica — el Mercado 4 es famoso en toda la región", "Las ruinas jesuitas de Trinidad son las mejor conservadas del continente — merece el desvío", "El guaraní se mezcla con el español en el jopará — aprende dos palabras en guaraní y los locales te adoptarán"],
    "travel_styles": ["cultura", "historia", "budget", "autenticidad"],
    "vibes": ["south america", "overlooked", "guarani", "authentic"],
    "climate": ["humid subtropical"],
    "best_months": ["May", "June", "July", "August", "September"],
    "budget_daily_low": 20, "budget_daily_mid": 45, "budget_daily_high": 110, "guide_quality": 8
},
{
    "slug": "la-paz", "name": "La Paz", "country": "Bolivia", "continent": "América", "type": "city",
    "coordinates": {"lat": -16.5000, "lng": -68.1500},
    "tagline": "La capital más alta del mundo, el teleférico urbano más bonito y la luna a tocar con la mano",
    "intro": "La Paz es la capital ejecutiva y de facto de Bolivia, construida en un cañón a 3.640m de altitud rodeada por el altiplano y con el nevado de Illimani (6.438m) como telón de fondo permanente. La ciudad en sí es un espectáculo topográfico: las clases medias viven en el fondo del cañón y los barrios más pobres (como El Alto, a 4.100m) cuelgan de las paredes del cañón como nidos de golondrina.\n\nEl sistema de teleféricos urbanos (Mi Teleférico) con 10 líneas es la solución de transporte más original del mundo — cruzar La Paz de un barrio a otro es un espectáculo de vistas por sí mismo. El Mercado de las Brujas vende ingredientes para rituales andinos junto a puestos de comida callejera, y la Calle Sagárnaga tiene la mayor concentración de artesanía andina del continente.\n\nSalar de Uyuni (el espejo más grande del mundo) está a 10h en bus al sur.",
    "when_to_go": "Mayo-octubre: la estación seca del altiplano con días soleados y noches frías. El verano (noviembre-abril) trae lluvias fuertes pero el Salar de Uyuni queda cubierto de agua, creando el efecto espejo más perfecto del año (mejor diciembre-marzo).",
    "how_to_get_there": "Aeropuerto Internacional de El Alto (4.061m, el aeropuerto más alto del mundo accesible comercialmente). Taxi al centro: 10-15 BOB. Buses internacionales desde Lima (20h), Buenos Aires (36h), Santiago (24h).",
    "where_to_sleep": [
        {"name": "Sopocachi", "description": "El barrio más agradable y con los mejores restaurantes. Hostels desde 8$, apartamentos desde 20$/noche."},
        {"name": "Miraflores", "description": "Barrio tranquilo y bien situado. Hoteles boutique desde 35$."},
        {"name": "Zona Central (calle Sagárnaga)", "description": "El corazón turístico con la artesanía. Hostels desde 6$, ambiente animado."}
    ],
    "what_to_do": [
        {"title": "Mi Teleférico — tour por las líneas", "description": "El sistema de teleféricos urbanos con 10 líneas y 30 estaciones es la forma más espectacular de ver La Paz. El billete de 3 BOB (~0,40€) da una de las mejores vistas de ciudad de Sudamérica."},
        {"title": "Mercado de las Brujas (Hechicería)", "description": "El mercado donde las 'yatiris' (curanderas aymaras) venden amuletos, plantas medicinales, fetos de llama para rituales y ofrendas a la Pachamama. Único en el mundo."},
        {"title": "Valle de la Luna", "description": "A 10 km del centro, las formaciones erosionadas de arcilla forman un paisaje lunático de agujas y laberintos. Entrada: 30 BOB, taxi 30-40 BOB ida y vuelta."},
        {"title": "Salar de Uyuni (excursión de 3-4 días)", "description": "El salar más grande del mundo (10.582 km²) a 640 km al sur. El espejo salado, las islas de cactus y el tren fantasma son una experiencia única en el planeta. Tours desde La Paz: 150-250$."},
        {"title": "Titicaca y la isla del Sol", "description": "A 3h de bus, el lago más alto del mundo navegable (3.800m) tiene en la Isla del Sol las ruinas del Templo del Sol incaico y comunidades aymaras viviendo como en el siglo XV."},
        {"title": "Death Road en mountain bike", "description": "El descenso en bicicleta por la 'Carretera de la Muerte' (64 km, bajada de 3.600m a 1.200m) es el tour de aventura más famoso de Sudamérica. Tours desde 65$ con equipo y guía."}
    ],
    "food_and_drink": "La cocina boliviana altiplánica: salteñas (empanadas horneadas con caldo de carne, el desayuno nacional, se sirven hasta las 11am), fricasé (cerdo con maíz en caldo picante), sopa de maní (cacahuete), thimpu (estofado de cordero) y las papas bolivianas (más de 3.000 variedades). Las salteñas de La Paz son las mejores de Bolivia. Almuerzo completo: 3-5 BOB.",
    "safety": "La Paz tiene zonas de diferente seguridad. El centro y Sopocachi son razonablemente seguros. Cuidado con los timos de taxi ('taxi piratas'). Usa RadioTaxi (llamando) o aplicaciones. La altitud puede afectar — no hagas esfuerzo físico las primeras 24-48h.",
    "visa_info": "Españoles entran sin visado hasta 90 días. Moneda: boliviano (BOB). 1€ ≈ 7,50 BOB.",
    "local_tips": ["La altitud de 3.640m afecta con dolor de cabeza y cansancio — descansa las primeras 24h y bebe mucha agua (no alcohol)", "Las salteñas se comen DE PIE, por la mañana (se venden hasta las 11am) y con cuidado de no manchar — hay arte en comerlas sin perder el caldo", "Mi Teleférico con el billete combinado de 3 BOB permite cruzar toda la ciudad — hazlo", "El Salar de Uyuni requiere mínimo 3 días de tour — no intentes hacerlo en 1 día", "Compra la artesanía andina (tejidos, alpaca) en el Mercado Artesanal, no en las tiendas de la calle Sagárnaga (más caras)"],
    "travel_styles": ["aventura", "cultura", "naturaleza", "budget"],
    "vibes": ["andean", "high altitude", "indigenous", "salt flat"],
    "climate": ["highland subarctic", "cold nights"],
    "best_months": ["May", "June", "July", "August", "September"],
    "budget_daily_low": 20, "budget_daily_mid": 45, "budget_daily_high": 120, "guide_quality": 8
},
{
    "slug": "panama-city", "name": "Ciudad de Panamá", "country": "Panamá", "continent": "América", "type": "city",
    "coordinates": {"lat": 8.9936, "lng": -79.5197},
    "tagline": "El canal que une dos océanos, el Casco Viejo y la jungla a 30 minutos del rascacielos",
    "intro": "Ciudad de Panamá es la única ciudad del mundo con dos océanos visibles desde el mismo rascacielos — el Atlántico al norte y el Pacífico al sur. El Canal de Panamá, que une los dos océanos y por donde pasa el 5% del comercio mundial, tiene el centro de visitantes más espectacular de Centroamérica: el mirador de Miraflores te pone frente a los portacontenedores más grandes del planeta cruzando una esclusa a 10 metros.\n\nEl Casco Antiguo (UNESCO), el barrio colonial del siglo XVII restaurado con bares de rooftop, restaurantes de alta cocina y galerías de arte, es el lugar más agradable del istmo centroamericano. El barrio de Marbella y Punta Pacífica forman el skyline más impresionante del norte de Sudamérica.\n\nLo que pocos saben: a 40 minutos del centro hay selva tropical con monos, perezosos y tucanes — el Parque Nacional Soberanía tiene la mayor densidad de aves por km² de cualquier parque del mundo.",
    "when_to_go": "Diciembre-abril: la estación seca en el Pacífico. El Canal siempre funciona. La estación lluviosa (mayo-noviembre) tiene lluvias intensas en la tarde pero las mañanas suelen ser soleadas — los precios bajan y hay menos turistas.",
    "how_to_get_there": "Aeropuerto Internacional de Tocumen, el hub de Copa Airlines para toda América. Muchas conexiones directas de Europa. Metro al centro (0,35$). Taxi al Casco Antiguo: 25-30$ (negociar).",
    "where_to_sleep": [
        {"name": "Casco Antiguo", "description": "El barrio histórico UNESCO con los mejores hoteles boutique (desde 70$) y restaurantes. La experiencia más recomendada."},
        {"name": "Marbella / Bella Vista", "description": "El barrio moderno más agradable con buenos hoteles desde 60$ y acceso a todo."},
        {"name": "El Cangrejo", "description": "El barrio de vida nocturna y restaurantes locales. Más económico, buena relación calidad-precio."}
    ],
    "what_to_do": [
        {"title": "Esclusas de Miraflores (Canal de Panamá)", "description": "El centro de visitantes del Canal es uno de los mejores del mundo: ves los barcos gigantes cruzando las esclusas desde una terraza a 10 metros. El documental en el teatro es excelente. 20$."},
        {"title": "Casco Antiguo — calles coloniales", "description": "El barrio colonial restaurado con la catedral metropolitana, la plaza de la Independencia y los bares de rooftop con vistas al skyline moderno. El mejor contraste arquitectónico de Centroamérica."},
        {"title": "Parque Natural Metropolitano y Soberanía", "description": "A 30 minutos del centro, los coatíes, perezosos y 400 especies de aves de la selva tropical panameña son accesibles sin salir de la ciudad. Gratuito el Metropolitan Park."},
        {"title": "Isla Taboga (excursión de día)", "description": "La 'isla de las flores' a 20 km del centro en ferry (30 min, 20$) tiene playas de arena, el pueblo colonial más antiguo de la costa pacífica y caminatas con vistas al Canal."},
        {"title": "Mercado de Mariscos", "description": "El mayor mercado de pescado y mariscos de Panamá junto a la bahía. El ceviche panameño (con ají chombo) es el mejor de Centroamérica. Un desayuno completo de marisco: 8-12$."},
        {"title": "Biomuseo (Frank Gehry)", "description": "El único edificio de Frank Gehry en América Latina documenta cómo el istmo de Panamá dividió los océanos y creó dos ecosistemas distintos. Arquitectónicamente espectacular. 22$."}
    ],
    "food_and_drink": "La cocina panameña mezcla afrocaribeña, indígena e hispana: el sancocho (sopa de pollo con coriandro, el plato nacional), el ceviche de corvina (con limón y ají chombo, muy diferente al peruano), los patacones (plátano frito aplastado) y el arroz con pollo panameño. El Mercado de Mariscos es el mejor lugar para el ceviche. Cena en Casco Antiguo: 15-30$.",
    "safety": "Ciudad de Panamá tiene áreas de diferente seguridad. El Casco Antiguo, Marbella y El Cangrejo son seguros para turistas. Evita El Chorrillo (junto al Casco, pero diferente zona) y las periferias. Usa Uber o taxis de hotel.",
    "visa_info": "Españoles entran sin visado hasta 90 días. El dólar americano es la moneda oficial (Panamá no tiene moneda propia — usa el 'balboa' que es 1:1 con el dólar).",
    "local_tips": ["Uber funciona perfectamente en Ciudad de Panamá — mucho más cómodo que negociar taxis", "El Canal se puede ver mejor en Miraflores (esclusa del Pacífico) o en las de Agua Clara (Atlántico) — esta última más nueva y espectacular", "El Casco Antiguo de día es para turistas; de noche los bares de rooftop con el skyline iluminado son para locales", "El ceviche del Mercado de Mariscos a las 8am es el mejor desayuno de Ciudad de Panamá", "Panamá es el hub de vuelos de Copa Airlines — revisar conexiones antes de reservar puede ahorrar mucho"],
    "travel_styles": ["cultura", "naturaleza", "historia", "negocios"],
    "vibes": ["canal", "cosmopolitan", "tropical", "two oceans"],
    "climate": ["tropical", "dry season Dec-Apr"],
    "best_months": ["December", "January", "February", "March", "April"],
    "budget_daily_low": 45, "budget_daily_mid": 95, "budget_daily_high": 230, "guide_quality": 8
},
# More Asia
{
    "slug": "vientiane", "name": "Vientián", "country": "Laos", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 17.9757, "lng": 102.6331},
    "tagline": "La capital más tranquila de Asia: templos dorados, el Mekong y el ritmo que el mundo olvidó",
    "intro": "Vientián es la capital más lenta de Asia — en el buen sentido. No tiene la intensidad de Bangkok, el caos de Hanói ni la masa de Pekín. Lo que tiene es una dimensión humana única para una capital asiática: se puede recorrer completamente en bicicleta, los restaurantes cierran antes de las 22h y el paseo del Mekong al atardecer es el ritual cotidiano más relajante del sudeste asiático.\n\nEl Pha That Luang, la estupa dorada más importante de Laos (símbolo nacional), el Arco del Triunfo laosiano (Patuxai, copia del de Paris pero con decoración budista) y los templos coloniales franco-laotinos forman un paisaje urbano de elegancia discreta. El mercado nocturno junto al Mekong tiene la mejor artesanía laosiana a precios honestos.\n\nVientián es ideal combinada con Vang Vieng (3h al norte) y Luang Prabang (6-8h al norte), las otras capitales de un país que tiene el ritmo del río que lo atraviesa.",
    "when_to_go": "Noviembre-febrero: la estación seca y más fresca (20-28°C). El Mekong está en su nivel normal. El monzón (mayo-octubre) tiene lluvias fuertes pero el paisaje es más verde.",
    "how_to_get_there": "Aeropuerto Internacional de Vientián con conexiones de Bangkok, Hanói, Kuala Lumpur y Singapur. Vuelos directos desde Pekín y Guangzhou. Bus nocturno desde Bangkok (12h). Tren de alta velocidad Laos-China (desde 2021) desde la frontera norte.",
    "where_to_sleep": [
        {"name": "Setthathirath / Centro", "description": "El corazón colonial con los mejores hoteles boutique (desde 30$) y acceso a pie a los templos y el Mekong."},
        {"name": "Riviera del Mekong", "description": "Las guesthouses junto al río tienen las mejores terrazas. Desde 15$/noche."},
        {"name": "Barrio Sur", "description": "Más tranquilo y económico, con buen transporte al centro. Guesthouses desde 12$."}
    ],
    "what_to_do": [
        {"title": "Pha That Luang", "description": "La estupa dorada del siglo XVI, símbolo de Laos y del budismo laosiano. Impresionante al amanecer cuando la luz dorada refleja el mismo tono que el edificio. Entrada: 5.000 LAK (~0,25€)."},
        {"title": "Paseo del Mekong al atardecer", "description": "El río Mekong que marca la frontera con Tailandia al atardecer es el momento más bello de Vientián. El paseo fluvial con los puestos de comida callejera y las familias laotianas es el salón de la ciudad."},
        {"title": "Mercado Nocturno del Mekong", "description": "Los fines de semana el paseo fluvial se llena de puestos con artesanía laosiana (seda, tejidos, figuras de Buda), comida callejera y la mejor atmósfera de Vientián."},
        {"title": "Wat Sisaket", "description": "El templo más antiguo de Vientián (1818), con 6.840 miniaturas de Buda en las paredes del claustro. El más auténtico de la ciudad. Entrada: 5.000 LAK."},
        {"title": "Patuxai (Arco del Triunfo laosiano)", "description": "El arco del triunfo construido con cemento donado por EEUU para una pista de aterrizaje, con decoraciones budistas laotianas en los frescos. Las vistas desde arriba (3.000 LAK) son las mejores de la ciudad."},
        {"title": "Excursión en bici a Buda Park (Xieng Khuan)", "description": "A 25 km del centro, el parque de esculturas budistas e hinduistas del siglo XX del 'profeta' Bunleua Sulilat es surrealista y fascinante. Alquila bicicleta y ve por la carretera del Mekong."}
    ],
    "food_and_drink": "La cocina laosiana es la menos conocida del sudeste asiático: laap (ensalada de carne picada con hierbas, el plato nacional), tam mak hoong (papaya verde picada con chile, diferente al thai), khao niew (arroz glutinoso que se come con las manos) y el Or Lam (estofado de búfalo con hierbas del bosque). El mercado matutino Talat Sao tiene el mejor desayuno de fideo pho local por 1-2$.",
    "safety": "Vientián es una de las capitales más seguras de Asia. Prácticamente sin incidentes para turistas. El único riesgo es el tráfico sin semáforos — cruza con cuidado.",
    "visa_info": "Los españoles pueden obtener visa a la llegada en el aeropuerto (30 días, 30-40$) o e-visa online. El visa on arrival requiere foto de pasaporte. Moneda: kip laosiano (LAK). 1€ ≈ 22.000 LAK.",
    "local_tips": ["Alquila una bicicleta para moverse — Vientián es plana y tiene muy poco tráfico en comparación con otras capitales asiáticas", "La cerveza Beerlao (especialmente la oscura) es la cerveza nacional y está fría a 1$ en cualquier bar del Mekong", "El laap de pollo o cerdo en los puestos del mercado es el plato más auténtico de Laos por menos de 2$", "El Buda Park en bicicleta por la carretera del Mekong es uno de los paseos más tranquilos de Asia", "Combina Vientián con al menos 3 noches en Luang Prabang — es la joya de Laos"],
    "travel_styles": ["cultura", "relajado", "budget", "budismo"],
    "vibes": ["mekong", "slow", "buddhist", "colonial french"],
    "climate": ["tropical monsoon"],
    "best_months": ["November", "December", "January", "February", "March"],
    "budget_daily_low": 18, "budget_daily_mid": 40, "budget_daily_high": 100, "guide_quality": 8
},
{
    "slug": "lahore", "name": "Lahore", "country": "Pakistán", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 31.5204, "lng": 74.3587},
    "tagline": "La ciudad mogola: la Fortaleza Lahore, la mezquita Badshahi y el corazón cultural de Pakistán",
    "intro": "Lahore es la segunda ciudad de Pakistán y la capital cultural del país — la Venecia de Asia del Sur, según algunos. El conjunto de la Fortaleza Lahore y la Mezquita Badshahi (UNESCO) es uno de los conjuntos arquitectónicos mogoles más impresionantes del mundo, equiparable al Taj Mahal en calidad aunque mucho menos visitado por turistas occidentales.\n\nLahore tiene una energía intelectual y artística que Karachi no tiene: las universidades históricas, el barrio de Anarkali con sus especias y tejidos, el mercado de Wazir Khan y el Jardín Shalimar hacen de la Ciudad Vieja una de las mejores de Asia del Sur. Los lahories (habitantes de Lahore) tienen fama de ser los más hospitalarios de Pakistán — y Pakistán ya tiene fama de ser uno de los países más hospitalarios del mundo.\n\nATENCIÓN: Consulta las condiciones de seguridad antes de viajar. La situación política y de seguridad de Pakistán puede cambiar. Las zonas turísticas de Lahore son consideradas relativamente seguras.",
    "when_to_go": "Octubre-marzo: temperaturas agradables (15-25°C). El verano (abril-junio) puede superar los 45°C — no apto para turismo intensivo. El monzón (julio-septiembre) baja temperaturas pero con lluvias intensas.",
    "how_to_get_there": "Aeropuerto Internacional de Lahore (Allama Iqbal) con conexiones de Dubái, Doha, Estambul y las principales ciudades asiáticas. Vuelos directos desde algunas ciudades europeas. Tren desde Islamabad (4h) y Karachi (20h).",
    "where_to_sleep": [
        {"name": "Gulberg", "description": "El barrio moderno más seguro con los mejores hoteles desde 40$ y restaurantes de calidad."},
        {"name": "Ciudad Vieja (Walled City)", "description": "Alojarse dentro de las murallas mogolas es la experiencia más auténtica. Guesthouses desde 15$."},
        {"name": "Defence Housing Authority (DHA)", "description": "El barrio más moderno y seguro, preferido por expatriados. Hoteles desde 60$."}
    ],
    "what_to_do": [
        {"title": "Fortaleza Lahore y Mezquita Badshahi (UNESCO)", "description": "La fortaleza mogola del siglo XVI con sus palacios de mármol y el Sheesh Mahal (palacio de los espejos), junto a la mezquita más grande del mundo cuando fue construida en 1673. Un conjunto arquitectónico comparable al mejor del continente. 500 PKR."},
        {"title": "Ciudad Vieja amurallada — calles y bazares", "description": "El laberinto de la Ciudad Vieja con el bazar de Anarkali (tejidos y especias), el bazar de Coppersmiths y la mezquita de Wazir Khan (la más elaborada de los mogoles) — un día entero de exploración."},
        {"title": "Jardín Shalimar", "description": "El jardín mogol del siglo XVII con canales, fuentes y terrazas escalonadas, construido por el mismo Shah Jahan que construyó el Taj Mahal. UNESCO, menos masificado (500 PKR)."},
        {"title": "Museo de Lahore", "description": "La colección más completa de arte gandhárico (greco-budista del siglo I-IV d.C.) del mundo, más arte mogol y del período colonial. El fasting Buddha es la escultura más famosa del museo."},
        {"title": "Food Street de Gawalmandi", "description": "La calle gastronómica más animada de Lahore: barbacoa de paya (patas de cabra), seekh kebab, nihari (estofado de carne lenta) y los mejores dulces punjabís del mundo. Mejor de noche."},
        {"title": "Ruta de la Luz de Wagah (ceremonia de la bandera)", "description": "La ceremonia de cambio de guardia en la frontera India-Pakistán a 30 km de Lahore es uno de los espectáculos más curiosos del mundo — 20.000 espectadores en cada lado mirándose a través de la valla."}
    ],
    "food_and_drink": "La cocina lahori punjabí es la más rica de Pakistán: nihari (estofado de carne cocida 8h), karahi de pollo (wok de pollo con tomate y chile), haleem (trigo y carne molida), seekh kebab y las mithai (dulces) de leche condensada. La Food Street de Gawalmandi de noche es imprescindible. Cena completa 5-15$.",
    "safety": "Lahore es considerada más segura que Karachi para turistas. La Ciudad Vieja, Gulberg y el área turística son manejables. Siempre con guía local para la Ciudad Vieja. Consulta el nivel de alerta del Ministerio de Exteriores español antes de viajar.",
    "visa_info": "Los españoles necesitan visa de Pakistán. El e-visa online es la opción más fácil (50$, tramitación 7-10 días). Moneda: rupia pakistaní (PKR). 1€ ≈ 310 PKR.",
    "local_tips": ["Un guía local de la Ciudad Vieja (20-30$) hace la experiencia mucho más rica — evita perderte en el laberinto sin contexto", "La ceremonia de Wagah requiere llegar 1-2h antes para conseguir buen sitio — es gratuita", "El chai pakistaní (con leche y cardamomo) se sirve en todos lados como acto de hospitalidad", "Los paquistanís son genuinamente entusiastas con los turistas occidentales — prepárate para muchas invitaciones a tomar chai", "El e-visa proceso online — el sitio oficial puede ser lento, ten paciencia y guarda confirmación"],
    "travel_styles": ["historia", "cultura", "gastronomía", "arquitectura"],
    "vibes": ["mughal", "south asia", "intense", "cultural capital"],
    "climate": ["semi-arid", "hot summers"],
    "best_months": ["October", "November", "December", "January", "February", "March"],
    "budget_daily_low": 20, "budget_daily_mid": 45, "budget_daily_high": 120, "guide_quality": 8
},
# More Africa
{
    "slug": "windhoek", "name": "Windhoek", "country": "Namibia", "continent": "África", "type": "city",
    "coordinates": {"lat": -22.5597, "lng": 17.0832},
    "tagline": "La puerta al desierto del Namib, el Etosha y los paisajes más dramáticos de África austral",
    "intro": "Windhoek es la capital más pequeña y ordenada del África austral — una ciudad alemana transplantada al corazón de África, con Bratwurst y cerveza en la misma calle que la artesanía herero y los vendedores de biltong (carne seca). El legado colonial alemán de 1884-1915 está en los edificios de la Alte Feste (fortaleza alemana) y la Christuskirche (iglesia luterana), pero la ciudad es profundamente namibiana.\n\nLo que importa de Windhoek es lo que tiene alrededor: el Desierto del Namib (el más antiguo del mundo, 55 millones de años), las dunas de Sossusvlei (300m de altura, las más altas del mundo), el Parque Nacional Etosha con el mejor safari de rinocerontes blancos de África y la Costa de los Esqueletos.\n\nNamibia tiene una densidad de población de solo 3 personas por km² — el país más despoblado de África y de los más despoblados del mundo. Lo que hay en esos km² es pura naturaleza salvaje.",
    "when_to_go": "Junio-octubre: la estación seca y fresca (15-25°C). El Etosha tiene los mejores avistamientos de fauna cuando los animales se concentran en los aguaderos. La estación lluviosa (noviembre-abril) hace algunas pistas intransitables.",
    "how_to_get_there": "Aeropuerto Internacional de Hosea Kutako (45 km del centro). Conexiones de Frankfurt (Lufthansa, directo), Johannesburgo, El Cairo y Dubái. Taxi al centro: 300-400 NAD.",
    "where_to_sleep": [
        {"name": "Klein Windhoek", "description": "El barrio residencial más agradable y seguro con los mejores lodges boutique (desde 80$) y restaurantes."},
        {"name": "Centro (Independence Avenue)", "description": "El centro histórico con los hoteles principales desde 60$ y los atractivos coloniales."},
        {"name": "Katutura", "description": "El township con la vida namibiana más auténtica. Solo con guía local."}
    ],
    "what_to_do": [
        {"title": "Alte Feste y Museo Nacional de Namibia", "description": "La fortaleza alemana de 1890 alberga el museo con la historia de Namibia, desde los San Bushmen hasta la independencia de 1990. El edificio es de lejos el más emblemático de la ciudad."},
        {"title": "Post Street Mall y artesanía namibiana", "description": "La calle peatonal del centro con artesanía herero, tejidos namas y el mejor biltong de Namibia. Los mercadillos de los fines de semana en el Craft Market tienen precios más honestos."},
        {"title": "Excursión a Sossusvlei (desierto del Namib)", "description": "A 350 km, las dunas de 300 metros de altura de color rojo-naranja del Sossusvlei al amanecer son una de las imágenes más icónicas de África. Dune 45 y Dead Vlei (árboles muertos en sal) son los puntos más fotográficos."},
        {"title": "Parque Nacional Etosha (2-3 días)", "description": "A 400 km al norte, el mejor parque para ver los cinco grandes (más elefantes, jirafas y rinocerontes blancos) en un escenario de pan salino (etosha = 'gran espacio blanco'). Self-drive safari posible."},
        {"title": "Katutura Township Tour", "description": "El township de Windhoek con guía local muestra la vida de la mayoría de los namibianos — el mercado Soweto, la cerveza chibuku fermentada y el contexto histórico del apartheid namibiano."},
        {"title": "Joe's Beerhouse para una braai (barbacoa namibia)", "description": "El restaurante más famoso de Windhoek combina cocina namibiana (oryx, kudu, warthog a la brasa) con el ambiente más relajado de la ciudad."}
    ],
    "food_and_drink": "La cocina namibiana mezcla legados alemán, afrikáner e indígena: biltong (carne seca curada) de oryx y kudu, Bratwurst namibia, bredie (estofado de cordero) y el kapana (carne de res a la brasa callejera) del mercado Soweto. La cerveza Windhoek Lager (fabricada con las recetas de pureza alemanas) es la mejor cerveza de África. Joe's Beerhouse es el mejor lugar para comer carne de caza.",
    "safety": "Windhoek es relativamente segura para capitales africanas. Klein Windhoek y el centro colonial son los barrios más seguros. Katutura requiere guía. No salgas a caminar solo de noche fuera del área turística.",
    "visa_info": "Los españoles pueden entrar sin visado hasta 90 días. Moneda: dólar namibio (NAD) = rand sudafricano (ambas válidas). 1€ ≈ 20 NAD.",
    "local_tips": ["El self-drive en Namibia es posible y recomendable — las carreteras de grava son transitables con un turismo normal en la mayoría de parques", "Alquila el coche en Windhoek (mucho más barato que en Johannesburgo) para el safari por Etosha y Sossusvlei", "El biltong de oryx en cualquier supermercado namibio es el mejor souvenir gastronómico de África austral", "El Etosha en self-drive es perfectamente posible — los campamentos del parque son excelentes y económicos", "La cerveza Windhoek Lager se fabrica con la Ley de Pureza Alemana de 1516 — pruébala directamente en Namibia"],
    "travel_styles": ["naturaleza", "safari", "aventura", "road trip"],
    "vibes": ["namibian", "desert", "german colonial", "wildlife"],
    "climate": ["semi-arid", "hot summers"],
    "best_months": ["June", "July", "August", "September", "October"],
    "budget_daily_low": 45, "budget_daily_mid": 100, "budget_daily_high": 280, "guide_quality": 8
},
{
    "slug": "maputo", "name": "Maputo", "country": "Mozambique", "continent": "África", "type": "city",
    "coordinates": {"lat": -25.9692, "lng": 32.5732},
    "tagline": "La capital más vibrante del África lusófona: arquitectura art nouveau, jazz y playas del Índico",
    "intro": "Maputo es la capital de Mozambique y la más sorprendente de las capitales lusófonas de África — tiene una arquitectura art nouveau y modernista de los años 60 (Amâncio Guedes diseñó más de 500 edificios) que ninguna otra ciudad africana posee, playas de arena blanca a 30 minutos del centro y una escena musical de marrabenta (el ritmo mozambiqueño) que llena los bares del barrio de Sommerschield hasta las 4 de la madrugada.\n\nMozambique es un país que salió de una guerra civil devastadora (1977-1992) y aún tiene las marcas económicas de esa historia, pero Maputo avanza — la ciudad tiene una energía creativa y una mezcla cultural africana-portuguesa que produce artistas, músicos y cocineros de un nivel inesperado.\n\nLa comida de Maputo — piri piri, marisco del Índico, camarão (gambas) gigantes y caril de coco — es de las mejores de toda África.",
    "when_to_go": "Mayo-octubre: la estación seca con temperaturas de 22-28°C. El verano (noviembre-marzo) es caluroso y húmedo (30-35°C) con lluvias intensas. Las playas del Índico son visitables todo el año pero los meses secos son más agradables.",
    "how_to_get_there": "Aeropuerto Internacional de Maputo con conexiones de Johannesburgo (1h), Lisboa (directo), Nairobi y Dubái. Ferry desde la KwaZulu-Natal de Sudáfrica. Bus desde Johannesburgo (9h).",
    "where_to_sleep": [
        {"name": "Polana / Sommerschield", "description": "El barrio más seguro y agradable, con los mejores restaurantes y el famoso Hotel Polana. Hoteles desde 60$."},
        {"name": "Costa do Sol", "description": "El barrio de playa a 15 km del centro, más económico y relajado. Pousadas desde 30$."},
        {"name": "Centro (Baixa)", "description": "El corazón histórico con los mejores edificios art nouveau. Hoteles desde 50$."}
    ],
    "what_to_do": [
        {"title": "Arquitectura de Amâncio Guedes y Baixa", "description": "La Baixa de Maputo tiene la mayor concentración de arquitectura modernista africana del continente: el Mercado Municipal, el edificio Smiling Lion y la Estação Central de Caminhos de Ferro (estación del tren, la más bonita de África oriental)."},
        {"title": "Restaurante Costa do Sol y marisco del Índico", "description": "El restaurante más famoso de Mozambique, abierto desde 1938 junto a la playa, sirve el camarão gigante (gambas de 300g) a la piri piri que es el plato más icónico del país. Precio: 25-40$."},
        {"title": "Mercado Municipal", "description": "El mercado central de Maputo con sus pinturas exteriores y el mejor pescado y marisco fresco del Índico. Los vendedores de camarão (gambas) y lagostim (langostinos) tienen los mejores precios."},
        {"title": "Museo Nacional de Arte", "description": "La mejor colección de arte mozambiqueño y makondes (tallas de ébano) de África. El surrealismo africano de los escultores makondes es una de las expresiones artísticas más originales del continente."},
        {"title": "Punta de Oro y Tofo (excursión de 2-3 días)", "description": "A 1-2h al norte, las playas de Tofo y Barra son algunas de las mejores del mundo para el buceo con tiburones ballena, mantarrayas y tortugas. El arrecife de coral está entre los mejores del Índico."},
        {"title": "Bares de marrabenta en Sommerschield", "description": "La marrabenta (el ritmo mozambiqueño) tiene sus mejores sesiones en Maputo. Gil Semedo Bar y Restaurante Víctor's tienen los mejores conciertos los fines de semana."}
    ],
    "food_and_drink": "La cocina mozambiqueña es la mejor de África lusófona: camarão piri piri (gambas gigantes en salsa de chile y lima), matapa (hojas de yuca con coco y gambas), frango à zambeziana (pollo al vino y lima) y piri piri en todo. La piri piri mozambiqueña es la original — más fresca y cítrica que la portuguesa. Cena en restaurante local: 10-20$.",
    "safety": "Maputo tiene zonas de diferente seguridad. Polana y Sommerschield son seguros. La Baixa de día es manejable. No camines solo de noche fuera de las áreas turísticas. Usa chapas (minibuses) o chapas+táxi para moverse.",
    "visa_info": "Los españoles necesitan visa de Mozambique. Solicita e-visa online antes del viaje (50$, 30 días). Moneda: metical mozambiqueño (MZN). 1€ ≈ 70 MZN.",
    "local_tips": ["El camarão piri piri gigante del Costa do Sol justifica el viaje por sí solo", "El Mercado Municipal a primera hora de la mañana (7-9am) tiene la mejor selección de marisco fresco", "Aprende dos palabras en portugués — los mozambiqueños aprecian el intento aunque hablen inglés", "El buceo en Tofo con tiburones ballena (noviembre-marzo) es uno de los mejores encuentros marinos del mundo", "El rand sudafricano también se acepta en muchos lugares de Maputo"],
    "travel_styles": ["playa", "cultura", "gastronomía", "buceo"],
    "vibes": ["lusophone", "indian ocean", "jazz", "marrabenta"],
    "climate": ["tropical savanna"],
    "best_months": ["May", "June", "July", "August", "September", "October"],
    "budget_daily_low": 30, "budget_daily_mid": 70, "budget_daily_high": 180, "guide_quality": 8
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
