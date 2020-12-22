import requests
from telegram import ParseMode

url = '1493323704:AAHuLjTwMhY-KYm0mvQWoM6PUq9mR5VB7Zk'
api = f'https://api.telegram.org/bot{url}/'


# create function that get chat id
def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


# create function that get message text
def get_message_text(update):
    message_text = update['message']['text']
    return message_text


# create function that get last update
def last_update(req):
    response = requests.get(req + 'getUpdates')
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(chat_id, message_text):
    params = {'chat_id': chat_id, "text": message_text}
    response = requests.post(api + "sendMessage", data=params)
    print(response.status_code)
    return response


def send_image(chat_id, caption):
    files = {"photo": open('logo.png', 'rb')}
    params = {'chat_id': chat_id, "caption": caption}
    response = requests.post(api + "sendPhoto" , data=params, files=files)
    print(response.status_code)
    return response


# create main function for nevigate or reply message back
def main():
    update_id = last_update(api)['update_id']
    while True:
        update = last_update(api)
        if update_id == update['update_id']:

            if get_message_text(update).lower() == "/start":
                first_name = last_update(api)['message']['from']['first_name']
                send_message(get_chat_id(
                    update), f"Hello {first_name} !! Welcome To Medi Health NFG")

            if get_message_text(update).lower() == "/about":
                send_caption = 'About NFG ℹ️: \n\nThis is a bot built by Python developer of Northfox Group and this bot is for sending every bill and new information to every customer of Medi Health NFG. \n\nIf you also want this software, you can contact us directly.<a href="#">Hello</a>'
                send_image(get_chat_id(update), send_caption)

            update_id += 1


main()