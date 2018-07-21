import platform
if platform.system() == "Windows":
    import fcntl  # If run on a Windows machine, use an alternative fcntl module
from bottle import run, post, request
from yeelight import Bulb
import configparser

bulbs = []
maxtemps = []
mintemps = []
check_state = True


@post('/room_1')
def room_handler():
    post_dict = request.query.decode()
    if 'ct' in post_dict and 'bri' in post_dict:
        ct = int(post_dict['ct'])
        bri = int(float(post_dict['bri']) * 100)
        for (currentbulb, maxtemp, mintemp) in zip(bulbs, maxtemps, mintemps):
            if currentbulb != '':
                print('Sending command to Yeelight at', currentbulb)
                bulb = Bulb(currentbulb)
                bulb.set_brightness(bri)
                print('Brightness set to', bri, 'percent')
                if mintemp < ct < maxtemp:
                    bulb.set_color_temp(ct)
                    print('Color temperature set to', ct, 'Kelvin')
                else:
                    if ct > maxtemp:
                        bulb.set_color_temp(maxtemp)
                        print('Reached highest color temperature of', maxtemp, 'Kelvin')
                    if ct < mintemp:
                        bulb.set_color_temp(mntemp)
                        print('Reached lowest color temperature of', mintemp, 'Kelvin')


def main():
    print('Welcome to fluxee by davidramiro')
    print('Reading config...')
    config = configparser.ConfigParser()
    config.read('config.ini')
    check_state = config.getboolean('general', 'CheckLampState')
    bulbs.append(config.get('lamp one', 'ip'))
    maxtemp1 = config.get('lamp one', 'MaxColorTemperature')
    mintemp1 = config.get('lamp one', 'MinColorTemperature')
    if mintemp1 == '':
        mintemp1 = 1700
    if maxtemp1 == '':
        maxtemp1 = 6500
    else:
        mintemp1 = int(mintemp1)
        maxtemp1 = int(maxtemp1)
    maxtemps.append(maxtemp1)
    mintemps.append(mintemp1)
    bulbs.append(config.get('lamp two', 'ip'))
    maxtemp2 = config.get('lamp two', 'MaxColorTemperature')
    mintemp2 = config.get('lamp two', 'MinColorTemperature')
    if mintemp2 == '':
        mintemp2 = 1700
    if maxtemp2 == '':
        maxtemp2 = 6500
    else:
        mintemp2 = int(mintemp2)
        maxtemp2 = int(maxtemp2)
    maxtemps.append(maxtemp2)
    mintemps.append(mintemp2)
    bulbs.append(config.get('lamp three', 'ip'))
    maxtemp3 = config.get('lamp three', 'MaxColorTemperature')
    mintemp3 = config.get('lamp three', 'MinColorTemperature')
    if mintemp3 == '':
        mintemp3 = 1700
    if maxtemp3 == '':
        maxtemp3 = 6500
    else:
        mintemp3 = int(mintemp3)
        maxtemp3 = int(maxtemp3)
    maxtemps.append(maxtemp3)
    mintemps.append(mintemp3)
    bulbs.append(config.get('lamp four', 'ip'))
    maxtemp4 = config.get('lamp four', 'MaxColorTemperature')
    mintemp4 = config.get('lamp four', 'MinColorTemperature')
    if mintemp4 == '':
        mintemp4 = 1700
    if maxtemp4 == '':
        maxtemp4 = 6500
    else:
        mintemp4 = int(mintemp4)
        maxtemp4 = int(maxtemp4)
    maxtemps.append(maxtemp4)
    mintemps.append(mintemp4)
    bulbs.append(config.get('lamp five', 'ip'))
    maxtemp5 = config.get('lamp five', 'MaxColorTemperature')
    mintemp5 = config.get('lamp five', 'MinColorTemperature')
    if mintemp5 == '':
        mintemp5 = 1700
    if maxtemp5 == '':
        maxtemp5 = 6500
    else:
        mintemp5 = int(mintemp5)
        maxtemp5 = int(maxtemp5)
    maxtemps.append(maxtemp5)
    mintemps.append(mintemp5)
    print('Initializing...')
    for init_bulb in bulbs:
        if init_bulb != '':
            print('Initializing Yeelight at %s' % init_bulb)
            bulb = Bulb(init_bulb)
            if check_state == True:
                state = bulb.get_properties(requested_properties=['power'])
                if 'off' in state['power']:
                    print('Powered off. Ignoring Yeelight at %s' % init_bulb)
            else:
                print('Turning on Yeelight at %s' % init_bulb)
                bulb.turn_on()
                bulb.set_brightness(100)

    run(host='127.0.0.1', port=8080)
    print('Thank you for using fluxee. Have a good one!')


main()
