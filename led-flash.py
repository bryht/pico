import machine
import utime

led_internal = machine.Pin(25, machine.Pin.OUT);

while True:
 led_internal.toggle()
 utime.sleep(1)
