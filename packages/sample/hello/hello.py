import requests
import time

def sendSignal(SIGNAL_MESSAGE):
    base_url = 'https://api.telegram.org/bot5574070283:AAEwwDxoG6dCtSKgO7E59ZCxXymhgB9Tx2o/sendMessage?chat_id=-722668052&text={}'.format(SIGNAL_MESSAGE)
    requests.get(base_url) 
    print(SIGNAL_MESSAGE)

def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!"
      print(greeting)
      
      while 1:
            sendSignal("YELDA")
            time.sleep(3)
            
      return {"body": greeting}
  