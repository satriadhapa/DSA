import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep

# Inisialisasi geolocator Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

# Fungsi untuk mendapatkan koordinat dari alamat
def get_coordinates(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return f"{location.latitude}, {location.longitude}"
        else:
            return None
    except Exception as e:
        print(f"Error getting coordinates for {address}: {e}")
        return None

# Load file Excel
file_path = 'data.xlsx'  # Ganti dengan path file Anda
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Pastikan kolom "Address Line 1" ada
data['Generated LongLat'] = data['Address Line 1'].apply(lambda x: get_coordinates(x) if pd.notnull(x) else None)

# Tunggu sejenak untuk menghindari rate limit
sleep(1)

# Simpan kembali hasilnya ke file Excel baru
output_path = 'data_with_coordinates.xlsx'
data.to_excel(output_path, index=False)
print(f"File dengan koordinat disimpan di: {output_path}")
