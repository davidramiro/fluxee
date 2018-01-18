from bottle import run, post, request
from yeelight import Bulb
import configparser

@post('/room_1')
def room_handler():
    post_dict = request.query.decode()
    if 'ct' in post_dict and 'bri' in post_dict:
        ct = int(post_dict['ct'])
        bri = int(float(post_dict['bri']) * 100)
        
        if bulb1 != '':
            print('Setting first lamp...')
            bulb = Bulb(bulb1)
            bulb.set_brightness(bri)
            print('Brightness set to %s percent' % (bri))
            if mintemp1 < ct < maxtemp1:
                bulb.set_color_temp(ct)
                print('Color temperature set to %s Kelvin' % ct)
            else:
                if ct > maxtemp1:
                    bulb.set_color_temp(maxtemp1)
                    print('Reached highest color temperature of %s Kelvin' % maxtemp1)
                if ct < mintemp1:
                    bulb.set_color_temp(mintemp1)
                    print('Reached lowest color temperature of %s Kelvin' % mintemp1)
        
        if bulb2 != '':
            print('Setting second lamp...')
            bulb = Bulb(bulb2)
            bulb.set_brightness(bri)
            print('Brightness set to %s percent' % (bri))
            if mintemp2 < ct < maxtemp2:
                bulb.set_color_temp(ct)
                print('Color temperature set to %s Kelvin' % ct)
            else:
                if ct > maxtemp2:
                    bulb.set_color_temp(maxtemp2)
                    print('Reached highest color temperature of %s Kelvin' % maxtemp2)
                if ct < mintemp5:
                    bulb.set_color_temp(mintemp2)
                    print('Reached lowest color temperature of %s Kelvin' % mintemp2)
        
        if bulb3 != '':
            print('Setting third lamp...')
            bulb = Bulb(bulb3)
            bulb.set_brightness(bri)
            print('Brightness set to %s percent' % (bri))
            if mintemp3 < ct < maxtemp3:
                bulb.set_color_temp(ct)
                print('Color temperature set to %s Kelvin' % ct)
            else:
                if ct > maxtemp3:
                    bulb.set_color_temp(maxtemp3)
                    print('Reached highest color temperature of %s Kelvin' % maxtemp3)
                if ct < mintemp3:
                    bulb.set_color_temp(mintemp3)
                    print('Reached lowest color temperature of %s Kelvin' % mintemp3)
        
        if bulb4 != '':
            print('Setting fourth lamp...')
            bulb = Bulb(bulb4)
            bulb.set_brightness(bri)
            print('Brightness set to %s percent' % (bri))
            if mintemp4 < ct < maxtemp4:
                bulb.set_color_temp(ct)
                print('Color temperature set to %s Kelvin' % ct)
            else:
                if ct > maxtemp4:
                    bulb.set_color_temp(maxtemp4)
                    print('Reached highest color temperature of %s Kelvin' % maxtemp4)
                if ct < mintemp4:
                    bulb.set_color_temp(mintemp4)
                    print('Reached lowest color temperature of %s Kelvin' % mintemp4)
        
        if bulb5 != '':
            print('Setting fifth lamp...')
            bulb = Bulb(bulb5)
            bulb.set_brightness(bri)
            print('Brightness set to %s percent' % (bri))
            if mintemp5 < ct < maxtemp5:
                bulb.set_color_temp(ct)
                print('Color temperature set to %s Kelvin' % ct)
            else:
                if ct > maxtemp5:
                    bulb.set_color_temp(maxtemp5)
                    print('Reached highest color temperature of %s Kelvin' % maxtemp5)
                if ct < mintemp5:
                    bulb.set_color_temp(mintemp5)
                    print('Reached lowest color temperature of %s Kelvin' % mintemp5)


config = configparser.ConfigParser()
config.read('config.ini')
bulb1 = config.get('lamp one','ip')
maxtemp1 = config.get('lamp one','MaxColorTemperature')
mintemp1 = config.get('lamp one','MinColorTemperature')
if mintemp1 == '':
    mintemp1 = 1700
if maxtemp1 == '':
    maxtemp1 = 6500
else:
    mintemp1 = int(mintemp1)
    maxtemp1 = int(maxtemp1)

bulb2 = config.get('lamp two','ip')
maxtemp2 = config.get('lamp two','MaxColorTemperature')
mintemp2 = config.get('lamp two','MinColorTemperature')
if mintemp2 == '':
    mintemp2 = 1700
if maxtemp2 == '':
    maxtemp2 = 6500
else:
    mintemp2 = int(mintemp2)
    maxtemp2 = int(maxtemp2)

bulb3 = config.get('lamp three','ip')
maxtemp3 = config.get('lamp three','MaxColorTemperature')
mintemp3 = config.get('lamp three','MinColorTemperature')
if mintemp3 == '':
    mintemp3 = 1700
if maxtemp3 == '':
    maxtemp3 = 6500
else:
    mintemp3 = int(mintemp3)
    maxtemp3 = int(maxtemp3)

bulb4 = config.get('lamp four','ip')
maxtemp4 = config.get('lamp four','MaxColorTemperature')
mintemp4 = config.get('lamp four','MinColorTemperature')
if mintemp4 == '':
    mintemp4 = 1700
if maxtemp4 == '':
    maxtemp4 = 6500
else:
    mintemp4 = int(mintemp4)
    maxtemp4 = int(maxtemp4)

bulb5 = config.get('lamp five','ip')
maxtemp5 = config.get('lamp five','MaxColorTemperature')
mintemp5 = config.get('lamp five','MinColorTemperature')
if mintemp5 == '':
    mintemp5 = 1700
if maxtemp5 == '':
    maxtemp5 = 6500
else:
    mintemp5 = int(mintemp5)
    maxtemp5 = int(maxtemp5)

run(host='127.0.0.1', port=8080)