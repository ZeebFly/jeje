
ANAK USERBOT KONTOL, BISA NYA NYOLONG KONTOL, KAGA PUNYA OTAK KONTOL, LU MAKAN KONTOL, MIKIR DONG KONTOL, MAKANYA JANGAN SERING MAKAN KONTOL KONTOL


YANG NYOLONG KONTOL || SEMUA PANDUAN ADA DISINI KALO ADA APA APA TANYA KE GW @KENAPANAN JANGAN KE ORANG LAEN


## 🖇 VPS Deployment
- ganti semua isi config.py sama punya lu kalo udah lanjut dibawah
- clone repo : `git clone https://git_token@github.com/username/nama_repo && cd nama_repo`
- Setup Vps (Jalankan hanya sekali) : `bash setup.sh`
- `tmux new-session -s ubot`
- `python3 -m venv venv && source venv/bin/activate`
- `pip3 install -U pip`
- `pip3 install --no-cache-dir -r req.txt`
- `bash start`
- Klik CTRL B + D di keyboard Vps
- 

# Cara buka cek log userbot di vps
Ketik 
- `tmux a -t ubot`

# Note:
  Kalo ada eror "sqlite3.OperationalError: unable to open database file" buka vps terus ketik
- `tmux a -t ubot`
- Klik CTRL + C
- Lanjut `bash start.sh`
- close vps


# Cara ambil cookies disini https://t.me/kynansupport/872 . kalo udah dapet tinggal tempel di ireng.txt terus save


# Fitur asupan, porn, bing-img, gemini memakai api. Silahkan buat sendiri jika api mati

# Kalo divps gunicorn nya belom connect atau log divps kaya gini "Retrying in 1 seconds" ketik `pkill -f gunicorn` baru `bash start.sh`