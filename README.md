# 🔥 SMASH — 7+ Layer DDoS Ultimate

**SMASH** adalah alat uji penetrasi (penetration testing) yang dirancang untuk mensimulasikan serangan DDoS (Distributed Denial of Service) dengan **8 metode serangan** berbeda, mencakup lapisan 3 hingga 7. Script ini hanya untuk tujuan edukasi dan pengujian keamanan pada sistem yang kamu miliki atau dengan izin tertulis dari pemilik sistem.

> ⚠️ **PERINGATAN:** Penggunaan tanpa izin adalah tindakan ilegal dan dapat dikenai sanksi pidana sesuai UU ITE dan undang‑undang lainnya. Penulis tidak bertanggung jawab atas penyalahgunaan.

---

## 🚀 Fitur Utama

- ✅ **9 Metode Serangan** — ICMP Flood, UDP Flood, TCP SYN Flood, DNS Amplification, SSL Renegotiation, HTTP GET Flood, HTTP POST Flood, Slowloris.
- ✅ **Multi‑threading** — Atur jumlah thread hingga ribuan.
- ✅ **Durasi Fleksibel** — Tentukan durasi serangan atau jalankan tanpa batas (unlimited).
- ✅ **Pilihan Metode Bebas** — Pilih satu metode atau jalankan semua secara acak.
- ✅ **Terminal Warna** — Tampilan yang nyaman dengan kode ANSI.
- ✅ **ICMP Flood (Root)** — Mendukung serangan ICMP jika dijalankan sebagai root.

---



## 🛠️ Instalasi Keperluan
```bash
pkg update && pkg upgrade
pkg install python
pkg install git
pkg install openssl-tool
pip install requests
```
---

## 📁 Instalasi Git
```bash
git clone https://github.com/vsa-html/smash.git
```
---

## 📱 Jalankan
```bash
cd smash
python main.py
```
---

## 📦 Persyaratan

- Modul `requests`
- (Opsional) Hak akses root untuk ICMP Flood.
- Aplikasi Termux

---

## Peringkat Metode Layer Kekuatan

1- *UDP Flood* `⭐⭐⭐⭐⭐` 

Paling brutal buat server yang gak pake proteksi. Bisa bikin mati total dalam detik.

##

2- *HTTP Flood*  `⭐⭐⭐⭐½`

Sangat ganas buat web server. Memakan resource CPU & RAM.

##

3- *TCP SYN Flood* `⭐⭐⭐⭐`

Bikin server kehabisan koneksi (half-open connections).

##

4- *DNS Amplification* `⭐⭐⭐½`

Efek besar kalo target pake DNS. Bisa amplify traffic 50-100x.

##

5- *Slowloris* `⭐⭐⭐`

Halus tapi mematikan. Bikin server kehabisan thread.

##

6- *HTTP POST Flood* `⭐⭐⭐`

Mirip HTTP Flood, tapi lebih berat di server.

##

7- *SSL Renegotiation* `⭐⭐½`

Lumayan buat server HTTPS, tapi butuh resource lebih.

##

8- *ICMP Flood* `⭐⭐`

Paling lemah kalo target pake firewall, butuh root.

---

## Rekomendasi Gw:

1- Kalo target web biasa → Pilih `UDP` `Flood` (nomor 2)

##

2- Kalo target pake Cloudflare → Pilih `HTTP Flood` (nomor 6)

##

3- Kalo target pake HTTPS → Pilih `SSL` `Renegotiation` (nomor 5)

##

4- Kalo target server lemah → Pilih `Slowloris` (nomor 8)
