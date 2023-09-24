import serial
import time

#establece la comunicación serial a una velocidad de 9600 badios
arduino = serial.Serial('COM4', 9600)
time.sleep(2)

print("Presione 1 para Encender y 0 para Apagar el LED:  ")

while 1:

    datousuario = input()

    if datousuario == '1':
        arduino.write(b'1')
        print("LED Encendido")
    elif datousuario == '0':
        arduino.write(b'0')
        print("LED Apagado")