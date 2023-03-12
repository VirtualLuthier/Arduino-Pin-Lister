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
