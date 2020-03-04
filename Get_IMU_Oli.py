from smbus2 import SMBus
import time

bus = SMBus(1)

address = 0x1e 
address2 = 0x6b


bus.write_byte_data(address,0x20,0b10100111)
bus.write_byte_data(address,0x21,0b00100001)
bus.write_byte_data(address,0x24,0b01100100)
bus.write_byte_data(address,0x25,0b00100000)

bus.write_byte_data(address2,0x20,0x0f)

def readSensorData():
        MX1 = bus.read_byte_data(address, 0x08)
        MX2 = bus.read_byte_data(address, 0x09)
        MX = 256 * MX2 + MX1
        if MX >= 32768:
                MX= MX - 65536
        else:
                MX= MX     


        MY1= bus.read_byte_data(address, 0x0A)
        MY2 = bus.read_byte_data(address, 0x0B)
        MY = 256 * MY2 + MY1
        if MY >= 32768:
                MY= MY - 65536
        else:
                MY= MY
                
        MZ1 = bus.read_byte_data(address, 0x0C)
        MZ2 = bus.read_byte_data(address, 0x0D)
        MZ = 256 * MZ2 + MZ1
        if MZ >= 32768:
                MZ= MZ - 65536
        else:
                MZ= MZ


        AX1 = bus.read_byte_data(address, 0x28)
        AX2 = bus.read_byte_data(address, 0x29)
        AX = 256 * AX2 + AX1
        if AX >= 32768:
                AX= AX - 65536
        else:
                AX= AX
                
        AY1= bus.read_byte_data(address, 0x2A)
        AY2 = bus.read_byte_data(address, 0x2B)
        AY = 256 * AY2 + AY1
        if AY >= 32768:
                AY= AY - 65536
        else:
                AY= AY
                
        AZ1 = bus.read_byte_data(address, 0x2C)
        AZ2 = bus.read_byte_data(address, 0x2D)
        AZ = 256 * AZ2 + AZ1      
        if AZ >= 32768:
                AZ= AZ - 65536
        else:
                AZ= AZ


        GX1 = bus.read_byte_data(address2, 0x28)
        GX2 = bus.read_byte_data(address2, 0x29)
        GX = 256 * GX2 + GX1      
        if GX >= 32768:
                GX= GX- 65536
        else:
                GX= GX


        GY1 = bus.read_byte_data(address2, 0x2A)
        GY2 = bus.read_byte_data(address2, 0x2B)
        GY = 256 * GY2 + GY1      
        if GY >= 32768:
                GY= GY- 65536
        else:
                GY= GY


        GZ1 = bus.read_byte_data(address2, 0x2C)
        GZ2 = bus.read_byte_data(address2, 0x2D)
        GZ = 256 * GZ2 + GZ1      
        if GZ >= 32768:
                GZ= GZ - 65536
        else:
                GZ= GZ


                      
        return MX, MY, MZ,AX, AY, AZ, GX, GY, GZ


while True:
        SensorData = readSensorData()     
        print(SensorData)
        time.sleep(0)