import os

os.makedirs('PoryRoku/wiosna/marzec', exist_ok=True)
os.makedirs('PoryRoku/wiosna/kwiecień', exist_ok=True)
os.makedirs('PoryRoku/wiosna/maj', exist_ok=True)

os.makedirs('PoryRoku/lato/czerwiec', exist_ok=True)
os.makedirs('PoryRoku/lato/lipiec', exist_ok=True)
os.makedirs('PoryRoku/lato/sierpień', exist_ok=True)

os.makedirs('PoryRoku/jesien/wrzesień', exist_ok=True)
os.makedirs('PoryRoku/jesien/październik', exist_ok=True)
os.makedirs('PoryRoku/jesien/listopad', exist_ok=True)

os.makedirs('PoryRoku/zima/grudzień', exist_ok=True)
os.makedirs('PoryRoku/zima/styczeń', exist_ok=True)
os.makedirs('PoryRoku/zima/luty', exist_ok=True)

os.chmod('PoryRoku', 0o700)
