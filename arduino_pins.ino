void setup() {
	Serial.begin(9600);
	outputAll();
}

void loop() {
	outputAll();
	delay(1000);
}

void outputAll()
{
	output("A0", A0);
	output("A1", A1);
	output("A10", A10);
	output("A11", A11);
	output("A2", A2);
	output("A3", A3);
	output("A4", A4);
	output("A5", A5);
	output("A6", A6);
	output("A7", A7);
	output("A8", A8);
	output("A9", A9);
	output("EXTERNAL_NUM_INTERRUPTS", EXTERNAL_NUM_INTERRUPTS);
	output("LED_BUILTIN", LED_BUILTIN);
	output("NUM_ANALOG_INPUTS", NUM_ANALOG_INPUTS);
	output("NUM_DIGITAL_PINS", NUM_DIGITAL_PINS);
	output("PB0", PB0);
	output("PB1", PB1);
	output("PB2", PB2);
	output("PB3", PB3);
	output("PB4", PB4);
	output("PB5", PB5);
	output("PB6", PB6);
	output("PB7", PB7);
	output("PC0", PC0);
	output("PC1", PC1);
	output("PC2", PC2);
	output("PC3", PC3);
	output("PC4", PC4);
	output("PC5", PC5);
	output("PC6", PC6);
	output("PC7", PC7);
	output("PD0", PD0);
	output("PD1", PD1);
	output("PD2", PD2);
	output("PD3", PD3);
	output("PD4", PD4);
	output("PD5", PD5);
	output("PD6", PD6);
	output("PD7", PD7);
	output("PF0", PF0);
	output("PF1", PF1);
	output("PF2", PF2);
	output("PF3", PF3);
	output("PF4", PF4);
	output("PF5", PF5);
	output("PF6", PF6);
	output("PF7", PF7);
	output("SCK", SCK);
	output("SCL", SCL);
	output("SDA", SDA);
	output("SS", SS);

	Serial.println("-------");
	}

void output(const char *what, int num)
{
  char outString[130];
  sprintf(outString, "%s:	%d", what, num);
  Serial.println(outString);
}
