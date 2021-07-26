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

    def before_next_page(self):
        self.session.vars['expiry'] = time.time() + Constants.task_time_c_p

    #def before_next_page(self):
    #    p1 = self.group.get_player_by_id(1)
    #    treatment = p1.participant.vars['group_treatment']
    #    if treatment=='C' or treatment=='T1':
    #        self.session.vars['expiry'] = time.time() + Constants.task_time_c_s
    #    else:
    #        self.session.vars['expiry'] = time.time() + Constants.task_time_c_t

class Prueba_conteo(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    timer_text = 'Tiempo que le falta para completar la ronda: '
    timeout_seconds = Constants.task_time_c_p

    form_model = "player"
    form_fields = ["answer_p"]

    def vars_for_template(self):
        return {
            'row1' : self.subsession.row1_p,
            'row2' : self.subsession.row2_p,
            'row3' : self.subsession.row3_p,
            'row4' : self.subsession.row4_p,
            'row5' : self.subsession.row5_p,
            'row6' : self.subsession.row6_p,
            'row7' : self.subsession.row7_p,
            'row8' : self.subsession.row8_p,
            'row9' : self.subsession.row9_p,
            'row10' : self.subsession.row10_p,
        }
    
    def get_timeout_seconds(self):
        return self.session.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.session.vars['expiry'] - time.time() > 2 

    def before_next_page(self):
        if self.player.answer_p == self.subsession.total_zeroes_p:
            self.player.answer_correct_p = 1
        elif self.player.answer_p == None:
            self.player.answer_correct_p = 0
        else:
            self.player.answer_correct_p = 0

class Wait_p(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    after_all_players_arrive='total_p'

class Ranking_conteo_p(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        pt_p, p_p = self.group.rank_p()
        p_p1=p_p[0]
        p_p2=p_p[1]
        p_p3=p_p[2]
        p_p4=p_p[3]
        pt_p1=pt_p[0]
        pt_p2=pt_p[1]
        pt_p3=pt_p[2]
        pt_p4=pt_p[3]
        return dict(p_p1=p_p1, p_p2=p_p2, p_p3=p_p3, p_p4=p_p4,
        pt_p1=pt_p1, pt_p2=pt_p2, pt_p3=pt_p3, pt_p4=pt_p4)

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
        timeout_seconds = Constants.task_time_c_t

    form_model = "player"
    form_fields = ["answer_R1"]

    def vars_for_template(self):
        return {
            'row1' : self.subsession.row1_R1,
            'row2' : self.subsession.row2_R1,
            'row3' : self.subsession.row3_R1,
            'row4' : self.subsession.row4_R1,
            'row5' : self.subsession.row5_R1,
            'row6' : self.subsession.row6_R1,
            'row7' : self.subsession.row7_R1,
            'row8' : self.subsession.row8_R1,
            'row9' : self.subsession.row9_R1,
            'row10' : self.subsession.row10_R1,
        }
    
    def get_timeout_seconds(self):
        return self.session.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.session.vars['expiry'] - time.time() > 2 

    def before_next_page(self):
        if self.player.answer_R1 == self.subsession.total_zeroes_R1:
            self.player.answer_correct_R1 = 1
        elif self.player.answer_R1 == None:
            self.player.answer_correct_R1 = 0
        else:
            self.player.answer_correct_R1 = 0

class Wait_1(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    after_all_players_arrive='total_R1'

class Ranking_conteo_R1(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        pt_p, p_p = self.group.rank_R1()
        p_p1=p_p[0]
        p_p2=p_p[1]
        p_p3=p_p[2]
        p_p4=p_p[3]
        pt_p1=pt_p[0]
        pt_p2=pt_p[1]
        pt_p3=pt_p[2]
        pt_p4=pt_p[3]
        return dict(p_p1=p_p1, p_p2=p_p2, p_p3=p_p3, p_p4=p_p4,
        pt_p1=pt_p1, pt_p2=pt_p2, pt_p3=pt_p3, pt_p4=pt_p4)
    
    def before_next_page(self):
        p1 = self.group.get_player_by_id(1)
        treatment = p1.participant.vars['group_treatment']
        if treatment=='C' or treatment=='T1':
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_s
        else:
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_t

class Tarea_conteo_R2(Page):
    if Group.treatment=='C' or Group.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_c_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_c_t

    form_model = "player"
    form_fields = ["answer_R2"]

    def vars_for_template(self):
        return {
            'row1' : self.subsession.row1_R2,
            'row2' : self.subsession.row2_R2,
            'row3' : self.subsession.row3_R2,
            'row4' : self.subsession.row4_R2,
            'row5' : self.subsession.row5_R2,
            'row6' : self.subsession.row6_R2,
            'row7' : self.subsession.row7_R2,
            'row8' : self.subsession.row8_R2,
            'row9' : self.subsession.row9_R2,
            'row10' : self.subsession.row10_R2,
        }
    
    def get_timeout_seconds(self):
        return self.session.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.session.vars['expiry'] - time.time() > 2 

    def before_next_page(self):
        if self.player.answer_R2 == self.subsession.total_zeroes_R2:
            self.player.answer_correct_R2 = 1
        elif self.player.answer_R2 == None:
            self.player.answer_correct_R2 = 0
        else:
            self.player.answer_correct_R2 = 0

class Wait_2(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    after_all_players_arrive='total_R2'

class Ranking_conteo_R2(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        pt_p, p_p = self.group.rank_R2()
        p_p1=p_p[0]
        p_p2=p_p[1]
        p_p3=p_p[2]
        p_p4=p_p[3]
        pt_p1=pt_p[0]
        pt_p2=pt_p[1]
        pt_p3=pt_p[2]
        pt_p4=pt_p[3]
        return dict(p_p1=p_p1, p_p2=p_p2, p_p3=p_p3, p_p4=p_p4,
        pt_p1=pt_p1, pt_p2=pt_p2, pt_p3=pt_p3, pt_p4=pt_p4)
    
    def before_next_page(self):
        p1 = self.group.get_player_by_id(1)
        treatment = p1.participant.vars['group_treatment']
        if treatment=='C' or treatment=='T1':
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_s
        else:
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_t

class Tarea_conteo_R3(Page):
    if Group.treatment=='C' or Group.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_c_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_c_t

    form_model = "player"
    form_fields = ["answer_R3"]

    def vars_for_template(self):
        return {
            'row1' : self.subsession.row1_R3,
            'row2' : self.subsession.row2_R3,
            'row3' : self.subsession.row3_R3,
            'row4' : self.subsession.row4_R3,
            'row5' : self.subsession.row5_R3,
            'row6' : self.subsession.row6_R3,
            'row7' : self.subsession.row7_R3,
            'row8' : self.subsession.row8_R3,
            'row9' : self.subsession.row9_R3,
            'row10' : self.subsession.row10_R3,
        }
    
    def get_timeout_seconds(self):
        return self.session.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.session.vars['expiry'] - time.time() > 2 

    def before_next_page(self):
        if self.player.answer_R3 == self.subsession.total_zeroes_R3:
            self.player.answer_correct_R3 = 1
        elif self.player.answer_R3 == None:
            self.player.answer_correct_R3 = 0
        else:
            self.player.answer_correct_R3 = 0

class Wait_3(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    after_all_players_arrive='total_R3'

class Ranking_conteo_R3(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        pt_p, p_p = self.group.rank_R3()
        p_p1=p_p[0]
        p_p2=p_p[1]
        p_p3=p_p[2]
        p_p4=p_p[3]
        pt_p1=pt_p[0]
        pt_p2=pt_p[1]
        pt_p3=pt_p[2]
        pt_p4=pt_p[3]
        return dict(p_p1=p_p1, p_p2=p_p2, p_p3=p_p3, p_p4=p_p4,
        pt_p1=pt_p1, pt_p2=pt_p2, pt_p3=pt_p3, pt_p4=pt_p4)
    
    def before_next_page(self):
        p1 = self.group.get_player_by_id(1)
        treatment = p1.participant.vars['group_treatment']
        if treatment=='C' or treatment=='T1':
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_s
        else:
            self.session.vars['expiry'] = time.time() + Constants.task_time_c_t

class Tarea_conteo_R4(Page):
    if Group.treatment=='C' or Group.treatment=='T1':
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_c_s
    else:
        timer_text = 'Tiempo que le falta para completar la ronda: '
        timeout_seconds = Constants.task_time_c_t

    form_model = "player"
    form_fields = ["answer_R4"]

    def vars_for_template(self):
        return {
            'row1' : self.subsession.row1_R4,
            'row2' : self.subsession.row2_R4,
            'row3' : self.subsession.row3_R4,
            'row4' : self.subsession.row4_R4,
            'row5' : self.subsession.row5_R4,
            'row6' : self.subsession.row6_R4,
            'row7' : self.subsession.row7_R4,
            'row8' : self.subsession.row8_R4,
            'row9' : self.subsession.row9_R4,
            'row10' : self.subsession.row10_R4,
        }
    
    def get_timeout_seconds(self):
        return self.session.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.session.vars['expiry'] - time.time() > 2 

    def before_next_page(self):
        if self.player.answer_R4 == self.subsession.total_zeroes_R4:
            self.player.answer_correct_R4 = 1
        elif self.player.answer_R4 == None:
            self.player.answer_correct_R4 = 0
        else:
            self.player.answer_correct_R4 = 0

class Wait_4(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    after_all_players_arrive='total_R4'

class Ranking_conteo_R4(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        pt_p, p_p = self.group.rank_R4()
        p_p1=p_p[0]
        p_p2=p_p[1]
        p_p3=p_p[2]
        p_p4=p_p[3]
        pt_p1=pt_p[0]
        pt_p2=pt_p[1]
        pt_p3=pt_p[2]
        pt_p4=pt_p[3]
        return dict(p_p1=p_p1, p_p2=p_p2, p_p3=p_p3, p_p4=p_p4,
        pt_p1=pt_p1, pt_p2=pt_p2, pt_p3=pt_p3, pt_p4=pt_p4)

class Encuesta_final(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['num_ID','gender','age','career','ciclo','escala','exp',
    'q1','q2','q3','q4','q5','q6','q7','q8','q9','q10', 'q11','q12','q13',
    'q14','q15','q16','q17','q18','q19','q20',]

##solo son para probar códigos
class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return dict(a=self.player.pay)


page_sequence = [
    #MyPage,
    Instrucciones_conteo,
    Prueba_conteo,
    Wait_p,
    Ranking_conteo_p,
    Tarea_conteo_R1,
    Wait_1,
    Ranking_conteo_R1,
    Tarea_conteo_R2,
    Wait_2,
    Ranking_conteo_R2,
    Tarea_conteo_R3,
    Wait_3,
    Ranking_conteo_R3,
    Tarea_conteo_R4,
    Wait_4,
    Ranking_conteo_R4,
    Encuesta_final, 
    #ResultsWaitPage, 
    #Results
    ]



        #timeout_happened = self.timeout_happened
        #if timeout_happened:
        #    self.player.participant.vars['timedout_realeffort_R1'] = True
        #else:
        #    self.player.participant.vars['timedout_realeffort_R1'] = False
        #if self.round_number == Constants.num_rounds: #creo que esto no es necesario
        #player_in_all_rounds = self.player.in_all_rounds()
        #self.player.total_answers_correct_R1 = sum([p.answer_correct_R1 for p in player_in_all_rounds])
            #self.player.participant.vars['realeffort_correct_R1'] = sum([p.answer_correct_R1 for p in player_in_all_rounds])
            #self.session.vars['realeffort_possible_R1'] = Constants.num_rounds
            #print(self.player.participant.vars['realeffort_correct_R1'])
        #return self.player.total_answers_correct_R1
