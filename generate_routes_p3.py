#!/usr/bin/env python3
"""Priority 3: 21-day routes."""
import psycopg2

conn = psycopg2.connect(dbname='viajeramente', user='tenant')
cur = conn.cursor()

routes = [
    {
        "slug": "japon-21-dias",
        "name": "Japón en 21 días",
        "country": "Japón",
        "continent": "Asia",
        "tagline": "Tres semanas para entender el alma de Japón: del norte de Hokkaido a los arrecifes de Okinawa",
        "intro": "Tres semanas en Japón es el tiempo mínimo para ir más allá del circuito turístico y acercarse al Japón que los japoneses conocen: el Hokkaido salvaje del norte con sus osos y sus fields de lavanda, la Tohoku de las onsen volcánicas y los festivales de nieve, los Alpes del centro, el corredor Kioto-Osaka-Nara, y si el tiempo lo permite, las islas subtropicales de Okinawa con sus arrecifes de coral.\n\nEste itinerario requiere planificación seria: el JR Pass de 21 días (680€ aprox.) cubre prácticamente todo, pero algunos tramos necesitan reserva de asiento con antelación, especialmente en temporada alta. Los precios de alojamiento en Hokkaido y Okinawa son más bajos que en Tokio; aprovecha para quedarte en ryokans auténticos sin el premium de la capital.\n\nPresupuesto: 130-200€/día incluyendo JR Pass, alojamiento mixto con noches en ryokan, y comidas. Japón no es barato si comes en restaurantes todo el tiempo, pero el convenience store japonés (7-Eleven, FamilyMart, Lawson) tiene comida caliente de calidad real a 2-4€.",
        "ideal_duration": ["21 días"],
        "when_to_go": "Marzo-mayo y septiembre-noviembre. Para Hokkaido: julio-agosto para el verano y la lavanda, febrero para el Festival de Nieve de Sapporo. Para Okinawa: mayo-octubre (agua caliente para el arrecife). Evitar el Golden Week (finales de abril-inicio de mayo) para el transporte y los hoteles.",
        "how_to_get_there": "Vuelo a Tokio Narita (NRT) o Haneda (HND). Si terminas en Okinawa, el regreso puede ser desde Naha (OKA) con escala en Osaka o Tokio. JR Pass de 21 días comprado en España antes de salir.",
        "budget_daily_low": 100,
        "budget_daily_mid": 165,
        "budget_daily_high": 320,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Naturaleza", "Gastronomía", "Fotografía"],
        "days": [
            ("Semana 1: Tokio y alrededores (Días 1-7)", "Los primeros tres días en Tokio sin prisa: Shinjuku y el Golden Gai (los micro-bares de 6 taburetes donde caben los mejores barmans del mundo), Harajuku y Yoyogi, Asakusa y el Senso-ji con el mercado Nakamise. El día 4, excursión a Nikko (mausoleo de Tokugawa) y al día siguiente a Kamakura (el Gran Buda de 13 metros al aire libre, los templos zen de Engaku-ji y Kencho-ji, la playa de Yuigahama). El día 6, Hakone y las vistas del Fuji. El día 7, Yokohama: la Chinatown más grande de Japón, el barrio de Minato Mirai y el museo de la taza de ramen (sí, existe y es interesante)."),
            ("Semana 2: Japón central y los Alpes (Días 8-14)", "Shinkansen a Nagoya y bus a Takayama (2h): el Japón rural más auténtico, las destilerías de sake Hirata y las casas machiya de 300 años. Día 9 excursión a Shirakawa-go y Gokayama (las aldeas gassho-zukuri con tejados de paja inclinados bajo nieve en invierno). Día 10: bus a Kanazawa, el 'Kioto del oeste', con su jardín Kenroku-en (uno de los tres mejores del país) y el mercado de marisco Omi-cho. Días 11-12: Kioto a fondo — Fushimi Inari, Arashiyama, Nishiki Market, las geishas de Gion al atardecer. Día 13: Nara (los ciervos sagrados y el Todai-ji). Día 14: Hiroshima y Miyajima (torii rojo en el mar)."),
            ("Semana 3: Hokkaido y/o Okinawa (Días 15-21)", "Vuelo desde Osaka a Sapporo (Hokkaido, 2h) o a Naha (Okinawa, 2h30min) según la época del año. Hokkaido en verano: el lago Toya, el volcán Showa-Shinzan, los campos de lavanda de Furano (julio) y el Parque Nacional Daisetsuzan con los mejores senderos de Japón. Hokkaido en invierno: el Festival de Nieve de Sapporo (febrero), las fuentes termales de Noboribetsu y el drift ice de Abashiri. Okinawa en cualquier época: los arrecifes de Kerama (el mejor buceo/snorkel de Japón), el castillo de Shuri (Ryukyu), la gastronomía de la longevidad (champuru de tofu, goya, beni-imo) y el ritmo de las islas subtropicales, tan distinto al Japón continental.")
        ]
    },
    {
        "slug": "sudeste-asiatico-21-dias",
        "name": "Sudeste Asiático en 21 días",
        "country": "Tailandia",
        "continent": "Asia",
        "tagline": "Tailandia, Vietnam y Camboya en tres semanas: el grand tour del Sudeste Asiático",
        "intro": "El Sudeste Asiático en tres semanas es el viaje iniciático de muchos viajeros y el viaje favorito de muchos veteranos. Combinar Tailandia, Vietnam y Camboya en un solo recorrido permite ver la diversidad de la región: la modernidad de Bangkok frente a la melancolía de Hanói, los templos khmer de Angkor frente a los torii budistas de Chiang Mai, las playas del Golfo de Tailandia frente a la bahía de Ha Long.\n\nLa logística es manejable con vuelos de bajo coste asiáticos: AirAsia, VietJet, Cambodia Angkor Air y Bangkok Airways conectan toda la región por 20-60€ por trayecto. La ruta clásica es Bangkok-Chiang Mai-Hanói-Hội An-Ho Chi Minh City-Siem Reap-Bangkok, que se puede hacer en sentido contrario o con variaciones.\n\nPresupuesto: 40-70€/día con vuelos domésticos incluidos. Es uno de los viajes más accesibles del mundo en términos de calidad-precio: cenas extraordinarias por 3-5€, habitaciones con vista al mar por 25-40€, masajes de 90 minutos por 8€.",
        "ideal_duration": ["21 días"],
        "when_to_go": "Noviembre-febrero es la temporada perfecta para toda la región. Marzo-mayo: caluroso pero seco. Mayo-octubre: temporada de lluvias (diferente intensidad por zonas). El Año Nuevo khmer (abril) en Camboya y el Songkran tailandés (abril) son festivales únicos pero con alojamiento más caro.",
        "how_to_get_there": "Vuelo a Bangkok Suvarnabhumi (BKK) como entrada. Regreso desde Siem Reap (REP) a Bangkok y de ahí a Europa, o vuelo directo desde Phnom Penh con escala. Precio: 550-850€ ida y vuelta.",
        "budget_daily_low": 28,
        "budget_daily_mid": 55,
        "budget_daily_high": 130,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Naturaleza", "Playa", "Aventura"],
        "days": [
            ("Semana 1: Tailandia — Bangkok y norte (Días 1-7)", "Días 1-2 en Bangkok: el Gran Palacio y Wat Pho, el barrio chino de Yaowarat, el mercado nocturno de Talad Rot Fai, el tuk-tuk como filosofía de vida. Día 3: vuelo Bangkok-Chiang Mai (1h, 25€). Días 4-5 en Chiang Mai: el santuario ético de elefantes (el mejor día de la semana), los templos del casco histórico, la clase de cocina tailandesa en un mercado local, el Night Bazaar para artesanía. Día 6: Chiang Rai y el Templo Blanco (Wat Rong Khun, excentrismo budista llevado a la excelencia). Día 7: Triángulo de Oro y la frontera con Myanmar y Laos, el museo del opio, el río Mekong desde el mirador."),
            ("Semana 2: Vietnam (Días 8-14)", "Vuelo Chiang Mai-Hanói (2h con escala en Bangkok, 40-70€). Días 8-9 en Hanói: el bun cha de Obama, el lago Hoan Kiem, el barrio de los 36 gremios, la ópera del agua (muclas, 6€, 50 minutos de magia). Días 10-11: crucero de 2 noches en la Bahía de Ha Long (reserva barco de calidad media-alta). Día 12: tren nocturno Hanói-Da Nang. Día 13 en Hội An: la ciudad de las linternas, la sastrería de 48h, la playa de An Bang en bici. Día 14: vuelo Da Nang-Ho Chi Minh City (1h15min) y primera noche en Saigón."),
            ("Semana 3: Ho Chi Minh City y Camboya (Días 15-21)", "Días 15-16 en Saigón: el Museo de los Vestigios de la Guerra (imprescindible y duro), los túneles de Cu Chi (la red subterránea de la resistencia vietnamita, 70 km de túneles bajo la selva), el barrio de Bui Vien en su apogeo nocturno. Día 17: bus o vuelo a Siem Reap (Camboya, 4h en bus o 45min en vuelo). Días 18-19: Angkor — el complejo arqueológico más grande del mundo. Angkor Wat al amanecer (llegada antes de las 5h30m), Angkor Thom y el Bayon (las caras de piedra emergiendo de la selva), Ta Prohm (el templo donde los árboles han absorbido las piedras, el de Lara Croft). Día 20: los templos menores de Banteay Srei (escultura más refinada del Imperio Khmer) y el lago Tonle Sap (el mayor lago de Sudeste Asiático, que se cuadruplica en la estación de lluvias). Día 21: vuelo Siem Reap-Bangkok para conexión internacional.")
        ]
    },
    {
        "slug": "mexico-21-dias",
        "name": "México en 21 días",
        "country": "México",
        "continent": "América",
        "tagline": "México completo: megalópolis azteca, Oaxaca indígena, Chiapas selvático y el Yucatán maya",
        "intro": "México en tres semanas es el viaje completo que el país se merece: el tiempo suficiente para ir más allá de los circuitos habituales y llegar a la Chiapas de los indígenas tzeltales y tzotziles, a los ríos subterráneos de Yucatán, a los mercados de Tlaxiaco donde todavía se habla mixteco antes que español. México tiene capas y capas de historia, y con 21 días puedes pelar bastantes.\n\nEste itinerario añade a la ruta de 15 días el estado de Chiapas (San Cristóbal de las Casas, las cascadas de Agua Azul, las ruinas mayas de Palenque) y tiempo extra en el Yucatán para los cenotes más remotos y la laguna de Bacalar, el 'lago de los siete colores' que los turistas aún no han masificado del todo.\n\nPresupuesto: 55-100€/día incluyendo vuelos domésticos. México tiene una red de autobuses ADO de primera clase muy cómoda y económica (10-25€ entre ciudades) que puedes usar para muchos tramos si el tiempo no aprieta.",
        "ideal_duration": ["21 días"],
        "when_to_go": "Noviembre-abril: temporada seca en todo el itinerario. El Día de los Muertos en Oaxaca (1-2 noviembre) requiere reservar alojamiento con 6 meses de antelación pero es una experiencia única en el mundo. Diciembre-enero tiene clima perfecto pero más turistas en el Yucatán. Julio-agosto es temporada de lluvias pero Chiapas está especialmente verde.",
        "how_to_get_there": "Vuelo directo Madrid-Ciudad de México (MEX) con Iberia o Aeromexico, 12h. Regreso desde Cancún (CUN) directamente. Vuelo open jaw (entrada y salida por distintos aeropuertos): busca en Skyscanner como vuelo abierto.",
        "budget_daily_low": 38,
        "budget_daily_mid": 75,
        "budget_daily_high": 170,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Naturaleza", "Gastronomía", "Aventura"],
        "days": [
            ("Semana 1: CDMX, Puebla y Oaxaca (Días 1-7)", "Días 1-3 en Ciudad de México: el Centro Histórico y el Zócalo, Teotihuacán al amanecer (las pirámides del Sol y la Luna antes de las 9h), el barrio de Coyoacán (casa azul de Frida Kahlo, mercado de sabores, el parque con sus ajolotes), la Zona Rosa y la Condesa para la noche. Día 4: autobús a Puebla (2h), la ciudad de los talaveras y del mole poblano, las iglesias barrocas más ornamentadas de México, la salsa de chile de los fondas del mercado El Parián. Días 5-7: vuelo o autobús a Oaxaca (1h avión / 5h bus): los tres mejores días del viaje si eres gastrónomo. Monte Albán al amanecer, el mezcal artesanal en el pueblo de Santiago Matatlán (the mezcal capital of the world), el mercado de Tlacolula en domingo, el árbol de Tule."),
            ("Semana 2: Chiapas (Días 8-14)", "Vuelo Oaxaca-Tuxtla Gutiérrez (1h30min) y minivan a San Cristóbal de las Casas (1h). San Cristóbal es la ciudad más bonita de México para muchos viajeros: colonial, multicultural, con comunidades indígenas tzotziles y tzeltales que bajan al mercado con sus trajes tradicionales. Días 9-10: excursiones desde San Cristóbal al Cañón del Sumidero (río y acantilados de 1.000m), los pueblos indígenas de San Juan Chamula (la iglesia sincrética donde se mezcla el catolicismo con el chamanismo maya) y Zinacantán. Días 11-12: Palenque — las ruinas mayas más espectaculares de México, en el borde de la selva lacandona, con el palacio, el templo de las Inscripciones y la tumba del rey Pakal a 25 metros bajo tierra. Las cascadas de Agua Azul y Misol-Ha de camino. Días 13-14: vuelo desde Villahermosa a Mérida (1h30min con escala o directo)."),
            ("Semana 3: Yucatán completo (Días 15-21)", "Días 15-16 en Mérida: el Paseo de Montejo, la cochinita pibil del mercado Lucas de Gálvez para el desayuno, la ruta Puuc (Uxmal, Kabah, Sayil). Día 17: Chichén Itzá antes de las 9h y Cenote Ik-Kil (el cenote más fotogénico del Yucatán, 60m de diámetro, raíces que cuelgan desde lo alto). Noche en Valladolid. Día 18: Tulum y las ruinas sobre el acantilado con el Caribe de fondo, el cenote Grand Cenote. Día 19: Bacalar — la laguna de los siete colores, 60 km de agua dulce con tonos del turquesa al añil, kayak entre manglares, ningún oleaje, sin medusas. El Fuerte de San Felipe con la historia de los piratas y los mayas. Día 20: Akumal (bahía de las tortugas, snorkel directo desde la playa) y regreso a Cancún. Día 21: si el vuelo es tarde, el Muelle de Cancún o Isla Mujeres (20 min en ferry) para una última mañana de Caribe antes del vuelo de regreso.")
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
print("Priority 3 routes inserted successfully!")
