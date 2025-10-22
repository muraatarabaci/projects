import os

dosya = "gorevler.txt"

def yukle():
    if os.path.exists(dosya):
        with open(dosya, "r", encoding="utf-8") as f:
            return [x.strip() for x in f]
    print("Dosya bulunamadı. Yeni liste oluşturuluyor.\n")
    return []
    
def kaydet(gorevler):
    with open(dosya, "w", encoding="utf-8") as f:
        f.write("\n".join(gorevler))
    print("Görevler kaydedildi.\n")

def listele(gorevler):
    if not gorevler:
        print("Henüz görev yok.\n")
    else:
        for i, g in enumerate(gorevler, 1):
            print(f"{i}. {g}")
        print()

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

def tumunu_sil(gorevler):
    cevap = input("Tüm görevleri silmek istediğinize emin misiniz? (e/h): ").lower()
    if cevap == "e":
        gorevler.clear()
        kaydet(gorevler)
        print("Tüm görevler silindi.\n")
    else:
        print("İşlem iptal edildi.\n")

def menu():
    print("1. Görevleri Göster")
    print("2. Yeni Görev Ekle")
    print("3. Görev Düzenle")
    print("4. Görev Sil")
    print("5. Tüm Görevleri Sil")
    print("6. Çık\n")

def hosgeldin():
    print("To-Do List Uygulamasına Hoş geldiniz.\n")
    g_list = yukle()

    if g_list:
        print("Kayıtlı görevleriniz:\n")
        listele(g_list)
    else:
        print("Herhangi bir kayıtlı görev bulunamadı.\n")

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

if __name__ == "__main__":
    hosgeldin()

