class metode:
    #init method
    def __init__(self, harga):
        self.harga = harga

    #self parameter
    def thx(self):
        print(f"Terimakasih sudah mencoba program dari Kelompok 28")

    #method dengan parameter
    def selesai(self, waktu):
        print("Percobaan akan selesai dalam :")
        while waktu > 0:
            print(waktu)
            waktu -= 1
