# VOC Telegram Bot

A simple Telegram, bot that sends VOC (volatile organic compounds) and eCO2
(equivalent CO2) data from an [SGP30 Air Quality Sensor](https://www.sparkfun.com/products/16531)
to a chat.

## bot commands
### start
Sends a welcome message to the chat.
```
Hello Marco.
```

### get
Reads the VOC and eCO2 values from the sensor and returns them:
```
VOC: 12 ppb
eCO2: 402 ppm
```

## getting started

The bot needs to run on a Raspberry Pi that has an
[SGP30 Air Quality Sensor](https://www.sparkfun.com/products/16531) connected.

```bash
cd voc-telegram-bot
pip install -r requirements.txt
python3 main.py YOUR_BOT_TOKEN
```

Running the bot in a background process (e.g when connected via ssh):

```bash
# start in background
nohup python3 main.py YOUR_BOT_TOKEN &
# save pid in txt
echo $! > pid.txt
# stop background process
kill -9 `cat pid.txt`
rm pid.txt
```

## used libraries

- [Python Telegram Bot](https://python-telegram-bot.org/)
- [SGP30 Python](https://github.com/pimoroni/sgp30-python)