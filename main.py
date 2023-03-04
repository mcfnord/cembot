import utime
from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import data

loop = 0

def update_breath(c):
    oled.contrast(c)
    led.off()
    if c % 86 == 0:
        led.on()
    utime.sleep_ms(9)
    if loop > 1:
        ledUV.duty_u16(int(256 * c))     # Set the duty cycle, between 0-65535


led = Pin(25, Pin.OUT)
ledUV = PWM(Pin(28))
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128,64,i2c)

images = [
     {"bitmap": data.epd_bitmap_scar_monalisathinna,         "x_offset" :   20, "y_offset" : 30 }
    ,{"bitmap": data.epd_bitmap_highcontrast,                "x_offset" :  -10, "y_offset" :  5 }
    ,{"bitmap": data.epd_bitmap_tough,                       "x_offset" :  -20, "y_offset" : 10 }
    ,{"bitmap": data.epd_bitmap_thinnersmile,                "x_offset" :   -5, "y_offset" : 15 }
    ,{"bitmap": data.epd_bitmap_sided,                       "x_offset" :  -15, "y_offset" : 15 }
    ,{"bitmap": data.epd_bitmap_true,                        "x_offset" :    0, "y_offset" : 15 }
    ,{"bitmap": data.epd_bitmap_stiff2x,                     "x_offset" :  -15, "y_offset" : 15 }
    ,{"bitmap": data.epd_bitmap_knitcaprotated,              "x_offset" :    8, "y_offset" : 15 }
    ,{"bitmap": data.epd_bitmap_tatt,                        "x_offset" :   -5, "y_offset" : 30 }
    ,{"bitmap": data.epd_bitmap_oohrah,                      "x_offset" :  -20, "y_offset" : 10 }
    ,{"bitmap": data.epd_bitmap_sidespeck,                   "x_offset" :    0, "y_offset" : 15 }
    ,{"bitmap": data.epd_bitmap__RKKZ00K_SharpenAI_Standard, "x_offset" :    0, "y_offset" : 15 }
    ]

ledUV.duty_u16(0)
for dimness in range(500, 0, -44):
    oled.fill(0)
    oled.show()
    utime.sleep_ms(dimness)
    oled.text("erm", 50, 50, 1)
    oled.show()
    utime.sleep_ms(11)
    
while True:
    for img in range(0, len(images)):
        oled.fill(0)
        oled.show()

        for pos in range(0, len(images[img]["bitmap"])):
            byt = images[img]["bitmap"][pos]
            for bit in range(0,8):
                x = (pos * 8) % 128
                x += (7 - bit)
                y = int(pos / 16)
                on = 0
                if (byt & (2 ** bit)) > 0:
                    on = 1
                oled.pixel(x, y, on)

        oled.scroll(images[img]["x_offset"],images[img]["y_offset"])
        if loop < 4 :
            oled.fill(0)
        oled.show()
        for loops in range(0, 2):
            for c in range (1, 255):
                update_breath(c)
                    
            led.off()
            for c in range (255, 0, -1):
                update_breath(c)
        loop += 1
    