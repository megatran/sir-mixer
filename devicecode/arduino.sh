#!/bin/sh
cd $1

/usr/share/arduino/hardware/tools/avr/../avrdude -q -V -p atmega328p -C /usr/share/arduino/hardware/tools/avr/../avrdude.conf -D -c arduino -b 115200 -P /dev/tty96B0 \
                -U flash:w:build-uno/a.hex:i
