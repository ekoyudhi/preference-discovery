from random import sample
import random

import numpy as np
import pandas as pd
from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Putu Sanjiwacika Wibisana'

doc = """
Adaptation of Preference Discovery by Delaney, Jacobson and Moenig (2018) for risk preference discovery.
"""

class Constants(BaseConstants):
    name_in_url = 'preference_discovery_v2'
    players_per_group = None
    num_rounds = 33
    num_training_rounds = 3
    num_real_rounds_per_session = 10
    endowment = c(1000)
    multiplier = 2
    with open('preference_discovery/Lottery.csv', encoding="utf-8") as file:
        prospects = pd.read_csv(file)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    payoff_thisround = models.CurrencyField()
    player_payoff = models.CurrencyField()

    def set_payoff(self):
        players = self.get_players()
        payoff_thisround = [p.payoff_thisround for p in players]
        self.player_payoff = sum(payoff_thisround)

    def set_tot_payoffs(self):
        player_payoff = sum([p.payoff for p in self.player.in_previous_rounds()])
        return player_payoff


class Player(BasePlayer):

    def sequence_setup(self):
        set1 = Constants.prospects[Constants.prospects['Game_Type'] == "Block_1"]
        set2 = Constants.prospects[Constants.prospects['Game_Type'] == "Block_2"]
        set3 = Constants.prospects[Constants.prospects['Game_Type'] == "Block_3"]
        orgnl_sequence = [set1, set2, set3]
        player_sequence = random.sample(orgnl_sequence, len(orgnl_sequence))
        player_prospects = player_sequence[0].append(player_sequence[1], ignore_index=True).append(player_sequence[2],ignore_index=True)
        player_prospects['rounds'] = [self.session.config["rounds"]] * 63
        self.participant.vars["p_app_sequence"] = player_prospects  # Contains the dataframe for all parameters for all players
    
    def set_player_param(self):
        # round settings
        self.training_round = 1 if self.round_number <= self.session.config["training_rounds"] else 0
        if self.round_number == 1:
            self.participant.vars["prospect_table"] = Constants.prospects
            self.endowment = self.session.config["endowment"]
            self.participant.vars["payoff_vector"] = list()
        elif self.round_number == self.session.config["training_rounds"] + 1:
            self.participant.vars["prospect_table"] = Constants.prospects
                

        #inisiasi untuk tiap blok
        if self.round_number >= 1 and self.round_number <= self.session.config["training_rounds"]:
            # randomizer untuk Block Latihan
            rand = sample(list(range(0, 20)), 4)
            rand.append(20)
        if self.round_number >= self.session.config["training_rounds"] + 1 and self.round_number <= self.session.config["training_rounds"] + 10:
            # randomizer untuk Block 1 dari index 0 s.d index 20 sesuai csv lotere yang di load
            rand = sample(list(range(0, 20)), 4)
            rand.append(20)
        elif self.round_number >= self.session.config["training_rounds"] + 1 + 10 and self.round_number <= self.session.config["training_rounds"] + 10 + 10:
            # randomizer untuk Block 1 dari index 21 s.d index 41 sesuai csv lotere yang di load
            rand = sample(list(range(0+21, 20+21)), 4)
            rand.append(20+21)
        elif self.round_number >= self.session.config["training_rounds"] + 1 + 10 + 10 and self.round_number <= self.session.config["training_rounds"] + 10 + 10 + 10:
            # randomizer untuk Block 1 dari index 42 s.d index 62 sesuai csv lotere yang di load
            rand = sample(list(range(0+21+21, 20+21+21)), 4)
            rand.append(20+21+21)

        self.participant.vars["random_indexes"] = rand
        
        self.participant.vars["displayed_lotteries"] = list(
            self.participant.vars["prospect_table"].loc[self.participant.vars["random_indexes"], "Index"])
        self.participant.vars["displayed_prospects"] = self.participant.vars["prospect_table"].loc[
                                                       self.participant.vars["random_indexes"], :]
        self.displayed_lotteries = str(list(self.participant.vars["displayed_lotteries"]))

    def payoff_realizer(self):
        df = self.participant.vars["displayed_prospects"]
        print(self.round_number)
        print("new")
        print(df)
        print("ori")
        print(self.participant.vars["displayed_prospects"])
        df["Allocation"] = [self.Lotere_A, self.Lotere_B, self.Lotere_C, self.Lotere_D,
                              self.Lotere_E]  ### df[["Allocation"]] = [0,0,2,1,2]
        df["payoff"] = [0, 0, 0, 0, 0]
        for i in self.participant.vars["random_indexes"]:
            df.loc[i,"A_or_B"] = np.random.choice(["A","B"], p=[df.loc[i,"p1"],df.loc[i,"p2"]])
            df.loc[i,"payoff"] = df.loc[i,"x1"] * df.loc[i,"Allocation"] if df.loc[i,"A_or_B"] == "A" else df.loc[i,"x2"] * df.loc[i,"Allocation"]
        self.payoff_thisround = int(df[["payoff"]].sum())
        self.payoff = self.payoff_thisround
        if not self.training_round:
            self.participant.vars["payoff_vector"].append(self.payoff_thisround)
        self.participant.vars["prospect_table"].update(df)
        for i in range(0, len(self.participant.vars["prospect_table"])):
            if self.participant.vars["prospect_table"].loc[i, "A_or_B"] != "X":
                if self.participant.vars["prospect_table"].loc[i, "A_or_B"] == "A":
                    self.participant.vars["prospect_table"].loc[i, "p1"] = 1
                    self.participant.vars["prospect_table"].loc[i, "p2"] = 0
                elif self.participant.vars["prospect_table"].loc[i, "A_or_B"] == "B":
                    self.participant.vars["prospect_table"].loc[i, "p1"] = 0
                    self.participant.vars["prospect_table"].loc[i, "p2"] = 1
            else:
                pass
        self.participant.vars["displayed_prospects"] = df

    def set_payoff(self):
        self.payoff = self.payoff_thisround
        
    
    endowment = models.IntegerField()
    player_payoff = models.IntegerField()
    payoff_thisround = models.IntegerField()
    displayed_lotteries = models.StringField()
    training_round = models.BooleanField()

    
    Lotere_A = models.IntegerField(min=0, max=10, initial=0)
    Lotere_B = models.IntegerField(min=0, max=10, initial=0)
    Lotere_C = models.IntegerField(min=0, max=10, initial=0)
    Lotere_D = models.IntegerField(min=0, max=10, initial=0)
    Lotere_E = models.IntegerField(min=0, max=10, initial=0)
   

    ## Vars for questionnaire
    s1 = models.IntegerField(label="1) Usia:", min=14, max=35)
    s2 = models.IntegerField(choices=[[1,'Laki-laki'],[2,'Perempuan']], label='2) Jenis kelamin Anda')
    s3 = models.IntegerField(choices=[[1,'Diploma 3 (D3)'],[2,'Sarjana (S1/D4)'],[3,'Magister (S2)'],[4,'Doktoral (S3)']], label='3) Tingkat pendidikan yang sedang atau telah Anda ditempuh')
    s4 = models.IntegerField(choices=[[1,'Sekolah/Kuliah'],[2,'Lulus belum bekerja'],[3,'Bekerja']], label='4) Aktivitas utama Anda saat ini')
    s5 = models.IntegerField(choices=[[1,'Biologi'],[2,'Farmasi'],[3,'Geografi'],[4,'Kedokteran Gigi'],[5,'Kedokteran Gigi'],[6,'Kedokteran, Kesehatan Masayarakat dan Keperawatan'],[7,'Kehutanan'],[8,'MIPA'],[9,'Pertanian'],[10,'Peternakan'],[11,'Teknik'],[12,'Teknologi Pertanian'],[13,'Ekonomika dan Bisnis'],[14,'Filsafat'],[15,'Hukum'],[16,'Ilmu Budaya'],[17,'Isipol'],[18,'Psikologi'],[19,'Sekolah Vokasi'],[20,'Sekolah Pascasarjana']], label='5) Bidang studi')
    s6 = models.IntegerField(choices=[[1,'Di bawah 500.000'],[2,'500.001 s.d 1.000.000'],[3,'1.000.001 s.d 1.500.000'],[4,'1.500.001 s.d 2.000.000'],[5,'2.000.0001 s.d 2.500.000'],[6,'Di atas 2.500.0001']], label='6) Rata-rata pengeluaran setiap bulan')
    s7 = models.IntegerField(choices=[[1,'OVO'],[2,'GoPay'],[3,'ShopeePay'],[4,'Bank Mandiri'],[5,'Bank BNI']], label='7) Metode pembayaran yang Anda inginkan')
    s8 = models.StringField(label="8) Nomor HP e-money/No Rekening")
    s9 = models.IntegerField(choices=[[1,"Tidak Menarik"],[2,"Cukup Menarik"],[3,"Menarik"],[4,"Sangat Menarik"]], label='9) Seberapa menariknya eksperimen ini bagi Anda:')

 
    payoff_selected = models.IntegerField(initial=0, blank=False)
    round_selected = models.IntegerField(min=11, max=99, label="2 digit angka")
    payoff_selected_rupiah = models.FloatField(initial=0, blank=False)
