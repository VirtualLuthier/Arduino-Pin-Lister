'''
	Build a simple arduino sketch printing out a lot of predefined constants.
	(If the compiler complains, that a constant is not defined, replace it with -1)
	Finally it is written to file 'arduino_pins.ino'.
	This sketch should be called on every arduino variant
'''

docuList = [
	'https://store.arduino.cc/products/arduino-micro',
	'https://store.arduino.cc/products/arduino-uno-rev3'
]

pinList = [
	'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11',
	
	'PB0', 'PB1', 'PB2', 'PB3', 'PB4', 'PB5', 'PB6', 'PB7',
	'PC0', 'PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7',
	
	'PD0', 'PD1', 'PD2', 'PD3', 'PD4', 'PD5', 'PD6', 'PD7',	
	'PF0', 'PF1', 'PF2', 'PF3', 'PF4', 'PF5', 'PF6', 'PF7',
	
	'EXTERNAL_NUM_INTERRUPTS',
	'LED_BUILTIN',
	'NUM_DIGITAL_PINS', 
	'NUM_ANALOG_INPUTS',
	
	'SCL', 'SDA', 'SCK', 'SS', 
	]

def create():
	pinList.sort()
	cmd = '''void setup() {
	Serial.begin(9600);
	outputAll();
}

void loop() {
	outputAll();
	delay(1000);
}

void outputAll()
{
'''
	for pin in pinList:
		cmd += "\t" + 'output("' + pin + '", ' + pin + ');' + "\n"
	cmd += '''
	Serial.println("-------");
	}

void output(const char *what, int num)
{
  char outString[130];
  sprintf(outString, "%s:\t%d", what, num);
  Serial.println(outString);
}
'''
	print(cmd)
	with open('arduino_pins.ino', 'w') as outFile:
		outFile.write(cmd)
		
####################################

create()