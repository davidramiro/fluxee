from bottle import run, post, request
import yeelight
import traceback
from yaml import load, Loader

bulbs = []

class Bulb(yeelight.Bulb):

    def __init__(self, ip, min_temp=1700, max_temp=6500, static_brightness=None, brightness_offset=0):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.static_brightness = static_brightness
        self.brightness_offset = brightness_offset
        super().__init__(ip)

    def set_brightness(self, brightness):
        if self.static_brightness:
            super().set_brightness(self.static_brightness)
            print('Static brightness set to', self.static_brightness, 'percent')
        else:
            super().set_brightness(brightness + self.brightness_offset)
            print('Brightness set to', brightness + self.brightness_offset, 'percent')

    def set_color_temp(self, color_temp):
        if color_temp >= self.max_temp:
            super().set_color_temp(self.max_temp)
            print('Reached highest color temperature of', self.max_temp, 'Kelvin')
        elif color_temp <= self.min_temp:
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
    with open('config.yaml', 'r') as config_file:
        config = load(config_file, Loader=Loader)
        print('Initializing...')
        for bulb_config in config["bulbs"]:
            ip = bulb_config["ip"]
            static_brightness = bulb_config.get("static_brightness")
            brightness_offset = bulb_config.get("brightness_offset", 0)
            min_temp = bulb_config.get("min_temp")
            max_temp = bulb_config.get("max_temp")

            print('Initializing Yeelight at %s' % ip)
            bulb = Bulb(ip, min_temp, max_temp, static_brightness, brightness_offset)
            bulbs.append(bulb)

        run(host=config["host"], port=config["port"])
    print('Thank you for using fluxee. Have a good one!')


if __name__ == "__main__":
    main()
