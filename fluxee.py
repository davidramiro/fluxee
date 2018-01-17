from bottle import run, post, request
from yeelight import Bulb
import configparser

@post('/room_1')
def room_handler():
    post_dict = request.query.decode()
    if 'ct' in post_dict and 'bri' in post_dict:
        ct = int(post_dict['ct'])
        bri = int(float(post_dict['bri']) * 100)

        bulb.set_color_temp(ct)
        print('Color temperature set to %s' % ct)
        bulb.set_brightness(bri)
        print('Brightness set to %s' % (bri))

config = configparser.ConfigParser()
config.read('config.ini')
address = config.get('config','ip')

print('Initializing Yeelight')
bulb = Bulb(address)
run(host='127.0.0.1', port=8080)