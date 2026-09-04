# 🔥 SMASH XSO — 7+ Layer DDoS Ultimate

**SMASH XSO** adalah alat uji penetrasi (penetration testing) yang dirancang untuk mensimulasikan serangan DDoS (Distributed Denial of Service) dengan **9 metode serangan** berbeda, mencakup lapisan 3 hingga 7. Script ini hanya untuk tujuan edukasi dan pengujian keamanan pada sistem yang kamu miliki atau dengan izin tertulis dari pemilik sistem.

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

- Python 3.x
- Modul `requests`
- (Opsional) Hak akses root untuk ICMP Flood.

---

## 🛠️ Instalasi & Penggunaan
bash```
# 1. Install dependencies dasar
pkg update && pkg upgrade -y
pkg install python -y
pkg install git -y
pkg install openssl-tool -y

# 2. Install module Python
pip install requests

# 3. Clone repo dari GitHub
git clone https://github.com/username/repo-name.git

# 4. Masuk ke folder hasil clone
cd smash

# 5. Jalankan script
python main.py
