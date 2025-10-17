import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "IPK": 2,
    "Jumlah_Absensi": 3,
    "Waktu_Belajar_Jam": 20,
    "IPK_x_Study": 2 * 20,       # fitur turunan
    "Rasio_Absensi": 3 / 14       # fitur turunan
}

response = requests.post(url, json=data)
print(response.json())
