import pyqrcode 
from pyqrcode import QRCode 
  

s = "https://youtu.be/hlWiI4xVXKY"
  

url = pyqrcode.create(s) 
  
url.svg("youtube.svg", scale = 8)
