import subprocess
import os

html_file = r"c:\Dev\Learning\rifki\rifki_skor_karti.html"
pdf_file = r"c:\Dev\Learning\rifki\rifki_skor_karti.pdf"

# Chrome ile PDF oluştur
chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

for chrome_path in chrome_paths:
    if os.path.exists(chrome_path):
        cmd = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            "--run-all-compositor-stages-before-draw",
            "--print-to-pdf=" + pdf_file,
            "file:///" + html_file.replace("\\", "/")
        ]
        print(f"Chrome bulundu: {chrome_path}")
        print(f"PDF oluşturuluyor...")
        subprocess.run(cmd)
        
        if os.path.exists(pdf_file):
            print(f"✓ PDF başarıyla oluşturuldu: {pdf_file}")
        else:
            print("✗ PDF oluşturulamadı")
        break
else:
    print("Chrome bulunamadı. Lütfen tarayıcıdan manuel olarak PDF'e yazdırın.")

