# fluxee
Changing your Yeelight smart lamp corresponding to your f.lux display temperature.

## Prerequisites
- Python
- f.lux
- Any Yeelight/Xiaomi/Mijia Wi-Fi lamp

## Usage
To control your Yeelight via local network, you need to enable the [developer mode](https://www.yeelight.com/en_US/developer) (also called LAN mode) on your lamp in the Yeelight app.
In the f.lux settings enter `http://127.0.0.1:8080/room_1` in the bottom URL mask as shown here:

![f.lux settings](https://i.imgur.com/ybEWdIC.png "f.lux settings")

Run fluxee.py, enter your lamp's ip address and enjoy.


## Important note

- Keep in mind that your f.lux settings might not match your lamp's capabilities. My Mi Desk Lamp supports 2700K to 6500K, f.lux ranges from 1900K to 6500K. Works well for my needs but your mileage may vary depending on your lamp. The application will output an error if you go beyond that but it will still keep working.

## Credits
Gratefully using the Yeelight python library by Stavros Korokithakis.

https://github.com/skorokithakis/python-yeelight/

Copyright (c) 2016, Stavros Korokithakis

All rights reserved.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details