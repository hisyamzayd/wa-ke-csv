# panduan penggunaan 'wa ke csv'
untuk whatsapp ios dan android
author: hisyam zayd

## langkah run program
1. pastikan sudah terinstall pandas pada python
2. pastikan sebelum export nomor lawan bicara chat sudah disimpan dalam kontak
3. letakkan hasil export pada folder dengan nama yang sesuai dengan os hp saat dilakukan export
4. masuk ke cmd, jalankan command 
```python
python wa_ke_csv_android.py
```
atau 
```python 
python wa_ke_csv_ios.py
```
5. hasil file csv ada pada folder "hasil csv"

## kekurangan
* regex belum berfungsi pada hasil export chat dengan nomor kontak lawan bicara yang belum disimpan.

## license :
* tidak ada. mau langsung pakai silahkan, kalau mau diperbaiki saya sangat berterima kasih 🙏.

## keterangan lain :
* format regex pada masing-masing os tersedia dalam file [format_pesan_export.txt](format_pesan_export.txt)
* file format ipynb sama dengan format py. dibuat untuk memudahkan debugging.