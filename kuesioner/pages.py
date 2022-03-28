from distutils.log import error
from modulefinder import AddPackagePath
import random
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

class Kuesioner(Page):
    pass

class Kuesioner2(Page):
    pass

class Survey(Page):
    form_model = 'player'
    form_fields = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10']

    def vars_for_template(self):
        treatment = self.session.config['treatment']
        return {'treatment': treatment}

class Survey2(Page):
    form_model = 'player'
    form_fields = ['s11','s12','s13','s14','s15','s16','s17','s18']

class Ambilpay(Page):
    form_model = 'player'
    form_fields = ['angka_random']

    def before_next_page(self):
        periode = self.participant.vars['periode']
        list1 = list(range(1, (periode+1)))
        rnd = random.choice(list1)
        self.participant.vars['periode_terpilih'] = rnd

class Prosespay(Page):
    form_model = 'player'
    form_fields = ['periode_terpilih','payoff_real']

    def vars_for_template(self):
        #player = self.player.participant.get_players()
        #player = self.player.participant.vars
        periode_terpilih = self.participant.vars['periode_terpilih']
        payoff_awal = self.participant.vars['payoff_awal_'+str(periode_terpilih)]
        payoff_total = self.participant.vars['total_payoff_'+str(periode_terpilih)]
        if payoff_total <= 0:
            payoff_real = 15000
        else:
            payoff_real = round(15000 + (payoff_total/1000), -3)
        return{'periode_terpilih':periode_terpilih,
                'payoff_awal':payoff_awal,
                'payoff_total':payoff_total,
               'payoff_real':payoff_real}
    
class Hasilpay(Page):
    pass


page_sequence = [Kuesioner, Survey2]
#page_sequence = [Prosespay]
