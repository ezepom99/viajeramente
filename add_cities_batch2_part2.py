import psycopg2
import json

conn = psycopg2.connect("dbname=viajeramente user=tenant")
cur = conn.cursor()

cities = [
# EUROPA (cont.)
{
    "slug": "valletta", "name": "La Valeta", "country": "Malta", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 35.8997, "lng": 14.5148},
    "tagline": "La capital más pequeña de la UE: barroca, amurallada y con vistas al Gran Puerto",
    "intro": "La Valeta es oficialmente la capital más pequeña de la Unión Europea — apenas 8.000 habitantes dentro de las murallas del siglo XVI, construidas por los Caballeros de Malta tras el Gran Asedio de 1565. Cada calle dentro del recinto amurallado es una bajada o subida hacia el mar, y cada esquina revela iglesias barrocas, palacios y vistas al Gran Puerto donde la historia del Mediterráneo parece suspendida en el tiempo.\n\nLo que hace especial a Malta es que todo está a escala humana: el Gran Puerto desde los jardines de Upper Barrakka, la Co-Catedral de San Juan con el Caravaggio original, el Hipódromo de los Caballeros y los Tres Ciudades al otro lado del agua son todos accesibles a pie o en ferry en menos de 30 minutos.\n\nMalta en general es una isla donde el tiempo ralentiza. El maltés es un idioma único (árabe con influencia italiana y normanda escrito en caracteres latinos). El ftira (pan maltés), el pastizzi (hojaldre de queso o guisantes) y el vino maltés son la mejor introducción.",
    "when_to_go": "Abril-junio y septiembre-noviembre: temperatura perfecta (18-26°C), mar templado y sin el agobio de julio-agosto cuando los precios se duplican. El invierno (dic-feb) es suave (12-16°C) y perfecto para visitas culturales.",
    "how_to_get_there": "Aeropuerto de Malta con conexiones directas de toda Europa. Bus X2 al centro de La Valeta (2€). Ferries desde Sicilia (Catania/Pozzallo) para quien viene del sur.",
    "where_to_sleep": [
        {"name": "La Valeta intramuros", "description": "Dentro de las murallas, con el ambiente más auténtico. Hoteles boutique desde 70€, algunas casas de carácter desde 60€."},
        {"name": "Sliema / St. Julian's", "description": "A 15 min en ferry o bus, con más opciones y ambiente más joven. Hoteles desde 50€, hostels desde 20€."},
        {"name": "Tres Ciudades (Vittoriosa)", "description": "Al otro lado del Gran Puerto, menos turístico y más auténtico. Apartamentos malteses desde 55€/noche."}
    ],
    "what_to_do": [
        {"title": "Co-Catedral de San Juan", "description": "Una de las mejores iglesias barrocas del mundo: suelo de mármol con 400 lápidas de Caballeros y dos Caravaggios originales incluyendo 'La Decapitación de San Juan Bautista' (15€)."},
        {"title": "Jardines de Upper Barrakka", "description": "El mirador más emblemático de Malta: vistas al Gran Puerto y los bastiones con el cañonazo del mediodía (gratuito). Las vistas al atardecer son extraordinarias."},
        {"title": "Hipódromo de los Caballeros (Lascaris War Rooms)", "description": "Las salas de mando subterráneas de la Segunda Guerra Mundial donde Churchill y Eisenhower coordinaron la invasión de Sicilia. Visita guiada imprescindible (10€)."},
        {"title": "Las Tres Ciudades en ferry", "description": "El ferry cruzando el Gran Puerto a Vittoriosa, Senglea y Cospicua (2,80€ ida y vuelta) es un viaje en el tiempo. Menos turístico y más auténtico que La Valeta."},
        {"title": "Templos megalíticos de Tarxien y Hagar Qim", "description": "Los templos prehistóricos de Malta (3600 a.C.) son los edificios religiosos más antiguos del mundo, más viejos que Stonehenge. UNESCO, imprescindibles."},
        {"title": "Mdina — la ciudad silenciosa", "description": "La antigua capital medieval amurallada a 15 km de La Valeta. Permanentemente tranquila, sin coches, con un café en las murallas y vistas de toda la isla."}
    ],
    "food_and_drink": "El pastizzi (hojaldre de ricotta o guisantes, 0,50€) es el snack nacional por excelencia — pruébalo en Crystal Bar. El ftira (bocadillo maltes con atún y aceitunas), el bragjoli (carne rellada) y el conejo (fenek) son imprescindibles. El vino maltés (Meridiana, Marsovin) es sorprendentemente bueno. Cena completa 20-30€.",
    "safety": "Malta es muy segura para turistas. Sin precauciones especiales.",
    "visa_info": "Malta es UE y Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: euro.",
    "local_tips": ["El pastizzi de Crystal Palace (Pjazza Regina) es el mejor de la isla y cuesta 0,50€", "El ferry al Grand Harbour Ferries conecta La Valeta con las Tres Ciudades por 2,80€ — no uses el bus", "La Ko-Catedral requiere reserva online en temporada alta — los Caravaggios son impresionantes en persona", "Mdina es la ciudad más silenciosa de Malta — visítala de mañana temprano antes de los tours", "El Karozzin (calesa histórica) en La Valeta es caro y para turistas — pásate"],
    "travel_styles": ["historia", "cultura", "playa", "arquitectura"],
    "vibes": ["baroque", "mediterranean", "knights", "island"],
    "climate": ["mediterranean"],
    "best_months": ["April", "May", "June", "September", "October", "November"],
    "budget_daily_low": 50, "budget_daily_mid": 95, "budget_daily_high": 210, "guide_quality": 8
},
{
    "slug": "zagreb", "name": "Zagreb", "country": "Croacia", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 45.8150, "lng": 15.9819},
    "tagline": "La capital croata que se descubre a pie entre museos excéntricos y cafés de mañana eterna",
    "intro": "Zagreb es la capital más ignorada de la antigua Yugoslavia y, para quien la descubre, una de las más agradables de los Balcanes. La ciudad alta (Gornji Grad) con el casco histórico medieval y el colorido tejado de la Catedral de San Esteban contrasta con la ciudad baja (Donji Grad) de arquitectura austrohúngara del siglo XIX con sus amplias avenidas y parques.\n\nLo que hace única a Zagreb son sus museos excéntricos: el Museo de las Relaciones Rotas (objetos dejados por parejas separadas de todo el mundo) es uno de los conceptos museísticos más originales del planeta. El Dolac, el mercado al aire libre de la ciudad alta, es donde se toma el café matutino con los locales.\n\nZagreb funciona muy bien como punto de partida para explorar Croacia: a 90 min de Plitvice, a 2h del mar Adriático y a 30 min de las termas de Terme Tuhelj.",
    "when_to_go": "Mayo-junio y septiembre son perfectos (20-26°C). El verano es caluroso pero agradable. El invierno (dic-feb) puede sorprender: el mercado de Adviento de Zagreb ha ganado varios años el premio al mejor de Europa.",
    "how_to_get_there": "Aeropuerto de Zagreb con conexiones europeas. Bus al centro en 25 min (7 kuna/1€). Trenes y buses internacionales desde Viena, Ljubljana, Budapest, Belgrado.",
    "where_to_sleep": [
        {"name": "Gornji Grad (Ciudad Alta)", "description": "El casco histórico medieval con el Dolac y los museos. Hoteles boutique desde 70€."},
        {"name": "Donji Grad (Ciudad Baja)", "description": "El centro austrohúngaro con los mejores cafés y arquitectura. Apartamentos desde 50€/noche."},
        {"name": "Gornji Grad / Medveščak", "description": "El barrio residencial tranquilo al norte del centro. Mejor precio-calidad para estancias largas."}
    ],
    "what_to_do": [
        {"title": "Mercado Dolac", "description": "El mercado al aire libre sobre las escaleras de la ciudad baja. Mañanas (hasta las 14h) con las mejores frutas, verduras y quesos croatas. El café de terraza aquí es el mejor ritual matutino de Zagreb."},
        {"title": "Museo de las Relaciones Rotas", "description": "Objetos cotidianos de parejas separadas de todo el mundo, con las historias detrás. Uno de los conceptos museísticos más originales del mundo (9€)."},
        {"title": "Ciudad Alta (Gornji Grad)", "description": "El barrio histórico medieval con la Catedral de San Esteban (tejado de azulejos multicolor) y la Torre Lotrščak con el cañonazo diario al mediodía."},
        {"title": "Excursión a Plitvice", "description": "El parque nacional más visitado de Croacia, a 90 min en bus, con cascadas y lagos turquesa UNESCO. Uno de los paisajes más espectaculares de Europa (30-40€ entrada según temporada)."},
        {"title": "Parque Maksimir", "description": "El parque más grande de Zagreb (316 hectáreas) con bosque, lago y el zoo. El pulmón verde de la ciudad donde corren y pasean los locales."},
        {"title": "Funicular de Zagreb", "description": "El funicular más corto del mundo (66 metros) conecta la ciudad baja con la alta por 0,66 kuna (~0,09€). Una rareza histórica operativa desde 1890."}
    ],
    "food_and_drink": "La cocina continental croata es distinta a la dálmata: štrukli (pasta con queso fresco, el plato más típico de Zagreb), purica s mlincima (pavo con pasta seca), kobasice a la plancha y burek. La escena de cafés es la mejor de los Balcanes — el 'spica' (salida del sábado a los cafés) es una institución social. Cena completa 15-25€, café 1,5€.",
    "safety": "Zagreb es muy segura. Sin precauciones especiales para turistas.",
    "visa_info": "Croacia es UE y Schengen (desde 2023). Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: euro (desde 2023).",
    "local_tips": ["El funicular más corto del mundo (66m) cuesta literalmente 0,07€ — úsalo", "El Museos de las Relaciones Rotas vale los 9€ aunque suene a gimmick — es genuinamente conmovedor", "El mercado Dolac cierra a las 14h — llega antes de las 11h para lo mejor", "El autobús a Plitvice sale de la estación de autobuses — reserva online en temporada alta", "Zagreb es perfecta para 2 noches como base para explorar Eslovenia, Hungría y la costa croata"],
    "travel_styles": ["cultura", "gastronomía", "historia", "naturaleza"],
    "vibes": ["central europe", "balkans", "coffee culture", "authentic"],
    "climate": ["continental"],
    "best_months": ["April", "May", "June", "September", "October"],
    "budget_daily_low": 40, "budget_daily_mid": 80, "budget_daily_high": 170, "guide_quality": 8
},
{
    "slug": "ljubljana", "name": "Liubliana", "country": "Eslovenia", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 46.0569, "lng": 14.5058},
    "tagline": "La capital europea más verde, con el castillo más accesible y los Alpes a la vuelta",
    "intro": "Liubliana tiene todo lo que debería tener una capital europea y no tiene la masificación que arruina otras ciudades similares: un castillo medieval sobre la ciudad, un río con terrazas de cafés, una arquitectura art nouveau del arquitecto Jože Plečnik que da personalidad única a cada puente y fuente, y todo ello a 60 minutos del lago de Bled.\n\nEslovenia es la joya verde de los Balcanes — el 60% del territorio es bosque, tiene acceso tanto al Adriático como a los Alpes, y Liubliana es su epicentro urbano accesible y bien organizado. La ciudad es perfecta para dos o tres noches pero con el lago de Bled y el parque Triglav a tan corta distancia, quedarse una semana es fácil de justificar.\n\nLa escena gastronómica ha evolucionado enormemente: el Mercado Central y los restaurantes a lo largo del Ljubljanica hacen de la ciudad una experiencia gastronómica genuina.",
    "when_to_go": "Mayo-septiembre es la ventana óptima. Junio-agosto tiene los días más largos y el lago de Bled en su máximo esplendor. Diciembre tiene mercados navideños genuinamente bonitos y la ciudad con decoración festiva elegante.",
    "how_to_get_there": "Aeropuerto de Brnik-Liubliana con conexiones europeas. Bus shutttle al centro (9€). Tren desde Viena (6h), Zagreb (2h), Venecia (3,5h). Muy bien conectada por tierra.",
    "where_to_sleep": [
        {"name": "Casco Histórico (Stare Mesto)", "description": "Junto al río y el castillo. Hoteles boutique desde 80€, apartamentos desde 65€/noche."},
        {"name": "Krakovo / Trnovo", "description": "El barrio más bohemio y local, a 10 min del centro. Cafés excelentes, mercado de productores. Más económico."},
        {"name": "BTC / Šiška", "description": "Zona moderna al norte, con los mejores hostels (desde 18€) y apartamentos económicos."}
    ],
    "what_to_do": [
        {"title": "Castillo de Liubliana", "description": "El castillo sobre la colina central se sube a pie (15 min) o en funicular (4€). Vistas de la ciudad y los Alpes Julianos en días despejados. Museo de historia eslovena en el interior."},
        {"title": "Puentes de Plečnik y paseo fluvial", "description": "El Triple Puente, el Puente del Zapatero y el Mercado al aire libre a orillas del Ljubljanica son el legado del arquitecto Plečnik — una ciudad diseñada como una obra de arte."},
        {"title": "Mercado Central y Mercado de Productores", "description": "El mercado junto al río (mañanas, de martes a domingo) tiene los mejores produktos de Eslovenia: queso tolminc, jamón de Karst, miel de abeto y aceite de oliva istriano."},
        {"title": "Lago de Bled en excursión de día", "description": "A 60 km (1h en bus o coche), el lago de Bled con la isla y el castillo es uno de los paisajes más icónicos de Europa. Nada o alquila una barquita (15€/h)."},
        {"title": "Metelkova — zona autónoma", "description": "El barrio autónomo en una antigua cuartel militar es el epicentro de la cultura underground de Liubliana: galerías, bares alternativos y conciertos."},
        {"title": "Cueva de Postojna en excursión", "description": "A 60 km, las cuevas de Postojna (27 km de galerías, train dentro) y el Castillo de Predjama (medieval construido en una cueva) son un día completo espectacular."}
    ],
    "food_and_drink": "La cocina eslovena mezcla influencias centroeuropeas, mediterráneas y balcánicas: potica (rollito de nueces dulce, el postre nacional), štruklji (pasta rellena dulce o salada), kranjska klobasa (salchicha de Carniola) y el excelente vino esloveno de Primorska. Los restaurantes del paseo fluvial son más caros (20-35€); los del barrio Krakovo más auténticos y económicos.",
    "safety": "Liubliana es una de las ciudades más seguras de Europa. Sin incidentes para turistas.",
    "visa_info": "Eslovenia es UE y Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: euro.",
    "local_tips": ["El lago de Bled es de las excursiones más bonitas de Europa — no te lo saltes", "La potica de nueces (pastel nacional) se vende en panaderías locales — pruébala", "El Metelkova empieza animarse tarde (23h+) pero es uno de los barrios alternativos más auténticos del continente", "El mercado del sábado tiene los mejores productores — llega antes de las 10h", "Liubliana es una de las capitales más ciclables de Europa — alquila una bici para moverte"],
    "travel_styles": ["naturaleza", "cultura", "arquitectura", "gastronomía"],
    "vibes": ["green", "alpine", "bohemian", "compact"],
    "climate": ["continental", "mild"],
    "best_months": ["May", "June", "July", "August", "September"],
    "budget_daily_low": 50, "budget_daily_mid": 95, "budget_daily_high": 200, "guide_quality": 8
},
# ASIA
{
    "slug": "beirut", "name": "Beirut", "country": "Líbano", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 33.8938, "lng": 35.5018},
    "tagline": "La Fénix del Mediterráneo: cosmopolita, resiliente y con la mejor gastronomía del Oriente Medio",
    "intro": "Beirut es una ciudad que ha sido destruida y reconstruida varias veces y cada vez resurge con más energía. El barrio de Gemmayzeh y Mar Mikhael concentran una escena de cafés, restaurantes y galerías que rivaliza con cualquier capital europea. El horizonte mezcla rascacielos modernos, edificios baleados de la guerra civil que nadie ha derribado y mezquitas junto a iglesias maronitas.\n\nLa gastronomía libanesa es la mejor del Oriente Medio sin discusión: hummus, kibbeh, fattoush, shawarma auténtico, mezze infinito y el arak (licor de anís) son una religión local. El precio de comer bien en Beirut es sorprendentemente bajo — los restaurantes locales son accesibles incluso con la crisis económica que atraviesa el país.\n\nATENCIÓN: Beirut vive una crisis económica y política severa desde 2019. Consulta el estado del país antes de viajar. La situación puede cambiar rápidamente.",
    "when_to_go": "Primavera (marzo-mayo) y otoño (sept-nov) son los mejores momentos: clima mediterráneo perfecto (20-26°C). El verano es caluroso y húmedo pero la ciudad está en su máximo social. El invierno permite esquiar en las montañas del Líbano (a 45 min de Beirut).",
    "how_to_get_there": "Aeropuerto Internacional de Beirut con conexiones de Medio Oriente, Europa y África. Taxi del aeropuerto al centro: negociar precio (no hay metro ni bus oficial eficiente).",
    "where_to_sleep": [
        {"name": "Gemmayzeh / Mar Mikhael", "description": "El barrio más animado con los mejores bares y restaurantes. Boutique hotels desde 60$, apartamentos desde 45$"},
        {"name": "Hamra", "description": "El barrio universitario y cosmopolita, más económico. Hostels desde 18$, hoteles desde 40$."},
        {"name": "Achrafieh", "description": "El barrio cristiano con el ambiente más seguro y animado. Hoteles desde 55$."}
    ],
    "what_to_do": [
        {"title": "Barrios Gemmayzeh y Mar Mikhael", "description": "El corazón de la escena cultural de Beirut: galerías de arte, bares de autor, restaurantes locales y edificios otomanos y franceses restaurados. El mejor paseo de la ciudad."},
        {"title": "Corniche al atardecer", "description": "El paseo marítimo donde Beirut se despoja de sus tensiones: familias, parejas, vendedores de maíz y el sol poniéndose sobre el Mediterráneo."},
        {"title": "Barrio de Achrafieh y Notre-Dame du Liban", "description": "El barrio histórico cristiano con calles bohemias, las mejores tiendas de segunda mano y la ciudad más antigua de Beirut."},
        {"title": "Museo Nacional de Beirut", "description": "La colección arqueológica más importante del Líbano: sarcófagos fenicios, mosaicos romanos y bronces medievales. Imprescindible para entender el país (5$)."},
        {"title": "Excursión a Byblos", "description": "A 40 km, una de las ciudades habitadas más antiguas del mundo con puerto fenicio, castillo cruzado y centro histórico perfectamente preservado."},
        {"title": "Gastronomía y mezze", "description": "El mezze libanés (20-30 platos pequeños) en un restaurante local es una de las mejores experiencias gastronómicas del Mediterráneo. Em Sherif y Tawlet son los mejores."}
    ],
    "food_and_drink": "El hummus libanés, el kibbeh (carne picada con bulgur), el shawarma de falda, el tabbouleh auténtico (con más perejil que trigo), el fattoush y la kunafeh (postre de queso) son incomparables. Un mezze completo para dos: 25-40$. El arak con agua y hielo es el aperitivo nacional.",
    "safety": "Beirut tiene zonas con diferente nivel de seguridad. Gemmayzeh, Hamra y Achrafieh son seguros para turistas. Evita las zonas del sur (Dahieh, frontera con Israel) y consulta avisos del gobierno antes de viajar. La situación política es volátil.",
    "visa_info": "Los ciudadanos españoles pueden obtener visa a la llegada (30 días, gratuita para turismo). Con sello israelí en el pasaporte la entrada está prohibida. Consulta la situación actual antes de viajar.",
    "local_tips": ["Negocia siempre el precio del taxi antes de subir — no hay taxímetro", "El arak se sirve con agua y hielo — nunca solo — y cambia completamente de sabor", "Las mejores hummus de la ciudad están en Ali Baba (Hamra) o Falafel Sahyoun", "Cambia dinero en casas de cambio — los dólares americanos son la moneda de facto", "La situación puede cambiar rápido — registra tu viaje en la embajada española"],
    "travel_styles": ["gastronomía", "cultura", "historia", "urbano"],
    "vibes": ["mediterranean", "cosmopolitan", "resilient", "nightlife"],
    "climate": ["mediterranean"],
    "best_months": ["March", "April", "May", "September", "October", "November"],
    "budget_daily_low": 35, "budget_daily_mid": 75, "budget_daily_high": 180, "guide_quality": 8
},
{
    "slug": "amman", "name": "Ammán", "country": "Jordania", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 31.9539, "lng": 35.9106},
    "tagline": "La puerta al Wadi Rum y Petra, con una escena gastronómica árabe que sorprende",
    "intro": "Ammán es la puerta de entrada a Jordania y uno de los destinos del Oriente Medio más accesibles y seguros. Construida sobre siete colinas, la ciudad mezcla el Ammán antiguo de Jabal al-Qalaa (la ciudadela) con el barrio moderno y cosmopolita de Abdali y el hub gastronómico de Rainbow Street y Weibdeh.\n\nLa mayoría usa Ammán como escala para Petra, el Wadi Rum y el Mar Muerto, pero la ciudad merece al menos dos días propios. La gastronomía jordana — mansaf, falafel, mezze árabe — es excelente y el café de cardamomo es una constante social. El barrio de Rainbow Street con sus cafés, librerías y vistas del casco antiguo es uno de los más agradables del Oriente Medio.\n\nJordania es estable y segura en el contexto regional, con una hospitalidad genuina que hace los intercambios con locales especialmente agradables.",
    "when_to_go": "Marzo-mayo y septiembre-noviembre son perfectos (20-26°C). El verano puede ser muy caluroso (36°C+) y el invierno frío (5-15°C) con lluvia ocasional. Evita el Ramadán si quieres plena apertura de restaurantes.",
    "how_to_get_there": "Aeropuerto Internacional de Amman (Queen Alia) con conexiones de Europa y el Oriente Medio. Bus al centro en 45 min (3 JOD). Taxis abundantes. JETT bus a Petra (5h, 12 JOD).",
    "where_to_sleep": [
        {"name": "Rainbow Street / Weibdeh", "description": "El barrio más animado y turístico con vistas al casco antiguo. Hostels desde 10 JOD, hoteles desde 30 JOD."},
        {"name": "Downtown (Balad)", "description": "El centro histórico más antiguo, ruidoso y auténtico. Cercano a la ciudadela y mercados. Hoteles económicos."},
        {"name": "Abdali / Shmeisani", "description": "El barrio moderno y bien equipado. Hoteles internacionales desde 50 JOD."}
    ],
    "what_to_do": [
        {"title": "Ciudadela de Ammán (Jabal al-Qalaa)", "description": "La colina histórica con el Templo de Hércules romano, el Palacio Omeya y el Museo Arqueológico de Jordania. Las vistas del anfiteatro romano de abajo son espectaculares (3 JOD)."},
        {"title": "Anfiteatro Romano", "description": "El teatro del siglo II con capacidad para 6.000 espectadores, perfectamente conservado en el corazón de la ciudad antigua. Gratuito."},
        {"title": "Barrio Rainbow Street y Weibdeh", "description": "Las dos calles con más ambiente de Ammán: cafés, librerías, galerías y vistas del downtown. El alma cosmopolita de la ciudad moderna."},
        {"title": "Excursión a Petra (día completo)", "description": "El tesoro nabateo a 3h en bus es la razón principal de muchos viajes a Jordania. El Siq, el Tesoro y el Monasterio requieren al menos un día completo (50 JOD entrada)."},
        {"title": "Mar Muerto (excursión de día)", "description": "A 70 km, el punto más bajo de la Tierra a -430m. Flotar en las aguas hipersalinas es una experiencia única. Acceso a playas públicas desde 20 JOD."},
        {"title": "Mercado de Al-Balad", "description": "El zoco del centro histórico con especias, oro, ropa y el mejor ambiente local. La calle Al-Hashemi concentra los mejores falafel de la ciudad (0,20 JOD por unidad)."}
    ],
    "food_and_drink": "El mansaf (cordero en salsa de yogur fermentado con arroz) es el plato nacional. El falafel y el hummus de Ammán son de otro nivel. El knafeh (postre de queso y sémola con sirope de rosas) en Habibah es el mejor dulce de la región. Cena local 5-12 JOD. Café árabe con cardamomo: gratuito en la mayoría de establecimientos (señal de hospitalidad).",
    "safety": "Ammán es una de las ciudades más seguras del Oriente Medio para turistas. Jordan es considerada excepcionalmente estable en su contexto regional. Mujeres: dressing conservador fuera de Rainbow Street.",
    "visa_info": "España puede obtener visa a la llegada (40 JOD) o el Jordan Pass (desde 70 JOD incluye visa + Petra). El Jordan Pass es la opción más inteligente si visitas el país más de 3 noches.",
    "local_tips": ["El Jordan Pass incluye visa + Petra y muchos otros sitios — compra online antes de llegar", "El falafel de Al-Quds (Downtown) o los de la calle Al-Hashemi son los mejores de la ciudad por 0,20 JOD", "Negocia el taxi antes de subir o pide Uber/Careem (funciona bien en Ammán)", "El café árabe con cardamomo es una señal de hospitalidad — aceptarlo siempre con la mano derecha", "El Wadi Rum de noche bajo las estrellas es una de las experiencias más intensas de Oriente Medio"],
    "travel_styles": ["historia", "cultura", "gastronomía", "aventura"],
    "vibes": ["middle east", "ancient", "cosmopolitan", "gateway"],
    "climate": ["semi-arid", "hot summers"],
    "best_months": ["March", "April", "May", "September", "October", "November"],
    "budget_daily_low": 30, "budget_daily_mid": 65, "budget_daily_high": 150, "guide_quality": 8
},
{
    "slug": "muscat", "name": "Mascate", "country": "Omán", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 23.5880, "lng": 58.3829},
    "tagline": "El Oriente Medio que no esperabas: tranquilo, limpio y con desiertos y wadis a la puerta",
    "intro": "Mascate es la capital más subestimada del Oriente Medio. Mientras Dubái compite en altura y Riad se moderniza a marchas forzadas, Mascate ha decidido preservar su identidad omaní: arquitectura de estilo árabe clásico (ningún edificio supera los seis pisos en el centro), mercados tradicionales de incienso y plata, una corniche con dhows (barcos de madera árabes) y acceso en 30 minutos a wadis (cañones con agua), dunas de arena y montañas de 3.000 metros.\n\nOmán es el país árabe más abierto y tolerante de la Península. Las mujeres no están obligadas a cubrirse y el alcohol está disponible en hoteles y algunos restaurantes. La hospitalidad omaní es genuina — que un desconocido te invite a café es perfectamente normal.\n\nMascate no tiene la escena de vida nocturna de Dubái pero tiene algo más valioso: autenticidad y naturaleza extraordinaria accesibles sin coche de lujo.",
    "when_to_go": "Octubre-marzo es la ventana ideal: temperaturas de 22-30°C. El verano (mayo-septiembre) es prohibitivo con 40-45°C y humedad extrema. El monzón (junio-septiembre en Salalah, al sur) es el momento opuesto.",
    "how_to_get_there": "Aeropuerto Internacional de Mascate con conexiones de Europa y Asia. Oman Air tiene vuelos directos desde Madrid y Barcelona. Taxi al centro (15 OMR fijo, ~35€).",
    "where_to_sleep": [
        {"name": "Muttrah", "description": "El corazón histórico junto al puerto con el mejor zoco. Hoteles desde 30 OMR/noche."},
        {"name": "Ruwi / CBD", "description": "El barrio de negocios con buenos hoteles de precio medio. Desde 25 OMR/noche."},
        {"name": "Qantab / Al Mouj", "description": "Los barrios costeros modernos con acceso a playas y hoteles de lujo."}
    ],
    "what_to_do": [
        {"title": "Muttrah Souq", "description": "El mercado histórico del puerto es uno de los mejores zocos de Arabia: incienso de Dhofar, plata omaní, khanjars (dagas curvas) y textiles. Mejor de noche cuando el ambiente es más fresco."},
        {"title": "Gran Mezquita del Sultán Qaboos", "description": "Una de las mezquitas más grandes del mundo, accesible a no-musulmanes por la mañana (excepto viernes). El alfombra persa del interior es la segunda más grande del mundo (4 OMR)."},
        {"title": "Corniche y puerto de Muttrah", "description": "El paseo marítimo con los dhows anclados al amanecer es la postal más auténtica de Mascate. El mercado de pescado matutino junto al puerto es espectacular."},
        {"title": "Wadi Shab (excursión de día)", "description": "A 150 km, el cañón con agua turquesa que termina en una cueva con cascada es uno de los lugares más espectaculares de Omán. Alquila coche o únete a un tour (30-40€)."},
        {"title": "Fuerte de Bahla y Nizwa", "description": "La antigua capital de Omán a 165 km con el mejor zoco de plata del país y el fuerte más grande de la Península Arábiga. Excursión de día imprescindible."},
        {"title": "Bañarse en las playas de Qantab", "description": "Las calas de piedra caliza blanca en la costa de Mascate son perfectas para nadar y hacer snorkel. Completamente gratuitas y pocas veces masificadas."}
    ],
    "food_and_drink": "El shuwa (cordero marinado cocinado bajo tierra durante 24h, plato nacional) es excepcional. El salmón al hasbah (arroz con especias y carne), el halwa omaní (dulce de rosas y cardamomo) y el kahwa (café árabe) son imprescindibles. Los restaurantes indios son los más asequibles (4-8 OMR). Alcohol solo en hoteles (10-15 OMR/copa).",
    "safety": "Omán es uno de los países más seguros del mundo. Sin precauciones especiales para turistas.",
    "visa_info": "Los españoles pueden obtener e-visa online antes de viajar (20 OMR) o visa a la llegada para turismo. Moneda: rial omaní (OMR). 1 OMR ≈ 2,40€.",
    "local_tips": ["Alquila un coche — Omán es uno de los países más seguros para conducir en el Oriente Medio y abre todo el país", "El Wadi Shab requiere hidratarse bien y llevar ropa que se pueda mojar", "El khanja (daga curva) de plata es el mejor souvenir pero verifica autenticidad", "Los supermercados Lulu tienen todo a precios razonables", "Conducir al anochecer en zonas de montaña puede tener camelos salvajes — precaución"],
    "travel_styles": ["naturaleza", "cultura", "aventura", "historia"],
    "vibes": ["arabian", "authentic", "desert", "coastal"],
    "climate": ["hot arid desert"],
    "best_months": ["October", "November", "December", "January", "February", "March"],
    "budget_daily_low": 45, "budget_daily_mid": 90, "budget_daily_high": 220, "guide_quality": 8
},
{
    "slug": "doha", "name": "Doha", "country": "Catar", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 25.2854, "lng": 51.5310},
    "tagline": "El futuro del Golfo Pérsico: arquitectura de vanguardia, el mejor museo del Oriente Medio y el zoco más auténtico",
    "intro": "Doha se ha transformado en tres décadas de aldea pesquera a ciudad global con el skyline más ambicioso del Oriente Medio. Lo que sorprende a quien llega con prejuicios es que junto a los rascacielos tiene el Souq Waqif, el mercado restaurado más auténtico de la Península, donde los locales compran especias y las cafeterías sirven té con cardamomo.\n\nEl Museo de Arte Islámico de Doha, diseñado por I.M. Pei, es uno de los mejores museos del mundo — la colección de arte islámico abarca desde España hasta Indonesia a lo largo de 14 siglos. El nuevo Museo Nacional de Catar (Jean Nouvel) es otro espectáculo arquitectónico.\n\nDoha es cara para comer y beber en restaurantes occidentales, pero el Souq y la comida árabe e india son sorprendentemente asequibles. El alcohol está disponible solo en hoteles.",
    "when_to_go": "Noviembre-marzo: la única ventana cómoda (20-28°C). El resto del año el calor es prohibitivo (40-50°C en verano). El Mundial de Fútbol fue en noviembre-diciembre 2022 y activó infraestructura turística permanente.",
    "how_to_get_there": "Aeropuerto de Hamad, uno de los mejores del mundo y hub de Qatar Airways. Metro desde el aeropuerto al centro en 25 min (2 QAR). Escala perfecta entre Europa y Asia.",
    "where_to_sleep": [
        {"name": "Souq Waqif / Msheireb", "description": "El centro histórico revivido, junto al mejor mercado. Hoteles boutique desde 150 QAR/noche."},
        {"name": "West Bay / Corniche", "description": "El barrio de rascacielos junto al mar. Hoteles internacionales desde 200 QAR, algunas opciones más económicas."},
        {"name": "Al Sadd", "description": "Barrio residencial con hoteles económicos para la zona (desde 120 QAR) y buenos restaurantes indios y libaneses."}
    ],
    "what_to_do": [
        {"title": "Museo de Arte Islámico", "description": "La colección de arte islámico más completa del mundo en un edificio de I.M. Pei sobre el agua. 14 siglos de arte desde Marruecos hasta Indonesia. Gratuito — probablemente el mejor gratuito del Golfo."},
        {"title": "Souq Waqif", "description": "El mercado tradicional restaurado con laberintos de calles cubiertas, especias, halcones (la cetrería es deporte nacional), textiles y los mejores cafés árabes con shisha de la ciudad."},
        {"title": "Corniche de Doha al atardecer", "description": "El paseo marítimo de 7km frente al skyline del West Bay es el paseo más impresionante del Golfo. El anfiteatro al aire libre tiene eventos culturales gratuitos."},
        {"title": "Museo Nacional de Qatar", "description": "El edificio de Jean Nouvel (pétalos del desierto de hormigón) es ya icónico. La narrativa de la historia y cultura de Catar es exhaustiva y bien presentada (50 QAR)."},
        {"title": "Katara Cultural Village", "description": "El barrio cultural con anfiteatro griego (escala 1:1), galerías, restaurantes y el Katara Beach. El espacio más auténtico del Doha no-comercial."},
        {"title": "Excursión al desierto de Khor Al Adaid", "description": "El 'mar interior' de Catar — las dunas del desierto llegando directamente al golfo. Tours de 4x4 desde 60 QAR, una de las experiencias más únicas de la Península."}
    ],
    "food_and_drink": "El machboos (arroz con carne y especias, el plato nacional), el harees (trigo con cordero molido) y el jareesh (gachas con cordero) son lo mejor de la cocina catarí. El Souq Waqif tiene los mejores restaurantes locales (20-40 QAR). Los restaurantes indios de Al Sadd son los más económicos (15-25 QAR). Alcohol solo en hoteles de lujo (50-80 QAR/copa).",
    "safety": "Doha es extremadamente segura. Sin precauciones especiales para turistas. Código de vestimenta conservador en espacios públicos.",
    "visa_info": "Los españoles pueden obtener visa gratuita a la llegada o e-visa online. Qatar Airways Stopover ofrece visados de 96h gratuitos si vuelas con su aerolínea. Moneda: rial catarí (QAR). 1€ ≈ 4 QAR.",
    "local_tips": ["El Museo de Arte Islámico es gratuito y de nivel mundial — no lo saltes aunque no seas fan de los museos", "Qatar Airways Stopover puede incluir hotel gratuito si haces escala — comprueba antes de reservar", "El metro de Doha funciona perfectamente y es barato — las tarjetas se compran en las estaciones", "Viste con respeto en el Souq y espacios públicos — hombros y rodillas cubiertos", "La visa a la llegada es gratuita para españoles — no necesitas tramitarla antes"],
    "travel_styles": ["cultura", "arquitectura", "historia", "diseño"],
    "vibes": ["gulf", "modern", "islamic", "stopover"],
    "climate": ["hot arid desert"],
    "best_months": ["November", "December", "January", "February", "March"],
    "budget_daily_low": 60, "budget_daily_mid": 130, "budget_daily_high": 350, "guide_quality": 8
},
{
    "slug": "dhaka", "name": "Daca", "country": "Bangladesh", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 23.8103, "lng": 90.4125},
    "tagline": "El caos y la vitalidad de una megaciudad que pocos viajeros se atreven a explorar",
    "intro": "Daca es la megaciudad más densa del mundo — 23 millones de personas en un área donde el espacio es una quimera. Los rickshaws de colores saturan cada calle, el mercado de Sadarghat en el río Buriganga tiene el tráfico fluvial más intenso de Asia y el Old Dhaka guarda arquitecturas mogoles y palacios olvidados entre tendencias de ropa y especias.\n\nVisitar Daca requiere paciencia, apertura mental y disposición para perderse. No tiene las facilidades de Bangkok o Katmandú, pero tiene algo que esas ciudades han perdido: una autenticidad sin filtro que pocos destinos en el mundo pueden ofrecer. Los viajeros que pasan por Bangladesh suelen recordarlo como uno de sus viajes más intensos.\n\nBangladesh es uno de los países más baratos del mundo para viajar. Un día completo con alojamiento, transporte y comida puede costar menos de 20€.",
    "when_to_go": "Noviembre-febrero: la única ventana seca y soportable (20-28°C). El resto del año, el monzón (junio-octubre) inunda parte de la ciudad y el calor pre-monzón (marzo-mayo) es agotador.",
    "how_to_get_there": "Aeropuerto Internacional de Hazrat Shahjalal con conexiones de Asia y el Golfo. Vuelos indirectos desde Europa (Doha, Dubái, Delhi como hubs). Taxi al centro en 30-60 min.",
    "where_to_sleep": [
        {"name": "Gulshan / Banani", "description": "El barrio diplomático y más internacional, con los mejores hoteles (40-80$) y restaurantes seguros."},
        {"name": "Motijheel", "description": "El centro de negocios, más económico pero ruidoso. Hoteles locales desde 15$."},
        {"name": "Old Dhaka", "description": "La ciudad vieja, inmersión total pero básica. Solo para viajeros experimentados. Guesthouses desde 10$."}
    ],
    "what_to_do": [
        {"title": "Sadarghat River Terminal", "description": "El puerto fluvial más concurrido de Asia: cientos de ferrys y lanchitas cruzando el Buriganga cada hora. Toma un bote (50 taka) para una hora en el agua."},
        {"title": "Old Dhaka — Shakhari Bazar y Chawk Bazar", "description": "El barrio histórico con el mercado de especias más grande de Bangladesh, los concheros de Shakhari Bazar y la arquitectura mogol y británica mezclada."},
        {"title": "Mezquita de Baitul Mukarram", "description": "La mezquita nacional de Bangladesh con capacidad para 40.000 personas, en el centro de la ciudad. Arquitectura modernista inesperada."},
        {"title": "Museo Nacional de Bangladesh", "description": "La colección más completa sobre historia y arte de Bangladesh, desde los períodos hinduista y budista hasta el siglo XX. Barato y bien organizado."},
        {"title": "Excursión a Sonargaon", "description": "La antigua capital del sultanato medieval de Bangla, a 29 km. El Panam City — una calle de mansiones coloniales en ruinas — es uno de los lugares más atmosféricos de Bangladesh."},
        {"title": "Cocina callejera de Old Dhaka", "description": "El biryani de Old Dhaka (especialmente en Haji Biriyani) y los iftar snacks de Chawk Bazar son legendarios en toda Asia del Sur."}
    ],
    "food_and_drink": "La cocina de Bangladesh es la hermana menor de la india con más énfasis en pescado de río: hilsa al curry (el pez nacional), biryani al estilo Dhaka con carne y especias aromáticas, pitha (pasteles de arroz) y el té con leche espeso. Una comida completa cuesta 1-3€. El biryani de Haji Mohammad Ali Road es el más famoso del país.",
    "safety": "Daca tiene zonas de diferente nivel de seguridad. El barrio de Gulshan/Banani es el más seguro para turistas. El Old Dhaka requiere más atención, especialmente de noche. Las movilizaciones políticas pueden interrumpir el tráfico. Evita zonas de conflicto y mantén el registro consular.",
    "visa_info": "Los españoles necesitan visa previa. Solicita e-visa online (al menos 2 semanas antes, 51$). Bangladesh es técnicamente abierto al turismo pero los trámites pueden ser complicados.",
    "local_tips": ["Negocia siempre el precio del rickshaw antes — los conductores son honestos pero cobran precio turista", "El Haji Biriyani de Old Dhaka es el biryani más famoso del país — merece el desvío", "El metro de Dhaka abrió en 2022 y cubre el corredor norte-sur — un alivio en el tráfico", "Lleva papel de baño y desinfectante de manos — esencial en la ciudad vieja", "Los bangladesíes son extremadamente curiosos y amistosos con los extranjeros — las conversaciones espontáneas son parte de la experiencia"],
    "travel_styles": ["aventura", "cultura", "budget", "inmersión"],
    "vibes": ["intense", "authentic", "south asia", "urban chaos"],
    "climate": ["tropical monsoon"],
    "best_months": ["November", "December", "January", "February"],
    "budget_daily_low": 15, "budget_daily_mid": 35, "budget_daily_high": 90, "guide_quality": 8
},
{
    "slug": "phnom-penh", "name": "Phnom Penh", "country": "Camboya", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 11.5564, "lng": 104.9282},
    "tagline": "La capital renacida de Camboya: historia dolorosa, futuro vibrante y el Mekong al lado",
    "intro": "Phnom Penh tiene una capa de historia que pesa. El Museo del Genocidio de Tuol Sleng (S-21) y los Campos de la Muerte de Choeung Ek son los recuerdos más presentes del Khmer Rouge, y entender Camboya es imposible sin enfrentarse a esa historia. Pero Phnom Penh de 2024 es también una ciudad que mira hacia adelante con una escena gastronómica y cultural en pleno despegue.\n\nEl Palacio Real con sus tejados dorados junto al río, el mercado central (Phsar Thmei) con su cúpula art déco, el barrio ribereño de Riverside con sus cafés y el vecindario de Tuol Tom Poung (Russian Market) con los mejores precios de ropa en toda Asia componen una ciudad con más capas de lo que sugiere su tamaño.\n\nPhnom Penh es más asequible que Bangkok y mucho menos turístico que Siem Reap, con mejor gastronomía que ambas.",
    "when_to_go": "Noviembre-marzo: la estación seca, temperaturas de 25-32°C. Enero y febrero son los más frescos. El monzón (junio-octubre) transforma la ciudad — el Tonle Sap invierte su flujo y el paisaje es espectacular pero húmedo.",
    "how_to_get_there": "Aeropuerto Internacional de Phnom Penh con conexiones de Bangkok, HCMC, Kuala Lumpur y Singapur. Tuk-tuk del aeropuerto: 7-12$. Ferries desde Vietnam por el Mekong (experiencia única pero lenta).",
    "where_to_sleep": [
        {"name": "Riverside / BKK1", "description": "El barrio turístico central junto al río. Hostels desde 5$, hoteles boutique desde 25$."},
        {"name": "Boeung Keng Kang (BKK1)", "description": "El barrio más agradable y moderno, con los mejores restaurantes y cafés. Apartamentos desde 20$/noche."},
        {"name": "Toul Tom Poung (Russian Market)", "description": "El barrio más auténtico, junto al mejor mercado. Opciones económicas desde 10$."}
    ],
    "what_to_do": [
        {"title": "Museo del Genocidio Tuol Sleng (S-21)", "description": "El centro de detención y tortura del Khmer Rouge, convertido en museo de la memoria. Emocionalmente devastador e históricamente imprescindible (5$)."},
        {"title": "Campos de la Muerte de Choeung Ek", "description": "A 15 km del centro, el memorial donde fueron ejecutadas más de 17.000 personas. La audioguía (narrada por sobrevivientes) es una de las experiencias más impactantes posibles (6$)."},
        {"title": "Palacio Real y Templo de la Plata", "description": "El palacio oficial del rey con el Templo de la Plata (suelo de 5.000 baldosas de plata maciza) y la esmeralda Buda. El conjunto es extraordinario (10$)."},
        {"title": "Mercado Central (Phsar Thmei)", "description": "La cúpula art déco amarilla de 1937 alberga uno de los mejores mercados de joyería y textiles de Asia. Los precios requieren regateo."},
        {"title": "Russian Market (Toul Tom Poung)", "description": "El mejor mercado para ropa de marca excedente de fábrica, antigüedades jemeres y souvenirs auténticos. Los domingos es la mejor mañana."},
        {"title": "Ribera del Mekong al atardecer", "description": "El paseo junto al Tonle Sap y el Mekong al caer el sol, con los templos dorados del Palacio Real al fondo, es el mejor momento del día en Phnom Penh."}
    ],
    "food_and_drink": "La cocina jemer es más sutil que la thai: amok (curry en hoja de banana), lok lak (carne salteada con pimienta verde de Kampot), nom banh chok (fideos de arroz con curry verde matutino) y el samlor (sopa jemer). El barrio BKK1 tiene excelentes restaurantes modernos (8-18$). Los mercados tienen comida por 2-4$.",
    "safety": "Phnom Penh ha mejorado mucho en seguridad. Los robos de mochila desde moto son el principal problema en el Riverside. Por la noche, Riverside y BKK1 son seguros. Evita sacar el teléfono en la calle en zonas poco transitadas.",
    "visa_info": "Los españoles pueden obtener e-visa online (36$, válida 30 días) o visa a la llegada en el aeropuerto. Se puede extender en Phnom Penh fácilmente.",
    "local_tips": ["El tuk-tuk compartido PassApp es la forma más honesta de moverse — evita negociar precio con desconocidos", "El S-21 y los Campos de la Muerte requieren preparación emocional — ve por la mañana", "El mercado ruso tiene los mejores precios en ropa pero requiere regateo", "La pimienta de Kampot (verde o negra) es el mejor souvenir gastronómico de Camboya", "Combina Phnom Penh con al menos 2 noches en Siem Reap para los templos de Angkor"],
    "travel_styles": ["historia", "cultura", "budget", "gastronomía"],
    "vibes": ["mekong", "dark history", "resilient", "emerging"],
    "climate": ["tropical monsoon"],
    "best_months": ["November", "December", "January", "February", "March"],
    "budget_daily_low": 18, "budget_daily_mid": 40, "budget_daily_high": 100, "guide_quality": 8
},
{
    "slug": "yangon", "name": "Rangún", "country": "Myanmar", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 16.8661, "lng": 96.1951},
    "tagline": "La pagoda dorada más grande del mundo y una ciudad que el tiempo ha preservado por accidente",
    "intro": "Rangún es la gran ciudad de Asia que menos cambios ha experimentado en el siglo XX — precisamente porque el régimen militar mantuvo al país cerrado durante décadas. El resultado accidental es una ciudad con más arquitectura colonial británica intacta que cualquier otra en la región, mercados de otra época y una espiritualidad budista omnipresente.\n\nLa Pagoda Shwedagon es el punto de llegada: una estupa de 98 metros cubierta de oro auténtico (más de 60 toneladas) que brilla sobre toda la ciudad. No es una ruina histórica — es un templo vivo donde monjes y laicos conviven en una atmósfera que no existe en ningún otro lugar.\n\nATENCIÓN: Myanmar atraviesa una crisis política grave desde el golpe militar de 2021. Consulta la situación actual y los consejos de viaje de tu gobierno antes de planificar cualquier visita.",
    "when_to_go": "Noviembre-febrero: la estación seca y más fresca (25-32°C). El monzón (mayo-octubre) hace la ciudad más verde pero las lluvias pueden ser intensas. Marzo-abril es muy caluroso (38°C+).",
    "how_to_get_there": "Aeropuerto Internacional de Yangon con conexiones de Bangkok, Singapur y Kuala Lumpur. Bus local al centro (200 kyat). Taxi: 7-12$. CONSULTA SITUACIÓN POLÍTICA ANTES DE VOLAR.",
    "where_to_sleep": [
        {"name": "Downtown colonial", "description": "El centro con la mayor concentración de arquitectura colonial. Hoteles boutique desde 35$, hostels desde 10$."},
        {"name": "Bahan / Shwedagon", "description": "El barrio residencial cerca de la pagoda. Más tranquilo y con mejores opciones de precio medio."},
        {"name": "Dagon / Chinatown", "description": "El barrio chino con la comida más asequible y el ambiente más animado."}
    ],
    "what_to_do": [
        {"title": "Pagoda Shwedagon", "description": "La pagoda más sagrada de Myanmar: 98 metros de altura cubiertos de oro y piedras preciosas reales. Visita al amanecer para ver a los monjes rezando (8$ entrada para extranjeros)."},
        {"title": "Arquitectura colonial del Downtown", "description": "El paseo por las calles del centro histórico revela más edificios victorianos y eduardianos que cualquier otra ciudad de Asia. El antiguo secretariado (en restauración) es el más impresionante."},
        {"title": "Mercado de Bogyoke Aung San (Scott Market)", "description": "El mejor mercado cubierto de Rangún: joyería de rubíes y jade, lacas birmanas, sombrillas de papel y textiles. El rubí birmano es el más valorado del mundo."},
        {"title": "Templo de Sule Pagoda", "description": "La pagoda en el centro mismo de la ciudad, rodeada de tráfico, con más de 2.000 años de historia. Gratis para locales, 2$ para turistas."},
        {"title": "Paseo en el tren circular de Rangún", "description": "El tren de vía estrecha que rodea toda la ciudad en 3 horas cuesta 200 kyat. La mejor manera de ver barrios locales fuera del circuito turístico."},
        {"title": "Mercado nocturno de Chinatown (19th Street)", "description": "La calle de barbacoas nocturnas en el barrio chino, con carne a la brasa, seafood y shan noodles. El ambiente callejero más auténtico de la ciudad."}
    ],
    "food_and_drink": "La cocina birmana es una de las más desconocidas de Asia: mohinga (sopa de fideos de arroz con pescado, el desayuno nacional), shan noodles (fideos secos con tomate y cacahuetes), laphet thoke (ensalada de hoja de té fermentada) y el curry birmano con verduras encurtidas. Una comida completa en restaurante local: 3-6$.",
    "safety": "SITUACIÓN POLÍTICA GRAVE desde el golpe de 2021. Consulta los avisos de viaje del Ministerio de Exteriores español. El turismo ha caído drásticamente y muchas zonas son inaccesibles. Solo viajeros experimentados que estén al día de la situación.",
    "visa_info": "Visa obligatoria. El sistema de e-visa ha estado interrumpido por la crisis política. Consulta el estado actual antes de solicitar. El régimen militar controla el sistema de visados.",
    "local_tips": ["IMPORTANTE: verifica la situación política antes de viajar — ha cambiado radicalmente desde 2021", "La pagoda Shwedagon al amanecer (6-7am) es el mejor momento — poca gente y luz dorada", "El tren circular es la forma más auténtica de ver barrios locales por 200 kyat", "El laphet thoke (ensalada de té) es el snack más único de la gastronomía birmana", "Lleva kyat en efectivo — las tarjetas y transferencias internacionales tienen restricciones"],
    "travel_styles": ["cultura", "historia", "espiritual", "aventura"],
    "vibes": ["buddhist", "colonial", "authentic", "golden"],
    "climate": ["tropical monsoon"],
    "best_months": ["November", "December", "January", "February"],
    "budget_daily_low": 20, "budget_daily_mid": 45, "budget_daily_high": 120, "guide_quality": 8
},
{
    "slug": "ulaanbaatar", "name": "Ulán Bator", "country": "Mongolia", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 47.8864, "lng": 106.9057},
    "tagline": "La capital más fría del mundo, puerta a las estepas y la ruta del tren transiberiano",
    "intro": "Ulán Bator es la capital más fría del mundo — en enero las temperaturas bajan a -30°C o menos. Es también la ciudad más aislada geográficamente de Asia: a 1.500 km del mar más cercano, rodeada de estepas infinitas. Y es precisamente eso lo que la hace tan fascinante para cierto tipo de viajero.\n\nLa ciudad en sí no es la razón del viaje — el Monasterio de Gandantegchinlen, el Museo del Dinosaurio y el Museo Nacional de Mongolia son destinos válidos pero lo que realmente llama es el exterior. A 60 km del centro empieza el Parque Nacional Gorkhi-Terelj con yurts, caballos y paisajes que parecen de otro siglo. El desierto de Gobi está a 20 horas en tren al sur.\n\nUlán Bator también es la escala del tren Transiberiano entre Moscú y Pekín — uno de los viajes en tren más míticos del mundo.",
    "when_to_go": "Junio-agosto es el único momento viable para turistas sin experiencia extrema: temperaturas de 15-25°C, el festival Naadam (julio, el más importante de Mongolia con lucha, tiro con arco y carreras de caballos) y el acceso completo a la estepa.",
    "how_to_get_there": "Aeropuerto Internacional de Chinggis Khaan con conexiones de Pekín, Seúl y Moscú. Bus al centro. Tren Transiberiano desde Pekín (30h) o Moscú (6 días) — una experiencia en sí mismo.",
    "where_to_sleep": [
        {"name": "Centro (Sükhbaatar)", "description": "Alrededor de la plaza principal. Hostels desde 10$, hoteles desde 35$. La opción más práctica."},
        {"name": "Zaisan", "description": "El barrio residencial al sur con las mejores vistas de la ciudad. Más tranquilo."},
        {"name": "Yurt camp en Terelj", "description": "Alojarse en un ger (yurt) a 60km del centro es la experiencia más auténtica de Mongolia (30-50$/noche con comidas)."}
    ],
    "what_to_do": [
        {"title": "Festival Naadam (julio)", "description": "El festival nacional de Mongolia con los Tres Juegos Viriles: lucha mongola, tiro con arco a caballo y carreras de caballos. El 11-13 de julio es el evento cultural más importante del país."},
        {"title": "Monasterio de Gandantegchinlen", "description": "El monasterio budista más importante de Mongolia, sobreviviente de la represión comunista. La estatua de Megjid Janraisig (26m de altura en el interior) es impresionante."},
        {"title": "Parque Nacional Gorkhi-Terelj", "description": "A 60 km del centro: montañas de granito, ríos y yurts. Alquila un caballo (15$/h) para explorar la estepa — la experiencia más auténtica de Mongolia."},
        {"title": "Museo Nacional de Mongolia", "description": "La historia mongola desde el Paleolítico hasta el Imperio de Gengis Kahn y el período soviético. El traje de un khan del siglo XIII es extraordinario."},
        {"title": "Estatua ecuestre de Gengis Khan (Tsonjin Boldog)", "description": "La estatua ecuestre más grande del mundo (40m de altura) a 54 km del centro. Se puede subir por el cuello del caballo hasta la cabeza."},
        {"title": "Tren Transiberiano hasta Pekín o Moscú", "description": "Ulán Bator está en la ruta del Transmongoliano (rama del Transiberiano). El tren a Pekín tarda 30h a través del desierto de Gobi. Una experiencia de viaje definitiva."}
    ],
    "food_and_drink": "La cocina mongola es carne y lácteos: khuushuur (empanadillas fritas con carne), buuz (dumplings al vapor), tsuivan (pasta con carne salteada) y el airag (leche de yegua fermentada, el 'vino' nacional). El mejor restaurante de comida mongola tradicional es Millie's Café. Cena completa 5-12$.",
    "safety": "Ulán Bator tiene zonas de riesgo, especialmente barrios de gers (asentamientos informales) de noche. El centro es seguro durante el día. Mantén los objetos de valor guardados en el mercado Narantuul.",
    "visa_info": "Los españoles pueden entrar sin visado hasta 30 días con pasaporte español. Para estancias más largas se necesita visa. Moneda: tugrik (MNT). 1€ ≈ 3.700 MNT.",
    "local_tips": ["El festival Naadam (11-13 julio) es la razón para organizar el viaje en esas fechas", "Alójate al menos una noche en un ger camp fuera de la ciudad — es la esencia de Mongolia", "El mercado Narantuul (Black Market) tiene de todo pero requiere atención — carteristas", "Alquila un guía-conductor para salir de la ciudad — las carreteras no señalizadas requieren experiencia local", "La temporada corta significa que los operadores se reservan rápido — reserva con antelación"],
    "travel_styles": ["aventura", "naturaleza", "cultura", "trenes"],
    "vibes": ["nomadic", "steppe", "cold", "remote"],
    "climate": ["continental subarctic", "extreme cold winters"],
    "best_months": ["June", "July", "August"],
    "budget_daily_low": 25, "budget_daily_mid": 55, "budget_daily_high": 150, "guide_quality": 8
},
{
    "slug": "almaty", "name": "Almatý", "country": "Kazajistán", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 43.2220, "lng": 76.8512},
    "tagline": "La metrópolis de Asia Central al pie del Tian Shan, donde la estepa se encuentra con los glaciares",
    "intro": "Almatý es la mayor ciudad de Kazajistán y la más dinámica de Asia Central — cosmopolita, con buena gastronomía, vida nocturna animada y un acceso extraordinario a la naturaleza: los picos de Tian Shan (4.000m) están a literalmente 30 minutos en coche del centro. El Big Almaty Lake a 2.500m de altitud, la pista de patinaje de Medeu (la más alta del mundo) y las laderas de esquí de Shymbulak forman un entorno natural único para una ciudad de más de 2 millones de habitantes.\n\nLa ciudad fue construida en estilo soviético con amplias avenidas arboladas que la hacen agradable para caminar, y tiene una mezcla étnica de kazajos, rusos, uigures y coreanos que se refleja en la gastronomía. El Gran Bazar Verde (Zelyony Bazar) es el mercado más completo de Asia Central.\n\nAlmatý es el punto de entrada para explorar Kazajistán y Asia Central — a pocas horas de la antigua ruta de la seda.",
    "when_to_go": "Mayo-junio y septiembre-octubre: templado (18-24°C), colores de temporada y senderismo en la montaña sin el calor del verano. El invierno (nov-feb) es frío (-15°C) pero perfecto para esquí en Shymbulak.",
    "how_to_get_there": "Aeropuerto Internacional de Almatý con conexiones de Europa (Frankfurt, Londres, Estambul) y Asia. Vuelos directos desde Moscú y las capitales de Asia Central. Bus al centro en 40 min.",
    "where_to_sleep": [
        {"name": "Centro (Alatau)", "description": "El centro con los mejores hoteles boutique (desde 50$) y acceso a pie a los principales atractivos."},
        {"name": "Medeu / Górky Park", "description": "Zona más tranquila al sur, cerca de la montaña. Mejores apartamentos para estancias largas."},
        {"name": "Almaly", "description": "El barrio de los mercados y la vida local. Más económico y auténtico."}
    ],
    "what_to_do": [
        {"title": "Big Almaty Lake", "description": "El lago glaciar a 2.500m de altitud con agua turquesa-esmeralda. La ruta de senderismo desde Shymbulak es de 4 horas. El acceso en taxi-compartido cuesta 5-8$."},
        {"title": "Pista de Medeu y Shymbulak", "description": "La pista de patinaje más alta del mundo (1.691m) y la estación de esquí de Shymbulak (3.200m) están conectadas por telecabina. En invierno: esquí; en verano: senderismo y vistas."},
        {"title": "Gran Bazar Verde (Zelyony Bazar)", "description": "El mercado más rico de Asia Central: especias, frutos secos, carne de caballo, kumis (leche de yegua fermentada) y ropa de pieles. El desayuno samsa (hojaldre de carne) aquí es el mejor de la ciudad."},
        {"title": "Parque Central de Cultura y Descanso", "description": "El enorme parque soviético con el Palacio de la República sigue siendo el pulmón de la ciudad. Los fines de semana es donde los almatenses pasean y socializan."},
        {"title": "Museo de Arte de Kazajistán", "description": "La colección más completa de arte kazajo, de nómada y soviético a contemporáneo. El edificio soviético pomposo es parte del atractivo (800 tenge)."},
        {"title": "Canyon Charyn (excursión de día)", "description": "A 195 km al este, el Charyn Canyon es el Grand Canyon de Asia Central — 150m de profundidad en roca roja. Alquila coche o únete a un tour (30-40$)."}
    ],
    "food_and_drink": "La cocina kazaja es la más carnívora de Asia Central: beshbarmak (carne de caballo o cordero con pasta plana, el plato nacional), manti (dumplings), samsa (hojaldre de carne) y el kurt (bolas de queso seco). El Zelyony Bazar tiene los mejores precios. Los restaurantes rusos y uigures de la ciudad son excelentes. Cena completa 10-20$.",
    "safety": "Almatý es segura para turistas. El centro y la zona de montaña no presentan problemas. Los mercados requieren atención con los bolsillos. Registra tu viaje en el consulado.",
    "visa_info": "Los ciudadanos españoles pueden entrar sin visado hasta 30 días. Para visitas más largas existe el e-visa online. Moneda: tenge (KZT). 1€ ≈ 480 KZT.",
    "local_tips": ["El Big Almaty Lake solo tiene cupo limitado de visitantes — compra el permiso online antes de ir", "Shymbulak en invierno tiene nieve garantizada y precios de esquí muy bajos respecto a los Alpes", "El kumis (leche de yegua fermentada) en el mercado verde es una experiencia gastronómica única — adquirido el gusto, es excelente", "Los taxis se negocian o usa la app InDriver (Uber local)", "Lleva un adaptador universal — los enchufes son de tipo soviético (tipo C/F)"],
    "travel_styles": ["naturaleza", "aventura", "cultura", "esquí"],
    "vibes": ["central asia", "soviet", "mountain", "steppe"],
    "climate": ["continental", "cold winters", "hot summers"],
    "best_months": ["May", "June", "September", "October"],
    "budget_daily_low": 30, "budget_daily_mid": 65, "budget_daily_high": 160, "guide_quality": 8
},
{
    "slug": "baku", "name": "Bakú", "country": "Azerbaiyán", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 40.4093, "lng": 49.8671},
    "tagline": "Donde el petróleo se vistió de arquitectura: la ciudad más sorprendente del Cáucaso",
    "intro": "Bakú es una de las ciudades más sorprendentes de Europa/Asia — ninguna categoría la describe completamente. El casco histórico amurallado (Icheri Sheher) con la Torre de la Doncella es Patrimonio UNESCO y tiene más de 2.000 años de historia. Justo al lado, los rascacielos de las Flame Towers (torres que simulan llamas de gas en sus pantallas LED gigantes) y el Bulevar Caspiano forman una imagen urbana única en el mundo.\n\nAzerbaiyán es un país musulmán mayoritariamente laico con una tradición de tolerancia religiosa. El alcohol es fácilmente disponible, las mujeres no están obligadas a cubrirse y la cultura es una mezcla fascinante de turco, persa, ruso y caucásico.\n\nEl petróleo del Caspio transformó Bakú en el siglo XX y de nuevo en el XXI — la arquitectura de Hadid, Portzamparc y Foster por la ciudad atestigua una inversión urbanística extraordinaria.",
    "when_to_go": "Abril-junio y septiembre-octubre: temperaturas perfectas (18-26°C), sin el calor de julio-agosto (35°C) ni el frío invernal. El Cáucaso ofrece colores de otoño espectaculares.",
    "how_to_get_there": "Aeropuerto Internacional Heydar Aliyev con conexiones de Europa (vuelos directos desde Madrid y Barcelona con Buta Airways/Azerbaijan Airlines), Turquía, Dubái y toda la región.",
    "where_to_sleep": [
        {"name": "Icheri Sheher (Ciudad Vieja)", "description": "Dentro de las murallas milenarias, el alojamiento más atmosférico. Boutique hotels desde 60$."},
        {"name": "Bulevar Caspiano", "description": "Junto al mar Caspio y los grandes hoteles. Opciones desde 45$."},
        {"name": "Narimanov", "description": "El barrio residencial más auténtico, a 15 min del centro. Mejor precio-calidad."}
    ],
    "what_to_do": [
        {"title": "Icheri Sheher (Ciudad Vieja amurallada)", "description": "El casco histórico UNESCO con la Torre de la Doncella (9€, vistas desde arriba) y el Palacio de los Shirvanshah (siglo XV). Las calles laberínticas guardan caravaserás y mezquitas."},
        {"title": "Flame Towers al atardecer", "description": "Las tres torres en forma de llama (182, 165 y 161 metros) con pantallas LED gigantes que simulan fuego cambian de color con el atardecer. El mejor mirador está en las murallas de Icheri Sheher."},
        {"title": "Centro Cultural Heydar Aliyev", "description": "El edificio de Zaha Hadid sin una sola línea recta es uno de los edificios más fotogénicos del siglo XXI. El museo de la cultura azerbaiyana en el interior es también excelente (entrada gratis el lunes)."},
        {"title": "Bulevar Caspiano", "description": "El paseo marítimo de 4km junto al Mar Caspio (técnicamente el mayor lago del mundo) es la sala de estar de Bakú. Mirillas, edificios art nouveau ruso y vistas a las torres."},
        {"title": "Templo del Fuego de Ateshgah", "description": "A 30 km, el templo zoroástrico del siglo XVIII construido sobre un fuego natural de gas que lleva ardiendo siglos. Único en el mundo (2€)."},
        {"title": "Excursión al Fango Volcánico de Gobustan", "description": "A 65 km, los volcanes de fango que erupclonan barro frío forman un paisaje lunar únicos. En el mismo parque, petroglifos del Paleolítico (UNESCO)."}
    ],
    "food_and_drink": "La cocina azerbaiyana mezcla influencias persas, turcas y del Cáucaso: plov (arroz con azafrán y cordero, el plato nacional), dolma de hoja de parra, kebab de cordero a la brasa, kutab (crepes rellenos de verduras) y dushbara (dumpling en caldo). El té negro con mermelada es el ritual social por excelencia. Cena completa 15-25 AZN.",
    "safety": "Bakú es muy segura para turistas. Sin precauciones especiales. La Ciudad Vieja es tranquila incluso de noche.",
    "visa_info": "Los españoles necesitan visa de turismo. Obtén el e-visa online (23$, tramitación en 3 días) antes de viajar. Moneda: manat azerbaiyano (AZN). 1€ ≈ 1,85 AZN.",
    "local_tips": ["El e-visa se tramita online en e-visa.gov.az — hazlo con al menos 5 días de antelación", "El metro es eficiente pero las estaciones no tienen nombres en latín — lleva el mapa en azerbaiyano", "El teahouse (çayxana) del bulevar es el lugar para tomar el té a la azerbaiyana", "La gastronomía de Bakú está infravalorada — el plov de azafrán aquí es de otro nivel", "El Centro Heydar Aliyev es gratis los lunes — aprovecha"],
    "travel_styles": ["arquitectura", "cultura", "historia", "diseño"],
    "vibes": ["caucasus", "fire", "oil", "cosmopolitan"],
    "climate": ["humid subtropical", "mild winters"],
    "best_months": ["April", "May", "June", "September", "October"],
    "budget_daily_low": 35, "budget_daily_mid": 75, "budget_daily_high": 180, "guide_quality": 8
},
{
    "slug": "yerevan", "name": "Ereván", "country": "Armenia", "continent": "Asia", "type": "city",
    "coordinates": {"lat": 40.1792, "lng": 44.4991},
    "tagline": "La ciudad rosada al pie del Ararat, con el mejor brandy del mundo y 3.000 años de historia",
    "intro": "Ereván es una de las ciudades más antiguas del mundo — fundada en 782 a.C., es más vieja que Roma. El Monte Ararat (5.137m), símbolo nacional armenio aunque hoy esté en territorio turco, se ve perfectamente desde la ciudad en días despejados y crea una de las postales más poderosas de Oriente Próximo.\n\nLa ciudad fue reconstruida en los años 30 en toba rosada armeniana (la piedra volcánica local) dando a todo el centro una tonalidad única. La Cascada — una escalera monumental con jardines escalonados y el Museo de Arte Moderno en su interior — es el símbolo urbano contemporáneo.\n\nArmenia es uno de los países más hospitalarios del mundo, con una diáspora global que tiene a medio país con familiares en Los Ángeles y París, lo que explica su mentalidad abierta y el excelente nivel de inglés entre los jóvenes.",
    "when_to_go": "Mayo-junio y septiembre-octubre: temperaturas ideales (20-26°C) y el Monte Ararat visible. El verano es caluroso (34°C) pero animado. El invierno (dic-feb) es frío y con posibilidad de nieve — la ciudad tiene encanto invernal.",
    "how_to_get_there": "Aeropuerto Internacional Zvartnots con conexiones directas de Moscú, Dubái, París, Frankfurt, Estambul y Teherán. También desde Tbilisi por carretera (5h). Taxi del aeropuerto: 12-15$.",
    "where_to_sleep": [
        {"name": "Centro (República)", "description": "Alrededor de la Plaza de la República. Hostels desde 10$, hoteles boutique desde 40$. La zona más conveniente."},
        {"name": "Barrio Norte / Cascada", "description": "Junto a la Cascada y el Parque de la Victoria. Animado y bien situado. Apartamentos desde 35$."},
        {"name": "Kentron histórico", "description": "El corazón de toba rosada, más tranquilo. Buenas opciones de precio medio."}
    ],
    "what_to_do": [
        {"title": "La Cascada y el Cafesjian Center", "description": "La escalera monumental de mármol blanco con el monte Ararat de fondo al atardecer es la imagen más icónica de Ereván. El museo de arte moderno en su interior (gratis) tiene esculturas de Botero y otros."},
        {"title": "Monasterio de Geghard y Valle de Azat", "description": "A 40 km, el monasterio medieval parcialmente excavado en la roca viva (UNESCO) en un desfiladero dramático. Una de las experiencias más impresionantes de Armenia (gratuito)."},
        {"title": "Templo de Garni", "description": "El único templo grecorromano de toda la Unión Soviética, del siglo I d.C., en una meseta volcánica sobre un desfiladero. A 30 km del centro."},
        {"title": "Brandy Ararat (destilería)", "description": "El coñac armenio es considerado uno de los mejores del mundo — Churchill lo bebía en exclusiva. La destilería Ararat tiene visitas con cata (15-30$)."},
        {"title": "Mercado Vernissage", "description": "El mercado de arte y artesanía del fin de semana donde se venden alfombras armenias, grabados de Ararat, lavash decorado y joyas de granate (la piedra nacional). Regateo obligatorio."},
        {"title": "Museo de Historia y Genocide Memorial", "description": "El Tsitsernakaberd — memorial del genocidio armenio de 1915 — es un lugar de peregrinación para los armenios de todo el mundo. El eterno fuego y el memorial son de visita obligada."}
    ],
    "food_and_drink": "La cocina armenia es una de las más antiguas del mundo: khorovats (barbacoa de cordero, el plato nacional), dolma (hojas de parra rellenas de carne y arroz), manti armenio (ravioli al horno con yogur), lavash (pan armenio plano UNESCO) y el bastirma (embutido curado). El brandy Ararat es la bebida nacional. Cena completa 15-25$.",
    "safety": "Ereván es muy segura para turistas. La tensión geopolítica con Azerbaiyán existe pero no afecta a la capital. Evita zonas fronterizas con Azerbaiyán.",
    "visa_info": "Los españoles pueden entrar sin visado hasta 180 días con pasaporte español. Armenia es uno de los países más accesibles del Cáucaso. Moneda: dram armenio (AMD). 1€ ≈ 430 AMD.",
    "local_tips": ["La visa es libre para españoles y el período es generoso — Armenia es ideal para estancias largas", "El coñac armenio en cualquier tienda de licores es mucho más barato que en el aeropuerto", "La excursión a Geghard + Garni en un día es imprescindible — alquila coche compartido (8-12$)", "El lavash armenio recién hecho en un tonir (horno de barro) es un espectáculo y el mejor pan de la región", "El Vernissage los fines de semana tiene los precios más bajos de artesanía — llega pronto por las mejores alfombras"],
    "travel_styles": ["historia", "cultura", "gastronomía", "arquitectura"],
    "vibes": ["caucasus", "ancient", "pink city", "brandy"],
    "climate": ["continental", "cold winters", "hot summers"],
    "best_months": ["May", "June", "September", "October"],
    "budget_daily_low": 28, "budget_daily_mid": 60, "budget_daily_high": 150, "guide_quality": 8
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
