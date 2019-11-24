from bottle import run, post, request
import yeelight
import configparser
import traceback

bulbs = []
maxtemps = []
mintemps = []
check_state = True


class Bulb(yeelight.Bulb):

    def __init__(self, ip, min_temp=1700, max_temp=6500, static_brightness=None):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.static_brightness = static_brightness
        super().__init__(ip)

    def set_brightness(self, brightness):
        if self.static_brightness:
            super().set_brightness(self.static_brightness)
            print('Static brightness set to', self.static_brightness, 'percent')
        else:
            super().set_brightness(brightness)
            print('Brightness set to', brightness, 'percent')

    def set_color_temp(self, color_temp):
        if color_temp > self.max_temp:
            super().set_color_temp(self.max_temp)
            print('Reached highest color temperature of', self.max_temp, 'Kelvin')
        elif color_temp < self.min_temp:
            super().set_color_temp(self.min_temp)
            print('Reached lowest color temperature of', self.min_temp, 'Kelvin')
        else:
            super().set_color_temp(color_temp)
            print('Color temperature set to', color_temp, 'Kelvin')


@post('/room_1')
def room_handler():
    post_dict = request.query.decode()
    if 'ct' in post_dict and 'bri' in post_dict:
        color_temp = int(post_dict['ct'])
        brightness = int(round(float(post_dict['bri']) * 100))
        for bulb in bulbs:
            try:
                print('Sending command to Yeelight at', bulb._ip)
                bulb.set_brightness(brightness)
                bulb.set_color_temp(color_temp)
            except Exception:
                traceback.print_exc()


def main():
    print('Welcome to fluxee by davidramiro')
    print('Reading config...')
    config = configparser.ConfigParser()
    config.read('config.ini')
    global static_brightness
    bulb_count = int(config.get('general', 'LampCount'))
    check_state = config.getboolean('general', 'CheckLampState')
    static_brightness = config.getboolean('general', 'StaticBrightness')
    default_brightness = int(config.get('general', 'BrightnessValue'))
    for n in range(1, (bulb_count + 1)):
        ip = config.get(str(n), 'ip')
        max_temp = 6500
        min_temp = 1700
        if config.get(str(n), 'MaxColorTemperature') == '':
            pass
        else:
            max_temp = int(config.get(str(n), 'MaxColorTemperature'))
        if config.get(str(n), 'MinColorTemperature') == '':
            pass
        else:
            min_temp = int(config.get(str(n), 'MinColorTemperature'))
        bulbs.append(Bulb(ip, min_temp, max_temp, static_brightness))
    print('Initializing...')
    for bulb in bulbs:
            print('Initializing Yeelight at %s' % bulb._ip)
            if check_state is True:
                state = bulb.get_properties(requested_properties=['power'])
                if 'off' in state['power']:
                    print('Powered off. Ignoring Yeelight at %s' % bulb._ip)
                elif static_brightness is True:
                    print('Changing brightness of', bulb._ip)
                    bulb.set_brightness(default_brightness)
            else:
                print('Turning on Yeelight at %s' % bulb.up)
                bulb.turn_on()

    run(host=config.get('general', 'Host'), port=config.get('general', 'Port'))
    print('Thank you for using fluxee. Have a good one!')


if __name__ == "__main__":
    main()
