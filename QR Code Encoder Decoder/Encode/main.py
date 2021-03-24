import qrcode
data = "Please star and share @HighnessAtharva's Repository if you found this useful."
img = qrcode.make(data)
img.save('E:/ToTransfer/myQRCode.png')
