import utime
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import data

led = Pin(25, Pin.OUT)
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128,64,i2c)
#oled.text("1234567890", 0, 0, 1)
#oled.pixel(30, 30, 1)

images = [
    data.epd_bitmap_sidespeck,
    data.epd_bitmap_oohrah,
    data.epd_bitmap_knitcaprotated,
    data.epd_bitmap_tatt,
    data.epd_bitmap__RKKZ00K_SharpenAI_Standard,
    data.epd_bitmap_thinnersmile,
    data.epd_bitmap_sided,
    data.epd_bitmap_tough,
    data.epd_bitmap_highcontrast,
    data.epd_bitmap_true,
    data.epd_bitmap_scar_monalisathinna,
    data.epd_bitmap_stiff2x  ]


while True:
    for img in range(0, len(images)):
        oled.fill(0)
        for pos in range(0, len(images[img])):
            byt = images[img][pos]
            for bit in range(0,8):
                x = (pos * 8) % 128
                x += (7 - bit)
                y = int(pos / 16)
                on = 0
                if (byt & (2 ** bit)) > 0:
                    on = 1
                oled.pixel(x, y, on)
        oled.show()
        for loops in range(0, 3):
            for c in range (0, 255):
                oled.contrast(c)
                led.off()
                if c % 85 == 0:
                    led.on()
                utime.sleep_ms(9)
                    
            led.off()
            for c in range (255, 0, -1):
                oled.contrast(c)
                led.off()
                if c % 85 == 0:
                    led.on()
                utime.sleep_ms(9)
