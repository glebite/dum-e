// arduino.ino
//
// dummy install/template for building remote-make arduino code to
// be deployed on the arduino attached to the raspberry pi.
//

// includes

// macros
#define DEBUG 1
#define SERiAL_SPEED 115200

// constants

// globals
String command="";
byte character;

// local functions

//==================================================================
// setup:
//
// Configure Serial to a decent 'baudrate', insert any other system
// configuration here where it says: 'insert good stuff here'
//==================================================================
void setup() {
    Serial.begin(SERIAL_SPEED);    // go broke or go home
		#ifdef DEBUG
		Serial.println("Initializing.");
		#endif
		
		// insert good stuff here

		#ifdef DEBUG
		Serial.println("Initialization complete.");
		#endif
}

//=================================================================
// loop:
//
// Essentially loop forever, building strings up from the
// serial input if there are characters available.  When a \r
// is encountered, we trim the string and then can process it
// there.
//=================================================================
void loop() {
	if (Serial.available() > 0) {
		character = Serial.read();
		command += (char) character;
		if (character == '\r') {
			command.trim();

			Serial.println(command);
			
			// hand off to command handler function
			command="";
		}
	}
}
