import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot('ТОКЕН СЮДА')
url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
answer = json.loads(response.text)
w = {}

def test_otsl(message):
    bot.send_message(message.chat.id, "Статистика по вашим избранным валютам")
    try:
        for i in range(len(w[int(message.chat.id)])):
            res = w[int(message.chat.id)][i]
            if answer["Valute"][res]["Value"] >= answer["Valute"][res]["Previous"]:
                res += "\U0001F7E9"
            else:
                res += "\U0001F7E5"
            bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, "Никакая из валют не отслеживается")
def prognoz(message):
    res = "На данный момент доступен только ручной прогноз от аналитиков"
    res += "\U0001F60E:"
    bot.send_message(message.chat.id, res)
    bot.send_message(message.chat.id, "Советуем к покупке: USD")
    keyboard3 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="investing.com", url="https://ru.investing.com/currencies/usd-rub-chart")
    keyboard3.add(url_button)
    bot.send_message(message.chat.id, "Источники:", reply_markup=keyboard3)

def place_for_buy_currency(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="investing.com", url="https://ru.investing.com")
    url_button0 = types.InlineKeyboardButton(text="banki.ru", url="https://www.banki.ru/products/currency/cash/moskva/")
    url_button00 = types.InlineKeyboardButton(text="broker.ru", url="https://broker.ru/promo/currency8/?refid=11476&utm_source=google&utm_medium=cpc&utm_campaign=767305818~Broker_Currency_RF_Poisk&utm_content=39948041946~kwd-30793872212~511201698404~c~9047028~~&gclid=Cj0KCQjwsqmEBhDiARIsANV8H3bLVfe-lhirVeiXFx1tdBSyC2_puKeoPEyd1IDvoGUkBgUYM48FHSIaAqhWEALw_wcB")
    keyboard.add(url_button, url_button0, url_button00)
    bot.send_message(message.chat.id, "Валюту вы можете приобрести на данный сайтах:", reply_markup=keyboard)



def spisok_valute(message):
    try:
        for i in range(len(w[int(message.chat.id)])):
            bot.send_message(message.chat.id, w[int(message.chat.id)][i])
        if len(w[int(message.chat.id)]) == 0:
            bot.send_message(message.chat.id, "Никакая из валют не отслеживается")
    except:
        bot.send_message(message.chat.id, "Никакая из валют не отслеживается")


def actualcurrency(message):
    #print(answer["AUD"]["Name"])
    tmp = 'Актуальные курсы на сегодня: \n'
    for i in answer["Valute"]:
        tmp00 = abs(answer["Valute"][i]["Value"] - answer["Valute"][i]["Previous"])
        tmp0 = f"{tmp00:.{3}f}"
        if answer["Valute"][i]["Value"] > answer["Valute"][i]["Previous"]:
            tmp += str(
                "{}{}({})  = {} ({}{}) \n ".format("\U0001F7E9", i,answer["Valute"][i]["Name"], answer["Valute"][i]["Value"], "\U00002B06", tmp0))
        elif answer["Valute"][i]["Value"] < answer["Valute"][i]["Previous"]:
            tmp += str("{}{}({})  = {} ({}{}) \n ".format("\U0001F7E5", i, answer["Valute"][i]["Name"], answer["Valute"][i]["Value"],"\U00002B07",tmp0))
        else:
            tmp += str("{}  = {} (не изменился)\n ".format(i, answer["Valute"][i]["Value"]))
    bot.send_message(message.chat.id, tmp)


def otsl_valute(message, valute_actual):
    x = int(message.chat.id)
    y = valute_actual
    try:
        if y in w[x]:
            w[x].remove(y)
            res = "\U0000274C"
            res += "Валюта успешно удалена из отслеживания!"
            bot.send_message(message.chat.id, res)
        else:
            w[x] += [y]
            res = "\U00002705"
            res += "Валюта успешно добавлена для отслеживания!"
            bot.send_message(message.chat.id, res)
    except:
        w[x] = [y]
        res = "\U00002705"
        res += "Валюта успешно добавлена для отслеживания!"
        bot.send_message(message.chat.id, res)
    print(w)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "/menu - для отображения меню")


@bot.message_handler(commands=["menu"])
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_actual_currency = types.KeyboardButton(text="Посмотреть актуальные курсы", )
    button_buy_currency = types.KeyboardButton(text="Приобрести валюту", )
    button_otsl_valute = types.KeyboardButton(text="Отслеживать конкретную валюту", )
    button_test = types.KeyboardButton(text="Тест", )
    button_prognoz = types.KeyboardButton(text="Прогноз", )
    button_spisok_otsl_valute = types.KeyboardButton(text="Посмотреть список отслеживаемых валют", )
    keyboard.add(button_actual_currency, button_buy_currency,button_prognoz, button_otsl_valute, button_spisok_otsl_valute,button_test)
    bot.send_message(message.chat.id, "Выберите:", reply_markup=keyboard)


@bot.message_handler(commands=["currency"])
def currency(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False)
    button_valute_000 = types.KeyboardButton(text="AUD", )
    button_valute_001 = types.KeyboardButton(text="AZN", )
    button_valute_002 = types.KeyboardButton(text="GBP", )
    button_valute_003 = types.KeyboardButton(text="AMD", )
    button_valute_004 = types.KeyboardButton(text="BYN", )
    button_valute_005 = types.KeyboardButton(text="BGN", )
    button_valute_006 = types.KeyboardButton(text="BRL", )
    button_valute_007 = types.KeyboardButton(text="HUF", )
    button_valute_008 = types.KeyboardButton(text="HKD", )
    button_valute_009 = types.KeyboardButton(text="DKK", )
    button_valute_010 = types.KeyboardButton(text="USD", )
    button_valute_011 = types.KeyboardButton(text="EUR", )
    button_valute_012 = types.KeyboardButton(text="INR", )
    button_valute_013 = types.KeyboardButton(text="KZT", )
    button_valute_014 = types.KeyboardButton(text="CAD", )
    button_valute_015 = types.KeyboardButton(text="KGS", )
    button_valute_016 = types.KeyboardButton(text="CNY", )
    button_valute_017 = types.KeyboardButton(text="MDL", )
    button_valute_018 = types.KeyboardButton(text="NOK", )
    button_valute_019 = types.KeyboardButton(text="PLN", )
    button_valute_020 = types.KeyboardButton(text="RON", )
    button_valute_021 = types.KeyboardButton(text="XDR", )
    button_valute_022 = types.KeyboardButton(text="SGD", )
    button_valute_023 = types.KeyboardButton(text="TJS", )
    button_valute_024 = types.KeyboardButton(text="TRY", )
    button_valute_025 = types.KeyboardButton(text="TMT", )
    button_valute_026 = types.KeyboardButton(text="UZS", )
    button_valute_027 = types.KeyboardButton(text="UAH", )
    button_valute_028 = types.KeyboardButton(text="CZK", )
    button_valute_029 = types.KeyboardButton(text="SEK", )
    button_valute_030 = types.KeyboardButton(text="CHF", )
    button_valute_031 = types.KeyboardButton(text="ZAR", )
    button_valute_032 = types.KeyboardButton(text="KRW", )
    button_valute_032 = types.KeyboardButton(text="JPY", )
    button_exit = types.KeyboardButton(text="Назад")
    keyboard.add(button_valute_000, button_valute_001, button_valute_002, button_valute_003, button_valute_004,
                 button_valute_005, button_valute_006, button_valute_007, button_valute_008, button_valute_009,
                 button_valute_010, button_valute_011, button_valute_012, button_valute_013, button_valute_014,
                 button_valute_015, button_valute_016, button_valute_017, button_valute_018, button_valute_019,
                 button_valute_020, button_valute_021, button_valute_022, button_valute_023, button_valute_024,
                 button_valute_025, button_valute_026, button_valute_027, button_valute_028, button_valute_029,
                 button_valute_030, button_valute_031, button_valute_032, button_exit)
    bot.send_message(message.chat.id, "Выберите:", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Посмотреть актуальные курсы":
        actualcurrency(message)
    elif message.text == "Приобрести валюту":
        place_for_buy_currency(message)
    elif message.text == "Отслеживать конкретную валюту":
        currency(message)
    elif message.text == "Прогноз":
        prognoz(message)
    elif message.text == "Тест":
        test_otsl(message)
    elif message.text == "AUD":
        otsl_valute(message, "AUD")
    elif message.text == "AZN":
        otsl_valute(message, "AZN")
    elif message.text == "GBP":
        otsl_valute(message, "GBP")
    elif message.text == "AMD":
        otsl_valute(message, "AMD")
    elif message.text == "BYN":
        otsl_valute(message, "BYN")
    elif message.text == "BGN":
        otsl_valute(message, "BGN")
    elif message.text == "BRL":
        otsl_valute(message, "BRL")
    elif message.text == "HUF":
        otsl_valute(message, "HUF")
    elif message.text == "HKD":
        otsl_valute(message, "HKD")
    elif message.text == "DKK":
        otsl_valute(message, "DKK")
    elif message.text == "USD":
        otsl_valute(message, "USD")
    elif message.text == "EUR":
        otsl_valute(message, "EUR")
    elif message.text == "INR":
        otsl_valute(message, "INR")
    elif message.text == "KZT":
        otsl_valute(message, "KZT")
    elif message.text == "CAD":
        otsl_valute(message, "CAD")
    elif message.text == "KGS":
        otsl_valute(message, "KGS")
    elif message.text == "CNY":
        otsl_valute(message, "CNY")
    elif message.text == "MDL":
        otsl_valute(message, "MDL")
    elif message.text == "NOK":
        otsl_valute(message, "NOK")
    elif message.text == "PLN":
        otsl_valute(message, "PLN")
    elif message.text == "RON":
        otsl_valute(message, "RON")
    elif message.text == "XDR":
        otsl_valute(message, "XDR")
    elif message.text == "SGD":
        otsl_valute(message, "SGD")
    elif message.text == "TJS":
        otsl_valute(message, "TJS")
    elif message.text == "TRY":
        otsl_valute(message, "TRY")
    elif message.text == "TMT":
        otsl_valute(message, "TMT")
    elif message.text == "UZS":
        otsl_valute(message, "UZS")
    elif message.text == "UAH":
        otsl_valute(message, "UAH")
    elif message.text == "CZK":
        otsl_valute(message, "CZK")
    elif message.text == "SEK":
        otsl_valute(message, "SEK")
    elif message.text == "CHF":
        otsl_valute(message, "CHF")
    elif message.text == "ZAR":
        otsl_valute(message, "ZAR")
    elif message.text == "KRW":
        otsl_valute(message, "KRW")
    elif message.text == "JPY":
        otsl_valute(message, "JPY")
    elif message.text == "Назад":
        menu(message)
    elif message.text == "Посмотреть список отслеживаемых валют":
        spisok_valute(message)


if __name__ == '__main__':
    while 1:
        try:
            bot.polling(none_stop=True)
        except:
            pass

