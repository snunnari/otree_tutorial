from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):

    def is_displayed(self):
        return self.round_number == 1  # displayed only at round 1


class Structure(Page):
    pass


class Bootstrap(Page):
    pass


class Instructions(Page):
    pass


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [Welcome, Structure, Bootstrap, Instructions, MyPage]
