from smbus2 import SMBus, i2c_msg
import numpy as np
import atexit
from logging import warning


class SFM4300:
    """Wrapper for the SFM4300-20 sensor.
    This class sets the bus up and starts the measurement.
    Methods
        -------
        get_flow()
            return the flow value as float.
        
    """
    def __init__(self, bus_id=1) -> int:
        self.i2cbus = SMBus(bus_id)
        self.measurement_start_msg = i2c_msg.write(0x2A,[0x36, 0x08])
        self.measurement_stop_msg = i2c_msg.write(0x2A,[0x3F,0xF9])
        self.measure_data_msg = i2c_msg.read(0x2A,2)

        # these are taken from the sensor datasheet directly
        self.scale_factor = 2500        # 2’500 slm-1
        self.offset = -28672            # -28’672
        
        self.i2cbus.i2c_rdwr(self.measurement_start_msg)        
        atexit.register(self.cleanup)

    def tc(self, hb, lb):
        comp = (hb<<8)|lb
        return comp
    
    def get_flow(self):
        """Ask for sensor value on preset i2c bus. 
        Please take into account, that the sensor needs ~12m
        after measurement start before being able to deliver first value.
        :returns: a floating point flow value with unit 'slm' (standard liter per minute)
        """
        try:
            self.i2cbus.i2c_rdwr(self.measure_data_msg)
            bytes_from_iterator = list(self.measure_data_msg)
            high_byte = np.int8(bytes_from_iterator[0])
            low_byte = np.int16(bytes_from_iterator[1])
            int_val = self.tc(high_byte, low_byte)
            scaled_val = (int_val - self.offset) /self.scale_factor
            return scaled_val
        except:
            warning("SFM4300:\t could not get sensor value.")
        return

    def cleanup(self):
        self.i2cbus.i2c_rdwr(self.measurement_stop_msg)
    

