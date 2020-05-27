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


author = 'Luca Congiu'

doc = """
An example of oTree App.
"""


class Constants(BaseConstants):
    name_in_url = 'mock_app'
    players_per_group = None
    num_rounds = 1

    # Generate the indices to unpack to generate table cells in the template
    indices = [i for i in range(11)]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
