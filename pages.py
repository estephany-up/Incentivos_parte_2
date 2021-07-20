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
        self.player.is_correct_R1()
        player = self.player
        timeout_happened = self.timeout_happened
        if timeout_happened:
             player.participant.vars["timedout_realeffort_R1"] = True
        else:
            player.participant.vars["timedout_realeffort_R1"] = False
        if self.player.round_number == Constants.num_rounds: #creo que esto no es necesario
            player_in_all_rounds = self.player.in_all_rounds()
            player.total_answers_correct_R1 = sum([p.answer_correct_R1 for p in player_in_all_rounds])
            self.player.participant.vars["realeffort_correct_R1"] = sum([p.answer_correct_R1 for p in player_in_all_rounds])
            self.session.vars['realeffort_possible_R1'] = Constants.num_rounds
            print(self.player.participant.vars['realeffort_correct_R1'])
        


class Ranking_conteo_R1(Page):
    def is_displayed(self):
        return self.round_number == 10
    
    def vars_for_template(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        p_1=0 #id del puesto
        p_2=0
        p_3=0
        p_4=0

        for p in self.group.get_players(): 
            if p.total_answers_correct_R1 > i_4:
                i_4=p.total_answers_correct_R1
                p_4=p
            if i_4 > i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=p_3
                p_3=p_4
                p_4=tee
            if i_3 > i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=p_2
                p_2=p_3
                p_3=tee
            if i_2 > i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=p_1
                p_1=p_2
                p_2=tee
        return dict(
            pt_1=i_1, pt_2=i_2, pt_3=i_3, pt_4=i_4,
            p_1=p_1, p_2=p_2, p_3=p_3, p_4=p_4,
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
