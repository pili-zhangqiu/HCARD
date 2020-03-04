from smbus2 import SMBus
import struct
import collections

class Regs(object):
  CTRL1_XL    = 0x10	# Linear Accel Sensor - Control Register ------ ENABLED
  CTRL2_G     = 0x11	# Angular Rate Sensor - Control Register ------ ENABLED
  CTRL3_C     = 0x12	# Control Register 3 -------------------------- ENABLED
  OUTX_L_G    = 0x22	# Angular Rate Pitch Axis (X) - Output Register
  OUTX_L_XL   = 0x28	# Linear Accel of X Axis - Output Register

Vector = collections.namedtuple('Vector', 'x y z')
print(Vector)

class LSM6(object):

  def __init__(self, slave_addr = 0b1101011):
    self.bus = SMBus(1)
    self.sa = slave_addr
    self.g = Vector(0, 0, 0)
    self.a = Vector(0, 0, 0)
      
  def enable(self):
    self.bus.write_byte_data(self.sa, Regs.CTRL1_XL, 0x50) # 208 Hz ODR, 2 g FS
    self.bus.write_byte_data(self.sa, Regs.CTRL2_G, 0x58) # 208 Hz ODR, 1000 dps FS
    self.bus.write_byte_data(self.sa, Regs.CTRL3_C, 0x04) # IF_INC = 1 (automatically increment register address)

  def read_gyro(self):
    byte_list = self.bus.read_i2c_block_data(self.sa, Regs.OUTX_L_G, 6)
    self.g = Vector(*struct.unpack('hhh', bytes(byte_list)))

  def read_accel(self):
    byte_list = self.bus.read_i2c_block_data(self.sa, Regs.OUTX_L_XL, 6)
    self.a = Vector(*struct.unpack('hhh', bytes(byte_list)))

  def read(self):
    self.read_gyro()
    self.read_accel() 

print(LSM6.__init__)
print(LSM6.enable)
print(LSM6.read_accel)
print(LSM6.read_gyro)