import qrcode as qr
import qrcode.image.svg
import sys



def create_qr(url, file_name):
    img = qr.make(url, image_factory= qrcode.image.svg.SvgImage)
    type(img)  # qrcode.image.pil.PilImage
    img.save(file_name + ".svg")


if __name__ == '__main__':
    create_qr(sys.argv[1], sys.argv[2])