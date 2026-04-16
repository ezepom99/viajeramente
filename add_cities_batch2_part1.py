import psycopg2
import json

conn = psycopg2.connect("dbname=viajeramente user=tenant")
cur = conn.cursor()

cities = [
# EUROPA
{
    "slug": "dublin", "name": "Dublín", "country": "Irlanda", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 53.3498, "lng": -6.2603},
    "tagline": "Pubs con historia, costa salvaje y la hospitalidad más genuina de Europa",
    "intro": "Dublín es una ciudad que se disfruta a pie y a ritmo de pinta. El Trinity College con el Libro de Kells, el castillo, el barrio georgiano de Merrion Square y la animada Temple Bar forman el núcleo histórico, pero la ciudad real está en sus pubs de barrio, donde la conversación fluye tan naturalmente como la Guinness.\n\nMás allá del centro, Howth ofrece acantilados y mariscos frescos a 30 minutos en DART, mientras que las Wicklow Mountains están a menos de una hora. Los barrios de Portobello y Rathmines tienen la mejor escena de cafés y restaurantes de la ciudad.\n\nDublín es cara para ser Europa del Este, pero tiene carácter propio que pocas capitales europeas conservan. Los irlandeses son genuinamente amistosos y las conversaciones en el pub son parte del atractivo.",
    "when_to_go": "Mayo-septiembre es la ventana óptima: días largos, temperaturas de 15-20°C y la mayoría de festivales. Junio y julio son los mejores meses aunque llueve igualmente. El invierno es gris y frío (5-10°C) pero los pubs están llenos y los precios bajan. Evita el fin de semana de San Patricio (17 marzo) si no buscas turismo de borrachera masiva.",
    "how_to_get_there": "El aeropuerto de Dublín conecta con toda Europa. El Airlink Express llega al centro en 30-45 min (7€). Ferrys desde Holyhead (Gales) y Liverpool para quien viene del Reino Unido.",
    "where_to_sleep": [
        {"name": "Temple Bar / City Centre", "description": "El corazón turístico, cómodo pero ruidoso los fines de semana. Hostels desde 25€, hoteles desde 90€."},
        {"name": "Portobello / Rathmines", "description": "El barrio más local y con mejor gastronomía. 20 min a pie al centro. Apartamentos desde 80€/noche."},
        {"name": "Docklands", "description": "Zona moderna junto al río Liffey. Buenos hoteles de diseño desde 100€, tranquilo y bien conectado."}
    ],
    "what_to_do": [
        {"title": "Trinity College y Libro de Kells", "description": "El manuscrito iluminado del siglo IX es uno de los tesoros medievales más impresionantes del mundo. Reserva online (14€)."},
        {"title": "Guinness Storehouse", "description": "El museo de la cerveza más visitado de Europa, con degustación en la Sky Bar con vistas panorámicas (26€). Turístico pero genuinamente bueno."},
        {"title": "Pub tradicional en Mulligan's o The Stag's Head", "description": "Evita Temple Bar para el primer pub. Estos dos son de los más auténticos de Dublín, con más de 150 años de historia."},
        {"title": "DART hasta Howth o Dalkey", "description": "El tren costero llega a dos pueblos pesqueros espectaculares. Howth tiene acantilados, faro y langosta fresca. Dalkey tiene castillo y encanto."},
        {"title": "Chester Beatty Library", "description": "Uno de los mejores museos gratuitos de Europa: manuscritos islámicos, budistas y europeos de valor incalculable."},
        {"title": "Kilmainham Gaol", "description": "La cárcel donde ejecutaron a los líderes del Alzamiento de Pascua 1916. Visita guiada obligatoria (9€), muy bien narrada."}
    ],
    "food_and_drink": "La escena gastronómica dublinesa ha evolucionado enormemente. Prueba el full Irish breakfast (huevos, salchichas, black pudding), el chowder de marisco en Howth y las ostras en cualquier fishmonger. Los mercados de Temple Bar y Dún Laoghaire tienen buen street food. Pinta de Guinness entre 5-7€ en pubs normales.",
    "safety": "Dublín es muy segura para turistas. El centro tiene algo de mendicidad agresiva puntual y carteristas en Temple Bar. Por la noche, Temple Bar puede ser ruidoso y con borracheras pero raramente peligroso.",
    "visa_info": "Irlanda NO forma parte del espacio Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. EEUU, Canadá, Australia: sin visado hasta 90 días. Requiere pasaporte válido.",
    "local_tips": ["Una pinta en Temple Bar cuesta el doble que en un pub de barrio — aléjate dos calles", "El Leap Card es la tarjeta de transporte recargable, imprescindible si usas buses y DART", "Los museos nacionales (Arqueología, Arte Moderno, Historia Natural) son gratuitos", "Reserva Kilmainham Gaol online — se agotan con días de antelación", "El mercado de Dún Laoghaire los fines de semana tiene los mejores productores locales"],
    "travel_styles": ["cultura", "gastronomía", "naturaleza", "historia"],
    "vibes": ["cozy", "pub culture", "literary", "atlantic"],
    "climate": ["oceanic", "rainy"],
    "best_months": ["May", "June", "July", "August", "September"],
    "budget_daily_low": 65, "budget_daily_mid": 130, "budget_daily_high": 280, "guide_quality": 8
},
{
    "slug": "bucarest", "name": "Bucarest", "country": "Rumanía", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 44.4268, "lng": 26.1025},
    "tagline": "El París del Este resurge con vida nocturna, mercados art déco y una energía imparable",
    "intro": "Bucarest fue llamada el 'París del Este' en los años 30 y aunque el comunismo dejó cicatrices arquitectónicas enormes (el Palacio del Parlamento es el segundo edificio más grande del mundo), la ciudad ha recuperado su energía con una escena cultural y nocturna que sorprende a todos los que llegan con expectativas bajas.\n\nEl barrio de Floreasca y las calles del centro histórico Lipscani concentran la mejor gastronomía, mercados vintage y bares de moda. Los precios son de los más bajos de la UE: una cerveza cuesta 1,5€ y una cena con vino sale por 15€.\n\nBucarest no es la ciudad más bonita de Europa, pero tiene autenticidad, carácter y una hospitalidad que pocas capitales europeas pueden igualar.",
    "when_to_go": "Primavera (abril-junio) y otoño (septiembre-octubre) son perfectos: 20-25°C y sin extremos. El verano puede ser muy caluroso (35°C+) pero la vida nocturna es espectacular. El invierno es frío (-5°C a 5°C) pero la ciudad tiene encanto navideño y los precios bajan aún más.",
    "how_to_get_there": "El aeropuerto Henri Coandă conecta con toda Europa. Express train al centro en 40 min (3€). Buses nocturnos económicos desde ciudades europeas (Flixbus).",
    "where_to_sleep": [
        {"name": "Lipscani (Centro Histórico)", "description": "El barrio más animado con edificios art déco restaurados. Hostels desde 12€, hoteles boutique desde 45€."},
        {"name": "Floreasca / Dorobanți", "description": "El barrio residencial más agradable, con los mejores restaurantes y cafés. Apartamentos desde 40€/noche."},
        {"name": "Aviatorilor", "description": "Cerca del parque Herăstrău y el Museo del Pueblo. Tranquilo, verde y bien conectado. Hoteles desde 55€."}
    ],
    "what_to_do": [
        {"title": "Palacio del Parlamento", "description": "El megalómano proyecto de Ceaușescu: 12 pisos, 1.100 habitaciones, 3.500 toneladas de cristal. Visita guiada obligatoria (10€), imprescindible por su escala absurda."},
        {"title": "Barrio Lipscani de noche", "description": "El casco histórico se transforma en la noche más vibrante de Europa del Este. Bares, clubs y terrazas en edificios centenarios hasta el amanecer."},
        {"title": "Museo Nacional de Historia", "description": "Tesoros daciorromanos incluyendo la Columna de Trajano en réplica y la corona real. Excelente para entender Rumanía más allá de los estereotipos."},
        {"title": "Museo del Pueblo (Muzeu Național al Satului)", "description": "Museo al aire libre con 300 casas tradicionales trasladadas de todo el país, junto al lago Herăstrău. Imprescindible."},
        {"title": "Excursión a Sinaia o Brasov", "description": "El castillo de Peles en Sinaia (1,5h) o la ciudad medieval de Brasov (2,5h) son excursiones de día perfectas desde Bucarest."},
        {"title": "Mercado de Obor", "description": "El mercado más auténtico de la ciudad: frutas, quesos, embutidos rumanos y ropa vintage. El lado menos turístico de Bucarest."}
    ],
    "food_and_drink": "Prueba el sarmale (rollitos de col rellenos), mici (salchichas a la brasa), ciorba de burta (sopa de callos), mamaliga (polenta) y cozonac (brioche dulce). Los restaurantes del centro histórico son asequibles: cena completa con vino local 15-25€. Cerveza local (Ursus, Timișoreana) desde 1,5€.",
    "safety": "Bucarest es relativamente segura. El centro histórico tiene carteristas y timos de taxi — usa Uber o Bolt siempre. Evita los taxis de calle sin taxímetro. Por la noche, el barrio Lipscani es muy animado pero seguro en grupos.",
    "visa_info": "Rumanía es UE pero NO Schengen (aunque se unió parcialmente en 2024 para aeropuertos/puertos). Ciudadanos UE entran con DNI. Españoles sin visado adicional.",
    "local_tips": ["Bolt y Uber son la forma de moverse — los taxis de calle pueden cobrarte 10x más", "El metro es barato y eficiente, cubre bien el centro", "El vino rumano es excelente y muy barato — prueba Feteasca Neagra", "La mayoría de museos cierran los lunes", "Cambia dinero en casas de cambio, nunca en el aeropuerto"],
    "travel_styles": ["ciudad", "cultura", "nocturno", "budget"],
    "vibes": ["eastern europe", "emerging", "nightlife", "authentic"],
    "climate": ["continental"],
    "best_months": ["April", "May", "June", "September", "October"],
    "budget_daily_low": 30, "budget_daily_mid": 65, "budget_daily_high": 150, "guide_quality": 8
},
{
    "slug": "belgrado", "name": "Belgrado", "country": "Serbia", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 44.8176, "lng": 20.4569},
    "tagline": "La capital balcánica que nunca duerme y siempre sorprende",
    "intro": "Belgrado es una de las ciudades más infraesitmadas de Europa: buena comida, buen vino, noches que duran hasta mediodía y un carácter balcánico genuino que no se puede fabricar. La fortaleza de Kalemegdan en la confluencia del Sava y el Danubio es el corazón de la ciudad, rodeada de parques llenos de locales.\n\nEl barrio de Savamala, antigua zona industrial reconvertida en epicentro cultural con galerías, bares y splavovi (clubs flotantes en el río), es uno de los barrios más interesantes de los Balcanes. Los precios están entre los más bajos de Europa.\n\nSin visa Schengen, Belgrado recibe flujo constante de viajeros de larga distancia que la usan como base para explorar los Balcanes.",
    "when_to_go": "Mayo-junio y septiembre son perfectos (20-28°C). El verano es muy caluroso (35°C+) pero es cuando la vida nocturna en el río está en su apogeo. El invierno es gris y frío pero los precios caen aún más y los kafanas (tabernas) están llenas de ambiente.",
    "how_to_get_there": "Aeropuerto Nikola Tesla con conexiones europeas. Bus desde el aeropuerto al centro (89 dinares, ~0,75€). Buses internacionales económicos desde toda Europa (Flixbus).",
    "where_to_sleep": [
        {"name": "Savamala", "description": "El barrio más cool y artístico, junto al río. Hostels desde 10€, apartamentos desde 30€. El epicentro de la escena creativa."},
        {"name": "Stari Grad (Ciudad Vieja)", "description": "El centro histórico cerca de Kalemegdan. Hoteles boutique desde 50€, bien conectado con todo."},
        {"name": "Vračar", "description": "Barrio residencial tranquilo con el mercado Kalenic y buenos restaurantes locales. Apartamentos desde 35€/noche."}
    ],
    "what_to_do": [
        {"title": "Fortaleza de Kalemegdan", "description": "La fortaleza medieval en la confluencia de dos ríos con museo militar y vistas épicas al atardecer. Entrada al parque gratuita, museos desde 3€."},
        {"title": "Barrio Savamala y splavovi", "description": "Los clubs flotantes en el río Sava son únicos en Europa. La escena empieza tarde (2-3am) y acaba al mediodía siguiente."},
        {"title": "Calle Skadarlija", "description": "La calle bohemia del siglo XIX con restaurantes, músicos de folk y ambiente de taberna auténtico. El barrio artístico original de Belgrado."},
        {"title": "Museo de Historia de Yugoslavia", "description": "Incluye la tumba de Tito y una colección fascinante sobre la Yugoslavia socialista. Contexto imprescindible para entender los Balcanes."},
        {"title": "Templo de San Sava", "description": "Una de las iglesias ortodoxas más grandes del mundo, en construcción desde 1935. El interior dorado es impresionante."},
        {"title": "Mercado Kalenic", "description": "El mejor mercado de productores de Belgrado: queso kajmak, ajvar, rakija artesanal. El desayuno con burek cuesta menos de 2€."}
    ],
    "food_and_drink": "Prueba el cevapi (salchichas de ternera con pan y cebolla), pljeskavica (hamburguesa balcánica), ajvar (paté de pimiento asado) y kajmak (queso cremoso). La rakija (aguardiente) se ofrece en todas partes — aceptar es un acto social. Cena completa 10-18€, cerveza 1-2€.",
    "safety": "Belgrado es segura para turistas. Precaución normal en zonas de fiesta nocturna. El transporte público nocturno es escaso — usa Bolt o Uber. Los taxis del aeropuerto negocian precio, usa la aplicación.",
    "visa_info": "Serbia no es UE ni Schengen. Españoles y ciudadanos UE pueden entrar sin visado hasta 90 días con pasaporte. El sello serbio en el pasaporte puede complicar la entrada a Kosovo.",
    "local_tips": ["La rakija casera que te ofrecen los locales suele ser mejor que la de tienda", "El desayuno con burek y yogur en una pekara (panadería) es la mejor forma de empezar el día por 1,5€", "Bolt funciona mejor que los taxis de calle", "Los splavovi están en su apogeo en verano — en invierno la mayoría cierran", "Cambia dinero en las casas de cambio del centro, no en el aeropuerto"],
    "travel_styles": ["nocturno", "budget", "cultura", "gastronomía"],
    "vibes": ["balkans", "nightlife", "authentic", "social"],
    "climate": ["continental"],
    "best_months": ["May", "June", "September", "October"],
    "budget_daily_low": 25, "budget_daily_mid": 55, "budget_daily_high": 130, "guide_quality": 8
},
{
    "slug": "sofia", "name": "Sofía", "country": "Bulgaria", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 42.6977, "lng": 23.3219},
    "tagline": "La capital más asequible de la UE, con historia milenaria al pie del monte Vitosha",
    "intro": "Sofía tiene la peculiaridad de ser capital de un país UE y a la vez una de las ciudades más baratas de Europa. El centro histórico mezcla iglesias ortodoxas, mezquitas otomanas, ruinas romanas y arquitectura soviética en un espacio peatonal de apenas unos kilómetros. El metro es nuevo y eficiente, y el monte Vitosha (1.800m) asoma al fondo de la ciudad como telón de fondo permanente.\n\nEl barrio de Studentski Grad tiene la vida nocturna universitaria más barata del continente. El NDK (Palacio de Cultura) y sus alrededores concentran la escena cultural moderna. La ciudad tiene una energía de transición que la hace interesante.\n\nBulgaria es el país más pobre de la UE pero Sofía tiene más carácter y autenticidad que muchas capitales europeas 'completas'.",
    "when_to_go": "Primavera (abril-mayo) y otoño (sept-oct) son ideales: 18-25°C. El verano es caluroso (30-35°C) pero agradable. El invierno es frío con nieve posible (dic-feb) — se puede combinar con esquí en Borovets (70km).",
    "how_to_get_there": "Aeropuerto de Sofía con conexiones europeas directas (Ryanair, Wizz Air baratos). Metro línea 1 llega al aeropuerto (1,60 leva, ~0,80€). Buses Flixbus económicos desde ciudades europeas.",
    "where_to_sleep": [
        {"name": "Centro (Serdika)", "description": "Junto a las ruinas romanas y la Catedral Alejandro Nevsky. Hostels desde 8€, hoteles boutique desde 30€."},
        {"name": "Studentski Grad", "description": "El barrio universitario con la vida nocturna más barata de Europa. Apartamentos desde 20€/noche."},
        {"name": "Zona NDK", "description": "El barrio más moderno y tranquilo, cerca del Parque Borisova. Buenos apartamentos de diseño desde 35€."}
    ],
    "what_to_do": [
        {"title": "Catedral Alejandro Nevsky", "description": "La catedral ortodoxa más grande de Bulgaria y una de las más impresionantes de los Balcanes. Gratuita, interior dorado impresionante."},
        {"title": "Ruinas romanas de Serdica", "description": "El centro comercial Serdika fue construido sobre y alrededor de las ruinas romanas del siglo IV — se pueden ver desde dentro del metro y las calles peatonales."},
        {"title": "Iglesia de Boyana", "description": "UNESCO: frescos medievales del siglo XIII extraordinariamente bien conservados, precursores del Renacimiento. A 8km del centro (8€)."},
        {"title": "Senderismo en Vitosha", "description": "El monte que domina Sofía tiene rutas accesibles en transporte público. En verano: senderismo; en invierno: pequeña estación de esquí."},
        {"title": "Mercado central (Centralas Hali)", "description": "Mercado cubierto art nouveau con dos plantas de productos locales: queso búlgaro, banitsa (hojaldre de queso), miel y rakija."},
        {"title": "Tour gratuito de la ciudad", "description": "Sofia Free Tour sale dos veces al día de la Catedral Alejandro Nevsky — el mejor modo de entender la historia de la ciudad en 2,5 horas."}
    ],
    "food_and_drink": "Prueba la banitsa (hojaldre relleno de queso o espinacas), shopska salata (tomate, pepino, queso), kavarma (estofado en cazuela de barro) y el yogur búlgaro que es genuinamente el mejor del mundo. Cena completa con vino 8-15€. Cerveza local (Kamenitza, Zagorka) desde 1€.",
    "safety": "Sofía es segura para turistas. Los taxis tienen fama de timar — usa Bolt siempre. En el centro algunos vendedores pueden ser insistentes. Zona de Vitosha tiene pickpockets ocasionales.",
    "visa_info": "Bulgaria es UE pero NO Schengen (en proceso de adhesión). Ciudadanos UE entran con DNI. Españoles sin visado. Moneda propia: lev búlgaro (BGN), aproximadamente 2 BGN = 1€.",
    "local_tips": ["Un desayuno búlgaro completo (banitsa + café + zumo) cuesta menos de 3€ en cualquier pekarna", "El metro es moderno, barato y limpio — cubre los puntos principales", "El vino búlgaro es excelente y muy barato: Mavrud y Rubin son variedades autóctonas extraordinarias", "Las termas públicas del centro (Las Halite) tienen fuente de agua termal gratuita", "Combina Sofía con un día en Plovdiv (2h en bus) — ciudad con el mejor casco histórico del país"],
    "travel_styles": ["budget", "cultura", "historia", "naturaleza"],
    "vibes": ["eastern europe", "authentic", "emerging", "orthodox"],
    "climate": ["continental"],
    "best_months": ["April", "May", "September", "October"],
    "budget_daily_low": 22, "budget_daily_mid": 45, "budget_daily_high": 100, "guide_quality": 8
},
{
    "slug": "riga", "name": "Riga", "country": "Letonia", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 56.9496, "lng": 24.1052},
    "tagline": "La capital del art nouveau báltico, con la ciudad vieja más auténtica del norte de Europa",
    "intro": "Riga tiene el barrio art nouveau más extenso del mundo — más de 800 edificios de principios del siglo XX con fachadas elaboradas que son Patrimonio UNESCO. La Ciudad Vieja medieval a orillas del Daugava completa un panorama urbano único. A diferencia de Tallinn y Vilnius, Riga tiene una escala más grande y una escena local más desarrollada.\n\nEl mercado central de Riga, instalado en cinco hangares de zepelines de los años 20, es el mayor mercado cubierto de Europa y un imprescindible para entender la gastronomía letona. El barrio de Āgenskalns al otro lado del río es donde viven los locales.\n\nLatvía es la menos visitada del triángulo báltico y eso es precisamente su mejor argumento.",
    "when_to_go": "Junio-agosto: días con 18 horas de luz, temperaturas de 20-25°C y el Festival del Solsticio (Jāņi) que es una celebración pagana espectacular. El invierno (dic-feb) es oscuro y frío (-5°C) pero hay mercados navideños genuinamente bonitos y los precios caen.",
    "how_to_get_there": "Aeropuerto de Riga bien conectado con Europa (Ryanair, airBaltic). Bus n°22 al centro en 30 min (1,15€). Ferries desde Helsinki y Estocolmo.",
    "where_to_sleep": [
        {"name": "Ciudad Vieja (Vecrīga)", "description": "El centro histórico medieval, perfecto para moverse a pie. Hostels desde 14€, hoteles boutique desde 55€."},
        {"name": "Barrio Art Nouveau (Centrs)", "description": "Las mejores fachadas están aquí. Apartamentos desde 45€/noche en edificios históricos."},
        {"name": "Āgenskalns", "description": "El barrio local al otro lado del río, con el mercado del mismo nombre y cafés bohemios. Más barato y auténtico."}
    ],
    "what_to_do": [
        {"title": "Barrio Art Nouveau", "description": "Paseo autoguiado por Alberta iela y Elizabetes iela para ver las mejores fachadas. El Museo Art Nouveau (Albertas 12) muestra un apartamento original de época (8€)."},
        {"title": "Mercado Central de Riga", "description": "Los cinco pabellones de zepelines albergan el mayor mercado cubierto de Europa. Prueba el kefir, el pan negro, el pescado ahumado y los productos forestales."},
        {"title": "Ciudad Vieja y Torre de San Pedro", "description": "El casco histórico medieval con la Casa de las Cabezas Negras (siglo XIV) y la Torre de San Pedro (vistas panorámicas, 9€)."},
        {"title": "Cementerio de la Libertad", "description": "El lugar más emotivo de Riga: memorial a los soldados letones con guardias de honor. Escultura de la Madre Latvia presidiendo la escena."},
        {"title": "Playa de Jūrmala", "description": "A 25 min en tren, la playa de arena blanca y los chalets de madera de principios del siglo XX forman un conjunto único. Muy frecuentado por locales en verano."},
        {"title": "Museo de la Ocupación", "description": "Documentación exhaustiva sobre las ocupaciones soviética y nazi. Gratuito, emocionalmente intenso e imprescindible para entender los países bálticos."}
    ],
    "food_and_drink": "La cocina letona es contundente y de temporada: pan negro de centeno (rupjmaize), sopa de remolacha (borsch local), pescado ahumado, pastel de cebolla y carnes guisadas. Los mercados son el mejor lugar para comer barato. Restaurante local: 12-20€ por persona. Cerveza local (Aldaris, Valmiermuiža) desde 2€.",
    "safety": "Riga es segura pero la Ciudad Vieja concentra turismo de borrachera del norte de Europa — baches ocasionales de noche. Los taxis tienen tarifa fija desde el aeropuerto, confirma el precio antes. Usa Bolt.",
    "visa_info": "Letonia es UE y Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: euro.",
    "local_tips": ["El pan negro letón es un producto nacional — compra una barra en el mercado", "La tarjeta de 24h del transporte público (5€) vale la pena si visitas Jūrmala", "El Festival del Solsticio (Jāņi, 23-24 junio) transforma todo el país en una fiesta pagana — uno de los eventos más auténticos de Europa", "Los baños de sauna son una institución social letona — pregunta en tu alojamiento", "Jūrmala se puede combinar con una tarde de spa en el centro termal"],
    "travel_styles": ["cultura", "historia", "arquitectura", "naturaleza"],
    "vibes": ["baltic", "art nouveau", "authentic", "northern"],
    "climate": ["humid continental", "cold winters"],
    "best_months": ["June", "July", "August"],
    "budget_daily_low": 40, "budget_daily_mid": 80, "budget_daily_high": 175, "guide_quality": 8
},
{
    "slug": "tallinn", "name": "Tallin", "country": "Estonia", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 59.437, "lng": 24.7536},
    "tagline": "La ciudad medieval mejor conservada de Europa del Norte, digital y antigua a la vez",
    "intro": "Tallin tiene el casco histórico medieval más completo del norte de Europa — torres, murallas, calles adoquinadas y la Plaza del Ayuntamiento que parece sacada de un cuento, todo Patrimonio UNESCO. Lo sorprendente es que este fondo medieval convive con el país más digital del mundo: Estonia inventó el e-Residency y tiene más startups per cápita que casi nadie.\n\nEl barrio de Kalamaja, antigua zona de pescadores reconvertida en el barrio más hipster de los Bálticos, tiene las mejores cafeterías y restaurantes de la ciudad. El mercado de Balti Jaam y el Telliskivi Creative City son el corazón del Tallin joven.\n\nA solo 80km de Helsinki por ferry, Tallin funciona bien como add-on de un viaje nórdico, aunque merece más atención propia.",
    "when_to_go": "Junio-agosto: la Ciudad Vieja en verano con días larguísimos (hasta las 23h hay luz) es mágica. El solsticio de verano (Jaanipäev) es la fiesta nacional por excelencia. El invierno es oscuro y frío pero los mercados navideños de la Plaza del Ayuntamiento son de los más auténticos de Europa.",
    "how_to_get_there": "Aeropuerto de Tallin con conexiones europeas. Bus n°2 al centro (2€). Ferry desde Helsinki (2-2,5h, desde 25€) muy recomendable.",
    "where_to_sleep": [
        {"name": "Ciudad Vieja (Vanalinn)", "description": "Dentro de las murallas medievales, cero coches y máxima atmósfera. Hoteles boutique desde 70€, hostels desde 18€."},
        {"name": "Kalamaja", "description": "El barrio más auténtico y creativo, a 15 min a pie de la Ciudad Vieja. Apartamentos desde 50€/noche."},
        {"name": "Telliskivi", "description": "Zona industrial reconvertida con mercados y galerías. Excelente base para moverse, con buen transporte."}
    ],
    "what_to_do": [
        {"title": "Ciudad Vieja y murallas medievales", "description": "Pasea por Toompea (la colina alta) y la Ciudad Baja. Las murallas se pueden caminar parcialmente. El Museo de las Torres (5€) explica la historia."},
        {"title": "Barrio Kalamaja y Telliskivi", "description": "El barrio creativo más animado de los Bálticos. Cafés de especialidad, galerías, el mercado del sábado y el flea market de Balti Jaam."},
        {"title": "Museo Kumu", "description": "El mejor museo de arte de los países bálticos, con arte estonio desde el siglo XVIII hasta hoy. Edificio espectacular (15€)."},
        {"title": "Ferry a Helsinki para el día", "description": "Helsinki está a 2h en ferry — es una excursión de día perfecta para comparar las dos culturas vecinas."},
        {"title": "Playa de Pirita y bosques costeros", "description": "A 10 min en bus, la playa de arena fina con el bosque de Pirita detrás ofrece el mejor escape natural de la ciudad."},
        {"title": "Mercado de Keskturg", "description": "El mercado central de Tallin, menos turístico que el de la Ciudad Vieja, con los mejores precios en queso, pan y productos locales."}
    ],
    "food_and_drink": "La cocina estonia es de producto: pan negro de centeno (leib), carne de alce, pescado báltico ahumado, kefir, queso holandés local y bayas silvestres en temporada. Kalamaja tiene los mejores restaurantes creativos (25-40€/persona). El mercado de Balti Jaam tiene el mejor street food (5-8€).",
    "safety": "Tallin es muy segura. La Ciudad Vieja en temporada alta atrae turismo de borrachera del norte (especialmente finlandeses en ferry) — los fines de semana puede ser ruidosa. Carteristas esporádicos en zonas turísticas.",
    "visa_info": "Estonia es UE y Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: euro.",
    "local_tips": ["El ferry Helsinki-Tallin es una experiencia en sí mismo y hace la ruta más interesante", "El mercado de Telliskivi los sábados tiene los mejores productores locales", "La tarjeta de transporte de 24h cuesta 3€ y cubre todos los buses y tranvías", "Toompea al atardecer (la colina alta) tiene las mejores vistas de la ciudad medieval", "El café de especialidad de Tallin es sorprendentemente bueno — la tercera ola del café llegó fuerte"],
    "travel_styles": ["cultura", "historia", "arquitectura", "digital"],
    "vibes": ["medieval", "baltic", "tech", "authentic"],
    "climate": ["humid continental", "cold winters"],
    "best_months": ["June", "July", "August"],
    "budget_daily_low": 45, "budget_daily_mid": 90, "budget_daily_high": 200, "guide_quality": 8
},
{
    "slug": "vilnius", "name": "Vilna", "country": "Lituania", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 54.6872, "lng": 25.2797},
    "tagline": "El Berlín de los Bálticos: bohemia, barata y con el barrio viejo más grande de Europa del Norte",
    "intro": "Vilna tiene el casco histórico barroco más grande de Europa del Norte — 1.500 edificios en un área de 3,6km², todo Patrimonio UNESCO. Pero lo que la hace especial es Užupis, el barrio artístico que declaró su independencia en 1997 (con su propia constitución, presidente y ejército de 12 personas). Es exactamente tan raro y maravilloso como suena.\n\nEn los últimos años, Vilna ha desarrollado una escena gastronómica y de café que sorprende. El barrio de Šnipiškės (Naujamiestis) tiene la concentración más alta de buenos restaurantes por metro cuadrado. Los precios siguen siendo claramente más bajos que Europa Occidental.\n\nCombinada con Riga y Tallin en un road trip báltico, Vilna cierra un triángulo que es uno de los mejores itinerarios de Europa.",
    "when_to_go": "Mayo-septiembre: temperaturas agradables (18-26°C) y la ciudad en su mejor momento. El solsticio de San Juan (Joninės) es una fiesta popular espectacular. Diciembre tiene un mercado navideño genuinamente bonito en la Plaza de la Catedral.",
    "how_to_get_there": "Aeropuerto de Vilna con conexiones europeas. Bus n°1 y n°2 al centro (1€). Flixbus económico desde Varsovia, Riga y Tallin.",
    "where_to_sleep": [
        {"name": "Ciudad Vieja", "description": "El corazón histórico barroco, todo a pie. Hostels desde 14€, hoteles boutique desde 60€."},
        {"name": "Užupis", "description": "El barrio artístico independiente, bohemio y tranquilo. Apartamentos desde 45€/noche."},
        {"name": "Naujamiestis", "description": "El barrio nuevo con la mejor gastronomía y vida nocturna local. Excelente relación calidad-precio."}
    ],
    "what_to_do": [
        {"title": "Ciudad Vieja barroca", "description": "La mayor concentración de arquitectura barroca del norte de Europa. La calle Pilies conecta el Castillo con la Plaza de la Catedral en 15 minutos de paseo."},
        {"title": "República de Užupis", "description": "Cruza el puente sobre el río Vilnelė para entrar en la 'república' artista. Lee su constitución en español en la calle Paupio. Pasea por sus calles bohemias."},
        {"title": "Torre Gediminas y colinas", "description": "La torre medieval sobre la colina con vistas panorámicas de la ciudad vieja y el río. Sube por el funicular (3€)."},
        {"title": "Antigua sinagoga y Gaon Street", "description": "Vilna fue llamada la 'Jerusalén del Norte'. El museo Paneriai documenta el holocausto lituano — emotivo e imprescindible."},
        {"title": "Mercado de las Pulgas de Užupis", "description": "Los domingos, el mercado de antigüedades y objetos soviéticos junto al río es uno de los más auténticos de los Bálticos."},
        {"title": "Trakai con castillo lacustre", "description": "A 28km, el castillo medieval en una isla rodeada de lagos es una excursión de día perfecta (bus desde la estación, 2€ ida)."}
    ],
    "food_and_drink": "La cocina lituana es hearty: cepelinai (bolas de patata rellenas de carne, el plato nacional), kugelis (budín de patata), sopa de remolacha, arenque marinado y queso local. Naujamiestis tiene restaurantes modernos excelentes. Cena completa 15-25€, cerveza local (Švyturys, Utenos) desde 2€.",
    "safety": "Vilna es muy segura para turistas. Prácticamente sin incidentes reportados. El transporte público es fiable y barato.",
    "visa_info": "Lituania es UE y Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: euro.",
    "local_tips": ["La constitución de Užupis en español está en la calle Paupio — léela, es genuinamente filosófica y divertida", "Los cepelinai son el plato más contundente del mundo — uno es suficiente", "Trakai vale el desvío aunque sea por medio día", "Los cafés de especialidad en Naujamiestis son de los mejores del norte de Europa", "El parque Vingis al atardecer es donde los locales hacen deporte y socializan"],
    "travel_styles": ["cultura", "historia", "budget", "gastronomía"],
    "vibes": ["baroque", "bohemian", "baltic", "emerging"],
    "climate": ["humid continental"],
    "best_months": ["May", "June", "July", "August", "September"],
    "budget_daily_low": 38, "budget_daily_mid": 75, "budget_daily_high": 160, "guide_quality": 8
},
{
    "slug": "oslo", "name": "Oslo", "country": "Noruega", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 59.9139, "lng": 10.7522},
    "tagline": "Los fiordos a la puerta de la ciudad más cara de Europa que aun así vale cada corona",
    "intro": "Oslo es cara. Muy cara. Una cerveza cuesta 10-12€ y una cena sencilla fácilmente 30€. Dicho esto, es también una de las ciudades más espectaculares de Europa: fiordos navegables desde el centro, bosques a 15 minutos en metro, museos de clase mundial y una calidad de vida que se nota en el aire.\n\nEl barrio de Grünerløkka es el epicentro creativo — cafés de especialidad, mercados de segunda mano y galerías en un área que hace 20 años era obrera. El puerto de Aker Brygge y el nuevo barrio de Bjørvika (con la Ópera) definen el Oslo contemporáneo.\n\nVisítala sabiendo que el presupuesto subirá, pero los supermercados (Kiwi, Rema 1000) y el outdoor gratuito compensan parcialmente.",
    "when_to_go": "Junio-agosto: días casi continuos de luz (sol de medianoche), temperaturas de 20-25°C, fiordos navegables y la ciudad en su momento más vibrante. El invierno (dic-feb) tiene sus encantos: auroras boreales posibles, esquí a 15 min en metro y la Navidad noruega.",
    "how_to_get_there": "Aeropuerto de Gardermoen con conexiones globales. Flytoget (tren expreso) al centro en 19 min (200 NOK, ~18€). Alternativa: bus Flybussen (150 NOK).",
    "where_to_sleep": [
        {"name": "Grünerløkka", "description": "El barrio más animado y auténtico de Oslo. Hostels desde 25€, apartamentos desde 90€/noche."},
        {"name": "Frogner", "description": "Barrio elegante cerca del Parque Vigeland. Hoteles boutique desde 120€, tranquilo y bien situado."},
        {"name": "Centro (Sentrum)", "description": "Junto al Puerto y la Ópera. Práctico para visitas pero más turístico. Hoteles desde 100€."}
    ],
    "what_to_do": [
        {"title": "Crucero por el fiordo de Oslo", "description": "Los ferries públicos (línea B1/B2, 5€ con tarjeta transporte) navegan entre las islas del fiordo — nadar, caminar y vistas de la ciudad desde el agua."},
        {"title": "Parque de Esculturas Vigeland", "description": "El mayor parque de esculturas del mundo realizado por un solo artista. 200 esculturas de bronce y granito, gratuito."},
        {"title": "Barrio Grünerløkka", "description": "El corazón creativo de Oslo: mercado de Birkelunden los domingos, cafés de especialidad, vintage shops y la mejor selección de restaurantes de la ciudad."},
        {"title": "Museo de la Ópera y Bjørvika", "description": "El techo inclinado de la Ópera es una plaza pública donde la gente camina — arquitectura noruega contemporánea espectacular. Gratuito subir."},
        {"title": "Museo Fram y Museo Kon-Tiki", "description": "Los barcos de las expediciones polares de Nansen y Amundsen y la balsa de Heyerdahl, conservados en perfecto estado. Cultura marítima noruega a fondo (14€ cada uno)."},
        {"title": "Esquí en Holmenkollen", "description": "A 15 minutos en metro T-bane, la pista más famosa de Noruega tiene museo del esquí y vistas panorámicas de Oslo y el fiordo."}
    ],
    "food_and_drink": "El salmón noruego, los camarones de fiordo y el skrei (bacalao en temporada) son incomparables. Mercado de Mathallen Oslo para tapeo de calidad (5-12€ por plato). Los supermercados Kiwi tienen buena comida preparada por 5-8€ — estrategia de supervivencia recomendada. Cerveza en bar: 10-12€.",
    "safety": "Oslo es una de las ciudades más seguras del mundo. Sin precauciones especiales salvo el bolsillo.",
    "visa_info": "Noruega NO es UE pero SÍ es Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: corona noruega (NOK).",
    "local_tips": ["Compra en supermercados Kiwi/Rema para controlar el presupuesto — el food hall de Mathallen es caro pero merece una visita", "El Oslo Pass (24h: 495 NOK) incluye transporte y entrada a museos — sale rentable", "El metro T-bane llega al bosque de Nordmarka en 30 min — senderismo gratuito", "Las farmacias son más baratas que en muchos países europeos", "El salmón en el mercado de Fisketorvet es mejor y más barato que en restaurante"],
    "travel_styles": ["naturaleza", "cultura", "outdoor", "diseño"],
    "vibes": ["nordic", "fjord", "design", "outdoor"],
    "climate": ["oceanic", "cold winters"],
    "best_months": ["June", "July", "August"],
    "budget_daily_low": 85, "budget_daily_mid": 170, "budget_daily_high": 380, "guide_quality": 8
},
{
    "slug": "helsinki", "name": "Helsinki", "country": "Finlandia", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 60.1699, "lng": 24.9384},
    "tagline": "Diseño nórdico, saunas en el mar y la ciudad que mejor equilibra naturaleza y urbanismo",
    "intro": "Helsinki es compacta, eficiente y sorprendentemente acogedora para una ciudad del norte. El diseño nórdico está en todas partes — desde el mercado de Hakaniemi hasta el Museo de Diseño, pasando por las tiendas de Marimekko y Iittala. Pero lo que realmente diferencia Helsinki es la relación con el mar: la ciudad está en una península rodeada de archipiélagos, y en verano todos los finlandeses acaban en el agua.\n\nLas saunas públicas son una institución cultural: Löyly y Allas Sea Pool son las más conocidas, pero la sauna pública del estadio olímpico es la más auténtica y barata. El mercado de Kauppatori junto al puerto es el mejor desayuno posible.\n\nCombina perfectamente con Tallin (ferry de 2h) para un viaje báltico eficiente.",
    "when_to_go": "Junio-agosto es la mejor época: días larguísimos con sol hasta las 23h, temperatura 18-24°C y la ciudad abierta y animada. El invierno (nov-feb) tiene 6h de luz al día pero también auroras boreales posibles, Navidad con nieve y la experiencia sauna más auténtica.",
    "how_to_get_there": "Aeropuerto de Helsinki-Vantaa con conexiones globales. Tren I/P al centro en 30 min (4€). Ferry desde Tallin (2-2,5h, desde 25€) y Estocolmo (overnight, desde 35€).",
    "where_to_sleep": [
        {"name": "Punavuori / Design District", "description": "El barrio de diseño más animado, con galerías y cafés. Hoteles boutique desde 90€, hostels desde 30€."},
        {"name": "Kallio", "description": "El barrio obrero reconvertido, más barato y auténtico. Bares locales, mercado de Hakaniemi. Apartamentos desde 65€."},
        {"name": "Katajanokka", "description": "Barrio histórico junto al puerto con arquitectura Jugend. Tranquilo y con buena conexión al ferry de Tallin."}
    ],
    "what_to_do": [
        {"title": "Sauna Löyly o Allas Sea Pool", "description": "Las saunas frente al mar báltico con salto al agua incluido. Löyly (20€) es arquitectónicamente espectacular; Allas (18€) tiene piscinas de agua caliente y fría."},
        {"title": "Mercado Kauppatori y Mercado Cubierto", "description": "El mercado junto al puerto tiene los mejores camarones de fiordo, salmón ahumado y café de desayuno. El mercado cubierto (Vanha Kauppahalli) tiene más calidad."},
        {"title": "Catedral y Senado", "description": "La plaza del Senado con la catedral luterana blanca neoclásica y la catedral ortodoxa de Uspenski forman el corazón histórico de la ciudad."},
        {"title": "Suomenlinna", "description": "Fortaleza marítima UNESCO en una isla a 15 min en ferry desde el mercado (ferries del transporte público, 3€). Museos, murallas y playas."},
        {"title": "Museo de Diseño y Districto del Diseño", "description": "El Districto del Diseño concentra más de 200 tiendas de diseño, galerías y showrooms en un área compacta. El Museo de Diseño explica la historia del diseño finlandés (12€)."},
        {"title": "Temppeliaukio y Kamppi", "description": "La iglesia tallada en roca (Temppeliaukio, 5€) y la capilla de silencio de Kamppi (gratuita) son dos de los espacios arquitectónicos más singulares de la ciudad."}
    ],
    "food_and_drink": "Prueba el karelian pasty (empanadilla de arroz con mantequilla de huevo), el salmón gravlax, los camarones de fiordo y el pulla (bollo de cardamomo). Los mercados son la opción más auténtica. Cena en restaurante local: 25-40€. Cerveza en bar: 7-9€. Los supermercados K-Market tienen buena comida preparada.",
    "safety": "Helsinki es de las ciudades más seguras del mundo. Sin precauciones especiales.",
    "visa_info": "Finlandia es UE y Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: euro.",
    "local_tips": ["La sauna no es opcional — es parte de entender la cultura finlandesa", "El ferry nocturno a Estocolmo (Silja/Viking Line) es una experiencia en sí mismo", "Kallio es el barrio donde comen los locales — mucho más barato que el centro turístico", "El transporte público funciona perfectamente: app HSL para validar billetes", "En verano, alquila una bicicleta — Helsinki es completamente llana y cicloamigable"],
    "travel_styles": ["diseño", "cultura", "naturaleza", "sauna"],
    "vibes": ["nordic", "design", "sea", "sauna"],
    "climate": ["humid continental", "cold winters"],
    "best_months": ["June", "July", "August"],
    "budget_daily_low": 70, "budget_daily_mid": 140, "budget_daily_high": 300, "guide_quality": 8
},
{
    "slug": "zurich", "name": "Zúrich", "country": "Suiza", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 47.3769, "lng": 8.5417},
    "tagline": "Calidad de vida suiza, lago alpino y la mejor escena cultural de la Confederación",
    "intro": "Zúrich es cara, eficiente y genuinamente hermosa. El lago de Zúrich y el río Limmat en verano se convierten en playas urbanas gratuitas donde los locales se bañan con la misma naturalidad que en cualquier resort mediterráneo. El casco histórico de Altstadt y las colinas de Zürichberg ofrecen calles medievales sin el agobio turístico de otras ciudades europeas similares.\n\nEl barrio de Langstrasse fue la zona roja de la ciudad y hoy es el epicentro de la escena alternativa y gastronómica: restaurantes de todo el mundo, bares indie y el mejor ambiente nocturno de Suiza. El Musée des Beaux-Arts y el Kunsthaus son de clase mundial.\n\nPara compensar los precios suizos: los supermercados Migros y Coop tienen comida de altísima calidad a precios razonables, las playas del lago son gratuitas y los museos municipales tienen entrada libre los miércoles.",
    "when_to_go": "Mayo-septiembre es perfecto: lagos para bañarse, senderismo alpino accesible y la ciudad en su mejor momento. Junio y julio son los mejores meses. El invierno tiene su encanto (Navidad muy suiza) pero los costes se mantienen igual de altos.",
    "how_to_get_there": "Aeropuerto de Zúrich directamente conectado al centro con tren (10 min, 5 CHF). Una de las mejores conexiones aeropuerto-ciudad del mundo.",
    "where_to_sleep": [
        {"name": "Altstadt (Ciudad Vieja)", "description": "El centro histórico en ambas orillas del Limmat. Hoteles boutique desde 130 CHF. Caro pero céntrico."},
        {"name": "Langstrasse", "description": "El barrio alternativo más animado, con los mejores restaurantes. Apartamentos desde 100 CHF/noche."},
        {"name": "Zürich Oerlikon", "description": "Zona más moderna al norte, con mejores precios y buen transporte. Hoteles desde 90 CHF."}
    ],
    "what_to_do": [
        {"title": "Bañarse en el lago de Zúrich", "description": "Los badis (piscinas-plataformas en el lago) son gratuitas o con pequeña tasa (5 CHF). Aguas cristalinas y vistas a los Alpes en días despejados. Imprescindible en verano."},
        {"title": "Kunsthaus Zürich", "description": "El mayor museo de arte de Suiza, con obras de Monet, Picasso, Munch y el mejor Giacometti del mundo (26 CHF, gratis miércoles tarde)."},
        {"title": "Altstadt y Grossmünster", "description": "Las dos torres de la catedral Grossmünster dominan el casco histórico. Sube a la torre (5 CHF) para las mejores vistas. Calles medievales de Niederdorf."},
        {"title": "Excursión a Rigi o Uetliberg", "description": "Uetliberg (870m) se sube en tren desde el centro (30 min, billete normal de transporte) con vistas panorámicas del lago y los Alpes. Rigi requiere un día completo."},
        {"title": "Barrio Langstrasse", "description": "El barrio multicultural con más vida nocturna y gastronómica de Zúrich. Restaurantes étnicos excelentes (15-25 CHF) y bares hasta las 4am."},
        {"title": "Musée Rietberg", "description": "Arte asiático, africano y americano precolombino de nivel excepcional, en una villa junto al lago. Gratuito miércoles noche (11€ normalmente)."}
    ],
    "food_and_drink": "Prueba el Zürich Geschnetzeltes (ternera en salsa de nata con rösti), la fondue de queso, los Luxemburgerli (macarons suizos de Sprüngli) y el chocolate suizo (Läderach, Lindt). Los mercados (Helvetiaplatz los miércoles y sábados) tienen buen street food. Cena restaurante: 30-50 CHF. Cerveza local (Hürlimann, Feldschlösschen): 6-8 CHF.",
    "safety": "Zúrich es una de las ciudades más seguras del mundo. Sin precauciones especiales.",
    "visa_info": "Suiza no es UE pero sí Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: franco suizo (CHF). 1€ ≈ 0,95 CHF.",
    "local_tips": ["Los supermercados Migros y Coop tienen la mejor relación calidad-precio de Suiza — come ahí para controlar presupuesto", "La ZürichCard (1 día: 27 CHF) incluye todo el transporte y entradas a museos", "Bañarse en el río Limmat (corriente que baja del lago) es una tradición local veraniega gratuita", "La ruta de senderismo alrededor del lago tiene 35km y es completamente llana", "Los hostels de la cadena Youth Hostel Suiza son los mejores de precio-calidad"],
    "travel_styles": ["cultura", "naturaleza", "diseño", "gastronomía"],
    "vibes": ["swiss", "alpine", "lakeside", "clean"],
    "climate": ["temperate oceanic"],
    "best_months": ["May", "June", "July", "August", "September"],
    "budget_daily_low": 90, "budget_daily_mid": 180, "budget_daily_high": 400, "guide_quality": 8
},
{
    "slug": "lyon", "name": "Lyon", "country": "Francia", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 45.7640, "lng": 4.8357},
    "tagline": "La capital gastronómica de Francia donde los bouchons llevan 200 años de gloria",
    "intro": "Lyon tiene tres ríos, dos colinas y la mejor cocina de Francia — lo que en un país donde la cocina es religión es decir mucho. Los bouchons lyonnais son los restaurantes de cocina tradicional regional donde los canuts (tejedores de seda) comían en el siglo XIX y donde hoy los locales siguen tomando quenelles de brochet, tablier de sapeur (callos rebozados) y rosette de Lyon.\n\nVieux-Lyon, el barrio renacentista en la orilla del Saône, es Patrimonio UNESCO y tiene los mejores traboules — pasajes secretos que conectan patios interiores desde el siglo IV. Desde Fourvière, la colina de la Basílica, las vistas de la ciudad y los Alpes en días despejados son extraordinarias.\n\nLyon es la tercera ciudad de Francia pero tiene una escala perfecta para viajeros: suficientemente grande para tener de todo, suficientemente compacta para recorrerse a pie.",
    "when_to_go": "Primavera (abril-junio) y otoño (sept-oct) son los mejores momentos: clima agradable, sin multitudes. El Festival de la Luz (Fête des Lumières) en diciembre es uno de los eventos más espectaculares de Europa. El verano es caluroso (30°C+) pero festivo.",
    "how_to_get_there": "TGV desde París en 2h (desde 25€). Aeropuerto Saint-Exupéry con conexiones europeas; tren Rhônexpress al centro en 30 min (16€). Desde Barcelona: TGV 4,5h.",
    "where_to_sleep": [
        {"name": "Presqu'île", "description": "El centro histórico entre los dos ríos, con las mejores tiendas y restaurantes. Hoteles boutique desde 80€."},
        {"name": "Vieux-Lyon", "description": "El barrio renacentista UNESCO en la orilla del Saône. Encantador pero muy turístico. Hoteles desde 90€."},
        {"name": "Guillotière / 7ème", "description": "El barrio multicultural con la mejor relación calidad-precio. Apartamentos desde 60€, ambiente local."}
    ],
    "what_to_do": [
        {"title": "Bouchon lyonnais", "description": "Un bouchon auténtico (Bouchon Sully, Café du Jura, Daniel et Denise) es una experiencia gastronómica imprescindible. Menú complet con entrante, plato y postre: 20-30€."},
        {"title": "Vieux-Lyon y traboules", "description": "Los pasajes secretos de los barrios de Saint-Jean y Saint-Paul conectan patios interiores desde el siglo IV. Mapa gratuito en la oficina de turismo."},
        {"title": "Basílica de Fourvière y colina", "description": "La basílica dorada domina la ciudad. Sube en funicular (tramway: billete de transporte normal) para las mejores vistas. Los teatros romanos al lado son de los mejor conservados de Francia."},
        {"title": "Musée des Confluences", "description": "Uno de los edificios contemporáneos más espectaculares de Francia (arquitectura de Coop Himmelblau). Colecciones de ciencias naturales y antropología (9€)."},
        {"title": "Mercado Paul Bocuse", "description": "El mercado cubierto más elegante de Lyon, con los mejores productores de la región. Más para mirar que para comprar económico, pero impresionante."},
        {"title": "Festival de la Luz (diciembre)", "description": "Del 5 al 8 de diciembre, fachadas de toda la ciudad se iluminan con proyecciones. Uno de los eventos más concurridos de Europa (gratuito)."}
    ],
    "food_and_drink": "Lyon es la cuna de Paul Bocuse y la capital de la nouvelle cuisine. Los bouchons sirven quenelles (albóndigas de pescado en salsa), tablier de sapeur, andouillette y la salade lyonnaise con huevo escalfado. Los quesos de la región (Saint-Marcellin, Beaufort) son excepcionales. Precio bouchon: 20-35€/persona con vino.",
    "safety": "Lyon es una ciudad segura. Precaución normal en la estación de Perrache y en el metro por la noche. El barrio Guillotière tiene zonas que requieren atención extra de noche.",
    "visa_info": "Francia es UE y Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: euro.",
    "local_tips": ["Reserva el bouchon con antelación — los mejores se llenan a mediodía", "El funicular al Vieux-Lyon y Fourvière usa el mismo billete del metro", "El mercado de Croix-Rousse (martes-domingo mañanas) es el más auténtico para comprar", "Lyon es perfecta como escala entre Paris y la Costa Azul o los Alpes", "El barrio de Croix-Rousse, la 'colina que trabaja', tiene mejor ambiente local que Vieux-Lyon"],
    "travel_styles": ["gastronomía", "cultura", "historia", "arquitectura"],
    "vibes": ["culinary", "french", "renaissance", "local"],
    "climate": ["temperate oceanic", "hot summers"],
    "best_months": ["April", "May", "June", "September", "October"],
    "budget_daily_low": 55, "budget_daily_mid": 110, "budget_daily_high": 240, "guide_quality": 8
},
{
    "slug": "niza", "name": "Niza", "country": "Francia", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 43.7102, "lng": 7.2620},
    "tagline": "El Mediterráneo en estado puro: Promenade, mercados provenzales y cocina niçoise",
    "intro": "Niza tiene todo lo que se busca en la Costa Azul con una escala de ciudad real: el Vieux-Nice con sus fachadas barrocas de colores, el mercado del Cours Saleya con flores y productos provenzales, la Promenade des Anglais para el paseo matutino y las mejores playas de guijarros del Mediterráneo occidental.\n\nLo que menos gente sabe es que Niza tiene una identidad cultural propia — fue italiana (reino de Saboya) hasta 1860 y tiene su propio idioma (niçard) y cocina específica: socca (crepe de garbanzo), pissaladière (focaccia con cebollas y anchoas), pan bagnat y la salade niçoise auténtica (sin lechuga, con huevo duro y anchoas).\n\nEs más cara que otras ciudades mediterráneas pero sigue siendo asequible comparada con Mónaco (a 20 min en tren, gratuito con el pase regional).",
    "when_to_go": "Mayo-junio y septiembre-octubre: playas sin saturación, 22-26°C de agua y precios razonables. Julio-agosto es cuando se dispara todo (30€/noche de parking, colas en el mercado). El invierno es suave (12-16°C) y perfecto para visitas culturales sin multitudes.",
    "how_to_get_there": "Aeropuerto de Niza-Costa Azul con conexiones de toda Europa. Tram línea 2 al centro en 30 min (1,50€). TGV desde París en 5,5h. Desde Barcelona: bus o vuelo directo.",
    "where_to_sleep": [
        {"name": "Vieux-Nice", "description": "El casco histórico barroco junto al mar. Apartamentos desde 75€/noche, hoteles desde 90€. Animado y con el mejor mercado."},
        {"name": "Cimiez", "description": "El barrio residencial en las colinas, tranquilo con vistas. Hoteles desde 80€. Cerca de los museos Matisse y Chagall."},
        {"name": "Libération", "description": "El barrio de los locales, más económico y auténtico. Apartamentos desde 60€/noche."}
    ],
    "what_to_do": [
        {"title": "Cours Saleya y mercado", "description": "El mercado de flores y productos provenzales (martes-domingo mañanas) es uno de los más bonitos de Francia. Los lunes es mercado de antigüedades."},
        {"title": "Colline du Château", "description": "La colina sobre el Vieux-Nice con los mejores puntos de vista de la bahía de los Ángeles. Sube a pie o en ascensor gratuito. Ideal al atardecer."},
        {"title": "Musée Matisse", "description": "La colección más completa de Matisse del mundo, en una villa italiana en el barrio de Cimiez. El contexto — Matisse vivió en Niza 37 años — la hace especial (10€)."},
        {"title": "Excursión a Mónaco y Eze", "description": "El tren regional llega a Mónaco en 20 min (4€ ida y vuelta) y a Eze-sur-Mer en 15 min. El pueblo medieval de Eze a 429m sobre el mar es uno de los más espectaculares de Europa."},
        {"title": "Socca en la Vieille-Ville", "description": "La socca (crepe de harina de garbanzo a la plancha) se come de pie en el Cours Saleya o en Chez René Socca — 2-3€ por porción, absolutamente auténtico."},
        {"title": "Playas de la Promenade", "description": "Las playas de guijarros de la Promenade des Anglais son gratuitas (públicas) o con sombrilla de pago (15-20€). Las de Villefranche-sur-Mer (20 min en tren) son más tranquilas."}
    ],
    "food_and_drink": "La cocina niçoise tiene identidad propia: socca, pissaladière, salade niçoise (sin lechuga — con anchoas, huevo, judías verdes y olivas), pan bagnat (bocadillo niçois), ratatouille auténtica. El mercado del Cours Saleya es el mejor lugar para comer en verano (5-10€). Restaurante: 20-35€ por persona.",
    "safety": "Niza es segura. El Vieux-Nice tiene carteristas en temporada alta. La Promenade ha reforzado seguridad tras los atentados de 2016.",
    "visa_info": "Francia es UE y Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: euro.",
    "local_tips": ["El tren regional permite llegar a Mónaco, Cannes y Antibes sin coche — esencial", "La socca está mejor recién hecha, caliente, con pimienta — cómela de pie en el mercado", "Las playas de guijarros requieren chanclas — lleva las tuyas", "Aparcar en Niza en verano es prohibitivo — ven en tren", "La Carte d'Azur de 3 días (20€) cubre todo el transporte de la región"],
    "travel_styles": ["playa", "gastronomía", "cultura", "naturaleza"],
    "vibes": ["mediterranean", "provençal", "beach", "french riviera"],
    "climate": ["mediterranean"],
    "best_months": ["May", "June", "September", "October"],
    "budget_daily_low": 65, "budget_daily_mid": 130, "budget_daily_high": 300, "guide_quality": 8
},
{
    "slug": "ginebra", "name": "Ginebra", "country": "Suiza", "continent": "Europa", "type": "city",
    "coordinates": {"lat": 46.2044, "lng": 6.1432},
    "tagline": "El lago alpino más elegante de Europa, diplomacia y chocolate entre montañas",
    "intro": "Ginebra es pequeña (200.000 habitantes), cosmopolita y cara. Sede de la ONU, la Cruz Roja y 200 organizaciones internacionales, tiene un perfil diplomático que impregna la ciudad. El lago Léman (Lago de Ginebra) con el Jet d'Eau (el chorro de agua a 140m de altura) y los Alpes de fondo es una postal imposiblemente bonita.\n\nLo que distingue Ginebra de Zúrich es su herencia francesa — más mediterránea en temperamento, con mejor gastronomía en relación al precio y una escena cultural sorprendentemente activa para su tamaño. El barrio Carouge, justo al sur del centro, es el más auténtico y bohemio, con mercado propio y ambiente completamente distinto al centro financiero.\n\nVale la pena combinarla con Lausana (40 min en tren) y los viñedos de Lavaux (UNESCO), o con Chamonix en el lado francés para ver el Mont Blanc.",
    "when_to_go": "Mayo-septiembre: el lago en todo su esplendor, temperaturas de 20-26°C y los picos nevados de fondo. Diciembre tiene mercados navideños suizos excepcionales. El invierno es frío (2-7°C) pero con mucho menos turismo.",
    "how_to_get_there": "Aeropuerto internacional de Ginebra con conexiones globales. Tren al centro en 6 min (billete gratuito con la tarjeta del aeropuerto, recógela en la cinta de equipaje). TGV a París en 3,5h.",
    "where_to_sleep": [
        {"name": "Paquis", "description": "El barrio multicultural junto al lago y la estación. Hoteles desde 90 CHF, con acceso directo al lago."},
        {"name": "Carouge", "description": "El barrio bohemio al sur con el mejor ambiente local. Apartamentos desde 85 CHF/noche."},
        {"name": "Plainpalais", "description": "Barrio universitario con mercado de pulgas los miércoles y domingos. Más económico y animado."}
    ],
    "what_to_do": [
        {"title": "Paseo por el lago y Jet d'Eau", "description": "El Jet d'Eau (chorro de 140m visible desde 40km) es el símbolo de Ginebra. El paseo del Quai du Mont-Blanc con vistas a los Alpes es gratuito y obligatorio."},
        {"title": "Palacio de las Naciones (ONU)", "description": "La sede europea de la ONU recibe visitas guiadas (12 CHF) — el interior es fascinante y la Sala de los Derechos Humanos es una obra de arte contemporáneo."},
        {"title": "Museo de la Cruz Roja", "description": "Uno de los mejores museos temáticos del mundo: historia del humanitarismo desde Dunant y Solferino hasta hoy. Emocionalmente intenso (15 CHF)."},
        {"title": "Carouge y su mercado", "description": "El barrio con carácter sardo-piamontés tiene mercado los miércoles y sábados, talleres artesanales y los mejores bares de la ciudad."},
        {"title": "Viñedos de Lavaux (UNESCO)", "description": "Los terrazas de viñedo en el lago de Ginebra entre Lausana y Montreux son un espectáculo. Tren a Cully (30 min) + senderismo entre viñedos + cata de chasselas local."},
        {"title": "Excursión a Chamonix y Mont Blanc", "description": "A 80 min en coche o bus desde Ginebra, el teleférico del Aiguille du Midi (3.842m) lleva al techo de los Alpes. Espectacular en cualquier estación."}
    ],
    "food_and_drink": "Fondue de queso (Gruyère + Vacherin, 25-35 CHF), raclette, rösti y la fondue de chocolate son imprescindibles. Carouge tiene los mejores restaurantes a precios ligeramente más bajos que el centro. Los mercados de productores tienen quesos y vinos de la región del Lago a precios razonables.",
    "safety": "Ginebra es extremadamente segura. El barrio Paquis puede ser ruidoso por la noche, pero sin peligro real.",
    "visa_info": "Suiza no es UE pero sí Schengen. Ciudadanos UE entran con DNI. Españoles sin visado. Moneda: franco suizo (CHF).",
    "local_tips": ["El billete de tren gratuito del aeropuerto dura 80 minutos — suficiente para llegar al centro", "La Geneva Transport Card (gratuita con alojamiento en la ciudad) cubre todo el transporte público", "Carouge a pie desde el centro son 20 minutos y la diferencia de precio en bares/restaurantes es notable", "El mercado de Plainpalais los miércoles tiene los mejores quesos artesanales de la región", "El Jet d'Eau se apaga con viento fuerte o en invierno — consulta antes de ir"],
    "travel_styles": ["cultura", "naturaleza", "gastronomía", "diplomacia"],
    "vibes": ["cosmopolitan", "alpine", "lakeside", "swiss"],
    "climate": ["temperate oceanic"],
    "best_months": ["May", "June", "July", "August", "September"],
    "budget_daily_low": 100, "budget_daily_mid": 200, "budget_daily_high": 420, "guide_quality": 8
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
