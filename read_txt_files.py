"""
Python script to read and display all .txt files in a directory
Klasördeki tüm .txt dosyalarını okuyup ekrana yazan Python scripti
"""

import os
from pathlib import Path


def read_txt_files(directory_path=None):
    """
    Belirtilen klasördeki tüm .txt dosyalarını okuyup ekrana yazdırır.
    Eğer klasör yolu belirtilmezse, mevcut klasörü kullanır.
    """
    
    # Eğer klasör yolu belirtilmemişse, mevcut klasörü kullan
    if directory_path is None:
        directory_path = os.getcwd()
    
    # Path objesi oluştur
    folder_path = Path(directory_path)
    
    # Klasörün var olup olmadığını kontrol et
    if not folder_path.exists():
        print(f"Hata: '{directory_path}' klasörü bulunamadı!")
        return
    
    if not folder_path.is_dir():
        print(f"Hata: '{directory_path}' bir klasör değil!")
        return
    
    # Klasördeki tüm .txt dosyalarını bul
    txt_files = list(folder_path.glob("*.txt"))
    
    # Eğer dosya bulunamadıysa
    if not txt_files:
        print(f"'{directory_path}' klasöründe .txt dosyası bulunamadı.")
        return
    
    print(f"\n'{directory_path}' klasöründe {len(txt_files)} adet .txt dosyası bulundu.\n")
    print("=" * 80)
    
    # Her dosyayı oku ve ekrana yazdır
    for txt_file in txt_files:
        print(f"\n>> Dosya: {txt_file.name}")
        print(f">> Tam Yol: {txt_file}")
        print("-" * 80)
        
        try:
            # Dosyayı aç ve içeriğini oku
            with open(txt_file, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Eğer dosya boşsa
                if not content.strip():
                    print("(Dosya boş)")
                else:
                    print(content)
                    
        except UnicodeDecodeError:
            # UTF-8 ile okunamazsa, latin-1 kodlamasını dene
            try:
                with open(txt_file, 'r', encoding='latin-1') as file:
                    content = file.read()
                    print(content)
            except Exception as e:
                print(f"HATA: Dosya okunurken hata olustu - {e}")
                
        except Exception as e:
            print(f"HATA: Dosya okunurken hata olustu - {e}")
        
        print("=" * 80)
    
    print(f"\n>> Toplam {len(txt_files)} dosya islendi.")


# Ana fonksiyon
if __name__ == "__main__":
    import sys
    
    # Komut satırından klasör yolu verilmişse kullan, yoksa mevcut klasörü kullan
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
        print(f"Verilen klasör: {folder_path}")
    else:
        folder_path = None
        print("Klasör belirtilmedi. Mevcut klasörde aranacak...")
    
    read_txt_files(folder_path)

