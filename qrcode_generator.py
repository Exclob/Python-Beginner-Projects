import qrcode
from PIL import ImageColor

def qrgenerator(data:str,fillColor: str = 'black',backColor: str = 'white')->str:

    qr = qrcode.QRCode(
        version = 1,
        box_size = 15,
        border = 5
    )

    qr.add_data(data)
    qr.make(fit=True)
    fill = ImageColor.getrgb(fillColor)
    back = ImageColor.getrgb(backColor)
    img = qr.make_image(fill_color = fill,back_color = back)
    img.save('qr.png')

qrgenerator('messiah')
