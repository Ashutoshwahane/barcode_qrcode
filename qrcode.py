from pyqrcode import QRCode
import pyqrcode
# String which represent the QR code
str = "https://github.com/Ashutoshwahane"
# Generate QR code
url = pyqrcode.create(str)
# Create and save the png file naming "myqr.png"
url.svg("qrcode.png", scale=8)
