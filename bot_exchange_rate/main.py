import telebot

from config import TOKEN
from config import keys
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать работу введите команду боту в следующем формате: \n<b>Количество Валюта№1 Валюта№2 </b> \n\n'
            'Например: <pre>1 Биткоин Доллар</pre> \nУвидеть список всех доступных валют: /values')
    bot.reply_to(message, text, parse_mode='HTML')


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionException('Слишком много параметров')

        amount, quote, base = values
        total_base = CryptoConverter.get_price(amount, quote, base)
    except ConvertionException as e:
        bot.reply_to(message, f'<b>Ошибка пользователя:</b> {e}', parse_mode='HTML')
    except Exception as e:
        bot.reply_to(message, f'<b>Не удалось обработать команду:</b> {e}', parse_mode='HTML')
    else:
        text = f'Цена {amount} {quote.title()} в {base.title()} - {total_base}'
        bot.send_message(message.chat.id, text, parse_mode='HTML')


bot.polling()
