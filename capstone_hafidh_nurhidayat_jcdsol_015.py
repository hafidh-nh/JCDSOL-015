from tabulate import tabulate
from datetime import datetime

# Dummy data
data = [
    {'NIK': 202201001, 'Nama': 'Fahmi Hasan', 'Usia': 25, 'Kota': 'Jakarta', 'Departemen': 'HR'},
    {'NIK': 202201002, 'Nama': 'Dimas Susanto', 'Usia': 30, 'Kota': 'Bandung', 'Departemen': 'IT'},
    {'NIK': 202201003, 'Nama': 'Joko Susanto', 'Usia': 22, 'Kota': 'Surabaya', 'Departemen': 'Finance'},
    {'NIK': 202201004, 'Nama': 'Sherly Sherla', 'Usia': 28, 'Kota': 'Medan', 'Departemen': 'Marketing'}
]

def read_data():
    """Fungsi untuk memunculkan data dalam format tabel"""
    print(tabulate(data, headers="keys", tablefmt="grid"))

def create_data():
    """Fungsi untuk menambahkan data baru dengan NIK yang di-generate otomatis"""
    try:
        # Generate NIK with current year and month
        current_year_month = datetime.now().strftime('%Y%m')
        max_nik = max((int(str(item['NIK'])[6:]) for item in data if str(item['NIK']).startswith(current_year_month)), default=0)
        new_nik = int(current_year_month) * 1000 + max_nik + 1

        new_data = {
            'NIK': new_nik,
            'Nama': input("Masukkan Nama: "),
            'Usia': int(input("Masukkan Usia: ")),
            'Kota': input("Masukkan Kota: "),
            'Departemen': input("Masukkan Departemen: ")
        }
        data.append(new_data)
        print("Data baru berhasil ditambahkan.")
    except ValueError:
        print("Input tidak valid. Pastikan Usia adalah integer.")

def update_data():
    """Fungsi untuk mengupdate data berdasarkan NIK"""
    try:
        nik = int(input("Masukkan NIK yang akan diupdate: ").strip())
        item = next((item for item in data if item['NIK'] == nik), None)
        if not item:
            print("NIK tidak ditemukan.")
            return

        update_fields = {
            'Nama': lambda x: x,
            'Usia': lambda x: int(x) if x else None,
            'Kota': lambda x: x,
            'Departemen': lambda x: x
        }

        for field, transform in update_fields.items():
            new_value = input(f"Masukkan {field} baru (kosongkan jika tidak ingin mengubah): ").strip()
            if new_value:
                item[field] = transform(new_value)

        print("Data berhasil diperbarui.")
    except ValueError:
        print("Input tidak valid. Pastikan NIK dan Usia adalah integer.")

def delete_data():
    """Fungsi untuk menghapus data berdasarkan NIK"""
    try:
        nik = int(input("Masukkan NIK yang akan dihapus: ").strip())
        global data
        data = [item for item in data if item['NIK'] != nik]
        print("Data berhasil dihapus.")
    except ValueError:
        print("Input tidak valid. NIK harus berupa integer.")

def filter_kota():
    """Fungsi untuk memfilter data berdasarkan nama kota"""
    nama_kota = input("Masukkan Nama Kota yang ingin difilter: ").strip().lower()
    filtered_data = [item for item in data if item['Kota'].lower() == nama_kota]
    print(tabulate(filtered_data, headers="keys", tablefmt="grid") if filtered_data else "Tidak ada data yang sesuai dengan nama kota tersebut.")

def sort_data():
    """Fungsi untuk mengurutkan data berdasarkan kolom yang dipilih"""
    columns = ['NIK', 'Nama', 'Usia', 'Kota', 'Departemen']
    print("\n".join(f"{i+1}. {col}" for i, col in enumerate(columns)))

    try:
        key = columns[int(input("Masukkan pilihan kolom: ").strip()) - 1]
        data.sort(key=lambda x: x[key])
        print(f"Data diurutkan berdasarkan {key}.")
        read_data()
    except (IndexError, ValueError):
        print("Pilihan tidak valid.")

# Menu
menu_functions = {
    '1': read_data,
    '2': create_data,
    '3': update_data,
    '4': delete_data,
    '5': filter_kota,
    '6': sort_data
}

while True:
    print("\nMenu:\n1. Lihat Data\n2. Tambah Data\n3. Update Data\n4. Hapus Data\n5. Filter Data Berdasarkan Kota\n6. Urutkan Data\n7. Keluar")
    pilihan = input("Pilih menu: ").strip()
    if pilihan == '7':
        print("Keluar dari program.")
        break
    menu_functions.get(pilihan, lambda: print("Pilihan tidak valid. Silakan coba lagi."))()

