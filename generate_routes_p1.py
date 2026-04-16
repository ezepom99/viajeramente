#!/usr/bin/env python3
"""Priority 1: 7-day routes for top travel countries."""
import psycopg2

conn = psycopg2.connect(dbname='viajeramente', user='tenant')
cur = conn.cursor()

routes = [
    {
        "slug": "japon-7-dias",
        "name": "Japón en 7 días",
        "country": "Japón",
        "continent": "Asia",
        "tagline": "Del caos de Tokio a la serenidad de Kioto en una semana perfecta",
        "intro": "Siete días en Japón es poco, pero suficiente para enamorarse para siempre. Este itinerario conecta los grandes hitos del país —Tokio, Nikko, Hakone y el corredor Kioto-Osaka— sin sacrificar profundidad por velocidad. Cada parada tiene su razón de ser: Nikko para entender el Japón imperial, Hakone para ver el Fuji sin multitudes, Kioto para los templos, Osaka para comer hasta rendirse.\n\nLa ruta usa el JR Pass de 7 días a fondo: cómpralo antes de salir de casa porque dentro de Japón cuesta el doble. Reserva el ryokan de Hakone con al menos dos semanas de antelación, especialmente si viajas en otoño o primavera —son las temporadas más demandadas y las más espectaculares.\n\nPresupuesto orientativo: 120-180€/día en nivel medio, incluyendo alojamiento, transporte interno y comidas. El sake y el ramen de medianoche no están incluidos, pero son obligatorios.",
        "ideal_duration": ["7 días"],
        "when_to_go": "Marzo-abril (sakura) y noviembre (momiji) son las épocas más fotogénicas pero también las más masificadas. Mayo y octubre son casi igual de bonitos con la mitad de turistas. Evita agosto (calor brutal, typhoons) y semana dorada de mayo (todo reservado meses antes).",
        "how_to_get_there": "Vuelos directos desde Madrid y Barcelona a Tokio Narita (NRT) o Haneda (HND) con Iberia y Japan Airlines, unas 14h. Desde Europa del norte hay opciones más baratas con escala en Helsinki (Finnair) o Doha (Qatar). Precio medio: 700-1.100€ ida y vuelta.",
        "budget_daily_low": 85,
        "budget_daily_mid": 140,
        "budget_daily_high": 280,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Gastronomía", "Naturaleza", "Fotografía"],
        "days": [
            ("Día 1: Llegada a Tokio", "Aterrizas en Narita o Haneda y lo primero que sientes es el jet lag mezclado con fascinación. Toma el Narita Express (3.020¥) o el Keikyu desde Haneda directamente a Shinjuku. Check-in, ducha, y sal: el barrio de Shinjuku en tu primera noche japonesa es la bienvenida perfecta —luces de neón, izakayas abarrotadas, takoyaki en la calle. Duerme temprano: mañana madrugas."),
            ("Día 2: Tokio — Harajuku, Shibuya, Akihabara", "Empieza en el santuario Meiji (llegad antes de las 9h para tenerlo casi solo), después Harajuku y la calle Takeshita, y come en alguno de los restaurantes de ramen de la zona de Shibuya. Por la tarde, el cruce de Shibuya a las 18h es obligatorio —es el cruce peatonal más transitado del mundo y a esa hora se vuelve caótico de la mejor forma. Termina en Akihabara si te interesa la cultura gamer/anime, o en un bar de jazz en Shimokitazawa."),
            ("Día 3: Excursión a Nikko", "Tren desde Tokio (2h en Shinkansen + local, o directo en el Nikko-go limitado de Tobu desde Asakusa por unos 1.300¥). El Tosho-gu es excesivo en el buen sentido: lacas rojas, monos de la sabiduría y el mausoleo de Tokugawa Ieyasu. Sube después al lago Chuzenji —30 minutos en bus— para almorzar con vistas. Vuelve a Tokio para cenar en el mercado de Tsukiji (el exterior, el interior se trasladó a Toyosu)."),
            ("Día 4: Hakone — Fuji y onsen", "Toma el Romancecar desde Shinjuku (1h50min, reserva asiento con antelación) hasta Hakone. El pase Hakone Free Pass cubre el rotenburo, el funicular al volcán Owakudani y el barco por el lago Ashi. Si el Fuji está despejado —nada garantizado— la vista desde el barco es imbatible. Alójate en un ryokan con onsen al aire libre: es la noche más cara del viaje (150-300€) pero también la más memorable. Kaiseki de 8 platos incluido."),
            ("Día 5: Kioto — Fushimi Inari y Gion", "Shinkansen Hikari desde Odawara a Kioto (2h, cubierto por JR Pass). Deja el equipaje en el hotel y ve directo a Fushimi Inari: empieza a subir antes de las 7h o después de las 17h para evitar el colapso de turistas. Come en Nishiki Market (el 'kitchen de Kioto'). Por la tarde, Gion al atardecer tiene la mayor probabilidad de ver a una maiko de verdad caminando entre los machiya. Cena en un restaurante de tofu kaiseki —no tan caro como parece, desde 40€."),
            ("Día 6: Kioto — Arashiyama y templos del norte", "Arashiyama temprano (el bambú antes de las 8h es otra cosa), después el templo Tenryu-ji y su jardín zen, y los monos de Iwatayama si llevas niños —o ganas. Come en el barrio de Arashiyama y por la tarde ve al Kinkaku-ji (el Pabellón de Oro) y al Ryoan-ji para el jardín de piedras más famoso del mundo. Termina en el templo Nijo-jo. Duerme en Kioto o muévete ya a Osaka (40 min en tren local)."),
            ("Día 7: Osaka — Dotonbori, Namba, vuelo de regreso", "Si dormiste en Kioto, tren de las 9h a Osaka. El barrio de Dotonbori es kitsch en el mejor sentido: el cartel del cangrejo, el takoyaki que se hace delante de ti, el okonomiyaki que te mancha la camisa. Namba para compras de último minuto, y si tu vuelo es nocturno tienes tiempo de subir al Osaka Castle por la mañana. El aeropuerto de Kansai (KIX) está a 70 min del centro en el Haruka Express.")
        ]
    },
    {
        "slug": "tailandia-7-dias",
        "name": "Tailandia en 7 días",
        "country": "Tailandia",
        "continent": "Asia",
        "tagline": "Templos dorados, jungla en el norte y playas de postal en el sur",
        "intro": "Tailandia en una semana es uno de los itinerarios más satisfactorios de Asia: hay suficiente variedad —ciudad, montaña, playa— como para no aburrirse, y la infraestructura turística es tan buena que los desplazamientos casi nunca arruinan el viaje. Este recorrido une Bangkok, Chiang Mai y las islas del sur con vuelos domésticos baratos (AirAsia y Thai Lion Air), dejando tiempo real en cada lugar.\n\nEl secreto de Tailandia es bajar el ritmo. Los mejores momentos no están en los itinerarios: están en el night market callejero donde comes por 1,5€, en el tuk-tuk que tomas con desconfianza y terminas siendo tu transporte favorito, en el monje que te explica su templo en inglés a las 6 de la mañana.\n\nPresupuesto: Tailandia es de los destinos más accesibles de Asia. Puedes viajar bien por 40-60€/día en nivel medio, incluyendo vuelos domésticos. Nivel mochilero: 25-35€. Nivel boutique: 80-150€.",
        "ideal_duration": ["7 días"],
        "when_to_go": "Noviembre-febrero es la temporada perfecta: sin lluvia, temperaturas soportables (28-32°C). Marzo-mayo es seco pero muy caluroso. La temporada de lluvias (junio-octubre) en el norte no es tan mala si vas a Chiang Mai, pero el sur puede tener ciclones. Songkran (festival del agua, abril) es caótico y divertidísimo.",
        "how_to_get_there": "Vuelos directos desde Madrid con Thai Airways (11h) o con escala en Doha, Dubái o Abu Dhabi. Precio habitual: 500-800€ ida y vuelta. Llegar a Bangkok Suvarnabhumi (BKK) es lo más cómodo; el aeropuerto de Don Mueang (DMK) es más barato pero solo para vuelos de bajo coste.",
        "budget_daily_low": 30,
        "budget_daily_mid": 60,
        "budget_daily_high": 130,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Playa", "Gastronomía", "Naturaleza"],
        "days": [
            ("Día 1: Bangkok — llegada y primer golpe de calor", "El aeropuerto de Suvarnabhumi está a 30 km del centro. Toma el Airport Rail Link (45 min, 45 baht) hasta Phaya Thai y de ahí BTS Skytrain a tu hotel. El calor de Bangkok en la calle es un choque físico real —no te preocupes, en dos días te acostumbras. Primera noche en el barrio de Silom o Sukhumvit: come pad thai en un puesto callejero (60-80 baht), bebe una Chang bien fría y observa la ciudad. Cena en Raan Jay Fai si reservaste con semanas de antelación (vale cada baht)."),
            ("Día 2: Bangkok — templos y mercados", "Despierta antes de las 8h y ve en barco por el río Chao Phraya al Wat Pho (el Buda reclinado de 46 metros). Después, el Gran Palacio —lleva ropa que cubra hombros y rodillas o te venden un sarong en la entrada. Come en el barrio chino de Yaowarat (la mejor comida callejera de Bangkok). Por la tarde, el mercado flotante de Damnoen Saduak está a 80 km pero es una trampa turística; mejor el mercado de Chatuchak si es fin de semana (15.000 puestos, imposible salir sin comprar nada). Cóctel en el rooftop del Lebua o similar."),
            ("Día 3: Vuelo a Chiang Mai — templos del bosque", "Vuelo doméstico Bangkok-Chiang Mai (1h15min, 30-60€ con AirAsia o Thai Lion). Check-in en el casco antiguo amurallado. Por la tarde, visita el Wat Phra Singh (el más importante de la ciudad) y el Wat Chedi Luang con su chedi parcialmente destruido por un terremoto en 1545. El Sunday Walking Street o el Night Bazaar según el día de la semana —come en los puestos, no en los restaurantes para turistas."),
            ("Día 4: Chiang Mai — elefantes y jungla", "Reserva con antelación una visita ética a un santuario de elefantes (Elephant Nature Park es el más reputado, ~75€): nada de montar, solo bañarlos en el río y observarlos. Es uno de esos días que recuerdas décadas después. Por la tarde, si tienes energía, sube al Doi Suthep (templo a 1.073m de altitud, vistas de toda la ciudad, 30 min en songthaew desde el casco antiguo por 50 baht). Cena en el Khao Soi Islam o cualquier local que sirva khao soi —es el plato de Chiang Mai y es sublime."),
            ("Día 5: Vuelo al sur — Koh Samui o Krabi", "Vuelo a Koh Samui (USM) o a Krabi (KBV) según la época del año: en nov-abril ambas están bien, en mayo-oct mejor Krabi (costa andamán se protege antes de los monzones del golfo). Tarde de playa y descompresión total. Sunset en Lamai Beach (Samui) o en Railay Beach (Krabi, accesible solo en barco). Cena de pescado fresco en la playa —elige el que quieres directamente en la caja de hielo, lo cocinan en 15 minutos."),
            ("Día 6: Islas — snorkel, kayak, playa", "Excursión de día completo en barca: en Krabi, las islas Phi Phi o el Parque Nacional de Koh Lanta. En Samui, las islas Ang Thong (parque marino con lagunas esmeralda). El snorkel en Tailandia es espectacular incluso para no iniciados —peces loro, tortugas marinas y arrecifes de coral en aguas de 28°C. Vuelta al atardecer, masaje tailandés en la playa (300-500 baht = 8-14€, el mismo precio que en Bangkok), cena ligera."),
            ("Día 7: Última mañana en las islas — vuelo de regreso", "Última mañana para lo que quede pendiente: el amanecer en la playa, un último baño, compras en el mercado local. Los vuelos de regreso desde el sur suelen hacer escala en Bangkok —calcula al menos 3h de margen para el vuelo internacional. Si tu vuelo sale muy tarde, guarda equipaje en el aeropuerto de Suvarnabhumi (hay consigna 24h) y pasa el tiempo en el barrio de Bangrak.")
        ]
    },
    {
        "slug": "vietnam-7-dias",
        "name": "Vietnam en 7 días",
        "country": "Vietnam",
        "continent": "Asia",
        "tagline": "De los arrozales de Hanói a las aguas turquesas de la bahía de Ha Long y las callejuelas de Hội An",
        "intro": "Vietnam en una semana te deja con ganas de más —esa es la trampa y también el mejor elogio. Este itinerario se concentra en el norte y centro del país: Hanói caótica y deliciosa, la bahía de Ha Long que parece pintada, y Hội An con sus linternas y su sastrería de 48 horas. Es un viaje intenso pero manejable, con desplazamientos planificados en tren nocturno y vuelo doméstico para maximizar el tiempo.\n\nVietnam ha cambiado mucho en los últimos años: los precios han subido, el turismo de masas ha llegado a las zonas más icónicas, pero el país sigue siendo uno de los más fascinantes del mundo. La clave es salir de los circuitos trillados aunque sea dos horas: un pho a las 6 de la mañana con vietnamitas de camino al trabajo vale más que cualquier atracción de pago.\n\nPresupuesto: 35-70€/día en nivel medio. El crucero por Ha Long Long es el gasto principal (80-200€ por noche); el resto del viaje es increíblemente barato.",
        "ideal_duration": ["7 días"],
        "when_to_go": "Para Hanói y Ha Long: octubre-abril (menos lluvia, más fresco). Para Hội An: febrero-agosto (evita los tifones de septiembre-noviembre). El país es largo y el clima varía mucho entre norte y sur, así que no hay una época perfecta universal.",
        "how_to_get_there": "No hay vuelos directos desde España a Vietnam. Las mejores conexiones son vía Doha (Qatar, ~14h total), Dubái (Emirates) o Bangkok/Singapur. Llega a Noi Bai (Hanói, HAN) y sal por Da Nang (DAD) para Hội An. Precio: 600-900€ ida y vuelta.",
        "budget_daily_low": 25,
        "budget_daily_mid": 55,
        "budget_daily_high": 120,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Gastronomía", "Naturaleza", "Aventura"],
        "days": [
            ("Día 1: Hanói — el casco antiguo y sus 36 gremios", "Aterriza en Noi Bai y toma el bus 86 al centro (45 min, 35.000 dong = 1,3€). El casco antiguo de Hanói tiene 36 calles, cada una dedicada históricamente a un gremio: la calle del papel, la del bambú, la de la seda. Pasear sin rumbo es la actividad. Toma un bia hoi (cerveza vietnamita de barril, 20 céntimos) sentado en un taburete de plástico en el cruce de Luong Ngoc Quyen. Cena: bun cha en el mismo restaurante donde Obama comió con Anthony Bourdain en 2016 (Bun Cha Huong Lien, 24 Le Van Huu)."),
            ("Día 2: Hanói — Hoan Kiem, Museo Ho Chi Minh, tarde libre", "Mañana en el lago Hoan Kiem (el templo de la Tortuga al amanecer tiene otra dimensión). Visita el Mausoleo de Ho Chi Minh si te interesa —cierra por las tardes y los lunes y viernes. El Museo de Historia de Vietnam es mejor que muchos museos europeos y cuesta 40.000 dong. Por la tarde, el mercado de Dong Xuan para ver cómo compran los locales. Noche: el Hanói Old Quarter Night Market si es fin de semana, o una clase de cocina vietnamita (muchas academias hacen clases vespertinas por 25-35€)."),
            ("Día 3-4: Bahía de Ha Long — crucero 2 días/1 noche", "Bus desde Hanói hasta el puerto de Tuan Chau (3,5h). Crucero por Ha Long: embarcaciones de madera o junco con camarotes, kayak entre las formaciones kársticas, cueva Sung Sot (la más espectacular), y esa cena en cubierta mientras el sol se pone entre los islotes. La diferencia entre un crucero de 80€ y uno de 200€ es real: habitaciones más amplias, menos turistas, mejor comida. Evita los cruceros de 1 noche en temporada alta —el segundo día sin el gentío de los day-trippers es otra cosa. Regresa a Hanói la tarde del día 4."),
            ("Día 5: Tren nocturno a Da Nang", "Tarde libre en Hanói (última vuelta por el casco antiguo, compras). Tren nocturno SE3 o SE5 a las 19h-22h desde Hanói a Da Nang (literas blandas, 20-35€, 16h de trayecto). Duerme en el tren. El paisaje al amanecer mientras el tren bordea la costa central vietnamita es uno de esos momentos de viaje que no olvidarás."),
            ("Día 6: Hội An — linternas, sastrería y comida", "Llegada a Da Nang por la mañana, taxi o Grab a Hội An (30 km, 8-10€). La ciudad antigua de Hội An es Patrimonio de la Humanidad y merece cada centímetro cuadrado de su estatus: casas comerciales chinas del siglo XVI, el Puente Japonés, los talleres de seda. Si necesitas ropa hecha a medida, elige la sastrería el primer día y recógela el último (son rápidos y buenos). Tarda al menos 2 horas en pasear por el mercado central. Por la tarde, alquila una bici y pedalea hasta la playa de An Bang (4 km, playa sin masificar)."),
            ("Día 7: Último día en Hội An — vuelo de regreso", "Mañana temprana en el casco antiguo antes de que lleguen los grupos: las linternas de colores, los puestos de cao lau (el plato local, hecho con agua del único pozo de Hội An según la tradición) y el silencio de las 7h son el mejor recuerdo posible. Taxi a Da Nang (aeropuerto DAD), vuelo a Hanói o conexión directa internacional. Si tienes vuelo tarde, Da Nang tiene una playa urbana magnífica a 10 minutos del aeropuerto.")
        ]
    },
    {
        "slug": "marruecos-7-dias",
        "name": "Marruecos en 7 días",
        "country": "Marruecos",
        "continent": "África",
        "tagline": "De la medina de Marrakech al silencio del desierto del Sáhara pasando por la Fez imperial",
        "intro": "Marruecos es el viaje de larga distancia más accesible desde España —a 35 minutos en ferry o 3 horas en avión, y sin cambio horario. Pero no lo confundas con un destino fácil: sus medinas son laberintos reales, el regateo es un arte social que requiere paciencia, y el contraste entre la modernidad de Marrakech y la tradición milenaria de Fez puede desconcertar. Eso es exactamente lo que lo hace fascinante.\n\nEste itinerario de 7 días conecta las dos ciudades imperiales más importantes, el desierto de Merzouga y la cordillera del Atlas. Es un viaje de contrastes: los colores de la medina de Fez, el silencio absoluto del erg Chebbi al amanecer, el bullicio de Djemaa el-Fna al anochecer. La mejor forma de hacerlo es con coche de alquiler o con un conductor local contratado para la parte del desierto (150-200€ el coche con conductor por día).\n\nPresupuesto: 50-90€/día incluyendo el tour al desierto. Las riads son baratas y mucho mejores que los hoteles de cadena.",
        "ideal_duration": ["7 días"],
        "when_to_go": "Marzo-mayo y septiembre-noviembre son los mejores meses: temperaturas suaves en las ciudades y desierto, sin el calor brutal del verano (45°C en Merzouga en agosto). El Ramadán cambia el ritmo del país —los restaurantes cierran de día pero la vida nocturna es única.",
        "how_to_get_there": "Vuelos directos desde Madrid, Barcelona, Málaga y Sevilla a Marrakech Menara (RAK) con Ryanair, Vueling e Iberia. También desde Madrid a Fez (FEZ) directamente. Precio: 80-250€ ida y vuelta. Otra opción: ferry Algeciras-Tánger y ruta por tierra.",
        "budget_daily_low": 35,
        "budget_daily_mid": 65,
        "budget_daily_high": 140,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Aventura", "Gastronomía", "Fotografía"],
        "days": [
            ("Día 1: Llegada a Marrakech — la plaza que nunca duerme", "Aterrizas en Menara, taxi hasta la medina (15-20 min, precio pactado antes: ~80 dirhams). No intentes orientarte enseguida: la medina de Marrakech es un laberinto diseñado para que te pierdas. Déjate llevar. La plaza Djemaa el-Fna cambia de cara cada hora: por la mañana hay zumo de naranja y dentistas ambulantes; al anochecer, encantadores de serpientes, músicos gnaoua y cientos de puestos de comida humeante. Cena en un puesto de la plaza: elige uno con mucha gente local, no el que tiene al niño jalándote del brazo."),
            ("Día 2: Marrakech — souks, jardines y palacios", "Mañana en los souks: empieza en la zona de las tenerías (curtidurías) y trabaja hacia el interior. Los vendedores son insistentes pero no agresivos —un 'no gracias' firme funciona. Visita el Palacio Bahía y las Tumbas Saadíes (reserva online, hay colas). Come en el mercado central (Marché Central) o en cualquier restaurante de la medina donde el menú del día cuesta 50-80 dirhams. Por la tarde, los jardines de la Majorelle (casa de Yves Saint Laurent, 150 dirhams de entrada) son un oasis de calma."),
            ("Día 3: Marrakech → Ouarzazate → Valle del Draa", "Salida temprano en coche hacia Ouarzazate cruzando el paso de montaña Tizi n'Tichka (2.260m): el paisaje del Alto Atlas es de película, literalmente —Ouarzazate es 'Hollywood del desierto' y aquí se rodaron Gladiator y Juego de Tronos. Visita las kasbahs de Aït Benhaddou (Patrimonio UNESCO, 50 dirhams). Por la tarde, continúa por el Valle del Draa con sus palmerales infinitos hasta Zagora o Agdz. Noche en una kasbah-hotel."),
            ("Día 4: Desierto de Merzouga — el erg Chebbi", "Conducción por la Ruta de las Mil Kasbahs (N10) hacia Merzouga. Las dunas del erg Chebbi aparecen de repente, naranja intenso sobre el azul del cielo. Excursión en dromedario al atardecer (negociado directamente en el campamento, ~30€ por persona) y noche en un campamento jaima con cena bereber y música bajo las estrellas. El silencio del desierto en mitad de la noche, sin contaminación lumínica, con la Vía Láctea visible a simple vista, es una de esas experiencias que cambian perspectivas."),
            ("Día 5: Desierto → Fez por el sur", "Madruga para ver el amanecer sobre las dunas (imprescindible). Después, larga conducción hacia el norte por Erfoud, Midelt y el paso del Medio Atlas hasta Fez (unas 5-6h). Si tienes tiempo, para en Azrou para ver los monos bárbaro del bosque de cedros. Llegada a Fez al atardecer, cena en la medina de Bou Jeloud."),
            ("Día 6: Fez — la medina más antigua del mundo", "Fez el Bali es la medina mejor conservada del mundo islámico: 9.000 callejuelas, más de 300.000 habitantes, sin coches. Empieza en la madraza Bou Inania, sigue a las tenerías de Chouara (el espectáculo de los tintes en cubetas de colores visto desde las terrazas de cuero, gratis), la mezquita Karaouine y el fondo de la medina donde los artesanos trabajan exactamente igual que hace 500 años. Come en Café Clock (famoso por la hamburguesa de camello, pero también por el cuscús). Noche en un riad de la medina."),
            ("Día 7: Fez — última mañana, vuelo de regreso", "Última vuelta matutina por la medina sin agenda: un hammam tempranero (20-40 dirhams en uno local, no en el turístico), té con menta en cualquier tetería, compras de cerámica azul de Fez (la más auténtica de Marruecos). Taxi al aeropuerto de Fez-Saís (FEZ) para vuelo directo a España. Alternativa: vuelo desde Casablanca si sale más barato (1,5h en bus o tren desde Fez).")
        ]
    },
    {
        "slug": "islandia-7-dias",
        "name": "Islandia en 7 días",
        "country": "Islandia",
        "continent": "Europa",
        "tagline": "La Ring Road en una semana: géiseres, cascadas, glaciares y auroras boreales",
        "intro": "Islandia es el país donde la naturaleza hace lo que le da la gana y tú simplemente observas con la boca abierta. En 7 días puedes completar los highlights de la Ring Road —la carretera que rodea toda la isla— y salir con la sensación de haber visto más paisajes distintos que en años de viaje convencional. Géiseres que explotan cada 8 minutos, cascadas que caen desde lo alto de acantilados de 60 metros, glaciares de color azul, y en invierno, el espectáculo de las auroras boreales.\n\nAlquilar un coche es casi obligatorio —el transporte público es muy limitado fuera de Reikiavik. En invierno, un 4x4 es recomendable para las carreteras de montaña (F-roads); en verano, un turismo normal funciona para la Ring Road principal. La gasolina es cara (2,3-2,6€/litro), el alojamiento también, y la comida en restaurantes es una ruina —cocina en albergues con cocina compartida y ahorra 40€/día.\n\nPresupuesto: 120-180€/día por persona incluyendo coche, gasolina, alojamiento y comida cocinada. Con restaurantes, 180-280€.",
        "ideal_duration": ["7 días"],
        "when_to_go": "Junio-agosto para el sol de medianoche, días infinitos y carreteras abiertas. Noviembre-febrero para auroras boreales y nieve, pero con días muy cortos (5-6h de luz). Septiembre-octubre es el equilibrio: posibilidad de auroras, paisajes otoñales, menos turistas.",
        "how_to_get_there": "Vuelos directos desde Madrid con Icelandair (3h) o WizzAir desde varias ciudades españolas. Icelandair permite parada técnica en Reikiavik sin coste extra en vuelos a Norteamérica. Precio: 150-400€ ida y vuelta según temporada.",
        "budget_daily_low": 100,
        "budget_daily_mid": 160,
        "budget_daily_high": 300,
        "guide_quality": 9,
        "travel_styles": ["Naturaleza", "Aventura", "Fotografía", "Senderismo"],
        "days": [
            ("Día 1: Reikiavik — llegada y Círculo Dorado", "Aterrizas en Keflavík (KEF), recoge el coche de alquiler en el aeropuerto. El Círculo Dorado (Golden Circle) está de camino a Reikiavik si lo haces en sentido inverso: el Parque Nacional de Þingvellir (donde se separan las placas tectónicas de Eurasia y América), el área geotérmica de Geysir (el géiser Strokkur explota cada 6-8 minutos) y la cascada Gullfoss de dos escalones. Llega a Reikiavik de noche, come en el Bæjarins Beztu Pylsur (la salchicha más famosa de Islandia, 5€, Obama la probó)."),
            ("Día 2: Costa sur — Seljalandsfoss, Skógafoss, playa negra", "Salida temprano hacia el este por la costa sur. Seljalandsfoss es la cascada que puedes rodear por detrás (mojarse garantizado, impermeable obligatorio). Skógafoss es más alta y más fotogénica, y desde su base hay un sendero que sube a lo alto del acantilado con vistas increíbles. La playa de arena negra de Reynisfjara con sus columnas de basalto hexagonales es uno de los lugares más dramáticos de Europa. Duerme en Vík o cerca."),
            ("Día 3: Glaciares — Jökulsárlón y Diamond Beach", "La laguna glaciar de Jökulsárlón es el momento del viaje: icebergs de color azul eléctrico flotando en silencio hacia el mar, focas tomando el sol, y la luz ártica que convierte cualquier foto en arte. A 200 metros, la Diamond Beach tiene los mismos icebergs varados en arena negra —el contraste es imposiblemente bello. Haz una excursión guiada sobre el glaciar Vatnajökull (el más grande de Europa, cubre el 8% de Islandia). Duerme en la zona de Höfn."),
            ("Día 4: Fiordos del Este — carreteras vacías y pueblos de pescadores", "El este de Islandia es lo que visitan menos turistas y lo que más sorprende: fiordos profundos, pueblos de pescadores de 200 habitantes, renos sueltos en la carretera. La ciudad de Egilsstaðir es el hub del este. El lago Lagarfljót tiene según la tradición local su propio monstruo del lago. Hoy es un día de conducción y de paradas espontáneas —un glaciar visto desde lejos, una cascada sin nombre en el mapa, un rebaño de caballos islandeses que bloquea la carretera."),
            ("Día 5: Norte — Dettifoss y área volcánica de Mývatn", "Dettifoss es la cascada más poderosa de Europa: 193 m³ de agua por segundo, el rugido se escucha a kilómetros. El área de Mývatn es volcánica y alienígena: los pseudocráteres de Skútustaðagígar, los campos de lava del Dimmuborgir y los baños geotérmicos de Mývatn Nature Baths (alternativa más tranquila y barata a la Blue Lagoon, 45€). En verano hay tantos mosquitos que se venden redes para la cara —no es broma, úsalas."),
            ("Día 6: Akureyri y la península de Snæfellsnes (o auroras)", "Akureyri es la segunda ciudad de Islandia (18.000 habitantes) con catedral, heladerías improbablemente buenas y ambiente relajado. Si tienes tiempo, la cascada Goðafoss ('cascada de los dioses') está de camino. En invierno, esta noche es la apuesta para las auroras: aleja del pueblo, apaga el coche, espera. La app 'Aurora' predice la actividad geomagnética. Si vas en verano, considera un desvío a la península de Snæfellsnes con el volcán-glaciar que inspiró a Julio Verne."),
            ("Día 7: Blue Lagoon — vuelo de regreso", "La Blue Lagoon (Bláa Lónið) está a 20 minutos del aeropuerto de Keflavík: el plan perfecto para el último día es bañarte en las aguas geotérmicas de color aguamarina (reserva online con semanas de antelación, 60-100€), y después vuelo directo a casa. Es un final de viaje ridículamente bueno. Si prefieres un comienzo, también puedes hacer la Blue Lagoon el día de llegada —el efecto del baño termal después de 4h de vuelo es inmediato.")
        ]
    },
    {
        "slug": "portugal-7-dias",
        "name": "Portugal en 7 días",
        "country": "Portugal",
        "continent": "Europa",
        "tagline": "Lisboa bohemia, palacios de Sintra, vino del Douro y la energía de Oporto",
        "intro": "Portugal es el secreto mejor guardado de Europa Occidental —aunque ya no tan secreto. En una semana puedes recorrer la columna vertebral del país: Lisboa con sus siete colinas y su fado melancólico, los palacios románticos de Sintra, el estuario del Tajo en el Alentejo, y Oporto con su ribera del Duero, sus azulejos descascarados y su vino de oporto bebido directamente en la bodega.\n\nEs un viaje sin grandes esfuerzos logísticos: Portugal es pequeño (el tamaño de Andalucía), las carreteras son buenas, los trenes funcionan y la gente es amable de manera genuina, no turística. Cada región tiene su personalidad propia y su cocina: el bacalhau en Lisboa, el vino verde en el Miño, el francesinha en Oporto.\n\nPresupuesto: 70-120€/día en nivel medio con alojamiento de calidad. Portugal sigue siendo más barato que España en hostelería.",
        "ideal_duration": ["7 días"],
        "when_to_go": "Abril-junio y septiembre-octubre: clima perfecto, sin el colapso turístico de julio-agosto. Lisboa en verano está al límite de su capacidad. El interior del país (Alentejo, Douro) es más agradable en primavera y otoño. El surf en la costa atlántica está activo todo el año.",
        "how_to_get_there": "Vuelos directos desde cualquier aeropuerto español a Lisboa (LIS) u Oporto (OPO) con Iberia, TAP, Ryanair y Vueling desde 40-120€. También en tren o coche desde Madrid (Lisboa está a 7h en coche, 10h en tren).",
        "budget_daily_low": 50,
        "budget_daily_mid": 90,
        "budget_daily_high": 180,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Gastronomía", "Naturaleza", "Relax"],
        "days": [
            ("Día 1: Lisboa — llegada y los barrios de las colinas", "Lisboa Humberto Delgado (LIS) está a 20 min del centro en metro (rojo, directo a Marquês de Pombal, 1,65€). El barrio de Alfama en tu primera tarde: sube a pie desde la Baixa Pombalina hasta el castillo de São Jorge, baja por calles donde la ropa tendida cruza de balcón a balcón y de donde sale fado en directo por las noches (Casa de Fado, Tasca do Chico). Come un pastel de nata en la Confeitaria Nacional (fundada en 1829) y decide si merece su fama —merece."),
            ("Día 2: Lisboa — Belém, LX Factory y el Tajo", "Tranvía 15E o Uber hasta Belém (15 min). La Torre de Belém es más pequeña de lo que parece en las fotos pero el entorno es bonito. El Monasterio de los Jerónimos es el edificio más impresionante de Portugal (manuelino puro, estilo único que mezcla gótico con elementos náuticos). Los pastéis de Belém en la Antiga Confeitaria son los más buenos del mundo —no es opinión, es hecho científico. Por la tarde, LX Factory en el barrio de Alcântara: un mercado industrial reconvertido con restaurantes, librerías y diseñadores locales. Domingo hay mercado de pulgas."),
            ("Día 3: Sintra — palacios de cuento", "Tren desde Lisboa Rossio a Sintra (40 min, 2,35€, frecuente). La línea de Sintra es la más bonita de los cercanías portugueses. Los palacios: el Nacional (en el pueblo, entrada libre exterior), el Pena (kitsch romántico sobre una colina, impresionante desde fuera y desde dentro), la Quinta da Regaleira (el más misterioso, con su iniciático pozo invertido). Come en el pueblo de Sintra con las típicas travesseiras (hojaldre de almendra). Vuelve a Lisboa para la noche o quédate en Sintra si encuentras buen alojamiento."),
            ("Día 4: Viaje a Oporto — el tren del Douro", "Tren Alfa Pendular desde Lisboa Oriente a Oporto Campanhã (2h45min, 25-35€, reserva con antelación). Llegada a Oporto a mediodía. Check-in en la Ribeira o en el barrio de Bonfim (más auténtico, más barato). Por la tarde, el Puente Dom Luís I a pie (las vistas del Douro son lo mejor de Oporto) y las bodegas de Vila Nova de Gaia al otro lado del río: la visita y cata en Graham's o Ramos Pinto incluye dos copas de oporto por 15-20€. Cena: francesinha (el sándwich de la resaca con salsa de cerveza que no tiene ningún sentido pero es adictivo)."),
            ("Día 5: Oporto a fondo — azulejos, librerías y playa", "La estación de São Bento tiene el vestíbulo de azulejos más bonito de Portugal (gratis, abierto todo el día). La Livraria Lello es la librería más fotografiada del mundo (cobran 5€ de entrada que descuentan si compras un libro). El Mercado do Bolhão recién reformado para comprar quesos, charcutería y vino verde. Si el día acompaña, bus o Uber hasta la playa de Matosinhos (20 min): los mejores percebes y mariscos de la costa atlántica, a precios de Portugal."),
            ("Día 6: Valle del Duero — viñedos en terrazas", "Tren o coche hacia el este por el valle del Duero: los viñedos en terrazas sobre el río son Patrimonio UNESCO y uno de los paisajes más bonitos de Europa. Los pueblos de Pinhão (2.000 habitantes, estación de tren con azulejos) y Régua son la base para catas y cruceros en barco rabelo por el río. Come en una quinta vinícola. Si vuelves en coche, la carretera nacional por la margen del Douro al atardecer es antología. Noche en Oporto de nuevo."),
            ("Día 7: Última mañana en Oporto — vuelo de regreso", "El Mercado de Matosinhos o el del Bolhão para provisiones de viaje (vino verde, licor beirão, queso curado). El mirador da Vitória para la foto panorámica de los tejados de Oporto. Vuelo desde Oporto Francisco Sá Carneiro (OPO) de regreso, o tren a Lisboa para vuelo desde allí. Deja tiempo para el inevitable retraso en el control de seguridad: el aeropuerto de Oporto es pequeño y se colapsa en temporada alta.")
        ]
    },
    {
        "slug": "grecia-7-dias",
        "name": "Grecia en 7 días",
        "country": "Grecia",
        "continent": "Europa",
        "tagline": "La Acrópolis, el volcán de Santorini y las playas turquesas de Mykonos en una semana perfecta",
        "intro": "Grecia tiene el problema del niño popular: todo el mundo quiere ir, todo el mundo sabe que es bonito, y cuando llegas te preguntas si la realidad estará a la altura del hype. La respuesta es sí. La Acrópolis de Atenas sigue siendo uno de los monumentos más impresionantes del mundo aunque hayas visto mil fotos. El volcán de Santorini sigue siendo surrealista aunque Instagram lo haya reproducido hasta la náusea. Y el Egeo sigue teniendo ese azul específico que no existe en ningún otro mar.\n\nEste itinerario de 7 días usa los ferris y los vuelos domésticos baratos para conectar Atenas, Santorini y Mykonos en la combinación clásica. Es un viaje entre cultura y hedonismo, entre ruinas milenarias y piscinas infinitas —y la mezcla funciona. La clave es reservar ferris y alojamiento en Santorini con meses de antelación en temporada alta.\n\nPresupuesto: 100-170€/día en nivel medio. Santorini es significativamente más cara que el resto de Grecia; Mykonos también. Atenas es razonable.",
        "ideal_duration": ["7 días"],
        "when_to_go": "Mayo-junio y septiembre-octubre son los meses perfectos: clima ideal, mar en temperatura, menos masificación que julio-agosto. En julio-agosto las islas están al límite y los precios se duplican. Semana Santa griega (fecha variable) es un espectáculo cultural único pero muy concurrida.",
        "how_to_get_there": "Vuelos directos desde Madrid y Barcelona a Atenas (ATH) con Iberia, Vueling y Aegean Airlines (3,5h). En temporada, también hay vuelos directos a Santorini (JTR) desde algunas ciudades españolas. Precio: 150-350€ ida y vuelta.",
        "budget_daily_low": 70,
        "budget_daily_mid": 130,
        "budget_daily_high": 280,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Playa", "Gastronomía", "Relax"],
        "days": [
            ("Día 1: Atenas — llegada y primer ouzo", "Metro desde el aeropuerto Eleftherios Venizelos hasta Sintagma (40 min, 10€). El barrio de Monastiraki y la zona del mercado de pulgas de Avissinias en tu primera tarde: ruidoso, auténtico, con la Acrópolis de fondo. Cena en Psirri, el barrio de tabernas y mezedhopolia (restaurantes de mezze): taramosalata, tzatziki, pulpo a la brasa y vino retsina. Un ouzo con hielo para terminar —adquiere el gusto en 24h.",),
            ("Día 2: Atenas — Acrópolis y Museo Arqueológico", "Llega a la Acrópolis antes de las 8h30m (abre a las 8h en temporada alta): el Partenón con luz de mañana y sin multitudes es una experiencia completamente diferente a la del mediodía. El nuevo Museo de la Acrópolis (al pie de la colina) es el mejor museo arqueológico de Europa — la sala del Partenón con los frisos originales que quedan (los otros están en el British Museum, y el debate sobre su devolución sigue abierto) es impresionante. Come en el barrio de Koukaki (más barato y local que Plaka) y tarde libre para el mercado central de Atenas o el barrio de Exarchia."),
            ("Día 3: Atenas → Santorini en ferri o avión", "Ferri desde el Pireo a Santorini (4-8h según tipo de barco, 40-80€; el high-speed ferry de Seajet hace la ruta en 4h30m). Llegada al puerto de Thira o Athinios. El teleférico hasta Fira cuesta 6€ o puedes subir en burro (discutible éticamente) o a pie (30 min, 587 escalones). Primera tarde en Fira explorando las callejuelas. Sunset desde el pueblo de Oia: llega 2h antes para conseguir sitio. El sol hundiéndose en la caldera volcánica con la cúpula azul en primer plano es exactamente como en las fotos —y aún así emociona."),
            ("Día 4: Santorini — playas volcánicas y caldera", "La playa de Perissa (arena negra volcánica) y Perivolos son las mejores del sur de la isla. La Red Beach es espectacular pero muy concurrida. Alquila un quad o scooter (25-35€/día) para moverte —los autobuses van llenos en temporada. Excursión en barco a la caldera: visita al volcán activo Nea Kameni (puedes subir a la cima con guía), baño en las aguas termales de Palea Kameni (30°C) y snorkel en aguas turquesas. Atardecer desde Oia de nuevo o desde el faro de Akrotiri."),
            ("Día 5: Santorini → Mykonos en ferri", "Ferri de Santorini a Mykonos (2-3h, 40-60€). Mykonos es más pequeña, más cara y más festiva que Santorini. Check-in y tarde de playa: Super Paradise Beach y Paradise Beach son las de fiesta; Agios Sostis y Fokos son tranquilas y preciosas. El pueblo de Mykonos (Chora) en la noche: el Barrio Pequeño con sus pelícanos (mascota oficial de la isla), los molinos de viento, los callejones blancos. Cena en el restaurante Niko's o en cualquier taverna del puerto — el marisco es el plato."),
            ("Día 6: Mykonos — isla de Delos y playa", "La isla de Delos en ferri (30 min desde el puerto de Mykonos, 20€ ida y vuelta + 12€ entrada): considerada el centro del mundo en la antigua Grecia, lugar de nacimiento de Apolo y Artemisa, y uno de los yacimientos arqueológicos mejor conservados del Mediterráneo. Sin alojamiento permitido en la isla, tienes que volver el mismo día. Tarde de playa o de compras en el pueblo (es caro pero el diseño griego es auténtico). Última cena en Mykonos: reserva con días de antelación en temporada alta."),
            ("Día 7: Mykonos — vuelo de regreso", "Vuelo desde el aeropuerto de Mykonos (JMK) directamente a España si hay conexión, o con escala en Atenas. Los vuelos domésticos Sky Express y Aegean son frecuentes. Si tienes tiempo antes del vuelo, el barrio de Little Venice (casas sobre el mar, balcones de colores) a primera hora de la mañana, sin turistas, es el mejor recuerdo posible de las islas griegas.")
        ]
    },
    {
        "slug": "italia-7-dias",
        "name": "Italia en 7 días",
        "country": "Italia",
        "continent": "Europa",
        "tagline": "Roma eterna, la Florencia del Renacimiento y la Venecia irrepetible en un viaje de película",
        "intro": "Italia es el país que más personas en el mundo sueñan con visitar, y cuando lo conoces entiendes perfectamente por qué. En 7 días, la ruta clásica Roma-Florencia-Venecia comprime tres de las ciudades más extraordinarias de la historia de la humanidad en un viaje que mezcla arte, gastronomía, caos organizado y momentos de belleza absoluta.\n\nEl itinerario funciona de sur a norte o de norte a sur; aquí lo hacemos empezando en Roma para terminar en Venecia, que merece ser el punto de llegada emocional del viaje. Los trenes de alta velocidad de Trenitalia (Frecciarossa) conectan las tres ciudades en menos de 2 horas entre sí, así que los desplazamientos son parte del placer, no del problema.\n\nPresupuesto: 100-160€/día en nivel medio. Roma y Florencia son caras; Venecia es la más cara de las tres. Come en trattorie, no en los restaurantes de las plazas turísticas, y pagarás la mitad por el doble de calidad.",
        "ideal_duration": ["7 días"],
        "when_to_go": "Abril-mayo y septiembre-octubre son los meses ideales: clima perfecto, sin el colapso de verano. Julio-agosto en Roma y Florencia es sufrimiento climático (38°C, humedad). Venecia en verano tiene el acqua alta (inundaciones) menos probable, pero junio ya está al límite. Navidad en Italia tiene su magia propia.",
        "how_to_get_there": "Vuelos directos desde España a Roma Fiumicino (FCO), Florencia (FLR) o Venecia Marco Polo (VCE) con Iberia, Vueling y Ryanair. También en tren desde Barcelona a Milán (9h, Renfe-SNCF-Trenitalia) y de ahí al sur. Precio vuelo: 80-200€ ida y vuelta.",
        "budget_daily_low": 70,
        "budget_daily_mid": 120,
        "budget_daily_high": 250,
        "guide_quality": 9,
        "travel_styles": ["Cultura", "Gastronomía", "Arte", "Historia"],
        "days": [
            ("Día 1: Roma — llegada al Coliseo y Campo de' Fiori", "Tren Leonardo Express desde Fiumicino a Roma Termini (32 min, 14€). El Coliseo en tu primera tarde si reservaste entrada online (hazlo siempre, las colas sin reserva son de 2h en temporada). El Foro Romano y el Palatino están incluidos en la misma entrada. Cena en el barrio de Trastevere: tonnarelli cacio e pepe en Da Enzo al 29, una botella de vino por 12€ y la Roma que quieres imaginar."),
            ("Día 2: Roma — Vaticano y Panteón", "Museos Vaticanos y Capilla Sixtina (reserva online imprescindible, 2-3h mínimo). El techo de la Sixtina de Miguel Ángel con buena luz y antes de las 10h es diferente a verlo con 500 personas apiñadas. La Plaza de San Pedro a mediodía. Por la tarde, el Panteón (ahora cuesta 5€ de entrada, antes gratis) y la Fontana di Trevi (lanzar la moneda y escapar rápido de las selfies masivas). Aperitivo en el Pigneto o en San Lorenzo —los barrios más auténticos de Roma."),
            ("Día 3: Roma → Florencia en Frecciarossa", "Tren de alta velocidad Roma Termini → Florencia Santa Maria Novella (1h25min, 25-45€ según antelación). Florencia a mediodía: el Ponte Vecchio (la ciudad de los joyeros desde el siglo XIV), la Plaza de la Señoría con el David de Miguel Ángel (réplica; el original está en la Galería de la Academia). Reserva la Galería de los Uffizi para el día siguiente. Come en el Mercato Centrale (primer piso: bistec florentino, lampredotto, ribollita). Atardecer desde la Piazzale Michelangelo."),
            ("Día 4: Florencia — Uffizi, Oltrarno y bisteca", "Los Uffizi por la mañana temprano (reserva siempre): La Primavera y El Nacimiento de Venus de Botticelli son el motivo principal, pero hay cien obras más que en cualquier otro museo serían las piezas estrella. El barrio de Oltrarno (al otro lado del Arno) es la Florencia de los artesanos: encuadernadores, restauradores de muebles, joyeros. Come en la Trattoria Sostanza (fundada en 1869, la tortita al burro es legendaria). Por la tarde, el jardín de Bóboli o una visita al Palazzo Pitti."),
            ("Día 5: Florencia → Venecia en tren", "Frecciarossa Florencia → Venecia Santa Lucia (2h, 25-50€). Llegada a Venecia: pon el equipaje en el alojamiento y sal a perderte. En Venecia el mapa no funciona y el GPS tampoco —eso es parte del plan. El Gran Canal al atardecer desde el vaporetto (agua-bus, 9,50€/viaje o 25€ pase de 24h), la Plaza de San Marcos con la basílica y el Campanile al fondo. Cena de bacalà mantecato en el bacaro más antiguo que encuentres."),
            ("Día 6: Venecia — Dorsoduro, San Polo y el sestiere", "Venecia sin turistas existe: madrugar a las 6h30 y caminar hacia Cannaregio o Dorsoduro. El Museo de la Academia (la mejor colección de pintura veneciana del mundo) y la Colección Peggy Guggenheim (arte moderno en el palacio más bajo del Gran Canal). El Mercado de Rialto a media mañana para comer cicchetti (tapas venecianas: 1-2€/pieza) con un spritz Aperol (la bebida de Venecia, aunque los italianos prefieren el Campari). Si el tiempo lo permite, vaporetto a la isla de Burano (45 min): casas pintadas en colores primarios como un Mondrian real."),
            ("Día 7: Venecia — última mañana, aeropuerto", "El mejor consejo de Venecia: levántate antes que los cruceristas (suelen desembarcar a las 9h) y camina hasta Castello, el barrio más residencial y menos turístico. El Campo Santa Maria Formosa a las 7h tiene panadería abierta, gatos callejeros y ningún turista. Vaporetto hasta el Piazzale Roma, autobús al aeropuerto Marco Polo (20 min) o motoscafo acuático (30 min, 15€). Último café en el aeropuerto y vuelo de vuelta a casa, ya pensando en cuándo volver.")
        ]
    }
]

# Insert routes
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
print("Priority 1 routes inserted successfully!")
