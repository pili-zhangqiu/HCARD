from smbus2 import SMBus
import time
bus = SMBus(1)
address = 0x6b
#address2 = 0x1e

#print bus.read_byte_data(address, 0x0f) # Output 61


#CTRL1_XL 
bus.write_byte_data(address,0x10,0b10100111)

#CTRL2_G 
bus.write_byte_data(address,0x11,0xb669ec48)

#CTRL5_C 
bus.write_byte_data(address,0x14,0b01100100)

#CTRL6_C 
bus.write_byte_data(address,0x15,0b00100000)

#CTRL7_G 
bus.write_byte_data(address,0x16,0x44)


#Convert Bytes to Number
def byteToNumber(val_1,val_2):
        number = 256 * val_2 + val_1
        if number >= 32768:
                number= number - 65536
        return number
        
def readSensorData():
        #Read acc x   0x28 & 0x29  
        AX = byteToNumber(bus.read_byte_data(address, 0x28),bus.read_byte_data(address, 0x29))

        #Read acc y   0x2a & 0x2b 
        AY = byteToNumber(bus.read_byte_data(address, 0x2A),bus.read_byte_data(address, 0x2B))

        #Read acc z   0x2c & 0x2d 
        AZ = byteToNumber(bus.read_byte_data(address, 0x2C),bus.read_byte_data(address, 0x2D))

        #Read gyro x   0x22 & 0x23  
        GX = byteToNumber(bus.read_byte_data(address, 0x22),bus.read_byte_data(address, 0x23))

        #Read gyro y   0x24 & 0x25 
        GY = byteToNumber(bus.read_byte_data(address, 0x24),bus.read_byte_data(address, 0x25))

        #Read gyro z   0x26 & 0x27 
        GZ = byteToNumber(bus.read_byte_data(address, 0x26),bus.read_byte_data(address, 0x27))

        return AX, AY, AZ, GX, GY, GZ

while True:
        SensorData = readSensorData()     
        print(SensorData)
        #Output (-3980, 1206, 4994, 3, 100, 0)
        time.sleep(0.05)
