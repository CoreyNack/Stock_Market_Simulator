#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 02, 2024, at 11:37
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

CRNT_savings = 10000 
CRNT_investment = 10000 
ins_loops=0
year=0
min=0
max=15
ins_loop = 1
ins_image = "Ins0.png"
prac_block_count = 0
SRmapping_all = [['Q','P', 'Q', 'P'], ['Q', 'P', 'P', 'Q'], ['P', 'Q', 'Q', 'P'], ['P', 'Q', 'P', 'Q']] 
SRmapping = SRmapping_all[1]
vaid_key_list = ['q','p']
phase = 'prac'
prac_block_count = 0
main_block_count = 2
tsk_txt_maker_color = "Black"
tsk_txt = "    "
bloc_acc = 100
corr_count = 0
assets_avaliable = 100000


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Stock_Market_Simulator'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\cnack\\Desktop\\Stock_market_simulator\\Stock_Market_Simulator_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Invest_Instructions"
Invest_InstructionsClock = core.Clock()
instructions_image_maker = visual.ImageStim(
    win=win,
    name='instructions_image_maker', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
instruction_response = keyboard.Keyboard()

# Initialize components for Routine "Salary"
SalaryClock = core.Clock()
salary_background_image = visual.ImageStim(
    win=win,
    name='salary_background_image', 
    image='Salary_background.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
accept_button = visual.ImageStim(
    win=win,
    name='accept_button', 
    image='Accept.png', mask=None,
    ori=0, pos=(0,-.04), size=(0.75, 0.19779),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
salary_mouse = event.Mouse(win=win)
x, y = [None, None]
salary_mouse.mouseClock = core.Clock()
year_readout = visual.TextStim(win=win, name='year_readout',
    text='',
    font='Calibri',
    pos=(-.41, .39), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "invest_blank"
invest_blankClock = core.Clock()
blank_image = visual.ImageStim(
    win=win,
    name='blank_image', 
    image='blank_background.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
year_readout_6 = visual.TextStim(win=win, name='year_readout_6',
    text='',
    font='Calibri',
    pos=(-.41, .39), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
savings_readout_3 = visual.TextStim(win=win, name='savings_readout_3',
    text='',
    font='Calibri',
    pos=(-.1, .2801), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
investment_readout_3 = visual.TextStim(win=win, name='investment_readout_3',
    text='',
    font='Calibri',
    pos=(-.1, .21), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Choice"
ChoiceClock = core.Clock()
choice_background_image_maker = visual.ImageStim(
    win=win,
    name='choice_background_image_maker', 
    image='Choice_background.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
investment_choice = event.Mouse(win=win)
x, y = [None, None]
investment_choice.mouseClock = core.Clock()
buy = visual.ImageStim(
    win=win,
    name='buy', units='height', 
    image='buy_button.png', mask=None,
    ori=0, pos=(-0.33, -.04), size=(0.25, 0.1007),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
sell = visual.ImageStim(
    win=win,
    name='sell', 
    image='sin', mask=None,
    ori=0, pos=(0,-.04), size=(0.25, 0.1007),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
no_change = visual.ImageStim(
    win=win,
    name='no_change', 
    image='nothing_button.png', mask=None,
    ori=0, pos=(.33, -.04), size=(0.25, 0.1007),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
timer = visual.TextStim(win=win, name='timer',
    text='',
    font='Calibri',
    pos=(-.17,-.19), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
year_readout_3 = visual.TextStim(win=win, name='year_readout_3',
    text='',
    font='Calibri',
    pos=(-.41, .39), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
savings_readout = visual.TextStim(win=win, name='savings_readout',
    text='',
    font='Calibri',
    pos=(-.1, .2801), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
investment_readout = visual.TextStim(win=win, name='investment_readout',
    text='',
    font='Calibri',
    pos=(-.1, .21), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
late = visual.TextStim(win=win, name='late',
    text='200 dollar late fee assigned! Choose faster',
    font='Arial',
    pos=(0, -.30), height=0.05, wrapWidth=None, ori=0, 
    color='Red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
Price_readout = visual.TextStim(win=win, name='Price_readout',
    text='',
    font='Calibri',
    pos=(.4, .21), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "invest_blank"
invest_blankClock = core.Clock()
blank_image = visual.ImageStim(
    win=win,
    name='blank_image', 
    image='blank_background.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
year_readout_6 = visual.TextStim(win=win, name='year_readout_6',
    text='',
    font='Calibri',
    pos=(-.41, .39), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
savings_readout_3 = visual.TextStim(win=win, name='savings_readout_3',
    text='',
    font='Calibri',
    pos=(-.1, .2801), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
investment_readout_3 = visual.TextStim(win=win, name='investment_readout_3',
    text='',
    font='Calibri',
    pos=(-.1, .21), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Quantity"
QuantityClock = core.Clock()
quantity_background = visual.ImageStim(
    win=win,
    name='quantity_background', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
slider_mouse = event.Mouse(win=win)
x, y = [None, None]
slider_mouse.mouseClock = core.Clock()
money_submit_button = visual.ImageStim(
    win=win,
    name='money_submit_button', 
    image='submit.png', mask=None,
    ori=0, pos=(.3, -.3), size=(0.25, 0.1007),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
slider_value = visual.TextStim(win=win, name='slider_value',
    text='',
    font='Arial',
    pos=(0, -.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
click_line = visual.TextStim(win=win, name='click_line',
    text='',
    font='Arial',
    pos=(0, -.1), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
year_readout_4 = visual.TextStim(win=win, name='year_readout_4',
    text='',
    font='Calibri',
    pos=(-.41, .39), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
savings_readout_2 = visual.TextStim(win=win, name='savings_readout_2',
    text='',
    font='Calibri',
    pos=(-.1, .2801), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
investment_readout_2 = visual.TextStim(win=win, name='investment_readout_2',
    text='',
    font='Calibri',
    pos=(-.1, .21), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
Quantity_slider = visual.Slider(win=win, name='Quantity_slider',
    startValue=None, size=(1.3, 0.05), pos=(0, -0.055), units=None,
    labels=(min, max), ticks=(min, max), granularity=5,
    style=['rating', 'triangleMarker'], styleTweaks=[], opacity=1,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-9, readOnly=False)
timer_2 = visual.TextStim(win=win, name='timer_2',
    text='',
    font='Calibri',
    pos=(-.17,-.19), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
late_2 = visual.TextStim(win=win, name='late_2',
    text='200 dollar late fee assigned! Choose faster',
    font='Arial',
    pos=(0, -.30), height=0.05, wrapWidth=None, ori=0, 
    color='Red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
Price_readout_2 = visual.TextStim(win=win, name='Price_readout_2',
    text='',
    font='Calibri',
    pos=(.4, .21), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "invest_blank"
invest_blankClock = core.Clock()
blank_image = visual.ImageStim(
    win=win,
    name='blank_image', 
    image='blank_background.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
year_readout_6 = visual.TextStim(win=win, name='year_readout_6',
    text='',
    font='Calibri',
    pos=(-.41, .39), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
savings_readout_3 = visual.TextStim(win=win, name='savings_readout_3',
    text='',
    font='Calibri',
    pos=(-.1, .2801), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
investment_readout_3 = visual.TextStim(win=win, name='investment_readout_3',
    text='',
    font='Calibri',
    pos=(-.1, .21), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "News"
NewsClock = core.Clock()
news_background_image = visual.ImageStim(
    win=win,
    name='news_background_image', 
    image='news_background.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
main_news_image = visual.ImageStim(
    win=win,
    name='main_news_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
secondary_news_image = visual.ImageStim(
    win=win,
    name='secondary_news_image', 
    image='sin', mask=None,
    ori=0, pos=(.29, -.25), size=(0.6, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
tweet_1 = visual.ImageStim(
    win=win,
    name='tweet_1', 
    image='sin', mask=None,
    ori=0, pos=(-.42, -.3), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
tweet_2 = visual.ImageStim(
    win=win,
    name='tweet_2', 
    image='sin', mask=None,
    ori=0, pos=(.42, .25), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
Accept_news = keyboard.Keyboard()
year_readout_2 = visual.TextStim(win=win, name='year_readout_2',
    text='',
    font='Calibri',
    pos=(-.41, .39), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "End_Results"
End_ResultsClock = core.Clock()
end_results_background = visual.ImageStim(
    win=win,
    name='end_results_background', 
    image='results_background.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
results_image = visual.ImageStim(
    win=win,
    name='results_image', 
    image='sin', mask=None,
    ori=0, pos=(0.25, -0.202), size=(.999, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
new_year_button = visual.ImageStim(
    win=win,
    name='new_year_button', 
    image='new_year.png', mask=None,
    ori=0, pos=(.5, .12), size=(0.4, 0.10991),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
new_year_mouse = event.Mouse(win=win)
x, y = [None, None]
new_year_mouse.mouseClock = core.Clock()
year_readout_5 = visual.TextStim(win=win, name='year_readout_5',
    text='',
    font='Calibri',
    pos=(-.41, .39), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
savings_readout_4 = visual.TextStim(win=win, name='savings_readout_4',
    text='',
    font='Calibri',
    pos=(-.1, .2801), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
investment_readout_4 = visual.TextStim(win=win, name='investment_readout_4',
    text='',
    font='Calibri',
    pos=(-.1, .21), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
savings_results = visual.TextStim(win=win, name='savings_results',
    text='',
    font='Calibri',
    pos=(.15, .2801), height=0.05, wrapWidth=None, ori=0, 
    color='Darkgreen', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
Investment_results = visual.TextStim(win=win, name='Investment_results',
    text='',
    font='Calibri',
    pos=(.15, .21), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "final_results"
final_resultsClock = core.Clock()
Results_image_maker = visual.ImageStim(
    win=win,
    name='Results_image_maker', 
    image='final_reslts_background.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
final_results_key_resp = keyboard.Keyboard()
final_money_readout = visual.TextStim(win=win, name='final_money_readout',
    text='',
    font='Calibri',
    pos=(0, .15), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank_text = visual.TextStim(win=win, name='blank_text',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Questions"
QuestionsClock = core.Clock()
strategy_question = visual.TextStim(win=win, name='strategy_question',
    text='During the investment simulator, did you have a strategy for buying and selling, or were the choices more random? ',
    font='Calibri',
    pos=(0, .4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Strategy = visual.Slider(win=win, name='Strategy',
    startValue=None, size=(1.2, 0.08), pos=(0, .27), units=None,
    labels=("Very strategic", "Neutral", "Very Random"), ticks=(1, 2, 3, 4, 5), granularity=1,
    style=['rating', 'triangleMarker'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
negative_emotion = visual.TextStim(win=win, name='negative_emotion',
    text='How did you feel about the bad years in the sumulator (market crashes)? ',
    font='Calibri',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Emotion_response = visual.Slider(win=win, name='Emotion_response',
    startValue=None, size=(1.2, 0.08), pos=(0, -.1), units=None,
    labels=("very negative", "neutral", "very positive"), ticks=(1, 2, 3, 4, 5), granularity=1,
    style=['rating', 'triangleMarker'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-3, readOnly=False)
sell_pressure_text = visual.TextStim(win=win, name='sell_pressure_text',
    text='Did you feel pressure to sell stocks during the market crashes? ',
    font='Calibri',
    pos=(0, -.27), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
sell_pressure_response = visual.Slider(win=win, name='sell_pressure_response',
    startValue=None, size=(1.2, 0.08), pos=(0, -.36), units=None,
    labels=("strong pressure", "neutral", "no pressure"), ticks=(1, 2, 3, 4, 5), granularity=1,
    style=['rating', 'triangleMarker'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-5, readOnly=False)
qual_submit_button = visual.ImageStim(
    win=win,
    name='qual_submit_button', 
    image='submit.png', mask=None,
    ori=0, pos=(.5, .45), size=(0.25, 0.1007),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
slider_mouse_2 = event.Mouse(win=win)
x, y = [None, None]
slider_mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "end"
endClock = core.Clock()
End_text = visual.TextStim(win=win, name='End_text',
    text='You have finished the experiment. You may now find the researcher to recieve SONA credit.\n\nPress spacebar to close the window',
    font='Arial',
    pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instruction_loop = data.TrialHandler(nReps=13, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instruction_loop')
thisExp.addLoop(instruction_loop)  # add the loop to the experiment
thisInstruction_loop = instruction_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction_loop.rgb)
if thisInstruction_loop != None:
    for paramName in thisInstruction_loop:
        exec('{} = thisInstruction_loop[paramName]'.format(paramName))

for thisInstruction_loop in instruction_loop:
    currentLoop = instruction_loop
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction_loop.rgb)
    if thisInstruction_loop != None:
        for paramName in thisInstruction_loop:
            exec('{} = thisInstruction_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Invest_Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    ins_image = "Ins"+str(ins_loop)+".png"
    instructions_image_maker.setImage(ins_image)
    instruction_response.keys = []
    instruction_response.rt = []
    _instruction_response_allKeys = []
    # keep track of which components have finished
    Invest_InstructionsComponents = [instructions_image_maker, instruction_response]
    for thisComponent in Invest_InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Invest_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Invest_Instructions"-------
    while continueRoutine:
        # get current time
        t = Invest_InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Invest_InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_image_maker* updates
        if instructions_image_maker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_image_maker.frameNStart = frameN  # exact frame index
            instructions_image_maker.tStart = t  # local t and not account for scr refresh
            instructions_image_maker.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_image_maker, 'tStartRefresh')  # time at next scr refresh
            instructions_image_maker.setAutoDraw(True)
        
        # *instruction_response* updates
        waitOnFlip = False
        if instruction_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instruction_response.frameNStart = frameN  # exact frame index
            instruction_response.tStart = t  # local t and not account for scr refresh
            instruction_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_response, 'tStartRefresh')  # time at next scr refresh
            instruction_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instruction_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instruction_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruction_response.status == STARTED and not waitOnFlip:
            theseKeys = instruction_response.getKeys(keyList=['space'], waitRelease=False)
            _instruction_response_allKeys.extend(theseKeys)
            if len(_instruction_response_allKeys):
                instruction_response.keys = _instruction_response_allKeys[-1].name  # just the last key pressed
                instruction_response.rt = _instruction_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Invest_InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Invest_Instructions"-------
    for thisComponent in Invest_InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ins_loop = ins_loop + 1
    # the Routine "Invest_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 13 repeats of 'instruction_loop'


# set up handler to look after randomisation of conditions etc
yearly_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('investment_conditions.csv'),
    seed=None, name='yearly_loop')
thisExp.addLoop(yearly_loop)  # add the loop to the experiment
thisYearly_loop = yearly_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisYearly_loop.rgb)
if thisYearly_loop != None:
    for paramName in thisYearly_loop:
        exec('{} = thisYearly_loop[paramName]'.format(paramName))

for thisYearly_loop in yearly_loop:
    currentLoop = yearly_loop
    # abbreviate parameter names if possible (e.g. rgb = thisYearly_loop.rgb)
    if thisYearly_loop != None:
        for paramName in thisYearly_loop:
            exec('{} = thisYearly_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Salary"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the salary_mouse
    salary_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    year_readout.setText(year)
    # keep track of which components have finished
    SalaryComponents = [salary_background_image, accept_button, salary_mouse, year_readout]
    for thisComponent in SalaryComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SalaryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Salary"-------
    while continueRoutine:
        # get current time
        t = SalaryClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SalaryClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *salary_background_image* updates
        if salary_background_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            salary_background_image.frameNStart = frameN  # exact frame index
            salary_background_image.tStart = t  # local t and not account for scr refresh
            salary_background_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(salary_background_image, 'tStartRefresh')  # time at next scr refresh
            salary_background_image.setAutoDraw(True)
        
        # *accept_button* updates
        if accept_button.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            accept_button.frameNStart = frameN  # exact frame index
            accept_button.tStart = t  # local t and not account for scr refresh
            accept_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(accept_button, 'tStartRefresh')  # time at next scr refresh
            accept_button.setAutoDraw(True)
        # *salary_mouse* updates
        if salary_mouse.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            salary_mouse.frameNStart = frameN  # exact frame index
            salary_mouse.tStart = t  # local t and not account for scr refresh
            salary_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(salary_mouse, 'tStartRefresh')  # time at next scr refresh
            salary_mouse.status = STARTED
            salary_mouse.mouseClock.reset()
            prevButtonState = salary_mouse.getPressed()  # if button is down already this ISN'T a new click
        if salary_mouse.status == STARTED:  # only update if started and not finished!
            buttons = salary_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(accept_button)
                        clickableList = accept_button
                    except:
                        clickableList = [accept_button]
                    for obj in clickableList:
                        if obj.contains(salary_mouse):
                            gotValidClick = True
                            salary_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *year_readout* updates
        if year_readout.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            year_readout.frameNStart = frameN  # exact frame index
            year_readout.tStart = t  # local t and not account for scr refresh
            year_readout.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(year_readout, 'tStartRefresh')  # time at next scr refresh
            year_readout.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SalaryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Salary"-------
    for thisComponent in SalaryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    CRNT_savings = CRNT_savings + 30000
    crnt_price = "The current price of investments is $"+str(price)+" per stock"
    # store data for yearly_loop (TrialHandler)
    # the Routine "Salary" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "invest_blank"-------
    continueRoutine = True
    routineTimer.add(0.600000)
    # update component parameters for each repeat
    year_readout_6.setText(year)
    savings_readout_3.setText(CRNT_savings)
    investment_readout_3.setText(CRNT_investment)
    # keep track of which components have finished
    invest_blankComponents = [blank_image, year_readout_6, savings_readout_3, investment_readout_3]
    for thisComponent in invest_blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    invest_blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "invest_blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = invest_blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=invest_blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_image* updates
        if blank_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_image.frameNStart = frameN  # exact frame index
            blank_image.tStart = t  # local t and not account for scr refresh
            blank_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_image, 'tStartRefresh')  # time at next scr refresh
            blank_image.setAutoDraw(True)
        if blank_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_image.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                blank_image.tStop = t  # not accounting for scr refresh
                blank_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_image, 'tStopRefresh')  # time at next scr refresh
                blank_image.setAutoDraw(False)
        
        # *year_readout_6* updates
        if year_readout_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            year_readout_6.frameNStart = frameN  # exact frame index
            year_readout_6.tStart = t  # local t and not account for scr refresh
            year_readout_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(year_readout_6, 'tStartRefresh')  # time at next scr refresh
            year_readout_6.setAutoDraw(True)
        if year_readout_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > year_readout_6.tStartRefresh + .6-frameTolerance:
                # keep track of stop time/frame for later
                year_readout_6.tStop = t  # not accounting for scr refresh
                year_readout_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(year_readout_6, 'tStopRefresh')  # time at next scr refresh
                year_readout_6.setAutoDraw(False)
        
        # *savings_readout_3* updates
        if savings_readout_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            savings_readout_3.frameNStart = frameN  # exact frame index
            savings_readout_3.tStart = t  # local t and not account for scr refresh
            savings_readout_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(savings_readout_3, 'tStartRefresh')  # time at next scr refresh
            savings_readout_3.setAutoDraw(True)
        if savings_readout_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > savings_readout_3.tStartRefresh + .6-frameTolerance:
                # keep track of stop time/frame for later
                savings_readout_3.tStop = t  # not accounting for scr refresh
                savings_readout_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(savings_readout_3, 'tStopRefresh')  # time at next scr refresh
                savings_readout_3.setAutoDraw(False)
        
        # *investment_readout_3* updates
        if investment_readout_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            investment_readout_3.frameNStart = frameN  # exact frame index
            investment_readout_3.tStart = t  # local t and not account for scr refresh
            investment_readout_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(investment_readout_3, 'tStartRefresh')  # time at next scr refresh
            investment_readout_3.setAutoDraw(True)
        if investment_readout_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > investment_readout_3.tStartRefresh + .6-frameTolerance:
                # keep track of stop time/frame for later
                investment_readout_3.tStop = t  # not accounting for scr refresh
                investment_readout_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(investment_readout_3, 'tStopRefresh')  # time at next scr refresh
                investment_readout_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in invest_blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "invest_blank"-------
    for thisComponent in invest_blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Choice"-------
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('pre_choice_savings', CRNT_savings)
    thisExp.addData('pre_choice_investment', CRNT_investment)
    # setup some python lists for storing info about the investment_choice
    investment_choice.clicked_name = []
    gotValidClick = False  # until a click is received
    sell.setImage('sell_button.png')
    year_readout_3.setText(year)
    savings_readout.setText(CRNT_savings)
    investment_readout.setText(CRNT_investment)
    Price_readout.setText(crnt_price)
    # keep track of which components have finished
    ChoiceComponents = [choice_background_image_maker, investment_choice, buy, sell, no_change, timer, year_readout_3, savings_readout, investment_readout, late, Price_readout]
    for thisComponent in ChoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Choice"-------
    while continueRoutine:
        # get current time
        t = ChoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ChoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *choice_background_image_maker* updates
        if choice_background_image_maker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_background_image_maker.frameNStart = frameN  # exact frame index
            choice_background_image_maker.tStart = t  # local t and not account for scr refresh
            choice_background_image_maker.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_background_image_maker, 'tStartRefresh')  # time at next scr refresh
            choice_background_image_maker.setAutoDraw(True)
        # *investment_choice* updates
        if investment_choice.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            investment_choice.frameNStart = frameN  # exact frame index
            investment_choice.tStart = t  # local t and not account for scr refresh
            investment_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(investment_choice, 'tStartRefresh')  # time at next scr refresh
            investment_choice.status = STARTED
            investment_choice.mouseClock.reset()
            prevButtonState = investment_choice.getPressed()  # if button is down already this ISN'T a new click
        if investment_choice.status == STARTED:  # only update if started and not finished!
            buttons = investment_choice.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(buy, sell, no_change)
                        clickableList = buy, sell, no_change
                    except:
                        clickableList = [buy, sell, no_change]
                    for obj in clickableList:
                        if obj.contains(investment_choice):
                            gotValidClick = True
                            investment_choice.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *buy* updates
        if buy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buy.frameNStart = frameN  # exact frame index
            buy.tStart = t  # local t and not account for scr refresh
            buy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buy, 'tStartRefresh')  # time at next scr refresh
            buy.setAutoDraw(True)
        
        # *sell* updates
        if sell.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sell.frameNStart = frameN  # exact frame index
            sell.tStart = t  # local t and not account for scr refresh
            sell.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sell, 'tStartRefresh')  # time at next scr refresh
            sell.setAutoDraw(True)
        if sell.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sell.tStartRefresh + assets_avaliable-frameTolerance:
                # keep track of stop time/frame for later
                sell.tStop = t  # not accounting for scr refresh
                sell.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sell, 'tStopRefresh')  # time at next scr refresh
                sell.setAutoDraw(False)
        
        # *no_change* updates
        if no_change.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no_change.frameNStart = frameN  # exact frame index
            no_change.tStart = t  # local t and not account for scr refresh
            no_change.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no_change, 'tStartRefresh')  # time at next scr refresh
            no_change.setAutoDraw(True)
        
        # *timer* updates
        if timer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timer.frameNStart = frameN  # exact frame index
            timer.tStart = t  # local t and not account for scr refresh
            timer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer, 'tStartRefresh')  # time at next scr refresh
            timer.setAutoDraw(True)
        if timer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                timer.tStop = t  # not accounting for scr refresh
                timer.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer, 'tStopRefresh')  # time at next scr refresh
                timer.setAutoDraw(False)
        if timer.status == STARTED:  # only update if drawing
            timer.setText(int(20+(routineTimer.getTime())), log=False)
        
        # *year_readout_3* updates
        if year_readout_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            year_readout_3.frameNStart = frameN  # exact frame index
            year_readout_3.tStart = t  # local t and not account for scr refresh
            year_readout_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(year_readout_3, 'tStartRefresh')  # time at next scr refresh
            year_readout_3.setAutoDraw(True)
        
        # *savings_readout* updates
        if savings_readout.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            savings_readout.frameNStart = frameN  # exact frame index
            savings_readout.tStart = t  # local t and not account for scr refresh
            savings_readout.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(savings_readout, 'tStartRefresh')  # time at next scr refresh
            savings_readout.setAutoDraw(True)
        
        # *investment_readout* updates
        if investment_readout.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            investment_readout.frameNStart = frameN  # exact frame index
            investment_readout.tStart = t  # local t and not account for scr refresh
            investment_readout.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(investment_readout, 'tStartRefresh')  # time at next scr refresh
            investment_readout.setAutoDraw(True)
        
        # *late* updates
        if late.status == NOT_STARTED and tThisFlip >= 20.0-frameTolerance:
            # keep track of start time/frame for later
            late.frameNStart = frameN  # exact frame index
            late.tStart = t  # local t and not account for scr refresh
            late.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(late, 'tStartRefresh')  # time at next scr refresh
            late.setAutoDraw(True)
        
        # *Price_readout* updates
        if Price_readout.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Price_readout.frameNStart = frameN  # exact frame index
            Price_readout.tStart = t  # local t and not account for scr refresh
            Price_readout.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Price_readout, 'tStartRefresh')  # time at next scr refresh
            Price_readout.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choice"-------
    for thisComponent in ChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if investment_choice.clicked_name[0] == 'no_change':
        present_quantity = 0
        range = (0, 15)
        qant_back = 'Quantity_background_image.png'
    if investment_choice.clicked_name[0] == 'buy':
        present_quantity = 1
        min = 10
        max = int(CRNT_savings)
        qant_back = 'buy_background.png'
    if investment_choice.clicked_name[0] == 'sell':
        present_quantity = 1
        min = 10
        max = int(CRNT_investment)
        qant_back = 'Quantity_background_image.png'
    # store data for yearly_loop (TrialHandler)
    x, y = investment_choice.getPos()
    buttons = investment_choice.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(buy, sell, no_change)
            clickableList = buy, sell, no_change
        except:
            clickableList = [buy, sell, no_change]
        for obj in clickableList:
            if obj.contains(investment_choice):
                gotValidClick = True
                investment_choice.clicked_name.append(obj.name)
    yearly_loop.addData('investment_choice.x', x)
    yearly_loop.addData('investment_choice.y', y)
    yearly_loop.addData('investment_choice.leftButton', buttons[0])
    yearly_loop.addData('investment_choice.midButton', buttons[1])
    yearly_loop.addData('investment_choice.rightButton', buttons[2])
    if len(investment_choice.clicked_name):
        yearly_loop.addData('investment_choice.clicked_name', investment_choice.clicked_name[0])
    # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    quant_loop = data.TrialHandler(nReps=present_quantity, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='quant_loop')
    thisExp.addLoop(quant_loop)  # add the loop to the experiment
    thisQuant_loop = quant_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisQuant_loop.rgb)
    if thisQuant_loop != None:
        for paramName in thisQuant_loop:
            exec('{} = thisQuant_loop[paramName]'.format(paramName))
    
    for thisQuant_loop in quant_loop:
        currentLoop = quant_loop
        # abbreviate parameter names if possible (e.g. rgb = thisQuant_loop.rgb)
        if thisQuant_loop != None:
            for paramName in thisQuant_loop:
                exec('{} = thisQuant_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "invest_blank"-------
        continueRoutine = True
        routineTimer.add(0.600000)
        # update component parameters for each repeat
        year_readout_6.setText(year)
        savings_readout_3.setText(CRNT_savings)
        investment_readout_3.setText(CRNT_investment)
        # keep track of which components have finished
        invest_blankComponents = [blank_image, year_readout_6, savings_readout_3, investment_readout_3]
        for thisComponent in invest_blankComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        invest_blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "invest_blank"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = invest_blankClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=invest_blankClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank_image* updates
            if blank_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank_image.frameNStart = frameN  # exact frame index
                blank_image.tStart = t  # local t and not account for scr refresh
                blank_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank_image, 'tStartRefresh')  # time at next scr refresh
                blank_image.setAutoDraw(True)
            if blank_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank_image.tStartRefresh + 0.6-frameTolerance:
                    # keep track of stop time/frame for later
                    blank_image.tStop = t  # not accounting for scr refresh
                    blank_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank_image, 'tStopRefresh')  # time at next scr refresh
                    blank_image.setAutoDraw(False)
            
            # *year_readout_6* updates
            if year_readout_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                year_readout_6.frameNStart = frameN  # exact frame index
                year_readout_6.tStart = t  # local t and not account for scr refresh
                year_readout_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(year_readout_6, 'tStartRefresh')  # time at next scr refresh
                year_readout_6.setAutoDraw(True)
            if year_readout_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > year_readout_6.tStartRefresh + .6-frameTolerance:
                    # keep track of stop time/frame for later
                    year_readout_6.tStop = t  # not accounting for scr refresh
                    year_readout_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(year_readout_6, 'tStopRefresh')  # time at next scr refresh
                    year_readout_6.setAutoDraw(False)
            
            # *savings_readout_3* updates
            if savings_readout_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                savings_readout_3.frameNStart = frameN  # exact frame index
                savings_readout_3.tStart = t  # local t and not account for scr refresh
                savings_readout_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(savings_readout_3, 'tStartRefresh')  # time at next scr refresh
                savings_readout_3.setAutoDraw(True)
            if savings_readout_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > savings_readout_3.tStartRefresh + .6-frameTolerance:
                    # keep track of stop time/frame for later
                    savings_readout_3.tStop = t  # not accounting for scr refresh
                    savings_readout_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(savings_readout_3, 'tStopRefresh')  # time at next scr refresh
                    savings_readout_3.setAutoDraw(False)
            
            # *investment_readout_3* updates
            if investment_readout_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                investment_readout_3.frameNStart = frameN  # exact frame index
                investment_readout_3.tStart = t  # local t and not account for scr refresh
                investment_readout_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(investment_readout_3, 'tStartRefresh')  # time at next scr refresh
                investment_readout_3.setAutoDraw(True)
            if investment_readout_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > investment_readout_3.tStartRefresh + .6-frameTolerance:
                    # keep track of stop time/frame for later
                    investment_readout_3.tStop = t  # not accounting for scr refresh
                    investment_readout_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(investment_readout_3, 'tStopRefresh')  # time at next scr refresh
                    investment_readout_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in invest_blankComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "invest_blank"-------
        for thisComponent in invest_blankComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "Quantity"-------
        continueRoutine = True
        # update component parameters for each repeat
        #more code to deal with the parts where PsychoPy is being stupid and won't accept varibles for the slider ticks
        Quantity_slider = visual.Slider(win=win,
            size=(1.3, 0.05), pos=(0, -0.055), units=None,
            labels=(min, max), ticks=(min, max),
            granularity=5, style=('rating', 'triangleMarker'),
            color='White', font='HelveticaBold',
            flip=False, depth=-8)
        
        
        quantity_background.setImage(qant_back)
        # setup some python lists for storing info about the slider_mouse
        slider_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        year_readout_4.setText(year)
        savings_readout_2.setText(CRNT_savings)
        investment_readout_2.setText(CRNT_investment)
        Quantity_slider.reset()
        Price_readout_2.setText(crnt_price)
        # keep track of which components have finished
        QuantityComponents = [quantity_background, slider_mouse, money_submit_button, slider_value, click_line, year_readout_4, savings_readout_2, investment_readout_2, Quantity_slider, timer_2, late_2, Price_readout_2]
        for thisComponent in QuantityComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        QuantityClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Quantity"-------
        while continueRoutine:
            # get current time
            t = QuantityClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=QuantityClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *quantity_background* updates
            if quantity_background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                quantity_background.frameNStart = frameN  # exact frame index
                quantity_background.tStart = t  # local t and not account for scr refresh
                quantity_background.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(quantity_background, 'tStartRefresh')  # time at next scr refresh
                quantity_background.setAutoDraw(True)
            # *slider_mouse* updates
            if slider_mouse.status == NOT_STARTED and Quantity_slider.rating:
                # keep track of start time/frame for later
                slider_mouse.frameNStart = frameN  # exact frame index
                slider_mouse.tStart = t  # local t and not account for scr refresh
                slider_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_mouse, 'tStartRefresh')  # time at next scr refresh
                slider_mouse.status = STARTED
                slider_mouse.mouseClock.reset()
                prevButtonState = slider_mouse.getPressed()  # if button is down already this ISN'T a new click
            if slider_mouse.status == STARTED:  # only update if started and not finished!
                buttons = slider_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(money_submit_button)
                            clickableList = money_submit_button
                        except:
                            clickableList = [money_submit_button]
                        for obj in clickableList:
                            if obj.contains(slider_mouse):
                                gotValidClick = True
                                slider_mouse.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *money_submit_button* updates
            if money_submit_button.status == NOT_STARTED and Quantity_slider.rating:
                # keep track of start time/frame for later
                money_submit_button.frameNStart = frameN  # exact frame index
                money_submit_button.tStart = t  # local t and not account for scr refresh
                money_submit_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(money_submit_button, 'tStartRefresh')  # time at next scr refresh
                money_submit_button.setAutoDraw(True)
            
            # *slider_value* updates
            if slider_value.status == NOT_STARTED and Quantity_slider.rating:
                # keep track of start time/frame for later
                slider_value.frameNStart = frameN  # exact frame index
                slider_value.tStart = t  # local t and not account for scr refresh
                slider_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_value, 'tStartRefresh')  # time at next scr refresh
                slider_value.setAutoDraw(True)
            if slider_value.status == STARTED:  # only update if drawing
                slider_value.setText(Quantity_slider.getRating(), log=False)
            
            # *click_line* updates
            if click_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                click_line.frameNStart = frameN  # exact frame index
                click_line.tStart = t  # local t and not account for scr refresh
                click_line.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(click_line, 'tStartRefresh')  # time at next scr refresh
                click_line.setAutoDraw(True)
            if click_line.status == STARTED:
                if bool(Quantity_slider.rating):
                    # keep track of stop time/frame for later
                    click_line.tStop = t  # not accounting for scr refresh
                    click_line.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(click_line, 'tStopRefresh')  # time at next scr refresh
                    click_line.setAutoDraw(False)
            if click_line.status == STARTED:  # only update if drawing
                click_line.setText('Click and drag on line', log=False)
            
            # *year_readout_4* updates
            if year_readout_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                year_readout_4.frameNStart = frameN  # exact frame index
                year_readout_4.tStart = t  # local t and not account for scr refresh
                year_readout_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(year_readout_4, 'tStartRefresh')  # time at next scr refresh
                year_readout_4.setAutoDraw(True)
            
            # *savings_readout_2* updates
            if savings_readout_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                savings_readout_2.frameNStart = frameN  # exact frame index
                savings_readout_2.tStart = t  # local t and not account for scr refresh
                savings_readout_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(savings_readout_2, 'tStartRefresh')  # time at next scr refresh
                savings_readout_2.setAutoDraw(True)
            
            # *investment_readout_2* updates
            if investment_readout_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                investment_readout_2.frameNStart = frameN  # exact frame index
                investment_readout_2.tStart = t  # local t and not account for scr refresh
                investment_readout_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(investment_readout_2, 'tStartRefresh')  # time at next scr refresh
                investment_readout_2.setAutoDraw(True)
            
            # *Quantity_slider* updates
            if Quantity_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Quantity_slider.frameNStart = frameN  # exact frame index
                Quantity_slider.tStart = t  # local t and not account for scr refresh
                Quantity_slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Quantity_slider, 'tStartRefresh')  # time at next scr refresh
                Quantity_slider.setAutoDraw(True)
            
            # *timer_2* updates
            if timer_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timer_2.frameNStart = frameN  # exact frame index
                timer_2.tStart = t  # local t and not account for scr refresh
                timer_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timer_2, 'tStartRefresh')  # time at next scr refresh
                timer_2.setAutoDraw(True)
            if timer_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > timer_2.tStartRefresh + 20-frameTolerance:
                    # keep track of stop time/frame for later
                    timer_2.tStop = t  # not accounting for scr refresh
                    timer_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(timer_2, 'tStopRefresh')  # time at next scr refresh
                    timer_2.setAutoDraw(False)
            if timer_2.status == STARTED:  # only update if drawing
                timer_2.setText(int(20+(routineTimer.getTime())), log=False)
            
            # *late_2* updates
            if late_2.status == NOT_STARTED and tThisFlip >= 20.0-frameTolerance:
                # keep track of start time/frame for later
                late_2.frameNStart = frameN  # exact frame index
                late_2.tStart = t  # local t and not account for scr refresh
                late_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(late_2, 'tStartRefresh')  # time at next scr refresh
                late_2.setAutoDraw(True)
            
            # *Price_readout_2* updates
            if Price_readout_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Price_readout_2.frameNStart = frameN  # exact frame index
                Price_readout_2.tStart = t  # local t and not account for scr refresh
                Price_readout_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Price_readout_2, 'tStartRefresh')  # time at next scr refresh
                Price_readout_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in QuantityComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Quantity"-------
        for thisComponent in QuantityComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if investment_choice.clicked_name[0] == 'buy':
            CRNT_investment = CRNT_investment + Quantity_slider.getRating()
            CRNT_savings = CRNT_savings - Quantity_slider.getRating()
        elif investment_choice.clicked_name[0] == 'sell':
            CRNT_investment = CRNT_investment - Quantity_slider.getRating()
            CRNT_savings = CRNT_savings + Quantity_slider.getRating()
            
        thisExp.addData('post_choice_savings', CRNT_savings)
        thisExp.addData('post_choice_investment', CRNT_investment)
        thisExp.addData('money_moved_at_choice', Quantity_slider.getRating())
        
        
        
        # store data for quant_loop (TrialHandler)
        x, y = slider_mouse.getPos()
        buttons = slider_mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(money_submit_button)
                clickableList = money_submit_button
            except:
                clickableList = [money_submit_button]
            for obj in clickableList:
                if obj.contains(slider_mouse):
                    gotValidClick = True
                    slider_mouse.clicked_name.append(obj.name)
        quant_loop.addData('slider_mouse.x', x)
        quant_loop.addData('slider_mouse.y', y)
        quant_loop.addData('slider_mouse.leftButton', buttons[0])
        quant_loop.addData('slider_mouse.midButton', buttons[1])
        quant_loop.addData('slider_mouse.rightButton', buttons[2])
        if len(slider_mouse.clicked_name):
            quant_loop.addData('slider_mouse.clicked_name', slider_mouse.clicked_name[0])
        quant_loop.addData('Quantity_slider.response', Quantity_slider.getRating())
        quant_loop.addData('Quantity_slider.rt', Quantity_slider.getRT())
        # the Routine "Quantity" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed present_quantity repeats of 'quant_loop'
    
    
    # ------Prepare to start Routine "invest_blank"-------
    continueRoutine = True
    routineTimer.add(0.600000)
    # update component parameters for each repeat
    year_readout_6.setText(year)
    savings_readout_3.setText(CRNT_savings)
    investment_readout_3.setText(CRNT_investment)
    # keep track of which components have finished
    invest_blankComponents = [blank_image, year_readout_6, savings_readout_3, investment_readout_3]
    for thisComponent in invest_blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    invest_blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "invest_blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = invest_blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=invest_blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_image* updates
        if blank_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_image.frameNStart = frameN  # exact frame index
            blank_image.tStart = t  # local t and not account for scr refresh
            blank_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_image, 'tStartRefresh')  # time at next scr refresh
            blank_image.setAutoDraw(True)
        if blank_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_image.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                blank_image.tStop = t  # not accounting for scr refresh
                blank_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_image, 'tStopRefresh')  # time at next scr refresh
                blank_image.setAutoDraw(False)
        
        # *year_readout_6* updates
        if year_readout_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            year_readout_6.frameNStart = frameN  # exact frame index
            year_readout_6.tStart = t  # local t and not account for scr refresh
            year_readout_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(year_readout_6, 'tStartRefresh')  # time at next scr refresh
            year_readout_6.setAutoDraw(True)
        if year_readout_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > year_readout_6.tStartRefresh + .6-frameTolerance:
                # keep track of stop time/frame for later
                year_readout_6.tStop = t  # not accounting for scr refresh
                year_readout_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(year_readout_6, 'tStopRefresh')  # time at next scr refresh
                year_readout_6.setAutoDraw(False)
        
        # *savings_readout_3* updates
        if savings_readout_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            savings_readout_3.frameNStart = frameN  # exact frame index
            savings_readout_3.tStart = t  # local t and not account for scr refresh
            savings_readout_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(savings_readout_3, 'tStartRefresh')  # time at next scr refresh
            savings_readout_3.setAutoDraw(True)
        if savings_readout_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > savings_readout_3.tStartRefresh + .6-frameTolerance:
                # keep track of stop time/frame for later
                savings_readout_3.tStop = t  # not accounting for scr refresh
                savings_readout_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(savings_readout_3, 'tStopRefresh')  # time at next scr refresh
                savings_readout_3.setAutoDraw(False)
        
        # *investment_readout_3* updates
        if investment_readout_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            investment_readout_3.frameNStart = frameN  # exact frame index
            investment_readout_3.tStart = t  # local t and not account for scr refresh
            investment_readout_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(investment_readout_3, 'tStartRefresh')  # time at next scr refresh
            investment_readout_3.setAutoDraw(True)
        if investment_readout_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > investment_readout_3.tStartRefresh + .6-frameTolerance:
                # keep track of stop time/frame for later
                investment_readout_3.tStop = t  # not accounting for scr refresh
                investment_readout_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(investment_readout_3, 'tStopRefresh')  # time at next scr refresh
                investment_readout_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in invest_blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "invest_blank"-------
    for thisComponent in invest_blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    news_loop = data.TrialHandler(nReps=show_news, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='news_loop')
    thisExp.addLoop(news_loop)  # add the loop to the experiment
    thisNews_loop = news_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNews_loop.rgb)
    if thisNews_loop != None:
        for paramName in thisNews_loop:
            exec('{} = thisNews_loop[paramName]'.format(paramName))
    
    for thisNews_loop in news_loop:
        currentLoop = news_loop
        # abbreviate parameter names if possible (e.g. rgb = thisNews_loop.rgb)
        if thisNews_loop != None:
            for paramName in thisNews_loop:
                exec('{} = thisNews_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "News"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        #extra code needed here to work with the sizes because PsychoPy is kinda dumb
        A = News1_sizeA
        B = News1_sizeB
        C = Tweet_1_sizeA
        D = Tweet_1_sizeB
        E = Tweet_2_sizeA
        F = Tweet_2_sizeB
        
        
        
        
        main_news_image.setPos((0, 0))
        main_news_image.setSize((A,B))
        main_news_image.setImage(select_news)
        secondary_news_image.setImage(extra_news)
        tweet_1.setSize((C, D))
        tweet_1.setImage(Tweet_1_select)
        tweet_2.setSize((E,F))
        tweet_2.setImage(Tweet_2_select)
        Accept_news.keys = []
        Accept_news.rt = []
        _Accept_news_allKeys = []
        year_readout_2.setText(year)
        # keep track of which components have finished
        NewsComponents = [news_background_image, main_news_image, secondary_news_image, tweet_1, tweet_2, Accept_news, year_readout_2]
        for thisComponent in NewsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        NewsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "News"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = NewsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=NewsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *news_background_image* updates
            if news_background_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                news_background_image.frameNStart = frameN  # exact frame index
                news_background_image.tStart = t  # local t and not account for scr refresh
                news_background_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(news_background_image, 'tStartRefresh')  # time at next scr refresh
                news_background_image.setAutoDraw(True)
            if news_background_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > news_background_image.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    news_background_image.tStop = t  # not accounting for scr refresh
                    news_background_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(news_background_image, 'tStopRefresh')  # time at next scr refresh
                    news_background_image.setAutoDraw(False)
            
            # *main_news_image* updates
            if main_news_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                main_news_image.frameNStart = frameN  # exact frame index
                main_news_image.tStart = t  # local t and not account for scr refresh
                main_news_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(main_news_image, 'tStartRefresh')  # time at next scr refresh
                main_news_image.setAutoDraw(True)
            if main_news_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > main_news_image.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    main_news_image.tStop = t  # not accounting for scr refresh
                    main_news_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(main_news_image, 'tStopRefresh')  # time at next scr refresh
                    main_news_image.setAutoDraw(False)
            
            # *secondary_news_image* updates
            if secondary_news_image.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
                # keep track of start time/frame for later
                secondary_news_image.frameNStart = frameN  # exact frame index
                secondary_news_image.tStart = t  # local t and not account for scr refresh
                secondary_news_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(secondary_news_image, 'tStartRefresh')  # time at next scr refresh
                secondary_news_image.setAutoDraw(True)
            if secondary_news_image.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 10-frameTolerance:
                    # keep track of stop time/frame for later
                    secondary_news_image.tStop = t  # not accounting for scr refresh
                    secondary_news_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(secondary_news_image, 'tStopRefresh')  # time at next scr refresh
                    secondary_news_image.setAutoDraw(False)
            
            # *tweet_1* updates
            if tweet_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                tweet_1.frameNStart = frameN  # exact frame index
                tweet_1.tStart = t  # local t and not account for scr refresh
                tweet_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tweet_1, 'tStartRefresh')  # time at next scr refresh
                tweet_1.setAutoDraw(True)
            if tweet_1.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 10-frameTolerance:
                    # keep track of stop time/frame for later
                    tweet_1.tStop = t  # not accounting for scr refresh
                    tweet_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tweet_1, 'tStopRefresh')  # time at next scr refresh
                    tweet_1.setAutoDraw(False)
            
            # *tweet_2* updates
            if tweet_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                tweet_2.frameNStart = frameN  # exact frame index
                tweet_2.tStart = t  # local t and not account for scr refresh
                tweet_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tweet_2, 'tStartRefresh')  # time at next scr refresh
                tweet_2.setAutoDraw(True)
            if tweet_2.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 10-frameTolerance:
                    # keep track of stop time/frame for later
                    tweet_2.tStop = t  # not accounting for scr refresh
                    tweet_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tweet_2, 'tStopRefresh')  # time at next scr refresh
                    tweet_2.setAutoDraw(False)
            
            # *Accept_news* updates
            waitOnFlip = False
            if Accept_news.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Accept_news.frameNStart = frameN  # exact frame index
                Accept_news.tStart = t  # local t and not account for scr refresh
                Accept_news.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Accept_news, 'tStartRefresh')  # time at next scr refresh
                Accept_news.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Accept_news.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Accept_news.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Accept_news.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 10-frameTolerance:
                    # keep track of stop time/frame for later
                    Accept_news.tStop = t  # not accounting for scr refresh
                    Accept_news.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Accept_news, 'tStopRefresh')  # time at next scr refresh
                    Accept_news.status = FINISHED
            if Accept_news.status == STARTED and not waitOnFlip:
                theseKeys = Accept_news.getKeys(keyList=['space'], waitRelease=False)
                _Accept_news_allKeys.extend(theseKeys)
                if len(_Accept_news_allKeys):
                    Accept_news.keys = _Accept_news_allKeys[-1].name  # just the last key pressed
                    Accept_news.rt = _Accept_news_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *year_readout_2* updates
            if year_readout_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                year_readout_2.frameNStart = frameN  # exact frame index
                year_readout_2.tStart = t  # local t and not account for scr refresh
                year_readout_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(year_readout_2, 'tStartRefresh')  # time at next scr refresh
                year_readout_2.setAutoDraw(True)
            if year_readout_2.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 10-frameTolerance:
                    # keep track of stop time/frame for later
                    year_readout_2.tStop = t  # not accounting for scr refresh
                    year_readout_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(year_readout_2, 'tStopRefresh')  # time at next scr refresh
                    year_readout_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NewsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "News"-------
        for thisComponent in NewsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    # completed show_news repeats of 'news_loop'
    
    
    # ------Prepare to start Routine "End_Results"-------
    continueRoutine = True
    # update component parameters for each repeat
    CRNT_savings = int(CRNT_savings + (CRNT_savings*0.05))
    CRNT_investment = int(CRNT_investment + (CRNT_investment*stock_return))
    
    
    
    savings_results_text = str("Gained "+ str(int((CRNT_savings*0.005))))
    if stock_return > 0:
        investment_results_text = str("Gained " + str(int((CRNT_investment*stock_return))))
        investment_results_color = "Darkgreen"
    elif stock_return < 0:
        investment_results_text = str("Lost " + str(int((CRNT_investment*stock_return))))
        investment_results_color = "Red"
    
    if CRNT_investment == 0:
        assets_avaliable = 0
    else:
        assets_avaliable = 10000
    results_image.setImage(results_chart)
    # setup some python lists for storing info about the new_year_mouse
    new_year_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    year_readout_5.setText(year)
    savings_readout_4.setText(CRNT_savings)
    investment_readout_4.setText(CRNT_investment)
    savings_results.setText(savings_results_text)
    Investment_results.setColor(investment_results_color, colorSpace='rgb')
    Investment_results.setText(investment_results_text)
    # keep track of which components have finished
    End_ResultsComponents = [end_results_background, results_image, new_year_button, new_year_mouse, year_readout_5, savings_readout_4, investment_readout_4, savings_results, Investment_results]
    for thisComponent in End_ResultsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_ResultsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_Results"-------
    while continueRoutine:
        # get current time
        t = End_ResultsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_ResultsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_results_background* updates
        if end_results_background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_results_background.frameNStart = frameN  # exact frame index
            end_results_background.tStart = t  # local t and not account for scr refresh
            end_results_background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_results_background, 'tStartRefresh')  # time at next scr refresh
            end_results_background.setAutoDraw(True)
        
        # *results_image* updates
        if results_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            results_image.frameNStart = frameN  # exact frame index
            results_image.tStart = t  # local t and not account for scr refresh
            results_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(results_image, 'tStartRefresh')  # time at next scr refresh
            results_image.setAutoDraw(True)
        
        # *new_year_button* updates
        if new_year_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_year_button.frameNStart = frameN  # exact frame index
            new_year_button.tStart = t  # local t and not account for scr refresh
            new_year_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_year_button, 'tStartRefresh')  # time at next scr refresh
            new_year_button.setAutoDraw(True)
        # *new_year_mouse* updates
        if new_year_mouse.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            new_year_mouse.frameNStart = frameN  # exact frame index
            new_year_mouse.tStart = t  # local t and not account for scr refresh
            new_year_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_year_mouse, 'tStartRefresh')  # time at next scr refresh
            new_year_mouse.status = STARTED
            new_year_mouse.mouseClock.reset()
            prevButtonState = new_year_mouse.getPressed()  # if button is down already this ISN'T a new click
        if new_year_mouse.status == STARTED:  # only update if started and not finished!
            buttons = new_year_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(new_year_button)
                        clickableList = new_year_button
                    except:
                        clickableList = [new_year_button]
                    for obj in clickableList:
                        if obj.contains(new_year_mouse):
                            gotValidClick = True
                            new_year_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *year_readout_5* updates
        if year_readout_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            year_readout_5.frameNStart = frameN  # exact frame index
            year_readout_5.tStart = t  # local t and not account for scr refresh
            year_readout_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(year_readout_5, 'tStartRefresh')  # time at next scr refresh
            year_readout_5.setAutoDraw(True)
        
        # *savings_readout_4* updates
        if savings_readout_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            savings_readout_4.frameNStart = frameN  # exact frame index
            savings_readout_4.tStart = t  # local t and not account for scr refresh
            savings_readout_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(savings_readout_4, 'tStartRefresh')  # time at next scr refresh
            savings_readout_4.setAutoDraw(True)
        
        # *investment_readout_4* updates
        if investment_readout_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            investment_readout_4.frameNStart = frameN  # exact frame index
            investment_readout_4.tStart = t  # local t and not account for scr refresh
            investment_readout_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(investment_readout_4, 'tStartRefresh')  # time at next scr refresh
            investment_readout_4.setAutoDraw(True)
        
        # *savings_results* updates
        if savings_results.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            savings_results.frameNStart = frameN  # exact frame index
            savings_results.tStart = t  # local t and not account for scr refresh
            savings_results.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(savings_results, 'tStartRefresh')  # time at next scr refresh
            savings_results.setAutoDraw(True)
        
        # *Investment_results* updates
        if Investment_results.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Investment_results.frameNStart = frameN  # exact frame index
            Investment_results.tStart = t  # local t and not account for scr refresh
            Investment_results.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Investment_results, 'tStartRefresh')  # time at next scr refresh
            Investment_results.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_ResultsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_Results"-------
    for thisComponent in End_ResultsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for yearly_loop (TrialHandler)
    # the Routine "End_Results" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'yearly_loop'


# ------Prepare to start Routine "final_results"-------
continueRoutine = True
# update component parameters for each repeat
final_score = "$"+str(int(CRNT_savings + CRNT_investment))
phase="main"

thisExp.addData('final_score', final_score)
final_results_key_resp.keys = []
final_results_key_resp.rt = []
_final_results_key_resp_allKeys = []
final_money_readout.setText(final_score)
# keep track of which components have finished
final_resultsComponents = [Results_image_maker, final_results_key_resp, final_money_readout]
for thisComponent in final_resultsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
final_resultsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "final_results"-------
while continueRoutine:
    # get current time
    t = final_resultsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=final_resultsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Results_image_maker* updates
    if Results_image_maker.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Results_image_maker.frameNStart = frameN  # exact frame index
        Results_image_maker.tStart = t  # local t and not account for scr refresh
        Results_image_maker.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Results_image_maker, 'tStartRefresh')  # time at next scr refresh
        Results_image_maker.setAutoDraw(True)
    
    # *final_results_key_resp* updates
    waitOnFlip = False
    if final_results_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        final_results_key_resp.frameNStart = frameN  # exact frame index
        final_results_key_resp.tStart = t  # local t and not account for scr refresh
        final_results_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(final_results_key_resp, 'tStartRefresh')  # time at next scr refresh
        final_results_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(final_results_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(final_results_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if final_results_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = final_results_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _final_results_key_resp_allKeys.extend(theseKeys)
        if len(_final_results_key_resp_allKeys):
            final_results_key_resp.keys = _final_results_key_resp_allKeys[-1].name  # just the last key pressed
            final_results_key_resp.rt = _final_results_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *final_money_readout* updates
    if final_money_readout.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        final_money_readout.frameNStart = frameN  # exact frame index
        final_money_readout.tStart = t  # local t and not account for scr refresh
        final_money_readout.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(final_money_readout, 'tStartRefresh')  # time at next scr refresh
        final_money_readout.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_resultsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final_results"-------
for thisComponent in final_resultsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "final_results" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blank"-------
continueRoutine = True
routineTimer.add(0.020000)
# update component parameters for each repeat
# keep track of which components have finished
blankComponents = [blank_text]
for thisComponent in blankComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blankClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *blank_text* updates
    if blank_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        blank_text.frameNStart = frameN  # exact frame index
        blank_text.tStart = t  # local t and not account for scr refresh
        blank_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_text, 'tStartRefresh')  # time at next scr refresh
        blank_text.setAutoDraw(True)
    if blank_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blank_text.tStartRefresh + .02-frameTolerance:
            # keep track of stop time/frame for later
            blank_text.tStop = t  # not accounting for scr refresh
            blank_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank_text, 'tStopRefresh')  # time at next scr refresh
            blank_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Questions"-------
continueRoutine = True
# update component parameters for each repeat
Strategy.reset()
Emotion_response.reset()
sell_pressure_response.reset()
# setup some python lists for storing info about the slider_mouse_2
slider_mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
QuestionsComponents = [strategy_question, Strategy, negative_emotion, Emotion_response, sell_pressure_text, sell_pressure_response, qual_submit_button, slider_mouse_2]
for thisComponent in QuestionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
QuestionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Questions"-------
while continueRoutine:
    # get current time
    t = QuestionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=QuestionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *strategy_question* updates
    if strategy_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        strategy_question.frameNStart = frameN  # exact frame index
        strategy_question.tStart = t  # local t and not account for scr refresh
        strategy_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(strategy_question, 'tStartRefresh')  # time at next scr refresh
        strategy_question.setAutoDraw(True)
    
    # *Strategy* updates
    if Strategy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Strategy.frameNStart = frameN  # exact frame index
        Strategy.tStart = t  # local t and not account for scr refresh
        Strategy.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Strategy, 'tStartRefresh')  # time at next scr refresh
        Strategy.setAutoDraw(True)
    
    # *negative_emotion* updates
    if negative_emotion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        negative_emotion.frameNStart = frameN  # exact frame index
        negative_emotion.tStart = t  # local t and not account for scr refresh
        negative_emotion.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(negative_emotion, 'tStartRefresh')  # time at next scr refresh
        negative_emotion.setAutoDraw(True)
    
    # *Emotion_response* updates
    if Emotion_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Emotion_response.frameNStart = frameN  # exact frame index
        Emotion_response.tStart = t  # local t and not account for scr refresh
        Emotion_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Emotion_response, 'tStartRefresh')  # time at next scr refresh
        Emotion_response.setAutoDraw(True)
    
    # *sell_pressure_text* updates
    if sell_pressure_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sell_pressure_text.frameNStart = frameN  # exact frame index
        sell_pressure_text.tStart = t  # local t and not account for scr refresh
        sell_pressure_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sell_pressure_text, 'tStartRefresh')  # time at next scr refresh
        sell_pressure_text.setAutoDraw(True)
    
    # *sell_pressure_response* updates
    if sell_pressure_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sell_pressure_response.frameNStart = frameN  # exact frame index
        sell_pressure_response.tStart = t  # local t and not account for scr refresh
        sell_pressure_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sell_pressure_response, 'tStartRefresh')  # time at next scr refresh
        sell_pressure_response.setAutoDraw(True)
    
    # *qual_submit_button* updates
    if qual_submit_button.status == NOT_STARTED and sell_pressure_response.rating:
        # keep track of start time/frame for later
        qual_submit_button.frameNStart = frameN  # exact frame index
        qual_submit_button.tStart = t  # local t and not account for scr refresh
        qual_submit_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(qual_submit_button, 'tStartRefresh')  # time at next scr refresh
        qual_submit_button.setAutoDraw(True)
    # *slider_mouse_2* updates
    if slider_mouse_2.status == NOT_STARTED and sell_pressure_response.rating:
        # keep track of start time/frame for later
        slider_mouse_2.frameNStart = frameN  # exact frame index
        slider_mouse_2.tStart = t  # local t and not account for scr refresh
        slider_mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_mouse_2, 'tStartRefresh')  # time at next scr refresh
        slider_mouse_2.status = STARTED
        slider_mouse_2.mouseClock.reset()
        prevButtonState = slider_mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if slider_mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = slider_mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(qual_submit_button)
                    clickableList = qual_submit_button
                except:
                    clickableList = [qual_submit_button]
                for obj in clickableList:
                    if obj.contains(slider_mouse_2):
                        gotValidClick = True
                        slider_mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in QuestionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Questions"-------
for thisComponent in QuestionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Strategy.response', Strategy.getRating())
thisExp.addData('Emotion_response.response', Emotion_response.getRating())
thisExp.addData('sell_pressure_response.response', sell_pressure_response.getRating())
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "Questions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(8.000000)
# update component parameters for each repeat
end_resp.keys = []
end_resp.rt = []
_end_resp_allKeys = []
# keep track of which components have finished
endComponents = [End_text, end_resp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *End_text* updates
    if End_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End_text.frameNStart = frameN  # exact frame index
        End_text.tStart = t  # local t and not account for scr refresh
        End_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_text, 'tStartRefresh')  # time at next scr refresh
        End_text.setAutoDraw(True)
    if End_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > End_text.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            End_text.tStop = t  # not accounting for scr refresh
            End_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(End_text, 'tStopRefresh')  # time at next scr refresh
            End_text.setAutoDraw(False)
    
    # *end_resp* updates
    waitOnFlip = False
    if end_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.tStart = t  # local t and not account for scr refresh
        end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_resp, 'tStartRefresh')  # time at next scr refresh
        end_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_resp.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            end_resp.tStop = t  # not accounting for scr refresh
            end_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_resp, 'tStopRefresh')  # time at next scr refresh
            end_resp.status = FINISHED
    if end_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_resp.getKeys(keyList=['space'], waitRelease=False)
        _end_resp_allKeys.extend(theseKeys)
        if len(_end_resp_allKeys):
            end_resp.keys = _end_resp_allKeys[-1].name  # just the last key pressed
            end_resp.rt = _end_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
