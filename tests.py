from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield pages.Instruccion_conteo
        yield pages.Tarea_conteo, dict(answer=random.randint(30,75))