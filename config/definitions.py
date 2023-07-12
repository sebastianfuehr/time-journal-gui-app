import os

APP_VERSION = 'v0.1.2-alpha'

APP_ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

# Filter options
FILTER_PERIODS = ['Max', '1 Year', '6 Months', 'Month', 'Week']

# Medal thresholds in seconds (h*m*s)
MEDAL_TH_BRONZE = 2*60*60
MEDAL_TH_SILVER = 4*60*60
MEDAL_TH_GOLD = 6*60*60

#######################################################################
# STYLING
#######################################################################

# Font options
DASHBOARD_HEADING_SIZE = 24
FORM_HEADING_FONT = (None, 24, 'bold')
COMBO_BOX_FONT = (None, 16)
FONTS = {
    'default': (None, 16)
}

# Colors
COLORS = {
    'text': 'white',
    'highlight': '#21eaad'
}

#######################################################################
# LAYOUT STYLING
#######################################################################

# MENUS
MAINFRAME_TABS_NAV = {
    'elements': ['Dashboard', 'Time Entries', 'Projects', 'Categories'],
    'padx': (40, 0),
    'pady': 20,
    'side': 'left',
    'font': (None, 20),
    'colors': {'text': COLORS['text'], 'highlight': COLORS['highlight']}
}
FILTER_PERIODS = {
    'elements': ['Max', '1 Year', '6 Months', 'Month', 'Week'],
    'padx': 10,
    'pady': 10,
    'side': 'right',
    'font': FONTS['default'],
    'colors': {'text': COLORS['text'], 'highlight': COLORS['highlight']}
}

# TABS

# FORMS
