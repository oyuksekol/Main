"""
Test Script: Klasördeki tüm .txt dosyalarının satır sayısını raporlar
Test Script: Reports line count for all .txt files in a directory
"""

import os
from pathlib import Path


def count_lines_in_txt_files(directory_path=None):
    """
    Belirtilen klasördeki tüm .txt dosyalarını bulur ve her dosya için satır sayısını raporlar.
    Eğer klasör yolu belirtilmezse, mevcut klasörü kullanır.
    """
    
    # Eğer klasör yolu belirtilmemişse, mevcut klasörü kullan
    if directory_path is None:
        directory_path = os.getcwd()
    
    # Path objesi oluştur
    folder_path = Path(directory_path)
    
    # Klasörün var olup olmadığını kontrol et
    if not folder_path.exists():
        print(f"Hata: '{directory_path}' klasoru bulunamadi!")
        return
    
    if not folder_path.is_dir():
        print(f"Hata: '{directory_path}' bir klasor degil!")
        return
    
    # Klasördeki tüm .txt dosyalarını bul
    txt_files = list(folder_path.glob("*.txt"))
    
    # Eğer dosya bulunamadıysa
    if not txt_files:
        print(f"'{directory_path}' klasorunde .txt dosyasi bulunamadi.")
        return
    
    # Dosyaları isme göre sırala
    txt_files.sort(key=lambda x: x.name)
    
    print("=" * 70)
    print(f"RAPOR: '{directory_path}' klasorundeki .txt dosyalarinin satir sayilari")
    print("=" * 70)
    
    total_lines = 0
    total_files = len(txt_files)
    
    # Her dosya için satır sayısını hesapla
    for txt_file in txt_files:
        try:
            # Dosyayı aç ve satır sayısını hesapla
            with open(txt_file, 'r', encoding='utf-8') as file:
                line_count = sum(1 for line in file)
            
            total_lines += line_count
            
            # Dosya adı ve satır sayısını göster
            file_size = txt_file.stat().st_size
            print(f"  {txt_file.name:40} | {line_count:5} satir | {file_size:8} byte")
            
        except UnicodeDecodeError:
            # UTF-8 ile okunamazsa, latin-1 kodlamasını dene
            try:
                with open(txt_file, 'r', encoding='latin-1') as file:
                    line_count = sum(1 for line in file)
                total_lines += line_count
                file_size = txt_file.stat().st_size
                print(f"  {txt_file.name:40} | {line_count:5} satir | {file_size:8} byte")
            except Exception as e:
                print(f"  {txt_file.name:40} | HATA: {e}")
        
        except Exception as e:
            print(f"  {txt_file.name:40} | HATA: {e}")
    
    print("=" * 70)
    print(f"TOPLAM: {total_files} dosya, {total_lines} satir")
    print("=" * 70)


# Ana fonksiyon
if __name__ == "__main__":
    import sys
    
    # Komut satırından klasör yolu verilmişse kullan, yoksa mevcut klasörü kullan
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
        print(f"Verilen klasor: {folder_path}")
    else:
        folder_path = None
        print("Klasor belirtilmedi. Mevcut klasorde aranacak...")
    
    count_lines_in_txt_files(folder_path)
