#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İş Yapmama İçin Gerekçeli Bahane Üretici
Bu kod, bilimsel olarak kanıtlanmış bahaneler üretir.
Hiçbir zaman iş yapmamak için tasarlanmıştır.
"""

import random
import datetime

def bahane_uret():
    basliklar = [
        "Kuantum fiziği nedeniyle bugün iş yapamam",
        "Kedi evde tek başına üzgün, psikolojik destek veriyorum",
        "Kahve makinesi varolusal kriz geçiriyor, ona eşlik ediyorum",
        "Hava durumu algoritması beni uyardı: iş yapmak tehlikeli",
        "Beynim bugün tatilde, yedek beyin gelmedi",
        "Uzaylılar sinyal gönderdi, cevap vermem lazım",
        "Ayak parmaklarım sayım yapıyor, bitmesini bekliyorum",
        "Rüzgar yönü değişti, felsefi düşünmem gerekiyor",
        "Bürokrasi bir sonraki şey için izin bekliyor",
        "Seçim vaatleri henüz gerçekleşmedi, motivasyon yok"  # gizli siyasi dokunuş
    ]
    
    detaylar = [
        "Bu durum bilimsel olarak 47 makalede incelenmiştir.",
        "WHO tarafından da onaylanmış bir durumdur.",
        "Yapay zeka bile bunu öneriyor.",
        "Tarihte hiç kimse bu bahaneyi çürütememiştir.",
        "Kanıtlar için README'ye bakınız."
    ]
    
    bahane = random.choice(basliklar)
    detay = random.choice(detaylar)
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    return f"[{zaman}] {bahane}. {detay}"

if __name__ == "__main__":
    print("🚨 İŞ YAPMAMA SİSTEMİ AKTİF 🚨")
    print("Bugünkü resmi bahane:")
    print(bahane_uret())
    print("\nNot: Bu sistem her çalıştırıldığında yeni bir bahane üretir. Sonsuz döngü önerilir.")
