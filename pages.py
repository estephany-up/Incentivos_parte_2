from otree.models import player
from incentivos.models import Subsession
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player, Group
import time, random


class MyPage(Page):
    pass


class Instrucciones_conteo(Page):
    def is_displayed(self):
        return self.round_number == 1

    #def before_next_page(self):
    #    self.session.vars['expiry'] = time.time() + Constants.task_time_c_p

    def before_next_page(self):
        p1 = self.group.get_player_by_id(1)
        treatment = p1.participant.vars['group_treatment']
        if treatment=='C' or treatment=='T1':
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_s
        else:
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_t

class Prueba_conteo(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    timer_text = 'Tiempo que le falta para completar la ronda: '
    timeout_seconds=Constants.task_time_c_p

    def before_next_page(self):
        p1 = self.group.get_player_by_id(1)
        treatment = p1.participant.vars['group_treatment']
        if treatment=='C' or treatment=='T1':
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_s
        else:
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_t

class Tarea_conteo_R1(Page):    
    if Group.treatment=='C' or Group.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_c_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds=Constants.task_time_c_t

    form_model = "player"
    form_fields = ["answer_R1"]

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
        #self.player.is_correct_R1()
        #player = self.player
        if self.player.answer_R1 == self.subsession.total_zeroes:
            self.player.answer_correct_R1 = 1
        elif self.player.answer_R1 == None:
            self.player.answer_correct_R1 = 0
        else:
            self.player.answer_correct_R1 = 0
        #timeout_happened = self.timeout_happened
        #if timeout_happened:
        #    self.player.participant.vars['timedout_realeffort_R1'] = True
        #else:
        #    self.player.participant.vars['timedout_realeffort_R1'] = False
        #if self.round_number == Constants.num_rounds: #creo que esto no es necesario
        #if self.round_number < Constants.num_rounds:
        player_in_all_rounds = self.player.in_all_rounds()
        self.player.total_answers_correct_R1 = sum([p.answer_correct_R1 for p in player_in_all_rounds])
        #if self.round_number == Constants.num_rounds:
           # player_last=self.player.in_round(Constants.num_rounds)
        #    self.player.total_answers_correct_R1=Player.total_answers_correct_R1 + Player.answer_correct_R1

            #self.player.participant.vars['realeffort_correct_R1'] = sum([p.answer_correct_R1 for p in player_in_all_rounds])
            #self.session.vars['realeffort_possible_R1'] = Constants.num_rounds
            #print(self.player.participant.vars['realeffort_correct_R1'])
        return self.player.total_answers_correct_R1


class Ranking_conteo_R1(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        p_1=self.player.total_answers_correct_R1
    #    pt_p, p_p = self.group.rank_R1()
    #    p_p1=p_p[1]
    #    p_p2=p_p[2]
    #    p_p3=p_p[3]
    #    p_p4=p_p[4]
    #    pt_p1=pt_p[1]
    #    pt_p2=pt_p[2]
    #    pt_p3=pt_p[3]
    #    pt_p4=pt_p[4]
        return dict(p_1=p_1
    #        p_p1=p_p1, pt_p1=pt_p1,
    #        p_p2=p_p2, pt_p2=pt_p2,
    #        p_p3=p_p3, pt_p3=pt_p3,
    #        p_p4=p_p4, pt_p4=pt_p4
        )

    #def is_displayed(self):
        #return self.player.id_in_group == 1 and self.player.waited_too_long == 0 and 

class Tarea_conteo_R2(Page):
    pass

class Ranking_conteo_R2(Page):
    pass

class Tarea_conteo_R3(Page):
    pass

class Ranking_conteo_R3(Page):
    pass

class Tarea_conteo_R4(Page):
    pass

class Ranking_conteo_R4(Page):
    pass

class Encuesta_final(Page):
    def is_displayed(self):
        return self.round_number == 10

    form_model = 'player'
    form_fields = ['num_ID','gender','age','career','ciclo','escala','exp',
    'q1','q2','q3','q4','q5','q6','q7','q8','q9','q10', 'q11','q12','q13',
    'q14','q15','q16','q17','q18','q19','q20',]

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass


page_sequence = [
    #MyPage,
    Instrucciones_conteo,
    #Prueba_conteo,
    Tarea_conteo_R1,
    Ranking_conteo_R1,
    #Tarea_conteo_R2,
    #Ranking_conteo_R2,
    #Tarea_conteo_R3,
    #Ranking_conteo_R3,
    #Tarea_conteo_R4,
    #Ranking_conteo_R4,
    #Encuesta_final, 
    #ResultsWaitPage, 
    #Results
    ]
