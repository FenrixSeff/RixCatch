# RixCatch
**Script Python** untuk mengunduh video, audio, atau thumbnail dari YouTube menggunakan yt-dlp. Dirancang untuk kemudahan dan efisiensi.

## Features
- Download video
- Pilih audio bitrate sesuai kebutuhan (128–320 kbps)
- Download thumbnail saja (format JPG/PNG)
- User friendly

## Dependencies
- Python 3
- yt-dlp
- colorama
- pyfiglet
- termux-api (untuk scan media)
- Termux dengan izin storage (`termux-setup-storage`)

## How to install RixCatch
```bash
pkg install git
git clone https://github.com/FenrixSeff/RixCatch.git
cd RixCatch
```

## Install Dependencies
```bash
./requirements.sh
```

## How to use
```bash
python RixCatch.py
```
Masukkan URL video YouTube, pilih opsi download (video, audio, thumbnail), lalu tunggu proses selesai.

## Notes
- Jika resolusi/bitrate tidak tersedia, akan otomatis disesuaikan ke yang tersedia
- Folder otomatis dibuat di:
  - `~/storage/shared/DCIM/` (video/thumbnail)
  - `~/storage/shared/YMusic/` (audio)

## License
Open-source, bebas digunakan dan dimodifikasi.

## Authors
Fenrix
