# Lazy SAK

Aplikasi Self Assessment Untuk Yang Malas

## Instalasi

1. Instal Python3: 
   - Windows [32 bit](https://www.python.org/ftp/python/3.7.7/python-3.7.7.exe), [64 bit](https://www.python.org/ftp/python/3.7.7/python-3.7.7-amd64.exe)
   - Mac OS X [64 bit](https://www.python.org/ftp/python/3.7.7/python-3.7.7-macosx10.9.pkg)
   - Linux
     ```bash
     # Debian-Based
     sudo apt update
     sudo apt install python3

     # Red Hat
     sudo yum install python3

     # Fedora
     sudo dnf install python3
     ```

2. Unduh File Berikut: [LazySAK](https://github.com/Ikhsan6012/LazySAK/archive/master.zip) atau Clone melalui [Git](https://git-scm.com/downloads)
    ```bash
    git clone https://github.com/Ikhsan6012/LazySAK.git
    ```

## Cara Penggunaan
1. Buka CMD / Terminal
2. Pastikan Python3 telah terinstal
    ```bash
    python --version
    # Python 3.7.7
    ```
3. Masuk ke folder LazySAK
    ```bash
    # Windows
    cd "PATH\TO\FOLDER"

    # Mac OS X / Linux
    cd "PATH/TO/FOLDER"
    ```
4. Jalankan Perintah Berikut:
    ```bash
    # Hanya dilakukan sekali saat instalasi
    pip install -r requirements.txt
    ```
5. Untuk Penggunaan Pertama, buka File "config.json". Isi semua "value" yang kosong (kecuali "required": false).
   - Untuk type "text". Contoh:
      ```bash
      "alamat": {
        "label": "Alamat Saat ini",
        "type": "text",
        "required": true,
        "value": "", # Sebelum Diisi
        "value": "Jl. Mandala Utara III, Tomang, Grogol Petamburan", # Setelah Diisi
      },
      ```
    - Untuk type "radio". Contoh:
      ```bash
      "jenis_alamat": {
        "label": "Jenis Tempat Tinggal Saat ini",
        "type": "radio",
        "required": true,
        "options": [
          { "label": "Rumah Pribadi", "value": 1 },
          { "label": "Rumah Dinas", "value": 2 },
          { "label": "Indekos", "value": 3 }
        ],
        "value": "", # Sebelum Diisi
        "value": 3, # Setelah Diisi. Pilihan Terdapat pada 'value' di dalam 'options'
      },
      ```
      Catatan:
      - Untuk "kd_kota" harus sesuai referensi pada file "kota.json"
      - Untuk "latitude" dan "longitude" bisa dicek pada aplikasi logbook. Apabila ingin otomatis bisa diisi dengan "default"
      
    - Untuk type "checkbox" sama dengan "radio",  tetapi 'options' nya hanya 2 yaitu:
      ```bash
      "options": [
        { "label": "Ya", "value": 1 },
        { "label": "Tidak", "value": 2 },
      ],
      ```
6. Jalankan Perintah Berikut:
    ```bash
    python self_assessment.py <NIP> <PASSWORD>
    ```
    atau
    ```bash
    python self_assessment.py
    # Masukkan NIP: 
    # Masukkan Password: 
    ```

## Penutup
<b><h2><center>:sleeping::sleeping: SELAMAT TIDUR :sleeping::sleeping:</center></h2></b>

## Lisensi
[MIT](https://choosealicense.com/licenses/mit/)
