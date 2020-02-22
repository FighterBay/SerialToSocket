from __future__ import division
import serial
import socket
import threading
import time
import sys
bytes_tot = 256
class se_to_so (threading.Thread):
  def __init__(self, so, se):
    threading.Thread.__init__(self)
    self.sock = so
    self.seri = se
  
  def run(self):
    global bytes_tot
    while True:
      self.sock.sendall(self.seri.read(bytes_tot))
      time.sleep(1/100)


class so_to_se (threading.Thread):
  def __init__(self, so, se):
    threading.Thread.__init__(self)
    self.sock = so
    self.seri = se

  def run(self):
    global bytes_tot
    while True:
      b = self.sock.recv(bytes_tot)
      #print b.decode('utf-8',errors='ignore')	
      self.seri.write(b)
      time.sleep(1/100)

#Main_Inst
#Connect to socket
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.bind(('', int(sys.argv[1])))
#Connect to serial
ser = serial.Serial(
  port='/dev/ttyACM0',
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=2
)

so.listen(10)
con, addr = so.accept()
t1 = se_to_so(con,ser)
t2 = so_to_se(con,ser)

t1.start()
t2.start()

