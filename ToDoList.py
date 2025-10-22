import os

dosya = "gorevler.txt"

# Görevleri dosyadan okuyoruz. Dosya yoksa boş liste dönüyor.
def yukle():
    if os.path.exists(dosya):
        with open(dosya, "r", encoding="utf-8") as f:
            return [x.strip() for x in f]
    print("Dosya bulunamadı. Yeni liste oluşturuluyor.\n")
    return []

# Görevleri dosyaya kaydediyoruz.
def kaydet(gorevler):
    with open(dosya, "w", encoding="utf-8") as f:
        f.write("\n".join(gorevler))
    print("Görevler kaydedildi.\n")

# Görevleri ekranda liste halinde gösteriyoruz.
def listele(gorevler):
    if not gorevler:
        print("Henüz görev yok.\n")
    else:
        for i, g in enumerate(gorevler, 1):
            print(f"{i}. {g}")
        print()

# Yeni görev ekliyoruz, boş girilirse uyarı veriyoruz.
def ekle(gorevler):
    while True:
        g = input("Yeni görev: ").strip()
        if g:
            gorevler.append(g)
            print("Görev eklendi.\n")
            kaydet(gorevler)
            break
        else:
            print("Görev boş olamaz! Lütfen bir görev girin.")

# Mevcut görevlerden birini düzenliyoruz.
def duzenle(gorevler):
    listele(gorevler)
    try:
        i = int(input("Düzenlenecek görev no: ")) - 1
        if 0 <= i < len(gorevler):
            yeni = input("Yeni görev: ").strip()
            gorevler[i] = yeni
            print("Görev güncellendi.\n")
            kaydet(gorevler)
        else:
            print("Geçersiz numara.\n")
    except:
        print("Lütfen geçerli bir sayı girin.\n")

# Seçilen görevi siliyoruz.
def sil(gorevler):
    listele(gorevler)
    try:
        i = int(input("Silinecek görev no: ")) - 1
        if 0 <= i < len(gorevler):
            print(f"{gorevler.pop(i)} silindi.\n")
            kaydet(gorevler)
        else:
            print("Geçersiz numara.\n")
    except:
        print("Lütfen geçerli bir sayı girin.\n")

# Kullanıcı tüm görevleri silmek isterse bu kod satırı çalışıyor ve en son yanlışlıkla silinmemesi için kullanıcıdan onay alıyoruz.
def tumunu_sil(gorevler):
    cevap = input("Tüm görevleri silmek istediğinize emin misiniz? (e/h): ").lower()
    if cevap == "e":
        gorevler.clear()
        kaydet(gorevler)
        print("Tüm görevler silindi.\n")
    else:
        print("İşlem iptal edildi.\n")

# Kullanıcıya menüdeki seçenekleri gösteriyoruz.
def menu():
    print("1. Görevleri Göster")
    print("2. Yeni Görev Ekle")
    print("3. Görev Düzenle")
    print("4. Görev Sil")
    print("5. Tüm Görevleri Sil")
    print("6. Çık\n")

# Programın karşılama ekranında burası çalışıyor.
def hosgeldin():
    print("To-Do List Uygulamasına Hoş geldiniz.\n")
    g_list = yukle()

    # Program açıldığında görev varsa hemen gösteriyoruz.
    if g_list:
        print("Kayıtlı görevleriniz:\n")
        listele(g_list)
    else:
        print("Herhangi bir kayıtlı görev bulunamadı.\n")

    # Kullanıcı çıkmak isteyene kadar menüyü döngüde gösteriyoruz.
    while True:
        menu()
        secim = input("Seçiminiz (1-6): ").strip()
        print()
        if secim == "1":
            listele(g_list)
        elif secim == "2":
            ekle(g_list)
        elif secim == "3":
            duzenle(g_list)
        elif secim == "4":
            sil(g_list)
        elif secim == "5":
            tumunu_sil(g_list)
        elif secim == "6":
            print("Çıkılıyor.")
            break
        else:
            print("Geçersiz giriş.\n")

# Programı başlatan kısım.
if __name__ == "__main__":
    hosgeldin()
