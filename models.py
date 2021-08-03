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
from otree.db.models import IntegerField

from otree.models import player


author = 'Estephany y Yadira'

doc = """
Experimento de incentivos (a partir de la tarea de conteo)
"""


class Constants(BaseConstants):
    name_in_url = 'Tar_conteo'
    players_per_group = 4
    num_rounds = 85
    task_time_c_p = 60  #prueba conteo
    task_time_c_s = 300 #conteo sin presión
    task_time_c_t = 180 #conteo con presión
    s_inc=0
    c_inc=0.2

class Subsession(BaseSubsession):
    def creating_session(self):    
        self.row1_p = ' '.join(random.choices(["0","1"], k=10))
        self.row2_p = ' '.join(random.choices(["0","1"], k=10))
        self.row3_p = ' '.join(random.choices(["0","1"], k=10))
        self.row4_p = ' '.join(random.choices(["0","1"], k=10))
        self.row5_p = ' '.join(random.choices(["0","1"], k=10))
        self.row6_p = ' '.join(random.choices(["0","1"], k=10))
        self.row7_p = ' '.join(random.choices(["0","1"], k=10))
        self.row8_p = ' '.join(random.choices(["0","1"], k=10))
        self.row9_p = ' '.join(random.choices(["0","1"], k=10))
        self.row10_p = ' '.join(random.choices(["0","1"], k=10))
        self.total_zeroes_p = sum([self.row1_p.count("0"), self.row2_p.count("0"), self.row3_p.count("0"),
                               self.row4_p.count("0"), self.row5_p.count("0"), self.row6_p.count("0"),
                               self.row7_p.count("0"), self.row8_p.count("0"), self.row9_p.count("0"), 
                               self.row10_p.count("0"),
                               ])

        self.row1_R1 = ' '.join(random.choices(["0","1"], k=10))
        self.row2_R1 = ' '.join(random.choices(["0","1"], k=10))
        self.row3_R1 = ' '.join(random.choices(["0","1"], k=10))
        self.row4_R1 = ' '.join(random.choices(["0","1"], k=10))
        self.row5_R1 = ' '.join(random.choices(["0","1"], k=10))
        self.row6_R1 = ' '.join(random.choices(["0","1"], k=10))
        self.row7_R1 = ' '.join(random.choices(["0","1"], k=10))
        self.row8_R1 = ' '.join(random.choices(["0","1"], k=10))
        self.row9_R1 = ' '.join(random.choices(["0","1"], k=10))
        self.row10_R1 = ' '.join(random.choices(["0","1"], k=10))
        self.total_zeroes_R1 = sum([self.row1_R1.count("0"), self.row2_R1.count("0"), self.row3_R1.count("0"),
                               self.row4_R1.count("0"), self.row5_R1.count("0"), self.row6_R1.count("0"),
                               self.row7_R1.count("0"), self.row8_R1.count("0"), self.row9_R1.count("0"), 
                               self.row10_R1.count("0"),
                               ])

        self.row1_R2 = ' '.join(random.choices(["0","1"], k=10))
        self.row2_R2 = ' '.join(random.choices(["0","1"], k=10))
        self.row3_R2 = ' '.join(random.choices(["0","1"], k=10))
        self.row4_R2 = ' '.join(random.choices(["0","1"], k=10))
        self.row5_R2 = ' '.join(random.choices(["0","1"], k=10))
        self.row6_R2 = ' '.join(random.choices(["0","1"], k=10))
        self.row7_R2 = ' '.join(random.choices(["0","1"], k=10))
        self.row8_R2 = ' '.join(random.choices(["0","1"], k=10))
        self.row9_R2 = ' '.join(random.choices(["0","1"], k=10))
        self.row10_R2 = ' '.join(random.choices(["0","1"], k=10))
        self.total_zeroes_R2 = sum([self.row1_R2.count("0"), self.row2_R2.count("0"), self.row3_R2.count("0"),
                               self.row4_R2.count("0"), self.row5_R2.count("0"), self.row6_R2.count("0"),
                               self.row7_R2.count("0"), self.row8_R2.count("0"), self.row9_R2.count("0"), 
                               self.row10_R2.count("0"),
                               ])

        self.row1_R3 = ' '.join(random.choices(["0","1"], k=10))
        self.row2_R3 = ' '.join(random.choices(["0","1"], k=10))
        self.row3_R3 = ' '.join(random.choices(["0","1"], k=10))
        self.row4_R3 = ' '.join(random.choices(["0","1"], k=10))
        self.row5_R3 = ' '.join(random.choices(["0","1"], k=10))
        self.row6_R3 = ' '.join(random.choices(["0","1"], k=10))
        self.row7_R3 = ' '.join(random.choices(["0","1"], k=10))
        self.row8_R3 = ' '.join(random.choices(["0","1"], k=10))
        self.row9_R3 = ' '.join(random.choices(["0","1"], k=10))
        self.row10_R3 = ' '.join(random.choices(["0","1"], k=10))
        self.total_zeroes_R3 = sum([self.row1_R3.count("0"), self.row2_R3.count("0"), self.row3_R3.count("0"),
                               self.row4_R3.count("0"), self.row5_R3.count("0"), self.row6_R3.count("0"),
                               self.row7_R3.count("0"), self.row8_R3.count("0"), self.row9_R3.count("0"), 
                               self.row10_R3.count("0"),
                               ])

        self.row1_R4 = ' '.join(random.choices(["0","1"], k=10))
        self.row2_R4 = ' '.join(random.choices(["0","1"], k=10))
        self.row3_R4 = ' '.join(random.choices(["0","1"], k=10))
        self.row4_R4 = ' '.join(random.choices(["0","1"], k=10))
        self.row5_R4 = ' '.join(random.choices(["0","1"], k=10))
        self.row6_R4 = ' '.join(random.choices(["0","1"], k=10))
        self.row7_R4 = ' '.join(random.choices(["0","1"], k=10))
        self.row8_R4 = ' '.join(random.choices(["0","1"], k=10))
        self.row9_R4 = ' '.join(random.choices(["0","1"], k=10))
        self.row10_R4 = ' '.join(random.choices(["0","1"], k=10))
        self.total_zeroes_R4 = sum([self.row1_R4.count("0"), self.row2_R4.count("0"), self.row3_R4.count("0"),
                               self.row4_R4.count("0"), self.row5_R4.count("0"), self.row6_R4.count("0"),
                               self.row7_R4.count("0"), self.row8_R4.count("0"), self.row9_R4.count("0"), 
                               self.row10_R4.count("0"),
                               ])      

    total_zeroes_p = models.IntegerField()

    row1_p = models.CharField()
    row2_p = models.CharField()
    row3_p = models.CharField()
    row4_p = models.CharField()
    row5_p = models.CharField()
    row6_p = models.CharField()
    row7_p = models.CharField()
    row8_p = models.CharField()
    row9_p = models.CharField()
    row10_p = models.CharField()

    total_zeroes_R1 = models.IntegerField()

    row1_R1 = models.CharField()
    row2_R1 = models.CharField()
    row3_R1 = models.CharField()
    row4_R1 = models.CharField()
    row5_R1 = models.CharField()
    row6_R1 = models.CharField()
    row7_R1 = models.CharField()
    row8_R1 = models.CharField()
    row9_R1 = models.CharField()
    row10_R1 = models.CharField()

    total_zeroes_R2 = models.IntegerField()

    row1_R2 = models.CharField()
    row2_R2 = models.CharField()
    row3_R2 = models.CharField()
    row4_R2 = models.CharField()
    row5_R2 = models.CharField()
    row6_R2 = models.CharField()
    row7_R2 = models.CharField()
    row8_R2 = models.CharField()
    row9_R2 = models.CharField()
    row10_R2 = models.CharField()

    total_zeroes_R3 = models.IntegerField()

    row1_R3 = models.CharField()
    row2_R3 = models.CharField()
    row3_R3 = models.CharField()
    row4_R3 = models.CharField()
    row5_R3 = models.CharField()
    row6_R3 = models.CharField()
    row7_R3 = models.CharField()
    row8_R3 = models.CharField()
    row9_R3 = models.CharField()
    row10_R3 = models.CharField()

    total_zeroes_R4 = models.IntegerField()

    row1_R4 = models.CharField()
    row2_R4 = models.CharField()
    row3_R4 = models.CharField()
    row4_R4 = models.CharField()
    row5_R4 = models.CharField()
    row6_R4 = models.CharField()
    row7_R4 = models.CharField()
    row8_R4 = models.CharField()
    row9_R4 = models.CharField()
    row10_R4 = models.CharField()


class Group(BaseGroup):
    treatment=models.StringField()

    ### Funciones para PRUEBA ###
    def total_p(self):
        for player in self.get_players():
            player_in_all_rounds = player.in_all_rounds()
            player.total_answers_correct_p=sum([p.answer_correct_p for p in player_in_all_rounds])
    
    def rank_p(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        r_1=0 ##id player
        r_2=0
        r_3=0
        r_4=0

        for p in self.get_players(): 
            if p.total_answers_correct_p >= i_4:
                i_4=p.total_answers_correct_p
                r_4=p.id_in_group
            if i_4 >= i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=r_3
                r_3=r_4
                r_4=tee
            if i_3 >= i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=r_2
                r_2=r_3
                r_3=tee
            if i_2 >= i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=r_1
                r_1=r_2
                r_2=tee
        return [i_1, i_2, i_3, i_4], [r_1, r_2, r_3, r_4]

    ### Funciones para R1 ###
    def total_R1(self):
        for player in self.get_players():
            player_in_all_rounds = player.in_all_rounds()
            player.total_answers_correct_R1=sum([p.answer_correct_R1 for p in player_in_all_rounds])
    
    puesto1_R1=models.IntegerField()
    puesto2_R1=models.IntegerField()
    puesto3_R1=models.IntegerField()
    puesto4_R1=models.IntegerField()

    def rank_R1(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        #r_1=0 ##id player
        #r_2=0
        #r_3=0
        #r_4=0
        self.puesto1_R1=0
        self.puesto2_R1=0
        self.puesto3_R1=0
        self.puesto4_R1=0

        for p in self.get_players(): 
            if p.total_answers_correct_R1 >= i_4: 
                i_4=p.total_answers_correct_R1
                self.puesto4_R1=p.id_in_group
            if i_4 >= i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=self.puesto3_R1
                self.puesto3_R1=self.puesto4_R1
                self.puesto4_R1=tee
            if i_3 >= i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=self.puesto2_R1
                self.puesto2_R1=self.puesto3_R1
                self.puesto3_R1=tee
            if i_2 >= i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=self.puesto1_R1
                self.puesto1_R1=self.puesto2_R1
                self.puesto2_R1=tee
        return [i_1, i_2, i_3, i_4], [self.puesto1_R1, self.puesto2_R1, self.puesto3_R1, self.puesto4_R1]
        #[r_1, r_2, r_3, r_4]
    
    def pp_1(self):
        if self.treatment=='T1' or self.treatment=='T3':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R1:
                    player.payoff=player.total_answers_correct_R1*Constants.c_inc
                else:
                    player.payoff=0
        elif self.treatment=='C' or self.treatment=='T2':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R1:
                    player.payoff=player.total_answers_correct_R1*Constants.s_inc
                else:
                    player.payoff=0

    ### Funciones para R2 ###
    def total_R2(self):
        for player in self.get_players():
            player_in_all_rounds = player.in_all_rounds()
            player.total_answers_correct_R2=sum([p.answer_correct_R2 for p in player_in_all_rounds])
    
    puesto1_R2=models.IntegerField()
    puesto2_R2=models.IntegerField()
    puesto3_R2=models.IntegerField()
    puesto4_R2=models.IntegerField()

    def rank_R2(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        #r_1=0 ##id player
        #r_2=0
        #r_3=0
        #r_4=0

        self.puesto1_R2=0
        self.puesto2_R2=0
        self.puesto3_R2=0
        self.puesto4_R2=0

        for p in self.get_players(): 
            if p.total_answers_correct_R2 >= i_4: 
                i_4=p.total_answers_correct_R2
                self.puesto4_R2=p.id_in_group
            if i_4 >= i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=self.puesto3_R2
                self.puesto3_R2=self.puesto4_R2
                self.puesto4_R2=tee
            if i_3 >= i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=self.puesto2_R2
                self.puesto2_R2=self.puesto3_R2
                self.puesto3_R2=tee
            if i_2 >= i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=self.puesto1_R2
                self.puesto1_R2=self.puesto2_R2
                self.puesto2_R2=tee
        return [i_1, i_2, i_3, i_4], [self.puesto1_R2, self.puesto2_R2, self.puesto3_R2, self.puesto4_R2]
    
    def pp_2(self):
        if self.treatment=='T1' or self.treatment=='T3':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R2:
                    player.payoff=player.total_answers_correct_R2*Constants.c_inc
                else:
                    player.payoff=0
        elif self.treatment=='C' or self.treatment=='T2':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R2:
                    player.payoff=player.total_answers_correct_R2*Constants.s_inc
                else:
                    player.payoff=0
    
    ### Funciones para R3 ###
    def total_R3(self):
        for player in self.get_players():
            player_in_all_rounds = player.in_all_rounds()
            player.total_answers_correct_R3=sum([p.answer_correct_R3 for p in player_in_all_rounds])
    
    puesto1_R3=models.IntegerField()
    puesto2_R3=models.IntegerField()
    puesto3_R3=models.IntegerField()
    puesto4_R3=models.IntegerField()

    def rank_R3(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        #r_1=0 ##id player
        #r_2=0
        #r_3=0
        #r_4=0

        self.puesto1_R3=0
        self.puesto2_R3=0
        self.puesto3_R3=0
        self.puesto4_R3=0

        for p in self.get_players(): 
            if p.total_answers_correct_R3 >= i_4: 
                i_4=p.total_answers_correct_R3
                self.puesto4_R3=p.id_in_group
            if i_4 >= i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=self.puesto3_R3
                self.puesto3_R3=self.puesto4_R3
                self.puesto4_R3=tee
            if i_3 >= i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=self.puesto2_R3
                self.puesto2_R3=self.puesto3_R3
                self.puesto3_R3=tee
            if i_2 >= i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=self.puesto1_R3
                self.puesto1_R3=self.puesto2_R3
                self.puesto2_R3=tee
        return [i_1, i_2, i_3, i_4], [self.puesto1_R3, self.puesto2_R3, self.puesto3_R3, self.puesto4_R3]

    def pp_3(self):
        if self.treatment=='T1' or self.treatment=='T3':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R3:
                    player.payoff=player.total_answers_correct_R3*Constants.c_inc
                else:
                    player.payoff=0
        elif self.treatment=='C' or self.treatment=='T2':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R3:
                    player.payoff=player.total_answers_correct_R3*Constants.s_inc
                else:
                    player.payoff=0
    
    ### Funciones para R4 ###
    def total_R4(self):
        for player in self.get_players():
            player_in_all_rounds = player.in_all_rounds()
            player.total_answers_correct_R4=sum([p.answer_correct_R4 for p in player_in_all_rounds])
    
    puesto1_R4=models.IntegerField()
    puesto2_R4=models.IntegerField()
    puesto3_R4=models.IntegerField()
    puesto4_R4=models.IntegerField()

    def rank_R4(self):
        i_1=0 ##puestos 
        i_2=0
        i_3=0
        i_4=0
        #r_1=0 ##id player
        #r_2=0
        #r_3=0
        #r_4=0

        self.puesto1_R4=0
        self.puesto2_R4=0
        self.puesto3_R4=0
        self.puesto4_R4=0

        for p in self.get_players(): 
            if p.total_answers_correct_R4 >= i_4: 
                i_4=p.total_answers_correct_R4
                self.puesto4_R4=p.id_in_group
            if i_4 >= i_3:
                temp=i_3
                i_3=i_4
                i_4=temp
                tee=self.puesto3_R4
                self.puesto3_R4=self.puesto4_R4
                self.puesto4_R4=tee
            if i_3 >= i_2:
                temp=i_2
                i_2=i_3
                i_3=temp
                tee=self.puesto2_R4
                self.puesto2_R4=self.puesto3_R4
                self.puesto3_R4=tee
            if i_2 >= i_1:
                temp=i_1
                i_1=i_2
                i_2=temp
                tee=self.puesto1_R4
                self.puesto1_R4=self.puesto2_R4
                self.puesto2_R4=tee
        return [i_1, i_2, i_3, i_4], [self.puesto1_R4, self.puesto2_R4, self.puesto3_R4, self.puesto4_R4]

    def pp_4(self):
        if self.treatment=='T1' or self.treatment=='T3':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R4:
                    player.payoff=player.total_answers_correct_R4*Constants.c_inc
                else:
                    player.payoff=0
        elif self.treatment=='C' or self.treatment=='T2':
            for player in self.get_players():
                if player.id_in_group == self.puesto1_R4:
                    player.payoff=player.total_answers_correct_R4*Constants.s_inc
                else:
                    player.payoff=0


def make_field(label):
    return models.IntegerField(
        choices=[[1,''],[2,''],[3,''],[4,'']],
        label=label,
        widget=widgets.RadioSelect,
    )


class Player(BasePlayer):
    num_ID = models.StringField(label='1. ¿Cuál es tu etiqueta de participante? (se mostró al inicio del experimento)')
    age = models.IntegerField(label='3. ¿Cuál es tu edad?', min=13, max=40)
    gender = models.StringField(
        choices=[['Masculino', 'Masculino'], ['Femenino', 'Femenino'],['Otro', 'Otro']],
        verbose_name='2. ¿Cuál es tu género?',
        widget=widgets.RadioSelectHorizontal,
    )
    career = models.StringField(
        choices=[['Derecho', 'Derecho'], ['Finanzas', 'Finanzas'],['Marketing',' Marketing'],
        ['Economía',' Economía'],['Contabilidad',' Contabilidad'],['Administración','Administración'],
        ['Ingeniería informática','Ingeniería informática'],['Ingeniería empresarial','Ingeniería empresarial'],
        ['Negocios internacionales','Negocios internacionales']],
        verbose_name='4. ¿Cuál es la carrera que estudias? Seleccione su carrera',
        widget=widgets.RadioSelectHorizontal,
    )
    ciclo = models.IntegerField(label='5. ¿Qué ciclo estás cursando actualmente? (Ej:si te encuentras en quinto ciclo, ingresa el número 5)')
    escala = models.StringField(label='6. ¿En qué escala de pensión te encuentras?')
    exp = models.StringField(
        choices=[['No','No'],['Sí, una vez','Sí, una vez'],['Sí, más de una vez','Sí, más de una vez']],
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
    ##enunciados adicionales para tratamiento 1 y 3
    q19 = models.IntegerField(
        choices=[[1,''],[2,''],[3,''],[4,'']],
        label='Los incentivos monetarios ofrecidos coinciden con mi esfuerzo en las tareas realizadas',
        widget=widgets.RadioSelect,
        blank=True
    )
    q20 = models.IntegerField(
        choices=[[1,''],[2,''],[3,''],[4,'']],
        label='El incentivo monetario ofrecido no está a la altura de mis expectativas',
        widget=widgets.RadioSelect,
        blank=True
    )

    ##variables para obtener puntajes
    answer_p = models.IntegerField(verbose_name="""""", blank=True, initial=0)
    answer_correct_p = models.IntegerField(initial=0)
    total_answers_correct_p = models.IntegerField()

    answer_R1 = models.IntegerField(verbose_name="""""", blank=True, initial=0)
    answer_correct_R1 = models.IntegerField(initial=0)
    total_answers_correct_R1 = models.IntegerField()

    answer_R2 = models.IntegerField(verbose_name="""""", blank=True, initial=0)
    answer_correct_R2 = models.IntegerField(initial=0)
    total_answers_correct_R2 = models.IntegerField()

    answer_R3 = models.IntegerField(verbose_name="""""", blank=True, initial=0)
    answer_correct_R3 = models.IntegerField(initial=0)
    total_answers_correct_R3 = models.IntegerField()

    answer_R4 = models.IntegerField(verbose_name="""""", blank=True, initial=0)
    answer_correct_R4 = models.IntegerField(initial=0)
    total_answers_correct_R4 = models.IntegerField()
  
