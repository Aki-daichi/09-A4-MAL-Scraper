@echo off
cd /d "%~dp0"

python clear.py

cd manga
scrapy crawl manga-spider -o hasil.json

cd ..
python main.py

cd C:\Users\Asus\Documents\GitHub\zakiabdil.github.io
del hasil.json
copy "C:\Users\Asus\Documents\Tugas Python\Proyek 1\Week 9\manga\hasil.json" "C:\Users\Asus\Documents\GitHub\zakiabdil.github.io"


git add data.json
git add hasil.json
git commit -m "Updated data.json"
git push origin main
