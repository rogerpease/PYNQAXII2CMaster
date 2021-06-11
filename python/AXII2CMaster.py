#!/usr/bin/env python3 


#
# Interface to the AXI I2C Master peripheral. 
#
#
#

import time
import sys  

class AXII2CMaster:


   def __init__(self,overlayPeripheralPtr,i2cAddress):
     self.OverlayPeripheralPtr = overlayPeripheralPtr
     self.I2CAddress = i2cAddress
     self.valid = 1  
       
     
   def InitTransaction(self,ReadNotWrite=0,WriteByte=0xAD):
     startTime = time.time()
     result = dict() 
     result["Valid"]    = 1
     result["TimedOut"] = 0

     self.OverlayPeripheralPtr.write(0x40,0xA)
     self.OverlayPeripheralPtr.write(0x1C,0)    # GIE off 
     self.OverlayPeripheralPtr.write(0x20,0)    # ISR OFF 
     self.OverlayPeripheralPtr.write(0x28,0)    # IER OFF 
     self.OverlayPeripheralPtr.write(0x110,self.I2CAddress << 1)
     self.OverlayPeripheralPtr.write(0x108,(0<<9) + (0<<8) + self.I2CAddress << 1)
     self.OverlayPeripheralPtr.write(0x108,(1<<9) + (0<<8) + WriteByte) # Write Byte + start + stop 
     self.OverlayPeripheralPtr.write(0x100,13) # Transmit mode, Master mode, Enabled 
     return result


def SelfTest():
   from pynq import Overlay
   overlay = Overlay("AXII2CMaster.bit") 
   myi2cmaster = AXII2CMaster(overlay.axi_iic_0,0x27) 
   if (myi2cmaster.valid == 0):
     print (self.ErrorMessage)
     sys.exit(0)
   myi2cmaster.InitTransaction(WriteByte = 0x24)
   
   

 
if __name__ == "__main__":
   SelfTest()
