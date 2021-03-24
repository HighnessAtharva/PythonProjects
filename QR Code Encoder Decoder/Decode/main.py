from pyzbar.pyzbar import decode
from PIL import Image
# Add your own path here.
img = Image.open(
    'E:/GITHUB/Python Projects/Python Projects/QR Code Encoder Decoder/Encode/myQRCode.png')
result = decode(img)
result = result[0][0]
print(result)
