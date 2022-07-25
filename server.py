import requests

def sendSignal(SIGNAL_MESSAGE):
    base_url = 'https://api.telegram.org/bot5574070283:AAEwwDxoG6dCtSKgO7E59ZCxXymhgB9Tx2o/sendMessage?chat_id=-722668052&text={}'.format(SIGNAL_MESSAGE)
    requests.get(base_url) 
    print(SIGNAL_MESSAGE)


sendSignal('Deneme')
