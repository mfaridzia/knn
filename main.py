import csv 

# Menghitung jarak perkiraan dari dua buah titik
def hitung_perkiraan(x, y):
	return abs(x['x1'] - y['x1']) + abs(x['x2'] - y['x2']) + abs(x['x3'] - y['x3']) + abs(x['x4'] - y['x4']) + abs(x['x5'] - y['x5'])

# Memprediksi data dari datasets
def prediksi_data(nilai, data, x):
	daftar_perkiraan = [{'hitung_perkiraan': float('inf')}]
	for dataset in data:
		hasil = hitung_perkiraan(nilai, dataset)
		if hasil < daftar_perkiraan[-1]['hitung_perkiraan']:
			if len(daftar_perkiraan) >= x:
				daftar_perkiraan.pop()
			i = 0
			while i < len(daftar_perkiraan)-1 and hasil >= daftar_perkiraan[i]['hitung_perkiraan']:
				i += 1
			daftar_perkiraan.insert(i, {'hitung_perkiraan': hasil, 'Y': dataset['Y']})
	daftar_nilai = list(map(lambda x: x['Y'], daftar_perkiraan))
	return max(daftar_nilai, key=daftar_nilai.count)

# Menulis hasil keluaran data ke file berformat csv
def hasil_file_csv(file_data, datacsv):
	with open(file_data, mode='w', newline='') as csv_ouput:
		csv_file = csv.writer(csv_ouput)
		csv_file.writerows(datacsv)

# Klasifikasi datatest berdasarkan data pada file DataTrain
def hasil_klasifikasi(data_test, data_train, k):
	for d_test in data_test:
		d_test['Y'] = prediksi_data(d_test, data_train, k)
	hasil_file_csv('TebakanTugas3.csv', map(lambda x: [x['Y']], data_test)) # Generate file csv

# Fungsi untuk membaca data dari file csv 
def baca_input_csv(f, kondisi=False):
	dataset = [] # buat array kosong untuk menampung nilai dari file csv yang dibaca
	with open(f) as csv_input:
		baca_csv = csv.DictReader(csv_input, skipinitialspace=True)
		for baris in baca_csv:
			dataset.append({'i': int(baris['Index']), 'x1': float(baris['X1']), 'x2': float(baris		['X2']), 'x3': float(baris['X3']), 'x4': float(baris['X4']), 'x5': float(baris['X5']), 'Y': int(baris['Y']) if kondisi else baris['Y']}) 
	return dataset

# Main program untuk menjalankan fungsi yang sudah dibuat sebelumnya
if __name__ == '__main__':
	hasil_klasifikasi(baca_input_csv('DataTest_Tugas3_AI.csv'), baca_input_csv('DataTrain_Tugas3_AI.csv', kondisi=True), 15) # Nilai parameter k = 15
