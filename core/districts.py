# Districts and cities of the Republic of Karakalpakstan.
# Coordinates are district centres (approximate); population is an approximate figure
# used only for the "people in risk zone" estimate.
# (slug, qq, uz, ru, en, lat, lon, population, km_to_aralkum)
DISTRICTS = [
    ("nukus", "Nókis qalası", "Nukus shahri", "г. Нукус", "Nukus city", 42.4600, 59.6100, 330000, 230),
    ("moynaq", "Moynaq", "Mo'ynoq", "Муйнак", "Moynaq", 43.7683, 59.0214, 33000, 20),
    ("kungrad", "Qońırat", "Qo'ng'irot", "Кунград", "Kungrad", 43.0758, 58.9006, 130000, 120),
    ("kanlykul", "Qanlıkól", "Qanliko'l", "Канлыкуль", "Kanlykul", 42.8300, 59.0000, 50000, 160),
    ("shumanay", "Shomanay", "Shumanay", "Шуманай", "Shumanay", 42.7144, 58.9234, 60000, 170),
    ("takhtakupir", "Taxtakópir", "Taxtako'pir", "Тахтакупыр", "Takhtakupir", 43.0167, 60.3667, 45000, 160),
    ("karauzyak", "Qaraózek", "Qorao'zak", "Караузяк", "Karauzyak", 43.0300, 60.0200, 55000, 170),
    ("chimbay", "Shımbay", "Chimboy", "Чимбай", "Chimbay", 42.9311, 59.7708, 120000, 180),
    ("kegeyli", "Kegeyli", "Kegeyli", "Кегейли", "Kegeyli", 42.7764, 59.6078, 90000, 190),
    ("bozatau", "Bozataw", "Bo'zatov", "Бозатау", "Bozatau", 42.9100, 59.4000, 20000, 160),
    ("nukus-district", "Nókis rayonı", "Nukus tumani", "Нукусский район", "Nukus district", 42.6200, 59.7300, 55000, 220),
    ("khojeli", "Xojeli", "Xo'jayli", "Ходжейли", "Khojeli", 42.4047, 59.4517, 200000, 240),
    ("takhiatash", "Taqıyatas", "Taxiatosh", "Тахиаташ", "Takhiatash", 42.3200, 59.5800, 80000, 250),
    ("amudarya", "Ámiwdárya", "Amudaryo", "Амударья", "Amudarya", 42.1167, 60.0583, 200000, 290),
    ("beruniy", "Beruniy", "Beruniy", "Беруни", "Beruniy", 41.6911, 60.7525, 190000, 330),
    ("ellikkala", "Ellikqala", "Ellikqal'a", "Элликкала", "Ellikkala", 41.8460, 60.9300, 160000, 340),
    ("turtkul", "Tórtkúl", "To'rtko'l", "Турткуль", "Turtkul", 41.5500, 61.0000, 210000, 380),
]


def seed_districts():
    from .models import District

    for i, (slug, qq, uz, ru, en, lat, lon, pop, km) in enumerate(DISTRICTS):
        District.objects.update_or_create(
            slug=slug,
            defaults=dict(
                name_qq=qq, name_uz=uz, name_ru=ru, name_en=en,
                lat=lat, lon=lon, population=pop, distance_to_aralkum_km=km, order=i,
            ),
        )
    return District.objects.count()
