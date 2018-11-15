import telegram
from yaml import load

from binotel import CallStats

with open('config.yaml', 'r') as f:
    config = load(f)

token = config['token']     # Токен вашего бота
KEY = config['KEY']
SECRET = config['SECRET']
login = config['login']
passwd = config['passwd']
profile_id = config['profile_id']    # Профайл вашего представления в GA

# Кому будем слать сообщения. Достаём по ссылке - https://api.telegram.org/bot<Bot_token>/getUpdates
chat_ids = config['id'].split(',')

bot = telegram.Bot(token)

calls = CallStats(KEY, SECRET)
in_call, in_new_call = calls.incoming_calls()
out_call = calls.outgoing_calls()
get_call, get_call_new = calls.get_call(login, passwd)

in_call = in_call + get_call
in_new_call = in_new_call + get_call_new
google_data = calls.google_visits(profile_id)

text = f"""
Входящие звонки за вчера:
Всего - {in_call}
Новых - {in_new_call}
Исходящие звонки за вчера:
Всего - {out_call}

Посещаемость сайта за вчера:
Визитов - {google_data[0]}
Просмотрено страниц - {google_data[1]}
Достигнуто целей - {google_data[2]}
*********************************
"""

for chat_id in chat_ids:
    bot.sendMessage(chat_id=chat_id, text=text)

print('Сообщение отправилось на следующие id:', chat_ids)


# for last_update in bot.getUpdates():
#     chat_id = last_update.message.chat.id
#     print(chat_id)
#     bot.sendMessage(chat_id=chat_id, text=text)
