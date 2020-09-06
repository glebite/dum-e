// arduino.ino
//
// dummy install/template for building remote-make arduino code to
// be deployed on the arduino attached to the raspberry pi.
//

// includes

// macros
#define DEBUG 1

// constants

// globals

// local functions

void setup() {
    Serial.begin(115200);    // go broke or go home
		#ifdef DEBUG
		Serial.println("Initializing.");
		#endif
		
		// insert good stuff here

		#ifdef DEBUG
		Serial.println("Initialization complete.");
		#endif
}

void loop() {
}
