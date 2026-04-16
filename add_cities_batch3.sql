-- ASIA (10 nuevas ciudades)

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'kabul', 'Kabul', 'Afganistán', 'Asia', 'city',
  '{"lat": 34.5253, "lng": 69.1783}',
  'La ciudad de las montañas y la historia milenaria',
  'Kabul, capital de Afganistán, es una de las ciudades más antiguas del mundo con más de 3.500 años de historia. Enclavada a 1.800 metros de altitud rodeada de montañas, ofrece bazares históricos, jardines mogoles y una cultura de hospitalidad extraordinaria. El viaje más desafiante puede ser también el más memorable.',
  'La primavera (marzo-mayo) y el otoño (septiembre-octubre) son las mejores épocas con temperaturas agradables. Los inviernos son fríos con nevadas frecuentes. Consulta siempre la situación de seguridad actualizada antes de planificar.',
  'El Aeropuerto Internacional Hamid Karzai conecta con Dubái, Estambul, Delhi y ciudades vecinas. Varias aerolíneas operan vuelos regulares. Dentro de la ciudad los taxis y rickshaws son el transporte habitual.',
  '[{"name": "Zona Diplomática / Wazir Akbar Khan", "description": "El barrio más seguro para extranjeros con hoteles internacionales. Desde 50-100 USD/noche."}, {"name": "Shahr-e Naw", "description": "Zona central con hoteles más económicos y restaurantes locales. Desde 20-40 USD/noche."}]',
  '[{"title": "Jardines de Babur (Bagh-e Babur)", "description": "Jardines mogoles del siglo XVI, lugar de descanso del fundador del Imperio Mogol. Vista panorámica de la ciudad."}, {"title": "Bazar de Chicken Street", "description": "El mercado más famoso para artesanía, alfombras, lapislázuli y antigüedades afganas."}, {"title": "Museo Nacional de Afganistán", "description": "Alberga piezas de la Ruta de la Seda y colecciones greco-budistas únicas pese a los daños de la guerra."}, {"title": "Ciudadela de Bala Hissar", "description": "Fortaleza histórica con vistas sobre la ciudad, testigo de siglos de historia afgana."}]',
  'La cocina afgana es abundante y sabrosa: el kabuli pulao (arroz con cordero y pasas) es el plato nacional. Prueba el mantu (raviolis), el bolani (pan relleno) y los kebabs de cordero. El té verde con cardamomo acompaña cada comida.',
  'Afganistán es uno de los destinos más complicados del mundo para viajeros. Consulta siempre el aviso de viaje de tu país antes de ir. Si viajas, hazlo con guía local de confianza, mantén perfil bajo y evita zonas conflictivas.',
  'Los ciudadanos de la mayoría de países necesitan visado previo para entrar a Afganistán. Tramítalo en la embajada afgana de tu país con antelación. La situación política actual complica los trámites — infórmate antes.',
  ARRAY['Lleva efectivo en USD o Afghani; las tarjetas de crédito no funcionan', 'El lapislázuli afgano es famoso mundialmente — compra en tiendas de confianza', 'La hospitalidad afgana es legendaria: si te invitan a comer, acepta', 'Fotografiar personas siempre con permiso previo'],
  ARRAY['Aventura', 'Cultura', 'Mochilero'],
  ARRAY['history', 'mountains', 'bazaars', 'culture'],
  ARRAY['continental', 'cold-winters', 'dry'],
  ARRAY['March', 'April', 'May', 'September', 'October'],
  20, 60, 150, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'macau', 'Macao', 'China (RAE Macao)', 'Asia', 'city',
  '{"lat": 22.1987, "lng": 113.5439}',
  'El Las Vegas de Asia donde Portugal se fundió con China',
  'Macao, la antigua colonia portuguesa hoy región administrativa especial de China, es un territorio único donde los casinos más grandes del mundo conviven con iglesias barrocas y calles adoquinadas. Con una densidad de población extraordinaria y una mezcla cultural fascinante, Macao es el territorio con mayor PIB per cápita del mundo gracias al juego.',
  'Todo el año es bueno aunque octubre-diciembre es ideal: temperaturas suaves (20-26°C) y menos lluvia. Evita los tifones de julio-septiembre. Semana Santa y el Gran Premio de Macao (noviembre) llenan hoteles — reserva con mucha antelación.',
  'Desde Hong Kong hay ferries rápidos (1h) y el puente Hong Kong-Zhuhai-Macao (cruzar en lanzadera). Desde el aeropuerto internacional de Macao (MFM) con vuelos directos a varias ciudades asiáticas. Los casinos ofrecen lanzaderas gratuitas desde el aeropuerto y el ferry.',
  '[{"name": "Cotai Strip", "description": "Los grandes resorts integrados con casinos, hoteles de lujo y entretenimiento. Desde 100 USD/noche."}, {"name": "Centro Histórico / Península", "description": "Hoteles boutique y guesthouses cerca del patrimonio UNESCO. Mejor relación calidad-precio, desde 50-80 USD/noche."}]',
  '[{"title": "Ruinas de São Paulo", "description": "La fachada barroca de la iglesia del siglo XVII es el símbolo más icónico de Macao. Vista obligada al atardecer."}, {"title": "Fortaleza del Monte", "description": "Fortaleza del siglo XVII con cañones y vistas panorámicas de toda la península."}, {"title": "A-Ma Temple", "description": "El templo más antiguo de Macao (siglo XV), dedicado a la diosa del mar. Origen del nombre Macao."}, {"title": "Cotai Strip y los mega-casinos", "description": "El Venetian, el City of Dreams, el Galaxy — arquitectura espectacular incluso si no juegas."}]',
  'La cocina macaense es única: fusión portuguesa-china con toques africanos y malasios. Prueba el galinha à portuguesa (pollo al curry), el bacalao a lo macaense, las pork chop buns (bolo bao) y los pastéis de nata. El dim sum también es excelente y económico.',
  'Macao es extremadamente seguro para los viajeros. El mayor riesgo es gastar más de lo planeado en los casinos. Cuida pertenencias en zonas muy concurridas.',
  'Los ciudadanos de la UE, EEUU y muchos otros países entran sin visado hasta 90 días. Pasaporte con 6 meses de vigencia. El visado de China no cubre Macao — necesitas permiso específico si entras desde China continental.',
  ARRAY['Los casinos ofrecen lanzaderas gratuitas — úsalas aunque no juegues', 'La comida macaense es más barata en la península que en el Cotai Strip', 'La Torre de Macao tiene bungee jumping y sky walk con vistas increíbles', 'Las calles empedradas del centro histórico son perfectas para perderse'],
  ARRAY['Ciudad', 'Gastronomía', 'Cultura'],
  ARRAY['casinos', 'heritage', 'fusion-culture', 'food'],
  ARRAY['subtropical', 'humid'],
  ARRAY['October', 'November', 'December', 'January', 'February'],
  60, 150, 400, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'shenzhen', 'Shenzhen', 'China', 'Asia', 'city',
  '{"lat": 22.5431, "lng": 114.0579}',
  'La ciudad que pasó de aldea de pescadores a metrópolis tecnológica en 40 años',
  'Shenzhen es el milagro económico chino hecho ciudad: en 1980 era un pueblo de 30.000 habitantes; hoy es una megalópolis de 13 millones y la capital mundial de la electrónica. Fronteriza con Hong Kong, concentra fábricas de tecnología, barrios de diseño, museos ultramodernos y una escena gastronómica vibrante. El futuro de China se llama Shenzhen.',
  'Octubre a diciembre es ideal: tiempo seco y fresco (18-25°C). Primavera (marzo-abril) también es buena. Evita julio-agosto (calor húmedo extremo, 32-38°C) y el Año Nuevo Chino cuando todo cierra.',
  'El aeropuerto de Bao an (SZX) conecta con toda China y muchas ciudades asiáticas. Desde Hong Kong: metro MTR hasta Lo Wu o Lok Ma Chau, cruzar frontera a pie (30 min). El metro de Shenzhen es moderno, extenso y muy económico (2-8 CNY).',
  '[{"name": "Luohu / Dongmen", "description": "Zona fronteriza con Hong Kong, animada y económica. Cerca del mercado electrónico de Huaqiangbei. Hostels desde 80 CNY."}, {"name": "Nanshan / OCT", "description": "Barrio moderno con galerías de arte, parques temáticos y hoteles de diseño. Desde 200-400 CNY/noche."}]',
  '[{"title": "Mercado de Huaqiangbei", "description": "El mercado de electrónica más grande del mundo: varios edificios repletos de todo tipo de gadgets, componentes y tecnología a precios de fábrica."}, {"title": "OCT Contemporary Art Terminal (OCAT)", "description": "Complejo de arte contemporáneo con exposiciones de artistas chinos e internacionales en un antiguo espacio industrial."}, {"title": "Dafen Oil Painting Village", "description": "El pueblo más surrealista: centenares de artistas producen réplicas de obras maestras y pinturas originales para el mercado global."}, {"title": "Shenzhen Bay Park", "description": "Paseo costero de 15 km con vistas a Hong Kong. Perfecto para bicicleta o carrera al atardecer."}]',
  'La gastronomía cantonesa es la base de Shenzhen: dim sum de calidad en cualquier barrio, mariscos frescos en el barrio de Shekou, hot pot y la cocina sichuan picante. Los mercados nocturnos ofrecen una experiencia auténtica. Comida excelente por 20-40 CNY.',
  'Shenzhen es una ciudad muy segura para los viajeros. El mayor reto es el idioma: pocos locales hablan inglés fuera de zonas turísticas. Descarga WeChat y el traductor de Google (con descarga offline previa).',
  'Los ciudadanos extranjeros necesitan visado chino excepto los de algunos países con acuerdo de exención. Existe un visado de tránsito de 72/144 horas para pasar sin visado. Solicita el visado con antelación en el consulado chino.',
  ARRAY['La VPN es imprescindible en China — configúrala antes de llegar', 'WeChat Pay y Alipay son las formas de pago; lleva algo de efectivo CNY de respaldo', 'Huaqiangbei es abrumador — ve con lista de lo que buscas', 'El metro te lleva a casi todo; evita taxis en hora punta'],
  ARRAY['Ciudad', 'Tecnología', 'Negocios'],
  ARRAY['technology', 'modern', 'business', 'innovation'],
  ARRAY['subtropical', 'humid'],
  ARRAY['October', 'November', 'December', 'March', 'April'],
  30, 80, 200, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'chengdu', 'Chengdu', 'China', 'Asia', 'city',
  '{"lat": 30.5728, "lng": 104.0668}',
  'La capital del panda, del Sichuan picante y del arte de vivir chino',
  'Chengdu, capital de la provincia de Sichuan en el corazón de China, es una ciudad que ha dominado el arte de vivir bien durante siglos. Famosa mundialmente por sus pandas gigantes, su cocina explosivamente picante y sus teahouses donde la gente juega mahjong durante horas, Chengdu combina una vida cotidiana relajada con una modernidad pujante. Puerta de entrada al Tíbet y al Giant Panda country.',
  'Primavera (marzo-mayo) y otoño (septiembre-noviembre) son ideales. Chengdu es famosa por sus días nublados — el sol es una rareza. Julio-agosto es caluroso y húmedo. El Año Nuevo chino dispara los precios.',
  'El aeropuerto de Chengdu Tianfu (TFU), inaugurado en 2021, tiene excelentes conexiones nacionales e internacionales (Europa, Sudeste Asiático). El tren de alta velocidad conecta con Pekín (8h), Shanghái (11h) y Xi\'an (3h). El metro cubre bien la ciudad.',
  '[{"name": "Jinjiang District", "description": "El centro histórico con la famosa calle Jinli y el barrio de Kuanzhai Alley. Hostels desde 80 CNY, hoteles boutique desde 300 CNY."}, {"name": "Chunxi Road / Tianfu Square", "description": "Zona moderna y comercial, bien comunicada. Hotels mid-range desde 200-400 CNY/noche."}]',
  '[{"title": "Base de Investigación de Pandas Gigantes", "description": "Ver pandas gigantes y pandas rojos en su ambiente natural recreado. Llega temprano (8-10h) para ver a los pandas más activos."}, {"title": "Barrio de Kuanzhai Alley", "description": "Las calles anchas y estrechas — arquitectura Qing restaurada con teahouses, restaurantes y arte. El corazón del Chengdu tradicional."}, {"title": "Templo de Wuhou", "description": "El templo más importante de Chengdu, dedicado a los héroes del período de los Tres Reinos. Adyacente al animado barrio de Jinli."}, {"title": "Sanxingdui Museum (día de excursión)", "description": "A 40 km, uno de los museos arqueológicos más extraordinarios del mundo: máscaras de bronce de una civilización desconocida de 3.000 años."}]',
  'La cocina sichuan es una de las grandes cocinas del mundo: mapo tofu (tofu en salsa de chile y pimienta sichuan), hot pot sichuan (el más picante), dan dan noodles, gong bao pollo. El numbing-spicy de la pimienta sichuan es única. Precio: 20-50 CNY por plato.',
  'Chengdu es una ciudad muy segura. El mayor reto es el idioma. Descarga el traductor offline y aprende los caracteres básicos. Las estafas del té son comunes — desconfía de extraños que te inviten a una "tea ceremony".',
  'Requiere visado chino para la mayoría de nacionalidades. Existen políticas de tránsito de 72/144h. Solicita el visado con 4-6 semanas de antelación. Los ciudadanos de varios países europeos tienen acuerdos de exención — verifica tu caso.',
  ARRAY['Llega a la base de pandas antes de las 9h para verlos desayunando', 'La pimienta sichuan no pica sino que entumece la boca — efecto único', 'Las teahouses en el templo de Wangjiang son perfectas para pasar la tarde', 'El tren de alta velocidad a Xi\'an es espectacular y muy cómodo'],
  ARRAY['Cultura', 'Gastronomía', 'Naturaleza'],
  ARRAY['culture', 'food', 'pandas', 'history', 'relaxed'],
  ARRAY['temperate', 'cloudy', 'humid'],
  ARRAY['March', 'April', 'May', 'September', 'October', 'November'],
  25, 70, 180, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'xian', 'Xián', 'China', 'Asia', 'city',
  '{"lat": 34.3416, "lng": 108.9398}',
  'El ejército de terracota, las murallas milenarias y el inicio de la Ruta de la Seda',
  'Xián fue la capital imperial de China durante más de 1.000 años y punto de partida de la legendaria Ruta de la Seda. Hoy guarda el secreto mejor conservado de la arqueología mundial — el ejército de terracota del Primer Emperador — y mantiene unas murallas del siglo XIV que rodean el centro histórico. Su vibrante barrio musulmán (Hui) añade una dimensión cultural única a esta ciudad de 12 millones de habitantes.',
  'Primavera (abril-mayo) y otoño (septiembre-octubre) son perfectos. Los inviernos son fríos pero manejables (0-8°C). Verano (junio-agosto) es caluroso y húmedo (35°C). Evita el Año Nuevo chino y la Semana Dorada de octubre.',
  'El aeropuerto de Xianyang (XIY) tiene vuelos directos desde Europa (con escalas) y excelentes conexiones domésticas. El tren de alta velocidad conecta con Pekín (4,5h), Shanghái (5,5h) y Chengdu (3h). El metro de Xián es moderno y económico.',
  '[{"name": "Barrio de Beilin / Centro Histórico", "description": "Dentro de las murallas, cerca del Barrio Musulmán. Hoteles boutique en casas tradicionales (courtyard hotels) desde 200-500 CNY."}, {"name": "Yanta District", "description": "Zona moderna con muchos hoteles de cadena. Bien comunicado. Desde 200-400 CNY/noche."}]',
  '[{"title": "Ejército de Terracota", "description": "A 35 km de la ciudad, los 8.000 guerreros de arcilla del Primer Emperador son una de las maravillas arqueológicas más asombrosas del mundo. Visita las tres fosas."}, {"title": "Murallas de la ciudad", "description": "Las murallas del siglo XIV, las mejor conservadas de China, rodean el casco antiguo. Alquila una bicicleta y dale la vuelta completa (14 km, 1,5h)."}, {"title": "Barrio Musulmán (Huimin Jie)", "description": "El barrio de la minoría Hui con la Gran Mezquita Tang, calles de comida callejera y artesanía. El más animado al caer la tarde."}, {"title": "Gran Pagoda del Ganso Salvaje", "description": "Pagoda budista del siglo VII en el corazón de la ciudad. Los jardines que la rodean se iluminan espectacularmente por la noche."}]',
  'El barrio musulmán concentra la mejor comida callejera: los rou jia mo (bocadillos de cerdo o cordero picado, el hamburger chino), los noodles biang biang, el yang rou pao mo (sopa de cordero con pan), los persimmons secos y el jingao (turrón de arroz). Comida barata y abundante — 15-40 CNY por ración.',
  'Xián es una ciudad segura. El mayor riesgo son las estafas clásicas de los tea houses cerca de los monumentos. Las colas para el Ejército de Terracota son enormes en temporada alta — reserva entradas online con antelación.',
  'Visado chino necesario para la mayoría de viajeros. Política de tránsito de 72/144h disponible. Consulta acuerdos bilaterales de tu país. Tramita el visado con al menos un mes de antelación.',
  ARRAY['Reserva las entradas al Ejército de Terracota online — las colas son brutales', 'Alquila bici en las murallas al amanecer para verlas sin multitudes', 'El barrio musulmán está más tranquilo y auténtico a las 8-10h de la mañana', 'El tren nocturno Xián-Pekín es una experiencia clásica de la China viajera'],
  ARRAY['Cultura', 'Historia', 'Gastronomía'],
  ARRAY['history', 'silk-road', 'ancient', 'culture', 'food'],
  ARRAY['continental', 'four-seasons'],
  ARRAY['April', 'May', 'September', 'October'],
  25, 70, 200, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'surabaya', 'Surabaya', 'Indonesia', 'Asia', 'city',
  '{"lat": -7.2575, "lng": 112.7521}',
  'La ciudad de los héroes, puerta de entrada a Java Oriental',
  'Surabaya, la segunda ciudad más grande de Indonesia, es una metrópolis portuaria con carácter propio. Conocida como "Kota Pahlawan" (Ciudad de los Héroes) por su resistencia colonial, combina barrios históricos coloniales holandeses, una vibrante comunidad china, mezquitas históricas y una gastronomía reconocida como de las mejores de Java. Es la puerta de entrada al Monte Bromo, Ijen y el Este de Java.',
  'Mayo a septiembre (estación seca) es el mejor momento: cielos despejados y condiciones perfectas para excursiones al Bromo e Ijen. Octubre a abril es temporada de lluvias pero la ciudad sigue activa. Evita las multitudes del Eid y las vacaciones indonesias.',
  'El aeropuerto internacional Juanda (SUB) tiene vuelos directos desde Singapur, Kuala Lumpur y conexiones domésticas excelentes. Trenes cómodos desde Yogyakarta (5h) y Yakarta (12h en tren noche). Dentro de la ciudad: GoJek/Grab son imprescindibles.',
  '[{"name": "Zona Centro / Tunjungan", "description": "El corazón comercial con hoteles económicos y de gama media. Bien comunicado. Desde 150.000 IDR/noche."}, {"name": "Ciputra World Area", "description": "Zona moderna con hoteles internacionales de cadena. Más tranquila. Desde 400.000-800.000 IDR/noche."}]',
  '[{"title": "Casa de Sourabaya (Gedung Siola)", "description": "Icónico edificio colonial holandés convertido en museo de la historia de la ciudad con exposiciones interactivas."}, {"title": "Barrio Chino de Kembang Jepun", "description": "El barrio chino más antiguo de Indonesia con la Klenteng Boo Agung, la templo más importante de la comunidad china javanesa."}, {"title": "Monkasel (Submarino Monumento)", "description": "Un submarino de la guerra fría KRI Pasopati convertido en museo flotante — inusual y fascinante."}, {"title": "Excursión al Monte Bromo", "description": "A 3-4h de Surabaya, el volcán más dramático de Indonesia con el famoso amanecer sobre el mar de arena. Excursión de un día o noche."}]',
  'La gastronomía de Surabaya es famosa en Indonesia: la rawon (sopa negra de kluwek con carne), el lontong kupang, el bebek goreng (pato frito) y el rujak cingur (ensalada con morro de vaca) son especialidades locales. El Pasar Atom y los warungs de la ciudad son las mejores opciones.',
  'Surabaya es generalmente segura para viajeros. Cuidado con los pickpockets en zonas muy concurridas. Usa Grab/GoJek en lugar de taxis de la calle para evitar precios inflados.',
  'Los ciudadanos de la UE, EEUU, Australia y muchos otros países entran sin visado 30 días a Indonesia (ampliable a 60 con el Visa on Arrival pagando USD 35). Pasaporte con 6 meses de vigencia.',
  ARRAY['Desde Surabaya es fácil llegar al Monte Bromo y al Cráter Ijen — reserva tours desde tu alojamiento', 'GoJek es más barato que Grab para desplazamientos cortos', 'La rawon se sirve a todas horas en los warungs — perfecta para el desayuno', 'El barrio chino Kembang Jepun es más auténtico y tranquilo que los turísticos'],
  ARRAY['Cultura', 'Aventura', 'Gastronomía'],
  ARRAY['culture', 'gateway', 'food', 'colonial'],
  ARRAY['tropical', 'humid'],
  ARRAY['May', 'June', 'July', 'August', 'September'],
  20, 50, 130, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'male', 'Malé', 'Maldivas', 'Asia', 'city',
  '{"lat": 4.1755, "lng": 73.5093}',
  'La capital más pequeña del mundo, puerta al paraíso tropical',
  'Malé, la capital de Maldivas, es una de las ciudades más densamente pobladas del planeta: 130.000 personas en una isla de apenas 2 km². Aunque la mayoría de viajeros solo pasan por aquí de camino a los resorts de atolón, Malé tiene su propia personalidad: mezquitas blancas, un mercado de atún animadísimo, calles estrechas y una vida cotidiana maldiviana auténtica lejos del turismo de lujo.',
  'Diciembre a abril (temporada seca) es perfecta: aguas cristalinas, poca lluvia y sol garantizado. Mayo a noviembre es temporada húmeda con aguaceros frecuentes pero playas prácticamente vacías. Las temperaturas son constantes todo el año (28-32°C).',
  'El Aeropuerto Internacional Velana (MLE) en la isla de Hulhulé, conectado a Malé por ferry (15 min, 10 MVR) o speedboat (5 min, 15 USD). Vuelos directos desde Dubái, Singapur, Sri Lanka, India y varias capitales europeas. Seaplanes y lanchas rápidas conectan con los atolones.',
  '[{"name": "Centro de Malé", "description": "Guesthouses y hoteles de gama media en la ciudad. La opción más auténtica para conocer la vida local. Desde 50-100 USD/noche."}, {"name": "Hulhumalé", "description": "Isla artificial conectada al aeropuerto, con alojamientos más baratos y tranquilos. Desde 40-80 USD/noche."}]',
  '[{"title": "Mezquita del Viernes (Hukuru Miskiy)", "description": "La mezquita más antigua de Maldivas (1658), con intrincados trabajos en coral y madera de coco. La más importante del país."}, {"title": "Mercado de Malé", "description": "El mercado local de atún, frutas tropicales y verduras abre cada mañana — el más auténtico vistazo a la vida maldiviana cotidiana."}, {"title": "Cementerio Nacional", "description": "Curioso por las antiguas tumbas de coral y las inscripciones en dhivehi; testigo tranquilo de la historia del archipiélago."}, {"title": "Day trip a Maafushi", "description": "La isla local más popular: playas blancas, snorkel accesible, restaurantes de pescado y ambiente maldiviano sin precios de resort. Ferry desde Malé."}]',
  'La cocina maldiviana gira en torno al atún (mas) y el coco: el mas riha (curry de atún), el garudhiya (sopa clara de atún), el bajiya (empanadillas de atún y coco) y el short eats de los cafés locales. El té negro con leche acompaña cada día. Malé tiene restaurantes económicos (hedhika) donde comer bien por 5-8 USD.',
  'Malé y Maldivas en general son muy seguros para viajeros. El país es 100% musulmán — respeta las normas locales, cubre hombros y rodillas en la capital. Beber alcohol solo está permitido en resorts y áreas turísticas.',
  'Los ciudadanos de prácticamente todos los países entran sin visado, recibiendo un permiso de 30 días a la llegada (gratuito). Solo necesitas billete de salida y fondos suficientes. No hay restricciones de nacionalidad.',
  ARRAY['Malé se visita en un día — combínala con una island hopping o resort', 'Los guesthouses en islas locales son la opción económica auténtica de Maldivas', 'El ferry a Hulhulé para el aeropuerto cuesta menos de 1 USD — ignora los speedboats caros', 'Busca las "local islands" como Maafushi o Dhigurah para snorkel sin pagar precios de resort'],
  ARRAY['Playa', 'Lujo', 'Naturaleza'],
  ARRAY['tropical', 'islands', 'ocean', 'relaxed'],
  ARRAY['tropical', 'warm'],
  ARRAY['December', 'January', 'February', 'March', 'April'],
  60, 150, 500, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'thimphu', 'Timbu', 'Bután', 'Asia', 'city',
  '{"lat": 27.4728, "lng": 89.6393}',
  'La única capital del mundo sin semáforos, en el reino feliz del Himalaya',
  'Timbu, capital de Bután, es probablemente la capital más tranquila y peculiar del mundo: sin semáforos, con arquitectura tradicional por decreto real y en un reino que mide la felicidad como política de estado. A 2.320 metros de altitud en el valle del río Wang Chhu, Timbu es la puerta de entrada a un país que limitó deliberadamente el turismo masivo para preservar su cultura y naturaleza himalaya.',
  'Primavera (marzo-mayo) y otoño (septiembre-noviembre) son los mejores meses: cielos despejados, temperaturas agradables (10-20°C) y festivales Tshechu espectaculares. El invierno (dic-feb) es frío pero tranquilo. Monzón (jun-ago) con lluvias.',
  'El pequeño aeropuerto de Paro (PBH), uno de los más difíciles del mundo para pilotar, conecta con Delhi, Singapur, Bangkok, Katmandú y Dhaka via Druk Air y Bhutan Airlines. Desde el aeropuerto a Timbu en coche 1h por una carretera espectacular.',
  '[{"name": "Centro de Timbu", "description": "La mayoría de hoteles se concentran en el centro cerca del Chorten Memorial y Norzin Lam. Desde 50-100 USD/noche para viajeros con Sustainable Development Fee ya pagada."}, {"name": "Zonas periféricas del valle", "description": "Hoteles boutique y lodges con vistas al valle. Desde 100-300 USD/noche."}]',
  '[{"title": "Tashichho Dzong", "description": "La imponente fortaleza monástica blanca que alberga el gobierno butanés y el trono del rey. Visita obligada al atardecer."}, {"title": "Buddha Dordenma", "description": "Una colosal estatua dorada de Buda de 51 metros en una colina con vistas panorámicas del valle de Timbu."}, {"title": "Memorial Chorten", "description": "El stupa más visitado de Bután, construido en 1974 en memoria del tercer rey. Los locales lo circunvalan en oración toda la mañana."}, {"title": "Museo Textile Nacional", "description": "La mejor introducción a la intrincada tradición textil butanesa: los mejores tejidos del Himalaya con sus significados."}]',
  'La cocina butanesa es picante y sustanciosa: el ema datshi (chile picante con queso de yak) es el plato nacional que aparece en todas las mesas. El red rice butanés es único. El momo (raviolis al vapor) y el phaksha paa (cerdo con chile) completan el menú. El butter tea (suja) con mantequilla de yak es la bebida tradicional.',
  'Bután es extremadamente seguro, prácticamente sin crimen turístico. El reto principal es el coste: todos los visitantes deben contratar un paquete turístico con guía local y pagar la Sustainable Development Fee (100 USD/día para ciudadanos no SAARC).',
  'Para visitar Bután, ciudadanos de casi todos los países (excepto India, Bangladesh y Maldivas) necesitan: 1) visa butanesa (40 USD, gestionada a través de tu agencia de viajes local), 2) contratar tour package con agencia autorizada butanesa, 3) pagar Sustainable Development Fee (100 USD/día). No se puede viajar independiente.',
  ARRAY['La Sustainable Development Fee incluye alojamiento, comidas y guía — no es tan cara como parece', 'El festival Tshechu de Paro (marzo-abril) es uno de los mejores del Asia — reserva con meses de antelación', 'El ema datshi es más picante de lo que parece — pide "less spicy" si no toleras bien el picante', 'Caminar de Timbu a Paro por los montes es una experiencia himalaya al alcance de todos'],
  ARRAY['Cultura', 'Naturaleza', 'Aventura'],
  ARRAY['culture', 'mountains', 'buddhism', 'unique', 'peaceful'],
  ARRAY['highland', 'temperate'],
  ARRAY['March', 'April', 'May', 'September', 'October', 'November'],
  80, 150, 300, 8
) ON CONFLICT (slug) DO NOTHING;

-- EUROPA (12 nuevas ciudades)

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'poznan', 'Poznan', 'Polonia', 'Europa', 'city',
  '{"lat": 52.4064, "lng": 16.9252}',
  'La ciudad polaca más alegre, con los mejores mercados navideños y la Stare Miasto que enamora',
  'Poznan, ciudad de 550.000 habitantes en el corazón de la Gran Polonia, es una de las ciudades más auténticas e infravaloradas de Polonia. Su Rynek (plaza mayor) es una de las más bellas del país, con sus coloridas casas góticas y sus famosas cabras mecánicas que salen cada mediodía del reloj del Ayuntamiento. Universidad vibrante, escena gastronómica en auge y una historia que se remonta al origen mismo de Polonia.',
  'Mayo a septiembre es ideal: temperaturas agradables (20-28°C) y todo al aire libre. Diciembre es mágico por los mercados navideños. Enero-febrero es frío pero muy económico. Evita julio-agosto si no te gustan las multitudes universitarias.',
  'El aeropuerto de Lawica (POZ) con vuelos directos desde muchas ciudades europeas. Tren desde Varsovia (2,5h) y Berlín (3h) con la conexión más rápida de Europa Central. Poznán está en la ruta Berlín-Varsovia.',
  '[{"name": "Stare Miasto (Ciudad Vieja)", "description": "El corazón de Poznan junto al Rynek. Hostels desde 15 EUR/noche, hoteles boutique desde 50-80 EUR."}, {"name": "Jeżyce", "description": "El barrio hipster en auge con cafés de especialidad, restaurantes independientes y ambiente local auténtico. Desde 40-70 EUR/noche."}]',
  '[{"title": "Rynek y el Ayuntamiento con las cabras", "description": "La plaza mayor rodeada de casas coloridas. A mediodía, dos cabras mecánicas salen del reloj del Ayuntamiento y se topetean — desde 1551."}, {"title": "Ostrów Tumski", "description": "La isla catedralicia, el lugar más antiguo de Polonia. La Catedral de San Pedro y San Pablo fue la primera catedral del país (siglo X)."}, {"title": "Citadela de Poznan", "description": "El mayor parque de la ciudad con cementerios militares y los restos de la ciudadela prusiana. Paseo histórico imprescindible."}, {"title": "Barrio de Malta y el lago artificial", "description": "El área de ocio con el lago artificial, el tobogán de montaña y pistas de esquí de fondo. Perfecto para familias."}]',
  'La cocina de Gran Polonia tiene sus propias especialidades: el rogal świętomarcińskiy (el cruasán de San Martín relleno de pasta de amapola, DOP), la pyra z gzikiem (patata con queso fresco y cebollino), la czernina (sopa de sangre de pato) y la cerveza Lech, fabricada en la ciudad. El mercado del Stary Browar es perfecto para probar lo local.',
  'Poznan es una de las ciudades más seguras de Polonia. Cuidado con el tráfico en bici — los carriles bici no siempre son evidentes. El nivel de inglés es muy alto entre los jóvenes.',
  'Polonia forma parte de la Unión Europea y el espacio Schengen. Los ciudadanos de la UE entran con DNI. Los de EEU, Canadá, Australia y la mayoría de países desarrollados entran sin visado hasta 90 días. Moneda: Zloty polaco (PLN).',
  ARRAY['Las cabras del reloj salen exactamente a las 12:00 — llega 10 min antes para coger sitio', 'El rogal świętomarcińskiy solo se vende oficialmente en Poznan el 11 de noviembre (San Martín)', 'El barrio de Jeżyce es el antídoto perfecto al turismo — cenas auténticas a mitad de precio', 'La tarjeta de 24h de transporte público cuesta 4 PLN y vale para todo'],
  ARRAY['Cultura', 'Ciudad', 'Gastronomía'],
  ARRAY['history', 'charming', 'authentic', 'university'],
  ARRAY['continental', 'four-seasons'],
  ARRAY['May', 'June', 'July', 'August', 'September', 'December'],
  30, 60, 120, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'gdansk', 'Gdansk', 'Polonia', 'Europa', 'city',
  '{"lat": 54.3520, "lng": 18.6466}',
  'La ciudad del ámbar, Solidaridad y los astilleros que cambiaron la historia',
  'Gdansk, en la costa báltica de Polonia, es una ciudad de historia densa y belleza sorprendente. Fue aquí donde comenzó la Segunda Guerra Mundial (el bombardeo del Westerplatte en 1939) y donde terminó el comunismo europeo (Solidarność y los astilleros en 1980). El Casco Antiguo reconstruido es uno de los más hermosos de Europa del Norte, con sus casas flamencas y sus calles empedradas brillando junto al río Motława.',
  'Junio a agosto es la temporada alta: sol, terrazas y el festival de San Domingo. Primavera y otoño son ideales para el turismo cultural sin multitudes. El invierno báltico es crudo pero barato; el mercado navideño es de los mejores de Polonia.',
  'El aeropuerto de Gdansk Lech Walesa (GDN) con vuelos directos desde toda Europa. Tren desde Varsovia (3h AVE polaco) y Cracovia (5h). La ciudad es perfecta para combinar con Gdynia y Sopot (trimetropía — tren urbano SKM).',
  '[{"name": "Ciudad Vieja (Główne Miasto)", "description": "Calles de adoquín junto al Motława. Hostels desde 15 EUR, hoteles en casas históricas desde 60-100 EUR."}, {"name": "Wrzeszcz", "description": "El barrio universitario auténtico, más económico y local. Bien conectado al centro. Desde 40-60 EUR/noche."}]',
  '[{"title": "Calle Dluga y la Puerta Zlota", "description": "La arteria principal del casco antiguo con las casas más fotogénicas de Polonia. El Neptuno de bronce es el símbolo de Gdansk."}, {"title": "Museo Europeo de Solidaridad", "description": "Uno de los mejores museos de Europa, narra la historia del sindicato que derrumbó el comunismo. Imprescindible — reserva entrada online."}, {"title": "La Grúa (Zuraw)", "description": "La grúa medieval más grande de Europa (siglo XV) a orillas del Motława. Hoy museo de arqueología naval."}, {"title": "Westerplatte", "description": "El promontorio donde comenzó la IIGM el 1 de septiembre de 1939. Memorial sobrio y emocionante."}]',
  'La cocina gdañesa mezcla influencias polacas, alemanas y nórdicas: el żurek (sopa ácida de centeno con huevo), los śledzie (arenques marinados), el bigos con carne de caza y las pierogi rellenas de col y setas. El ámbar es la especialidad artesanal — compra solo en tiendas certificadas.',
  'Gdansk es muy segura. En verano (temporada de turismo masivo) cuida tu cartera en zonas turísticas. El nivel de inglés es alto, especialmente entre jóvenes.',
  'Schengen/UE. Los ciudadanos de la UE entran con DNI. La mayoría de países occidentales sin visado 90 días. Moneda: Zloty polaco (PLN).',
  ARRAY['El ámbar falso es habitual — compra solo con certificado de autenticidad', 'El SKM (tren urbano) conecta Gdansk-Sopot-Gdynia en 15 min — perfecto para una jornada completa', 'Sopot tiene la playa más elegante y el muelle más largo de madera de Europa', 'El Museo de Solidaridad cierra los lunes — comprueba horarios antes de ir'],
  ARRAY['Cultura', 'Historia', 'Ciudad'],
  ARRAY['history', 'amber', 'hanseatic', 'coastal'],
  ARRAY['continental', 'cool'],
  ARRAY['June', 'July', 'August', 'September'],
  30, 65, 130, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'tesalonica', 'Tesalónica', 'Grecia', 'Europa', 'city',
  '{"lat": 40.6401, "lng": 22.9444}',
  'La segunda ciudad de Grecia con la mejor gastronomía del país',
  'Tesalónica, con 1 millón de habitantes, es la segunda ciudad de Grecia y, en opinión de muchos griegos, la primera en comida, ambiente y autenticidad. Capital de Macedonia griega, combina 2.300 años de historia — romana, bizantina, otomana — con una universidad vibrante, una vida nocturna legendaria y una cocina reconocida como la mejor de toda Grecia. Sin la saturación turística de Atenas.',
  'Primavera (abril-junio) y otoño (septiembre-octubre) son perfectos: 20-28°C, sin multitudes y con el mejor ambiente. El verano (julio-agosto) es caluroso (35°C) pero la vida nocturna es en su punto álgido. Diciembre-febrero es frío pero mágico y barato.',
  'El aeropuerto Makedonia (SKG) con vuelos directos desde toda Europa. Tren desde Atenas (5h) o autobús (6h). La ciudad es perfecta a pie en el centro histórico; metro inaugurado en 2023.',
  '[{"name": "Centro Histórico", "description": "Cerca de la Rotonda, el Arco de Galerio y la iglesia de Hagios Demetrios. Hostels desde 15 EUR, hoteles desde 50-80 EUR."}, {"name": "Ladadika", "description": "El barrio de los almacenes reconvertidos en bares y restaurantes. El más animado por la noche. Desde 60-100 EUR/noche."}]',
  '[{"title": "Paseo marítimo Nikis", "description": "El paseo frente al Mar Egeo con la Torre Blanca (símbolo de la ciudad) al fondo. El corazón de la vida tesalonicense."}, {"title": "La Torre Blanca (Lefkos Pyrgos)", "description": "Símbolo de Tesalónica, esta torre otomana del siglo XV es hoy museo de la historia de la ciudad con vistas panorámicas."}, {"title": "Sitios Paleocristianos y Bizantinos (UNESCO)", "description": "15 monumentos declarados Patrimonio UNESCO: la Rotonda, el Arco de Galerio, las basílicas paleocrisitianas... La Roma del Este."}, {"title": "Barrio de Ano Poli", "description": "La ciudad alta con casas otomanas, murallas bizantinas y la mejor vista sobre Tesalónica. El barrio más auténtico."}]',
  'Tesalónica tiene fama de ser la capital gastronómica griega: el bougatsa (hojaldre con natillas o queso, desayuno obligado), los meze de Ladadika, las pitas macedonias, el souvlaki y los mariscos del Egeo. El café freddo y el frappe son omnipresentes. Come tarde — los griegos cenan después de las 21h.',
  'Tesalónica es muy segura para los viajeros. El barrio de Ano Poli puede ser solitario por la noche — ve con compañía. Ojo con los buhoneros en la zona turística.',
  'Grecia pertenece al Espacio Schengen. Ciudadanos UE con DNI. Mayoría de países occidentales sin visado 90 días. Moneda: Euro.',
  ARRAY['El bougatsa del Bougatsadiko Thessaloniki es el mejor desayuno de Grecia — abre a las 6h', 'El paseo marítimo al atardecer con la Torre Blanca al fondo es la foto más tesalonicense', 'Ladadika tiene los mejores meze del país — ve a cenar entre semana para evitar grupos', 'El Ano Poli se sube mejor en taxi o a pie desde la muralla — merece el esfuerzo'],
  ARRAY['Gastronomía', 'Cultura', 'Ciudad'],
  ARRAY['food', 'history', 'byzantine', 'nightlife', 'authentic'],
  ARRAY['mediterranean', 'warm'],
  ARRAY['April', 'May', 'June', 'September', 'October'],
  35, 70, 150, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'palermo', 'Palermo', 'Italia', 'Europa', 'city',
  '{"lat": 38.1157, "lng": 13.3615}',
  'La capital siciliana del caos magnífico, los mosaicos dorados y el arancino',
  'Palermo, capital de Sicilia, es una ciudad que seduce por su caos apasionante: mercados bulliciosos con 1.000 años de historia, iglesias normando-árabes con mosaicos dorados relucientes, calles barrocas y una gastronomía de las más ricas del Mediterráneo. Tres culturas — árabe, normanda, española — dejaron su huella en la ciudad más auténtica de Italia, aún no masificada como Roma o Florencia.',
  'Mayo-junio y septiembre-octubre son perfectos: clima mediterráneo ideal (22-28°C) sin el agobio del verano. Julio-agosto es caluroso (35°C) y más lleno de turistas. Noviembre a marzo es temporada baja — fresco pero con los mercados en plena actividad.',
  'El aeropuerto de Palermo Falcone-Borsellino (PMO) con vuelos directos desde toda Europa. Ferries desde Nápoles, Génova, Civitavecchia (Roma). Dentro de la ciudad: el centro se recorre a pie; buses para zonas más lejanas.',
  '[{"name": "Ballarò / Centro Histórico", "description": "Cerca de los mercados más auténticos y los monumentos normando-árabes. B&Bs desde 50 EUR, hoteles boutique desde 80-120 EUR."}, {"name": "Mondello / Politeama", "description": "Zona más elegante y moderna. Hoteles de categoría desde 100-200 EUR/noche."}]',
  '[{"title": "Cappella Palatina", "description": "La Capilla Palatina del Palazzo dei Normanni es una de las joyas del arte mundial: mosaicos dorados bizatinos del siglo XII de una perfección absoluta."}, {"title": "Mercado de Ballarò", "description": "El mayor mercado callejero de Palermo, en continuo desde la época árabe. Atún fresco, especias, verduras y el ambiente más auténtico de Sicilia."}, {"title": "Catedral Normanda", "description": "La catedral de Palermo mezcla estilos árabe, normando, gótico y barroco en una fusión arquitectónica única. Las tumbas reales albergan a Federico II."}, {"title": "Catacumbas de los Capuchinos", "description": "8.000 cuerpos momificados expuestos en galerías — perturbador, único y fascinante. Una de las experiencias más insólitas del mundo."}]',
  'La gastronomía palermitana es extraordinaria: el arancino (bola de arroz frita), el pane e panelle (bocadillo de garbanzos fritos), el stigghiola (intestinos de cordero a la brasa del mercado), la caponata de berenjenas y los cannoli con ricotta fresca. El granizado de almendras con brioche es el desayuno siciliano perfecto.',
  'Palermo es generalmente segura aunque el centro histórico tiene zonas con más carteristas que en otras ciudades italianas. Cuida el móvil y la cámara en los mercados. Los scooters son el mayor peligro del tráfico.',
  'Italia forma parte del Espacio Schengen. Ciudadanos UE con DNI. Mayoría de países occidentales sin visado 90 días. Moneda: Euro.',
  ARRAY['El mercado de Ballarò está más animado de 8h a 14h — ve con el estómago vacío', 'Los arancini de "Ke Palle" en el centro son los mejores de la ciudad', 'La Cappella Palatina cierra al mediodía — ve a primera hora con entrada reservada', 'Pasear de noche por el Quattro Canti y el Ballarò es completamente seguro y muy animado'],
  ARRAY['Gastronomía', 'Cultura', 'Historia'],
  ARRAY['food', 'baroque', 'markets', 'authentic', 'history'],
  ARRAY['mediterranean', 'warm', 'sunny'],
  ARRAY['May', 'June', 'September', 'October'],
  40, 80, 180, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'valencia', 'Valencia', 'España', 'Europa', 'city',
  '{"lat": 39.4699, "lng": -0.3763}',
  'La cuna de la paella, el fuego de las Fallas y el Mediterráneo a dos pedales',
  'Valencia, la tercera ciudad de España y una de las más habitables de Europa, ha sabido reinventarse sin perder su esencia mediterránea. La ciudad donde nació la paella celebra las Fallas más explosivas del mundo, tiene el frente marítimo más transformado de España (gracias a la Copa América y la Fórmula 1) y una Ciudad de las Artes y las Ciencias que es una declaración de principios arquitectónica. Todo esto en una ciudad donde la vida sucede en la calle, en el mercado y en la terraza.',
  'Primavera (marzo-mayo) y otoño (septiembre-noviembre) son perfectos: 20-28°C, playa aún disfrutable. Las Fallas (del 1 al 19 de marzo) son el evento más espectacular de España — reserva con meses de antelación y paga el triple. Verano es cálido y con playa, pero julio-agosto es lo más masificado.',
  'El aeropuerto de Valencia (VLC) con conexiones directas a toda Europa. AVE desde Madrid (1h40) y Barcelona (3h). La ciudad tiene un excelente transporte público (metro, tranvía, bus) y es perfecta en bicicleta (Valenbisi).',
  '[{"name": "Ruzafa / Eixample", "description": "El barrio más auténtico y de moda: cafés de especialidad, restaurantes creativos, ambiente local. Hostels desde 20 EUR, apartamentos desde 60 EUR."}, {"name": "Barrio del Carmen", "description": "El casco antiguo más animado, perfecto para tapas y vida nocturna. Desde 50-90 EUR/noche."}]',
  '[{"title": "Ciudad de las Artes y las Ciencias", "description": "El complejo arquitectónico de Santiago Calatrava: el museo de ciencias más espectacular de España, el oceanográfico más grande de Europa, el palau de les arts."}, {"title": "Mercado Central de Valencia", "description": "Uno de los mercados cubiertos más grandes de Europa (1928). 1.200 puestos de fruta, verdura, carnes y el mejor ambiente valenciano. Imprescindible por la mañana."}, {"title": "Barrio del Carmen y la Catedral", "description": "El corazón medieval de Valencia con el Miguelete, la catedral donde se venera el Santo Grial y las calles más fotogénicas."}, {"title": "La playa y el Puerto", "description": "La playa de la Malvarrosa y el puerto olímpico a solo 15 min en bicicleta del centro — una de las mejores playas urbanas del Mediterráneo."}]',
  'La paella valenciana original (con pollo, conejo, judía verde y garrofón) se elabora los domingos en los restaurantes de Ruzafa y alrededores. El all i pebre (anguila con ajo y pimentón), los buñuelos de calabaza con chocolate, la horchata con fartons y las ostras del Perellonet completan el repertorio. El mercado central para comprar fruta de huerta inigualable.',
  'Valencia es muy segura para viajeros. En la playa y zonas turísticas, cuida pertenencias. El Barrio del Carmen es animado hasta tarde — ambiente estudiantil y local.',
  'España pertenece al Espacio Schengen. Ciudadanos UE con DNI. Mayoría de países occidentales sin visado 90 días. Moneda: Euro.',
  ARRAY['Si vas en Fallas (1-19 marzo) reserva alojamiento con 6 meses de antelación', 'La paella auténtica valenciana solo lleva pollo, conejo y verduras — sin mariscos', 'Valenbisi (bicicleta pública) es la mejor forma de moverse — cógela desde el hotel', 'El mercado central es mejor de 8h a 13h — los sábados tiene más ambiente pero más gente'],
  ARRAY['Gastronomía', 'Playa', 'Cultura', 'Ciudad'],
  ARRAY['food', 'beach', 'festive', 'mediterranean', 'modern'],
  ARRAY['mediterranean', 'sunny', 'warm'],
  ARRAY['March', 'April', 'May', 'September', 'October', 'November'],
  50, 100, 200, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'bilbao', 'Bilbao', 'España', 'Europa', 'city',
  '{"lat": 43.2630, "lng": -2.9350}',
  'La ciudad que el Guggenheim transformó en capital cultural del Cantábrico',
  'Bilbao, capital de Bizkaia, es uno de los ejemplos más citados en urbanismo mundial: una ciudad industrial decrépita que se reinventó gracias al Guggenheim (1997) y se convirtió en referente cultural europeo. Pero Bilbao es mucho más que el titanio de Gehry: el Casco Viejo con sus Siete Calles, la mejor cultura de pintxos del mundo, el Mercado de la Ribera y una identidad vasca rotunda que impregna cada rincón.',
  'Todo el año es visitable aunque el mejor tiempo es mayo-octubre (18-25°C). El País Vasco tiene fama de lluvioso — el verde de los montes lo demuestra. La Semana Grande (agosto) es el festival más multitudinario. Navidad tiene ambiente especial.',
  'El aeropuerto de Bilbao (BIO) con vuelos directos europeos. AVE desde Madrid (4h30). Autobús desde San Sebastián (1h) y el tranvía costero (Euskotren). Dentro de la ciudad: Metro (Foster), tranvía y a pie para el centro.',
  '[{"name": "Casco Viejo (Zazpikaleak)", "description": "Las Siete Calles históricas con pintxos bars y ambiente local insuperable. Hostels desde 20 EUR, hoteles boutique desde 70-100 EUR."}, {"name": "Abando / Ensanche", "description": "El ensanche burgués con el Museo Guggenheim. Hoteles de diseño y hoteles de cadena. Desde 80-150 EUR/noche."}]',
  '[{"title": "Museo Guggenheim Bilbao", "description": "Frank Gehry creó en 1997 el edificio más influyente de finales del siglo XX. La colección permanente y las exposiciones temporales son de primer nivel mundial."}, {"title": "Casco Viejo y las Siete Calles", "description": "El casco histórico medieval con el Mercado de la Ribera (el mayor mercado cubierto de Europa), la Catedral de Santiago y el ambiente más bilbaíno."}, {"title": "La Alhóndiga (Azkuna Zentroa)", "description": "El antiguo almacén de vinos reconvertido por Philippe Starck en centro cultural con piscina de fondo transparente y exposiciones."}, {"title": "San Juan de Gaztelugatxe", "description": "A 30 km, el islote con la ermita más fotogénica del Cantábrico. Conocido como Rocadragón en Juego de Tronos — llega temprano para evitar colas."}]',
  'Bilbao tiene los mejores pintxos del mundo: en el Casco Viejo cada bar es una obra de arte culinaria. El Gilda (anchoa, guindilla y aceituna), el txangurro (buey de mar), el bacalao al pil-pil y los pintxos creativos del Ensanche. La txakoli (vino blanco espumoso vasco) es el maridaje perfecto. Come tarde — el vermú de los sábados empieza a las 12h.',
  'Bilbao es muy segura para viajeros. Cuidado con el tráfico en el Casco Viejo (calles estrechas). El ambiente de pintxos es muy local — respeta los horarios vascos (pintxos de 19h a 21h).',
  'España, Espacio Schengen. Ciudadanos UE con DNI. Mayoría de países occidentales sin visado 90 días. Moneda: Euro.',
  ARRAY['Los pintxos se comen de pie en el bar con txakoli — pide el vino vertiéndolo desde alto', 'La ruta de pintxos del Casco Viejo: cada bar tiene su especialidad — prueba 1-2 en cada uno', 'El Guggenheim tiene entrada gratuita el primer martes de mes (excepto julio y agosto)', 'Alquila una bicicleta para llegar al mar en Getxo por el paseo de la ría'],
  ARRAY['Gastronomía', 'Cultura', 'Ciudad'],
  ARRAY['food', 'culture', 'pintxos', 'design', 'basque'],
  ARRAY['oceanic', 'mild', 'rainy'],
  ARRAY['May', 'June', 'July', 'August', 'September'],
  50, 100, 200, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'san-sebastian', 'San Sebastián', 'España', 'Europa', 'city',
  '{"lat": 43.3183, "lng": -1.9812}',
  'La ciudad más bella del Cantábrico con la mayor concentración de estrellas Michelin del mundo',
  'San Sebastián (Donostia en euskera), con apenas 190.000 habitantes, es una ciudad que parece diseñada para la felicidad: una bahía de La Concha considerada una de las más bellas del mundo, un Casco Antiguo donde cada barra acumula pintxos de alta cocina, y la mayor densidad de estrellas Michelin por metro cuadrado del planeta. La elegancia belle époque, el sur de Francia a 20 km y una identidad vasca apasionada la convierten en un destino único.',
  'Julio-agosto es la temporada alta (Festival de Jazz, temporada de playa — Bahía perfecta). Mayo-junio y septiembre son ideales: menos gente y el mismo esplendor. El Festival Internacional de Cine (septiembre) es imperdible. El invierno es lluvioso pero con los mejores pintxos sin espera.',
  'El aeropuerto de Bilbao (BIO, 1h en bus) es la opción principal. El tren desde Madrid (5h30 AVE parcial) o Barcelona (5h). Desde Biarritz/Bayona (Francia) en bus 1h. Dentro de la ciudad: todo el centro a pie; buses para las playas de Zurriola y Ondarreta.',
  '[{"name": "Parte Vieja (Casco Antiguo)", "description": "El barrio de los pintxos con las mejores barras del país. Hostels desde 25 EUR, apartamentos desde 80 EUR."}, {"name": "Centro / La Concha", "description": "El barrio burgués frente a la bahía. Hoteles belle époque y modernos. Desde 100-200 EUR/noche."}]',
  '[{"title": "Bahía de La Concha", "description": "Considerada una de las diez playas más bellas de Europa, la bahía perfectamente encuadrada entre el Monte Igueldo y el Monte Urgull es el alma de la ciudad."}, {"title": "Parte Vieja — ruta de pintxos", "description": "Las calles del Casco Antiguo concentran la mayor densidad de bares de pintxos del mundo. Bar La Cepa, Bar Txepetxa (anchoas), Bar Martínez... cada uno con su especialidad."}, {"title": "Monte Urgull", "description": "El monte que cierra la bahía por el norte con el castillo de la Mota y la estatua del Sagrado Corazón. Vistas inigualables sobre La Concha."}, {"title": "Acuario de San Sebastián", "description": "Uno de los mejores acuarios del norte de España, con el túnel submarino y la sección de flora y fauna atlántica como principales atracciones."}]',
  'San Sebastián compite con Tokio por la mayor concentración de estrellas Michelin: Arzak (3 estrellas, desde 1960), Akelarre, Mugaritz... pero los mejores pintxos están en la Parte Vieja desde 2-3 EUR/pieza. La txangurro, el bacalao, el foie, las anchoas del Cantábrico. El vino local: txakoli donostiarra. Cenar tarde (21h) como los locales.',
  'San Sebastián es muy segura. En temporada alta la Parte Vieja se llena — cuida pertenencias en zonas muy concurridas. El ambiente es festivo pero tranquilo.',
  'España, Espacio Schengen. Ciudadanos UE con DNI. Mayoría de países occidentales sin visado 90 días. Moneda: Euro.',
  ARRAY['La ruta de pintxos de la Parte Vieja: Bar Txepetxa para anchoas, Bar La Cepa para jamón, Bar Bergara para creaciones', 'La playa de La Concha está llena en agosto — ve a Zurriola (surfistas) para más espacio', 'Subir al Monte Urgull a pie (30 min) para la mejor vista de la bahía', 'Reservar con meses de antelación para los restaurantes Michelin'],
  ARRAY['Gastronomía', 'Playa', 'Cultura'],
  ARRAY['food', 'beach', 'elegant', 'pintxos', 'michelin'],
  ARRAY['oceanic', 'mild'],
  ARRAY['May', 'June', 'July', 'August', 'September'],
  60, 120, 250, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'salzburgo', 'Salzburgo', 'Austria', 'Europa', 'city',
  '{"lat": 47.8095, "lng": 13.0550}',
  'La ciudad de Mozart, los Alpes y La Novicia Rebelde',
  'Salzburgo, ciudad de 155.000 habitantes al pie de los Alpes austriacos en la frontera con Alemania, es una de las ciudades barrocas más perfectas de Europa. Cuna de Wolfgang Amadeus Mozart (1756), escenario de La Novicia Rebelde y capital del estado del mismo nombre, Salzburgo combina un casco histórico UNESCO de rara belleza con la inmediatez de los Alpes nevados, el lago Königssee y la región del Salzkammergut.',
  'Verano (junio-agosto): Festival de Salzburgo, la cumbre del mundo de la música clásica. Diciembre: mercados navideños de los más hermosos de Europa. Primavera y otoño son ideales para visitar sin multitudes. El invierno (fuera de Navidad) ofrece precios muy bajos.',
  'El aeropuerto de Salzburgo (SZG) con vuelos directos europeos. Tren desde Viena (2,5h), Múnich (1,5h) y Zúrich (4h). El centro histórico es compacto y perfecto para recorrer a pie.',
  '[{"name": "Altstadt (Ciudad Vieja, izquierda del Salzach)", "description": "La joya barroca UNESCO. B&Bs y hoteles históricos desde 70-100 EUR, temporada alta mucho más."}, {"name": "Nonntal / Riedenburg", "description": "Barrios residenciales tranquilos a 10-15 min del centro. Precios más razonables, desde 60-90 EUR."}]',
  '[{"title": "Festung Hohensalzburg", "description": "La fortaleza del siglo XI que domina la ciudad desde el Festungsberg. Una de las fortalezas medievales mejor conservadas de Europa. Sube en funicular."}, {"title": "Getreidegasse y la casa natal de Mozart", "description": "La calle más fotogénica de Salzburgo con sus letreros de hierro forjado. El número 9 es la casa donde nació Mozart en 1756 — hoy museo."}, {"title": "Mirabell y sus jardines", "description": "El palacio barroco con los jardines donde se rodó parte de La Novicia Rebelde. Las rosas, las esculturas y los Alpes al fondo: la postal perfecta."}, {"title": "Lago Königssee (excursión)", "description": "A 25 km en Alemania (Berchtesgaden), el lago de montaña más puro de los Alpes accesible en barco eléctrico. Una de las excursiones más bellas de Europa central."}]',
  'La cocina salzburguesa es sólida y sustanciosa: el Wiener Schnitzel de ternera, el Tafelspitz (buey hervido con rábano picante), las Salzburger Nockerl (suflé de vainilla para dos personas), el Mozartkugel (bombón de mazapán y chocolate) y la cerveza local en los Biergärten. Los cafés vieneses tienen sucursales en Salzburgo.',
  'Salzburgo es una de las ciudades más seguras de Europa. En temporada alta del festival los precios se disparan. Reserva alojamiento con meses de antelación para el Festival de Salzburgo (julio-agosto).',
  'Austria pertenece al Espacio Schengen. Ciudadanos UE con DNI. Mayoría de países occidentales sin visado 90 días. Moneda: Euro.',
  ARRAY['El Festival de Salzburgo (julio-agosto) dobla o triplica los precios del alojamiento — reserva con 6 meses de antelación o ve en otra época', 'La Salzburg Card (24/48/72h) incluye transporte y entrada a museos — vale la pena', 'Los mercados navideños de la Domplatz son los más bellos de Austria (y de los más bellos del mundo)', 'El lago Königssee se puede visitar en excursión de medio día en coche o bus'],
  ARRAY['Cultura', 'Naturaleza', 'Historia'],
  ARRAY['baroque', 'music', 'alps', 'christmas', 'elegant'],
  ARRAY['alpine', 'continental'],
  ARRAY['June', 'July', 'August', 'December'],
  60, 120, 250, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'luxemburgo', 'Luxemburgo', 'Luxemburgo', 'Europa', 'city',
  '{"lat": 49.6117, "lng": 6.1319}',
  'El pequeño gran país europeo: cañones, fortalezas y el corazón financiero del continente',
  'Luxemburgo, capital del Gran Ducado del mismo nombre, sorprende a todos los que esperan una ciudad aburrida de funcionarios europeos: el Casco Histórico UNESCO es un laberinto de cañones, puentes y fortalezas colgando sobre ríos. El Pétrusse y el Alzette cortan la ciudad en niveles unidos por ascensores panorámicos y puentes viaductos que roban el aliento. Una de las ciudades más ricas del mundo con comida multiétnica excelente.',
  'Mayo a septiembre es ideal: temperaturas agradables (18-25°C) y todas las terrazas al aire libre. Diciembre es mágico por los mercados navideños en la Place d''Armes. Enero-febrero es frío y tranquilo — muy económico fuera de la temporada de congresos europeos.',
  'El aeropuerto de Luxemburgo (LUX) con vuelos directos europeos. Tren desde Bruselas (3h), Frankfurt (3h) y París (2h10 TGV). El transporte público es gratuito en todo Luxemburgo desde 2020.',
  '[{"name": "Ciudad Vieja (Vieille Ville)", "description": "El corazón histórico UNESCO con los mejores restaurantes y hoteles boutique. Desde 100-150 EUR/noche."}, {"name": "Gare / Hollerich", "description": "Zona de la estación, más económica y multicultural. Buenas conexiones. Desde 60-90 EUR/noche."}]',
  '[{"title": "Casemates du Bock", "description": "El laberinto de túneles y galerías subterráneas excavados en la roca por sucesivas potencias militares desde el siglo XVII. 23 km de galerías para explorar."}, {"title": "Corniche (Balcón de Europa)", "description": "El paseo que recorre el borde del acantilado con vistas sobre los valles del Alzette y el Pétrusse — considerado el balcón más bello de Europa."}, {"title": "Vianden (excursión)", "description": "A 40 km, el pueblo más bonito de Luxemburgo con su castillo medieval de cuento en lo alto del acantilado sobre el río Our."}, {"title": "MUDAM (Museo de Arte Moderno)", "description": "En el recinto de los Fort Thüngen, este museo de Ieoh Ming Pei mezcla lo histórico y lo contemporáneo con colecciones internacionales."}]',
  'La cocina luxemburguesa mezcla influencias francesas, alemanas y belgas: el judd mat gaardebounen (cuello de cerdo ahumado con habas), el gromperekichelcher (tortitas de patata), el Riesling luxemburgués y la Bofferding (cerveza nacional). La Place d''Armes tiene terrazas con cocina de todo el mundo. Los precios son los más altos de Europa central.',
  'Luxemburgo es una de las ciudades más seguras del mundo. Los precios son elevados — el alojamiento y los restaurantes doblan la media europea.',
  'Luxemburgo pertenece al Espacio Schengen. Ciudadanos UE con DNI. Mayoría de países occidentales sin visado 90 días. Moneda: Euro.',
  ARRAY['El transporte público (bus, tren) es completamente gratuito en todo el país desde 2020', 'Las Casemates du Bock solo abren de marzo a octubre — comprueba antes de ir', 'Vianden merece una excursión de medio día: el castillo y la teleférica sobre el río', 'Los restaurantes de la Place d''Armes son más caros — el barrio de la Gare tiene mejores precios'],
  ARRAY['Cultura', 'Historia', 'Ciudad'],
  ARRAY['history', 'gorges', 'fortifications', 'europe', 'compact'],
  ARRAY['continental', 'temperate'],
  ARRAY['May', 'June', 'July', 'August', 'September'],
  70, 140, 280, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'andorra-la-vella', 'Andorra la Vella', 'Andorra', 'Europa', 'city',
  '{"lat": 42.5063, "lng": 1.5218}',
  'La capital más alta de Europa entre picos pirenaicos y compras libres de impuestos',
  'Andorra la Vella, a 1.023 metros de altitud en el corazón de los Pirineos, es la capital más alta de Europa y la del único estado independiente pirenaico. País de apenas 77.000 habitantes entre España y Francia, Andorra es famosa por sus compras libres de impuestos (tabaco, alcohol, perfumes, electrónica), su esquí de calidad y su spa termal. Pequeña pero sorprendente, especialmente en invierno.',
  'Invierno (diciembre-marzo) para esquí en Grandvalira (el mayor dominio esquiable de los Pirineos). Verano (junio-agosto) para senderismo y la Vuelta Ciclista. Todo el año para compras. Semana Santa es temporada alta de compras.',
  'No tiene aeropuerto propio. Desde Barcelona: bus directo (3h) o coche por el Túnel del Cadí. Desde Toulouse: bus 3h. El principado se recorre a pie en el centro de Andorra la Vella o en coche/bus para las parroquias.',
  '[{"name": "Andorra la Vella centro", "description": "Hoteles en la capital con fácil acceso a las compras y la vida nocturna. Desde 50-100 EUR/noche."}, {"name": "Pas de la Casa / Grandvalira", "description": "Al pie de las pistas de esquí. Imprescindible en temporada de nieve. Desde 70-150 EUR/noche."}]',
  '[{"title": "Compras libres de impuestos", "description": "Alcohol, tabaco, perfumes, electrónica y moda con precios muy por debajo del resto de Europa. El Pas de la Case y la av. Meritxell son las zonas principales."}, {"title": "Caldea Spa Termal", "description": "El complejo termal más grande del sur de Europa con 6.000 m² de aguas termales a 3.000 metros de altitud. Un lujo imprescindible en invierno."}, {"title": "Grandvalira Ski Resort", "description": "El mayor dominio esquiable de los Pirineos con más de 200 km de pistas para todos los niveles. Accesible desde Andorra la Vella en 30 min."}, {"title": "Casa de la Vall", "description": "El parlamento histórico de Andorra (siglo XVI), uno de los edificios más antiguos del principado. Visita guiada imprescindible."}]',
  'La gastronomía andorrana mezcla la cocina catalana y la francesa con platos de montaña: el trinxat (col y patata con tocino), el escudella de montaña, el confit de pato y los embutidos artesanales. Los restaurantes de la av. Meritxell son accesibles. Alcohol y tabaco a precios mínimos de Europa.',
  'Andorra es extremadamente segura. El principal reto es el tráfico en la única carretera principal — evita festivos y fines de semana en temporada de compras.',
  'Andorra no pertenece a la UE pero sí al Espacio Schengen de facto — el acceso es libre con DNI o pasaporte europeo. Para ciudadanos extracomunitarios, el acceso depende del visado Schengen en vigor. Sin moneda propia — usa el Euro.',
  ARRAY['Los precios del tabaco y el alcohol son los más bajos de Europa — compra el límite permitido', 'Caldea es más económico los días de semana y se llena mucho los fines de semana en invierno', 'El trámite aduanero al salir de Andorra hacia España puede haber cola — calcula tiempo', 'El senderismo en verano por el GRP (Gran Recorrido Pirenaico) pasa por Andorra'],
  ARRAY['Aventura', 'Compras', 'Naturaleza'],
  ARRAY['mountains', 'skiing', 'shopping', 'pyrenees'],
  ARRAY['alpine', 'continental'],
  ARRAY['December', 'January', 'February', 'March', 'July', 'August'],
  50, 100, 200, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'monaco', 'Mónaco', 'Mónaco', 'Europa', 'city',
  '{"lat": 43.7384, "lng": 7.4246}',
  'El estado más pequeño del mundo (después del Vaticano) donde todo es lujo y Fórmula 1',
  'Mónaco, el principado de 2 km² entre la Riviera francesa y el mar Mediterráneo, es el segundo estado independiente más pequeño del mundo y el más denso. Capital es la ciudad de Mónaco (Monte-Carlo es el barrio). Con los coches más caros del mundo circulando por sus estrechas calles y el casino más famoso del planeta, Mónaco es el destino más exclusivo de Europa. Pero visitarlo gratis (como turista sin casino) es perfectamente posible.',
  'Todo el año es visitable con clima mediterráneo perfecto. El Gran Premio de Mónaco (mayo) es el evento más exclusivo — los precios se multiplican por 10. Verano (junio-septiembre) es caluroso y lleno de yates. El Rallye de Mónaco (enero-febrero) es más accesible.',
  'No tiene aeropuerto: el más cercano es Niza (NCE, 30 km). Helicóptero desde Niza (7 min, 150 EUR). Tren desde Niza (25 min, 4 EUR) o Menton. El principado se recorre a pie aunque hay varios ascensores públicos gratuitos para salvar el desnivel.',
  '[{"name": "Mónaco-Ville (La Roche)", "description": "La ciudad vieja en la roca con el Palacio y la Catedral. Hoteles de lujo desde 200-500 EUR/noche."}, {"name": "Monte-Carlo", "description": "El barrio del Casino. Los grandes hoteles de lujo (Hôtel de Paris, Hermitage). Desde 300-1000 EUR/noche."}]',
  '[{"title": "Casino de Monte-Carlo", "description": "El casino más famoso del mundo (1863) con su arquitectura Belle Époque. Entrada libre al vestíbulo (sin jugar). La plaza del casino al atardecer es inigualable."}, {"title": "Palacio del Príncipe", "description": "La residencia oficial del Príncipe Alberto II. La guardia cambia cada día a las 11:55h. Visitas guiadas en verano."}, {"title": "Jardines Exóticos de Mónaco", "description": "Colgados en el acantilado con 7.000 especies de suculentas y cactus y vistas panorámicas sobre el Mediterráneo."}, {"title": "Musée Océanographique de Monaco", "description": "Fundado por el Príncipe Alberto I en 1910, uno de los mejores acuarios y museos oceanográficos del mundo con el Mediterráneo como telón."}]',
  'Los restaurantes de Mónaco son inevitablemente caros. Para comer bien sin arruinarse: el Marché de la Condamine (el mercado municipal) con comida local a precios razonables, los restaurantes del paseo Fontveille y los bares de tapas del barrio de La Condamine. La socca (torta de garbanzos) de Niza está a 20 min en tren.',
  'Mónaco es uno de los países más seguros del mundo con una ratio de policía por habitante altísima. El mayor riesgo es el impacto en el bolsillo.',
  'Mónaco no pertenece a la UE ni al Schengen formalmente pero tiene frontera abierta con Francia. Los ciudadanos de la UE entran con DNI. El resto con los mismos requisitos que para Francia (Schengen). Moneda: Euro.',
  ARRAY['Los ascensores públicos gratuitos (hay 5) evitan las cuestas empinadas — úsalos siempre', 'El tren Niza-Mónaco (4 EUR) pasa por viaductos sobre el mar — paisaje espectacular', 'El vestíbulo del Casino es gratis — no necesitas jugar para ver la arquitectura', 'El Musée Océanographique vale la pena aunque parezca caro (20 EUR) — es excepcional'],
  ARRAY['Lujo', 'Ciudad', 'Cultura'],
  ARRAY['luxury', 'glamour', 'racing', 'sea', 'exclusive'],
  ARRAY['mediterranean', 'sunny', 'warm'],
  ARRAY['March', 'April', 'May', 'June', 'September', 'October'],
  100, 200, 600, 8
) ON CONFLICT (slug) DO NOTHING;


-- AMÉRICA (11 nuevas ciudades)

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'cusco', 'Cusco', 'Perú', 'América', 'city',
  '{"lat": -13.5320, "lng": -71.9675}',
  'El ombligo del mundo inca, puerta al Machu Picchu y la capital arqueológica de América',
  'Cusco, a 3.400 metros de altitud en los Andes peruanos, fue la capital del Imperio Inca y hoy es el epicentro del turismo arqueológico de toda América del Sur. Su Plaza de Armas, rodeada de iglesias barrocas construidas sobre templos incas, es una de las más impresionantes del continente. Desde aquí parten los caminos a Machu Picchu, el Valle Sagrado y los circuitos por la Ruta Inca — la razón por la que millones de viajeros cruzan el Atlántico cada año.',
  'Mayo a octubre es la temporada seca (la mejor para el Camino Inca y Machu Picchu). Junio-agosto es la alta temporada — reserva el tren y las entradas a Machu Picchu con 3 meses de antelación. Noviembre a abril es temporada húmeda con lluvias frecuentes pero precios bajos y menos gente.',
  'El aeropuerto de Alejandro Velasco Astete (CUZ) con vuelos desde Lima (1h10), Arequipa y otras ciudades peruanas. No hay trenes directos a Cusco — el acceso es aéreo o bus. Desde Puno (lacustre) en bus 6h. Dentro de la ciudad: taxis y a pie en el centro histórico.',
  '[{"name": "Centro Histórico / San Blas", "description": "El barrio más auténtico de artistas e independientes con calles de adoquín inca. Hostels desde 10 USD, hoteles boutique desde 60-100 USD."}, {"name": "San Pedro / Plaza de Armas", "description": "El corazón turístico cerca del Mercado de San Pedro. Hoteles desde 50-150 USD/noche."}]',
  '[{"title": "Machu Picchu", "description": "La ciudadela inca del siglo XV en lo alto del Huayna Picchu es la maravilla de las maravillas de América. Reserva entradas con 3 meses de antelación en machupicchu.gob.pe."}, {"title": "Qorikancha (Templo del Sol)", "description": "El templo más sagrado del Imperio Inca, recubierto de láminas de oro. Los conquistadores españoles construyeron el Convento de Santo Domingo sobre sus cimientos."}, {"title": "Sacsayhuamán", "description": "La fortaleza inca sobre Cusco con muros ciclópeos cuyas piedras de hasta 130 toneladas encajan perfectamente sin mortero — un enigma de ingeniería."}, {"title": "Valle Sagrado de los Incas", "description": "El valle entre Pisac y Ollantaytambo es una sucesión de ruinas incas, mercados andinos y paisajes sobrecogedores. Excursión de un día desde Cusco."}]',
  'La gastronomía cusqueña fusiona tradición andina con influencias coloniales: el ceviche, el lomo saltado, el cuy (conejillo de indias asado — plato ritual), la chicha morada (refresco de maíz morado) y la chicha de jora (cerveza de maíz fermentado). El Mercado de San Pedro tiene los mejores desayunos por 2-3 USD.',
  'Cusco tiene zonas de mayor y menor seguridad. El casco histórico y las zonas turísticas son relativamente seguros de día. Por la noche ve con compañía especialmente en zonas alejadas del centro. El robo de pertenencias es el mayor riesgo.',
  'Los ciudadanos de la UE, EEUU, Canadá, Australia y la mayoría de países entran a Perú sin visado hasta 90-183 días. Solo necesitas pasaporte con 6 meses de vigencia y billete de salida. No hay tasa de entrada a Perú.',
  ARRAY['El mal de altura (soroche) afecta a la mayoría — descansa el primer día y bebe mucha agua', 'Las entradas a Machu Picchu se agotan — reserva en machupicchu.gob.pe con meses de antelación', 'El tren Vistadome de PeruRail al Aguas Calientes es caro pero espectacular — hay opciones más económicas', 'El barrio de San Blas tiene mejores restaurantes y precios más honestos que la Plaza de Armas'],
  ARRAY['Historia', 'Aventura', 'Naturaleza'],
  ARRAY['inca', 'history', 'mountains', 'archaeology', 'ancient'],
  ARRAY['highland', 'dry-wet-seasons'],
  ARRAY['May', 'June', 'July', 'August', 'September', 'October'],
  20, 60, 150, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'salvador-de-bahia', 'Salvador de Bahía', 'Brasil', 'América', 'city',
  '{"lat": -12.9714, "lng": -38.5014}',
  'La primera capital de Brasil, cuna del candomblé, el axé y la capoeira',
  'Salvador, capital del estado de Bahía, es la ciudad más africana fuera de África: el 80% de sus 3 millones de habitantes tienen raíces africanas, lo que da forma a una cultura musical, gastronómica y espiritual sin igual en Brasil. El Pelourinho (centro histórico UNESCO con sus casas de colores) concentra una energía vibrante mientras que las playas del sur de la ciudad, la capoeira en cada esquina y el candomblé dan a Salvador una identidad irrepetible.',
  'Junio-septiembre es la temporada más fresca y seca (25-30°C) — ideal para el Pelourinho. El Carnaval de Salvador (enero-febrero) es el más masivo del mundo (más de 2 millones de personas), una experiencia extrema. Diciembre-marzo es temporada húmeda pero calurosa y festiva.',
  'El aeropuerto de Deputado Luís Eduardo Magalhães (SSA) con vuelos desde São Paulo (2h), Río (2h) y conexiones internacionales. Dentro de la ciudad: taxi, Uber y buses. El funicular conecta la Ciudad Alta con la Ciudad Baja.',
  '[{"name": "Pelourinho (Ciudad Alta)", "description": "El corazón histórico y cultural, el más fotogénico. Pousadas y hostels desde 30-50 BRL/noche."}, {"name": "Barra / Ondina", "description": "Zona de playa con hoteles de clase media. La mejor mezcla entre turismo, playa y vida local. Desde 150-300 BRL/noche."}]',
  '[{"title": "Pelourinho", "description": "El centro histórico colonial con sus casas de colores intensos declarado UNESCO. Los martes hay Olodum (batería callejera) desde las 19h — entrada libre."}, {"title": "Capoeira en acción", "description": "La capoeira nació en Bahía. La Fundação Mestre Bimba (Pelourinho) y el Forte de Santo Antônio tienen ruedas de capoeira abiertas."}, {"title": "Igrejas barrocas del Pelourinho", "description": "La Catedral Basílica, la Iglesia de São Francisco con sus interiores de oro puro y la Igreja do Bonfim (llena de fitas de colores) son las joyas barrocas de Salvador."}, {"title": "Playas de Salvador", "description": "Porto da Barra (la más céntrica), Itapuã y Flamengo son las mejores playas del norte. El sur, con Itacaré y la Costa do Descobrimento, a 2-5h."}]',
  'La cocina baiana es la más sabrosa de Brasil: el acarajé (buñuelo de alubia relleno de vatapá y camarón, vendido en las baianas de blanco), la moqueca baiana (guiso de pescado con aceite de dendê y coco), el caruru de camarão y el bobó de camarão. Todo lleva aceite de palma (dendê) y leche de coco. Barato y extraordinario.',
  'Salvador tiene zonas con alta criminalidad. El Pelourinho y las playas populares son relativamente seguros de día con presencia policial. Evita zonas alejadas del centro por la noche, no muestres teléfono o cámara en la calle y usa Uber en lugar de taxis de la calle.',
  'Brasil es libre de visado para ciudadanos de la UE, EEUU, Canadá, Australia y la mayoría de países. Pasaporte con 6 meses de vigencia. Los ciudadanos de algunos países necesitan visado previo — verifica tu caso.',
  ARRAY['El acarajé solo sabe auténtico comprado a las baianas vestidas de blanco en la calle', 'Los martes en el Pelourinho con el Olodum son gratuitos y una experiencia musical incomparable', 'Guarda el teléfono en el bolsillo delantero en todo momento en el Pelourinho', 'La fita do Bonfim (pulsera de la iglesia del Señor do Bonfim) da buena suerte — llévate una'],
  ARRAY['Cultura', 'Playa', 'Aventura'],
  ARRAY['afro-culture', 'music', 'food', 'carnival', 'colorful'],
  ARRAY['tropical', 'hot', 'humid'],
  ARRAY['June', 'July', 'August', 'September'],
  30, 70, 150, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'valparaiso', 'Valparaíso', 'Chile', 'América', 'city',
  '{"lat": -33.0472, "lng": -71.6127}',
  'La ciudad de los cerros pintados, los ascensores y el alma bohemia del Pacífico',
  'Valparaíso, a 120 km al oeste de Santiago, es la ciudad más pintoresca y caótica de Chile: 42 cerros cubiertos de casas de colores conectados por funiculares históricos (ascensores), murales callejeros, escalinatas sinuosas y una energía portuaria y bohemia sin igual. Declarada Patrimonio UNESCO, "Valpo" tiene una personalidad propia muy alejada del orden capitalino y una escena artística que la ha convertido en el epicentro cultural chileno.',
  'Noviembre a marzo (verano austral) es ideal: 20-28°C y cielos despejados. El año nuevo de Valparaíso (31 diciembre) con fuegos artificiales sobre la bahía es uno de los espectáculos más impresionantes de América del Sur. Julio-agosto es frío y brumoso pero muy fotogénico.',
  'Desde Santiago en bus Turbus o Pullman (1h30, desde 4.000 CLP). El aeropuerto más cercano es el de Santiago (SCL, 2h). El centro de Valparaíso se recorre a pie y en ascensores históricos.',
  '[{"name": "Cerro Alegre / Cerro Concepción", "description": "Los dos cerros más fotogénicos y turísticos, llenos de hostels boutique, cafeterías y galerías. Desde 15.000-40.000 CLP/noche."}, {"name": "El Plan (Ciudad Baja)", "description": "El centro histórico portuario y comercial, más económico pero menos pintoresco. Desde 10.000-25.000 CLP/noche."}]',
  '[{"title": "Cerro Alegre y sus murales", "description": "El cerro más bohemio de Valparaíso, con cada pared convertida en mural de arte callejero. La calle Templeman y la plaza Bismarck son los puntos álgidos."}, {"title": "Ascensores históricos", "description": "Los 16 ascensores (funiculares) históricos que conectan el Plan con los cerros son Monumento Nacional. El Ascensor Concepción (1883) es el más antiguo en uso."}, {"title": "La Sebastiana — Casa de Neruda", "description": "Una de las tres casas de Pablo Neruda en Chile, con su arquitectura irregular y coleccionista. Vista soberbia sobre la bahía."}, {"title": "Recorrido por El Plan", "description": "La ciudad baja con el Palacio Baburizza (Museo de Bellas Artes), la Bolsa de Comercio, el Muelle Prat y el Puerto — la escena del Valparaíso trabajador."}]',
  'La gastronomía de Valparaíso tiene el mejor mariscos frescos de Chile: el chupe de jaiba (gratinado de cangrejo), los picorocos (percebes gigantes chilenos), el congrio frito con papas fritas, las empanadas de mariscos y el pisco sour. Los restaurantes de la subida Templeman y la plaza Bismarck tienen buena relación calidad-precio.',
  'Valparaíso tiene barrios seguros (Cerro Alegre, Cerro Concepción) y otros que no lo son tanto. Queda cerca del plan nocturno — los cerros alejados de la zona turística son peligrosos por la noche. Usa Uber o taxis de radio para moverte después del anochecer.',
  'Chile es libre de visado para ciudadanos de la UE, EEUU, Canadá, Australia y la mayoría de países. Pasaporte con 6 meses de vigencia. Reciprocidad turística activa con algunos países — verifica tu caso.',
  ARRAY['Los ascensores históricos cuestan 100-300 CLP — el más pintoresco es el Concepción', 'Cerro Alegre se puede recorrer en 2-3h pero merece pasar la noche para vivir el ambiente nocturno', 'El año nuevo de Valparaíso (31 diciembre) reserva alojamiento con 6 meses de antelación', 'La Casa Neruda (La Sebastiana) cierra los lunes — comprueba horarios'],
  ARRAY['Cultura', 'Aventura', 'Mochilero'],
  ARRAY['bohemian', 'street-art', 'port', 'colorful', 'hills'],
  ARRAY['mediterranean', 'mild', 'foggy'],
  ARRAY['November', 'December', 'January', 'February', 'March'],
  25, 60, 130, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'arequipa', 'Arequipa', 'Perú', 'América', 'city',
  '{"lat": -16.4090, "lng": -71.5375}',
  'La Ciudad Blanca del volcán El Misti y la puerta al Cañón del Colca',
  'Arequipa, la "Ciudad Blanca" de Perú, debe su apodo al sillar, la roca volcánica blanca con la que están construidos sus magníficos edificios coloniales del siglo XVI. A 2.325 metros de altitud y dominada por el volcán El Misti (5.822 m), Arequipa es la segunda ciudad del Perú y la puerta de entrada al Cañón del Colca — el segundo más profundo del mundo y hogar del cóndor andino.',
  'Mayo a noviembre es la estación seca — perfecta para ver cóndores en el Colca y excursiones a los volcanes. Diciembre a abril es temporada húmeda pero los precios bajan y hay menos turistas. Arequipa tiene 300 días de sol al año.',
  'El aeropuerto de Rodríguez Ballón (AQP) con vuelos desde Lima (1h30) y Cusco (30 min). Bus nocturno de lujo desde Lima (10-12h) o Cusco (6h). Dentro de la ciudad: taxis y mototaxis — a pie en el centro histórico.',
  '[{"name": "Centro Histórico (alrededor de la Plaza de Armas)", "description": "El corazón colonial con los mejores hostels y restaurantes. Hostels desde 8-15 USD, hoteles boutique en conventos desde 50-100 USD."}, {"name": "Yanahuara", "description": "El barrio con la mejor vista del El Misti y ambiente más local. Pensiones y B&Bs desde 20-50 USD."}]',
  '[{"title": "Convento de Santa Catalina", "description": "Un convento del siglo XVI que es una ciudad dentro de la ciudad: calles, plazas, celdas de colores azules y rojos. Uno de los monumentos más impresionantes de Perú."}, {"title": "Cañón del Colca y los cóndores", "description": "A 3-4h de Arequipa, el cañón más dramático de Perú donde los cóndores surcan las corrientes térmicas cada mañana desde las 9h en la Cruz del Cóndor."}, {"title": "Plaza de Armas y la Catedral", "description": "Una de las plazas más hermosas del Perú colonial, dominada por la catedral de sillar blanco con el volcán El Misti al fondo — la postal perfecta."}, {"title": "Volcán El Misti (ascenso)", "description": "El volcán de 5.822 m que domina Arequipa es escalable sin equipo especial con guía. Salida a medianoche para amanecer en la cima — experiencia inolvidable."}]',
  'La gastronomía arequipeña es una de las más reconocidas de Perú: el rocoto relleno (pimiento picante con carne y queso gratinado), el chupe de camarones (sopa cremosa de camarones del río), el adobo arequipeño (cerdo marinado) y el queso helado (helado de canela y coco). Los picanterías — restaurantes tradicionales — son la auténtica experiencia local.',
  'Arequipa es una de las ciudades más seguras del Perú. El centro histórico tiene presencia policial constante. Evita zonas periféricas por la noche. El Cañón del Colca es seguro con operadores de tours establecidos.',
  'Los ciudadanos de la UE, EEUU, Canadá, Australia y la mayoría de países entran a Perú sin visado. Pasaporte con 6 meses de vigencia.',
  ARRAY['El Convento de Santa Catalina es enorme — calcula 2-3h para verlo bien', 'Para ver cóndores en el Colca: llega antes de las 9h a la Cruz del Cóndor', 'La altitud de Arequipa (2.325m) es más llevadera que Cusco — buena aclimatación previa', 'Los tours al Colca de 2 días incluyen pernoctación en Chivay — más recomendable que el tour de 1 día'],
  ARRAY['Historia', 'Naturaleza', 'Aventura'],
  ARRAY['volcanoes', 'colonial', 'condors', 'canyon', 'white-city'],
  ARRAY['highland', 'dry', 'sunny'],
  ARRAY['May', 'June', 'July', 'August', 'September', 'October'],
  20, 50, 120, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'oaxaca', 'Oaxaca', 'México', 'América', 'city',
  '{"lat": 17.0732, "lng": -96.7266}',
  'La capital gastronómica de México: mole, mezcal y Monte Albán',
  'Oaxaca, capital del estado del mismo nombre en el sur de México, es la meca de la gastronomía mexicana y uno de los destinos culturales más ricos del país. Sus calles coloniales de colores vivos, la majestuosa Catedral de Santo Domingo, los mercados de artesanía zapoteca, las ruinas de Monte Albán y su extraordinaria tradición culinaria con los siete moles oaxaqueños la convierten en una ciudad que ningún viajero serio debería perderse.',
  'Octubre a mayo es la temporada seca y más agradable. Las Fiestas de la Guelaguetza (julio) son el festival folclórico más importante de México — espectáculo visual único. El Día de Muertos en Oaxaca (31 oct - 2 nov) es uno de los más auténticos y emocionantes del país. Diciembre a enero es muy popular.',
  'El aeropuerto de Xoxocotlán (OAX) con vuelos desde Ciudad de México (1h), Cancún y algunas ciudades de EE.UU. Bus de lujo ADO desde CDMX (6-7h). El centro histórico es compacto y perfecto para recorrer a pie.',
  '[{"name": "Centro Histórico", "description": "Las calles coloniales de Oaxaca alrededor del Zócalo y Santo Domingo. Hostels desde 15 USD, hoteles boutique desde 80-150 USD."}, {"name": "Jalatlaco", "description": "El barrio más bonito de Oaxaca: callejones empedrados, casas de colores, más tranquilo y fotogénico que el centro. Desde 60-120 USD/noche."}]',
  '[{"title": "Convento de Santo Domingo y jardín Etnobotánico", "description": "La iglesia más imponente de Oaxaca con su interior dorado y el jardín botánico de plantas zapotecas únicas — visita guiada imprescindible."}, {"title": "Monte Albán", "description": "La ciudad zapoteca del siglo V a.C. a 8 km de Oaxaca con pirámides, observatorio y vistas panorámicas sobre el Valle de Oaxaca. Una de las ruinas más impresionantes de México."}, {"title": "Mercado Benito Juárez y 20 de Noviembre", "description": "Los dos mercados del centro: el primero para artesanía y el segundo para comer — las mejores tlayudas, tasajo y chapulines (saltamontes tostados) de Oaxaca."}, {"title": "Mezcal tour en los valles", "description": "El mezcal artesanal oaxaqueño es el mejor del mundo. Los palenques de los Valles Centrales (Matatlan, Tlacolula) ofrecen tours de producción y catas."}]',
  'Oaxaca es la capital gastronómica de México: los siete moles (negro, rojo, coloradito, amarillo, verde, chichilo, manchamanteles), la tlayuda (tortilla gigante con frijoles y tasajo), la memela, el tejate, los chapulines, el queso Oaxaca y los tamales oaxaqueños. El mezcal artesanal (no el industrial) con gusano de maguey es la bebida inevitable.',
  'Oaxaca es relativamente segura para los viajeros. El centro histórico y las zonas turísticas tienen presencia policial. Evita salir solo de noche por barrios poco iluminados. Usa Uber o sitios de taxi confiables.',
  'México es libre de visado para ciudadanos de la UE, EEUU, Canadá, Australia y la mayoría de países. El FMM (Forma Migratoria Múltiple) se gestiona online o en el aeropuerto. Permite estancias de hasta 180 días.',
  ARRAY['El Día de Muertos en Oaxaca (1-2 noviembre) es el más auténtico — reserva alojamiento con meses de antelación', 'Los mercados son mucho más baratos y auténticos que los restaurantes del Zócalo', 'El mezcal artesanal sin aditivos (busca "100% agave" en la etiqueta) no da resaca — el industrial sí', 'Monte Albán abre a las 8h — ve temprano para evitar el calor y las multitudes'],
  ARRAY['Gastronomía', 'Cultura', 'Historia'],
  ARRAY['food', 'culture', 'craft', 'mezcal', 'indigenous'],
  ARRAY['highland', 'dry', 'mild'],
  ARRAY['October', 'November', 'December', 'January', 'February', 'March'],
  25, 70, 150, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'puerto-vallarta', 'Puerto Vallarta', 'México', 'América', 'city',
  '{"lat": 20.6534, "lng": -105.2253}',
  'El paraíso del Pacífico mexicano donde la sierra madre cae al mar turquesa',
  'Puerto Vallarta, en la Bahía de Banderas del estado de Jalisco, es el destino de playa más auténtico del Pacífico mexicano. A diferencia de Cancún, PV —como la llaman los locales— tiene un malecón con escultura, un Casco Antiguo con iglesia colonial, barrios creativos llenos de arte y una gastronomía de mariscos extraordinaria. Los delfines, las ballenas jorobadas (en invierno) y los arrecifes de coral hacen el resto.',
  'Noviembre a abril es la temporada seca perfecta: 25-30°C, sin lluvia. Las ballenas jorobadas visitan la bahía de diciembre a marzo. Mayo a octubre es temporada de lluvias (calurosa) con precios muy bajos y el mar en calma perfecta. Evita septiembre (huracanes posibles).',
  'El aeropuerto de Puerto Vallarta (PVR) con vuelos directos desde muchas ciudades de EE.UU., Canadá y algunas desde Europa. Bus nocturno desde Ciudad de México (12h) y Guadalajara (5h). Las zonas turísticas principales están a lo largo del Malecón y en la Zona Hotelera.',
  '[{"name": "Zona Romántica / Casco Antiguo", "description": "El barrio más auténtico y gay-friendly al sur del río Cuale. Hostels y B&Bs desde 20-50 USD, hoteles boutique desde 80-150 USD."}, {"name": "Zona Hotelera Norte / Marina", "description": "Resorts all-inclusive y hoteles de playa. Desde 100-300 USD/noche todo incluido."}]',
  '[{"title": "Malecón y Centro Histórico", "description": "El paseo marítimo de 8 km con esculturas de bronce, restaurantes y vida nocturna junto a la Iglesia de Nuestra Señora de Guadalupe con su corona tejida."}, {"title": "Playa Los Muertos y Playa de Oro", "description": "Las playas más animadas de PV: sombrillas, cerveza, beach clubs y el muelle de la Zona Romántica. Perfectas para el primer día."}, {"title": "Avistamiento de ballenas jorobadas", "description": "De diciembre a marzo la Bahía de Banderas es el santuario de reproducción de la ballena jorobada. Tours desde el muelle — una experiencia de vida."}, {"title": "Pueblos Mágicos cercanos (Sayulita)", "description": "A 40 km, el pueblo surf de Sayulita con sus calles empedradas, restaurantes de mariscos, tiendas de artesanía y ambiente bohemio — perfecto para un día de playa alternativa."}]',
  'La gastronomía vallartense brilla con los mariscos del Pacífico: el aguachile (ceviche picante de camarón), el pescado zarandeado (a la leña), los mariscos en salsa de ajo, los tacos de marlín y las garnachas locales. La Zona Romántica tiene los mejores restaurantes. El mezcal jaliscense y la cerveza Corona bien fría sobre el malecón.',
  'Puerto Vallarta es una de las ciudades más seguras de México para el turismo. Las zonas hoteleras y el malecón tienen fuerte presencia policial. Evita zonas alejadas por la noche.',
  'México libre de visado para ciudadanos de la UE, EEUU, Canadá, Australia y la mayoría de países. FMM en el aeropuerto o en línea.',
  ARRAY['Diciembre-marzo: reserva el tour de ballenas con 2-3 días de antelación durante el fin de semana', 'La Zona Romántica tiene mejor ambiente local y precios más honestos que la Zona Hotelera', 'El barco a Yelapa (pueblito sin carretera) es una excursión de día inigualable', 'Los restaurantes del malecón son una trampa turística — camina una calle hacia el interior'],
  ARRAY['Playa', 'Gastronomía', 'Naturaleza'],
  ARRAY['beach', 'whales', 'sunset', 'tropical', 'authentic'],
  ARRAY['tropical', 'dry-season', 'warm'],
  ARRAY['November', 'December', 'January', 'February', 'March', 'April'],
  35, 80, 200, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'nassau', 'Nassau', 'Bahamas', 'América', 'city',
  '{"lat": 25.0480, "lng": -77.3554}',
  'El paraíso caribeño de las aguas turquesas más azules del mundo',
  'Nassau, capital de las Bahamas en la isla de New Providence, es la puerta de entrada a uno de los archipiélagos más hermosos del Caribe. Conocida principalmente por los cruceros y los resorts de lujo, Nassau tiene también calles coloridas de época colonial británica, mercados de artesanía, el mejor snorkel sobre corales vivos y unas aguas de un turquesa imposible que han convertido las Bahamas en sinónimo de paraíso tropical.',
  'Diciembre a abril es la temporada perfecta: 24-28°C, sin lluvia, las aguas más claras. Junio-noviembre es temporada de huracanes — evita especialmente agosto-octubre. El precio del alojamiento baja considerablemente en temporada baja.',
  'El Aeropuerto Internacional Lynden Pindling (NAS) con vuelos directos desde Miami (50 min), Nueva York (3h) y conexiones desde Europa. También hay ferries desde Miami. Dentro de Nassau: taxis y Jitney (bus local muy económico).',
  '[{"name": "Nassau Downtown / Bay Street", "description": "El centro histórico con los mejores hoteles económicos y de gama media. Cerca del Puerto de Cruceros. Desde 80-150 USD/noche."}, {"name": "Cable Beach / Paradise Island", "description": "Las playas más famosas con el complejo Atlantis. Resorts desde 200-500 USD/noche."}]',
  '[{"title": "Paradise Beach y Cable Beach", "description": "Las playas más impresionantes con el turquesa más profundo del Atlántico. El Atlantis Beach en Paradise Island tiene acceso público."}, {"title": "Fort Charlotte", "description": "La fortaleza colonial británica del siglo XVIII sobre la colina con vistas panorámicas sobre Nassau Harbour y el mar. Visita gratuita."}, {"title": "Mercado de artesanía de Straw Market", "description": "El mercado más animado de Nassau con artesanía bahameña: trenzados de paja, ropa, música y el ambiente más local de la ciudad."}, {"title": "Snorkel y buceo en arrecifes", "description": "Los arrecifes de coral de las Bahamas están entre los más vírgenes del Caribe. Tours desde Nassau a Stuart Cove y Love Beach con visibilidad de 30+ metros."}]',
  'La cocina bahameña gira en torno al caracol (conch): el conch salad (marisco crudo con limón, cebolla y pimienta — el ceviche caribeño), el cracked conch (frito), el conch fritters (buñuelos) y la sopa de caracol. El pan de Johnnycake, el pigeon peas and rice y el guayberry rum completan la mesa bahameña. Comida callejera en el puerto a precios muy razonables.',
  'Nassau tiene zonas seguras y otras que no lo son tanto. Las áreas turísticas (Bay Street, Cable Beach, Paradise Island) son seguras de día. El centro histórico de noche puede ser inseguro para turistas solos. Nunca lleves joyas ostentosas.',
  'Los ciudadanos de la UE, EE.UU., Canadá, Australia y muchos otros países entran sin visado hasta 90 días. Pasaporte con 6 meses de vigencia requerido. No hay visado de turista — solo presentas pasaporte y ticket de vuelta.',
  ARRAY['Los mejores arrecifes no están al lado de Nassau — reserva un tour de snorkel o buceo al día siguiente', 'El Jitney (bus local) cuesta 1.25 USD y va a todas partes — mucho más económico que el taxi', 'Exumas (con los cerdos nadadores) se puede visitar en vuelo chárter de 30 min desde Nassau', 'El conch salad fresco del mercado de Arawak Cay es la mejor comida de las Bahamas'],
  ARRAY['Playa', 'Lujo', 'Naturaleza'],
  ARRAY['beach', 'turquoise', 'caribbean', 'tropical', 'snorkel'],
  ARRAY['tropical', 'warm', 'dry-season'],
  ARRAY['December', 'January', 'February', 'March', 'April'],
  80, 180, 400, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'kingston', 'Kingston', 'Jamaica', 'América', 'city',
  '{"lat": 17.9970, "lng": -76.7936}',
  'La capital del reggae, Bob Marley y la cocina jamaicana más explosiva del Caribe',
  'Kingston, capital de Jamaica en la costa sur de la isla, es la ciudad más grande del Caribe de habla inglesa y el corazón cultural jamaicano. El barrio de Trenchtown —donde nació el reggae y se crió Bob Marley— el Museo Bob Marley, el Blue Mountain Coffee y una gastronomía caribeña sin igual hacen de Kingston un destino para quienes buscan la Jamaica auténtica, lejos de los resorts de Montego Bay.',
  'Diciembre a abril es la temporada seca perfecta (25-30°C). Junio-noviembre es temporada de huracanes — evita septiembre-octubre. El reggae Sunsplash (verano) es el festival más importante. El Carnaval de Kingston (Bacchanal, abril) atrae cada año más visitantes.',
  'El Aeropuerto Internacional Norman Manley (KIN) con vuelos desde Miami (1h30), Nueva York (4h) y conexiones caribeñas. También el aeropuerto de Montego Bay (MBJ, 2h en bus) con más vuelos europeos. Dentro de Kingston: taxis y el JUTC (bus público) — Uber disponible.',
  '[{"name": "New Kingston", "description": "El distrito financiero moderno y el más seguro para turistas. Hoteles internacionales de cadena desde 100-200 USD/noche."}, {"name": "Devon House área", "description": "Zona histórica y comercial con el Devon House, casas coloniales y los mejores helados de Jamaica. Desde 80-150 USD/noche."}]',
  '[{"title": "Museo Bob Marley (56 Hope Road)", "description": "La casa donde vivió y grabó Bob Marley convertida en el museo más visitado de Jamaica. La tour guiada transmite la energía del One Love."}, {"title": "Devon House", "description": "La mansión del primer millonario negro jamaicano (1881) con sus jardines coloniales y la famosa heladería I-Scream — los mejores helados del Caribe."}, {"title": "Barrio de Trenchtown", "description": "El barrio donde nació el reggae y se crió Bob Marley — con guía local para seguridad. El Culture Yard Museum es el inicio de todo."}, {"title": "Blue Mountains Day Trip", "description": "A 45 min de Kingston, el pico más alto de Jamaica (2.256 m) tiene el mejor café del mundo y senderismo con vistas sobre la isla y Cuba en días claros."}]',
  'La cocina jamaicana es una explosión de sabores: el jerk chicken (pollo marinado en pimienta scotch bonnet y especias, a la leña), el ackee and saltfish (desayuno nacional: fruta ackee con bacalao salado), el curry goat, el patty (empanada de carne picante), el rice and peas y el festival (pan dulce frito). El rum jamaicano (Appleton Estate) y el Red Stripe son las bebidas oficiales.',
  'Kingston tiene zonas con criminalidad alta. Las zonas turísticas (New Kingston, Devon House, Half Way Tree) son seguras. Evita Trenchtown y zonas de guetos sin guía local. No camines solo por la noche fuera de New Kingston.',
  'Los ciudadanos de la UE, EE.UU., Canadá, Australia y muchos otros países entran sin visado hasta 90 días. Pasaporte con 6 meses de vigencia. No hay requisitos adicionales para turistas.',
  ARRAY['El Museo Bob Marley es imprescindible — el tour guiado vale más que la entrada solo', 'El jerk chicken más auténtico está en los puestos de carretera — no en los restaurantes turísticos', 'Las Blue Mountains se pueden visitar en tour organizado desde Kingston o Ocho Ríos', 'Usa Uber para desplazarte — los taxis sin taxímetro pueden cobrar precios arbitrarios'],
  ARRAY['Cultura', 'Música', 'Naturaleza'],
  ARRAY['reggae', 'music', 'caribbean', 'culture', 'authentic'],
  ARRAY['tropical', 'warm', 'humid'],
  ARRAY['December', 'January', 'February', 'March', 'April'],
  50, 100, 200, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'cali', 'Cali', 'Colombia', 'América', 'city',
  '{"lat": 3.4516, "lng": -76.5320}',
  'La capital mundial de la salsa, donde Colombia baila sin parar',
  'Cali, la tercera ciudad de Colombia con 2,5 millones de habitantes, es la ciudad más caliente y bailable del país: capital mundial de la salsa caleña, un estilo diferente, más suave y sensual que el cubano o el puertorriqueño. Las salsotecas del barrio de Juanchito, la gastronomía valluna, el Valle del Cauca y las comunidades afrocolombianas que dan la identidad musical a la ciudad hacen de Cali un destino para viajeros que buscan Colombia más allá de Cartagena y Medellín.',
  'Diciembre a marzo y junio-agosto son la temporada seca. La Feria de Cali (del 25 al 30 de diciembre) es el festival de salsa más importante del mundo — la ciudad explota de ritmo. El Petronio Álvarez (agosto) celebra la cultura del Pacífico con música y gastronomía afrocolombiana.',
  'El aeropuerto Alfonso Bonilla Aragón (CLO) con vuelos desde Bogotá (1h), Medellín (1h) y conexiones internacionales. Dentro de la ciudad: MIO (bus articulado), Uber y taxi con taxímetro.',
  '[{"name": "El Peñón / Granada", "description": "El barrio más seguro y moderno para turistas con excelente oferta gastronómica. Hostels desde 30.000 COP, hoteles desde 100.000-200.000 COP."}, {"name": "San Antonio", "description": "El barrio bohemio sobre la colina con casas coloniales, cafeterías y murales. El más pintoresco. Desde 80.000-150.000 COP/noche."}]',
  '[{"title": "Aprender salsa caleña", "description": "Las academias de salsa de Cali (Son de Luz, Swing Latino) tienen clases para todos los niveles desde 30.000 COP/hora. Una noche en salsoteca después es obligatoria."}, {"title": "Juanchito — las mejores salsotecas", "description": "El barrio caleño de la salsa con la Topa Tolondra, la Tin Tin Deo y la mítica Zaperoco. Los fines de semana las pistas no paran de girar hasta el amanecer."}, {"title": "Cristo Rey y el Cerro de las Tres Cruces", "description": "Las dos cimas sobre Cali con vistas panorámicas del Valle del Cauca. El Cristo Rey (26 m) es visible desde toda la ciudad."}, {"title": "Zoológico de Cali", "description": "Uno de los mejores de Latinoamérica con fauna endémica del Valle del Cauca y del Chocó biogeográfico, incluyendo jaguares, caimanes y aves tropicales."}]',
  'La gastronomía valluna tiene sus propias especialidades: el sancocho de gallina, el champús (bebida de maíz con lulo y guanábana), la cholado (raspado con frutas tropicales), el pandebono (pan de yuca y queso) y el aborrajado (plátano maduro frito con queso). El lulada (bebida de lulo) es el refresco de Cali por excelencia.',
  'Cali tiene zonas con criminalidad variable. Los barrios del norte (El Peñón, Granada, Ciudad Jardín) son seguros para turistas. Evita el centro histórico por la noche y los barrios del sur (Aguablanca). Usa Uber en lugar de taxis de la calle.',
  'Colombia es libre de visado para ciudadanos de la UE, EE.UU., Canadá, Australia y muchos países. Pasaporte con 6 meses de vigencia. Entrada gratuita hasta 90 días.',
  ARRAY['Reserva clase de salsa caleña el primer día — la noche en la salsoteca tendrá más sentido', 'La Feria de Cali (25-30 diciembre) es la mejor época pero reserva con meses de antelación', 'El lulada y el champús son bebidas únicas de Cali — probarlas es obligatorio', 'Juanchito es seguro dentro de las salsotecas — no vayas caminando solo entre locales'],
  ARRAY['Cultura', 'Música', 'Gastronomía'],
  ARRAY['salsa', 'music', 'dancing', 'culture', 'afro-colombian'],
  ARRAY['tropical', 'warm', 'year-round'],
  ARRAY['December', 'January', 'February', 'June', 'July', 'August'],
  30, 70, 150, 8
) ON CONFLICT (slug) DO NOTHING;


-- ÁFRICA (10 nuevas ciudades)

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'fez', 'Fez', 'Marruecos', 'África', 'city',
  '{"lat": 34.0181, "lng": -5.0078}',
  'La medina más grande e intacta del mundo, donde el tiempo se detuvo en el siglo IX',
  'Fez, la ciudad más antigua del Magreb, tiene la distinción de albergar la medina (Fès el-Bali) más grande y mejor conservada del mundo islámico medieval, declarada Patrimonio UNESCO. Con 9.400 callejones y más de 150.000 artesanos trabajando con técnicas de hace 1.000 años, Fez es el lugar del mundo donde más fácil es sentirse transportado al Medievo. La universidad Al-Qarawiyyin, fundada en 859 d.C., es la más antigua del mundo en actividad continua.',
  'Primavera (marzo-mayo) y otoño (septiembre-noviembre) son ideales con temperaturas perfectas (18-26°C). El verano (junio-agosto) es abrasador (38-42°C) — solo para muy resistentes. El invierno es fresco y barato.',
  'El aeropuerto Fès-Saïss (FEZ) con vuelos directos desde muchas ciudades europeas (Ryanair, easyJet). Tren desde Casablanca (3h), Marrakech (7h) y Tánger (4h). La medina se recorre a pie — imposible para coches.',
  '[{"name": "Medina (Fès el-Bali)", "description": "Alojarse dentro de la medina en un riad es la experiencia más auténtica de Marruecos. Riads desde 30-100 EUR/noche, todo incluido desayuno."}, {"name": "Fès el-Jdid / Ville Nouvelle", "description": "La ciudad nueva francesa con hoteles más convencionales. Desde 40-80 EUR/noche."}]',
  '[{"title": "Curtidurías Chouara", "description": "Las tenerías medievales donde se tiñe el cuero a mano con las mismas técnicas del siglo XI — uno de los espectáculos visuales más impactantes del mundo. Acceso desde las terrazas de cuero de los riads."}, {"title": "Madrasa Bou Inania", "description": "La madraza islámica del siglo XIV con la más intrincada decoración de azulejos, madera de cedro tallada y estuco en todo el Magreb."}, {"title": "Universidad Al-Qarawiyyin", "description": "Fundada en 859 d.C. por Fatima al-Fihri, la universidad más antigua del mundo en funcionamiento continuo. La biblioteca tiene manuscritos de 1.200 años."}, {"title": "Zoco de herreros (Souk Nejjarine)", "description": "La plaza más hermosa de la medina con la fuente de mosaicos y el Museo del Madera — el corazón artesanal de Fez."}]',
  'La cocina de Fez es la más refinada de Marruecos: la pastela (hojaldre de paloma con almendras y azúcar — el plato más sofisticado del país), el mechoui (cordero asado lentamente), el cuscús del viernes, el harira (sopa de lentejas y garbanzos) y los dulces de almendra. El té de menta es la hospitalidad por excelencia.',
  'Fez en la medina es laberíntica y puede ser estresante para los visitantes. Los guías no oficiales son agresivos. Contrata siempre un guía oficial (certificado por el Ministerio de Turismo) para la primera visita. El riad te asignará uno de confianza.',
  'Los ciudadanos de la UE, EE.UU., Canadá, Australia y la mayoría de países entran a Marruecos sin visado hasta 90 días. Pasaporte con 6 meses de vigencia. Moneda: Dírham marroquí (MAD).',
  ARRAY['Alojarse en un riad dentro de la medina es la mejor inversión — te orienta y el desayuno marroquí vale la pena', 'La mejor vista de las curtidurías Chouara es desde las terrazas de cuero a las 10-11h — con luz de mañana', 'Lleva una ramita de menta para la nariz en las curtidurías — el olor es intenso', 'El mercado de especias (souk des épices) tiene los mejores precios si regateas con calma'],
  ARRAY['Cultura', 'Historia', 'Aventura'],
  ARRAY['medina', 'islamic', 'medieval', 'crafts', 'labyrinth'],
  ARRAY['mediterranean', 'continental', 'hot-summers'],
  ARRAY['March', 'April', 'May', 'September', 'October', 'November'],
  25, 60, 150, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'rabat', 'Rabat', 'Marruecos', 'África', 'city',
  '{"lat": 34.0209, "lng": -6.8416}',
  'La capital imperial más tranquila de Marruecos, con la Kasbah de los Udayas frente al Atlántico',
  'Rabat, capital de Marruecos desde 1912, es la ciudad imperial más tranquila y menos turística del país. A diferencia de Marrakech o Fez, Rabat ofrece al viajero la posibilidad de descubrir una medina auténtica sin el asedio de los guías agresivos, la magnífica Kasbah de los Udayas sobre el Atlántico, la Torre Hassan inacabada y un ambiente refinado de capital de embajadas. La ciudad perfecta para descubrir Marruecos con calma.',
  'Primavera (marzo-mayo) y otoño (septiembre-noviembre) son ideales: 18-25°C y agradable. El verano es cálido pero la brisa atlántica lo suaviza mucho más que el interior. El invierno (fresco y lluvioso) tiene menos turistas y precios muy bajos.',
  'El aeropuerto de Rabat-Salé (RBA) con vuelos directos desde Europa. Tren desde Casablanca (45 min) y Marrakech (5h). Tren de alta velocidad Al-Boraq a Tánger (1h20). El centro histórico se recorre a pie.',
  '[{"name": "Medina de Rabat", "description": "La medina más tranquila de Marruecos con riads auténticos. Riads desde 40-80 EUR/noche."}, {"name": "Agdal / Hassan", "description": "La zona moderna con hoteles de cadena y boutique. Desde 50-100 EUR/noche."}]',
  '[{"title": "Kasbah de los Udayas", "description": "La fortaleza del siglo XII sobre el Atlántico con sus calles encaladas de azul y blanco. Los jardines y el Café Maure con vistas al Atlántico y al río Bou Regreg."}, {"title": "Torre Hassan", "description": "El minarete inacabado del siglo XII que iba a ser el más alto del mundo. Las 200 columnas del patio y el Mausoleo Mohammed V al lado son impresionantes."}, {"title": "Chellah — Necropólis romana y jardín", "description": "Las ruinas romanas de Sala Colonia con cigüeñas y gatos entre las ruinas y un jardín exuberante. El lugar más tranquilo y evocador de Rabat."}, {"title": "Medina de Rabat", "description": "Una medina sin la presión de guías agresivos: Avenue Mohammed V, el zoco de la Semara, la joyería judía y el barrio de los alfareros."}]',
  'La cocina rabatí sigue la tradición marroquí con el cuscús del viernes como plato central. El bastilla de marisco (especialidad costera), el pescado a la chermoula, los msemen (crepes marroquíes) con miel de argan del desayuno y el té verde con hierbabuena. El mercado de Bab el-Had tiene los mejores precios.',
  'Rabat es la ciudad más segura de Marruecos para el viajero. Al ser capital administrativa, la presencia policial es alta. Sin el asedio de guías agresivos de otras ciudades.',
  'Sin visado hasta 90 días para ciudadanos de la UE, EE.UU. y mayoría de países occidentales. Pasaporte con 6 meses de vigencia. Moneda: Dírham marroquí (MAD).',
  ARRAY['La Kasbah de los Udayas al atardecer es la experiencia más fotogénica de Rabat', 'El tren Al-Boraq de alta velocidad a Tánger es excepcional — una experiencia única en África', 'Rabat-Salé tiene una bicisharing (BRT) excelente para moverse por la ciudad nueva', 'El Café Maure en la Kasbah tiene las mejores vistas y el té más caro vale la pena'],
  ARRAY['Cultura', 'Historia', 'Ciudad'],
  ARRAY['imperial', 'atlantic', 'quiet', 'authentic', 'kasbah'],
  ARRAY['mediterranean', 'atlantic', 'mild'],
  ARRAY['March', 'April', 'May', 'September', 'October', 'November'],
  25, 60, 140, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'mombasa', 'Mombasa', 'Kenia', 'África', 'city',
  '{"lat": -4.0435, "lng": 39.6682}',
  'La ciudad swahili del Índico, las especias y las playas blancas de la costa keniana',
  'Mombasa, la segunda ciudad de Kenia y principal puerto del África Oriental, es la ciudad más antigua y culturalmente diversa del país: árabe, swahili, indio y africano se mezclan en el Casco Histórico con su Fort Jesús portugués, sus calles de especias y su mezquita más antigua. Al norte y al sur de la ciudad se abren algunas de las playas más hermosas del Océano Índico, con arrecifes de coral perfectamente conservados.',
  'Junio a octubre (temporada seca) es el mejor momento para las playas del norte (Watamu, Malindi) y la costa. Enero-febrero también es seco y caluroso. Evita marzo-mayo (largo rains — lluvias intensas). Las playas están menos concurridas que en diciembre-enero.',
  'El aeropuerto de Moi (MBA) con vuelos desde Nairobi (1h), Zanzíbar y conexiones. Desde Nairobi el tren SGR (Standard Gauge Railway) moderno llega en 4h30 — una experiencia en sí misma. Ferry desde Likoni (imprescindible para las playas del sur).',
  '[{"name": "Casco Histórico / Fort Jesús area", "description": "El corazón swahili de la ciudad con el fuerte y los mejores restaurantes de marisco. Hostels desde 20 USD, hoteles desde 60-100 USD."}, {"name": "Playas Norte (Nyali / Bamburi / Shanzu)", "description": "Hoteles de playa de todos los rangos. Desde 50-200 USD/noche dependiendo del resort."}]',
  '[{"title": "Fort Jesús (UNESCO)", "description": "La fortaleza portuguesa del siglo XVI es el monumento histórico más importante de la costa swahili. Las luchas entre portugueses, árabes omaníes y británicos forjaron la historia del Índico."}, {"title": "Casco Histórico de Mombasa (Old Town)", "description": "Las calles estrechas con puertas de madera talladas, balcones de hierro forjado y mezquitas centenarias — la arquitectura swahili-árabe más auténtica de Kenia."}, {"title": "Playas de Diani (sur)", "description": "Las mejores playas de Kenia: arena blanca de talco y océano turquesa con arrecife de coral integro. A 30 km al sur del ferry de Likoni."}, {"title": "Haller Park y Mamba Village", "description": "El crocodrilo park y el haller park de tortugas y jirafas son perfectos para familias. El hipopótamo más famoso de Mombasa vive en el Haller Park."}]',
  'La cocina swahili-keniana de la costa mezcla sabores árabes e indios: el pilau (arroz con especias y carne), el biryani de marisco, el samaki wa kupaka (pescado en salsa de coco), el maandazi (pan dulce frito) y los mariscos frescos del Índico. El mkate wa ufuta (pan de sésamo) y el chai masala son el desayuno costero.',
  'Mombasa es más segura que Nairobi pero hay que tener precaución en el centro histórico por la noche. Las playas turísticas son seguras. Nunca vayas a playas solitarias solo/a. El ferry de Likoni tiene algún carterista — vigila pertenencias.',
  'Los ciudadanos de la UE, EE.UU., Canadá, Australia y la mayoría de países necesitan visado para Kenia. El E-Visa es la opción más práctica (50 USD, se tramita online en evisa.go.ke). Pasaporte con 6 meses de vigencia.',
  ARRAY['El tren SGR Nairobi-Mombasa es una experiencia — viaja en clase superior y disfruta el paisaje masái', 'El ferry de Likoni para las playas del sur es gratuito pero hay que esperar — ve temprano', 'Fort Jesús es mejor con guía — la historia de los portugueses y omaníes es extraordinaria', 'Las playas de Diani son mejores que las del norte — merece el viaje extra'],
  ARRAY['Playa', 'Cultura', 'Historia'],
  ARRAY['swahili', 'beach', 'coral', 'ocean', 'historic'],
  ARRAY['tropical', 'hot', 'humid'],
  ARRAY['June', 'July', 'August', 'September', 'October', 'January', 'February'],
  30, 70, 180, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'antananarivo', 'Antananarivo', 'Madagascar', 'África', 'city',
  '{"lat": -18.9249, "lng": 47.5185}',
  'La capital de la isla más extraña del planeta, donde el 80% de la fauna es endémica',
  'Antananarivo ("Tana"), capital de Madagascar, es la puerta de entrada a la isla más biodiversa y extraña del mundo: separada de África hace 88 millones de años, Madagascar evolucionó en completo aislamiento creando el 80% de su fauna y flora únicos en el planeta (lémures, fosas, baobabs). La capital, sobre doce colinas, mezcla arquitectura colonial francesa, mercados bulliciosos y una calidez malgache que sorprende a todos.',
  'Mayo a octubre (temporada seca) es ideal para explorar Madagascar. Noviembre a abril es temporada de ciclones y lluvias intensas. Agosto y septiembre son los meses más frescos y agradables.',
  'El Aeropuerto Internacional de Ivato (TNR) con vuelos directos desde París (11h), Reunión, Mauricio, Nairobi y Johannesburgo. Dentro de la ciudad: taxis y taxi-brousse (furgonetas compartidas).',
  '[{"name": "Haute-Ville (Ciudad Alta)", "description": "La zona histórica sobre la colina central con el Palacio de la Reina. Hoteles boutique y pensiones desde 25-60 EUR/noche."}, {"name": "Analakely / Basse-Ville", "description": "El centro comercial y el Gran Mercado. Hoteles de gama media desde 40-80 EUR/noche."}]',
  '[{"title": "Rova (Palacio de la Reina)", "description": "La ciudadela real del siglo XVII sobre la colina más alta de Tana con vistas panorámicas sobre la ciudad y el lago Anosy."}, {"title": "Mercado Zoma (los viernes)", "description": "El mercado más grande de Madagascar que ocupa el centro de la ciudad cada viernes. Artesanía, especias, animales y el ambiente más malgache posible."}, {"title": "Museo del Lemur", "description": "En el barrio de Tsimbazaza, el zoo y museo con la mejor colección de lémures del mundo — algunas especies en serio peligro de extinción."}, {"title": "Excursión a Andasibe-Mantadia", "description": "A 140 km, el parque nacional más visitado de Madagascar con el Indri (el lémur más grande, de voz retumbante) y senderismo en selva primaria."}]',
  'La cocina malgache mezcla influencias africanas, asiáticas y francesas: el romazava (estofado de zebu con hojas de anamamy), el vary amin''anana (arroz con verduras), el koba (pasta de cacahuete envuelta en hoja de banana) y los pasteles coloniales franceses que sobreviven en los salones de té de Tana. La vanila malgache es la mejor del mundo.',
  'Antananarivo tiene zonas seguras e inseguras. Evita el centro histórico por la noche y la zona del mercado Zoma. Usa taxis de hotel o de aplicación. No muestres cámara cara en la calle.',
  'Los ciudadanos de la mayoría de países necesitan visado para Madagascar. Se puede tramitar visado a la llegada (90.000 MGA/~20 USD para 30 días) o en la embajada antes de salir. Consulta los requisitos para tu país.',
  ARRAY['Madagascar no es un destino fácil — las carreteras son muy malas fuera de Tana, planifica con margen', 'El Indri de Andasibe canta al amanecer — impresionante — ve en tour organizado desde Tana', 'La vanila malgache que venden en los mercados es la mejor del mundo — lleva varios tarros', 'Los taxis en Tana deben tener taxímetro — acuerda siempre el precio antes de subir'],
  ARRAY['Naturaleza', 'Aventura', 'Cultura'],
  ARRAY['lemurs', 'unique', 'biodiversity', 'colonial', 'exotic'],
  ARRAY['tropical', 'highland'],
  ARRAY['May', 'June', 'July', 'August', 'September', 'October'],
  20, 50, 120, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'abidjan', 'Abiyán', 'Costa de Marfil', 'África', 'city',
  '{"lat": 5.3599, "lng": -4.0083}',
  'La capital económica del África Occidental con la arquitectura más audaz del continente',
  'Abiyán (Abidjan), la capital económica de Costa de Marfil y la ciudad más grande del África Occidental francófona, es una metrópolis de 5 millones de habitantes que sorprende por su dinamismo económico, su arquitectura modernista de los años 70 y su vida cultural. El barrio de Le Plateau con sus rascacielos frente a la laguna, el Treichville con su mercado y vida nocturna, y el barrio de Cocody con sus embajadas y restaurantes dan a Abiyán una energía de ciudad global en África.',
  'Noviembre a marzo (temporada seca) es el mejor período con cielo despejado y temperatura de 28-32°C. Evita mayo-junio (las lluvias más intensas). Diciembre-enero tiene el ambiente más festivo.',
  'El aeropuerto Felix Houphouet-Boigny (ABJ) es el hub del África Occidental con vuelos directos desde París (7h), Bruselas, Casablanca, Addis Abeba y muchas ciudades africanas. Taxis y Uber dentro de la ciudad.',
  '[{"name": "Le Plateau (Centro Financiero)", "description": "Los rascacielos modernistas y los mejores hoteles internacionales. Desde 80-200 USD/noche."}, {"name": "Cocody", "description": "El barrio diplomático residencial con hoteles boutique y restaurantes de calidad. Desde 60-130 USD/noche."}]',
  '[{"title": "Barrio de Le Plateau y el skyline", "description": "Los rascacielos modernistas de los años 70 frente a la laguna Ébrié — una arquitectura africana única del período del boom del marfil y el cacao."}, {"title": "Mercado de Treichville", "description": "El mercado más animado y auténtico de Abiyán con telas wax, especias, frutas tropicales y el ambiente más local de la ciudad."}, {"title": "Musée des Civilisations de Côte d''Ivoire", "description": "El mejor museo de arte y cultura tradicional de Costa de Marfil con máscaras, estatuaria dan y senufo de las colecciones más importantes de África."}, {"title": "Basílica de Yamoussoukro (excursión)", "description": "A 250 km, la basílica más grande del mundo (más que San Pedro del Vaticano), construida por Houphouet-Boigny en su pueblo natal — un monumento al delirio de grandeza africano post-independencia."}]',
  'La cocina marfileña combina ingredientes de la selva con influencias libanesas y francesas: el attiéké (sémola de yuca fermentada), el kedjenou (pollo estofado en olla de barro), el fufu con sopa de cacahuete, el alloco (plátano frito) y el garba (atún con attiéké, el street food más popular). La bière Solibra y el bangui (vino de palma) son las bebidas locales.',
  'Abiyán ha mejorado mucho en seguridad desde la crisis política de 2010-2011. Las zonas de Cocody, Le Plateau y Marcory son seguras para turistas. Treichville y Abobo de noche con más precaución. Usa Uber que es abundante y seguro.',
  'Los ciudadanos de la mayoría de países necesitan visado para Costa de Marfil. El visado electrónico (e-visa) se puede tramitar online (civd.gouv.ci). También existe visado a la llegada para algunos países. Consulta los requisitos para tu país.',
  ARRAY['El e-visa de Costa de Marfil es fácil de tramitar online — hazlo con 2 semanas de antelación', 'Uber funciona muy bien en Abiyán y es mucho más seguro que los taxis de la calle', 'La Basílica de Yamoussoukro requiere un día completo de excursión — merece el viaje', 'La playa de Assinie (120 km) es la mejor playa accesible desde Abiyán'],
  ARRAY['Negocios', 'Cultura', 'Aventura'],
  ARRAY['business', 'modern', 'west-africa', 'colonial', 'dynamic'],
  ARRAY['tropical', 'hot', 'humid'],
  ARRAY['November', 'December', 'January', 'February', 'March'],
  40, 90, 200, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'harare', 'Harare', 'Zimbabue', 'África', 'city',
  '{"lat": -17.8252, "lng": 31.0335}',
  'La puerta a las Cataratas Victoria, las ruinas del Gran Zimbabue y el Parque Nacional de Hwange',
  'Harare, capital de Zimbabue, es una ciudad que sorprende por su ambiente tranquilo, sus jacarandas en flor (octubre-noviembre) y su gente extraordinariamente cálida. Tras décadas de crisis económica, Zimbabue está experimentando una recuperación y los viajeros que se aventuran descubren no solo un hub para las increíbles atracciones naturales del país (Cataratas Victoria, Hwange, Gran Zimbabue) sino también una escena cultural y culinaria genuinamente africana.',
  'Abril a octubre (temporada seca) es el mejor momento: perfecta para safaris y excursiones. Mayo-agosto es fresco y seco — ideal. Noviembre las jacarandas tiñen Harare de morado. Diciembre-marzo es el verano lluvioso.',
  'El aeropuerto de Robert Gabriel Mugabe (HRE) con vuelos desde Johannesburgo (2h), Nairobi, Addis Abeba, Dubái y algunas ciudades europeas. Autobús desde Johannesburgo (12-14h). Taxis dentro de la ciudad.',
  '[{"name": "Avondale / Borrowdale", "description": "Los barrios más seguros con restaurantes y alojamiento para expats y turistas. Hoteles boutique desde 60-120 USD/noche."}, {"name": "Centro de Harare", "description": "El centro de negocios con hoteles de cadena. Más activo. Desde 70-150 USD/noche."}]',
  '[{"title": "Galería Nacional de Zimbabue", "description": "Una de las mejores colecciones de arte contemporáneo africano del continente con la escultura en piedra shona — el movimiento artístico más importante nacido en África."}, {"title": "Mbare Musika Market", "description": "El mercado más grande y auténtico de Harare — frutas, verduras, artesanía y el bullicio más africano de la capital."}, {"title": "Domboshawa y las pinturas rupestres", "description": "A 30 km de Harare, las formaciones de granito con pinturas rupestres San de 5.000 años y vistas panorámicas sobre el plateau de Zimbabue."}, {"title": "Excursión al Gran Zimbabue", "description": "A 290 km, las ruinas de piedra más grandes del África subsahariana (siglos XI-XIV) y el mayor monumento precolonial del continente — que da nombre al país."}]',
  'La cocina zimbabuense tiene el sadza (polenta de maíz) como base de casi todas las comidas, acompañado de nyama (carne), rape (hojas de mostaza), matemba (pescado seco) o muriwo. El braai (barbacoa) es la actividad social más importante. La cerveza Castle Lager y el Tanganda Tea son los productos más exportados del país.',
  'Harare es relativamente segura en los barrios de expats (Borrowdale, Avondale). El centro puede ser más complicado con carteristas. Nunca muestres efectivo en público — la economía de efectivo es importante en Zimbabue.',
  'Los ciudadanos de la mayoría de países necesitan visado para Zimbabue. El Kaza Univisa (50 USD) permite entrada a Zimbabue y Zambia y es ideal para visitar las Cataratas Victoria. Visa on arrival disponible en el aeropuerto. Consulta los requisitos para tu país.',
  ARRAY['El Kaza Univisa (Zimbabue + Zambia) vale la pena si visitas las Cataratas Victoria', 'La escultura en piedra shona es el arte más auténtico de Zimbabue — compra directamente a los artistas', 'El USD es la moneda más aceptada actualmente — lleva billetes pequeños y medios', 'Las Cataratas Victoria se ven mejor en junio-agosto (caudal máximo desde el lado de Zimbabue)'],
  ARRAY['Naturaleza', 'Cultura', 'Aventura'],
  ARRAY['safari', 'victoria-falls', 'culture', 'africa', 'art'],
  ARRAY['subtropical', 'highland', 'dry-wet-seasons'],
  ARRAY['May', 'June', 'July', 'August', 'September', 'October'],
  30, 80, 180, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'luanda', 'Luanda', 'Angola', 'África', 'city',
  '{"lat": -8.8368, "lng": 13.2343}',
  'La capital del petróleo africano, donde el Atlántico se encuentra con la sabana lusófona',
  'Luanda, capital de Angola, fue durante una época la ciudad más cara del mundo para expatriados. Tras el fin de la guerra civil (2002) y el boom del petróleo, Luanda se transformó en una metrópolis caótica de 8 millones de habitantes frente al Atlántico, con barrios de luxe rodeados de musseques (barrios de chabolas). Para el viajero aventurero que se sale de los circuitos habituales, Angola ofrece una de las experiencias africanas más auténticas e inesperadas.',
  'Mayo a octubre (temporada seca, cacimbo) es el mejor período: nublado pero fresco (18-24°C) y sin lluvias. Noviembre-abril es caluroso y húmedo (28-35°C) con lluvias frecuentes. El tiempo en Luanda es sorprendentemente fresco para su latitud por la corriente de Benguela.',
  'El aeropuerto internacional 4 de Fevereiro (LAD) con vuelos desde Lisboa (8h), Johannesburgo, Addis Abeba, Nairobi, Dubai y algunas ciudades europeas. Dentro de la ciudad: táxis (los candongueiros, furgonetas compartidas) y Uber.',
  '[{"name": "Miramar / Alvalade", "description": "Los barrios más seguros para turistas con hoteles internacionales y restaurantes. Desde 150-300 USD/noche."}, {"name": "Ilha de Luanda", "description": "La lengua de tierra sobre el Atlántico con clubs de playa, restaurantes de mariscos y ambiente nocturno. Desde 100-200 USD/noche."}]',
  '[{"title": "Ilha de Luanda", "description": "La lengua de arena de 8 km sobre el Atlántico con la mejor playa urbana, restaurantes de mariscos y la vida nocturna más animada de Luanda."}, {"title": "Museo Nacional de Angola", "description": "La historia de Angola desde la época precolonial hasta la independencia en 1975, en un palacio colonial del siglo XVIII."}, {"title": "Mercado do Kinaxixi", "description": "El mercado más animado y auténtico de Luanda con artesanía angolana, comida callejera y el ambiente más genuino de la ciudad."}, {"title": "Fortaleza de São Miguel", "description": "La fortaleza portuguesa del siglo XVI sobre la bahía de Luanda, con las mejores vistas de la ciudad y la costa atlántica."}]',
  'La cocina angolana mezcla influencias portuguesas y africanas: el funje (polenta de mandioca) con calulu (guiso de pescado seco), el mufete (pescado a la brasa con feijoada), el muamba de galinha (pollo en salsa de palma y gindungo) y el arroz de coco. La cerveza Cuca, el vinho português y o ginja (licor de guinda) son los tragos clásicos.',
  'Luanda es una ciudad compleja para el viajero. La disparidad económica es extrema. Evita los musseques y las zonas de mercado por la noche. Usa Uber siempre. La infraestructura turística es limitada — es un destino para viajeros muy experimentados.',
  'Los ciudadanos de la mayoría de países necesitan visado para Angola. El visado se tramita en el consulado con antelación — NO existe visado a la llegada para la mayoría de nacionalidades. El proceso puede ser burocrático — empieza con al menos 1 mes de antelación.',
  ARRAY['Tramita el visado angolano con 4-6 semanas de antelación — es el mayor obstáculo del viaje', 'Uber funciona en Luanda y es esencial para moverse con seguridad', 'Los restaurantes de la Ilha de Luanda son caros pero los mariscos son excepcionales', 'Angola acepta el kwanza como moneda pero los USD son ampliamente aceptados en hoteles y resorts'],
  ARRAY['Aventura', 'Negocios', 'Cultura'],
  ARRAY['atlantic', 'lusophone', 'africa', 'petrol-city', 'emerging'],
  ARRAY['tropical', 'cool-current'],
  ARRAY['May', 'June', 'July', 'August', 'September', 'October'],
  60, 150, 350, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'libreville', 'Libreville', 'Gabón', 'África', 'city',
  '{"lat": 0.3901, "lng": 9.4544}',
  'La capital del Gabón verde, puerta a la selva tropical más vírgene de África Central',
  'Libreville, capital de Gabón en el ecuador africano, es la base para explorar uno de los países con mayor cobertura forestal del planeta: el 88% del territorio de Gabón es selva tropical virgen con gorilas, chimpancés, elefantes de bosque y ballenas jorobadas. La ciudad en sí es tranquila, con un Bord de Mer agradable frente al estuario del Gabon y una infraestructura para expatriados del petróleo que hace la vida relativamente cómoda.',
  'La temperatura es constante todo el año (26-32°C). Junio-septiembre es más fresco y seco — el mejor período para safaris y la selva. Las ballenas jorobadas visitan el Parque Nacional Loango de julio a septiembre.',
  'El aeropuerto internacional de Libreville León-Mba (LBV) con vuelos directos desde París (8h), Addis Abeba, Casablanca y ciudades africanas. Dentro de la ciudad: taxis (siempre acordar precio) y taxi-moto.',
  '[{"name": "Louis", "description": "El barrio más seguro para extranjeros con hoteles, restaurantes y servicios. Desde 80-200 USD/noche."}, {"name": "Bord de Mer", "description": "El paseo marítimo con hoteles frente al estuario. Ambiente más relajado. Desde 100-200 USD/noche."}]',
  '[{"title": "Marché du Mont-Bouet", "description": "El mercado más grande de Libreville con artesanía gabonesa, máscaras fang, tejidos y productos de la selva. El más auténtico de la ciudad."}, {"title": "Parque Nacional Lopé (excursión)", "description": "A 4h de Libreville, uno de los mejores parques de África Central con gorilas, mandril, elefantes y la sabana-selva más antigua del continente (UNESCO)."}, {"title": "Parque Nacional Loango (excursión)", "description": "\"El último edén\": la única playa del mundo donde elefantes, búfalos e hipopótamos conviven en la arena. Las ballenas jorobadas en verano."}, {"title": "Musée National des Arts et Traditions du Gabon", "description": "Las mejores colecciones de arte tradicional gabonés con las máscaras ceremoniales fang, pounou y kota — entre las más sofisticadas de África."}]',
  'La cocina gabonesa es discreta pero sabrosa: el poulet nyembwe (pollo en salsa de palma), el bâton de manioc (tapioca envuelta en hoja de banana), el porc-épic (puerco espín) y el saka-saka (hojas de yuca). Los restaurantes franceses de calidad son abundantes para los expats del petróleo. Los mariscos del estuario son frescos y deliciosos.',
  'Libreville es una de las capitales más seguras de África Central. Las zonas de Louis y el Bord de Mer son tranquilas. El mercado y los barrios populares de noche con más precaución.',
  'Los ciudadanos de la mayoría de países necesitan visado para Gabón. El visado electrónico (e-visa) se puede tramitar en e-visa.gouv.ga. Existe también visado a la llegada. Verifica los requisitos para tu país con antelación.',
  ARRAY['Gabón es caro por la industria petrolera — presupuesto mayor de lo habitual en África', 'El Parque de Lopé puede visitarse en train-bush desde Libreville (6h de viaje escénico)', 'Las máscaras tradicionales gabonesas son las más sofisticadas de África — llevan certificado CITES si son antiguas', 'El e-visa de Gabón se tramita en 3-5 días — hazlo con 2 semanas de antelación'],
  ARRAY['Naturaleza', 'Aventura', 'Cultura'],
  ARRAY['gorillas', 'jungle', 'rainforest', 'wildlife', 'unspoiled'],
  ARRAY['equatorial', 'tropical', 'humid'],
  ARRAY['June', 'July', 'August', 'September'],
  60, 130, 280, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'douala', 'Duala', 'Camerún', 'África', 'city',
  '{"lat": 4.0511, "lng": 9.7679}',
  'El motor económico de África Central y puerta a la naturaleza más diversa del continente',
  'Duala, la mayor ciudad de Camerún con 3,5 millones de habitantes, es la capital económica del país y el mayor puerto de África Central. Aunque Yaundé es la capital política, Duala es donde late el corazón comercial de una de las naciones con mayor diversidad biológica, cultural y lingüística de todo el continente — Camerún es conocido como "el África en miniatura". El Monte Camerún (volcán activo, 4.040 m) domina el horizonte.',
  'Noviembre a febrero (temporada seca larga) es el mejor período. La gran estación lluviosa (julio-septiembre) es intensa — el Monte Camerún es el punto más lluvioso de África. Evitar julio-agosto para visitas.',
  'El aeropuerto de Duala (DLA) con vuelos desde París (8h), Addis Abeba, Nairobi, Casablanca y ciudades africanas. Dentro de la ciudad: taxis (siempre acordar precio) y mototaxis (bendskin).',
  '[{"name": "Akwa / Bonanjo", "description": "Los barrios más seguros con hoteles internacionales y restaurantes. Desde 60-150 USD/noche."}, {"name": "Bonapriso", "description": "El barrio más elegante con hoteles boutique y los mejores restaurantes. Desde 80-180 USD/noche."}]',
  '[{"title": "Puerto de Duala y el Boulevard de la Liberté", "description": "El mayor puerto de África Central y el paseo central de la ciudad con el ambiente más dinámico y cosmopolita del Camerún."}, {"title": "Marché Mokolo", "description": "El mayor mercado de Camerún con sus 1.200 puestos de telas kaba, artesanía del norte y los sabores más camerunenses de todos."}, {"title": "Museo de Arte Duala", "description": "Arte contemporáneo camerunés y expresiones tradicionales de las numerosas etnias del país — una de las escenas artísticas más vibrantes de África Central."}, {"title": "Ascensión del Monte Camerún", "description": "El volcán activo más alto de África Occidental (4.040 m) accesible desde Buea, a 70 km de Duala. Ascenso de 2 días con guía local."}]',
  'La cocina camerunesa es de las más variadas de África: el ndolé (plato nacional con hojas amargas, cacahuete y langostino), el eru (hojas guisadas con carne y pescado ahumado), el koki (buñuelo de alubias de ojos negros) y el brochettes en cada esquina. La 33 Export (cerveza) y el vino de palma son las bebidas locales.',
  'Duala tiene zonas seguras (Akwa, Bonanjo, Bonapriso) y otras más complicadas. Usa taxis de hotel o Taxify (Bolt) en lugar de parar taxis en la calle. El entorno comercial del puerto puede ser caótico para el turista.',
  'Los ciudadanos de la mayoría de países necesitan visado para Camerún. El visado se tramita en el consulado camerunés antes de viajar — NO existe visa on arrival. El proceso puede ser lento (2-3 semanas). Empieza con suficiente antelación.',
  ARRAY['Tramita el visado camerunés con 3-4 semanas de antelación en el consulado de tu país', 'El ndolé con langostinos es el plato que no puede faltar en Duala', 'Bolt/Taxify funciona en Duala — mucho más seguro que parar taxis en la calle', 'La ascensión del Monte Camerún desde Buea requiere 2 días y guía obligatorio por seguridad'],
  ARRAY['Negocios', 'Aventura', 'Cultura'],
  ARRAY['business', 'africa-miniature', 'port', 'diverse', 'volcano'],
  ARRAY['equatorial', 'tropical', 'very-humid'],
  ARRAY['November', 'December', 'January', 'February'],
  35, 80, 180, 8
) ON CONFLICT (slug) DO NOTHING;

-- OCEANÍA (6 nuevas ciudades)

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'gold-coast', 'Gold Coast', 'Australia', 'Oceanía', 'city',
  '{"lat": -28.0167, "lng": 153.4000}',
  'El paraíso del surf australiano con 70 km de playas doradas y los mejores parques temáticos del país',
  'Gold Coast, en el estado de Queensland, es la ciudad de vacaciones más famosa de Australia: 70 km de playas doradas, el mayor destino de surf del país (Surfers Paradise, Coolangatta), los mejores parques temáticos del hemisferio sur (Movie World, Sea World, Dreamworld) y un nightlife que no para. Sin la pretensión de Sídney ni la cultura de Melbourne, Gold Coast sabe exactamente lo que es: la capital australiana del buen tiempo, la playa y la diversión.',
  'Todo el año tiene buen tiempo en Gold Coast. Septiembre a abril es cálido (25-30°C) y perfecto para la playa. Mayo a agosto es fresco (18-22°C) pero seco y con menos turistas. Las vacaciones escolares australianas (diciembre-enero) disparan los precios.',
  'El aeropuerto de Gold Coast (OOL) en Coolangatta con vuelos directos desde toda Australia y Asia (Singapur, Tokio, Hong Kong). También desde Brisbane (1h en coche o el tren Airtrain). El tranvía G:link conecta el aeropuerto OOL con las playas del norte.',
  '[{"name": "Surfers Paradise", "description": "El centro neurálgico con los mejores hoteles frente a la playa. Hostels desde 25 AUD, hoteles desde 100-200 AUD/noche."}, {"name": "Broadbeach / Mermaid Beach", "description": "Zona más tranquila y local, con mejores restaurantes y menos ruido. Desde 100-180 AUD/noche."}]',
  '[{"title": "Surfers Paradise Beach", "description": "El corazón de Gold Coast con su icónico skyline de rascacielos frente al Pacífico. Aprende surf con clases para principiantes o observa a los pros en Kirra Beach."}, {"title": "Hinterland y el Parque Nacional Lamington", "description": "A 40 km al oeste, la selva subtropical del UNESCO con cataratas, senderismo y pademelones (pequeños canguros). El antídoto perfecto al turismo masivo."}, {"title": "Parques Temáticos (Movie World, Sea World)", "description": "Los mejores parques de Australia: Movie World con las atracciones de DC Comics, Sea World con delfines y tiburones, Wet'n'Wild con toboganes extremos."}, {"title": "Coolangatta y la frontera NSW-Queensland", "description": "El extremo sur de Gold Coast con las mejores olas para surf, ambiente más local y la frontera entre dos estados australianos."}]',
  'Gold Coast es una ciudad de turismo internacional con cocina de todo el mundo. Los fish and chips australianos en la playa, el café con leche de avena, el brunch del sábado, el kangaroo steak (carne de canguro) en los restaurantes australianos y las opciones de mar y huerta de Queensland. La cerveza XXXX (Four X) es la local.',
  'Gold Coast es muy segura. En las playas hay que respetar las banderas de bañistas y nadar siempre entre las banderas (hay rips y corrientes). Los tiburones y medusas son una posibilidad — sigue los consejos de salvamento.',
  'Los ciudadanos de la mayoría de países necesitan ETA (Electronic Travel Authority) o e-Visitor para Australia, tramitable online (20 AUD para ETA). Los ciudadanos de algunos países europeos tienen e-Visitor gratuito. El visado de turista permite hasta 3 meses.',
  ARRAY['Nada SIEMPRE entre las banderas amarillas y rojas — las corrientes son traicioneras', 'El pase multiparque de los parques temáticos es más barato que pagar por separado', 'Coolangatta tiene las mejores olas y menos turistas que Surfers Paradise', 'El tranvía G:link cubre toda la costa de norte a sur — muy cómodo y económico'],
  ARRAY['Playa', 'Aventura', 'Familia'],
  ARRAY['beach', 'surf', 'theme-parks', 'sun', 'party'],
  ARRAY['subtropical', 'warm', 'sunny'],
  ARRAY['September', 'October', 'November', 'March', 'April'],
  60, 130, 280, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'cairns', 'Cairns', 'Australia', 'Oceanía', 'city',
  '{"lat": -16.9186, "lng": 145.7781}',
  'La puerta al Gran Arrecife de Coral y a la selva más antigua del mundo',
  'Cairns, en el norte de Queensland, es el punto de partida para dos de las maravillas naturales del planeta: la Gran Barrera de Coral (la mayor estructura viva de la Tierra, 2.300 km de extensión) y la selva tropical de Daintree (la selva lluviosa más antigua del mundo, 180 millones de años). La pequeña ciudad de 170.000 habitantes vive del turismo de aventura: buceo, snorkel, paracaidismo, zip-line y senderismo entre ríos y cascadas.',
  'Mayo a octubre (temporada seca) es perfecta para el buceo y el snorkel en la Gran Barrera (visibilidad máxima). Noviembre a abril es temporada de lluvias tropicales (y de medusas box jellyfish — peligrosas en la playa). Junio-agosto es la mejor época.',
  'El aeropuerto internacional de Cairns (CNS) con vuelos directos desde Sídney (3h), Melbourne (4h), Brisbane (3h), Auckland, Singapur y Tokio. El Skyrail (teleférico sobre la selva) desde Kuranda es una experiencia en sí misma.',
  '[{"name": "Centro de Cairns", "description": "El centro compacto junto al estuario con hostels, restaurantes y acceso fácil a los tours. Hostels desde 20 AUD, hoteles desde 80-150 AUD/noche."}, {"name": "Northern Beaches", "description": "Las playas al norte (Palm Cove, Trinity Beach) más tranquilas y exclusivas. Desde 120-250 AUD/noche."}]',
  '[{"title": "Gran Barrera de Coral", "description": "Los tours de día a la outer reef en catamarán incluyen snorkel, buzo guía y almuerzo buffet (desde 180 AUD). El buceo certificado permite descender a los 18-20 m para ver el coral vivo."}, {"title": "Selva de Daintree", "description": "La selva más antigua del mundo, a 120 km de Cairns. Nocturno con guía para ver cásuarios, ranas de ojos rojos y la bioluminiscencia de la mariposa azul."}, {"title": "Atherton Tablelands", "description": "El plateau verde al oeste de Cairns con lagunas volcánicas de colores (Lake Eacham, Lake Barrine), cascadas (Millaa Millaa) y platypus en los ríos."}, {"title": "Kuranda — el pueblo en las nubes", "description": "El pueblo hippie en lo alto de la selva accesible en Skyrail (teleférico sobre el dosel) o en el Ferrocarril Escénico histórico de 1891 — una excursión clásica."}]',
  'Cairns tiene la mejor gastronomía de Queensland del Norte: el barramundi (el gran pez tropical australiano) frito con chips, el mudcrab (cangrejo de barro gigante) a la vapor, el reef fish de la Gran Barrera, el mango de Queensland (el mejor del mundo) y el pavlova. El Rusty''s Market del sábado tiene la mejor fruta tropical del país.',
  'Cairns es muy segura. Las playas del norte de Queensland tienen box jellyfish (medusas mortales) de noviembre a mayo — nada solo en las playas con red de protección o en Esplanade Lagoon (piscina gratuita en el centro). El cocodrilo de agua salada es real en ríos y estuarios.',
  'ETA o e-Visitor necesario para Australia. Los ciudadanos de muchos países europeos tienen e-Visitor gratuito. ETA cuesta 20 AUD (tramitable en la app AUS ETA). Permite 3 meses de turismo.',
  ARRAY['El tour de 1 día a la outer reef es diferente al reef de la costa — reserva con empresa certificada (Sunlover, Reef Magic, Quicksilver)', 'El Ferrocarril Escénico Kuranda tiene historia y paisaje — combínalo con el Skyrail de vuelta', 'Las medusas box jellyfish son mortales de noviembre a mayo — nada solo en Esplanade Lagoon', 'El Rusty''s Market (sábado 5h-15h) tiene el mejor fruto tropical y el mejor café de Cairns'],
  ARRAY['Naturaleza', 'Aventura', 'Buceo'],
  ARRAY['reef', 'jungle', 'diving', 'wildlife', 'adventure'],
  ARRAY['tropical', 'humid', 'dry-season'],
  ARRAY['June', 'July', 'August', 'September', 'October'],
  50, 110, 250, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'darwin', 'Darwin', 'Australia', 'Oceanía', 'city',
  '{"lat": -12.4634, "lng": 130.8456}',
  'La ciudad más remota de Australia, puerta al Kakadu y a Asia desde el Outback',
  'Darwin, capital del Territorio del Norte, es la ciudad más aislada y con más personalidad de Australia: 150.000 habitantes en el extremo norte del continente, frente al Mar de Timor, a 4h en avión de Sídney y a 3h de Singapur. Destruida por los japoneses en 1942 y por el ciclón Tracy en 1974, Darwin se reinventó como una ciudad multicultural, diversa y con la mejor escena de comida asiática del país. La puerta al parque Kakadu y al Outback.',
  'Mayo a octubre (la Dry Season) es absolutamente imprescindible: cielo azul, temperatura de 30°C, noches frescas y la mejor época para Kakadu. La Wet Season (noviembre-abril) es espectacular pero las tormentas eléctricas más intensas de Australia y los cocodrilos en los ríos complican el acceso al parque.',
  'El aeropuerto de Darwin (DRW) con vuelos desde Sídney (4h), Melbourne (4h30), Brisbane (3h30), Perth (4h) y conexiones directas a Singapur (5h), Denpasar/Bali (2h30) y Timor Leste. Dentro de la ciudad: taxis, Uber y alquiler de coche para el Outback.',
  '[{"name": "Darwin City Centre", "description": "El centro compacto con hostels y hoteles económicos. Desde 25 AUD (hostel) a 100-180 AUD (hotel) por noche."}, {"name": "Fannie Bay / Parap", "description": "Barrios residenciales tranquilos con bed & breakfasts australianos. Desde 100-150 AUD/noche."}]',
  '[{"title": "Parque Nacional Kakadu (UNESCO)", "description": "A 250 km de Darwin, el mayor parque nacional de Australia: pinturas rupestres aborígenes de 20.000 años, cocodrilos de agua salada, birruk (magpie geese) y cataratas espectaculares. Un mundo en sí mismo."}, {"title": "Mindil Beach Sunset Market", "description": "El mercado de atardecer de Darwin (jueves y domingos en temporada seca) con 300 puestos de comida asiática, artesanía y los mejores atardeceres de Australia."}, {"title": "Parque Nacional Litchfield", "description": "A 100 km de Darwin, cascadas cristalinas con pozas naturales, termiteros magnéticos y la selva más accesible del Territorio del Norte."}, {"title": "Museum & Art Gallery Northern Territory", "description": "El mejor museo del Territorio con la historia del ciclón Tracy (1974), el arte de los aborígenes del Arnhem Land y la fauna marina del Mar de Timor."}]',
  'Darwin tiene la mejor gastronomía asiática de Australia: el barramundi de las aguas del Norte, el crocodile satay (satay de cocodrilo — delicioso y sin presunción), las dumplings del mercado Mindil, el laksa malayo, la cocina vietnamita de Rapid Creek y el bush tucker (comida aborigen: quandong, witchetty grubs). La cerveza Northern Territory Draught bien fría y el Territory Sunset son los tragos locales.',
  'Darwin es muy segura. En la naturaleza los cocodrilos de agua salada son peligrosos reales — nunca nades en ríos o estuarios fuera de zonas declaradas seguras. Las box jellyfish de noviembre a abril son peligrosas en las playas.',
  'ETA o e-Visitor requerido para Australia. Muchos países europeos tienen e-Visitor gratuito. ETA (20 AUD en app AUS ETA). Permite 3 meses de turismo.',
  ARRAY['El mercado Mindil Beach Sunset (jueves y domingos, mayo-octubre) es la mejor experiencia de Darwin', 'Kakadu requiere mínimo 2 días — reserva tour o alquila 4x4 (los caminos pueden ser de tierra)', 'NUNCA nades en ríos o estuarios en el NT — los cocodrilos de agua salada son invisibles y atacan', 'Darwin está a solo 2h30 de Bali en avión — combina el viaje fácilmente'],
  ARRAY['Naturaleza', 'Aventura', 'Cultura'],
  ARRAY['outback', 'aboriginal', 'wildlife', 'remote', 'multicultural'],
  ARRAY['tropical', 'dry-wet-seasons'],
  ARRAY['May', 'June', 'July', 'August', 'September', 'October'],
  50, 110, 240, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'hobart', 'Hobart', 'Australia', 'Oceanía', 'city',
  '{"lat": -42.8821, "lng": 147.3272}',
  'La capital de Tasmania: el MONA más provocador del mundo y el fin del mundo austral',
  'Hobart, capital de Tasmania, es la segunda ciudad más antigua de Australia y una de las más sorprendentes: a 42° de latitud sur, con el Monte Wellington nevado dominando la ciudad, una bahía histórica llena de veleros y el MONA (Museum of Old and New Art) — el museo privado más provocador y discutido del mundo. Tasmania tiene los mejores quesos, vinos y salmón de Australia, y una naturaleza salvaje que cubre el 40% del territorio.',
  'Diciembre a marzo (verano austral) es ideal: 20-26°C, los días más largos y el Sydney to Hobart Yacht Race en diciembre. El MONA no cierra por temporada. Junio-agosto es frío (8-12°C) pero el ambiente del mercado de Salamanca y el MONA Dark Mofo son extraordinarios.',
  'El aeropuerto de Hobart (HBA) con vuelos desde Sídney (1h45), Melbourne (1h15), Brisbane (2h30). También el famoso ferry Spirit of Tasmania desde Melbourne (1 noche). Dentro de Hobart: taxi, Uber y bicicleta para el centro.',
  '[{"name": "Battery Point / Sandy Bay", "description": "El barrio histórico más pintoresco con casas victorianas y pubs históricos. B&Bs y boutique hotels desde 120-200 AUD/noche."}, {"name": "Salamanca / Waterfront", "description": "El frente portuario con galerías, restaurantes y el mercado del sábado. Apartamentos y hoteles desde 100-180 AUD/noche."}]',
  '[{"title": "MONA — Museum of Old and New Art", "description": "El museo privado más extraordinario y polémico del mundo: excavado en la roca arenisca de la península de Berriedale, con arte provocador de Bacon, Hirschhorn y creaciones propias. Imprescindible."}, {"title": "Mercado de Salamanca (sábados)", "description": "El mercado al aire libre más famoso de Australia: 300 puestos de queso tasmaniano, salmón ahumado, vino y artesanía local. El sábado por la mañana en Hobart."}, {"title": "Monte Wellington / kunanyi", "description": "A 20 min en coche del centro (1.270 m), la cumbre que domina Hobart tiene vistas sobre la ciudad, el río Derwent y la bahía D''Entrecasteaux. Con nieve en invierno."}, {"title": "Zona Salvaje de Tasmania (excursión)", "description": "El 40% de Tasmania es Patrimonio Natural UNESCO. Cradle Mountain, Wineglass Bay (Freycinet) y South West Cape son las joyas de la naturaleza más remota de Australia."}]',
  'Hobart tiene la mejor gastronomía de Tasmania: el salmón atlántico de las aguas limpias del sur (el mejor del mundo), los ostras de Bruny Island, el queso King Island camembert, las trufas negras de la región (la capital de la trufa del hemisferio sur) y los vinos pinot noir del valle Huon. El mercado de Salamanca condensa todo esto en 4 horas del sábado por la mañana.',
  'Hobart es extremadamente segura — una de las ciudades más tranquilas de Australia. El MONA tiene zonas de contenido adulto explícito (lo aclaran en la entrada). La naturaleza de Tasmania puede ser peligrosa sin equipo y preparación.',
  'ETA o e-Visitor para Australia. Muchos países europeos e-Visitor gratuito. ETA (20 AUD). 3 meses de turismo.',
  ARRAY['El MONA tiene una app (O) que sustituye al folleto convencional — descárgala antes de entrar', 'El mercado de Salamanca (sábados 8h30-15h) no puede faltar en ningún itinerario de Hobart', 'El ferry Spirit of Tasmania desde Melbourne es la manera más romántica de llegar a la isla', 'Wineglass Bay (Freycinet) se puede visitar desde Hobart en excursión de un día larga pero merece el viaje'],
  ARRAY['Cultura', 'Naturaleza', 'Gastronomía'],
  ARRAY['mona', 'wilderness', 'history', 'food', 'arts'],
  ARRAY['temperate', 'cool', 'oceanic'],
  ARRAY['December', 'January', 'February', 'March'],
  60, 120, 260, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'apia', 'Apia', 'Samoa', 'Oceanía', 'city',
  '{"lat": -13.8333, "lng": -171.8333}',
  'La capital polinesia más auténtica, donde el Pacífico Sur vive sin artificios turísticos',
  'Apia, capital de Samoa (no confundir con Samoa Americana), es la ciudad más auténtica del Pacífico Sur: una ciudad pequeña y relajada de 40.000 habitantes donde la cultura fa''a Samoa (el modo de vida samoano) sigue siendo el motor de la sociedad. La hospitalidad polinesia es legendaria, las playas son de acceso libre (sin resorts vallados), el fútbol samoano se juega en cada pueblo y los Sunday to''ona''i (festines familiares) son la institución más sagrada de la semana.',
  'Mayo a octubre (temporada seca) es el mejor período: 26-30°C, mar en calma y sol frecuente. Noviembre a abril es temporada de ciclones — evita enero y febrero. El agua del mar tiene temperatura constante (28°C) todo el año.',
  'El aeropuerto de Faleolo (APW) a 35 km de Apia con vuelos desde Auckland (3h30), Sídney (5h), Fiji, Tonga y Hawái. Autobús o taxi al centro de Apia (1h). Dentro de la ciudad y la isla: autobuses locales y taxis sin taxímetro (acordar precio).',
  '[{"name": "Centro de Apia", "description": "El pequeño centro colonial con los mejores fale (alojamientos tradicionales en bungalows de bambú) y algunos hoteles de gama media. Desde 80-150 WST/noche."}, {"name": "Playas de la costa norte (Upolu)", "description": "Faleolo, Lalomanu y Saleapaga tienen los fale de playa más auténticos de Samoa. Desde 50-120 WST/noche todo incluido."}]',
  '[{"title": "Playa de Lalomanu", "description": "Considerada una de las playas más hermosas del Pacífico Sur: arena blanca, palmeras y fale de bambú sobre el arrecife. A 1h de Apia."}, {"title": "To Sua Ocean Trench", "description": "La piscina natural más fotogénica de Oceanía: una grieta de 30 m de profundidad con agua turquesa del océano Pacífico con una escalera de madera."}, {"title": "Villa Vailima — Museo Robert Louis Stevenson", "description": "La mansión donde vivió y murió el autor de La Isla del Tesoro en 1894. Restaurada perfectamente, con su tumba en la cima del monte Vaea."}, {"title": "Mercado de Fugalei (Apia Market)", "description": "El mercado más animado de Samoa con taro, coco, palusami (hojas de taro con coco) y la artesanía más auténtica del Pacífico."}]',
  'La cocina samoana gira en torno al coco y el taro: el palusami (hojas de taro rellenas de leche de coco, el plato más samoano), el umu (horno de tierra del domingo), el oka (ceviche de atún con leche de coco), los bananas y papayas y el Vailima Beer (la cerveza nacional). Los Sunday to''ona''i son festines comunitarios: si te invitan, acepta siempre.',
  'Samoa es extremadamente segura para viajeros. El mayor riesgo son los perros callejeros de las carreteras. Respeta las normas del fa''a Samoa: vístete discretamente en los pueblos, quítate los zapatos antes de entrar a las casas y nunca interrumpas los lotu (oraciones).',
  'Los ciudadanos de la UE, EE.UU., Australia, Nueva Zelanda y muchos países entran sin visado hasta 60 días a Samoa. El permiso de entrada se da a la llegada gratuitamente. Pasaporte con 6 meses de vigencia.',
  ARRAY['El To Sua Ocean Trench vale la entrada (15 WST) — ve antes de las 10h para evitar los grupos de crucero', 'El Sunday to''ona''i (festín del domingo) es la mejor experiencia cultural de Samoa — pide a tu alojamiento que te incluya', 'Los fale de playa en Lalomanu son el alojamiento más auténtico del Pacífico Sur', 'El autobús local de Apia al resto de la isla cuesta 1-2 WST y es la experiencia más samoana'],
  ARRAY['Playa', 'Cultura', 'Naturaleza'],
  ARRAY['pacific', 'polynesian', 'authentic', 'beaches', 'culture'],
  ARRAY['tropical', 'warm', 'humid'],
  ARRAY['May', 'June', 'July', 'August', 'September', 'October'],
  40, 90, 200, 8
) ON CONFLICT (slug) DO NOTHING;

INSERT INTO destinations (slug, name, country, continent, type, coordinates, tagline, intro, when_to_go, how_to_get_there, where_to_sleep, what_to_do, food_and_drink, safety, visa_info, local_tips, travel_styles, vibes, climate, best_months, budget_daily_low, budget_daily_mid, budget_daily_high, guide_quality)
VALUES (
  'port-vila', 'Port Vila', 'Vanuatu', 'Oceanía', 'city',
  '{"lat": -17.7333, "lng": 168.3167}',
  'La capital del archipiélago del Pacífico Sur con el volcán más accesible del mundo',
  'Port Vila, capital de Vanuatu en la isla de Éfaté, es la puerta de entrada a uno de los archipiélagos más fascinantes y menos visitados del Pacífico: 83 islas con más de 100 idiomas distintos (el mayor número de lenguas por cápita del mundo), playas de arena negra volcánica, el volcán Yasur de Tanna (accesible en vehículo — el volcán más accesible del mundo con lava activa visible), y una cultura melanesia de ni-Vanuatu profundamente arraigada.',
  'Mayo a octubre (temporada seca) es ideal: 25-28°C, mar en calma y sin ciclones. Noviembre a abril es temporada de ciclones (el Pam de 2015 fue catastrófico). Junio-agosto tiene el tiempo más estable y las aguas más claras para buceo.',
  'El aeropuerto internacional de Bauerfield (VLI) en Port Vila con vuelos desde Brisbane (3h), Sídney (3h30), Auckland (3h30), Fiji y Noumea (Nueva Caledonia). Dentro de Port Vila: taxis y minibuses (buses públicos locales).',
  '[{"name": "Port Vila Centro / Efate", "description": "Hoteles boutique y económicos en el centro de la capital. Desde 80-150 AUD/noche."}, {"name": "Mele / Erakor Island", "description": "Resorts boutique en isla privada conectada por puente. Desde 150-300 AUD/noche."}]',
  '[{"title": "Volcán Yasur de Tanna", "description": "En la isla de Tanna (vuelo de 30 min desde Port Vila), el volcán más accesible del mundo: llegas en 4x4 hasta el borde del cráter y ves la lava activa a pocos metros. Una experiencia que cambia la vida."}, {"title": "Buceo en Million Dollar Point", "description": "Al norte de Éfaté, los restos del USS President Coolidge (trasatlántico hundido en 1942) forman el mayor pecio accesible en buceo recreativo del mundo."}, {"title": "Cascadas de Mele y la piscina natural de la playa", "description": "Las cascadas a 10 km de Port Vila con pozas naturales en distintos niveles de la selva tropical. Accesible en tour o taxi."}, {"title": "Mercado de Port Vila", "description": "El mercado más colorido del Pacífico con ñames, taro, kava fresca y artesanía ni-Vanuatu de cesto trenzado y tallas de madera."}]',
  'La cocina de Vanuatu mezcla tradición melanesia con influencias francesas: el lap-lap (pudding de ñame o yuca con coco y pollo), el bougna (ñame, coco y pollo envuelto en hojas de banana cocinado en horno de piedra), el pescado fresco del Pacífico y las langostas de arrecife. Y la kava: la bebida sagrada de Vanuatu hecha de raíz de piper methysticum — el ritual social más importante del país.',
  'Vanuatu es muy segura para los viajeros. El volcán Yasur en Tanna puede tener erupciones — sigue siempre las indicaciones de los guías locales. Los ciclones tropicales son el mayor riesgo natural.',
  'Los ciudadanos de Australia, Nueva Zelanda, UE, EE.UU. y muchos países entran sin visado hasta 30 días (ampliable). El permiso de entrada se da a la llegada gratuitamente. Pasaporte con 6 meses de vigencia.',
  ARRAY['El volcán Yasur de Tanna justifica solo el viaje a Vanuatu — no te lo pierdas si tienes tiempo', 'La kava en un nakamal (bar de kava) es la experiencia cultural más auténtica de Vanuatu — el ritual es importante', 'El pecio del SS President Coolidge es el mejor buceo de wreck del Pacífico Sur', 'El vuelo Port Vila - Tanna (30 min) es imprescindible para el volcán — reserva con antelación'],
  ARRAY['Naturaleza', 'Aventura', 'Buceo'],
  ARRAY['volcano', 'pacific', 'diving', 'wreck', 'melanesian'],
  ARRAY['tropical', 'warm', 'humid'],
  ARRAY['May', 'June', 'July', 'August', 'September', 'October'],
  50, 110, 250, 8
) ON CONFLICT (slug) DO NOTHING;

