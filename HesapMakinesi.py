sayi1 = float(input("1. Sayıyı Giriniz: "))
sayi2 = float(input("2. Sayıyı Giriniz: "))
islem = input("Hangi İşlemi Yapmak İstiyorsunuz (-,+,/,*)")

if islem == "+":
    print("Sonuç:" + str(sayi1 + sayi2))
elif islem == "-":
    print("Sonuç:" + str(sayi1 - sayi2))
elif islem =="/":
    print("Sonuç:" + str(sayi1 / sayi2))
elif islem =="*":
    print("Sonuç:" + str(sayi1 * sayi2))
else:
    print("Lütfen İşlem Girişini doğru yaptığınızdan veya Sayılıranızı girerken harf kullanmadığınızdan emin olun! ")
