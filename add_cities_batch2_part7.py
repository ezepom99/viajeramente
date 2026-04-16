import psycopg2
import json

conn = psycopg2.connect("dbname=viajeramente user=tenant")
cur = conn.cursor()

cities = [
{
    "slug": "new-orleans", "name": "Nueva Orleans", "country": "Estados Unidos", "continent": "América", "type": "city",
    "coordinates": {"lat": 29.9511, "lng": -90.0715},
    "tagline": "Jazz, creole food y el Mardi Gras más grande de América del Norte",
    "intro": "Nueva Orleans es la ciudad más europea de EEUU y también la más africana, caribeña y francesa — una mezcla que no existe en ningún otro lugar del mundo. El barrio francés (French Quarter) con sus edificios de balcones de hierro forjado, los bares de jazz en Frenchmen Street que abren hasta el amanecer y la cocina criolla más elaborada del continente son los argumentos principales.\n\nEl Mardi Gras (febrero-marzo) es el carnaval más grande de América del Norte — una semana de parades, máscaras y exceso que transforma toda la ciudad. Pero Nueva Orleans fuera del Mardi Gras tiene igual o más carácter: los cementerios de tumbas elevadas, los mercados del French Market, el Garden District victoriano y la escena culinaria del chef John Besh y sus sucesores son argumentos permanentes.\n\nEl huracán Katrina (2005) destruyó parte de la ciudad pero también despertó una resiliencia creativa que redefinió el carácter de Nueva Orleans.",
    "when_to_go": "Octubre-mayo: los meses más frescos (15-22°C). Febrero-marzo con el Mardi Gras es el pico turístico. El Jazz & Heritage Festival en abril-mayo es el segundo gran evento. El verano (junio-septiembre) es caluroso y húmedo (32-35°C) con riesgo de huracanes.",
    "how_to_get_there": "Aeropuerto Internacional Louis Armstrong con conexiones de EEUU y algunos vuelos internacionales. Bus al centro (2$) o taxi (35-40$). Amtrak desde Chicago y Los Ángeles.",
    "where_to_sleep": [
        {"name": "French Quarter", "description": "La experiencia más icónica pero la más cara y ruidosa. Hoteles boutique desde 120$, hostels desde 40$."},
        {"name": "Marigny / Bywater", "description": "El barrio más auténtico con la mejor escena musical local y los mejores hostels (desde 25$). El más recomendado."},
        {"name": "Garden District", "description": "El barrio victoriano más elegante, tranquilo y con buena gastronomía. Hoteles desde 90$."}
    ],
    "what_to_do": [
        {"title": "Frenchmen Street de noche", "description": "La calle con la mayor concentración de jazz en vivo del mundo: 6-8 clubs a 100 metros unos de otros, sin cover la mayoría. El verdadero jazz de Nueva Orleans, no el turístico de Bourbon Street."},
        {"title": "French Quarter y Jackson Square", "description": "El barrio histórico más icónico de EEUU: balcones de hierro forjado, la catedral de San Luis, el mercado francés y los artistas de calle en Jackson Square."},
        {"title": "Cementerios del Above Ground", "description": "Los cementerios con tumbas elevadas por encima del suelo (la ciudad está bajo el nivel del mar) son únicos en EEUU. St. Louis Cemetery #1 requiere visita guiada (25$) para ver la tumba de Marie Laveau (reina vudú)."},
        {"title": "Garden District Victorian Tour", "description": "Las mansiones antebellum del Garden District son las más grandes de EEUU. El paseo autoguiado por Prytania Street y Coliseum Square (gratis) muestra la opulencia de la era previa a la Guerra Civil."},
        {"title": "Swamp Tour en el bayou", "description": "Los tours en airboat por los bayous a 30 minutos del centro muestran caimanes, garzas y cipreses en un paisaje que parece de película. Tours desde 25$, el favorito de la mayoría de visitantes."},
        {"title": "Gastronomía criolla: Commander's Palace o Dooky Chase", "description": "La cocina criolla de Nueva Orleans en un restaurante de verdad: gumbo, jambalaya, crawfish étouffée y bananas foster. Commander's Palace tiene el jazz brunch del sábado a precio razonable (35$)."}
    ],
    "food_and_drink": "La cocina criolla de Nueva Orleans es una de las más únicas de EEUU: gumbo (guiso de mariscos con okra y roux negro), jambalaya (arroz con pollo, salchicha andouille y gambas), crawfish étouffée (langostinos de río en mantequilla), po'boy (sándwich de ostras o gambas rebozadas) y beignets (buñuelos de azúcar) con café au lait en el Café Du Monde. Cena de mariscos: 25-45$.",
    "safety": "Nueva Orleans tiene zonas de alta criminalidad (Lower Ninth Ward, partes de Central City). El French Quarter, Marigny y Garden District son seguros para turistas. No camines solo de noche fuera de zonas turísticas. Usa Uber.",
    "visa_info": "Españoles necesitan ESTA (21$, online antes del viaje). Estancias hasta 90 días sin visa.",
    "local_tips": ["Frenchmen Street tiene mejor jazz que Bourbon Street y sin cover la mayoría de clubs", "El brunch con jazz del sábado en Commander's Palace reserva con semanas de antelación", "Los beignets en Café Du Monde a las 3am son la mejor experiencia de madrugada de EEUU", "El swamp tour en airboat vale completamente la pena aunque sea turístico", "Durante el Mardi Gras (2-3 semanas antes del Martes Gordo) el alojamiento se reserva con 6 meses de antelación"],
    "travel_styles": ["música", "gastronomía", "cultura", "festival"],
    "vibes": ["jazz", "creole", "mardi gras", "bayou"],
    "climate": ["humid subtropical"],
    "best_months": ["October", "November", "December", "January", "February", "March"],
    "budget_daily_low": 70, "budget_daily_mid": 140, "budget_daily_high": 330, "guide_quality": 8
},
{
    "slug": "san-juan-pr", "name": "San Juan", "country": "Puerto Rico (EEUU)", "continent": "América", "type": "city",
    "coordinates": {"lat": 18.4655, "lng": -66.1057},
    "tagline": "El Caribe latino con pasaporte americano: el Viejo San Juan más bonito del Caribe y las mejores playas de la isla",
    "intro": "San Juan es la capital de Puerto Rico — el único lugar de América Latina donde puedes pagar en dólares, volar sin pasaporte desde EEUU y tener la gastronomía caribeña y latina más auténtica del Caribe bajo administración americana. El Viejo San Juan con sus adoquines azules, las casas de colores pastel y las fortalezas españolas del siglo XVI (El Morro y San Cristóbal) es el casco histórico colonial más bonito del Caribe.\n\nPuerto Rico tiene las mejores playas del Caribe en accesibilidad y calidad — Condado y Isla Verde para el turismo hotelero, pero Luquillo (la playa de los puertorriqueños), Flamenco Beach en Culebra (votada una de las mejores del mundo) y las playas de Rincón para el surf son de calidad extraordinaria.\n\nLa gastronomía boricua — mofongo, lechón asado, tostones — y la música salsa y reggaeton (Puerto Rico inventó el reggaeton) crean una identidad cultural incomparable en el Caribe.",
    "when_to_go": "Diciembre-abril: la temporada alta con clima perfecto (24-28°C) y mares calmados. La temporada de huracanes es junio-noviembre — el período menos recomendado aunque los hoteles están a mitad de precio.",
    "how_to_get_there": "Aeropuerto Internacional Luis Muñoz Marín con muchos vuelos directos desde EEUU y Europa (Iberia desde Madrid). Sin pasaporte para ciudadanos americanos. Taxi al Viejo San Juan: 15-20$.",
    "where_to_sleep": [
        {"name": "Viejo San Juan", "description": "La experiencia más única — hostels desde 25$ en casas coloniales, hoteles boutique desde 90$. Reserva con antelación."},
        {"name": "Condado", "description": "El barrio de hoteles de lujo junto a la playa. Desde 100$, acceso directo al mar."},
        {"name": "Santurce", "description": "El barrio más creativo con arte mural y los mejores restaurantes locales. Apartamentos desde 60$/noche."}
    ],
    "what_to_do": [
        {"title": "El Morro (Castillo San Felipe del Morro)", "description": "La fortaleza española del siglo XVI en el extremo de la península, con murallas de 140 metros sobre el mar. Los campos de viento delante del castillo son perfectos para volar cometas. 10$."},
        {"title": "Viejo San Juan — adoquines azules", "description": "Las calles adoquinadas en azul (adoquines de escoria de fundición traídos de España) del casco histórico colonial son únicas en el mundo. La Calle del Cristo y la Calle Fortaleza tienen las mejores fachadas de colores."},
        {"title": "Playa Flamenco en Culebra", "description": "La isla de Culebra (ferry desde Fajardo, 1,5h, 2,25$) tiene la playa más bonita del Caribe según muchas clasificaciones: aguas de laguna, arena blanca y ninguna infraestructura hotelera masiva."},
        {"title": "Bosque Nacional El Yunque", "description": "El único bosque tropical lluvioso de la red del US Forest Service, a 45 min del centro. Cascadas, cotorras puertorriqueñas y helechos gigantes en un ecosistema único. 5$ entrada."},
        {"title": "La Placita de Santurce de noche", "description": "La plaza de mercado que de noche se transforma en el mayor botellón de San Juan — decenas de bares alrededor de una plaza con música, ron y la escena más auténtica de la ciudad."},
        {"title": "Lechón asado en La Ruta del Lechón (Guavate)", "description": "A 30 min en coche, la carretera de Guavate tiene más de 20 restaurantes especializados en lechón asado entero. El domingo es el día de peregrinación gastronómica de los puertorriqueños."}
    ],
    "food_and_drink": "La cocina boricua: mofongo (plátano verde machacado con ajo y chicharrón, relleno de carne o mariscos — el plato nacional), tostones (plátano verde frito aplastado), lechón asado (cerdo al horno de pit), arroz con gandules (con pigeon peas) y el coquito (ron con coco, la bebida navideña). Ron Don Q o Bacardí (fabricado en Puerto Rico) son las bebidas nacionales. Cena en restaurante local: 15-30$.",
    "safety": "San Juan tiene zonas de diferente seguridad. El Viejo San Juan, Condado e Isla Verde son seguros para turistas. Evita los caseríos (proyectos de vivienda) y algunas zonas de Santurce de noche. Uber funciona bien.",
    "visa_info": "Puerto Rico es territorio de EEUU — mismas reglas. Españoles necesitan ESTA (21$) o visa de turista. Los ciudadanos americanos no necesitan pasaporte.",
    "local_tips": ["Flamenco Beach en Culebra (ferry desde Fajardo) justifica un desvío de 2 días — lleva snorkel", "El mofongo varía enormemente de restaurante en restaurante — el de La Mallorquina (el más antiguo de la isla) es el de referencia", "La Placita de Santurce los viernes y sábados noche tiene el mejor ambiente de San Juan por 3$ un mojito", "El Viejo San Juan se camina completamente en un día — lleva calzado cómodo para los adoquines", "El El Yunque cierra antes de lo esperado (las 6pm) — llega antes de las 10am para senderismo tranquilo"],
    "travel_styles": ["playa", "historia", "gastronomía", "caribe"],
    "vibes": ["caribbean", "latin", "colonial", "salsa"],
    "climate": ["tropical"],
    "best_months": ["December", "January", "February", "March", "April"],
    "budget_daily_low": 65, "budget_daily_mid": 130, "budget_daily_high": 320, "guide_quality": 8
},
{
    "slug": "kuala-lumpur", "name": "Kuala Lumpur", "country": "Malasia", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 3.1390, "lng": 101.6869},
    "tagline": "Las Torres Petronas, el mejor street food de Asia y el hub del Sudeste Asiático",
    "intro": "Kuala Lumpur tiene las Torres Petronas — los edificios más altos del mundo de 1998 a 2004, todavía los gemelos más altos jamás construidos — que dominan el skyline de una ciudad que es uno de los mejores destinos de Asia para comer. La escena gastronómica de KL mezcla malaya, china e india en una densidad sin igual: el Jalan Alor para el street food chino nocturno, el Little India de Brickfields para los roti canai al curry, el Chinatown de Petaling Street y los hawker centers del barrio de Chow Kit.\n\nKL es también el hub de conexiones de vuelo del Sudeste Asiático: AirAsia tiene su base aquí y los vuelos internos a Bali, Bangkok, Ho Chi Minh, Hanói, Yangon y Colombo son extraordinariamente baratos. Muchos viajeros usan KL como base para itinerarios de toda la región.\n\nEl barrio de Bangsar y KLCC tienen la escena de cafés y restaurantes modernos que compite con Singapur a precios dos veces más bajos.",
    "when_to_go": "Mayo-julio y enero-febrero son los menos lluviosos. KL tiene lluvia tropical casi todo el año — las tormentas ocurren por las tardes (14-17h) y el resto del día suele ser soleado. Temperatura constante de 28-33°C.",
    "how_to_get_there": "Aeropuerto Internacional de Kuala Lumpur (KLIA y klia2) con conexiones globales. Hub de AirAsia. KLIA Ekspres al centro en 28 min (55 MYR). klia2 tiene bus al centro (12 MYR).",
    "where_to_sleep": [
        {"name": "Bukit Bintang", "description": "El epicentro comercial y gastronómico de KL. Hoteles desde 40$, hostels desde 15$."},
        {"name": "KLCC / Petronas area", "description": "Junto a las Torres, más caro pero conveniente. Hoteles desde 60$."},
        {"name": "Chow Kit / Masjid India", "description": "El barrio más local y económico, con los mejores hawker centers. Hoteles desde 25$."}
    ],
    "what_to_do": [
        {"title": "Torres Petronas y Sky Bridge", "description": "La observación del Sky Bridge (piso 41) y la cúpula (piso 86) de las Torres Petronas. Entradas limitadas — reserva online con semanas de antelación (85 MYR). Las vistas de noche desde KLCC Park (gratis) son también espectaculares."},
        {"title": "Batu Caves y templo hindú", "description": "A 13 km del centro (KTM Komuter, 1$), las cuevas de caliza de 400 millones de años con un templo hindú de Sri Subramaniam y la estatua dorada de Murugan de 43m son la imagen más icónica de Malasia. Gratis."},
        {"title": "Jalan Alor street food de noche", "description": "La calle de street food chino más famosa de KL: pato asado, char kway teow (fideos fritos), satay, marisco a la plancha y zumo de caña de azúcar. El mejor hawker street de la ciudad (18-23h)."},
        {"title": "Chinatown de Petaling Street y Central Market", "description": "El Chinatown con los mejores precios de copia de marcas (sin garantías), el Central Market de artesanías y el Petaling Street con dim sum matutino forman el corazón histórico chino de KL."},
        {"title": "Barrio de Little India (Brickfields)", "description": "El barrio indio tamil más grande del Sudeste Asiático. Los roti canai con dal, el briyani de cordero y los sarees hacen de Brickfields una inmersión en la India sin salir de KL."},
        {"title": "Museo Nacional de Malasia y Perdana Botánico", "description": "El museo más completo sobre la historia y cultura de Malasia, con colecciones keris (daga malaya), wayang kulit (teatro de sombras) y artefactos del sultanato de Malaka. Junto al lago del Parque Perdana (gratuito)."}
    ],
    "food_and_drink": "KL tiene la mejor escena gastronómica de Asia del Sudeste en diversidad: nasi lemak (arroz de leche de coco con sambal, el desayuno nacional), roti canai (pan plano con curry de dal), char kway teow (fideos de arroz fritos con gambas y huevo), laksa (sopa de fideos en curry de coco) y satay con salsa de cacahuete. Un hawker meal completo: 5-8 MYR (1-2€). Café local (teh tarik): 2 MYR.",
    "safety": "KL es relativamente segura. Petaling Street y el Chinatown tienen carteristas. Evita el área de Chow Kit de noche solo. Grab (el Uber malayo) es esencial — evita taxis sin taxímetro.",
    "visa_info": "Los españoles pueden entrar sin visado hasta 90 días. Moneda: ringgit malayo (MYR). 1€ ≈ 5 MYR.",
    "local_tips": ["Grab (la app) es el único taxi que debes usar en KL — los taxis de calle son caros y a veces sin taxímetro", "El KLIA Ekspres es la mejor inversión de 55 MYR — evita el tráfico infernal de KL", "Los hawker centers del mediodía tienen los mejores almuerzos de nasi lemak o roti canai por 3-5 MYR", "Las Petronas al atardecer desde KLCC Park son completamente gratis y casi tan buenas como la visita pagada", "AirAsia tiene vuelos a Bali, Bangkok y toda la región desde KL desde 15-30€ — optimiza el itinerario desde aquí"],
    "travel_styles": ["gastronomía", "cultura", "arquitectura", "hub"],
    "vibes": ["multicultural", "food paradise", "towers", "southeast asia"],
    "climate": ["tropical rainforest"],
    "best_months": ["May", "June", "July", "January", "February"],
    "budget_daily_low": 25, "budget_daily_mid": 60, "budget_daily_high": 170, "guide_quality": 8
},
{
    "slug": "accra-ghana", "name": "Acra", "country": "Ghana", "continent": "África", "type": "city",
    "coordinates": {"lat": 5.6037, "lng": -0.1870},
    "tagline": "La puerta de vuelta a casa: la capital del retorno afrodiaspórico y el West Africa más accesible",
    "intro": "Acra es la capital de Ghana, el país que primero se independizó del colonialismo en el África subsahariana (1957, bajo Kwame Nkrumah). Es también la ciudad donde miles de afroamericanos y caribenos de la diáspora vienen a 'volver a casa' en el marco del 'Year of Return' iniciado en 2019 para el 400 aniversario de la llegada de los primeros esclavos a Virginia.\n\nAcra tiene una energía y calidad de vida para el viajero que pocas capitales africanas occidentales igualan: la zona de Osu tiene restaurantes de todo nivel y una escena nocturna que va desde el highlife (la música nacional) hasta el afrobeats moderno, las playas de Labadi y Bojo son perfectas para surf y relajarse, y el Castillo de Cape Coast a 3h es el lugar más significativo de toda la historia de la esclavitud transatlántica.\n\nGhana es considerado el país más estable y amigable de África occidental para el turismo.",
    "when_to_go": "Noviembre-marzo: la estación más seca (27-32°C). El verano tiene dos períodos lluviosos (mayo-junio y septiembre-octubre) pero las lluvias son de tarde y no impiden el turismo. La Harmattan (viento seco del norte) crea polvo en diciembre-febrero.",
    "how_to_get_there": "Aeropuerto Internacional de Kotoka con conexiones directas de Londres, Amsterdam, Francfort, París y Nueva York. Ethiopian Airways y Kenya Airways también conectan. Taxi al centro: 30-50 cedis.",
    "where_to_sleep": [
        {"name": "Osu / Cantonments", "description": "El barrio más animado con los mejores restaurantes y bares. Hoteles desde 60$, apartamentos desde 40$/noche."},
        {"name": "Labone / Airport Residential", "description": "El barrio más seguro y residencial para expatriados y turistas. Hoteles desde 70$."},
        {"name": "Labadi", "description": "Junto a la playa, más relajado. Hoteles de playa desde 50$."}
    ],
    "what_to_do": [
        {"title": "Castillo de Cape Coast y Elmina (excursión de día)", "description": "A 3h en bus, los castillos del siglo XVII que fueron los principales puertos de embarque de esclavos hacia América. La visita guiada del 'Door of No Return' es la experiencia más emotiva de toda África occidental. Imprescindible."},
        {"title": "Mercado de Makola", "description": "El mercado más grande de Acra con la vida cotidiana ghanesa en toda su intensidad: telas kente, nkontomire fresco, suyas de cerdo y el caos organizado característico de Ghana."},
        {"title": "National Museum of Ghana", "description": "La mayor colección de artefactos ghaneses: telas kente reales, objetos akan, armas de la época colonial y la historia de la independencia narrada desde la perspectiva africana."},
        {"title": "Playa de Labadi y Bojo Beach", "description": "Las mejores playas cercanas a Acra: Labadi tiene acceso público (5 cedis) con músicos y ambiente ghanés; Bojo Beach es privada (20 cedis) con kayak y más tranquilidad."},
        {"title": "Osu Castle y James Town", "description": "El casco histórico colonial de James Town con el faro, el mercado de pescadores y las calles más antiguas de Acra. Meno turístico que el centro pero mucho más auténtico."},
        {"title": "Noche de highlife y afrobeats", "description": "Silverbird Accra, Bloom Bar y Republic Bar tienen los mejores conciertos de highlife y afrobeats de Ghana. La escena musical de Acra es la más vibrante de África occidental."}
    ],
    "food_and_drink": "La cocina ghanesa: jollof rice (competencia épica con Nigeria), fufu (masa de yuca con sopa de cacahuete o palmnut), kelewele (plátano frito especiado), waakye (arroz con judías negras), suya de cerdo y el fresh pepper soup de marisco. El mejor jollof es en el Mövenpick o en cualquier chop bar (restaurante local). Precio chop bar: 3-8 cedis.",
    "safety": "Acra es una de las capitales más seguras de África occidental. El centro, Osu y Labone son seguros para turistas. Las playas requieren atención con los objetos de valor. Usa Uber o aplicaciones de transporte.",
    "visa_info": "Los españoles necesitan visa de Ghana. E-visa online antes del viaje (60$) o tramitación en embajada. Moneda: cedi ghanés (GHS). 1€ ≈ 16 GHS.",
    "local_tips": ["El Castillo de Cape Coast es la visita más importante de toda la costa occidental africana para entender la historia de la esclavitud — no la saltes", "Ghana es el país más fácil y acogedor para el turista occidental de África occidental — buen punto de entrada al continente", "El jollof rice ghanés vs nigeriano es un debate eterno — prueba ambos y da tu opinión", "Uber funciona en Acra y es mucho más transparente que los taxis de calle", "La tela kente (hecha a mano en Kumasi) es el mejor souvenir de Ghana — la artesanal cuesta más pero vale la diferencia"],
    "travel_styles": ["historia", "cultura", "playa", "gastronomía"],
    "vibes": ["west africa", "diaspora", "highlife", "independence"],
    "climate": ["tropical"],
    "best_months": ["November", "December", "January", "February", "March"],
    "budget_daily_low": 30, "budget_daily_mid": 70, "budget_daily_high": 190, "guide_quality": 8
},
{
    "slug": "nicosia", "name": "Nicosia", "country": "Chipre", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 35.1856, "lng": 33.3823},
    "tagline": "La última capital dividida del mundo: dos países, dos culturas y una línea verde en el centro",
    "intro": "Nicosia es la única capital dividida del mundo — la Línea Verde de la ONU, con sus barricadas y alambradas de espino, corta la ciudad desde 1974 separando la República de Chipre al sur de la República Turca de Chipre del Norte (reconocida solo por Turquía). Cruzar de un lado al otro en el checkpoint de Ledra Street es uno de los pasos fronterizos más peculiares y cargados de historia de Europa.\n\nLa Nicosia griega (sur) tiene la Catedral de San Juan, el Museo de Chipre con los mejores mosaicos bizantinos del mundo y el barrio de Laiki Yitonia con la mejor cocina chipriota. La Nicosia turca (norte) tiene la mezquita de Santa Sofía (antes catedral gótica), el mercado cubierto otomano y el Museo del Palacio de Dervish Pasha.\n\nAdemás de la singularidad política, Chipre tiene las mejores rutas de senderismo del Mediterráneo en las montañas de Troodos y el vino Comandaria (el más antiguo del mundo en producción continua, desde 800 a.C.).",
    "when_to_go": "Abril-junio y septiembre-noviembre: clima mediterráneo perfecto (22-28°C). El verano (julio-agosto) es muy caluroso (38°C en Nicosia, interior) — mejor la costa. El invierno es suave (10-16°C) en el centro.",
    "how_to_get_there": "Aeropuerto Internacional de Larnaca (50 km) con conexiones directas de Madrid, Barcelona y toda Europa. Bus al centro de Nicosia (7€). Aeropuerto de Pafos también con vuelos europeos directos.",
    "where_to_sleep": [
        {"name": "Casco Histórico amurallado (sur)", "description": "Dentro de las murallas venecianas del siglo XVI. Boutique hotels desde 70€, las mejores opciones de la ciudad."},
        {"name": "Strovolos / Engomi", "description": "Los barrios modernos con mejor precio-calidad. Hoteles desde 50€, apartamentos desde 40€/noche."},
        {"name": "Nicosia Norte (zona turca)", "description": "Para estancias experimentales al otro lado de la Línea Verde. Hoteles desde 40€ (pagan en libras turcas)."}
    ],
    "what_to_do": [
        {"title": "Cruzar la Línea Verde en Ledra Street", "description": "El único checkpoint urbano de la ONU en Europa, donde cruzar de la República de Chipre a la República Turca requiere mostrar el pasaporte. La experiencia de cruzar y volver es única en el mundo."},
        {"title": "Museo de Chipre", "description": "La mejor colección arqueológica de la isla: estatuas de Afrodita de Soli (el origen de la diosa del amor aquí), mosaicos romanos y artefactos de la Edad del Bronce chipriota. 4,50€."},
        {"title": "Catedral de San Juan (sur)", "description": "La catedral del siglo XVII con los frescos más completos del arte medieval chipriota y el tesoro de la iglesia ortodoxa más rico del Mediterráneo oriental."},
        {"title": "Mezquita de Santa Sofía / Catedral Selimiye (norte)", "description": "La catedral gótica francesa del siglo XIV convertida en mezquita en 1570 — los dos minaretes añadidos sobre las torres góticas originales crean uno de los edificios más singulares del Mediterráneo."},
        {"title": "Calles de Laiki Yitonia y restaurantes cypriotas", "description": "El barrio rehabilitado con las mejores tavernas de cocina chipriota clásica: meze completo (25-30 platos pequeños) con halloumi, souvlaki, kleftiko y commandaria."},
        {"title": "Montañas de Troodos y aldeas pintadas (excursión)", "description": "A 50 km, las montañas con sus iglesias con pinturas del siglo XII-XV (9 declaradas UNESCO) y los pueblos de producción de vino son la excursión más completa desde Nicosia."}
    ],
    "food_and_drink": "La cocina chipriota mezcla griega y medio-oriental: halloumi a la plancha (el queso más famoso de Chipre, exportado mundialmente), souvlaki y sheftalia (salchicha de cordero), kleftiko (cordero horneado en arcilla), meze infinito y el commandaria (vino dulce de pasa, el más antiguo del mundo). Un meze completo en taverna: 20-30€ por persona con vino local.",
    "safety": "Nicosia es muy segura tanto en el sur como en el norte. La Línea Verde con sus barricadas es la zona de 'tensión' visual pero completamente pacífica para turistas.",
    "visa_info": "Chipre (sur) es UE y Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: euro. El norte (TRNC) usa la lira turca y la entrada se selló separadamente históricamente — ya no afecta el pasaporte para viajar a Grecia.",
    "local_tips": ["Cruzar al lado norte requiere pasaporte (aunque seas UE) — lleva el pasaporte siempre en Nicosia", "El meze chipriota es interminable — no pidas entrante si vas a pedir meze", "El halloumi a la plancha comprado en el mercado cubierto y comido caliente es completamente diferente al exportado", "El commandaria se elabora desde hace 3.000 años ininterrumpidamente — la bodega KEO en Limassol hace visitas", "El norte de Nicosia tiene los precios más bajos del Mediterráneo europeo — perfecto para dormir económico"],
    "travel_styles": ["historia", "cultura", "gastronomía", "política"],
    "vibes": ["divided city", "mediterranean", "byzantine", "unique"],
    "climate": ["mediterranean"],
    "best_months": ["April", "May", "June", "September", "October", "November"],
    "budget_daily_low": 50, "budget_daily_mid": 95, "budget_daily_high": 220, "guide_quality": 8
},
{
    "slug": "luxor", "name": "Luxor", "country": "Egipto", "continent": "África", "type": "city",
    "coordinates": {"lat": 25.6872, "lng": 32.6396},
    "tagline": "El museo al aire libre más grande del mundo: Karnak, el Valle de los Reyes y el Nilo en un solo lugar",
    "intro": "Luxor es la ciudad que se asienta sobre Tebas — la capital del Imperio Nuevo egipcio, la ciudad más poderosa del mundo durante más de 500 años. Con el Templo de Karnak al norte, el Templo de Luxor en el centro y toda la necrópolis de la orilla occidental (el Valle de los Reyes, el Valle de las Reinas, los Templos de Hatshepsut y Medinet Habu), Luxor concentra la mayor acumulación de patrimonio arqueológico de cualquier ciudad del mundo.\n\nLa experiencia de Luxor a las 5am — el Nilo con niebla, los felucas con vela al amanecer y el Valle de los Reyes antes de que lleguen los tours — es de las más extraordinarias de cualquier viaje. El paseo en globo aerostático al amanecer sobre los templos del Valle es una de las experiencias visuales más únicas del planeta.\n\nA 670 km al sur de El Cairo y 225 km al norte de Asuán, Luxor es la parada central del crucero por el Nilo.",
    "when_to_go": "Octubre-abril: temperaturas de 20-28°C en el día, frescas por la noche. El verano (mayo-septiembre) alcanza 42-46°C en el Valle de los Reyes — literalmente peligroso sin preparación. El invierno (dic-feb) tiene las mejores temperaturas pero más turistas.",
    "how_to_get_there": "Aeropuerto de Luxor con vuelos directos de Europa (charters y regulares) y conexiones desde El Cairo. Tren desde El Cairo (8-9h, 200-400 EGP). Crucero por el Nilo desde Asuán (3-4 días). Calesa (hantour) del aeropuerto al hotel: 30-50 EGP (negocia).",
    "where_to_sleep": [
        {"name": "Corniche del Nilo (Este)", "description": "La orilla con todos los templos y hoteles junto al Nilo. Hotels flotantes y boutiques desde 25$. La mejor ubicación."},
        {"name": "Orilla Occidental (necrópolis)", "description": "Dormir en el lado de los muertos tiene su encanto. Guesthouses locales desde 15$, más tranquilas y auténticas."},
        {"name": "Barrio de Karnak", "description": "Al norte del Templo de Karnak, más económico. Guesthouses desde 12$/noche."}
    ],
    "what_to_do": [
        {"title": "Templo de Karnak al amanecer", "description": "El complejo religioso más grande jamás construido: 30 faraones distintos añadieron durante 2.000 años. La sala hipóstila con 134 columnas de 21m es la imagen más impresionante de Egipto (100 EGP). Llega antes de las 6am."},
        {"title": "Valle de los Reyes", "description": "Las tumbas de Tutankamón, Ramsés II, Seti I y 60 más excavadas en la roca calcárea. El ticket estándar (240 EGP) incluye 3 tumbas; Tutankamón requiere extra (150 EGP más). Llega a las 6am."},
        {"title": "Templo de Hatshepsut (Deir el-Bahari)", "description": "El templo funerario de la reina faraón Hatshepsut en tres terrazas contra el acantilado de caliza blanca es el edificio más elegante de Egipto. 100 EGP."},
        {"title": "Globo aerostático al amanecer", "description": "El vuelo en globo sobre el Valle de los Reyes al amanecer, cuando el sol ilumina el Nilo y los templos bajo la niebla, es posiblemente la mejor experiencia visual de Egipto. Desde 50-80$. Reserva con tu hotel."},
        {"title": "Crucero en feluca por el Nilo al atardecer", "description": "Un paseo en la vela de madera tradicional del Nilo al atardecer entre Luxor y la orilla occidental, con el Templo de Luxor iluminado, es la pausa más hermosa del día. 30-50 EGP la hora."},
        {"title": "Templo de Luxor de noche", "description": "El Templo de Luxor (el segundo más grande de la orilla este) iluminado de noche con los obeliscos y la avenida de esfinges es uno de los espectáculos nocturnos más impresionantes de Egipto. 100 EGP."}
    ],
    "food_and_drink": "La comida de Luxor es más sencilla que El Cairo: kushari (mezcla de arroz, lentejas, pasta y salsa de tomate picante — el street food nacional), ful medames (habas con comino y limón), ta'ameya (falafel egipcio de habas), shawarma y el pan baladi caliente. Los restaurantes del Corniche son más caros; los del barrio de Karnak tienen los mejores precios. Un almuerzo completo: 3-8$.",
    "safety": "Luxor es segura para turistas en las zonas históricas. Los vendedores y guías no oficiales pueden ser muy insistentes — aprende a decir 'la shukran' (no gracias) con firmeza. Los globos aerostáticos tienen historial de accidentes — usa empresas certificadas con buena reputación.",
    "visa_info": "Los españoles pueden obtener visa a la llegada en Egipto (25$) o e-visa online. Moneda: libra egipcia (EGP). 1€ ≈ 55 EGP.",
    "local_tips": ["El Valle de los Reyes a las 6am (apertura) tiene solo 30 minutos antes de que lleguen los primeros tours en bus — esas 30 minutos son mágicas", "El globo aerostático no es optativo si es tu única vez en Luxor — es la experiencia más extraordinaria", "La Biblia del viajero en Luxor: llega antes de las 7am a TODOS los sitios arqueológicos", "El alquiler de bicicleta para la orilla occidental (50 EGP/día) es la mejor forma de moverse entre los templos sin depender de taxis", "En todo Egipto: negocia el precio antes de subir a cualquier vehículo"],
    "travel_styles": ["historia", "arqueología", "cultura", "nilo"],
    "vibes": ["pharaonic", "nile", "ancient", "mythical"],
    "climate": ["hot desert"],
    "best_months": ["October", "November", "December", "January", "February", "March"],
    "budget_daily_low": 25, "budget_daily_mid": 60, "budget_daily_high": 180, "guide_quality": 8
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
