import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

temi_7_class = ["Прямая и отрезок", "Луч", "Угол", "Сравнение отрезков и углов"
                "Перпендикулярные прямые", "Первый признак равенства треугольников",
                "Медианы, биссектрисы и высоты треугольника", "Второй признак равенства треугольников",
                "Третий признак равенства треугольника",
                "Признаки параллельности двух прямых", "Аксиома параллельных прямых", "Сумма углов треугольника",
                "Соотношения между сторонами и углами треугольника",
                "Прямоугольные треугольники", "Построение треугольника по трём элементам"
                ]
spisok_so_ssilkami_7_class = ["https://www.youtube.com/watch?v=M9OvFov68bU",
                              "https://www.youtube.com/watch?v=tHMG42KvOw0",
                              "https://www.youtube.com/watch?v=WdFIjcoVpaY",
                              "https://www.youtube.com/watch?v=9znPvQjlk4Y",
                              "https://www.youtube.com/watch?v=A8k_sULGd3M",
                              "https://www.youtube.com/watch?v=6AFXd6leO88",
                              "https://www.youtube.com/watch?v=IMQJPa41zKs",
                              "https://www.youtube.com/watch?v=ZF9Aio84eVY",
                              "https://www.youtube.com/watch?v=DA8X8i3xhdA",
                              "https://www.youtube.com/watch?v=Dat5Rzx_xqw",
                              "https://www.youtube.com/watch?v=iEr8DIUa7GU",
                              "https://www.youtube.com/watch?v=4uSIN_2qBWs",
                              "https://www.youtube.com/watch?v=Ty5s_fMJ8cA",
                              "https://www.youtube.com/watch?v=GMdepGXKKPs",
                              "https://www.youtube.com/watch?v=d8Ka4TRyJpk"]
temi_8_class = ["Многоугольники", "Параллелограмм", "Трапеция", "Прямоугольник, ромб, квадрат", "Площадь многоугольника",
                "Площадь параллелограмма", "Площадь треугольника", "Площадь трапеции", "Теорема Пифагора",
                "Определение подобных треугольников","Признаки подобия треугольников",
                "Применение подобия к доказательству теорем и решению задач",
                "Соотношения между сторонами и углами прямоугольного треугольника", "Касательная к окружности",
                "Центральные и вписанные углы", "Четыре замечательные точки треугольника",
                "Вписанная и описанная окружности"]
spisok_so_ssilkami_8_class = ["https://www.youtube.com/watch?v=8q98FplWRcw",
                              "https://www.youtube.com/watch?v=Lhae5O6qLQo",
                              "https://www.youtube.com/watch?v=lA9EDQd2CoQ",
                              "https://www.youtube.com/watch?v=Ze9OyQzpjJM",
                              "https://www.youtube.com/watch?v=RRMxp7NiyL0",
                              "https://www.youtube.com/watch?v=_22y0C6O3Ek",
                              "https://www.youtube.com/watch?v=uXld6b4C14c",
                              "https://www.youtube.com/watch?v=ocqyAPc1ZBk",
                              "https://www.youtube.com/watch?v=LrPrhe4C4q4",
                              "https://www.youtube.com/watch?v=q4759Fb5TOM",
                              "https://www.youtube.com/watch?v=JfaAs5eNGso",
                              "https://www.youtube.com/watch?v=2pBa7HHiSkE",
                              "https://www.youtube.com/watch?v=6b_olMJglXU",
                              "https://www.youtube.com/watch?v=7_nvVF2BD-I",
                              "https://www.youtube.com/watch?v=vMnT9A1DHv0",
                              "https://www.youtube.com/watch?v=FNxmkbJKL1k",
                              "https://www.youtube.com/watch?v=RvYKLg0TmE8"
                              ]
temi_9_class = ["Понятие вектора", "Сложение и вычитание векторов",
                "Умножение вектора на число. Применение векторов к решению задач" ,"Координаты вектора",
                "Простейшие задачи в координатах", "Уравнения окружности и прямой",
                "Соотношения между сторонами и углами треугольника", "Скалярное произведение векторов",
                "Правильные многоугольники", "Длина окружности и площадь круга", "Понятие движения",
                "Параллельный перенос и поворот", "Многогранники", "Тела и поверхности вращения"]
spisok_so_ssilkami_9_class = ["https://www.youtube.com/watch?v=66jnOBZKRDQ",
                              "https://www.youtube.com/watch?v=YfTaFIEXsEM",
                              "https://www.youtube.com/watch?v=Ci3BJ1PHGsA",
                              "https://www.youtube.com/watch?v=REIBpnxvBAg",
                              "https://www.youtube.com/watch?v=PK4UvaAAkDA",
                              "https://www.youtube.com/watch?v=LSRuMHkZUyM",
                              "https://www.youtube.com/watch?v=OcHU2O03gkg",
                              "https://www.youtube.com/watch?v=hx5zG-3LcCo",
                              "https://www.youtube.com/watch?v=P4g5nS1AQyI",
                              "https://www.youtube.com/watch?v=s1b-2GH5Jgg",
                              "https://www.youtube.com/watch?v=maDJlV1IVGA",
                              "https://www.youtube.com/watch?v=gpH_DcKdrfY",
                              "https://www.youtube.com/watch?v=fUqzejSJuCs",
                              "https://www.youtube.com/watch?v=IWD3VGC2rdU"
                              ]
keyboard = VkKeyboard(one_time=True)
keyboard.add_button("Документация по 7 классу", VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button("Документация по 8 классу", VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_button("Документация по 9 классу", VkKeyboardColor.NEGATIVE)


def send_message(id, message):
    if i == 1:
        vk_session.method("messages.send", {"user_id": sender,
                                            "message": message,
                                            "random_id": get_random_id(),
                                            "keyboard": keyboard.get_keyboard()})
    elif i == 2:
        vk_session.method("messages.send", {"user_id": sender,
                                            "message": message,
                                            "random_id": get_random_id(),
                                            "keyboard": keyboard.get_keyboard()})
    elif i == 3:
        vk_session.method("messages.send", {"user_id": sender,
                                            "message": message,
                                            "random_id": get_random_id(),
                                            "keyboard": keyboard.get_keyboard()})


vk_session = vk_api.VkApi(token="71219b024a51cdec8451d097a39c9aa93e3fdd8e43e2979e757c01a9736a21a5f227db502da007da9e833")
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        reseived_messange = event.text
        sender = event.user_id
        if reseived_messange == "Привет":
            i = 1
            send_message(sender, "Привет")
        elif reseived_messange == "Пока":
            i = 2
            send_message(sender, "До скорого")
        elif reseived_messange == "Документация по 7 классу":
            i = 3
            for io in range(len(spisok_so_ssilkami_7_class)):
                o = []
                tema_i_video_7_class = temi_7_class[io] + ":" + " " + spisok_so_ssilkami_7_class[io]
                o.append(tema_i_video_7_class)
                send_message(sender, o)



