import serial
import time

def send_uart_message(ser, message):
    ser.write(message)
    print(f"Sent: {message}")

def read_uart_message(ser):
    if ser.in_waiting > 0:
        incoming_message = ser.readline().decode('utf-8').rstrip()
        print(f"Received: {incoming_message}")
        return incoming_message
    return None

def main():
    PORT = 'COM7'
    BAUDRATE = 115200
    MESSAGE = b'LED_ON'  # Modify as per your message

    with serial.Serial(PORT, BAUDRATE) as ser:
        while True:
            # Send a message
            send_uart_message(ser, MESSAGE)
            
            # Delay for a bit
            time.sleep(1)
            
            # Read and echo any incoming message
            read_uart_message(ser)

if __name__ == '__main__':
    main()
