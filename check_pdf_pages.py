import PyPDF2
import os

pdf_file = r"c:\Dev\Learning\rifki\rifki_skor_karti.pdf"

try:
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        
        print(f"📄 PDF Dosyası: {pdf_file}")
        print(f"📊 Toplam Sayfa Sayısı: {num_pages}")
        
        if num_pages == 1:
            print("✅ BAŞARILI! Tüm içerik tek sayfaya sığıyor!")
        else:
            print(f"❌ HATA! PDF {num_pages} sayfaya yayılıyor. Daha fazla küçültme gerekli.")
            
except FileNotFoundError:
    print(f"❌ PDF dosyası bulunamadı: {pdf_file}")
except ImportError:
    print("❌ PyPDF2 kütüphanesi yüklü değil. Yüklemek için çalıştırın:")
    print("   pip install PyPDF2")
except Exception as e:
    print(f"❌ Hata: {e}")

