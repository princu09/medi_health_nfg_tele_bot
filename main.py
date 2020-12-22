import requests

api = 'https://api.telegram.org/bot1301919835:AAFO8U4N4m2g1AwRv5YPseeXCCrfhXzw1S0/'

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
    response = requests.post(api + "sendMessage" , data=params)
    return response


# create main function for nevigate or reply message back
def main():
    update_id = last_update(api)['update_id']
    while True:
        update = last_update(api)
        if update_id == update['update_id']:
            if get_message_text(update).lower() == "/hello":
                send_message(get_chat_id(update), "Welcome To Medi Health NFG")
            elif get_message_text(update).lower() == "/about":
                send_message(get_chat_id(update), "NorthFoxGroup \n Owner : Prince Patel \n Telegram : @NorthFoxGroup")
                
            update_id += 1

main()