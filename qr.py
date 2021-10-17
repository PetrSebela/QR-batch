from typing import List
import qrcode
from PIL import Image

CONST = 250

def generate(start,stop) -> List:
    returnList = []
    for count in range(start,stop,1):
        returnList.append(str(count))
    return returnList

def createQR(data,location,size) -> None:
    code = qrcode.QRCode(
        border=0
    )
    code.add_data(data)
    code.make()
    code = code.make_image(fill='black',back_color='white')
    code.save(location+'/'+data+'.png')

    img = Image.open(location+'/'+data+'.png')
    img = img.resize((250,250))
    print(mm2DPI(size))
    img.save(location+'/'+data+".png",dpi=(mm2DPI(size),mm2DPI(size)))


def mm2DPI(dim) -> float:
    return CONST/(dim/25.4)


#createQR('suck','codes',0.2)