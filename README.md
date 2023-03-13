# Arduino-Pin-Lister

## Motivation
One problem with all those Arduino variants is, that the pins are different between them.
Most of the example sketches are written for the Uno, which is the most common variant. And often the pin numbers are used directly, 
not as predefined macros or variables.

But I do not like the Uno, because it cannot be attached to a normal breadboard. So I bought an Arduino Micro. And as a beginner, I had problems 
finding the according pins on the Micro.

## Concept
I propose a standard sketch (arduino_pins.ino) that outputs the numbers of the most predefined pins via serial. The output is then put into a .txt file. 
Finally a script (analyzePinList.py) runs over all the .txt files and builds a table of all pin numbers of all variants. I have attached the .txt files 
and the tables for the 2 variants that I own.

Not every variant has defined all the pin numbers. In this case, please replace the undefined symbolic number with -1.
If you own another Arduino Variant, it would be very kind, if you could adapt and run the sketch and send me a text file with the contents, 
so I can integrate it.


|Pin|Pins-A-Micro|Pins-A-Uno|
| -- | -- | -- |
|A0|18|14|
|A1|19|15|
|A10|28|-1|
|A11|29|-1|
|A2|20|16|
|A3|21|17|
|A4|22|18|
|A5|23|19|
|A6|24|20|
|A7|25|21|
|A8|26|-1|
|A9|27|-1|
|EXTERNAL_NUM_INTERRUPTS|-1|-1|
|LED_BUILTIN|13|13|
|NUM_ANALOG_INPUTS|12|6|
|NUM_DIGITAL_PINS|31|20|
|PB0|0|0|
|PB1|1|1|
|PB2|2|2|
|PB3|3|3|
|PB4|4|4|
|PB5|5|5|
|PB6|6|6|
|PB7|7|7|
|PC0|-1|0|
|PC1|-1|1|
|PC2|-1|2|
|PC3|-1|3|
|PC4|-1|4|
|PC5|-1|5|
|PC6|6|6|
|PC7|7|-1|
|PD0|0|0|
|PD1|1|1|
|PD2|2|2|
|PD3|3|3|
|PD4|4|4|
|PD5|5|5|
|PD6|6|6|
|PD7|7|7|
|PF0|0|-1|
|PF1|1|-1|
|PF2|-1|-1|
|PF3|-1|-1|
|PF4|4|-1|
|PF5|5|-1|
|PF6|6|-1|
|PF7|7|-1|
|SCK|15|13|
|SCL|3|19|
|SDA|2|18|
|SS|17|10|
