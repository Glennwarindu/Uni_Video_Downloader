#!/usr/bin/env python3
"""
universal_downloader.py

Download videos from Facebook, Instagram, YouTube, TikTok, Twitter, Reddit, and more.

Usage:
  python3 universal_downloader.py <URL> [--cookies cookies.txt] [--output-dir ./videos]

Requirements:
  - Python 3.8+
  - pip install yt-dlp
  - ffmpeg installed (for best quality merging)
"""

import argparse
import os
import sys
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

def download_video(url: str, cookies: str | None, outdir: str):
    ydl_opts = {
        'outtmpl': os.path.join(outdir, '%(extractor)s/%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'quiet': False,
        'no_warnings': True,
        'retries': 3,
        'continuedl': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117 Safari/537.36'
        }
    }

    if cookies:
        if not os.path.isfile(cookies):
            print(f"[!] Cookies file not found: {cookies}")
            return False
        ydl_opts['cookiefile'] = cookies

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print(f"[+] Downloading: {url}")
            info = ydl.extract_info(url, download=True)
            if info is None:
                print("[!] No info extracted — maybe invalid or private URL.")
                return False
            print(f"[+] Done: {info.get('title', 'Unknown title')}")
            return True
    except DownloadError as e:
        print("[!] DownloadError:", e)
        return False
    except Exception as e:
        print("[!] Unexpected error:", type(e).__name__, e)
        return False

def main():
    parser = argparse.ArgumentParser(description="Universal video downloader using yt-dlp")
    parser.add_argument('url', help='Video URL (Facebook, Instagram, YouTube, etc.)')
    parser.add_argument('--cookies', '-c', help='Path to cookies.txt (optional)', default=None)
    parser.add_argument('--output-dir', '-o', help='Output directory', default='./videos')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    success = download_video(args.url, args.cookies, args.output_dir)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()

