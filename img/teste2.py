import pygame as pg
from pgu import gui
from pygame.locals import *

main = gui.Container()
title = gui.Label('JOJO')
ok = gui.Dialog(title, main)
ok.open()
c = gui.Table(width=800, height=500)
c.tr()
c.td(ok)

app = gui.Desktop()
app.connect(gui.QUIT, app.quit, None)

app.run(ok)
