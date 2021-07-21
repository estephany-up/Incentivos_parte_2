from typing import List
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

import random
from random import randint
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from string import digits, ascii_lowercase

from otree.models import player


author = 'Estephany y Yadira'

doc = """
Experimento de incentivos (a partir de la tarea de conteo)
"""


class Constants(BaseConstants):
    name_in_url = 'Tar_conteo'
    players_per_group = 4
    num_rounds = 10
    task_time_c_p = 60  #prueba conteo
    task_time_c_s = 300 #conteo sin presión
    task_time_c_t = 180 #conteo con presión
    point=c(1)

#crear lista de ceros y unos
def func(n):
    lst=[]
    for i in range (1,n):
        a_i = str(random.choice([0,1]))
        lst.append(a_i)
    return (lst)

class Subsession(BaseSubsession):
    ##por ahora sólo se ha asignado tratamiento por participante
    ##cambiar más adelante a grupos
    def creating_session(self):    
        self.row1 = ' '.join(random.choices(["0","1"], k=10))
        self.row2 = ' '.join(random.choices(["0","1"], k=10))
        self.row3 = ' '.join(random.choices(["0","1"], k=10))
        self.row4 = ' '.join(random.choices(["0","1"], k=10))
        self.row5 = ' '.join(random.choices(["0","1"], k=10))
        self.row6 = ' '.join(random.choices(["0","1"], k=10))
        self.row7 = ' '.join(random.choices(["0","1"], k=10))
        self.row8 = ' '.join(random.choices(["0","1"], k=10))
        self.row9 = ' '.join(random.choices(["0","1"], k=10))
        self.row10 = ' '.join(random.choices(["0","1"], k=10))
        self.total_zeroes = sum([self.row1.count("0"), self.row2.count("0"), self.row3.count("0"),
                               self.row4.count("0"), self.row5.count("0"), self.row6.count("0"),
                               self.row7.count("0"), self.row8.count("0"), self.row9.count("0"), 
                               self.row10.count("0"),
                               ])

######falta juntar el tratamiento par ambas apps
        if self.round_number==1:
            for g in self.get_groups():
                p1=g.get_player_by_id(1)
                p1.participant.vars['group_treatment']=random.choice(['C', 'T1', 'T2', 'T3'])
                Group.treatment=p1.participant.vars['group_treatment']
               #Group.treatment = random.choice(['C', 'T1', 'T2', 'T3'])
                print('Treatment:', p1.participant.vars['group_treatment'])
        

    total_zeroes = models.IntegerField()

    row1 = models.CharField()
    row2 = models.CharField()
    row3 = models.CharField()
    row4 = models.CharField()
    row5 = models.CharField()
    row6 = models.CharField()
    row7 = models.CharField()
    row8 = models.CharField()
    row9 = models.CharField()
    row10 = models.CharField()

class Group(BaseGroup):
   treatment=models.StringField()


def make_field(label):
    return models.IntegerField(
        choices=[[1,''],[2,''],[3,''],[4,'']],
        label=label,
        widget=widgets.RadioSelect,
    )

class Player(BasePlayer):
    
    num_ID = models.StringField(label='1. ¿Cuál es tu número ID')
    age = models.IntegerField(label='3. ¿Cuál es tu edad?', min=13, max=40)
    gender = models.StringField(
        choices=[[0, 'Masculino'], [1, 'Femenino']],
        label='2. ¿Cuál es tu género?',
        widget=widgets.RadioSelect,
    )
    career = models.StringField(
        choices=[['Derecho', 'Derecho'], ['Finanzas', 'Finanzas'],['Marketing','Marketing'],
        ['Economía','Economía'],['Contabilidad','Contabilidad'],['Administración','Administración'],
        ['Ingeniería informática','Ingeniería informática'],['Ingeniería empresarial','Ingeniería empresarial'],
        ['Negocios internacionales','Negocios internacionales']],
        label='4. ¿Cuál es la carrera que estudias? Seleccione su carrera',
        widget=widgets.RadioSelect,
    )
    ciclo = models.IntegerField(label='5. ¿Qué ciclo estás cursando actualmente? (Ej:5to)')
    escala = models.StringField(label='6. ¿En qué escala de pensión te encuentras?')
    exp = models.StringField(
        choices=[[0,'No'],[1,'Sí, una vez'],[2,'Sí, más de una vez']],
        label='7. ¿Has participado en un experimento anteriormente?',
    )
    ##enunciados de competencia
    q1 = make_field('Me gusta competir')
    q2 = make_field('Me gusta competir individualmente')
    q3 = make_field('Disfruto competir contra un oponente')
    q4 = make_field('No me gusta competir contra otras personas')
    q5 = make_field('Competir contra otros me da satisfacción')
    q6 = make_field('La situaciones de competencia me parecen incómodas')
    q7 = make_field('Temo competir contra otras personas')
    q8 = make_field('Intento evitar competir contra otras personas')
    q9 = make_field('Trato de superar a los demás a menudo')
    q10 = make_field('No me gustan los juegos en los que el ganador se lleva todo el premio')
    q11 = make_field('La competencia destruye la amistad')
    q12 = make_field('Los juegos sin un solo ganador son aburridos')
    q13 = make_field('Usualmente no es importante para mí ser el mejor')
    q14 = make_field('Cuando juego, me gusta llevar el conteo de la puntuación')
    ##enunciados de incentivos para todos
    q15 = make_field('Le doy importancia a los incentivos monetarios')
    q16 = make_field('Los incentivos monetarios no tienen ningún valor para mí')
    q17 = make_field('Los incentivos monetarios tienen efectos positivos en mi performance')
    q18 = make_field('Un incentivo monetario atractivo aumentará mi motivación para trabajar más duro')
    ##enunciados adicionales para tratameinto 1 y 3
    q19 = make_field('Los incentivos monetarios ofrecidos coinciden con mi esfuerzo en las tareas realizadas')
    q20 = make_field('El incentivo monetario ofrecido no está a la altura de mis expectativas')
    

    def is_correct_R1(self):
        if self.answer_R1 == self.subsession.total_zeroes:
            self.answer_correct_R1 = 1
        else:
            self.answer_correct_R1 = 0

    answer_R1 = models.IntegerField(verbose_name="""""", blank = True)
    answer_correct_R1 = models.BooleanField()
    total_answers_correct_R1 = models.IntegerField()


    def rank_R1(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        r_1=0 ##id player
        r_2=0
        r_3=0
        r_4=0

        for p in self.group.get_players(): 
            if p.total_answers_correct_R1 > i_4:
                i_4=p.total_answers_correct_R1
                r_4=p
            if i_4 > i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=r_3
                r_3=r_4
                r_4=tee
            if i_3 > i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=r_2
                r_2=r_3
                r_3=tee
            if i_2 > i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=r_1
                r_1=r_2
                r_2=tee

        return [i_1, i_2, i_3, i_4], [r_1, r_2, r_3, r_4]

    pt_p, p_p = rank_R1(self=player)


    def is_correct_R2(self):
        if self.answer_R2 == self.subsession.total_zeroes:
            self.answer_correct_R2 = 1
        else:
            self.answer_correct_R2 = 0

    answer_R2 = models.IntegerField(verbose_name="""""", blank = True)
    answer_correct_R2 = models.BooleanField()
    total_answers_correct_R2 = models.IntegerField()



#            elif i_3==i_2:
#                if i_2==random.choice(i_3,i_2):
#                    i_2=i_2
#                else:
#                    i_3=i_4

#def rank_giver(Numbers):
#    first = 0
#    second = 0
#    third = 0
#    for num in Numbers:
#        if num > third:
#          third = num
#        if third > second:
#            temp = second
#            second = third
#            third = temp
#        if second > first:
#            temp = first
#            first = second                                           
#            second = temp
#            
#    return first,second,third
#
#print(rank_giver([10, 20, 50, 99]))   

#<table>
#{% for p in subsession.get_players %}
#<tr>
#<td>{{ p.id_in_group }}</td>
#<td>{{ p.total_payoff}}</td>
#<td>{{ p.donation}}</td>
#</tr>
#{% endfor %}
#</table>


#class Player(BasePlayer):
#     random_id = models.IntegerField()

#class Subsession(BaseSubsession):
#     def before_session_starts(self):
#         for p in self.get_players():
#             p.random_id = p.id_in_group