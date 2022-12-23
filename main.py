import serial
import time

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=1)

# reset the device before starting
ser.write(b"ATZ\r")
print(f"ATZ: {ser.readline()}")

while True:
    line = ser.readline()
    print(f"Received: {line}")
    if b"RING" in line:
        print("RING detected")
        time.sleep(1)
        # Set fax class to 8 to enable data communication
        ser.write(b"AT+FCLASS=8\r")
        print(f"Sent: AT+FCLASS=8")
        time.sleep(1)
        # Set VLS configuration to answer incoming calls and play through the speaker
        ser.write(b"AT+VLS=7\r")
        print(f"Sent: AT+VLS=7")
        time.sleep(1)
        ser.write(b"ATD9\r")
        print(f"Sent: ATD9")
        time.sleep(1)
        # Reset the modem to default settings
        ser.write(b"ATZ\r")
        print(f"Sent: ATZ")
        time.sleep(1)
        ser.write(b"ATH\r")
        print(f"Sent: ATH")
        time.sleep(1)
