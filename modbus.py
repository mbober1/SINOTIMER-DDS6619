#!/usr/bin/env python3
import minimalmodbus
import serial

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_EVEN
instrument.serial.stopbits = 1
instrument.serial.timeout  = 1          # seconds
instrument.address = 1
instrument.mode = minimalmodbus.MODE_RTU
instrument.clear_buffers_before_each_transaction = True

while True:
  voltage = instrument.read_float(0x00, functioncode=4)
  current = instrument.read_float(0x08, functioncode=4)
  active_power = instrument.read_float(0x12, functioncode=4)
  power_factor = instrument.read_float(0x2A, functioncode=4)
  frequency = instrument.read_float(0x36, functioncode=4)
  total_power = instrument.read_float(0x0100, functioncode=4)

  text = f"Voltage: {voltage:.2f} V    "
  text += f"Current: {current:.2f} A    "
  text += f"Active power: {active_power:.2f} KWh    "
  text += f"Power factor: {power_factor:.2f}     "
  text += f"Frequency: {frequency:.0f} Hz    "
  text += f"Total: {total_power:.2f} KWh    "

  print(text)
