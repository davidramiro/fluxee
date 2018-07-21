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
                if int(mintemp) < ct < int(maxtemp):
                    bulb.set_color_temp(ct)
                    print('Color temperature set to', ct, 'Kelvin')
                else:
                    if ct > int(maxtemp):
                        bulb.set_color_temp(int(maxtemp))
                        print('Reached highest color temperature of', maxtemp, 'Kelvin')
                    if ct < int(mintemp):
                        bulb.set_color_temp(int(mintemp))
                        print('Reached lowest color temperature of', mintemp, 'Kelvin')


def main():
    print('Welcome to fluxee by davidramiro')
    print('Reading config...')
    config = configparser.ConfigParser()
    config.read('config.ini')
    bulb_count = int(config.get('general', 'LampCount'))
    for n in range(1, (bulb_count + 1)):
        bulbs.append(config.get(str(n), 'ip'))
        if config.get(str(n), 'MaxColorTemperature') == '':
            maxtemps.append(6500)
        else:
            maxtemps.append(config.get(str(n), 'MaxColorTemperature'))
        if config.get(str(n), 'MinColorTemperature') == '':
            mintemps.append(1700)
        else:
            mintemps.append(config.get(str(n), 'MinColorTemperature'))
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
