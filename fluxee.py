from bottle import run, post, request
from yeelight import Bulb
import configparser

@post('/room_1')
def room_handler():
    post_dict = request.query.decode()
    if 'ct' in post_dict and 'bri' in post_dict:
        ct = int(post_dict['ct'])
        bri = int(float(post_dict['bri']) * 100)
        
        if lamps >= '1':
            print('Setting first lamp...')
            bulb = Bulb(bulb1)
            bulb.set_color_temp(ct)
            print('Color temperature set to %s' % ct)
            bulb.set_brightness(bri)
            print('Brightness set to %s' % (bri))
        
        if lamps >= '2':
            print('Setting second lamp...')
            bulb = Bulb(bulb2)
            bulb.set_color_temp(ct)
            print('Color temperature set to %s' % ct)
            bulb.set_brightness(bri)
            print('Brightness set to %s' % (bri))
        
        if lamps >= '3':
            print('Setting third lamp...')
            bulb = Bulb(bulb3)
            bulb.set_color_temp(ct)
            print('Color temperature set to %s' % ct)
            bulb.set_brightness(bri)
            print('Brightness set to %s' % (bri))
        
        if lamps >= '4':
            print('Setting fourth lamp...')
            bulb = Bulb(bulb4)
            bulb.set_color_temp(ct)
            print('Color temperature set to %s' % ct)
            bulb.set_brightness(bri)
            print('Brightness set to %s' % (bri))
        
        if lamps >= '5':
            print('Setting fifth lamp...')
            bulb = Bulb(bulb5)
            bulb.set_color_temp(ct)
            print('Color temperature set to %s' % ct)
            bulb.set_brightness(bri)
            print('Brightness set to %s' % (bri))

config = configparser.ConfigParser()
config.read('config.ini')
bulb1 = config.get('config','ip1')
bulb2 = config.get('config','ip2')
bulb3 = config.get('config','ip3')
bulb4 = config.get('config','ip3')
bulb5 = config.get('config','ip3')
lamps = config.get('config','lamps')

run(host='127.0.0.1', port=8080)