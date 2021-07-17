from incentivos.models import Subsession
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
import time

class MyPage(Page):
    pass


class Instrucciones_conteo(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        if Player.treatment=='C' or Player.treatment=='T1':
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_s
        else:
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_t

class Prueba_conteo(Page):
    pass

class Tarea_conteo(Page):
    if Player.treatment=='C' or Player.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_c_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds=Constants.task_time_c_t

    form_model = "player"
    form_fields = ["answer"]

    def vars_for_template(self):
        return {
            'row1' : self.subsession.row1,
            'row2' : self.subsession.row2,
            'row3' : self.subsession.row3,
            'row4' : self.subsession.row4,
            'row5' : self.subsession.row5,
            'row6' : self.subsession.row6,
            'row7' : self.subsession.row7,
            'row8' : self.subsession.row8,
            'row9' : self.subsession.row9,
            'row10' : self.subsession.row10,
        }
    
    def get_timeout_seconds(self):
        return self.session.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.session.vars['expiry'] - time.time() > 2

    def before_next_page(self):
        self.player.is_correct()
        player = self.player
        timeout_happened = self.timeout_happened
        if timeout_happened:
             player.participant.vars["timedout_realeffort"] = True
        else:
            player.participant.vars["timedout_realeffort"] = False
        if self.player.round_number == Constants.num_rounds:
            player_in_all_rounds = self.player.in_all_rounds()
            self.player.total_answers_correct = sum([p.answer_correct for p in player_in_all_rounds])
            self.player.participant.vars["realeffort_correct"] = sum([p.answer_correct for p in player_in_all_rounds])
            self.session.vars['realeffort_possible'] = Constants.num_rounds
            print(self.player.participant.vars['realeffort_correct'])


class Ranking_conteo(Page):
    pass

class Encuesta_final(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass


page_sequence = [
    #MyPage,
    Instrucciones_conteo,
    #Prueba_conteo,
    Tarea_conteo,
    #Ranking_conteo,
    Encuesta_final, 
    #ResultsWaitPage, 
    #Results
    ]
