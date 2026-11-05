# -*- coding: utf-8 -*-
"""UI strings in 4 languages: qq (Qaraqalpaq, Latin), uz (O'zbek), ru (Русский), en (English)."""

LANGS = [
    ("qq", "Qaraqalpaqsha"),
    ("uz", "O'zbekcha"),
    ("ru", "Русский"),
    ("en", "English"),
]
LANG_CODES = [c for c, _ in LANGS]
DEFAULT_LANG = "qq"

T = {
    # ---------- navigation / common
    "brand_tag": {
        "qq": "Aral duz-shań boranlarınan erte eskertiw sisteması",
        "uz": "Orol tuz-chang bo'ronlaridan erta ogohlantirish tizimi",
        "ru": "Система раннего оповещения о солево-пылевых бурях Арала",
        "en": "Early-warning system for Aral salt-dust storms",
    },
    "nav_home": {"qq": "Bas bet", "uz": "Bosh sahifa", "ru": "Главная", "en": "Home"},
    "nav_districts": {"qq": "Rayonlar", "uz": "Tumanlar", "ru": "Районы", "en": "Districts"},
    "nav_assistant": {"qq": "JI járdemshi", "uz": "AI yordamchi", "ru": "ИИ-помощник", "en": "AI assistant"},
    "nav_report": {"qq": "Xabar beriw", "uz": "Xabar berish", "ru": "Сообщить", "en": "Report"},
    "nav_dashboard": {"qq": "Mákemeler paneli", "uz": "Tashkilotlar paneli", "ru": "Панель ведомств", "en": "Agency dashboard"},
    "nav_about": {"qq": "Joybar haqqında", "uz": "Loyiha haqida", "ru": "О проекте", "en": "About"},
    "nav_download": {"qq": "Ilovanı júklew", "uz": "Ilovani yuklash", "ru": "Скачать приложение", "en": "Get the app"},
    "lang": {"qq": "Til", "uz": "Til", "ru": "Язык", "en": "Language"},
    "open": {"qq": "Ashıw", "uz": "Ochish", "ru": "Открыть", "en": "Open"},
    "back": {"qq": "Artqa", "uz": "Orqaga", "ru": "Назад", "en": "Back"},
    "loading": {"qq": "Júklenbekte…", "uz": "Yuklanmoqda…", "ru": "Загрузка…", "en": "Loading…"},
    "updated": {"qq": "Jańalandı", "uz": "Yangilandi", "ru": "Обновлено", "en": "Updated"},
    "yes": {"qq": "Awa", "uz": "Ha", "ru": "Да", "en": "Yes"},
    "no": {"qq": "Yaq", "uz": "Yo'q", "ru": "Нет", "en": "No"},
    "hours_short": {"qq": "saat", "uz": "soat", "ru": "ч", "en": "h"},
    "data_live": {
        "qq": "Tiri maǵlıwmat: Copernicus CAMS atmosfera modeli (Open-Meteo)",
        "uz": "Jonli ma'lumot: Copernicus CAMS atmosfera modeli (Open-Meteo)",
        "ru": "Живые данные: атмосферная модель Copernicus CAMS (Open-Meteo)",
        "en": "Live data: Copernicus CAMS atmosphere model (Open-Meteo)",
    },
    "data_sim": {
        "qq": "Dıqqat: maǵlıwmat deregi házir qoljetimsiz — simulyaciya kórsetilmekte",
        "uz": "Diqqat: ma'lumot manbai hozir mavjud emas — simulyatsiya ko'rsatilmoqda",
        "ru": "Внимание: источник данных недоступен — показана симуляция",
        "en": "Note: data source unavailable right now — showing a simulation",
    },

    # ---------- risk vocabulary
    "risk_index": {
        "qq": "Aral shań qáwip indeksi",
        "uz": "Orol chang xavf indeksi",
        "ru": "Индекс пылевой опасности Арала",
        "en": "Aral Dust Risk Index",
    },
    "risk_short": {"qq": "Qáwip", "uz": "Xavf", "ru": "Риск", "en": "Risk"},
    "lvl_low": {"qq": "Tómen", "uz": "Past", "ru": "Низкий", "en": "Low"},
    "lvl_moderate": {"qq": "Orta", "uz": "O'rtacha", "ru": "Умеренный", "en": "Moderate"},
    "lvl_high": {"qq": "Joqarı", "uz": "Yuqori", "ru": "Высокий", "en": "High"},
    "lvl_very_high": {"qq": "Júdá joqarı", "uz": "Juda yuqori", "ru": "Очень высокий", "en": "Very high"},
    "lvl_extreme": {"qq": "Qáwipli", "uz": "Favqulodda", "ru": "Экстремальный", "en": "Extreme"},
    "pm10": {"qq": "PM10 bólekshe", "uz": "PM10 zarracha", "ru": "Частицы PM10", "en": "PM10 particles"},
    "pm25": {"qq": "PM2.5 bólekshe", "uz": "PM2.5 zarracha", "ru": "Частицы PM2.5", "en": "PM2.5 particles"},
    "dust": {"qq": "Shań", "uz": "Chang", "ru": "Пыль", "en": "Dust"},
    "wind": {"qq": "Samal", "uz": "Shamol", "ru": "Ветер", "en": "Wind"},
    "humidity": {"qq": "Ígallıq", "uz": "Namlik", "ru": "Влажность", "en": "Humidity"},
    "temp": {"qq": "Temperatura", "uz": "Harorat", "ru": "Температура", "en": "Temperature"},
    "aod": {"qq": "Aerozol qalıńlıǵı", "uz": "Aerozol qalinligi", "ru": "Аэрозольная толща", "en": "Aerosol depth"},
    "salt_prob": {
        "qq": "Aralqum duzınıń keliw itimallıǵı",
        "uz": "Orolqum tuzi kelish ehtimoli",
        "ru": "Вероятность соли с Аралкума",
        "en": "Aralkum salt-dust probability",
    },
    "from_aralkum": {"qq": "Samal Aralqumnan", "uz": "Shamol Orolqumdan", "ru": "Ветер с Аралкума", "en": "Wind from Aralkum"},
    "part_pm10": {"qq": "PM10", "uz": "PM10", "ru": "PM10", "en": "PM10"},
    "part_pm25": {"qq": "PM2.5", "uz": "PM2.5", "ru": "PM2.5", "en": "PM2.5"},
    "part_dust": {"qq": "Shań", "uz": "Chang", "ru": "Пыль", "en": "Dust"},
    "part_wind": {"qq": "Aralqum samalı", "uz": "Orolqum shamoli", "ru": "Ветер с Аралкума", "en": "Aralkum wind"},
    "part_dry": {"qq": "Qurǵaqlıq", "uz": "Quruqlik", "ru": "Сухость", "en": "Dryness"},
    "part_reports": {"qq": "Puqara xabarları", "uz": "Fuqaro xabarlari", "ru": "Сообщения жителей", "en": "Citizen reports"},

    # ---------- home
    "hero_kicker": {
        "qq": "«Eń innovaciyalıq ideya» — NMTU, 2026",
        "uz": "«Eng innovatsion g'oya» — NDTU, 2026",
        "ru": "«Самая инновационная идея» — НГТУ, 2026",
        "en": "“Most Innovative Idea” — NSTU, 2026",
    },
    "hero_title": {
        "qq": "Aralboyında qáwipsiz dem alıń",
        "uz": "Orolbo'yida xavfsiz nafas oling",
        "ru": "Дышите безопасно в Приаралье",
        "en": "Breathe safely in the Aral region",
    },
    "hero_text": {
        "qq": "Hár jılı qurǵaǵan Aral túbi — Aralqum — hawaǵa millionlaǵan tonna duz hám shań kóteredi. AralShield sputnik tiykarındaǵı atmosfera maǵlıwmatların, samal analizin hám puqaralar xabarların birlestirip, boran kelmesten aldın Qaraqalpaqstannıń hár bir rayonın eskertedi hám hár bir adamǵa óz densawlıǵı ushın jasalma intellekt másláhátin beredi.",
        "uz": "Har yili qurigan Orol tubi — Orolqum — havoga millionlab tonna tuz va chang ko'taradi. AralShield sun'iy yo'ldosh asosidagi atmosfera ma'lumotlari, shamol tahlili va fuqarolar xabarlarini birlashtirib, bo'ron kelishidan oldin Qoraqalpog'istonning har bir tumanini ogohlantiradi va har bir insonga o'z sog'lig'i uchun sun'iy intellekt maslahatini beradi.",
        "ru": "Каждый год высохшее дно Арала — Аралкум — поднимает в воздух миллионы тонн соли и пыли. AralShield объединяет спутниковые атмосферные данные, анализ ветра и сообщения жителей, чтобы предупредить каждый район Каракалпакстана до прихода бури, и даёт каждому человеку персональный совет ИИ для его здоровья.",
        "en": "Every year the dried Aral seabed — the Aralkum — lifts millions of tonnes of salt and dust into the air. AralShield fuses satellite-based atmospheric data, wind analysis and citizen reports to warn every district of Karakalpakstan before the storm arrives, and gives each person AI advice for their own health.",
    },
    "cta_map": {"qq": "Tiri kartanı kóriw", "uz": "Jonli xaritani ko'rish", "ru": "Смотреть живую карту", "en": "See the live map"},
    "cta_app": {"qq": "Android ilovasın júklew", "uz": "Android ilovasini yuklash", "ru": "Скачать для Android", "en": "Download for Android"},
    "worst_now": {"qq": "Házir eń joqarı qáwip", "uz": "Hozir eng yuqori xavf", "ru": "Сейчас самый высокий риск", "en": "Highest risk right now"},
    "people_in_risk": {
        "qq": "Joqarı qáwip zonasındaǵı xalıq",
        "uz": "Yuqori xavf hududidagi aholi",
        "ru": "Население в зонах высокого риска",
        "en": "People in high-risk zones",
    },
    "districts_high": {
        "qq": "Joqarı qáwipli rayonlar",
        "uz": "Yuqori xavfli tumanlar",
        "ru": "Районов с высоким риском",
        "en": "Districts at high risk",
    },
    "peak72": {"qq": "72 saattaǵı eń joqarı", "uz": "72 soatdagi eng yuqori", "ru": "Пик за 72 часа", "en": "Peak in next 72 h"},
    "monitored": {"qq": "Baqlanatuǵın rayon hám qala", "uz": "Kuzatilayotgan tuman va shahar", "ru": "Районов и городов под наблюдением", "en": "Districts & cities monitored"},
    "map_title": {"qq": "Qaraqalpaqstannıń tiri qáwip kartası", "uz": "Qoraqalpog'istonning jonli xavf xaritasi", "ru": "Живая карта риска Каракалпакстана", "en": "Live risk map of Karakalpakstan"},
    "map_hint": {
        "qq": "Rayondı basıń — tolıq boljaw hám jeke másláhát ashıladı.",
        "uz": "Tumanni bosing — to'liq prognoz va shaxsiy maslahat ochiladi.",
        "ru": "Нажмите на район — откроется прогноз и личный совет.",
        "en": "Tap a district to open its forecast and personal advice.",
    },
    "how_title": {"qq": "Qalay isleydi", "uz": "Qanday ishlaydi", "ru": "Как это работает", "en": "How it works"},
    "how1_t": {"qq": "Kósh mánbeli maǵlıwmat", "uz": "Ko'p manbali ma'lumot", "ru": "Данные из многих источников", "en": "Multi-source data"},
    "how1_d": {
        "qq": "Copernicus CAMS sputnik-model maǵlıwmatları: PM10, PM2.5, shań, aerozol + samal baǵdarı, ıǵallıq — 17 rayon ushın hár saat.",
        "uz": "Copernicus CAMS sun'iy yo'ldosh-model ma'lumotlari: PM10, PM2.5, chang, aerozol + shamol yo'nalishi, namlik — 17 hudud uchun har soat.",
        "ru": "Спутниково-модельные данные Copernicus CAMS: PM10, PM2.5, пыль, аэрозоль + направление ветра и влажность — каждый час для 17 районов.",
        "en": "Copernicus CAMS satellite-model data: PM10, PM2.5, dust, aerosol + wind direction and humidity — hourly for 17 districts.",
    },
    "how2_t": {"qq": "Aralqum algoritmi", "uz": "Orolqum algoritmi", "ru": "Алгоритм «Аралкум»", "en": "Aralkum algorithm"},
    "how2_d": {
        "qq": "Samal Aralqum sektorınan (SB–S–SSh) esse hám rayon tenizge jaqın bolsa, duzlı shań qáwpi kúsheyedi. Nátiyje — 0–100 indeks.",
        "uz": "Shamol Orolqum sektoridan (ShG'–Sh–ShSh) essa va tuman dengizga yaqin bo'lsa, tuzli chang xavfi kuchayadi. Natija — 0–100 indeks.",
        "ru": "Если ветер дует из сектора Аралкума (СЗ–С–СВ) и район близко к бывшему морю, риск солевой пыли растёт. Итог — индекс 0–100.",
        "en": "When wind blows from the Aralkum sector (NW–N–NE) and a district is close to the former sea, salt-dust risk rises. Result: a 0–100 index.",
    },
    "how3_t": {"qq": "Puqara datchikleri", "uz": "Fuqaro datchiklari", "ru": "Жители как датчики", "en": "Citizens as sensors"},
    "how3_d": {
        "qq": "Xalıq shań, duz, kórinis yamasa densawlıq belgileri haqqında xabar beredi — bul indekske tikkeley tásir etedi.",
        "uz": "Aholi chang, tuz, ko'rinish yoki sog'liq belgilari haqida xabar beradi — bu indeksga bevosita ta'sir qiladi.",
        "ru": "Жители сообщают о пыли, соли, видимости и симптомах — это сразу учитывается в индексе.",
        "en": "Residents report dust, salt, visibility or symptoms — reports feed straight into the index.",
    },
    "how4_t": {"qq": "Jeke JI másláhát", "uz": "Shaxsiy AI maslahat", "ru": "Личный совет ИИ", "en": "Personal AI advice"},
    "how4_d": {
        "qq": "Astma, bala, ǵarrı, júkli hayal yamasa sırtta isleytuǵın adam — hár birine óz tilinde anıq háreket rejesi.",
        "uz": "Astma, bola, keksa, homilador ayol yoki ochiq havoda ishlovchi — har biriga o'z tilida aniq harakat rejasi.",
        "ru": "Астма, ребёнок, пожилой человек, беременность или работа на улице — каждому свой план действий на родном языке.",
        "en": "Asthma, child, elderly, pregnancy or outdoor work — everyone gets a concrete action plan in their own language.",
    },
    "all_districts": {"qq": "Barlıq rayonlar", "uz": "Barcha tumanlar", "ru": "Все районы", "en": "All districts"},
    "app_promo_t": {"qq": "Boran eskertiwi telefonıńızǵa", "uz": "Bo'ron ogohlantirishi telefoningizga", "ru": "Предупреждение о буре — на телефон", "en": "Storm alerts on your phone"},
    "app_promo_d": {
        "qq": "Android ilovası rayonıńızdı fon rejiminde baqlaydı hám qáwip joqarılaǵanda bildiriw jiberedi.",
        "uz": "Android ilovasi tumaningizni fon rejimida kuzatadi va xavf oshganda bildirishnoma yuboradi.",
        "ru": "Приложение для Android следит за вашим районом в фоне и присылает уведомление, когда риск растёт.",
        "en": "The Android app watches your district in the background and notifies you when the risk rises.",
    },

    # ---------- district page
    "forecast72": {"qq": "72 saatlıq boljaw", "uz": "72 soatlik prognoz", "ru": "Прогноз на 72 часа", "en": "72-hour forecast"},
    "components": {"qq": "Qáwip neden quralǵan", "uz": "Xavf nimalardan tashkil topgan", "ru": "Из чего складывается риск", "en": "What makes up the risk"},
    "now": {"qq": "Házir", "uz": "Hozir", "ru": "Сейчас", "en": "Now"},
    "advice_title": {"qq": "Jeke JI másláhát", "uz": "Shaxsiy AI maslahat", "ru": "Персональный совет ИИ", "en": "Personal AI advice"},
    "group_label": {"qq": "Siz kimsiz?", "uz": "Siz kimsiz?", "ru": "Кто вы?", "en": "Who are you?"},
    "grp_general": {"qq": "Ulıwma", "uz": "Umumiy", "ru": "Обычный взрослый", "en": "General adult"},
    "grp_child": {"qq": "Bala / ata-ana", "uz": "Bola / ota-ona", "ru": "Ребёнок / родитель", "en": "Child / parent"},
    "grp_elderly": {"qq": "Jası úlken adam", "uz": "Keksa inson", "ru": "Пожилой человек", "en": "Elderly person"},
    "grp_asthma": {"qq": "Astma / ókpe kesellikleri", "uz": "Astma / o'pka kasalligi", "ru": "Астма / болезни лёгких", "en": "Asthma / lung disease"},
    "grp_pregnant": {"qq": "Júkli hayal", "uz": "Homilador ayol", "ru": "Беременная", "en": "Pregnant woman"},
    "grp_outdoor": {"qq": "Sırtta isleytuǵın (diyqan, qurılısshı)", "uz": "Ochiq havoda ishlovchi (dehqon, quruvchi)", "ru": "Работа на улице (фермер, строитель)", "en": "Outdoor worker (farmer, builder)"},
    "get_advice": {"qq": "Másláhát alıw", "uz": "Maslahat olish", "ru": "Получить совет", "en": "Get advice"},
    "advice_note": {
        "qq": "Bul shıpakerdiń másláhátın almastırmaydı. Awır belgilerde 103 ge qońıraw etiń.",
        "uz": "Bu shifokor maslahatining o'rnini bosmaydi. Og'ir belgilarda 103 ga qo'ng'iroq qiling.",
        "ru": "Это не заменяет консультацию врача. При тяжёлых симптомах звоните 103.",
        "en": "This does not replace a doctor. For severe symptoms call 103.",
    },
    "recent_reports": {"qq": "Sońǵı xabarlar", "uz": "So'nggi xabarlar", "ru": "Последние сообщения", "en": "Latest reports"},
    "no_reports": {"qq": "Házirshe xabar joq.", "uz": "Hozircha xabar yo'q.", "ru": "Пока сообщений нет.", "en": "No reports yet."},
    "enable_alerts": {"qq": "Bul rayon ushın eskertiwdi qosıw", "uz": "Bu tuman uchun ogohlantirishni yoqish", "ru": "Включить оповещения для района", "en": "Enable alerts for this district"},
    "alerts_on": {"qq": "Eskertiw qosıldı ✓", "uz": "Ogohlantirish yoqildi ✓", "ru": "Оповещения включены ✓", "en": "Alerts enabled ✓"},

    # ---------- assistant
    "chat_title": {"qq": "AralShield JI járdemshisi", "uz": "AralShield AI yordamchisi", "ru": "ИИ-помощник AralShield", "en": "AralShield AI assistant"},
    "chat_sub": {
        "qq": "Hawa sapası, shań boranı hám densawlıqtı qorǵaw haqqında sorań. Járdemshi házirgi tiri maǵlıwmatlardı biledi.",
        "uz": "Havo sifati, chang bo'roni va sog'liqni himoya qilish haqida so'rang. Yordamchi hozirgi jonli ma'lumotlarni biladi.",
        "ru": "Спрашивайте о качестве воздуха, пыльных бурях и защите здоровья. Помощник видит текущие живые данные.",
        "en": "Ask about air quality, dust storms and protecting your health. The assistant sees the current live data.",
    },
    "chat_placeholder": {"qq": "Sorawıńızdı jazıń…", "uz": "Savolingizni yozing…", "ru": "Напишите вопрос…", "en": "Type your question…"},
    "send": {"qq": "Jiberiw", "uz": "Yuborish", "ru": "Отправить", "en": "Send"},
    "chat_ex1": {"qq": "Búgin Moynaqta balalar sırtta oynasa bola ma?", "uz": "Bugun Mo'ynoqda bolalar tashqarida o'ynasa bo'ladimi?", "ru": "Можно ли сегодня детям гулять в Муйнаке?", "en": "Can children play outside in Moynaq today?"},
    "chat_ex2": {"qq": "Shań boranı waqtında úyde ne islew kerek?", "uz": "Chang bo'roni paytida uyda nima qilish kerak?", "ru": "Что делать дома во время пыльной бури?", "en": "What should I do at home during a dust storm?"},
    "chat_ex3": {"qq": "Qaysı rayonda erteń qáwip eń joqarı?", "uz": "Qaysi tumanda ertaga xavf eng yuqori?", "ru": "Где завтра будет самый высокий риск?", "en": "Which district has the highest risk tomorrow?"},
    "ai_offline": {
        "qq": "JI serveri jalǵanbaǵan — qaǵıydalarǵa tiykarlanǵan juwap berildi.",
        "uz": "AI serveri ulanmagan — qoidalarga asoslangan javob berildi.",
        "ru": "ИИ-сервер не подключён — дан ответ на основе правил.",
        "en": "AI server not connected — showing a rule-based answer.",
    },
    "ai_error": {"qq": "Qátelik júz berdi, qaytadan urınıp kóriń.", "uz": "Xatolik yuz berdi, qayta urinib ko'ring.", "ru": "Произошла ошибка, попробуйте ещё раз.", "en": "Something went wrong, please try again."},

    # ---------- report
    "report_title": {"qq": "Shań yamasa duz haqqında xabar beriń", "uz": "Chang yoki tuz haqida xabar bering", "ru": "Сообщите о пыли или соли", "en": "Report dust or salt"},
    "report_sub": {
        "qq": "Siziń xabarıńız 3 saat dawamında rayon indeksine qosıladı hám qońsılarıńızdı qorǵaydı.",
        "uz": "Sizning xabaringiz 3 soat davomida tuman indeksiga qo'shiladi va qo'shnilaringizni himoya qiladi.",
        "ru": "Ваше сообщение 3 часа учитывается в индексе района и помогает защитить соседей.",
        "en": "Your report counts toward your district's index for 3 hours and helps protect your neighbours.",
    },
    "f_district": {"qq": "Rayon", "uz": "Tuman", "ru": "Район", "en": "District"},
    "f_kind": {"qq": "Ne baqladıńız?", "uz": "Nimani kuzatdingiz?", "ru": "Что вы наблюдаете?", "en": "What do you observe?"},
    "kind_dust": {"qq": "Shań boranı", "uz": "Chang bo'roni", "ru": "Пыльная буря", "en": "Dust storm"},
    "kind_salt": {"qq": "Aq duzlı shań / duz shógindisi", "uz": "Oq tuzli chang / tuz cho'kmasi", "ru": "Белая солевая пыль / налёт", "en": "White salt dust / deposits"},
    "kind_visibility": {"qq": "Kórinis tómen", "uz": "Ko'rinish past", "ru": "Плохая видимость", "en": "Low visibility"},
    "kind_health": {"qq": "Densawlıq belgileri (jótel, kóz ashıwı)", "uz": "Sog'liq belgilari (yo'tal, ko'z achishishi)", "ru": "Симптомы (кашель, жжение глаз)", "en": "Symptoms (cough, eye irritation)"},
    "f_severity": {"qq": "Kúshi (1 — álsiz, 5 — júdá kúshli)", "uz": "Kuchi (1 — kuchsiz, 5 — juda kuchli)", "ru": "Сила (1 — слабо, 5 — очень сильно)", "en": "Intensity (1 — weak, 5 — very strong)"},
    "f_comment": {"qq": "Qosımsha (májbúriy emes)", "uz": "Qo'shimcha (ixtiyoriy)", "ru": "Комментарий (необязательно)", "en": "Comment (optional)"},
    "submit": {"qq": "Jiberiw", "uz": "Yuborish", "ru": "Отправить", "en": "Submit"},
    "report_thanks": {"qq": "Raxmet! Xabarıńız qabıl etildi hám indekske qosıldı.", "uz": "Rahmat! Xabaringiz qabul qilindi va indeksga qo'shildi.", "ru": "Спасибо! Сообщение принято и учтено в индексе.", "en": "Thank you! Your report was received and added to the index."},
    "report_error": {"qq": "Formanı tekserip shıǵıń.", "uz": "Formani tekshirib chiqing.", "ru": "Проверьте форму.", "en": "Please check the form."},
    "latest_reports": {"qq": "Sońǵı 24 saattaǵı xabarlar", "uz": "So'nggi 24 soatdagi xabarlar", "ru": "Сообщения за 24 часа", "en": "Reports in the last 24 h"},

    # ---------- dashboard
    "dash_title": {"qq": "Mákemeler ushın operativ panel", "uz": "Tashkilotlar uchun operativ panel", "ru": "Оперативная панель для ведомств", "en": "Operational dashboard for agencies"},
    "dash_sub": {
        "qq": "Hákimiyatlar, mektepler, emlewxanalar hám FVB ushın: hár rayon boyınsha házirgi qáwip hám usınılatuǵın ilajlar.",
        "uz": "Hokimliklar, maktablar, shifoxonalar va FVV uchun: har bir tuman bo'yicha joriy xavf va tavsiya etilgan choralar.",
        "ru": "Для хокимиятов, школ, больниц и МЧС: текущий риск по районам и рекомендуемые меры.",
        "en": "For local government, schools, clinics and emergency services: current risk by district and recommended actions.",
    },
    "col_district": {"qq": "Rayon", "uz": "Tuman", "ru": "Район", "en": "District"},
    "col_level": {"qq": "Dárejesi", "uz": "Darajasi", "ru": "Уровень", "en": "Level"},
    "col_peak": {"qq": "72 saat piki", "uz": "72 soat cho'qqisi", "ru": "Пик 72 ч", "en": "72 h peak"},
    "col_reports": {"qq": "Xabarlar (24s)", "uz": "Xabarlar (24s)", "ru": "Сообщ. (24ч)", "en": "Reports (24h)"},
    "col_action": {"qq": "Mektep hám emlewxana ushın ilaj", "uz": "Maktab va shifoxona uchun chora", "ru": "Меры для школ и больниц", "en": "Action for schools & clinics"},
    "act_low": {"qq": "Ádettegi rejim", "uz": "Odatiy rejim", "ru": "Обычный режим", "en": "Normal regime"},
    "act_moderate": {"qq": "Sezimtal balalar ushın sırttaǵı sabaqlardı qısqartıw", "uz": "Sezgir bolalar uchun ochiq havodagi darslarni qisqartirish", "ru": "Сократить уличные занятия для чувствительных детей", "en": "Shorten outdoor lessons for sensitive children"},
    "act_high": {"qq": "Dene tárbiyasın ishke kóshiriw, áynalardı jabıw", "uz": "Jismoniy tarbiyani ichkariga ko'chirish, derazalarni yopish", "ru": "Физкультуру — в зал, закрыть окна", "en": "Move PE indoors, keep windows closed"},
    "act_very_high": {"qq": "Sırttaǵı ilajlardı biykar etiw, maskalar, emlewxanalardı tayarlaw", "uz": "Ochiq havodagi tadbirlarni bekor qilish, niqoblar, shifoxonalarni tayyorlash", "ru": "Отменить уличные мероприятия, маски, подготовить поликлиники", "en": "Cancel outdoor events, masks, prepare clinics"},
    "act_extreme": {"qq": "Tótenshe rejim: úyde qalıw, 103 hám FVB tayarlıǵı", "uz": "Favqulodda rejim: uyda qolish, 103 va FVV tayyorgarligi", "ru": "Режим ЧС: оставаться дома, готовность 103 и МЧС", "en": "Emergency regime: stay indoors, ambulance & rescue on standby"},
    "api_note": {
        "qq": "Barlıq maǵlıwmat ashıq API arqalı da qoljetimli",
        "uz": "Barcha ma'lumotlar ochiq API orqali ham mavjud",
        "ru": "Все данные доступны и через открытый API",
        "en": "All data is also available through an open API",
    },

    # ---------- about
    "about_title": {"qq": "AralShield haqqında", "uz": "AralShield haqida", "ru": "Об AralShield", "en": "About AralShield"},
    "problem_title": {"qq": "Mashqala", "uz": "Muammo", "ru": "Проблема", "en": "The problem"},
    "problem_text": {
        "qq": "Aral teńiziniń qurıwı nátiyjesinde payda bolǵan Aralqum shólinen kóterilgen duz hám shań Qaraqalpaqstan xalqınıń densawlıǵına, awıl xojalıǵına hám turmısına tásir etedi. Biraq xalıq hám mákemeler boran haqqında aldın ala, anıq hám óz tilinde maǵlıwmat almaydı.",
        "uz": "Orol dengizining qurishi natijasida paydo bo'lgan Orolqum cho'lidan ko'tarilgan tuz va chang Qoraqalpog'iston aholisining sog'lig'iga, qishloq xo'jaligiga va hayotiga ta'sir qiladi. Ammo aholi va tashkilotlar bo'ron haqida oldindan, aniq va o'z tilida ma'lumot olmaydi.",
        "ru": "Соль и пыль, поднимаемые с пустыни Аралкум, возникшей на месте высохшего Аральского моря, влияют на здоровье жителей Каракалпакстана, сельское хозяйство и повседневную жизнь. Но люди и ведомства не получают заблаговременной, точной информации о бурях на родном языке.",
        "en": "Salt and dust lifted from the Aralkum — the desert left by the drying Aral Sea — affect the health, farming and daily life of people in Karakalpakstan. Yet residents and agencies get no advance, precise warning about storms in their own language.",
    },
    "solution_title": {"qq": "Sheshim", "uz": "Yechim", "ru": "Решение", "en": "The solution"},
    "solution_text": {
        "qq": "AralShield — veb-platforma hám Android ilovası: 17 rayon ushın hár saatlıq tiri monitoring, 72 saatlıq boljaw, Aralqum algoritmi, puqara xabarları, jeke JI másláhátshi hám mákemeler paneli. Barlıǵı tórt tilde: qaraqalpaq, ózbek, orıs hám inglis.",
        "uz": "AralShield — veb-platforma va Android ilovasi: 17 hudud uchun har soatlik jonli monitoring, 72 soatlik prognoz, Orolqum algoritmi, fuqaro xabarlari, shaxsiy AI maslahatchi va tashkilotlar paneli. Hammasi to'rt tilda: qoraqalpoq, o'zbek, rus va ingliz.",
        "ru": "AralShield — веб-платформа и Android-приложение: ежечасный живой мониторинг 17 районов, прогноз на 72 часа, алгоритм «Аралкум», сообщения жителей, персональный ИИ-советник и панель для ведомств. Всё на четырёх языках: каракалпакском, узбекском, русском и английском.",
        "en": "AralShield is a web platform and Android app: hourly live monitoring of 17 districts, a 72-hour forecast, the Aralkum algorithm, citizen reports, a personal AI adviser and an agency dashboard. All in four languages: Karakalpak, Uzbek, Russian and English.",
    },
    "innovation_title": {"qq": "Nesi innovaciyalıq", "uz": "Nimasi innovatsion", "ru": "В чём инновация", "en": "What makes it innovative"},
    "innov1": {"qq": "Datchik satıp alıwdı talap etpeydi — sputnik-model maǵlıwmatları + puqaralar «tiri datchik» retinde.", "uz": "Datchik sotib olishni talab qilmaydi — sun'iy yo'ldosh-model ma'lumotlari + fuqarolar «tirik datchik» sifatida.", "ru": "Не требует закупки датчиков — спутниково-модельные данные + жители как «живые датчики».", "en": "No sensors to buy — satellite-model data plus residents as “living sensors”."},
    "innov2": {"qq": "Aralqum sektorı hám teńizge aralıqtı esapqa alatuǵın jergilikli qáwip indeksi.", "uz": "Orolqum sektori va dengizgacha masofani hisobga oladigan mahalliy xavf indeksi.", "ru": "Локальный индекс риска, учитывающий сектор Аралкума и расстояние до бывшего моря.", "en": "A local risk index that accounts for the Aralkum wind sector and distance to the former sea."},
    "innov3": {"qq": "Qaraqalpaq tilinde sóylesetuǵın JI densawlıq másláhátshisi.", "uz": "Qoraqalpoq tilida so'zlashadigan AI sog'liq maslahatchisi.", "ru": "ИИ-советник по здоровью, говорящий на каракалпакском языке.", "en": "An AI health adviser that speaks Karakalpak."},
    "innov4": {"qq": "Mektepler hám emlewxanalar ushın tayar ilajlar.", "uz": "Maktablar va shifoxonalar uchun tayyor choralar.", "ru": "Готовые меры для школ и больниц.", "en": "Ready-made action plans for schools and clinics."},
    "innov5": {"qq": "Telefonǵa fon rejiminde avtomatik eskertiw.", "uz": "Telefonga fon rejimida avtomatik ogohlantirish.", "ru": "Автоматические фоновые оповещения на телефон.", "en": "Automatic background alerts on your phone."},
    "impact_title": {"qq": "Kútiletuǵın nátiyje", "uz": "Kutilayotgan natija", "ru": "Ожидаемый эффект", "en": "Expected impact"},
    "impact1": {"qq": "~2 mln xalıq ushın tegin erte eskertiw", "uz": "~2 mln aholi uchun bepul erta ogohlantirish", "ru": "Бесплатное раннее оповещение для ~2 млн жителей", "en": "Free early warning for ~2 million residents"},
    "impact2": {"qq": "Balalar hám astma nawqasları ushın qáwipti azaytıw", "uz": "Bolalar va astma bemorlari uchun xavfni kamaytirish", "ru": "Снижение риска для детей и людей с астмой", "en": "Lower exposure for children and people with asthma"},
    "impact3": {"qq": "Mákemeler ushın maǵlıwmatqa tiykarlanǵan qararlar", "uz": "Tashkilotlar uchun ma'lumotga asoslangan qarorlar", "ru": "Решения на основе данных для ведомств", "en": "Data-driven decisions for agencies"},
    "impact4": {"qq": "Ilimpazlar ushın ashıq maǵlıwmatlar bazası", "uz": "Olimlar uchun ochiq ma'lumotlar bazasi", "ru": "Открытая база данных для исследователей", "en": "An open dataset for researchers"},
    "roadmap_title": {"qq": "Rawajlanıw jolı", "uz": "Rivojlanish yo'li", "ru": "Дорожная карта", "en": "Roadmap"},
    "road1": {"qq": "1-basqısh: prototip — veb + Android (tayar)", "uz": "1-bosqich: prototip — veb + Android (tayyor)", "ru": "Этап 1: прототип — веб + Android (готово)", "en": "Stage 1: prototype — web + Android (done)"},
    "road2": {"qq": "2-basqısh: 10 arzan PM-datchik penen kalibrovka (Moynaq, Qońırat, Nókis)", "uz": "2-bosqich: 10 ta arzon PM-datchik bilan kalibrlash (Mo'ynoq, Qo'ng'irot, Nukus)", "ru": "Этап 2: калибровка 10 недорогими PM-датчиками (Муйнак, Кунград, Нукус)", "en": "Stage 2: calibrate with 10 low-cost PM sensors (Moynaq, Kungrad, Nukus)"},
    "road3": {"qq": "3-basqısh: Telegram-bot, SMS eskertiw, mektepler menen pilot", "uz": "3-bosqich: Telegram-bot, SMS ogohlantirish, maktablar bilan pilot", "ru": "Этап 3: Telegram-бот, SMS-оповещения, пилот со школами", "en": "Stage 3: Telegram bot, SMS alerts, school pilot"},
    "road4": {"qq": "4-basqısh: Qızılorda hám Xorezm wálayatlarına keńeytiw, ML boljaw modeli", "uz": "4-bosqich: Qizilo'rda va Xorazmga kengaytirish, ML prognoz modeli", "ru": "Этап 4: расширение на Кызылорду и Хорезм, ML-модель прогноза", "en": "Stage 4: expand to Kyzylorda and Khorezm, ML forecast model"},
    "tech_title": {"qq": "Texnologiyalar", "uz": "Texnologiyalar", "ru": "Технологии", "en": "Technology"},
    "author_title": {"qq": "Avtor", "uz": "Muallif", "ru": "Автор", "en": "Author"},
    "author_text": {
        "qq": "Ikram Xiyasov — Nókis, Qaraqalpaqstan. Programmist, NMTU oqıtıwshısı, OSIYO gumanoid robot komandası menen «Kelajak muhandislari» xalıqaralıq festival-tańlawınıń 1-orın jeńimpazı.",
        "uz": "Ikram Xiyasov — Nukus, Qoraqalpog'iston. Dasturchi, NDTU o'qituvchisi, OSIYO gumanoid robot jamoasi bilan «Kelajak muhandislari» xalqaro festival-tanlovining 1-o'rin g'olibi.",
        "ru": "Икрам Хиясов — Нукус, Каракалпакстан. Разработчик, преподаватель НГТУ, победитель (1 место) международного фестиваля-конкурса «Kelajak muhandislari» в составе команды гуманоидного робота OSIYO.",
        "en": "Ikram Xiyasov — Nukus, Karakalpakstan. Developer, lecturer at NSTU, 1st-place winner of the “Kelajak muhandislari” international festival-competition with the OSIYO humanoid robot team.",
    },

    "global_title": {"qq": "Global keńeyiw", "uz": "Global kengayish", "ru": "Глобальное масштабирование", "en": "Global scaling"},
    "global_text": {
        "qq": "BMSh Bas Assambleyası 2021-jılı Aralboyın «ekologiyalıq innovaciyalar hám texnologiyalar zonası» dep járiyaladı. Qurǵaǵan kóllerden kóterilgen shań — global mashqala: Urmiya (Iran), Solton-Si hám Ouens (AQSh), Chad kóli. AralShield motorı pútkil planetanı qamtıytuǵın Copernicus maǵlıwmatlarında isleydi — jańa regionǵa ótiw ushın tek qalalar dizimi hám «shań deregi sektorı» ózgertiledi, úskene kerek emes.",
        "uz": "BMT Bosh Assambleyasi 2021-yilda Orolbo'yini «ekologik innovatsiyalar va texnologiyalar zonasi» deb e'lon qildi. Qurigan ko'llardan ko'tarilgan chang — global muammo: Urmiya (Eron), Salton-Si va Ouens (AQSh), Chad ko'li. AralShield dvigateli butun sayyorani qamrab oluvchi Copernicus ma'lumotlarida ishlaydi — yangi hududga o'tish uchun faqat shaharlar ro'yxati va «chang manbai sektori» o'zgartiriladi, uskuna kerak emas.",
        "ru": "В 2021 году Генассамблея ООН объявила Приаралье «зоной экологических инноваций и технологий». Пыль с высыхающих озёр — глобальная проблема: Урмия (Иран), Солтон-Си и Оуэнс (США), озеро Чад. Движок AralShield работает на данных Copernicus, покрывающих всю планету: для нового региона меняются только список городов и «сектор источника пыли» — оборудование не нужно.",
        "en": "In 2021 the UN General Assembly declared the Aral Sea region a “zone of ecological innovations and technologies”. Dust from drying lakes is a global problem: Lake Urmia (Iran), the Salton Sea and Owens Lake (USA), Lake Chad. The AralShield engine runs on Copernicus data that covers the whole planet — a new region only needs a list of cities and its “dust-source sector”, no hardware.",
    },
    "global_slogan": {"qq": "Aralda tuwıldı — Jerdegi hár bir qurıp atırǵan kól ushın jaratıldı.", "uz": "Orolda tug'ildi — Yerdagi har bir qurib borayotgan ko'l uchun yaratildi.", "ru": "Рождён у Арала — создан для каждого высыхающего озера Земли.", "en": "Born at the Aral — built for every drying lake on Earth."},
    "global_path": {"qq": "Qaraqalpaqstan → Ózbekstan (Xorezm, Buxara, Nawayı) → Qızılorda → Orta Aziya → Iran, Jaqın Shıǵıs, AQSh", "uz": "Qoraqalpog'iston → O'zbekiston (Xorazm, Buxoro, Navoiy) → Qizilo'rda → Markaziy Osiyo → Eron, Yaqin Sharq, AQSh", "ru": "Каракалпакстан → Узбекистан (Хорезм, Бухара, Навои) → Кызылорда → Центральная Азия → Иран, Ближний Восток, США", "en": "Karakalpakstan → Uzbekistan (Khorezm, Bukhara, Navoi) → Kyzylorda → Central Asia → Iran, Middle East, USA"},

    # ---------- download
    "dl_title": {"qq": "AralShield Android ilovası", "uz": "AralShield Android ilovasi", "ru": "Приложение AralShield для Android", "en": "AralShield for Android"},
    "dl_text": {
        "qq": "Ilova rayonıńızdı hár 30 minutta tekseredi hám qáwip «Joqarı» dárejege jetkende eskertiw jiberedi — hátte ilova jabıq bolsa da.",
        "uz": "Ilova tumaningizni har 30 daqiqada tekshiradi va xavf «Yuqori» darajaga yetganda ogohlantirish yuboradi — hatto ilova yopiq bo'lsa ham.",
        "ru": "Приложение проверяет ваш район каждые 30 минут и присылает оповещение, когда риск достигает уровня «Высокий», — даже если приложение закрыто.",
        "en": "The app checks your district every 30 minutes and alerts you when the risk reaches “High” — even when the app is closed.",
    },
    "dl_button": {"qq": "APK faylın júklew", "uz": "APK faylini yuklash", "ru": "Скачать APK", "en": "Download APK"},
    "dl_steps": {"qq": "Ornatıw", "uz": "O'rnatish", "ru": "Установка", "en": "How to install"},
    "dl_step1": {"qq": "Joqarıdaǵı túyme arqalı APK faylın júkleń.", "uz": "Yuqoridagi tugma orqali APK faylini yuklang.", "ru": "Скачайте APK кнопкой выше.", "en": "Download the APK with the button above."},
    "dl_step2": {"qq": "Faylǵa basıń. Soralsa, «Belgisiz derekten ornatıwǵa» ruqsat beriń.", "uz": "Faylni bosing. So'ralsa, «Noma'lum manbalardan o'rnatish»ga ruxsat bering.", "ru": "Откройте файл. Если попросит — разрешите «Установку из неизвестных источников».", "en": "Open the file. If asked, allow “Install unknown apps”."},
    "dl_step3": {"qq": "Ilovanı ashıp, rayonıńızdı tańlań hám bildiriwlerge ruqsat beriń.", "uz": "Ilovani ochib, tumaningizni tanlang va bildirishnomalarga ruxsat bering.", "ru": "Откройте приложение, выберите район и разрешите уведомления.", "en": "Open the app, pick your district and allow notifications."},
    "dl_qr": {"qq": "Telefon kamerası menen skanerlań", "uz": "Telefon kamerasi bilan skanerlang", "ru": "Отсканируйте камерой телефона", "en": "Scan with your phone camera"},
    "dl_req": {"qq": "Talap: Android 8.0 hám joqarı · ~1 MB", "uz": "Talab: Android 8.0 va yuqori · ~1 MB", "ru": "Требуется Android 8.0+ · ~1 МБ", "en": "Requires Android 8.0+ · ~1 MB"},
    "dl_missing": {"qq": "APK házirshe júklenbegen — tez arada.", "uz": "APK hozircha yuklanmagan — tez orada.", "ru": "APK ещё не загружен — скоро.", "en": "APK not uploaded yet — coming soon."},

    # ---------- footer
    "footer": {
        "qq": "AralShield · «Eń innovaciyalıq ideya» tańlawı ushın prototip · Ikram Xiyasov, Nókis",
        "uz": "AralShield · «Eng innovatsion g'oya» tanlovi uchun prototip · Ikram Xiyasov, Nukus",
        "ru": "AralShield · прототип для конкурса «Самая инновационная идея» · Икрам Хиясов, Нукус",
        "en": "AralShield · prototype for the “Most Innovative Idea” contest · Ikram Xiyasov, Nukus",
    },
    "disclaimer": {
        "qq": "Indeks modellik baha bolıp tabıladı hám rásmiy meteorologiyalıq eskertiwdi almastırmaydı.",
        "uz": "Indeks modelga asoslangan baho bo'lib, rasmiy meteorologik ogohlantirish o'rnini bosmaydi.",
        "ru": "Индекс — модельная оценка и не заменяет официальные метеопредупреждения.",
        "en": "The index is a model-based estimate and does not replace official weather warnings.",
    },
}

# Rule-based advice (used when the AI service is not available)
LEVEL_ADVICE = {
    "low": {
        "qq": "Hawa ádettegidey. Sırtta júriw hám shınıǵıw qáwipsiz. Áynalardı samallatıw ushın ashıwǵa boladı.",
        "uz": "Havo odatdagidek. Tashqarida yurish va mashq qilish xavfsiz. Derazalarni shamollatish uchun ochish mumkin.",
        "ru": "Воздух в норме. Прогулки и спорт на улице безопасны. Можно проветривать помещения.",
        "en": "Air is normal. Walking and exercise outdoors are safe. You can air out your home.",
    },
    "moderate": {
        "qq": "Shań bar. Uzaq waqıt sırtta awır jumıs islewdi azaytıń, kóp suw iship turıń, úyge kirgende júzińizdi juwıń.",
        "uz": "Chang bor. Uzoq vaqt tashqarida og'ir ish qilishni kamaytiring, ko'p suv iching, uyga kirganda yuzingizni yuving.",
        "ru": "Есть пыль. Сократите длительные тяжёлые нагрузки на улице, пейте больше воды, умывайтесь, придя домой.",
        "en": "Some dust. Cut down long, heavy exertion outdoors, drink plenty of water, wash your face when you come home.",
    },
    "high": {
        "qq": "Joqarı qáwip. Sırtqa shıqsańız, FFP2/N95 maska kiyiń, kózáynek taǵıń. Áynalardı jabıń, ılǵal shúberek penen tazalań.",
        "uz": "Yuqori xavf. Tashqariga chiqsangiz, FFP2/N95 niqob taqing, ko'zoynak taqing. Derazalarni yoping, nam latta bilan tozalang.",
        "ru": "Высокий риск. Выходя на улицу, надевайте маску FFP2/N95 и очки. Закройте окна, делайте влажную уборку.",
        "en": "High risk. If you go out, wear an FFP2/N95 mask and glasses. Keep windows shut, clean with a damp cloth.",
    },
    "very_high": {
        "qq": "Júdá joqarı qáwip. Múmkinshilik bolsa úyde qalıń. Sırtta maska shárt. Esik-áynalardıń sańlaqların ılǵal shúberek penen jabıń.",
        "uz": "Juda yuqori xavf. Imkoni bo'lsa uyda qoling. Tashqarida niqob shart. Eshik-deraza tirqishlarini nam latta bilan to'sing.",
        "ru": "Очень высокий риск. По возможности оставайтесь дома. На улице — только в маске. Заложите щели окон и дверей влажной тканью.",
        "en": "Very high risk. Stay indoors if you can. Masks are a must outside. Seal gaps around doors and windows with damp cloth.",
    },
    "extreme": {
        "qq": "Tótenshe jaǵday! Úyden shıqpań. Dem qısılsa yamasa kókirek awırsa, dárhal 103 ke qońıraw etiń.",
        "uz": "Favqulodda holat! Uydan chiqmang. Nafas qisilsa yoki ko'krak og'risa, darhol 103 ga qo'ng'iroq qiling.",
        "ru": "Чрезвычайная ситуация! Не выходите из дома. При одышке или боли в груди срочно звоните 103.",
        "en": "Emergency! Do not go outside. If you have shortness of breath or chest pain, call 103 immediately.",
    },
}

GROUP_ADVICE = {
    "general": {"qq": "", "uz": "", "ru": "", "en": ""},
    "child": {
        "qq": "Balalar: sırttaǵı oyındı qısqartıń, mektepke barıwda maska taqtırıń, kóp suw beriń.",
        "uz": "Bolalar: tashqaridagi o'yinni qisqartiring, maktabga borishda niqob taqtiring, ko'p suv bering.",
        "ru": "Дети: сократите игры на улице, по дороге в школу — маска, давайте больше воды.",
        "en": "Children: shorten outdoor play, use a mask on the way to school, give plenty of water.",
    },
    "elderly": {
        "qq": "Jası úlkenler: júrek hám qan basımı dárilerin óz waqtında ishiń, sırtqa erte azanda shıǵıń.",
        "uz": "Keksalar: yurak va qon bosimi dorilarini o'z vaqtida iching, tashqariga erta tongda chiqing.",
        "ru": "Пожилым: вовремя принимайте сердечные и гипотензивные препараты, выходите рано утром.",
        "en": "Elderly: take heart and blood-pressure medicines on time, go out early in the morning.",
    },
    "asthma": {
        "qq": "Astma: ingalyatordı ózińiz benen alıp júriń, shıpaker bergen reje boyınsha háreket etiń, belgiler kúsheyse 103.",
        "uz": "Astma: ingalyatorni o'zingiz bilan olib yuring, shifokor bergan reja bo'yicha harakat qiling, belgilar kuchaysa 103.",
        "ru": "Астма: держите ингалятор при себе, следуйте плану врача, при ухудшении — 103.",
        "en": "Asthma: keep your inhaler with you, follow your doctor's action plan, call 103 if symptoms worsen.",
    },
    "pregnant": {
        "qq": "Júkli hayallar: shańlı hawada sırtta bolıwdı shekleń, úyde hawa tazalaǵıshtan paydalanıń, shıpakerge aytıń.",
        "uz": "Homiladorlar: changli havoda tashqarida bo'lishni cheklang, uyda havo tozalagichdan foydalaning, shifokorga ayting.",
        "ru": "Беременным: ограничьте пребывание на улице в пыль, используйте очиститель воздуха, сообщите врачу.",
        "en": "Pregnancy: limit time outdoors in dust, use an air purifier at home, tell your doctor.",
    },
    "outdoor": {
        "qq": "Sırtta isleytuǵınlar: FFP2 maska, kózáynek, hár saatta saya jerde dem alıw hám suw iship turıw.",
        "uz": "Ochiq havoda ishlovchilar: FFP2 niqob, ko'zoynak, har soatda soya joyda dam olish va suv ichish.",
        "ru": "Работающим на улице: маска FFP2, очки, каждый час отдых в укрытии и вода.",
        "en": "Outdoor workers: FFP2 mask, goggles, rest in shelter and drink water every hour.",
    },
}

GROUPS = ["general", "child", "elderly", "asthma", "pregnant", "outdoor"]
LANG_NAMES_EN = {"qq": "Karakalpak (Latin script)", "uz": "Uzbek (Latin script)", "ru": "Russian", "en": "English"}


def strings(lang):
    return {k: v.get(lang) or v["en"] for k, v in T.items()}
