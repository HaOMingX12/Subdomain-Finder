████╗  ████╗██████╗  █████╗  ██████╗ ███╗   ██╗██╗███╗   ███╗██╗███╗   ██╗
████╗ ████║██╔══██╗██╔══██╗██╔══██╗████╗  ██║██║████╗ ████║██║████╗  ██║
██╔████╔██║███████║██████╔╝███████║██╔██╗ ██║██║██╔████╔██║██║██╔██╗ ██║
██║╚██╔╝██║██╔══██║██╔══██╗██╔══██╗██║╚██╗██║██║██║╚██╔╝██║██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██║██║ ╚████║██║██║ ╚═╝ ██║██║██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝╚═╝   ╚═══╝

HaOMing_X12 Team: Clan_X12



# Subdomain Finder Tool

## HaOMing_X12 Team: Clan_X12

### Deskripsi

Subdomain Finder Tool ini adalah alat sederhana yang dirancang untuk membantu Anda menemukan subdomain dari domain yang ditentukan. Skrip ini mendukung dua metode input: dari file yang berisi daftar subdomain atau input satu hostname/domain. Dengan tampilan header yang menarik dan warna yang mencolok, alat ini memudahkan Anda dalam menemukan subdomain dengan efisien.

### Fitur

- **Header Animasi**: Header dengan styling khusus untuk tampilan yang menarik.
- **Input Massal**: Kemampuan untuk membaca daftar subdomain dari file teks.
- **Input Single Domain**: Memeriksa subdomain dari satu domain yang diberikan.
- **Penggunaan Mudah**: Cukup dengan beberapa perintah di terminal untuk menjalankan alat ini.

### Instalasi

Untuk menggunakan alat ini, pastikan Anda telah memenuhi persyaratan berikut:

1. **Clone repositori**: 
    ```bash
    git clone https://github.com/HaOMingX12/Subdomain-Finder
    ```
2. **Masuk ke direktori skrip**:
    ```bash
    cd Subdomain-Finder
    ```
3. **Instal dependensi**:
    Pastikan Anda memiliki Python 3.x terinstal. Instal modul yang diperlukan menggunakan `pip`:
    ```bash
    pip install requests termcolor
    ```

### Penggunaan

#### Input Massal dari File

Untuk memeriksa subdomain dari daftar yang disimpan dalam file, siapkan file teks (`wordlist.txt`) yang berisi daftar subdomain (satu subdomain per baris). Jalankan skrip dengan opsi `-f` diikuti dengan nama file dan opsi `-d` untuk domain yang ingin Anda periksa.

Contoh perintah:
```bash
python subdomain_finder.py -f wordlist.txt -d example.com
