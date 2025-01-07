import time
import board
import adafruit_dht

# Initialize DHT11 sensor on GPIO15 (board.GP15)
sensor = adafruit_dht.DHT11(board.GP15)

while True:
    try:
        # Measure temperature and humidity
        temperature = sensor.temperature  # in Celsius
        humidity = sensor.humidity  # in percentage
        
        # Print values
        print("Temperature: {:.1f} °C".format(temperature))
        print("Humidity: {:.1f} %".format(humidity))
        
    except RuntimeError as e:
        # If there's an error reading the sensor, print it and continue
        print("Error reading sensor: ", e)
    
    # Wait before reading again
    time.sleep(2)

