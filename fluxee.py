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
            print(f'Static brightness set to {self.static_brightness}%')
        else:
            super().set_brightness(brightness + self.brightness_offset)
            print(f'Brightness set to {brightness + self.brightness_offset}%')

    def set_color_temp(self, color_temp):
        if color_temp >= self.max_temp:
            super().set_color_temp(self.max_temp)
            print(f'Reached maximum color temperature of {self.max_temp} Kelvin')
        elif color_temp <= self.min_temp:
            super().set_color_temp(self.min_temp)
            print(f'Reached minimum color temperature of {self.min_temp} Kelvin')
        else:
            super().set_color_temp(color_temp)
            print(f'Color temperature set to {color_temp} Kelvin')

def send_command(command, value=None):
    for bulb in bulbs:
        try:
            print(f'Sending {command} to Yeelight at {bulb._ip}')
            getattr(bulb, command)(value)
        except Exception:
            traceback.print_exc()


@post('/room_1')
def room_handler():
    post_dict = request.query.decode()
    if 'ct' in post_dict:
        color_temp = int(post_dict['ct'])
        send_command('set_color_temp', color_temp)

    if 'bri' in post_dict:
        brightness = int(round(float(post_dict['bri']) * 100))
        send_command('set_brightness', brightness)

    if 'on' in post_dict:
        send_command('turn_on')


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

            print(f'Initializing Yeelight at {ip}')
            bulb = Bulb(ip, min_temp, max_temp, static_brightness, brightness_offset)
            bulbs.append(bulb)

        run(host=config["host"], port=config["port"])
    print('Thank you for using fluxee. Have a good one!')


if __name__ == "__main__":
    main()

