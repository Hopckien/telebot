import schedule
import time
import requests
from telebot import TeleBot
from config import DTOKEN, BTOKEN


class EvoClientExample(object):
    """Dummy"""
    def __init__(self, token):
        self.token = token

    def make_request(self, url):
        """Dummy"""
        # method = self.method
        headers = {'Authorization': f'Bearer {self.token}',
                   'Content-type': 'application/json'}
        responce = requests.get(url, headers=headers, timeout = 3)
        if responce.status_code != 200:
            print('Error', responce.status_code)
        data = responce.json()

        return data

    def get_order_list(self):
        """Dummy"""
        method = 'get'
        url = 'https://my.deal.by/api/v1/orders/list?status=pending'
        return self.make_request(url)

    def get_order_received(self):
        '''Получение списка принятых заказов'''
        url = 'https://my.deal.by/api/v1/orders/list?limit=3'
        return self.make_request(url)
        

def send_timer_message(txta):
    '''Фоновый запуск задачи опроса апи deal и формирование списка заказов'''
    bot = TeleBot(BTOKEN)
    bot.send_message(chat_id=565035378,text=txta)

def receive_orders():
    """Main function"""
    # Initialize Client
    
    if not DTOKEN:
        raise Exception('Sorry, there\'s no any AUTH_TOKEN!')

    api_example = EvoClientExample(DTOKEN)

    #order_list = api_example.get_order_list()
    order_list = api_example.get_order_received()
    ###
    cnter = 0
    if not order_list['orders']:
        # raise Exception('Sorry, there\'s no any order!')
       # print(orders)
        print(time.strftime("%H:%M:%S"),   'Sorry, there\'s no any order!')
        
        print(order_list["orders"])
       #$ cnter = 0
    else:
        #zakaz=[]
        
        for i in order_list["orders"]:
            #telo =  i["client_first_name"]+i["products"][0]['name']+i["delivery_option"]["name"]
            #zakaz.append(telo)
            #print(zakaz)
            print(cnter, i["client_first_name"], i["products"][0]['name'], i["delivery_option"]["name"])
            zakaz = i["client_first_name"], i["products"][0]['name'], i["delivery_option"]["name"]

            cnter = cnter + 1
            send_timer_message(zakaz)
   # return order_list




if __name__ == '__main__':
    #orders = receive_orders()
    receive_orders()
    







schedule.every(1).minutes.do(receive_orders)
#while True:
#    schedule.run_pending()
#    time.sleep(10)

#send_timer_message()