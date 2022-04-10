from random import randint, random
from ._builtin import Page

class No1Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.sequence_setup()
        self.participant.vars['payoff_round_all'] = 0

class No2Instructions1(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'endowment': self.session.config["endowment"],
            'show_up_fee': int(self.session.config["participation_fee"]),
        }

class No2Instructions2(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'endowment': self.session.config["endowment"],
            'instrument': "preference_discovery/SC-1.jpeg",
            'result': "preference_discovery/SC-2.jpeg",
            'show_up_fee': int(self.session.config["participation_fee"]),
        }

class No2Instructions3(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'endowment': self.session.config["endowment"],
            'show_up_fee': int(self.session.config["participation_fee"]),
        }

class No2Instructions4(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'endowment': self.session.config["endowment"],
            'show_up_fee': int(self.session.config["participation_fee"]),
        }

class No2Warning(Page):

    def is_displayed(self):
        return self.round_number == self.session.config["training_rounds"] + 1

class No3Start0(Page):

    def is_displayed(self):
        return self.round_number in [1, 2, 3]

    def before_next_page(self, **kwargs):
        return {self.player.set_player_param()}

    def vars_for_template(self):
        return {
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
        }

class No3Start1(Page):

    def is_displayed(self):
        return self.round_number in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def before_next_page(self, **kwargs):
        return {self.player.set_player_param()}

    def vars_for_template(self):
        return {
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
        }

class No3Start2(Page):

    def is_displayed(self):
        return self.round_number in [14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    def before_next_page(self, **kwargs):
        return {self.player.set_player_param()}

    def vars_for_template(self):
        return {
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
        }

class No3Start3(Page):

    def is_displayed(self):
        return self.round_number in [24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

    def before_next_page(self, **kwargs):
        return {self.player.set_player_param()}

    def vars_for_template(self):
        return {
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
        }

class No4Purchase0(Page):

    def is_displayed(self):
        return self.round_number in [1, 2, 3]

    def vars_for_template(self):
        p = self.participant.vars['displayed_prospects']
        return {
            'p': self.participant.vars['displayed_prospects'],
            'rand_index': self.participant.vars["random_indexes"],
            'payoff_vector': self.participant.vars["payoff_vector"],
            'endowment': self.session.config["endowment"],
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
            'lot_1': p.iloc[0, 2], 'gain_A_1': p.iloc[0, 3], 'prob_A_1': p.iloc[0, 4], 'gain_B_1': p.iloc[0, 5],
            'prob_B_1': p.iloc[0, 6], 'rel_1': p.iloc[0, 7],
            'lot_2': p.iloc[1, 2], 'gain_A_2': p.iloc[1, 3], 'prob_A_2': p.iloc[1, 4], 'gain_B_2': p.iloc[1, 5],
            'prob_B_2': p.iloc[1, 6], 'rel_2': p.iloc[1, 7],
            'lot_3': p.iloc[2, 2], 'gain_A_3': p.iloc[2, 3], 'prob_A_3': p.iloc[2, 4], 'gain_B_3': p.iloc[2, 5],
            'prob_B_3': p.iloc[2, 6], 'rel_3': p.iloc[2, 7],
            'lot_4': p.iloc[3, 2], 'gain_A_4': p.iloc[3, 3], 'prob_A_4': p.iloc[3, 4], 'gain_B_4': p.iloc[3, 5],
            'prob_B_4': p.iloc[3, 6], 'rel_4': p.iloc[3, 7],
            'lot_5': p.iloc[4, 2], 'gain_A_5': p.iloc[4, 3], 'prob_A_5': p.iloc[4, 4], 'gain_B_5': p.iloc[4, 5],
            'prob_B_5': p.iloc[4, 6], 'rel_5': p.iloc[4, 7],
            'df': self.participant.vars["prospect_table"],
            'pagehold_timer': self.session.config['submit_delay'],
            'pagehold_timer_ths': self.session.config['submit_delay'] * 1000,
        }

    form_model = 'player'

    def get_form_fields(self):
        fields = ['Lotere_A', 'Lotere_B', 'Lotere_C', 'Lotere_D', 'Lotere_E']
        return fields

    def error_message(self, values):
        if values['Lotere_A'] + values['Lotere_B'] + values['Lotere_C'] + values['Lotere_D'] + values['Lotere_E'] <= \
                self.session.config["endowment"]:
            return
        return 'Total alokasi untuk seluruh alternatif tidak boleh lebih dari {0} poin!'.format(
            str(self.session.config["endowment"]))

    def before_next_page(self, **kwargs):
        return {self.player.payoff_realizer()}

class No4Purchase1(Page):

    def is_displayed(self):       
       return self.round_number in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def vars_for_template(self):
        p = self.participant.vars['displayed_prospects']
        return {
            'p': self.participant.vars['displayed_prospects'],
            'rand_index': self.participant.vars["random_indexes"],
            'payoff_vector': self.participant.vars["payoff_vector"],
            'endowment': self.session.config["endowment"],
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
            'lot_1': p.iloc[0, 2], 'gain_A_1': p.iloc[0, 3], 'prob_A_1': p.iloc[0, 4], 'gain_B_1': p.iloc[0, 5],
            'prob_B_1': p.iloc[0, 6], 'rel_1': p.iloc[0, 7],
            'lot_2': p.iloc[1, 2], 'gain_A_2': p.iloc[1, 3], 'prob_A_2': p.iloc[1, 4], 'gain_B_2': p.iloc[1, 5],
            'prob_B_2': p.iloc[1, 6], 'rel_2': p.iloc[1, 7],
            'lot_3': p.iloc[2, 2], 'gain_A_3': p.iloc[2, 3], 'prob_A_3': p.iloc[2, 4], 'gain_B_3': p.iloc[2, 5],
            'prob_B_3': p.iloc[2, 6], 'rel_3': p.iloc[2, 7],
            'lot_4': p.iloc[3, 2], 'gain_A_4': p.iloc[3, 3], 'prob_A_4': p.iloc[3, 4], 'gain_B_4': p.iloc[3, 5],
            'prob_B_4': p.iloc[3, 6], 'rel_4': p.iloc[3, 7],
            'lot_5': p.iloc[4, 2], 'gain_A_5': p.iloc[4, 3], 'prob_A_5': p.iloc[4, 4], 'gain_B_5': p.iloc[4, 5],
            'prob_B_5': p.iloc[4, 6], 'rel_5': p.iloc[4, 7],
            'df': self.participant.vars["prospect_table"],
            'pagehold_timer': self.session.config['submit_delay'],
            'pagehold_timer_ths': self.session.config['submit_delay'] * 1000,
        }

    form_model = 'player'

    def get_form_fields(self):
        fields = ['Lotere_A', 'Lotere_B', 'Lotere_C', 'Lotere_D', 'Lotere_E']
        return fields

    def error_message(self, values):
        if values['Lotere_A'] + values['Lotere_B'] + values['Lotere_C'] + values['Lotere_D'] + values['Lotere_E'] <= \
                self.session.config["endowment"]:
            return
        return 'Total alokasi untuk seluruh alternatif tidak boleh lebih dari {0} poin!'.format(
            str(self.session.config["endowment"]))

    def before_next_page(self, **kwargs):
        return {self.player.payoff_realizer()}
    
class No4Purchase2(Page):

    def is_displayed(self):
        return self.round_number in [14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    def vars_for_template(self):
        p = self.participant.vars['displayed_prospects']
        return {
            'p': self.participant.vars['displayed_prospects'],
            'rand_index': self.participant.vars["random_indexes"],
            'payoff_vector': self.participant.vars["payoff_vector"],
            'endowment': self.session.config["endowment"],
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
            'lot_1': p.iloc[0, 2], 'gain_A_1': p.iloc[0, 3], 'prob_A_1': p.iloc[0, 4], 'gain_B_1': p.iloc[0, 5],
            'prob_B_1': p.iloc[0, 6], 'rel_1': p.iloc[0, 7],
            'lot_2': p.iloc[1, 2], 'gain_A_2': p.iloc[1, 3], 'prob_A_2': p.iloc[1, 4], 'gain_B_2': p.iloc[1, 5],
            'prob_B_2': p.iloc[1, 6], 'rel_2': p.iloc[1, 7],
            'lot_3': p.iloc[2, 2], 'gain_A_3': p.iloc[2, 3], 'prob_A_3': p.iloc[2, 4], 'gain_B_3': p.iloc[2, 5],
            'prob_B_3': p.iloc[2, 6], 'rel_3': p.iloc[2, 7],
            'lot_4': p.iloc[3, 2], 'gain_A_4': p.iloc[3, 3], 'prob_A_4': p.iloc[3, 4], 'gain_B_4': p.iloc[3, 5],
            'prob_B_4': p.iloc[3, 6], 'rel_4': p.iloc[3, 7],
            'lot_5': p.iloc[4, 2], 'gain_A_5': p.iloc[4, 3], 'prob_A_5': p.iloc[4, 4], 'gain_B_5': p.iloc[4, 5],
            'prob_B_5': p.iloc[4, 6], 'rel_5': p.iloc[4, 7],
            'df': self.participant.vars["prospect_table"],
            'pagehold_timer': self.session.config['submit_delay'],
            'pagehold_timer_ths': self.session.config['submit_delay'] * 1000,
        }

    form_model = 'player'

    def get_form_fields(self):
        fields = ['Lotere_A', 'Lotere_B', 'Lotere_C', 'Lotere_D', 'Lotere_E']
        return fields

    def error_message(self, values):
        if values['Lotere_A'] + values['Lotere_B'] + values['Lotere_C'] + values['Lotere_D'] + values['Lotere_E'] <= \
                self.session.config["endowment"]:
            return
        return 'Total alokasi untuk seluruh alternatif tidak boleh lebih dari {0} poin!'.format(
            str(self.session.config["endowment"]))

    def before_next_page(self, **kwargs):
        return {self.player.payoff_realizer()}

class No4Purchase3(Page):

    def is_displayed(self):
        return self.round_number in [24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

    def vars_for_template(self):
        p = self.participant.vars['displayed_prospects']
        return {
            'p': self.participant.vars['displayed_prospects'],
            'rand_index': self.participant.vars["random_indexes"],
            'payoff_vector': self.participant.vars["payoff_vector"],
            'endowment': self.session.config["endowment"],
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
            'lot_1': p.iloc[0, 2], 'gain_A_1': p.iloc[0, 3], 'prob_A_1': p.iloc[0, 4], 'gain_B_1': p.iloc[0, 5],
            'prob_B_1': p.iloc[0, 6], 'rel_1': p.iloc[0, 7],
            'lot_2': p.iloc[1, 2], 'gain_A_2': p.iloc[1, 3], 'prob_A_2': p.iloc[1, 4], 'gain_B_2': p.iloc[1, 5],
            'prob_B_2': p.iloc[1, 6], 'rel_2': p.iloc[1, 7],
            'lot_3': p.iloc[2, 2], 'gain_A_3': p.iloc[2, 3], 'prob_A_3': p.iloc[2, 4], 'gain_B_3': p.iloc[2, 5],
            'prob_B_3': p.iloc[2, 6], 'rel_3': p.iloc[2, 7],
            'lot_4': p.iloc[3, 2], 'gain_A_4': p.iloc[3, 3], 'prob_A_4': p.iloc[3, 4], 'gain_B_4': p.iloc[3, 5],
            'prob_B_4': p.iloc[3, 6], 'rel_4': p.iloc[3, 7],
            'lot_5': p.iloc[4, 2], 'gain_A_5': p.iloc[4, 3], 'prob_A_5': p.iloc[4, 4], 'gain_B_5': p.iloc[4, 5],
            'prob_B_5': p.iloc[4, 6], 'rel_5': p.iloc[4, 7],
            'df': self.participant.vars["prospect_table"],
            'pagehold_timer': self.session.config['submit_delay'],
            'pagehold_timer_ths': self.session.config['submit_delay'] * 1000,
        }

    form_model = 'player'

    def get_form_fields(self):
        fields = ['Lotere_A', 'Lotere_B', 'Lotere_C', 'Lotere_D', 'Lotere_E']
        return fields

    def error_message(self, values):
        if values['Lotere_A'] + values['Lotere_B'] + values['Lotere_C'] + values['Lotere_D'] + values['Lotere_E'] <= \
                self.session.config["endowment"]:
            return
        return 'Total alokasi untuk seluruh alternatif tidak boleh lebih dari {0} poin!'.format(
            str(self.session.config["endowment"]))

    def before_next_page(self, **kwargs):
        return {self.player.payoff_realizer()}

class No5Result0(Page):

    def is_displayed(self):
        return self.round_number in [1, 2, 3]

    def vars_for_template(self):
        df = self.participant.vars['displayed_prospects'][["x1", "x2", "Allocation", "A_or_B", "payoff"]]
        p = self.participant.vars['displayed_prospects']
        return {
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
            'A1': df.iloc[0, 0], 'B1': df.iloc[0, 1], 'C1': df.iloc[0, 2], 'D1': df.iloc[0, 3], 'E1': df.iloc[0, 4],
            'A2': df.iloc[1, 0], 'B2': df.iloc[1, 1], 'C2': df.iloc[1, 2], 'D2': df.iloc[1, 3], 'E2': df.iloc[1, 4],
            'A3': df.iloc[2, 0], 'B3': df.iloc[2, 1], 'C3': df.iloc[2, 2], 'D3': df.iloc[2, 3], 'E3': df.iloc[2, 4],
            'A4': df.iloc[3, 0], 'B4': df.iloc[3, 1], 'C4': df.iloc[3, 2], 'D4': df.iloc[3, 3], 'E4': df.iloc[3, 4],
            'A5': df.iloc[4, 0], 'B5': df.iloc[4, 1], 'C5': df.iloc[4, 2], 'D5': df.iloc[4, 3], 'E5': df.iloc[4, 4],
            'payoff_thisround': self.player.payoff_thisround,
            'lot_1': p.iloc[0, 2],
            'lot_2': p.iloc[1, 2],
            'lot_3': p.iloc[2, 2],
            'lot_4': p.iloc[3, 2],
            'lot_5': p.iloc[4, 2]
        }

class No5Result1(Page):

    def is_displayed(self):
        return self.round_number in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def vars_for_template(self):
        df = self.participant.vars['displayed_prospects'][["x1", "x2", "Allocation", "A_or_B", "payoff"]]
        p = self.participant.vars['displayed_prospects']
        self.participant.vars['payoff_round_'+str(self.round_number)] =  self.player.payoff_thisround
        self.participant.vars['payoff_round_all'] += self.player.payoff_thisround
        return {
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
            'A1': df.iloc[0, 0], 'B1': df.iloc[0, 1], 'C1': df.iloc[0, 2], 'D1': df.iloc[0, 3], 'E1': df.iloc[0, 4],
            'A2': df.iloc[1, 0], 'B2': df.iloc[1, 1], 'C2': df.iloc[1, 2], 'D2': df.iloc[1, 3], 'E2': df.iloc[1, 4],
            'A3': df.iloc[2, 0], 'B3': df.iloc[2, 1], 'C3': df.iloc[2, 2], 'D3': df.iloc[2, 3], 'E3': df.iloc[2, 4],
            'A4': df.iloc[3, 0], 'B4': df.iloc[3, 1], 'C4': df.iloc[3, 2], 'D4': df.iloc[3, 3], 'E4': df.iloc[3, 4],
            'A5': df.iloc[4, 0], 'B5': df.iloc[4, 1], 'C5': df.iloc[4, 2], 'D5': df.iloc[4, 3], 'E5': df.iloc[4, 4],
            'payoff_thisround': self.player.payoff_thisround,
            'lot_1': p.iloc[0, 2],
            'lot_2': p.iloc[1, 2],
            'lot_3': p.iloc[2, 2],
            'lot_4': p.iloc[3, 2],
            'lot_5': p.iloc[4, 2]
        }
    
class No5Result2(Page):

    def is_displayed(self):
        return self.round_number in [14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    def vars_for_template(self):
        df = self.participant.vars['displayed_prospects'][["x1", "x2", "Allocation", "A_or_B", "payoff"]]
        p = self.participant.vars['displayed_prospects']
        self.participant.vars['payoff_round_'+str(self.round_number)] =  self.player.payoff_thisround
        self.participant.vars['payoff_round_all'] += self.player.payoff_thisround
        return {
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
            'A1': df.iloc[0, 0], 'B1': df.iloc[0, 1], 'C1': df.iloc[0, 2], 'D1': df.iloc[0, 3], 'E1': df.iloc[0, 4],
            'A2': df.iloc[1, 0], 'B2': df.iloc[1, 1], 'C2': df.iloc[1, 2], 'D2': df.iloc[1, 3], 'E2': df.iloc[1, 4],
            'A3': df.iloc[2, 0], 'B3': df.iloc[2, 1], 'C3': df.iloc[2, 2], 'D3': df.iloc[2, 3], 'E3': df.iloc[2, 4],
            'A4': df.iloc[3, 0], 'B4': df.iloc[3, 1], 'C4': df.iloc[3, 2], 'D4': df.iloc[3, 3], 'E4': df.iloc[3, 4],
            'A5': df.iloc[4, 0], 'B5': df.iloc[4, 1], 'C5': df.iloc[4, 2], 'D5': df.iloc[4, 3], 'E5': df.iloc[4, 4],
            'payoff_thisround': self.player.payoff_thisround,
            'lot_1': p.iloc[0, 2],
            'lot_2': p.iloc[1, 2],
            'lot_3': p.iloc[2, 2],
            'lot_4': p.iloc[3, 2],
            'lot_5': p.iloc[4, 2]
        }
    
class No5Result3(Page):

    def is_displayed(self):
        return self.round_number in [24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

    def vars_for_template(self):
        df = self.participant.vars['displayed_prospects'][["x1", "x2", "Allocation", "A_or_B", "payoff"]]
        p = self.participant.vars['displayed_prospects']
        self.participant.vars['payoff_round_'+str(self.round_number)] =  self.player.payoff_thisround
        self.participant.vars['payoff_round_all'] += self.player.payoff_thisround
        return {
            'training': self.round_number <= self.session.config["training_rounds"],
            'training_round': self.round_number,
            'round': self.round_number - self.session.config["training_rounds"],
            'A1': df.iloc[0, 0], 'B1': df.iloc[0, 1], 'C1': df.iloc[0, 2], 'D1': df.iloc[0, 3], 'E1': df.iloc[0, 4],
            'A2': df.iloc[1, 0], 'B2': df.iloc[1, 1], 'C2': df.iloc[1, 2], 'D2': df.iloc[1, 3], 'E2': df.iloc[1, 4],
            'A3': df.iloc[2, 0], 'B3': df.iloc[2, 1], 'C3': df.iloc[2, 2], 'D3': df.iloc[2, 3], 'E3': df.iloc[2, 4],
            'A4': df.iloc[3, 0], 'B4': df.iloc[3, 1], 'C4': df.iloc[3, 2], 'D4': df.iloc[3, 3], 'E4': df.iloc[3, 4],
            'A5': df.iloc[4, 0], 'B5': df.iloc[4, 1], 'C5': df.iloc[4, 2], 'D5': df.iloc[4, 3], 'E5': df.iloc[4, 4],
            'payoff_thisround': self.player.payoff_thisround,
            'lot_1': p.iloc[0, 2],
            'lot_2': p.iloc[1, 2],
            'lot_3': p.iloc[2, 2],
            'lot_4': p.iloc[3, 2],
            'lot_5': p.iloc[4, 2]
        }

class No6EndQuestionnaire(Page):
    form_model = 'player'
    form_fields = ['s1','s2','s3','s4','s5','s6','s7','s8','s9']

    def is_displayed(self):
        return self.round_number == self.session.config['rounds']

class No6EndResult(Page):
    form_model = 'player'
    form_fields = ['payoff_selected','round_selected','payoff_selected_rupiah']

    def is_displayed(self):
        return self.round_number == self.session.config['rounds']

    def vars_for_template(self):
        rnd = randint(4,33)
        payoff_selected = self.participant.vars['payoff_round_'+str(rnd)]
        payoff_all = self.participant.vars['payoff_round_all']
        return {
            'player_payoff': self.player.payoff,
            'round_selected' : rnd,
            'payoff_selected' : payoff_selected,
            'payoff_selected_rupiah' : payoff_selected * 500 + 5000,
            'payoff_all' : payoff_all,
            'payoff_all_rupiah' : payoff_all * 500 + 5000,
        }

#class No7Thanks(Page):

#     pass
#    def is_displayed(self):
#        return self.round_number == 1



page_sequence = [No1Introduction,
                 No2Instructions1,
                 No2Instructions2,
                 No2Instructions3,
                 No2Instructions4,
                 No2Warning,
                 No3Start0,
                 No4Purchase0,
                 No5Result0,
                 No3Start1,
                 No4Purchase1,
                 No5Result1,
                 No3Start2,
                 No4Purchase2,
                 No5Result2,
                 No3Start3,
                 No4Purchase3,
                 No5Result3,
                 No6EndQuestionnaire,
                 No6EndResult,
                 #No7Thanks,
                 ]

