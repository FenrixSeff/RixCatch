#!/data/data/com.termux/files/usr/bin/bash

echo -e "\nUpdate package list..\n"
pkg update

echo -e "\nInstalling dependencis system..\n"
pkg install -y python
pkg install -y ffmpeg
pkg install -y termux-api

echo -e "\nInstalling dependencis Python..\n"
pip install colorama
pip install pyfiglet
pip install yt-dlp

echo -e "\nAllow storage access\n"
termux-setup-storage
