# 🔥 SMASH — 7+ Layer DDoS Ultimate

**SMASH** adalah alat uji penetrasi (penetration testing) yang dirancang untuk mensimulasikan serangan DDoS (Distributed Denial of Service) dengan **9 metode serangan** berbeda, mencakup lapisan 3 hingga 7. Script ini hanya untuk tujuan edukasi dan pengujian keamanan pada sistem yang kamu miliki atau dengan izin tertulis dari pemilik sistem.

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

## 📦 Persyaratan

- Modul `requests`
- (Opsional) Hak akses root untuk ICMP Flood.

---

## 🛠️ Instalasi & Penggunaan
bash```
pkg update && pkg upgrade
pkg install python
pkg install git
pkg install openssl-tool
pip install requests
git clone https://github.com/vsa-html/smash.git
cd smash

## 📱 Jalankan
bash```
python main.py
