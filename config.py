import sqlite3

TOKEN = '1623710533:AAGodxYFRJocHyDr32cg1bOaedve87aCsig'

registrationMSG = "Congratulation! Now you are registered."
registrationErrorMSG = "Oops! You have already register in bot."
startMSG = "Hello! Welcome to EasyUnderstand Bot. " \
           "Do you have some problem with understanding? " \
           "Let's solve this!" \
           "  " \
           "Now you can translate Ukrainian to Romanian. " \
           "If you want to change these parameters use - /change_language"
chooseMSG = "What language do you want to change?"
outputMSG = "Choose output language"
inputMSG = "Choose input language"
mydb = sqlite3.connect("base.sqlite")
