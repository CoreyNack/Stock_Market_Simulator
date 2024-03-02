# Stock_Market_Simulator
Stock Market Simulator, Designed to elicit and measure panic selling behavior after a market crash. 

Running:
This experiment has been tested the most in PsychoPy version 2021.2.3. Running it in other versions, especially on Mac, may cause difficulties. After installing PsychoPy, find and open the Stock_Market_Simulator.psyexp 
file in the folder. 

The experiment:
Each “year” Out of 12, participants choose to move money from savings to an investment, or vice versa. During most years, the investment produces high returns. However, during two of the years (4 and 9), 
the markets produce a significant negative return. There is only one investment option available, and it more or less represents a total market index fund. 

The output:
The most important columns in the output data file are:
investment_choice.clicked_name  — can be buy, sell, or no_change

pre_choice_savings — indicates the amount of money in the savings account each year right before making the choice between buy, sell, or no_change

pre_choice_investment — indicates the amount of money in the investment account each year right before making the choice between buy, sell, or no_change

post_choice_savings — indicates the amount of money in the savings account each year right after making the choice between buy, sell, or no_change

post_choice_investment — indicates the amount of money in the investment account each year right after making the choice between buy, sell, or no_change

money_moved_at_choice — describes the absolute value of the money moved between savings and investment (or vice versa, depending on investment_choice.clicked_name). 
During crash years, if “sell” was clicked, this tracks the amount of money panic sold

Customization:
The present version incentivizes participants to perform well by offering them the chance to leave early for full SONA credit based on how much money they end with. 
This would then be followed by a different experimental task of variable length, which is not included in this PsychoPy experiment.  
If you wish to remove any mention of this incentive from the experiment, delete Ins1.png from the folder, then locate the InsXXX.png file and rename it to Ins1.png. 
Alternatively, if you wish to include a monetary incentive, you can use a graphics editing program to add desired text to InsXXX.png and then rename it. 

Citation:
A preprint for this project is pending. If you wish to use this program, please cite the preprint when available. 
