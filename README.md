# fluxee

Setting up a light scene with Yeelight smart lamps corresponding to your f.lux display temperature. Supports any number of lamps simultaneously.

## Prerequisites

- Python 3.11+
- Pipenv
- f.lux installed
- Any Yeelight/Xiaomi/Mijia Wi-Fi lamp

## Usage

- Clone the repo
- Run `pipenv install && pipenv shell`
- Enable LAN Control on your lamps in the Yeelight app.
- Create a copy of `config.yaml.default` called `config.yaml`
- Find out your lamp's IP addresses and put them into `config.yaml`.
- If you know your lamp's color temperature range you should set it in the config file aswell. If you don't know it, the script will use the widest range possible but you might get an error message. It will still work, though.
- In f.lux settings enter `http://127.0.0.1:8080/room_1` in the bottom URL
- Run `python fluxee.py`

## Important note

Keep in mind that your f.lux settings might not match your lamp's capabilities. For example, my Yeelight RGBW Bulb supports 1700K to 6500K, my Mi Desk Lamp only 2700K to 6500K. On default, f.lux ranges from 1900K to 6500K, its effectiveness may vary depending on your lamp. If you're very sensitive even 2700K might not be dim enough for you to achieve full melatonin secretion.

## Potential Issues

Some people seem to have issues getting the script to work flawlessly with the Xiaomi Mi LED Desk Lamp (Xiaomi Mijia Yeelight MJTD01YL). For me it works most of the time with an occasional error regarding the power state of the lamp. Disabling the state check in the `config.ini` might help.

## Credits

Thanks to [ekzi](https://github.com/mikhail-ekzi) for providing the idea and basis behind this project!

Gratefully using the [Yeelight python library](https://gitlab.com/stavros/python-yeelight) by Stavros Korokithakis.  
Copyright (c) 2016, Stavros Korokithakis  
All rights reserved.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
