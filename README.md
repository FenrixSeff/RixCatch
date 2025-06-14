# RixCatch
**Script Python berbasis Termux** untuk mengunduh video, audio, atau thumbnail dari YouTube menggunakan yt-dlp. Dirancang untuk kemudahan dan efisiensi.


## Fitur Utama
- Unduh video hingga resolusi 4K
- Pilih audio bitrate sesuai kebutuhan (128–320 kbps)
- Download thumbnail saja (format JPG/PNG)
- Tampilan CLI interaktif dan estetis
- Scan otomatis file media (butuh `termux-api`)


## Ketergantungan
- Python 3
- yt-dlp
- colorama
- pyfiglet
- termux-api (untuk scan media)
- Termux dengan izin storage (`termux-setup-storage`)


## Cara Menjalankan
```bash
python RixCatch.py

Masukkan URL video YouTube, pilih opsi download (video, audio, thumbnail), lalu tunggu proses selesai.


## Catatan

Jika resolusi/bitrate tidak tersedia, akan otomatis disesuaikan ke
yang tersedia.

Folder otomatis dibuat di ~/storage/shared/DCIM/ dan ~/storage/shared/YMusic.


## Pengembang

Script dibuat oleh Fenrix, dibuat dengan semangat belajar dan ngopi ☕
Kalau ada saran atau bug, jangan ragu hubungi atau buka Issue di GitHub.


## Lisensi

Open-source, bebas digunakan dan dimodifikasi.
