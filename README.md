# Subdomain Finder Tool

## HaOMing_X12 Team: Clan_X12

### Deskripsi

Subdomain Finder Tool ini adalah alat sederhana untuk menemukan subdomain dari domain yang diberikan. Skrip ini mendukung input baik dari file yang berisi daftar subdomain atau input single hostname/domain. 

### Fitur

- **Header Animasi**: Skrip ini menampilkan header yang disesuaikan dengan warna menarik.
- **Input Massal**: Dapat membaca daftar subdomain dari file.
- **Input Single Domain**: Memeriksa satu domain yang diberikan untuk subdomain.

### Cara Penggunaan

#### Input Massal dari File

Untuk menggunakan fitur input massal, siapkan file teks (`wordlist.txt`) yang berisi daftar subdomain (satu per baris). Kemudian jalankan skrip dengan opsi `-f` diikuti dengan nama file dan `-d` untuk domain yang ingin diperiksa.

Contoh:
```bash
python subdomain_finder.py -f wordlist.txt -d example.com
