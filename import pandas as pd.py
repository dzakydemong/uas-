import pandas as pd

# Membaca dataset dari file CSV
dataset = pd.read_csv('dataset_karyawan.csv')

# Menampilkan dataset
print(dataset)

# Menghitung rata-rata kinerja karyawan
rata_rata_kinerja = dataset['Kinerja'].mean()
print("Rata-rata Kinerja: ", rata_rata_kinerja)

# Mengelompokkan karyawan berdasarkan departemen
kelompok_departemen = dataset.groupby('Departemen')

# Menghitung rata-rata kinerja per departemen
rata_rata_per_departemen = kelompok_departemen['Kinerja'].mean()
print("\nRata-rata Kinerja per Departemen:\n", rata_rata_per_departemen)
