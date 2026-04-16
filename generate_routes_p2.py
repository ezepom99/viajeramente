#!/usr/bin/env python3
"""Priority 2: 15-day routes."""
import psycopg2

conn = psycopg2.connect(dbname='viajeramente', user='tenant')
cur = conn.cursor()

routes = [
    {
        "slug": "japon-15-dias",
        "name": "Japón en 15 días",
        "country": "Japón",
        "continent": "Asia",
        "tagline": "Dos semanas para entender Japón: de las montañas de los Alpes a los templos de Hiroshima",
        "intro": "Quince días en Japón te permiten ir más allá del circuito clásico y rozar el Japón real: el que existe entre los grandes hitos, el de los onsen de montaña, los ryokan de pueblo, los santuarios que no salen en las guías. Este itinerario amplía la ruta de 7 días añadiendo los Alpes japoneses de Kamikochi, el Japón rural de Takayama, el peso histórico de Hiroshima y la isla-santuario de Miyajima.\n\nCon 15 días tienes tiempo para equivocarte de tren, perderte en una ciudad, volver a un sitio que te gustó demasiado. Eso es exactamente lo que hay que hacer en Japón: los errores tienen su propio sabor. El JR Pass de 14 días (comprado en España: 460€ aprox.) cubre casi todo el transporte, incluyendo el Shinkansen.\n\nPresupuesto: 120-180€/día incluyendo alojamiento mixto (hostels/hotels + 2-3 noches en ryokan), transporte cubierto por JR Pass y comidas.",
        "ideal_duration": ["15 días"],
        "when_to_go": "Marzo-abril (sakura) y noviembre (momiji) son las épocas más espectaculares pero masificadas. Mayo, junio y octubre son excelentes con menos gente. Evita el golden week de abril-mayo (primera semana de mayo es festivo nacional, hoteles llenos).",
        "how_to_get_there": "Vuelos directos desde Madrid a Tokio Narita (NRT) o Haneda (HND) con Iberia o Japan Airlines, ~14h. Regreso desde Osaka Kansai (KIX) posible si haces el viaje en sentido lineal. Precio: 700-1.100€ ida y vuelta.",
        "budget_daily_low": 90,
        "budget_daily_mid": 150,
        "budget_daily_high": 300,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Naturaleza", "Gastronomía", "Fotografía"],
        "days": [
            ("Días 1-3: Tokio", "Tres días en la capital permiten explorar sin prisas: el día 1 para Shinjuku y Shibuya (cruce más transitado del mundo), el día 2 para Asakusa y el templo Senso-ji, el mercado de pescado de Tsukiji y el barrio tecnológico de Akihabara, el día 3 para un museo (el Mori Art Museum en Roppongi o el TeamLab Borderless) y los barrios residenciales de Shimokitazawa o Nakameguro. Tres noches en el mismo hotel sin cargar maletas cada mañana."),
            ("Días 4-5: Nikko y Mashiko", "Excursión de un día a Nikko (2h desde Tokio en Tobu Express): el mausoleo de Tokugawa con su exceso decorativo y el lago Chuzenji. El día 5, opcional pero excelente: Mashiko, el pueblo de la cerámica donde el maestro Shoji Hamada definió el mingei (arte popular japonés). Los talleres de alfarería aceptan visitas y puedes hacer tu propia pieza por 15-20€."),
            ("Días 6-7: Hakone y Monte Fuji", "Romancecar desde Shinjuku a Hakone: el Hakone Free Pass cubre el funicular a Owakudani, el barco por el lago Ashi y los autobuses locales. Si el Fuji está despejado (más probable en otoño y en días frescos), la vista desde el lago es el mejor plano del volcán. Dos noches en un ryokan con onsen al aire libre —la noche más cara del viaje pero la más memorable. Si vas en julio-agosto, puedes subir al Fuji (temporada oficial de ascenso)."),
            ("Días 8-9: Alpes japoneses — Matsumoto y Kamikochi", "Shinkansen a Nagoya y conexión a Matsumoto: el castillo de Matsumoto (uno de los cuatro castillos originales de Japón, construcción de madera negra del siglo XVI) es impresionante. Al día siguiente, autobús a Kamikochi (la carretera está prohibida a coches privados): el valle alpino más bonito de Japón, con los Alpes del Norte reflejados en el río Azusa. Senderismo de 2-4h por el valle o hasta el fondo del glaciar Dakesawa. Alojamiento en el propio valle o de vuelta en Matsumoto."),
            ("Días 10-11: Takayama — Japón rural en conserva", "Bus desde Matsumoto a Takayama (2h, un trayecto de montaña espectacular). Takayama es el mejor ejemplo de ciudad rural japonesa bien conservada: sus machinami (calles históricas) del período Edo tienen destilerías de sake, tiendas de lacas y casas de madera de 300 años. El Jinya (oficina del gobierno Tokugawa) y los mercados matutinos de Jinya-mae y Miyagawa son de los más auténticos del país. El día 11, excursión a la aldea de Shirakawa-go (autobús 50 min): casas gassho-zukuri con tejados de paja en forma de manos en oración, Patrimonio UNESCO."),
            ("Días 12-13: Kioto y Nara", "Shinkansen desde Toyama a Kioto (2h30min). Dos días completos para la antigua capital: día 12 para Fushimi Inari (los mil torii naranjas, espectacular al amanecer), el corredor de bambú de Arashiyama y el templo Tenryu-ji con su jardín zen. Día 13 para el Kinkaku-ji (Pabellón de Oro), Ryoan-ji (jardín de piedras), y excursión a Nara (45 min en tren): el parque con 1.200 ciervos que comen de tu mano y el Gran Buda de 15 metros en el templo Todai-ji."),
            ("Días 14-15: Hiroshima y Miyajima — vuelo desde Osaka", "Shinkansen a Hiroshima (1h desde Kioto, cubierto por JR Pass). El Parque Memorial de la Paz y el Museo de la Bomba Atómica son visitas emocionalmente intensas pero imprescindibles. El cenotafio, la cúpula de Genbaku y el río Motoyasu crean un espacio de reflexión único. Al día siguiente, ferry a la isla de Miyajima: el torii rojo de Itsukushima flotando en el mar en pleamar es una de las imágenes más icónicas de Japón. Vuelta en Shinkansen a Osaka (Shin-Osaka) para vuelo de regreso desde KIX.")
        ]
    },
    {
        "slug": "tailandia-15-dias",
        "name": "Tailandia en 15 días",
        "country": "Tailandia",
        "continent": "Asia",
        "tagline": "De los templos dorados de Bangkok a las cuevas de Chiang Rai y las islas más remotas del sur",
        "intro": "Quince días en Tailandia permiten ir más allá del triángulo clásico Bangkok-Chiang Mai-islas y explorar rincones que la mayoría de viajeros no ven: el triángulo dorado en la frontera con Myanmar y Laos, las cuevas y plantaciones de té de Chiang Rai, los manglares de Krabi y las islas Trang, todavía sin masificar. El norte y el sur son países distintos en términos de paisaje, cocina y ritmo —combinarlos en dos semanas es el viaje completo.\n\nEsta ruta usa dos vuelos domésticos (Bangkok-Chiang Rai y Krabi-Bangkok) para maximizar el tiempo. AirAsia y Thai Lion Air conectan prácticamente todo el país por 20-60€. El alojamiento en el norte es notablemente más barato que en las islas del sur; equilibra el presupuesto durmiendo bien en Chiang Rai para gastarlo en un bungalow de playa en Koh Lanta.\n\nPresupuesto: 45-80€/día incluyendo vuelos domésticos, 35-60€ sin ellos.",
        "ideal_duration": ["15 días"],
        "when_to_go": "Noviembre-febrero es la temporada perfecta para todo el país. Marzo-mayo: seco en el norte pero caluroso; las islas del sur del golfo pueden tener lluvia. Junio-octubre: monzón en el norte (verde y fresco), islas de Andamán (Krabi, Koh Lanta) más tranquilas que en el golfo.",
        "how_to_get_there": "Vuelos desde España a Bangkok con escala en Doha, Dubái o Kuala Lumpur. Llega a Suvarnabhumi (BKK). Precio: 500-800€ ida y vuelta.",
        "budget_daily_low": 30,
        "budget_daily_mid": 60,
        "budget_daily_high": 140,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Naturaleza", "Playa", "Gastronomía"],
        "days": [
            ("Días 1-3: Bangkok", "Tres días completos en la capital: la fiebre del primer día (calor, tráfico, grandeza caótica), el ritmo del segundo (Wat Pho, Gran Palacio, mercado de Chatuchak si es fin de semana, el canal Khlong Saen Saep en barco para ir rápido de un punto a otro), y la autenticidad del tercero (barrio chino de Yaowarat al atardecer, el mercado nocturno de Talad Rot Fai, la salsa de tamarindo del pad thai de los callejones de Silom). Tres noches en Silom o Sukhumvit — bien conectados en BTS Skytrain."),
            ("Días 4-5: Chiang Rai — el norte más profundo", "Vuelo Bangkok-Chiang Rai (1h, 25-45€). Chiang Rai es más tranquila y auténtica que Chiang Mai: el Wat Rong Khun (Templo Blanco, excentrismo artístico llevado al extremo de la belleza), el Baan Dam (Casa Negra, contrapunto oscuro y budista heterodoxo), los mercados de montaña. El día 5, excursión al Triángulo Dorado: el punto donde confluyen los ríos Mekong y Ruak, donde se juntan Tailandia, Laos y Myanmar. El opio fue el cultivo de esta región durante siglos; ahora hay un museo que lo cuenta mejor de lo esperado."),
            ("Días 6-7: Chiang Mai — elefantes y cocina", "Bus o minivan desde Chiang Rai a Chiang Mai (3h30min). Dos días para la capital del norte tailandés: el santuario ético de elefantes (reserva con antelación, Elephant Nature Park o similar), el Night Bazaar para compras de artesanía local, los templos del casco histórico amurallado (Wat Phra Singh, Wat Chedi Luang), y una clase de cocina tailandesa — hay muchas academias excelentes por 25-35€ que incluyen visita al mercado."),
            ("Días 8-9: Pai y los valles del norte", "Minivan desde Chiang Mai a Pai (3h por 762 curvas, literal): el pueblo de Pai en el valle del río del mismo nombre es un espacio entre colinas con ambiente relajado, cascadas cercanas (Mo Paeng, 8 km), aguas termales y cafeterías. Es el lugar del norte tailandés donde los viajeros se quedan más días de los previstos. El día 9, vuelta a Chiang Mai en minivan (o autobús nocturno a Bangkok directamente si prefieres)."),
            ("Días 10-11: Krabi — llegada al sur", "Vuelo Chiang Mai-Krabi (1h30min, 30-60€). Krabi es la puerta de entrada a las costas del Andamán: acantilados kársticos que caen al mar turquesa, kayak por manglares, playas escondidas accesibles solo en barco. El primer día: instalación en Ao Nang o en Railay Beach (acceso solo en barco de cola larga, el rincón más bonito del área). El día 11, excursión a las Cuatro Islas (Koh Poda, Koh Gai, Koh Tub, Koh Mor) en barca de cola larga: snorkel en el arrecife, playa virgen, laguna verde."),
            ("Días 12-13: Koh Lanta — las islas sin masificar", "Ferry desde Krabi a Koh Lanta (2h30min). Koh Lanta es más grande, menos masificada y más auténtica que Koh Phi Phi (que puedes visitar en excursión desde aquí). La playa de Klong Dao para el resort; Klong Nin y Kantiang Bay para la tranquilidad. El Parque Nacional marino del sur de la isla tiene los mejores fondos para bucear del área (inmersión guiada: 60-80€). El pueblo viejo de Ban Ko Lanta tiene casas de madera sobre pilotes en el mar y ambiente chill."),
            ("Días 14-15: Koh Phi Phi o regreso", "Excursión a Koh Phi Phi Don y la famosa Maya Bay (donde se rodó The Beach, ahora con reserva obligatoria y aforo limitado — se nota la diferencia). El snorkel en el área es de los mejores de Tailandia. El día 15, ferry de vuelta a Krabi, vuelo a Bangkok (conexión internacional) o vuelo directo si hay disponible. Última noche en Bangkok o en tránsito.")
        ]
    },
    {
        "slug": "vietnam-15-dias",
        "name": "Vietnam en 15 días",
        "country": "Vietnam",
        "continent": "Asia",
        "tagline": "De los arrozales en terrazas de Sapa al delta del Mekong: Vietnam de norte a sur completo",
        "intro": "Vietnam de norte a sur en 15 días es uno de los grandes viajes de Asia: el país cambia completamente cada 300 kilómetros, y ese contraste —el Hanói comunista y melancólico, las terrazas de arroz de Sapa, la bahía de Ha Long, el Hội An colonial, la frenética Ho Chi Minh City— es exactamente lo que hace el viaje tan completo.\n\nLa ruta usa el tren nocturno entre Hanói y Da Nang (una experiencia en sí misma), vuelo doméstico de Da Nang a Ho Chi Minh City, y diversas excursiones locales. Vietnam tiene una red de trenes histórica y lenta pero encantadora, y vuelos domésticos muy baratos (VietJet, Bamboo Airways: 20-50€ por trayecto).\n\nPresupuesto: 40-70€/día incluyendo alojamiento de calidad media (hoteles boutique de 30-60€ la noche). El crucero de Ha Long es el mayor gasto individual (80-200€ por noche en el barco).",
        "ideal_duration": ["15 días"],
        "when_to_go": "El país es largo y el clima varía: el norte tiene mejor clima en octubre-abril. El centro (Da Nang, Hội An) es ideal de febrero a agosto. El sur (Ho Chi Minh) tiene dos estaciones: seca (noviembre-abril) y lluviosa (mayo-octubre). La época perfecta para todo el país a la vez no existe, pero noviembre-enero es el mejor compromiso.",
        "how_to_get_there": "Vuelo a Hanói (HAN) y regreso desde Ho Chi Minh City (SGN) o Saigón. Sin vuelos directos desde España: escala en Doha, Dubái, Bangkok o Kuala Lumpur. Precio: 600-900€ ida y vuelta en vuelo abierto (open jaw).",
        "budget_daily_low": 25,
        "budget_daily_mid": 55,
        "budget_daily_high": 120,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Naturaleza", "Gastronomía", "Aventura"],
        "days": [
            ("Días 1-2: Hanói", "Dos días en la capital: el barrio de los 36 gremios para perderse, el mausoleo de Ho Chi Minh (cierra tardes, lunes y viernes), el lago Hoan Kiem al amanecer, el museo de etnología para entender las 54 etnias del país, el bun cha para almorzar y el bia hoi (cerveza de barril a 20 céntimos) para la noche. El día 2 una clase de cocina vietnamita por la mañana o una excursión a los pueblos de alfarería del lago Tay Ho."),
            ("Días 3-4: Sapa — terrazas de arroz y minorías étnicas", "Tren nocturno o autobús Hanói-Lào Cai + minivan a Sapa (total 8-9h). Las terrazas de arroz de los valles de Muong Hoa son las más fotogénicas del Sudeste Asiático — en septiembre con el arroz dorado antes de la cosecha, o en mayo-junio con el verde intenso del inicio. Los pueblos H'mong Negro y Red Dao todavía mantienen sus tradiciones textiles. Contrata guía local (20-30€/día) de las propias comunidades — conocen atajos que no están en ningún mapa. Noche en un homestay de montaña."),
            ("Días 5-6: Bahía de Ha Long — crucero 2 noches", "Autobús o transporte desde Sapa/Hanói al puerto de Tuan Chau. Dos noches en el barco permiten explorar zonas de la bahía inaccesibles en los cruceros de un día: la bahía de Lan Ha (menos visitada y más tranquila), el kayak por las cuevas flotantes, la pesca con los poblados flotantes. Amanecer sobre los islotes kársticos desde cubierta con una taza de té vietnamita."),
            ("Días 7-8: Hội An", "Bus desde Ha Long a Hanói y tren nocturno SE3/SE5 a Da Nang, taxi 30 km a Hội An — o vuelo Hanói-Da Nang (1h15min, 25€) más cómodo. Dos días en la ciudad de las linternas: día 7 para el casco antiguo (Patrimonio UNESCO), el Puente Japonés, el Museo de la Cultura Sa Huynh, y la sastrería de encargo (si quieres ropa hecha a medida, encárgala el primer día). Día 8 para la playa de An Bang (4 km en bici), el Cabo Rojo de Da Nang y la aldea alfarera de Thanh Ha."),
            ("Días 9-10: Hue — la ciudad imperial", "Bus desde Hội An a Hue (4h, 4-6€ en minivan). Hue fue la capital imperial de Vietnam de 1802 a 1945: la Ciudad Prohibida (Ciudadela Imperial) en el centro, las tumbas reales dispersas por las colinas a orillas del río Perfume (Khai Dinh y Tu Duc son las más espectaculares). Come bun bo Hue — la sopa de fideos con carne y citronella que es la especialidad local y supera en complejidad al pho de Hanói. Excursión al paso Hai Van (22 km de Hue a Da Nang): el paisaje costero más dramático de Vietnam, hecho famoso por Top Gear."),
            ("Días 11-12: Ho Chi Minh City (Saigón)", "Vuelo Da Nang-Ho Chi Minh City (1h15min, 25-40€). El choque con Saigón después del norte es total: 9 millones de personas, 5 millones de motos, rascacielos de cristal junto a pagodas del siglo XVII. El Museo de los Vestigios de la Guerra es duro pero obligatorio para entender el país. El Palacio de la Reunificación para la perspectiva histórica. El barrio de Bui Vien para la noche (la calle más caótica y viva de Vietnam). Come en el mercado Cho Ben Thanh — com tam (arroz roto con costillas a la plancha) para el desayuno es el plato de la ciudad."),
            ("Días 13-15: Delta del Mekong", "Excursión de 2 días al Delta del Mekong: My Tho, Can Tho y el mercado flotante de Cai Rang (el más grande del delta, los vendedores muestran la mercancía colgada de un palo en la proa del bote). El delta alimenta a todo el país — el arroz, el pescado, las frutas tropicales. Excursión en barca por los canales secundarios, lejos de los otros turistas. El día 15 vuelta a Ho Chi Minh para el vuelo de regreso.")
        ]
    },
    {
        "slug": "espana-15-dias",
        "name": "España en 15 días",
        "country": "España",
        "continent": "Europa",
        "tagline": "Madrid, Toledo, el sur andaluz, Valencia y Barcelona: España sin prisa y sin filtros",
        "intro": "España en 15 días es un itinerario de contrastes geográficos, culturales y gastronómicos que pocas veces se hace bien desde dentro del país. Este recorrido une la España castellana (Madrid, Toledo), la andaluza (Sevilla, Granada, Córdoba), la levantina (Valencia) y la mediterránea (Barcelona) en una ruta de sur a norte que va ganando modernidad sin perder profundidad.\n\nEste itinerario está pensado principalmente para viajeros internacionales que quieren ver España completa, pero también para españoles que, paradójicamente, a veces conocen peor su país que los turistas. La alta velocidad conecta las ciudades con una eficiencia que sorprende a quien viene de otros países europeos: Madrid-Sevilla en 2h30min, Sevilla-Barcelona en 5h.\n\nPresupuesto: 80-130€/día incluyendo alojamiento de calidad media, transporte en AVE y comidas con vino incluido. España tiene la mejor relación calidad-precio de Europa occidental en hostelería.",
        "ideal_duration": ["15 días"],
        "when_to_go": "Primavera (abril-junio) y otoño (septiembre-noviembre) son las épocas perfectas. La Semana Santa andaluza (Sevilla especialmente) es un espectáculo único pero requiere reservar con meses de antelación. El verano en el interior (Madrid, Toledo) puede superar los 40°C. La costa mediterránea y el sur son agradables todo el año.",
        "how_to_get_there": "Para viajeros internacionales: la mayoría de aerolíneas internacionales llegan a Madrid Barajas (MAD) o Barcelona El Prat (BCN). Lo ideal es llegar a Madrid y salir desde Barcelona (o viceversa). El AVE es el eje vertebrador de la ruta.",
        "budget_daily_low": 55,
        "budget_daily_mid": 95,
        "budget_daily_high": 200,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Gastronomía", "Historia", "Arte"],
        "days": [
            ("Días 1-3: Madrid", "Tres días en la capital: el día 1 para el Triángulo del Arte (Prado, Reina Sofía y Thyssen-Bornemisza en orden de complejidad creciente — el Guernica del Reina Sofía justifica el museo entero), el barrio de las Letras y la cena en el mercado de San Miguel o en cualquier taberna de la Cava Baja. Día 2 para el Rastro si es domingo, el barrio de Malasaña, La Latina y el retiro. Día 3 para el Palacio Real y los jardines de Sabatini, el barrio de Chueca y la cocina de mercado de los mejores restaurantes de España — Madrid tiene más estrellas Michelin per cápita que cualquier otra ciudad española."),
            ("Día 4: Toledo — la ciudad de las tres culturas", "Cercanías o bus desde Madrid (30-45 min). Toledo es de esas ciudades que te recuerdan que Europa tiene una historia de 2.000 años de convivencia y conflicto entre culturas: la catedral gótica más rica de España, la sinagoga del Tránsito del siglo XIV, las mezquitas convertidas, El Greco en el museo dedicado a él y en las propias iglesias. Come marzapán en la Confitería Santo Tomé (la original, desde 1856). Vuelta a Madrid para dormir o alojamiento en Toledo."),
            ("Días 5-6: Sevilla", "AVE Madrid-Sevilla (2h30min). Sevilla es la ciudad donde los tópicos de España son reales: el flamenco, el tapeo, la Giralda, la naranja amarga en los árboles de las calles. El Real Alcázar (Patrimonio UNESCO, escenario de Juego de Tronos — reserva online) y la Catedral son las visitas obligadas. El barrio de Triana al otro lado del Guadalquivir para las mejores tapas de la ciudad: montadito de pringa, espinacas con garbanzos, pescaíto frito. Espectáculo de flamenco en el Museo del Baile Flamenco o en La Casa del Flamenco."),
            ("Día 7: Córdoba", "Tren Sevilla-Córdoba (45 min). La Mezquita-Catedral de Córdoba es uno de los edificios más singulares del mundo: la superposición de una catedral cristiana en el interior de una gran mezquita islámica sobre una basílica visigoda es el resumen físico de la historia de España. El barrio de la Judería y el Alcázar de los Reyes Cristianos. Come salmorejo (el de Córdoba, más espeso y rico que el gazpacho) y flamenquín en cualquier taberna del centro. Vuelta a Sevilla o continúa a Granada."),
            ("Días 8-9: Granada", "Bus Sevilla-Granada (3h) o tren con escala. Granada tiene la Alhambra —el palacio-fortaleza nazarí más bello del mundo árabe occidental— y hay que reservar con semanas de antelación porque el aforo está limitado a 6.600 personas diarias. El Generalife con sus jardines de agua, los palacios Nazaríes y la Alcazaba. El barrio del Albaicín (Patrimonio UNESCO) al atardecer, con la Alhambra de fondo iluminada, es el mejor mirador de España. Las tapas en Granada son gratis con la consumición —la tradición más generosa de la hostelería española."),
            ("Días 10-11: Valencia", "Tren Granada-Valencia (directo 4h o con escala). Valencia tiene tres mejores versiones de sí misma: la paella original (solo en restaurantes del barrio de El Palmar o La Pepica — la de los turistas del centro no cuenta), la Ciudad de las Artes y las Ciencias de Calatrava (espectacular por fuera, excelente el Oceanogràfic por dentro), y el barrio del Carmen con sus galerías de arte y bares de vermut. El mercado central de Valencia (1910, art nouveau) es el más bonito de España."),
            ("Días 12-15: Barcelona", "AVE Valencia-Barcelona (3h15min). Cuatro días para la ciudad que tiene más para ver que ninguna otra de España: día 12 para la Sagrada Família (reserva con días de antelación, las torres son imprescindibles) y el Park Güell, día 13 para el Born (el barrio medieval más bien conservado de Europa), el Palau de la Música Catalana y el Barrio Gótico, día 14 para Montjuïc (castillo, Fundación Miró, vistas de toda la ciudad) y la Barceloneta, día 15 para mercado de la Boqueria temprano y la Diagonal. Vuelo desde El Prat (BCN).")
        ]
    },
    {
        "slug": "mexico-15-dias",
        "name": "México en 15 días",
        "country": "México",
        "continent": "América",
        "tagline": "De la megalópolis de Ciudad de México a las pirámides mayas del Yucatán pasando por Oaxaca",
        "intro": "México en 15 días es uno de los viajes más completos del continente americano: conecta tres realidades distintas del país —la megalópolis del centro con su historia azteca y colonial, la Oaxaca indígena con la mejor gastronomía de México, y el Yucatán maya con sus cenotes y ruinas en la selva— en un itinerario que combina historia milenaria, arte, cocina y naturaleza.\n\nMéxico es grande (el doble de España) pero este recorrido usa vuelos domésticos estratégicos para no perder tiempo en autobús. Interjet, VivaAerobus y Aeromar conectan CDMX con Oaxaca (1h) y Oaxaca con Mérida o Cancún (1h30min) por 40-100€. El autobús de lujo ADO es una alternativa económica pero lenta.\n\nPresupuesto: 60-110€/día incluyendo alojamiento de calidad, transporte y la gastronomía que se merece este país. Los vuelos domésticos son el mayor gasto del viaje.",
        "ideal_duration": ["15 días"],
        "when_to_go": "Noviembre-abril es la temporada seca en todo el itinerario: ideal. Mayo-junio es caluroso pero seco. Julio-octubre es la temporada de lluvias (el Yucatán puede tener huracanes en septiembre-octubre). El Día de los Muertos (1-2 noviembre) en Oaxaca es uno de los festivales más extraordinarios del mundo.",
        "how_to_get_there": "Vuelos directos desde Madrid a Ciudad de México (MEX/AICM) con Iberia y Aeromexico (12h). También desde Madrid a Cancún (CUN) directamente si quieres hacer el viaje al revés. Precio: 500-900€ ida y vuelta.",
        "budget_daily_low": 40,
        "budget_daily_mid": 75,
        "budget_daily_high": 160,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Gastronomía", "Historia", "Naturaleza"],
        "days": [
            ("Días 1-3: Ciudad de México", "Tres días en la capital más grande de América del Norte (22 millones de habitantes en la zona metropolitana). Día 1: el Centro Histórico (Zócalo, Catedral, Templo Mayor donde los aztecas construyeron su capital sobre el lago de Texcoco), el Palacio Nacional con los murales de Diego Rivera. Día 2: Coyoacán (barrio bohemio, casa azul de Frida Kahlo, mercado de sabores) y Xochimilco (las chinampas, los trajineros y los mariachis en las lanchas). Día 3: Teotihuacán (50 km al norte, las pirámides del Sol y la Luna — ve antes de las 9h para evitar el calor y las multitudes)."),
            ("Días 4-5: Puebla — la ciudad de los azulejos y el mole", "Autobús o combi desde CDMX a Puebla (2h, 8-12€). Puebla es la ciudad de los talaveras (cerámica artesanal de influencia árabe-española), del chile en nogada (el plato más patriótico de México) y del mole poblano. La catedral barroca y los barrios de Analco y Xanenetla (el 'barrio del arte', con murales en cada esquina). El mercado El Parián para artesanía. Excursión al volcán Popocatépetl (si está activo, te dejan acercarte hasta cierto punto — el espectáculo de los gases sobre el cráter nevado es impresionante)."),
            ("Días 6-8: Oaxaca", "Vuelo CDMX-Oaxaca (1h, 40-70€) o autobús nocturno (6h). Oaxaca es la capital gastronómica de México y uno de los centros culturales más ricos de América Latina: los mercados de Benito Juárez y la 20 de Noviembre (el pasillo de las tlayudas, los chapulines fritos, el mole negro), las ruinas zapotecas de Monte Albán sobre una montaña alisada artificialmente, el árbol de Tule (2.000 años, el tronco más grueso del mundo), la destilería de mezcal artesanal en los valles centrales. Tres días no son suficientes para Oaxaca."),
            ("Días 9-10: Mérida y la ruta puuc", "Vuelo Oaxaca-Mérida (1h30min). Mérida es la capital cultural del Yucatán: arquitectura colonial sobre basamentos mayas, el Paseo de Montejo con sus mansiones henequeneras, el mercado Lucas de Gálvez con sus cochinita pibil para el desayuno. El día 10, ruta puuc: las ruinas mayas de Uxmal (Pirámide del Adivino, cuadrángulo de las Monjas — menos masificada que Chichén Itzá y arquitectónicamente superior), Kabah y Sayil en una ruta de un día en coche."),
            ("Días 11-12: Chichén Itzá y Valladolid", "Autobús desde Mérida a Chichén Itzá (2h). La Pirámide de Kukulcán es una de las Nuevas Siete Maravillas del Mundo — el efecto de la serpiente de luz en los equinoccios es calculado matemáticamente. Ve a primera hora (abre a las 8h) y sal antes del mediodía cuando llegan los grupos de cruceros. Duerme en Valladolid (45 min de Chichén Itzá): ciudad colonial con cenotes a 10 minutos del centro (Zaci, Samulá — el más fotogénico) y una plaza con la mejor cochinita de la península."),
            ("Días 13-15: Tulum y Riviera Maya", "Autobús desde Valladolid a Tulum (2h). Las ruinas mayas de Tulum sobre el acantilado con el Caribe turquesa al fondo son la imagen más reproducida de México. El cenote Grand Cenote a 3 km del pueblo (snorkel entre estalactitas y agua dulce transparente, 10€). Las playas de Tulum — la zona norte es más tranquila y menos cara; la zona sur tiene los beach clubs de diseño. El día 14, excursión a la Reserva de la Biósfera de Sian Ka'an (laguna, manglares, manatíes). El día 15, vuelo desde Cancún (CUN, 2h en ADO desde Tulum) de regreso.")
        ]
    }
]

for route in routes:
    cur.execute("""
        INSERT INTO destinations (
            slug, name, country, continent, type, tagline, intro,
            ideal_duration, when_to_go, how_to_get_there,
            budget_daily_low, budget_daily_mid, budget_daily_high,
            guide_quality, travel_styles
        ) VALUES (
            %s, %s, %s, %s, 'route', %s, %s,
            %s, %s, %s,
            %s, %s, %s,
            %s, %s
        ) ON CONFLICT (slug) DO NOTHING
    """, (
        route["slug"], route["name"], route["country"], route["continent"],
        route["tagline"], route["intro"],
        route["ideal_duration"], route["when_to_go"], route["how_to_get_there"],
        route["budget_daily_low"], route["budget_daily_mid"], route["budget_daily_high"],
        route["guide_quality"], route["travel_styles"]
    ))

    for (section, content) in route["days"]:
        cur.execute("""
            INSERT INTO destination_guides (destination_slug, style, section, content)
            VALUES (%s, 'itinerary', %s, %s)
            ON CONFLICT DO NOTHING
        """, (route["slug"], section, content))

conn.commit()
cur.close()
conn.close()
print("Priority 2 routes inserted successfully!")
