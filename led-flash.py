import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT);
led_external = machine.Pin(15, machine.Pin.OUT);

while True:
 led_onboard.on()
 led_external.off()
 utime.sleep(1)
