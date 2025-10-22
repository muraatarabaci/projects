import random

def sayi_tahmin_oyunu():
    rastgele_sayi = random.randint(1, 100)
    tahmin_hakki = 10  # Kullanıcının tahmin hakkı
    print("1 ile 100 arasında bir sayı tuttum. Tahmin etmeye çalış!")

    while tahmin_hakki > 0:
        try:
            tahmin = int(input(f"Kalan hakkın {tahmin_hakki}. Bir sayı gir: "))
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")
            continue

        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayı gir.")
        elif tahmin > rastgele_sayi:
            print("Daha küçük bir sayı gir.")
        else:
            print(f"Tebrikler! {rastgele_sayi} sayısını doğru tahmin ettin! 🎉")
            break

        tahmin_hakki -= 1

    if tahmin_hakki == 0:
        print(f"Üzgünüm, tahmin hakkın bitti. Doğru sayı {rastgele_sayi} idi.")

sayi_tahmin_oyunu()
