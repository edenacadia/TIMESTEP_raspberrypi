import RPi.GPIO as GPIO
import time

# define the pins with board values
GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    GPIO.setup(pin_to_circuit, GPIO.OUT, initial=GPIO.LOW)
    time.sleep(0.1)
    # Change the light pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
    # loop until keyboard interrupt
    while True:
        if(GPIO.input(pin_to_circuit) == GPIO.LOW):
           print("LOW")
           time.sleep(0.5)
        elif(GPIO.input(pin_to_circuit) == GPIO.HIGH):
           print("HIGH")
           time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
