class pelabuhanmerak():
    def lokasi(self):
        print("Pelabuhan Merak berlokasi di Pulo Merak, Kota Cilegon, Banten.")
    def sejarah(self):
        print("Pelabuhan ini dibangun pada 1970 oleh Dinas Perhubungan.")
    def jenis(self):
        print("Jenis Pelabuhan Merak adalah pelabuhan penyebrangan.")

class pelabuhanTE():
    def lokasi(self):
        print("Pelabuhan Tanjung Mas Semarang berlokasi di Semarang, Jawa Tengah. ")
    def sejarah(self):
        print("Pelabuhan ini berdiri sejak tahun 1985.")
    def jenis(self):
        print("Jenis Pelabuhan Tanjung Mas Semarang adalah pelabuhan laut.")

obj_pelabuhanmerak = pelabuhanmerak()
obj_pelabuhanTE = pelabuhanTE()
for pelabuhan in (obj_pelabuhanmerak, obj_pelabuhanTE):
    pelabuhan.lokasi()
    pelabuhan.sejarah()
    pelabuhan.jenis()
    print("---------------------------------------------")