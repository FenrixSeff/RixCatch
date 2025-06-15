#!/usr/bin/env python

import os
import time
import subprocess
import threading
import pyfiglet
from pathlib import Path
from colorama import Fore, Back, Style


b_g = Back.GREEN
m = Fore.MAGENTA
b = Fore.BLUE       #\   ______________   /#
g = Fore.GREEN       #\  |            |  /#
y = Fore.YELLOW       #\ |    CODE    | /#
r = Fore.RED          #/ | EFFICIENCY | \#
c = Fore.CYAN        #/  |____________|  \#
w = Fore.WHITE      #/                    \#
B = Fore.BLACK
R = Style.RESET_ALL


def loading(teks):  # Animasi loading
    repeat = ["|", "/", "-", "\\"]
    f = 0
    while not done:
        print(f"\r{teks} {repeat[f % len(repeat)]} ", end="")
        f += 1
        time.sleep(1)


res = ["2160", "1440", "1080", "720", "480", "360", "240", "144"]

def vid_res():  # Index resolusi video
    while True:
        u = int(input(y + "\nSelect option: " + R))
        print("")
        if u in[1, 2, 3, 4, 5, 6, 7, 8]:
            break
        print("Pilih 1-8\n")
    u -= 1
    slct = res[u]
    return slct

def choice_vid(pix, url):   # Download video
    vid = subprocess.Popen(
        ["yt-dlp", "-f", f"bestvideo[height<={pix}][ext=mp4]"
                         f"+bestaudio[ext=m4a]",
        "--embed-thumbnail", "--embed-metadata",
        "-P", "~/storage/shared/DCIM/Video", f"{url}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        text=True   # → Jika ingin memunculkann informasi, rubah
    )               # DEVNULL menjadi PIPE ~Fenrix
    return vid


brt = ["0", "1", "2", "3", "4", "5"]

def aud_brt():  # Index bitrate audio
    while True:
        u = int(input(y + "\nSelect option: " + R))
        print("")
        if u in[1, 2, 3, 4, 5, 6]:
            break
        print("Pilih 1-6\n")
    u -= 1
    slct = brt[u]
    return slct

def choice_aud(pix, url):   # Download audio
    aud = subprocess.Popen(
        ["yt-dlp", "-f", "bestaudio", "--extract-audio",
        "--audio-format=mp3", f"--audio-quality={pix}",
        "--embed-thumbnail", "--embed-metadata", "-P",
        "~/storage/shared/YMusic", f"{url}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        text=True
    )
    return aud


pict = ["jpg", "png"]

def tum_frm():  # Index format gambar
    while True:
        u = int(input(y + "\nSelect option: " + R))
        print("")
        if u in[1, 2]:
            break
        print("Pilih 1-2\n")
    u -= 1
    slct = pict[u]
    return slct

def choice_tum(pix, url):   # Download gambar
    tum = subprocess.Popen(
        ["yt-dlp", "--skip-download", "--write-thumbnail",
        f"--convert-thumbnail={pix}", "-P",
        "~/storage/shared/DCIM/Thumbnail", f"{url}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        text=True
    )
    return tum


def scan(loc):  # Perlu install termux-api → (pkg install termux-api)
    track = Path.home() / f"storage/shared/{loc}"
    cek = subprocess.run(
        ["termux-media-scan", track],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        text=True
    )
    print("")
    print(g + "\nDownload complete.." + R)
    return cek


vid_opt = {"pilihan": {"[1]": "4K UHD", "[2]": "2K QHD",
           "[3]": "1080p", "[4]": "720p", "[5]": "480p",
           "[6]": "360p", "[7]": "240p", "[8]": "144p"}}

aud_opt = {"pilihan": {"[1]": "320 kbps", "[2]": "256 kbps",
           "[3]": "224 kbps", "[4]": "192 kbps", "[5]": "160 kbps",
           "[6]": "128 kbps"}}

need_frm = {"auvi": {"[1]": "Thumbnail only",
           "[2]": "Video", "[3]": "Audio only", "[4]": "Info",
           "[0]": "Exit"},
           "frm_pict": {"[1]": "JPG", "[2]": "PNG"}}

info_vid = (g + "Catatan: Jika resolusi yang kamu pilih "
            "tidak tersedia, sistem akan otomatis mengunduh "
            "dengan resolusi tertinggi di bawahnya." + R)

info_aud = (g + "Catatan: Jika bitrate yang kamu pilih "
            "tidak tersedia, sistem akan otomatis mengunduh "
            "dengan bitrate tertinggi di bawahnya." + R)

thx = (g + "\nTerima kasih telah menggunakan script ini. Jika Anda "
       "memiliki saran atau masukan, silakan hubungi pengembang untuk "
       "peningkatan lebih lanjut. ~Fenrix\n" + R)


print(g + "\nInformation: " + R + "Tool ini adalah versi "
      "instan dari" + r + " [yt-dlp] " + R + "\ndirancang "
      "untuk memberikan pengalaman yang lebih sesuai kebutuhan.\n")
time.sleep(0.5)

print(r + pyfiglet.figlet_format("RixCatch", font="smslant") + R)
print("_"* 25, "v.7.05.08")
print(g + "\nPeringatan!: " + R + "Script ini Masih butuh "
      "debugging & banyak asupan kopi!")

loc_sto = Path.home() / "storage"
loc_aud = Path.home() / "storage/shared/YMusic"

if not loc_sto.exists():
    os.system("termux-setup-storage")

for folder in["Video", "Thumbnail"]:
    path = Path.home() / f"storage/shared/DCIM/{folder}"
    path.mkdir(parents=True, exist_ok=True)

loc_aud.mkdir(parents=True, exist_ok=True)

print(m + "\n⟩——URL——⟨" + R)
url = input("")
print("")
done = False
t = threading.Thread(target=loading, args=("[?] Mencari..",))
t.start()
search = subprocess.run(
    ["yt-dlp", "--get-filename", "-o", "%(title)s", url],
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,
    stdin=subprocess.DEVNULL,
    text=True
    )

done = True
t.join()
time.sleep(0.3)
title = search.stdout.strip()
if not title:
    print("")
    print(
    r + "\nUps! Sepertinya ada masalah. Cek URL yang Anda masukkan "
    "atau coba lagi nanti.\n" + R)
    exit()  # ← Jangan dihapus

print("\n")
print(f"»»» {b_g + B + title + R} «««")
print(m + "\n⟩——Option——⟨\n" + R)
for opsi, isi in need_frm["auvi"].items():
    print(f"{opsi} {isi}")

while True:
    user = input(y + "\nSelect option: " + R).strip()
    if user in["1", "2", "3", "4", "5",]:
        break

    elif user == "0":
        print(thx)
        exit()
    print(r + "Pilih 1-4 untuk memilih opsi " + R)

if user == "1":   # download thumbnail
    time.sleep(0.3)
    print(m + "\n⟩——Format——⟨\n" + R)
    for opsi, isi in need_frm["frm_pict"].items():
        print(f"{opsi} {isi}")

    user_pref = tum_frm()
    user_slct = choice_tum(user_pref, url)
    done = False
    t = threading.Thread(target=loading, args=("[↓] Mengunduh..",))
    t.start()
    user_slct.wait()
    done = True
    t.join()
    scan("DCIM/Thumbnail")


elif user == "2":   # download video
    while True:
        response = input(g + "Unduh dengan kualitas "
                         "tertinggi yang TERSEDIA pada video?" + R
                         + w + "\n(N)ext o(P)tion e(X)it: " + R).strip()
        if response.lower() in["n", "p", "x"]:
            break
        print(r + "\nPilih opsi yang tersedia!" + R)

    if response.lower() == "n":
        i = "2160"
        user_slct = choice_vid(i, url)
        done = False
        t = threading.Thread(target=loading, args=("[↓] Mengunduh..",))
        t.start()
        user_slct.wait()
        done = True
        t.join()
        scan("DCIM/Video")

    elif response.lower() == "p":
        time.sleep(0.3)
        print(m + "\n⟩——Resolution——⟨\n" + R)
        for opsi, isi in vid_opt["pilihan"].items():
            print(f"{opsi} {isi}")
        print(f"\n{info_vid}")

        user_pref = vid_res()
        user_slct = choice_vid(user_pref, url)
        done = False
        t = threading.Thread(target=loading, args=("[↓] Mengunduh..",))
        t.start()
        user_slct.wait()
        done = True
        t.join()
        scan("DCIM/Video")

    elif response.lower() == "x":
        print(thx)
        exit()


elif user == "3":    # download audio
    while True:
        response = input(g + "Unduh dengan kualitas "
                         "tertinggi yang TERSEDIA pada audio" + R
                         + w + "\n(N)ext o(P)tion e(X)it: " + R).strip()
        if response.lower() in["n", "p", "x"]:
            break
        print(r + "\nPilih opsi yang tersedia!" + R)

    if response.lower() == "n":
        i = "0"
        user_slct = choice_aud(i, url)
        done = False
        t = threading.Thread(target=loading, args=("[↓] Mengunduh..",))
        t.start()
        user_slct.wait()
        done = True
        t.join()
        scan("YMusic")

    elif response.lower() =="p":
        time.sleep(0.3)
        print(m + "\n⟩——Bitrate——⟨\n" + R)
        for opsi, isi in aud_opt["pilihan"].items():
            print(f"{opsi} {isi}")
        print(f"\n{info_aud}")

        user_pref = aud_brt()
        user_slct = choice_aud(user_pref, url)
        done = False
        t = threading.Thread(target=loading, args=("[↓] Mengunduh..",))
        t.start()
        user_slct.wait()
        done = True
        t.join()
        scan("YMusic")

    elif response.lower() == "x":
        print(thx)
        exit()

elif user == "4":
    print(
    "• Information: \nPengunduhan video short masih belum optimal "
    "dan masih dalam tahap improvisasi\n"
    "• How to use: \nMasukkan URL video, pilih format,"
    "lalu tekan enter. Hanya itu saja!\n"
    "~Fenrix")

elif user == "5":
    subprocess.run(
    ["yt-dlp", "-F", f"{url}"]
    )
