import telebot
import os

from telebot import types

bot = telebot.TeleBot("6395318526:AAE-x7EqHToBKILDRKx2peFpncuCHRlmF4E")


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    card_mod = types.InlineKeyboardButton('Карта 🇺🇦', callback_data='card')
    crypt_mod = types.InlineKeyboardButton('Крипта 🏵', callback_data='crypt')
    paypal_mod = types.InlineKeyboardButton('PayPal 💰', callback_data='paypal')

    markup.add(card_mod, crypt_mod, paypal_mod)

    bot.send_message(message.chat.id,
                     'Привет👋! Тут ты можешь приобрести самую лучшую приватку во всем телеграме!✈️🏆 Весь материал заливаю прям в Telegram, никаких облачных хранилищ☁️ есть возможность скачивать весь материал✔️. Уже куплено 155 красивых девушек с Onlyfans🔥📷. Регулярные обновления контента👾 + покупаю эксклюзивный  контент моделей по 300 долларов💰 (видео с мастурбаци*й 🙈🔥). Так же после оплаты "подписки НАВСЕГДА♾️" вы можете предлагать своих  12 моделей с Onlyfans, буду их покупать и заливать в приватный канал😉')

    bot.send_message(message.chat.id,
                     'Список моделей в привате 👇\n'
                     'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                     'Выберите способ оплаты 👇',
                     reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        from pathlib import Path
        Path(f'files/').mkdir(parents=True, exist_ok=True)

        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = f'files/' + file_info.file_path.replace('photos/', '')
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.send_photo(chat_id='-920033082', photo=open('files/' + file_info.file_path.split('/')[1] , 'rb'), caption=f'@{message.from_user.username}')
        file_path = 'files/' + file_info.file_path.split('/')[1]
        os.remove(file_path)

    except Exception as e:
        print(repr(e))


user = {
    'id': [],
    'name': []
}


@bot.callback_query_handler(func=lambda message: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'one':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           '1 месяц 400грн🇺🇦')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, '5375411424984172')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'three':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           '3 месяца 900грн🇺🇦')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, '5375411424984172')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'six':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           '6 месяцев 1600грн🇺🇦')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, '5375411424984172')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'all':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           'НАВСЕГДА 3000грн🇺🇦')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, '5375411424984172')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'card':
                markup = types.InlineKeyboardMarkup(row_width=2)

                one_month = types.InlineKeyboardButton('1 месяц 400грн🇺🇦', callback_data='one')
                three_month = types.InlineKeyboardButton('3 месяца 900грн🇺🇦', callback_data='three')
                six_month = types.InlineKeyboardButton('6 месяцев 1600грн🇺🇦', callback_data='six')
                all_month = types.InlineKeyboardButton('НАВСЕГДА 3000грн🇺🇦', callback_data='all')

                markup.add(one_month, three_month, six_month, all_month)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n')
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id,
                                              reply_markup=markup)
            elif call.data == 'crypt':
                markup = types.InlineKeyboardMarkup(row_width=2)

                one_month = types.InlineKeyboardButton('1 месяц 10$ usdt🏵', callback_data='one_crypt')
                three_month = types.InlineKeyboardButton('3 месяца 25$ usdt🏵', callback_data='three_crypt')
                six_month = types.InlineKeyboardButton('6 месяцев 45$ usdt🏵', callback_data='six_crypt')
                all_month = types.InlineKeyboardButton('НАВСЕГДА 85$ usdt🏵', callback_data='all_crypt')

                markup.add(one_month, three_month, six_month, all_month)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n')
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id,
                                              reply_markup=markup)
            elif call.data == 'paypal':
                markup = types.InlineKeyboardMarkup(row_width=2)

                one_month = types.InlineKeyboardButton('1 месяц 10$ usd💰', callback_data='one_paypal')
                three_month = types.InlineKeyboardButton('3 месяца 25$ usd💰', callback_data='three_paypal')
                six_month = types.InlineKeyboardButton('6 месяцев 45$ usd💰', callback_data='six_paypal')
                all_month = types.InlineKeyboardButton('НАВСЕГДА 85$ usd💰', callback_data='all_paypal')

                markup.add(one_month, three_month, six_month, all_month)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n')
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id,
                                              reply_markup=markup)
            elif call.data == 'one_crypt':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           '1 месяц 10$ usdt🏵')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, 'КАШЕЛЕК В USDT!!!')
                bot.send_message(call.message.chat.id, 'TGfr6APJzf4KRLLhyr4d74gm8yJJMEPd1C')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'three_crypt':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           '3 месяца 25$ usdt🏵')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, 'КАШЕЛЕК В USDT!!!')
                bot.send_message(call.message.chat.id, 'TGfr6APJzf4KRLLhyr4d74gm8yJJMEPd1C')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'six_crypt':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           '6 месяцев 45$ usdt🏵')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, 'КАШЕЛЕК В USDT!!!')
                bot.send_message(call.message.chat.id, 'TGfr6APJzf4KRLLhyr4d74gm8yJJMEPd1C')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'all_crypt':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           'НАВСЕГДА 85$ usdt🏵')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, 'КАШЕЛЕК В USDT!!!')
                bot.send_message(call.message.chat.id,  'TGfr6APJzf4KRLLhyr4d74gm8yJJMEPd1C')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'one_paypal':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           '1 месяц 10$ usd💰')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, 'КАШЕЛЕК: sadowperchik@gmail.com')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'three_paypal':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           '3 месяца 25$ usd💰')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, 'КАШЕЛЕК: sadowperchik@gmail.com')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'six_paypal':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           '6 месяцев 45$ usd💰')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, 'КАШЕЛЕК: sadowperchik@gmail.com')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'all_paypal':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='Список моделей в привате 👇\n'
                                           'https://t.me/+OxOnzXm9yaM3YzRi\n\n'
                                           'Выбирете подписку 👇\n\n'
                                           'НАВСЕГДА 85$ usd💰')
                markup = types.InlineKeyboardMarkup(row_width=2)

                payed = types.InlineKeyboardButton('Я Оплатил 👾', callback_data='pay')
                back = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')

                markup.add(payed, back)

                bot.send_message(call.message.chat.id, 'КАШЕЛЕК: sadowperchik@gmail.com')
                bot.send_message(call.message.chat.id,
                                 'ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!',
                                 reply_markup=markup)
            elif call.data == 'pay':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!\n\n'
                                           'Я Оплатил 👾')
                bot.send_message(call.message.chat.id, f'🟢5% пойдет на поддержку ЗСУ🟢\n\n'
                                                       f'🇺🇦Слава Україні🇺🇦')

                user['id'].append(call.from_user.id)
                user['name'].append('@'+call.from_user.username)

                markup = types.InlineKeyboardMarkup(row_width=1)

                accept = types.InlineKeyboardButton('Принять ❓', callback_data='accept')

                markup.add(accept)

                bot.send_message('-920033082',
                                 f'Пользователь @{call.from_user.username} подтвердил оплату',
                                 reply_markup=markup)
            elif call.data == 'back':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text='ВАЖНО! ПОСЛЕ ОПЛАТЫ НАЖМИТЕ - Я ОПЛАТИЛ, И ОТПРАВЬТЕ СКРИНШОТ ОПЛАТЫ В БОТА!!!\n\n'
                                           'Назад ⬅️')

                welcome(call.message)
            elif call.data == 'accept':
                user_name = call.message.text.split()[1]

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=f'{call.message.text}\n\n'
                                           f'Принять ❓')

                bot.send_message(user['id'][user['name'].index(user_name)], 'Ты принят\n\n'
                                                                            'https://t.me/+0usKUCCWU8FiN2My')

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
