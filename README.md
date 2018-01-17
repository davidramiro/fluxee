# fluxee
Changing your Yeelight smart lamp corresponding to your f.lux display temperature.

## Prerequisites
- Python
- f.lux
- Any Yeelight/Xiaomi/Mijia Wi-Fi lamp

## Usage
* Enable the [developer mode](https://www.yeelight.com/en_US/developer) (sometimes also called LAN mode) on your lamp in the Yeelight app.
* Find out your lamp's IP address and put it into the config.ini file.
* In f.lux settings enter `http://127.0.0.1:8080/room_1` in the bottom URL mask as shown [here](https://i.imgur.com/ybEWdIC.png).
* Run fluxee.py and enjoy.


## Important note

Keep in mind that your f.lux settings might not match your lamp's capabilities. My Yeelight RGBW Bulb supports 1700K to 6500K, my Mi Desk Lamp only 2700K to 6500K. f.lux ranges from 1900K to 6500K. Your mileage may vary depending on your lamp, if you're very sensitive even 2700K might not be dim enough for you to achieve full melatonin secretion.

## Credits
Gratefully using the Yeelight python library by Stavros Korokithakis.

https://github.com/skorokithakis/python-yeelight/

Copyright (c) 2016, Stavros Korokithakis

All rights reserved.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details