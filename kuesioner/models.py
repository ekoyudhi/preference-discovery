from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


doc = """
After Survey
"""


class Constants(BaseConstants):
    name_in_url = 'AfterSurvey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    s1 = models.IntegerField(choices=[[1,"Ya, bekerja sebagai Wirausahawan"],[2,"Ya, bekerja sebagai Pekerja Paruh Waktu"],[3,"Ya, bekerja sebagai Pegawai Tetap"],[4,"Belum pernah bekerja"]], label="1) Apakah Anda pernah/sedang bekerja ?")
    s2 = models.IntegerField(choices=[[1,"0 – 3 tahun"],[2,"3 – 6 tahun"],[3,"Lebih dari 6 tahun"]], label="2) Berapa lama masa pengalaman kerja Anda?")
    s3 = models.IntegerField(choices=[[1,"Sudah punya"],[2,"Belum punya"]], label="3) Apakah Sudah memiliki NPWP?")
    s4 = models.IntegerField(choices=[[1,"Tidak Berminat"],[2,"Cukup Berminat"],[3,"Berminat"],[4,"Sangat Berminat"]], label="4) Jika belum, seberapa ingin Anda memiliki NPWP", blank=True)
    s5 = models.IntegerField(choices=[[1,"Belum pernah"],[2,"Sudah pernah"]], label="5) Jika sudah punya, apakah pernah Lapor SPT?", blank=True)
    s6 = models.IntegerField(choices=[[1,"Kurang dari 10%"],[2,"20%"],[3,"30%"],[4,"40%"],[5,"50%"],[6,"Lebih dari 50%"]], label="6) Menurut Anda, berapa besar probabilitas dari kemungkinan diperiksa yang Anda rasakan dalam game ini?")
    s7 = models.IntegerField(choices=[[1,"Tidak Adil"],[2,"Cukup Adil"],[3,"Adil"],[4,"Sangat Adil"]], label="7) Seberapa adilkah penghitungan pajak dalam penelitian ini? (tarif pajak dikali dengan omset, bukan dikali laba)")
    s8 = models.IntegerField(choices=[[1,"Tidak Mudah"],[2,"Cukup Mudah"],[3,"Mudah"],[4,"Sangat Mudah"]], label="8) Seberapa mudahkah penghitungan pajak dalam penelitian ini?")
    s9 = models.IntegerField(choices=[[1,"Tidak Setuju"],[2,"Cukup Setuju"],[3,"Setuju"],[4,"Sangat Setuju"]], label="9) Seberapa setuju Anda dengan penurunan tarif dari 20% ke 10% di negara Nusa Makmur?")
    s10 = models.IntegerField(choices=[[1,"Tidak Percaya"],[2,"Cukup Percaya"],[3,"Percaya"],[4,"Sangat Percaya"]], label="10) Seberapa besar kepercayaan Anda terhadap otoritas pajak Nusa Makmur terkait dengan perhitungan estimasi prefilled omset yang diterapkan dalam form pelaporan pajak?", blank=True)

    s11 = models.IntegerField(label="1) Usia Anda")
    s12 = models.IntegerField(choices=[[1, 'Laki-laki'], [2, 'Perempuan']], label='2) Jenis kelamin Anda')
    s13 = models.IntegerField(choices=[[1, 'Diploma 3 (D3)'], [2, 'Sarjana (S1/D4)'], [3, 'Magister (S2)'], [4, 'Doktoral (S3)']],label='3) Tingkat pendidikan yang sedang atau telah Anda ditempuh')
    s14 = models.IntegerField(choices=[[1, 'Sekolah/Kuliah'], [2, 'Lulus belum bekerja'], [3, 'Bekerja']], label='4) Aktivitas utama Anda saat ini')
    s15 = models.IntegerField(choices=[[1, 'Biologi'], [2, 'Farmasi'], [3, 'Geografi'], [4, 'Kedokteran Gigi'], [5, 'Kedokteran Gigi'],[6, 'Kedokteran, Kesehatan Masayarakat dan Keperawatan'], [7, 'Kehutanan'], [8, 'MIPA'],[9, 'Pertanian'], [10, 'Peternakan'], [11, 'Teknik'], [12, 'Teknologi Pertanian'],[13, 'Ekonomika dan Bisnis'], [14, 'Filsafat'], [15, 'Hukum'], [16, 'Ilmu Budaya'], [17, 'Isipol'],[18, 'Psikologi'], [19, 'Sekolah Vokasi']], label='5) Bidang studi')
    s16 = models.IntegerField(choices=[[1, 'Di bawah 500.000'], [2, '500.001 s.d 1.000.000'], [3, '1.000.001 s.d 1.500.000'],[4, '1.500.001 s.d 2.000.000'], [5, '2.000.0001 s.d 2.500.000'], [6, 'Di atas 2.500.0001']], label='6) Rata-rata pengeluaran setiap bulan')
    s17 = models.IntegerField(choices=[[1, 'OVO'], [2, 'GoPay'], [3, 'ShopeePay'], [4, 'Bank Mandiri'], [5, 'Bank BNI']], label='7) Metode pembayaran yang Anda inginkan')
    s18 = models.StringField(label="8) Nomor HP e-money/No Rekening")
    s19 = models.IntegerField(choices=[[1, "Tidak Menarik"], [2, "Cukup Menarik"], [3, "Menarik"], [4, "Sangat Menarik"]], label='9) Seberapa menariknya eksperimen ini bagi Anda:')

    p1 = models.IntegerField(label="1) Usia Anda")
    p2 = models.IntegerField(choices=[[1,'Laki-laki'],[2,'Perempuan']], label='2) Jenis kelamin Anda')
    p3 = models.IntegerField(choices=[[1,'Diploma 3 (D3)'],[2,'Sarjana (S1/D4)'],[3,'Magister (S2)'],[4,'Doktoral (S3)']], label='3) Tingkat pendidikan yang sedang atau telah Anda ditempuh')
    p4 = models.IntegerField(choices=[[1,'Sekolah/Kuliah'],[2,'Lulus belum bekerja'],[3,'Bekerja']], label='4) Aktivitas utama Anda saat ini')
    p5 = models.IntegerField(choices=[[1,'Biologi'],[2,'Farmasi'],[3,'Geografi'],[4,'Kedokteran Gigi'],[5,'Kedokteran Gigi'],[6,'Kedokteran, Kesehatan Masayarakat dan Keperawatan'],[7,'Kehutanan'],[8,'MIPA'],[9,'Pertanian'],[10,'Peternakan'],[11,'Teknik'],[12,'Teknologi Pertanian'],[13,'Ekonomika dan Bisnis'],[14,'Filsafat'],[15,'Hukum'],[16,'Ilmu Budaya'],[17,'Isipol'],[18,'Psikologi'],[19,'Sekolah Vokasi']], label='5) Bidang studi')
    p6 = models.IntegerField(choices=[[1,'Di bawah 500.000'],[2,'500.001 s.d 1.000.000'],[3,'1.000.001 s.d 1.500.000'],[4,'1.500.001 s.d 2.000.000'],[5,'2.000.0001 s.d 2.500.000'],[6,'Di atas 2.500.0001']], label='6) Rata-rata pengeluaran setiap bulan')
    p7 = models.IntegerField(choices=[[1,'OVO'],[2,'GoPay'],[3,'ShopeePay'],[4,'Bank Mandiri'],[5,'Bank BNI']], label='7) Metode pembayaran yang Anda inginkan')
    p8 = models.StringField(label="8) Nomor HP e-money/No Rekening")
    p9 = models.IntegerField(choices=[[1,"Tidak Menarik"],[2,"Cukup Menarik"],[3,"Menarik"],[4,"Sangat Menarik"]], label='9) Seberapa menariknya eksperimen ini bagi Anda:')

    angka_random = models.IntegerField(min=11, max=99, label="2 digit angka")
    periode_terpilih = models.IntegerField(initial=0, blank=False)
    payoff_real = models.FloatField(initial=0, blank=False)

