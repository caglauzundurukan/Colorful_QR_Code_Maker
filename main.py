import qrcode

# Özelliksiz qr code oluşturma kodu:
# code = qrcode.make('https://github.com/caglauzundurukan')
# code.save('code1.png')

# Özellikli qr code oluşturma kodu:
code = qrcode.QRCode(
    version=1,  # QR codeun boyutunu tanımlarız. 1-40 arası değer alabilir.
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi, L olduğu için LOW yani düşük.
    box_size=50,  # Pixel olarak boyutunu belirlediğimiz özellik.
    border=2  # Kenar boyutu
)
data = input("QR içine eklemek istediğiniz metni girin: ")
code.add_data(data)  # qr code'un içindeki veri
code.make(fit=True)  # fit ile qr code'un veriye otomatik olarak uyumlu olması sağlanır.

image = code.make_image(fill_color="pink", back_color="white")  # renkler
filename = input("QR kodunun kaydedileceği dosya adını girin: ") # sonu .png ile bitsin örneğin: code3.png
image.save(filename)
