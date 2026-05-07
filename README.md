# UNIDOWNLOADER

Unidownloader is a lightweight Python-based video downloader built using `yt-dlp`.
It is designed to help download videos from multiple platforms, including sites with restricted or authenticated content access.

Tested platforms so far:

* Facebook
* Vecteezy

The script supports:

* High-quality video/audio downloads
* Automatic stream merging with ffmpeg
* Cookies support for logged-in sessions
* Automatic `videos/` folder creation
* Organized output folders by platform
* Simple command-line usage

---

# Requirements

* Python 3.8+
* ffmpeg installed
* pip

---

# Installation

## 1. Clone the repository

```bash
git clone <your-github-repo-url>
cd <repo-folder>
```

## 2. Create a virtual environment

```bash
python3 -m venv .venv
```

## 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

## 4. Install dependencies

```bash
pip install yt-dlp
```

---

# Usage

Replace the example URL below with the video URL you want to download.

```bash
python3 uni_downloader.py "https://www.vecteezy.com/video/53974301-aerial-view-of-young-athletes-playing-streetball-on-an-open-summer-playground"
```

Downloaded videos are automatically saved inside a generated `videos/` directory.

---

# Using Cookies (Optional)

For platforms requiring authentication, export your browser cookies and use:

```bash
python3 uni_downloader.py "<VIDEO_URL>" --cookies cookies.txt
```

---

# Example Output Structure

```bash
videos/
└── extractor-name/
    └── video-title.mp4
```

---

# Disclaimer

This project is intended for educational and research purposes only.
Please respect platform terms of service, licensing agreements, and copyright laws when downloading content.

---

# Credits

Built with:

* Python
* yt-dlp
* ffmpeg
