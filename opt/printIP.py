import socket
import epd2in13b
from PIL import Image,ImageDraw,ImageFont
import traceback
import platform

try:
    epd = epd2in13b.EPD()
    epd.init()
    print("Clear")
    epd.Clear()

    print("Drawing")

    HBlackimage = Image.new("1", (epd2in13b.EPD_HEIGHT, epd2in13b.EPD_WIDTH), 255)
    HRedimage = Image.new("1", (epd2in13b.EPD_HEIGHT, epd2in13b.EPD_WIDTH), 255)

    drawblack = ImageDraw.Draw(HBlackimage)
    drawred = ImageDraw.Draw(HRedimage)

    font30 = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc" , 30)
    font20 = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc" , 20)


    drawblack.text((10,0), socket.gethostbyname(socket.gethostname()+".local"), font = font30, fill =0)
    drawred.text((0,35), "with " + platform.system(), font = font20, fill =0)
    drawred.text((0,55), platform.version(), font = font20, fill =0)
    drawred.text((10,75), "", font = font20, fill =0)

    epd.display(epd.getbuffer(HBlackimage.rotate(180)), epd.getbuffer(HRedimage.rotate(180)))

except:
    print("traceback")
    exit()
