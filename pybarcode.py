import barcode
EAN = barcode.get_barcode_class('upc')
ean = EAN('123456789012')
fullname = ean.save('ean13_barcode1')
