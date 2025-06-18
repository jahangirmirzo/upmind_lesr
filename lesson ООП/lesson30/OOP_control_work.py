# Задание 1
# Класс SocialMedia: name, users, posts.
# Методы: add_user(), remove_user(), add_post(), get_feed(), get_user_count().
# Подклассы Instagram и Facebook:
# - Instagram: посты с фото (проверять формат, нельзя без фото)
# - Facebook: текстовые посты, проверка на максимальную длину текста.
# Логика: нельзя добавлять пользователей с одинаковыми username, нельзя удалить последнего админа.

# Задание 2
# Класс SmartHomeDevice: device_name, status, energy_usage, firmware_version.
# Методы: turn_on(), turn_off(), update_firmware(version), get_status(), reset().
# Подклассы Thermostat и SecurityCamera:
# - Камера записывает только при достаточном освещении
# - Термостат требует предварительной калибровки
# Логика: нельзя обновлять прошивку, если устройство включено.

# Задание 3
# Класс DeliveryService: company, vehicles, orders, completed_orders.
# Методы: add_order(), dispatch_order(), track_order(), calculate_delivery_time(), summary().
# FoodDelivery: проверка на горячие/холодные блюда (разное время доставки).
# CourierDelivery: разные классы посылок (обычные, ценные).
# Логика: нельзя отправить заказ, если водитель уже занят.

# Задание 4
# Класс FitnessApp: name, users, workouts, challenges.
# Методы: add_workout(), remove_workout(), track_progress(), get_user_stats(), leaderboard().
# YogaApp: фиксирует выполнение асан.
# RunningApp: учитывает пройденное расстояние и калории.
# Логика: прогресс сохраняется только для зарегистрированных пользователей.

# Задание 5
# Класс ECommerceSite: name, products, users, carts.
# Методы: add_product(), search_product(), add_to_cart(user), checkout(user), get_sales_report().
# FashionStore: одежда проверяет размер и наличие.
# ElectronicsStore: проверка гарантии, запрет продажи бракованного товара.
# Логика: скидки считаются только при сумме корзины > 1000.

# Задание 6
# Класс Bank: name, accounts, total_balance, overdraft_limit.
# Методы: create_account(), deposit(), withdraw(), transfer(), get_summary().
# SavingsBank: запрет перевода, если баланс < 0.
# InvestmentBank: учёт комиссии при переводе.
# Логика: нельзя открыть второй аккаунт с тем же ID.

# Задание 7
# Класс StreamingService: name, content, subscribers, ratings.
# Методы: add_content(), remove_content(), play(), rate_content(), get_recommendations().
# Netflix: сериал нельзя начать с середины, если не смотрел первые серии.
# Spotify: рейтинг трека меняется от прослушивания.
# Логика: подписчик с низким рейтингом контента — контент скрывается.

# Задание 8
# Класс School: name, students, teachers, schedule.
# Методы: add_student(), add_teacher(), schedule_lesson(), get_statistics(), expel_student().
# PrimarySchool: не более 5 уроков в день.
# HighSchool: проверка наличия лабораторных занятий.
# Логика: ученик не может быть удалён, если у него есть незавершённые проекты.

# Задание 9
# Класс Transportation: type, capacity, routes, current_passengers.
# Методы: add_route(), remove_route(), board_passenger(), start_service(), stop_service().
# Bus: проверка билетов перед посадкой.
# Train: разные классы вагонов (1-й и 2-й).
# Логика: нельзя посадить пассажира без билета или если превышен capacity.

# Задание 10
# Класс Hotel: name, rooms, guests, bookings.
# Методы: book_room(), check_in(), check_out(), get_available_rooms(), generate_invoice().
# BoutiqueHotel: подарки для гостей при заселении.
# ResortHotel: туристический сбор.
# Логика: нельзя отменить бронирование за день до заселения без штрафа.

# Задание 11
# Класс Marketplace: name, sellers, buyers, active_products.
# Методы: register_seller(), register_buyer(), list_product(), buy_product(), get_market_stats().
# FarmerMarket: товар — только еда и растения.
# ArtMarket: проверка подлинности (уникальность продукта).
# Логика: один продавец не может продавать больше 100 товаров.

# Задание 12
# Класс NewsWebsite: name, articles, authors, categories.
# Методы: add_article(), remove_article(), search_articles(), get_top_authors(), get_analytics().
# TechNews: проверка достоверности фактов.
# SportsNews: сортировка статей по актуальности матчей.
# Логика: нельзя публиковать статью без проверки редактором.

# Задание 13
# Класс FlightBookingSystem: name, flights, passengers, taxes.
# Методы: add_flight(), book_ticket(), cancel_ticket(), check_status(), calculate_revenue().
# DomesticFlight: внутренние рейсы — местные налоги.
# InternationalFlight: загран — визовые сборы.
# Логика: нельзя забронировать место, если нет визы (для международного рейса).

# Задание 14
# Класс OnlineCourse: name, students, lessons, assignments.
# Методы: add_lesson(), remove_lesson(), enroll_student(), complete_lesson(), get_progress().
# ProgrammingCourse: обязательная сдача заданий.
# LanguageCourse: тесты после каждого урока.
# Логика: нельзя пройти итоговый тест без прохождения всех уроков.

# Задание 15
# Класс GamingPlatform: name, players, games, leaderboards.
# Методы: add_game(), remove_game(), play_game(), update_leaderboard(), get_total_playtime().
# PCGaming: бонус за длительные сессии.
# MobileGaming: лимит времени игры (анти-зависимость).
# Логика: в leaderboard попадают только активные игроки за последние 7 дней.

# Задание 16
# Класс Cinema: name, movies, viewers, tickets_sold.
# Методы: add_movie(), remove_movie(), sell_ticket(), get_movie_stats(), daily_report().
# IndieCinema: дополнительная скидка при повторном просмотре.
# MultiplexCinema: разные цены на сеанс в зависимости от времени.
# Логика: нельзя продать билет, если у фильма рейтинг < 3.

# Задание 17
# Класс Restaurant: name, menu, orders, reviews.
# Методы: add_dish(), remove_dish(), place_order(), calculate_bill(), get_popular_dishes().
# FastFood: скидки на большие заказы.
# GourmetRestaurant: сервисный сбор.
# Логика: нельзя заказать блюдо, если оно закончилось (остаток).

# Задание 18
# Класс Library: name, books, members, late_returns.
# Методы: add_book(), lend_book(), return_book(), search_book(), get_stats().
# PublicLibrary: бесплатная выдача.
# UniversityLibrary: плата за просрочку.
# Логика: член с долгами не может взять книгу.

# Задание 19
# Класс Pet: name, species, owner, health.
# Методы: feed(), play(), sleep(), get_info(), visit_vet().
# DogPet: игра восстанавливает здоровье.
# CatPet: больше спит — больше довольство.
# Логика: здоровье ухудшается без игр и еды, визит к ветеринару восстанавливает здоровье.

# Задание 20
# Класс Portfolio: owner, investments, total_value, risk_profile.
# Методы: add_investment(), remove_investment(), calculate_value(), rebalance(), summary().
# StockPortfolio: медленный рост, низкий риск.
# CryptoPortfolio: быстрые колебания, высокий риск.
# Логика: нельзя добавить инвестицию, если она превышает лимит по риску (risk_profile).

