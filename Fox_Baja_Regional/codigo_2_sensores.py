# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 12:02:44 2018

@author: Pedro Casella
"""
import time
import smbus
import struct

print("inicio")

i2c_address_1 = 0x68 #mpu6050_1
i2c_address_2 = 0x69 #mpu6050_2

sleep_mgmt = 0x6B
accel_x_out = 0x3B
bus = None

#mpu6050_1
acc_x_1 = 0
acc_y_1 = 0
acc_z_1 = 0
temp_1 = 0
gyro_x_1 = 0
gyro_y_1 = 0
gyro_z_1 = 0

#mpu6050_2
acc_x_2 = 0
acc_y_2 = 0
acc_z_2 = 0
temp_2 = 0
gyro_x_2 = 0
gyro_y_2 = 0
gyro_z_2 = 0

teste = 0

lista_acc_x_1 = []
lista_acc_y_1 = []
lista_acc_z_1 = []
lista_temp_1 = []

lista_acc_x_2 = []
lista_acc_y_2 = []
lista_acc_z_2 = []
lista_temp_2 = []




def initmpu():
    global bus
    bus = smbus.SMBus(1)
    bus.write_byte_data(i2c_address_1,sleep_mgmt,0x00)
    bus.write_byte_data(i2c_address_2,sleep_mgmt,0x00)
    
def get_data_1():
    
    #Mcpu6050_1
    global acc_x_1, acc_y_1, acc_z_1, temp_1, gyro_x_1, gyro_y_1, gyro_z_1
    bus.write_byte(i2c_address_1, accel_x_out)
    
    rawdata_1 = ""
    for i in range(14):
        rawdata_1 += chr(bus.read_byte_data(i2c_address_1,accel_x_out+i))
    data_1 = struct.unpack('>hhhhhhh', rawdata_1)
    
    acc_x_1 = data_1[0]/16384.0
    acc_y_1 = data_1[1]/16384.0
    acc_z_1 = data_1[2]/16384.0
    zero_point = -512 - (340*35)
    temp_1 = (data_1[3]-zero_point)/340.0
    
    gyro_x_1 = data_1[4]/131.0
    gyro_y_1 = data_1[5]/131.0
    gyro_z_1 = data_1[6]/131.0
    
    #Mcpu6050_2
    global acc_x_2, acc_y_2, acc_z_2, temp_2, gyro_x_2, gyro_y_2, gyro_z_2
    bus.write_byte(i2c_address_2, accel_x_out)
    
    rawdata_2 = ""
    for i in range(14):
        rawdata_2 += chr(bus.read_byte_data(i2c_address_2,accel_x_out+i))
    data_2 = struct.unpack('>hhhhhhh', rawdata_2)
    
    acc_x_2 = data_2[0]/16384.0
    acc_y_2 = data_2[1]/16384.0
    acc_z_2 = data_2[2]/16384.0
    zero_point = -512 - (340*35)
    temp_2 = (data_2[3]-zero_point)/340.0
    
    gyro_x_2 = data_2[4]/131.0
    gyro_y_2 = data_2[5]/131.0
    gyro_z_2 = data_2[6]/131.0
    
    
def main():
    initmpu()
    while True:
        get_data_1()
        print("Sensor_1 ---- data_1:")
        print("Acc (%.3f,%.3f,%.3f)g," %(acc_x_1,acc_y_1,acc_z_1))
        print("temp %.1f C," %temp_1)
        print("gyro (%.3f,%.3f,%.3f) deg/s" % (gyro_x_1,gyro_y_1,gyro_z_1))
        
        print("Sensor_2 ---- data_2:")
        print("Acc (%.3f,%.3f,%.3f)g," %(acc_x_2,acc_y_2,acc_z_2))
        print("temp %.1f C," %temp_2)
        print("gyro (%.3f,%.3f,%.3f) deg/s" % (gyro_x_2,gyro_y_2,gyro_z_2))
        
        print("Fim")
        time.sleep(0.5)
      
if __name__ == "__main__":
    
    print("Fox Baja")
    
    main()
    
    
    
    
    
    
    
    
    
    