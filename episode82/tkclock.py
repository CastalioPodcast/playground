"""
Creates a simple clock using Tkinter
makes use of recursive scheduled calls to perform the tictac()

# You must have python3-tk or python3-tkinter 
# installed in your system in Python <=3.4

"""

try:
    # python 3 :)
    import tkinter
except ImportError:
    # python 2.x :(
    import Tkinter as tkinter

from time import strftime

relogio = tkinter.Label()

relogio.pack()
relogio['font'] = "Helvetica 120 bold"
relogio['text'] = strftime("%H:%M:%S")


def tictac():
    agora = strftime("%H:%M:%S")
    if agora != relogio['text']:
        relogio['text'] = agora
    relogio.after(100, tictac)


tictac()
relogio.mainloop()

"""
TODO:

Include a timezone/country dropdown which when selected 
a different country increase or decrease the current clock time.
e.g: if selected "New York:  should decrease BRST time in 3 hours
Better if that data can be fetched via some timezone aware API :)
"""
