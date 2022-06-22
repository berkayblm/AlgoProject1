import sys

def oyun_tahtasi_goruntule(tas_liste, yatay_cizgi_sayi, dikey_cizgi_sayi, sutun = 0, satir = 0 , tas_rengi= " "):
    harf_liste = ["A","B","C","D","E","F","G","H"]
    #toplam 2 oyuncunun tas sayısı kadar hamle olacak
    # oyuncu_1 beyaz tas
    # oyuncu_2 siyah tas
    # tek sayili hamle icin oyuncu 1, cift icin oyuncu 2
    tas_liste[satir-1][sutun] = tas_rengi
    print("  ",end="")
    for harf in range(dikey_cizgi_sayi):
        print(harf_liste[harf],end=" "*3)
    print()
    for i in range(1, 2 * yatay_cizgi_sayi):
        if i % 2 != 0:  # yatay cizgi bastirma
            print(int((i+1)/2), end="")
            print(" ",end="")

            for j in range(dikey_cizgi_sayi):
                if j < dikey_cizgi_sayi-1:
                    print(tas_liste[int((i-1)/2)][j],end="")
                    print("---",end="")
                else:
                    print(tas_liste[int((i-1) / 2)][j],end="")
            print(" ",int((i+1)/2))

        else:
            print("  ",end="")
            for j in range(dikey_cizgi_sayi):
                print("|",end=" "*3)
            print()
    print("  ", end="")

    for harf in range(dikey_cizgi_sayi):
        print(harf_liste[harf], end=" " * 3)
    print()
    return tas_liste

def yatay_cizgi_al(): # kullanıcıdan girilen yatay cizgi sayisini alan ve hatali veri girisini kontrol eden function.
    while True:
        try:
            yatay_cizgi_sayi = int(input("Yatay cizgi sayisi: "))
            while not 3 <= yatay_cizgi_sayi <= 7:
                print("Yatay cizgi sayisi [3,7] arasında olmalıdır.")
                yatay_cizgi_sayi = int(input("Yatay cizgi sayisi: "))
        except ValueError:
            print("Geçersiz veri girisi. Tekrar giriniz.")
        else:
            break
    dikey_cizgi_sayi = yatay_cizgi_sayi + 1    # dikey cizgi yataydan 1 fazla
    oyuncu_1_tas_sayi = int(yatay_cizgi_sayi * dikey_cizgi_sayi / 2)   # 1. oyuncu icin toplam tas sayisi
    oyuncu_2_tas_sayi = int(yatay_cizgi_sayi * dikey_cizgi_sayi / 2)   # 2. oyuncu icin toplam tas sayisi
    tas_liste = [[" " for i in range(dikey_cizgi_sayi)] for j in range(yatay_cizgi_sayi)]  # 2 boyutlu matrix olusturur.
    oyun_tahtasi_goruntule(tas_liste,yatay_cizgi_sayi, dikey_cizgi_sayi)   # ilk once olusan tabloyu bos olarak bastirir
    ilk_asama(tas_liste,yatay_cizgi_sayi,dikey_cizgi_sayi,oyuncu_1_tas_sayi, oyuncu_2_tas_sayi)

def ilk_asama(tas_liste, yatay_cizgi_sayi,dikey_cizgi_sayi,oyuncu_1_tas_sayi, oyuncu_2_tas_sayi):

    harf_index_dict = harf_index_eslestir() # harflerin sutun indexlerini tutar
    birinci_oyuncu_hamle_sayi = oyuncu_1_tas_sayi #oyuncu 1 in hamle sayisi
    ikinci_oyuncu_hamle_sayi = oyuncu_2_tas_sayi #oyuncu 2 nin hamle sayisi
    toplam_hamle_sayi = birinci_oyuncu_hamle_sayi + ikinci_oyuncu_hamle_sayi  #toplam hamle iki oyuncunun hamle sayi toplami

    while toplam_hamle_sayi != 0:  # tas yerlestirme islemi gerceklestirilir ve hatali veri girileri kontrol edilir
        while True:
            try:
                oyuncu_hamle = input("Taşı yerleştirmek istediğiniz yerin konumunu giriniz (2A,3C,5B..): ").upper()
                hamle_sutun = harf_index_dict[oyuncu_hamle[1]]
                hamle_satir = int(oyuncu_hamle[0])

                while tas_liste[int(oyuncu_hamle[0]) - 1][harf_index_dict[oyuncu_hamle[1]]] != " ":
                    print("Girdiğiniz pozisyonda zaten bir taş bulunmakta. Lütfen boş bir pozisyona taşınızı ekleyiniz.")
                    oyuncu_hamle = input("Taşı yerleştirmek istediğiniz yerin konumunu giriniz (1A,3C...): ").upper()

                while len(oyuncu_hamle) > 2 or oyuncu_hamle.isdigit() or oyuncu_hamle.isalpha():
                    print("Geçersiz veri girisi. Tekrar giriniz. ")
                    oyuncu_hamle = input("Taşı yerleştirmek istediğiniz yerin konumunu giriniz (1A,3C...): ").upper()

            except (ValueError, KeyError, IndexError):
                print("Geçersiz veri girisi. Tekrar giriniz. ")

            else:
                break

        if toplam_hamle_sayi % 2 == 0:  # birinci oyuncu icin hamle sirasi
            tas = "b" #beyaz

        else:  # ikinci oyuncu icin hamle sayisi
            tas = "s" #siyah
        oyun_tahtasi_goruntule(tas_liste,yatay_cizgi_sayi, dikey_cizgi_sayi, sutun= hamle_sutun, satir= hamle_satir, tas_rengi= tas)
        # her hamle sonunda tablo ekrana bastirilir
        toplam_hamle_sayi -= 1

    final_turu(tas_liste, {}, 100001)  # tum hamleler bittikten sonra final_turu fonks. u cagirilir.
    # buradaki 3. parametre en sonda hareket_ettir_kazan fonks. nun while dongusunu kontrol edecek. Buyuk sayi verilmesinin nedeni hamle sayisinin cok olmasi.
def kareleri_say(tas_liste):
    oyuncu_kare_sayilari = {"beyaz_kare_sayi": 0, "siyah_kare_sayi": 0} # default olarak oyuncu kare sayilari 0 yaptik
    harf_index_dict = harf_index_eslestir()
    key_list = []
    value_list = []
    for key, value in harf_index_dict.items():
        key_list.append(key)
        value_list.append(value)
    kare_olusturan_tas_pozisyonlari = []  # kare olusturan taslarin konumlarini tutan array

    for satir_no in range(len(tas_liste)):
        if satir_no == 0: #ilk satir
            for eleman in range(len(tas_liste[satir_no])):

                if eleman < len(tas_liste[satir_no]) - 1:
                    if (tas_liste[satir_no][eleman] == tas_liste[satir_no][eleman+1] and
                            tas_liste[satir_no+1][eleman] == tas_liste[satir_no][eleman] and
                            tas_liste[satir_no+1][eleman] == tas_liste[satir_no+1][eleman+1]):

                        if tas_liste[satir_no][eleman] == "b":
                            oyuncu_kare_sayilari["beyaz_kare_sayi"] += 1
                        else:
                            oyuncu_kare_sayilari["siyah_kare_sayi"] += 1

                        if str(key_list[value_list[eleman]])+str(satir_no+1) not in kare_olusturan_tas_pozisyonlari:
                            kare_olusturan_tas_pozisyonlari.append(
                                (str(key_list[value_list[eleman]]) + str(satir_no + 1)))

                        if (str(key_list[value_list[eleman]]) + str(satir_no + 2)) not in kare_olusturan_tas_pozisyonlari:
                            kare_olusturan_tas_pozisyonlari.append((str(key_list[value_list[eleman]]) + str(satir_no + 2)))

                        if (str(key_list[value_list[eleman+1]])+str(satir_no+1)) not in kare_olusturan_tas_pozisyonlari:
                            kare_olusturan_tas_pozisyonlari.append((str(key_list[value_list[eleman+1]])+str(satir_no+1)))

                        if (str(key_list[value_list[eleman+1]])+str(satir_no+2)) not in kare_olusturan_tas_pozisyonlari:
                            kare_olusturan_tas_pozisyonlari.append((str(key_list[value_list[eleman+1]])+str(satir_no+2)))

        elif 0 < satir_no < len(tas_liste) - 1:  # son satir ve ilk satir haric aradaki satirlari tariyoruz
            for eleman in range(len(tas_liste[satir_no])):
                if eleman < len(tas_liste[satir_no]) - 1:
                    if (tas_liste[satir_no][eleman] == tas_liste[satir_no][eleman + 1] and
                            tas_liste[satir_no + 1][eleman] == tas_liste[satir_no][eleman] and
                            tas_liste[satir_no + 1][eleman] == tas_liste[satir_no + 1][eleman + 1]):

                        if tas_liste[satir_no][eleman] == "b":
                            oyuncu_kare_sayilari["beyaz_kare_sayi"] += 1
                        else:
                            oyuncu_kare_sayilari["siyah_kare_sayi"] += 1

                        if str(key_list[value_list[eleman]]) + str(satir_no + 1) not in kare_olusturan_tas_pozisyonlari:
                            kare_olusturan_tas_pozisyonlari.append(
                                (str(key_list[value_list[eleman]]) + str(satir_no + 1)))

                        if (str(key_list[value_list[eleman]]) + str(
                                satir_no + 2)) not in kare_olusturan_tas_pozisyonlari:
                            kare_olusturan_tas_pozisyonlari.append(
                                (str(key_list[value_list[eleman]]) + str(satir_no + 2)))

                        if (str(key_list[value_list[eleman + 1]]) + str(
                                satir_no + 1)) not in kare_olusturan_tas_pozisyonlari:
                            kare_olusturan_tas_pozisyonlari.append(
                                (str(key_list[value_list[eleman + 1]]) + str(satir_no + 1)))

                        if (str(key_list[value_list[eleman + 1]]) + str(
                                satir_no + 2)) not in kare_olusturan_tas_pozisyonlari:
                            kare_olusturan_tas_pozisyonlari.append(
                                (str(key_list[value_list[eleman + 1]]) + str(satir_no + 2)))

    return oyuncu_kare_sayilari, kare_olusturan_tas_pozisyonlari, tas_liste

def final_turu(tas_liste, default_dict, oyuncu_sira):

    oyuncu_kare_sayilari, kare_olusturan_tas_pozisyonlari, tas_liste = kareleri_say(tas_liste)  # kareleri_say dan donen degerleri degiskene attik
    harf_index_dict = harf_index_eslestir()
    oyuncu_1_silme_hakki = oyuncu_kare_sayilari["beyaz_kare_sayi"]
    oyuncu_2_silme_hakki = oyuncu_kare_sayilari["siyah_kare_sayi"]
    renk = ""   # tas listesinin son satirinin ilk elemani sıkıntı yaratıyordu onu cözmek icin boyle bi cozum buldum
    if len(tas_liste) == 3:
        renk = tas_liste[2][0]
    if len(tas_liste) == 4:
        renk = tas_liste[3][0]
    if len(tas_liste) == 5:
        renk = tas_liste[4][0]
    if len(tas_liste) == 6:
        renk = tas_liste[5][0]
    if len(tas_liste) == 7:
        renk = tas_liste[6][0]
    if len(tas_liste) == 8:
        renk = tas_liste[7][0]

    print(f"1. Oyuncu için oluşan toplam kare sayısı: {oyuncu_1_silme_hakki}" )
    print(f"2. Oyuncu için oluşan toplam kare sayısı: {oyuncu_2_silme_hakki}")


    if len(default_dict) > 0:   # hareket_ettir_kazan fonksiyonu cagirdiginda burasi calisacak
        oyuncu_1_silme_hakki = default_dict["oyuncu_1_silme_hakki"] # her bir tas hareketettirildiginde kare olusup olusmadıgına gore kare sayisi 1 veya 0 olur
        oyuncu_2_silme_hakki = default_dict["oyuncu_2_silme_hakki"]
    # 1. oyuncu icin hamle
    while oyuncu_1_silme_hakki != 0:
        print("Çıkarma Etabı: Beyaz taş için hamle sırası")
        atilacak_tas = atilacak_tas_input_checking(len(tas_liste)) # len(liste) aslinda hatali veri girinde kullaniliyor
        yatay_cizgi = int(atilacak_tas[0])  # ornegin 1A ise 1 e esit
        dikey_cizgi = harf_index_dict[atilacak_tas[1]]   # 1A ise A nin index nosuna esit
        # gecersiz girisler yeniden alinir
        while tas_liste[yatay_cizgi-1][dikey_cizgi] == "b" or tas_liste[yatay_cizgi-1][dikey_cizgi] == " " or  \
                (tas_liste[yatay_cizgi-1][dikey_cizgi] == "s" and  str(atilacak_tas[1]+atilacak_tas[0]) in kare_olusturan_tas_pozisyonlari):

            if tas_liste[yatay_cizgi-1][dikey_cizgi] == "b":
                print(f"{atilacak_tas} konumundaki taş beyaz taştır ve size aittir. Tekrar deneyiniz: ", end="")
                print("Çıkarma Etabı: Beyaz taş için hamle sırası")
                atilacak_tas = atilacak_tas_input_checking(len(tas_liste))
                yatay_cizgi = int(atilacak_tas[0])
                dikey_cizgi = harf_index_dict[atilacak_tas[1]]
                oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

            elif tas_liste[yatay_cizgi-1][dikey_cizgi] == " ":
                print(f"{atilacak_tas} konumundaki taşı zaten oyun alanından çıkarmışssınız. Tekrar deneyiniz: ",
                      end="")
                print("Çıkarma Etabı: Beyaz taş için hamle sırası")
                atilacak_tas = atilacak_tas_input_checking(len(tas_liste))
                yatay_cizgi = int(atilacak_tas[0])
                dikey_cizgi = harf_index_dict[atilacak_tas[1]]
                oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

            elif tas_liste[yatay_cizgi-1][dikey_cizgi] == "s" and  str(atilacak_tas[1]+atilacak_tas[0]) in kare_olusturan_tas_pozisyonlari:
                print(f"{atilacak_tas} konumundaki taş kare oluşturmaktadır.Tekrar deneyiniz: ", end="")
                print("Çıkarma Etabı: Beyaz taş için hamle sırası")
                atilacak_tas = atilacak_tas_input_checking(len(tas_liste))
                yatay_cizgi = int(atilacak_tas[0])
                dikey_cizgi = harf_index_dict[atilacak_tas[1]]
                oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

        else:
            tas_liste[yatay_cizgi-1][dikey_cizgi] = " "
            if (yatay_cizgi-1, dikey_cizgi) == (len(tas_liste)-1, 0):
                renk = " "
            oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi= renk)
        oyuncu_1_silme_hakki -= 1

    # 2. oyuncu icin hamle
    while oyuncu_2_silme_hakki != 0:
        print("Çıkarma etabı: Siyah taş için tamle sırası")
        atilacak_tas = atilacak_tas_input_checking(len(tas_liste))
        yatay_cizgi = int(atilacak_tas[0])
        dikey_cizgi = harf_index_dict[atilacak_tas[1]]

        while (tas_liste[yatay_cizgi-1][dikey_cizgi] == "s" or tas_liste[yatay_cizgi-1][dikey_cizgi] == " " or
                tas_liste[yatay_cizgi-1][dikey_cizgi] == "b" and str(atilacak_tas[1]+atilacak_tas[0]) in kare_olusturan_tas_pozisyonlari):

            if tas_liste[yatay_cizgi-1][dikey_cizgi] == "s":
                print(f"{atilacak_tas} konumundaki taş siyah taştır ve size aittir. Tekrar deneyiniz: ", end="")
                print("Çıkarma etabı: Siyah taş için tamle sırası")
                atilacak_tas = atilacak_tas_input_checking(len(tas_liste))
                yatay_cizgi = int(atilacak_tas[0])
                dikey_cizgi = harf_index_dict[atilacak_tas[1]]
                oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

            elif tas_liste[yatay_cizgi-1][dikey_cizgi] == " ":
                print(f"{atilacak_tas} konumundaki taşı zaten oyun alanından çıkarmışsınız. Tekrar deneyiniz: ",
                      end="")
                print("Çıkarma etabı: Siyah taş için tamle sırası")
                atilacak_tas = atilacak_tas_input_checking(len(tas_liste))
                yatay_cizgi = int(atilacak_tas[0])
                dikey_cizgi = harf_index_dict[atilacak_tas[1]]
                oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

            elif tas_liste[yatay_cizgi-1][dikey_cizgi] == "b" and str(atilacak_tas[1]+atilacak_tas[0]) in kare_olusturan_tas_pozisyonlari:
                print(f"{atilacak_tas} konumundaki taş kare oluşturmaktadır.Tekrar deneyiniz: ", end="")
                print("Çıkarma etabı: Siyah taş için tamle sırası")
                atilacak_tas = atilacak_tas_input_checking(len(tas_liste))
                yatay_cizgi = int(atilacak_tas[0])
                dikey_cizgi = harf_index_dict[atilacak_tas[1]]
                oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

        else:
            tas_liste[yatay_cizgi-1][dikey_cizgi] = " "  # o konumu bos string yapıyoruz
            if (yatay_cizgi-1, dikey_cizgi) == (len(tas_liste)-1, 0):  # sıkıntı cikaran konum (son satirin ilk sutununu) secerse ona gore parametreye gonderiyoruz
                renk = " "
            oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi= renk)

        oyuncu_2_silme_hakki -= 1
    oyuncu_sira -= 1  # hareket_ettir_kazan fonk. nun while dongusunu 1 azaltıyor her hamle yapısta
    hareket_ettir_kazan(tas_liste, oyuncu_sira)

def atilacak_tas_input_checking(tas_list_lenght):
    harf_index_dict = harf_index_eslestir()
    while True:
        try:
            atilacak_tas =  input("Çıkarmak istediğiniz rakip taşının konumunu giriniz (1A,4B...): ").upper()
            yatay_cizgi = int(atilacak_tas[0])
            dikey_cizgi = harf_index_dict[atilacak_tas[1]]
            while (len(atilacak_tas) > 2 or atilacak_tas.isdigit() or atilacak_tas.isalpha() or
                   yatay_cizgi not in range(0,tas_list_lenght+1)):
                print("Geçersiz veri girişi. Tekrar deneyiniz.")
                atilacak_tas = input("Çıkarmak istediğiniz rakip taşının konumunu giriniz (1A,4B...): ").upper()
        except (ValueError,KeyError,IndexError):
            print("Geçersiz veri girisi. Tekrar deneyiniz.")

        else:
            break

    return atilacak_tas

def hareket_ettir_kazan(tas_liste, oyuncu_sira):

    beyaz_tas_sayisi = 0  # her bir tas cikarmada yenilenirler
    siyah_tas_sayisi = 0  # eger ikisinden biri 3 e duserse oyun biter
    for i in tas_liste:
        for j in i:
            if j == "b":
                beyaz_tas_sayisi += 1
            elif j == "s":
                siyah_tas_sayisi +=1

    harf_index_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    renk = ""
    if len(tas_liste) == 3:
        renk = tas_liste[2][0]
    if len(tas_liste) == 4:
        renk = tas_liste[3][0]
    if len(tas_liste) == 5:
        renk = tas_liste[4][0]
    if len(tas_liste) == 6:
        renk = tas_liste[5][0]
    if len(tas_liste) == 7:
        renk = tas_liste[6][0]
    if len(tas_liste) == 8:
        renk = tas_liste[7][0]

    # cift ise beyaz hamle yapar, tek ise siyah
    while oyuncu_sira != 0:

        if beyaz_tas_sayisi == 3:
            print("Siyah taşlı oyuncu kazandı!")
            sys.exit()  # kazanan olustugunda program sonlanır
        elif siyah_tas_sayisi == 3:
            print("Beyaz taşlı oyuncu kazandı!")
            sys.exit()

        hareket_edilebilir = False

        if oyuncu_sira % 2 == 0:   # beyaz tas olan hamle yapar
            print("Hamle sırası beyaz taşta.")
            degistirilecek_taslar = degistirilecek_taslar_input_checking(len(tas_liste),len(tas_liste[0]))

            anlik_konum, gidilecek_konum = degistirilecek_taslar[0], degistirilecek_taslar[1]
            anlik_konum_satir, anlik_konum_sutun = int(anlik_konum[0]), harf_index_dict[anlik_konum[1]]
            gidilecek_konum_satir, gidilecek_konum_sutun = int(gidilecek_konum[0]), harf_index_dict[gidilecek_konum[1]]

            hareket_edilebilir = hareket_edilebilen_noktalari_bul(tas_liste, anlik_konum, gidilecek_konum) # returns True or False

            while (tas_liste[anlik_konum_satir-1][anlik_konum_sutun] == "s" or   # degistirilmek istenen tas icin gecersiz giris kontrolu
                   tas_liste[anlik_konum_satir-1][anlik_konum_sutun] == " " or
                   hareket_edilebilir == False):

                if tas_liste[anlik_konum_satir-1][anlik_konum_sutun] == "s":
                    print(f"{anlik_konum} konumunda siyah taş vardır. Sadece beyaz taşları hareket ettirebilirsiniz.")
                    print("Hamle sırası beyaz taşta.")

                    degistirilecek_taslar = degistirilecek_taslar_input_checking(len(tas_liste),len(tas_liste[0]))
                    anlik_konum, gidilecek_konum = degistirilecek_taslar[0], degistirilecek_taslar[1]
                    anlik_konum_satir, anlik_konum_sutun = int(anlik_konum[0]), harf_index_dict[anlik_konum[1]]
                    gidilecek_konum_satir, gidilecek_konum_sutun = int(gidilecek_konum[0]), harf_index_dict[
                        gidilecek_konum[1]]
                    hareket_edilebilir = hareket_edilebilen_noktalari_bul(tas_liste, anlik_konum, gidilecek_konum)
                    oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

                elif tas_liste[anlik_konum_satir-1][anlik_konum_sutun] == " ":
                    print(f"{anlik_konum} konumunda taş bulunmamaktadır. Tekrar deneyiniz: ",end="")
                    print("Hamle sırası beyaz taşta.")

                    degistirilecek_taslar = degistirilecek_taslar_input_checking(len(tas_liste),len(tas_liste[0]))
                    anlik_konum, gidilecek_konum = degistirilecek_taslar[0], degistirilecek_taslar[1]
                    anlik_konum_satir, anlik_konum_sutun = int(anlik_konum[0]), harf_index_dict[anlik_konum[1]]
                    gidilecek_konum_satir, gidilecek_konum_sutun = int(gidilecek_konum[0]), harf_index_dict[
                        gidilecek_konum[1]]
                    hareket_edilebilir = hareket_edilebilen_noktalari_bul(tas_liste, anlik_konum, gidilecek_konum)
                    oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

                elif hareket_edilebilir == False:
                    print(f"{gidilecek_konum} konumuna taşı hareket ettiremezsin. Tekrar deneyiniz: ")
                    print("Hamle sırası beyaz taşta.")

                    degistirilecek_taslar = degistirilecek_taslar_input_checking(len(tas_liste),len(tas_liste[0]))
                    anlik_konum, gidilecek_konum = degistirilecek_taslar[0], degistirilecek_taslar[1]
                    anlik_konum_satir, anlik_konum_sutun = int(anlik_konum[0]), harf_index_dict[anlik_konum[1]]
                    gidilecek_konum_satir, gidilecek_konum_sutun = int(gidilecek_konum[0]), harf_index_dict[
                        gidilecek_konum[1]]
                    hareket_edilebilir = hareket_edilebilen_noktalari_bul(tas_liste, anlik_konum, gidilecek_konum)
                    oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

            else:

                tas_liste[anlik_konum_satir - 1][anlik_konum_sutun] = " "
                tas_liste[gidilecek_konum_satir-1][gidilecek_konum_sutun] = "b"
                if (gidilecek_konum_satir - 1, gidilecek_konum_sutun) == (len(tas_liste) - 1, 0):
                    renk = "b"
                if (anlik_konum_satir - 1, anlik_konum_sutun) == (len(tas_liste) - 1, 0):
                    renk = " "
                oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

                oyuncu_kare_sayilari, kare_olusturan_tas_pozisyonlari, tas_liste = kareleri_say(tas_liste)

                if str(gidilecek_konum[1])+str(gidilecek_konum[0]) in kare_olusturan_tas_pozisyonlari:
                    oyuncu_kare_sayilari = {"oyuncu_1_silme_hakki":1,"oyuncu_2_silme_hakki":0}
                    final_turu(tas_liste, oyuncu_kare_sayilari, oyuncu_sira)
                else:
                    oyuncu_kare_sayilari = {"oyuncu_1_silme_hakki": 0, "oyuncu_2_silme_hakki": 0}
                    final_turu(tas_liste, oyuncu_kare_sayilari, oyuncu_sira)

        else:  # siyah tas olan hamle yapar
            print("Hamle sırası siyah taşta")
            degistirilecek_taslar = degistirilecek_taslar_input_checking(len(tas_liste),len(tas_liste[0]))
            anlik_konum, gidilecek_konum = degistirilecek_taslar[0], degistirilecek_taslar[1]
            anlik_konum_satir, anlik_konum_sutun = int(anlik_konum[0]), harf_index_dict[anlik_konum[1]]
            gidilecek_konum_satir, gidilecek_konum_sutun = int(gidilecek_konum[0]), harf_index_dict[gidilecek_konum[1]]
            hareket_edilebilir = hareket_edilebilen_noktalari_bul(tas_liste, anlik_konum, gidilecek_konum)

            while (tas_liste[anlik_konum_satir - 1][anlik_konum_sutun] == "b" or  # degistirilmek istenen tas icin
                   tas_liste[anlik_konum_satir - 1][anlik_konum_sutun] == " " or
                   hareket_edilebilir == False):


                if tas_liste[anlik_konum_satir - 1][anlik_konum_sutun] == "b":
                    print(f"{anlik_konum} konumunda beyaz taş vardır. Sadece siyah taşları hareket ettirebilirsiniz.")
                    print("Hamle sırası siyah taşta")
                    degistirilecek_taslar = degistirilecek_taslar_input_checking(len(tas_liste),len(tas_liste[0]))
                    anlik_konum, gidilecek_konum = degistirilecek_taslar[0], degistirilecek_taslar[1]
                    anlik_konum_satir, anlik_konum_sutun = int(anlik_konum[0]), harf_index_dict[anlik_konum[1]]
                    gidilecek_konum_satir, gidilecek_konum_sutun = int(gidilecek_konum[0]), harf_index_dict[
                        gidilecek_konum[1]]
                    hareket_edilebilir = hareket_edilebilen_noktalari_bul(tas_liste, anlik_konum, gidilecek_konum)
                    oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

                elif tas_liste[anlik_konum_satir - 1][anlik_konum_sutun] == " ":
                    print(f"{anlik_konum} konumunda taş bulunmamaktadır. Tekrar deneyiniz: ", end="")
                    print("Hamle sırası siyah taşta")
                    degistirilecek_taslar = degistirilecek_taslar_input_checking(len(tas_liste),len(tas_liste[0]))
                    anlik_konum, gidilecek_konum = degistirilecek_taslar[0], degistirilecek_taslar[1]
                    anlik_konum_satir, anlik_konum_sutun = int(anlik_konum[0]), harf_index_dict[anlik_konum[1]]
                    gidilecek_konum_satir, gidilecek_konum_sutun = int(gidilecek_konum[0]), harf_index_dict[
                        gidilecek_konum[1]]
                    hareket_edilebilir = hareket_edilebilen_noktalari_bul(tas_liste, anlik_konum, gidilecek_konum)
                    oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

                elif  hareket_edilebilir == False:
                    print(f"{gidilecek_konum} konumuna taşı hareket ettiremezsin. Tekrar deneyiniz: ")
                    print("Hamle sırası siyah taşta")
                    degistirilecek_taslar = degistirilecek_taslar_input_checking(len(tas_liste),len(tas_liste[0]))
                    anlik_konum, gidilecek_konum = degistirilecek_taslar[0], degistirilecek_taslar[1]
                    anlik_konum_satir, anlik_konum_sutun = int(anlik_konum[0]), harf_index_dict[anlik_konum[1]]
                    gidilecek_konum_satir, gidilecek_konum_sutun = int(gidilecek_konum[0]), harf_index_dict[
                        gidilecek_konum[1]]
                    hareket_edilebilir = hareket_edilebilen_noktalari_bul(tas_liste, anlik_konum, gidilecek_konum)
                    oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

            else:

                tas_liste[anlik_konum_satir - 1][anlik_konum_sutun] = " "
                tas_liste[gidilecek_konum_satir - 1][gidilecek_konum_sutun] = "s"

                if (gidilecek_konum_satir - 1, gidilecek_konum_sutun) == (len(tas_liste) - 1, 0):
                    renk = "s"
                if (anlik_konum_satir - 1, anlik_konum_sutun) == (len(tas_liste) - 1, 0):
                    renk = " "
                oyun_tahtasi_goruntule(tas_liste, len(tas_liste), len(tas_liste[0]), tas_rengi=renk)

                oyuncu_kare_sayilari, kare_olusturan_tas_pozisyonlari, tas_liste = kareleri_say(tas_liste)

                if str(gidilecek_konum[1]) + str(gidilecek_konum[0]) in kare_olusturan_tas_pozisyonlari:
                    oyuncu_kare_sayilari = {"oyuncu_1_silme_hakki": 0, "oyuncu_2_silme_hakki": 1}
                    final_turu(tas_liste, oyuncu_kare_sayilari, oyuncu_sira)
                else:
                    oyuncu_kare_sayilari = {"oyuncu_1_silme_hakki": 0, "oyuncu_2_silme_hakki": 0}
                    final_turu(tas_liste, oyuncu_kare_sayilari, oyuncu_sira)

def degistirilecek_taslar_input_checking(tas_list_satir_lenght, tas_list_sutun_lenght):
    harf_index_dict = harf_index_eslestir()
    # yerleri degisecek taslarin kontrolunu yapar
    while True:
        try:
            degistirilecek_taslar = input("Yerini değiştirmek istediginiz taşın şu anki konumunu ve"
                                    " taşımak istediginiz yerin konumunu giriniz (1A 3B..): ").upper().split()
            anlik_konum, gidilecek_konum = degistirilecek_taslar[0], degistirilecek_taslar[1]
            anlik_konum_satir, anlik_konum_sutun = int(anlik_konum[0]), harf_index_dict[anlik_konum[1]]
            gidilecek_konum_satir, gidilecek_konum_sutun = int(gidilecek_konum[0]), harf_index_dict[gidilecek_konum[1]]

            while (degistirilecek_taslar[0].isdigit() or degistirilecek_taslar[0].isalpha() or
                   degistirilecek_taslar[1].isdigit() or degistirilecek_taslar[1].isalpha() or
                   degistirilecek_taslar[0] == degistirilecek_taslar[1] or anlik_konum_satir not in range(1,tas_list_satir_lenght+1)
                    or anlik_konum_sutun not in range(0,tas_list_sutun_lenght +1) or
                   gidilecek_konum_satir not in range(1,tas_list_satir_lenght+1) or gidilecek_konum_sutun not in range(0,tas_list_sutun_lenght +1)):

                print("Geçersiz veri girişi. Tekrar deneyiniz.")
                degistirilecek_taslar = input("Yerini değiştirmek istediginiz taşın şu anki konumunu ve"
                                              " taşımak istediginiz yerin konumunu giriniz (1A 3B..): ").upper().split()

        except (ValueError, KeyError, IndexError):
            print("Geçersiz veri girişi. Tekar deneyiniz.")

        else:
            break
    return degistirilecek_taslar  # degistirilecek taslari dondurur

def hareket_edilebilen_noktalari_bul(tas_liste, anlik_konum, gidilecek_konum):
    harf_index_dict = harf_index_eslestir()
    anlik_konum_satir, anlik_konum_sutun = int(anlik_konum[0]), harf_index_dict[anlik_konum[1]]
    gidilecek_konum_satir, gidilecek_konum_sutun = int(gidilecek_konum[0]), harf_index_dict[gidilecek_konum[1]]
    buyuk_olan_sutun_no = 0  # bunlar taslarin soldan saga mi yoksa sagdan sola mı hareket edecegini kontrol etmek icin olusturuldu
    kucuk_olan_sutun_no = 0
    buyuk_olan_satir_no = 0  #bunlar taslariny yukardan asagıya mi yoksa asagıdan yukarı mı hareket edecegini kontrol etmek icin olusturuldu
    kucuk_olan_satir_no = 0
    if anlik_konum_sutun > gidilecek_konum_sutun:
        buyuk_olan_sutun_no = anlik_konum_sutun
        kucuk_olan_sutun_no = gidilecek_konum_sutun

    elif gidilecek_konum_sutun > anlik_konum_sutun:
        buyuk_olan_sutun_no = gidilecek_konum_sutun
        kucuk_olan_sutun_no = anlik_konum_sutun

    if anlik_konum_satir > gidilecek_konum_satir:
        buyuk_olan_satir_no = anlik_konum_satir
        kucuk_olan_satir_no = gidilecek_konum_satir

    elif gidilecek_konum_satir > anlik_konum_satir:
        buyuk_olan_satir_no = gidilecek_konum_satir
        kucuk_olan_satir_no = anlik_konum_satir

    if (tas_liste[anlik_konum_satir-1][anlik_konum_sutun] == "b" and tas_liste[gidilecek_konum_satir-1][gidilecek_konum_sutun] == "s"
         or (tas_liste[anlik_konum_satir-1][anlik_konum_sutun] == "s" and tas_liste[gidilecek_konum_satir-1][gidilecek_konum_sutun] == "b")):
        return False

    if anlik_konum_satir == gidilecek_konum_satir:  # ayni satirdalarsa

        if kucuk_olan_sutun_no + 1 == buyuk_olan_sutun_no:
            if buyuk_olan_sutun_no == anlik_konum_sutun: # hareket ettirilecek tas gidilecek konumun sagindaysa
                if tas_liste[anlik_konum_satir - 1][kucuk_olan_sutun_no] == "b" or tas_liste[anlik_konum_satir - 1][kucuk_olan_sutun_no] == "s":
                    return False

            elif kucuk_olan_sutun_no == anlik_konum_sutun:
                if tas_liste[anlik_konum_satir - 1][buyuk_olan_sutun_no] == "b" or tas_liste[anlik_konum_satir - 1][buyuk_olan_sutun_no] == "s":
                    return False

        else:
            for i in range(kucuk_olan_sutun_no+1, buyuk_olan_sutun_no):   # 7f 7d 3 5
                if tas_liste[anlik_konum_satir -1][i] == "b" or tas_liste[anlik_konum_satir -1][i] == "s":
                    return False

    elif anlik_konum_satir != gidilecek_konum_satir and anlik_konum_sutun == gidilecek_konum_sutun: # farklı satir ama aynı sutunda ise
        if kucuk_olan_satir_no + 1 == buyuk_olan_satir_no:
            if buyuk_olan_satir_no == anlik_konum_satir:
                if tas_liste[kucuk_olan_satir_no - 1][anlik_konum_sutun] == "b" or tas_liste[kucuk_olan_satir_no - 1][anlik_konum_sutun] == "s":
                    return False

            elif kucuk_olan_satir_no == anlik_konum_satir: # 7f 7d
                print(tas_liste[gidilecek_konum_satir-1])
                if tas_liste[gidilecek_konum_satir - 1][anlik_konum_sutun] == "b" or tas_liste[gidilecek_konum_satir - 1][anlik_konum_sutun] == "s":
                    return False

        else:
            for i in range(kucuk_olan_satir_no + 1, buyuk_olan_satir_no):
                if tas_liste[i-1][anlik_konum_sutun] == "b" or tas_liste[i-1][anlik_konum_sutun] == "s":
                    return False

    else:
        return False  # hamle yapamaz yani ayni satir ve sutunda degil

    return True  # hamle yapabilir

def harf_index_eslestir():  # harfleri indexlere gore eslestiren fonksiyon
    harf_index_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    return  harf_index_dict

yatay_cizgi_al() # bu fonk cagirilir ve program baslar.