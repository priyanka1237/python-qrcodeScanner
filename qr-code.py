# *********************create QR code scanner in python3 ***************#

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)
img = qr.make_image()
img.save('/home/netset/Desktop/index.jpeg')
img.show()

#***************************create  Barcode in python3 ************************#

import barcode
from barcode.writer import ImageWriter
ean = barcode.get('ean13','123456789101',writer=ImageWriter())
name = ean.save('ean13')
print(name)


# ******************************create xlsx file in python3 **************#

import xlsxwriter
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A',20)
bold = workbook.add_format({'bold':True})
worksheet.write('A1', 'Hello')
worksheet.write('A2', 'Hello')
worksheet.insert_image('B5','ean13.png')
workbook.close()