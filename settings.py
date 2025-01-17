from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
       name='mock_app',
       display_name="Mock App",
       num_demo_participants=1,
       app_sequence=['mock_app']
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
dict(
    name='Prolific_1',
    display_name='Prolific_1',
    use_secure_urls=False
),
dict(
    name='Prolific_2',
    display_name='Prolific_2',
    use_secure_urls=False
),
dict(
    name='Prolific_3',
    display_name='Prolific_3',
    use_secure_urls=False
),
dict(
    name='SONA_1',
    display_name='SONA_1',
    use_secure_urls=False
),
dict(
    name='SONA_2',
    display_name='SONA_2',
    use_secure_urls=False
),
dict(
    name='SONA_3',
    display_name='SONA_3',
    use_secure_urls=False
),
dict(
    name='BELSS',
    display_name='BELSS',
    participant_label_file='_rooms/belss.txt',
    use_secure_urls=True
),
dict(
    name='30463',
    display_name='Intro to Cognitive Science',
    use_secure_urls=False
),
dict(
    name='live_demo',
    display_name='Room for Live Demo (No Participant Labels)',
)
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'az$&mm2!2n!ztqq1(8f%i6@3z98vm_&us6799#%1^wtsnz8xc='

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
