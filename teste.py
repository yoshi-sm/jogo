"""<title>Dialogs and Documents</title>
"""
import pygame
from pygame.locals import *

"""# the following line is not needed if pgu is installed
import sys; sys.path.insert(0, "..")"""

from pgu import gui


##Documents layout widgets like words and images in a HTML document.  This
##example also demonstrates the ScrollBox container widget.
##::

class Arquivo_Lixo1(gui.Dialog):
    def __init__(self, **params):
        title = gui.Label("Doc1")

        width = 1000
        height = 600
        doc = gui.Document(width=width)

        space = title.style.font.size(" ")

        for i in range(0, 3):
            doc.block(align=-1)
            for word in """qBdXbMAIP23BLeP8Fzow
g5vCWNu69qDblTZds4DZ
t5qVFN6GI5AMVhFo4rVl
AhEuaxYVx1Tnj2hl6kfv
HjFSDEM9jwalpqP66DXF""".split(" "):
                doc.add(gui.Label(word))
                doc.space(space)
            doc.br(space[1])

        gui.Dialog.__init__(self, title, gui.ScrollArea(doc, 0, height))

class Arquivo_Lixo2(gui.Dialog):
    def __init__(self, **params):
        title = gui.Label("Doc2")

        width = 1000
        height = 600
        doc = gui.Document(width=width)

        space = title.style.font.size(" ")

        for i in range(0, 3):
            doc.block(align=-1)
            for word in """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ligula ligula, accumsan 
            vel ex id, fringilla lacinia sapien. Ut nulla.""".split(" "):
                doc.add(gui.Label(word))
                doc.space(space)
            doc.br(space[1])

        gui.Dialog.__init__(self, title, gui.ScrollArea(doc, 0, height))

class Arquivo_Lixo3(gui.Dialog):
    def __init__(self, **params):
        title = gui.Label("Doc3")

        width = 1000
        height = 600
        doc = gui.Document(width=width)

        space = title.style.font.size(" ")

        for i in range(0, 3):
            doc.block(align=-1)
            for word in """Para de procurar coisa no lixo!!!""".split(" "):
                doc.add(gui.Label(word))
                doc.space(space)
            doc.br(space[1])

        gui.Dialog.__init__(self, title, gui.ScrollArea(doc, 0, height))

class Arquivo_Dados1(gui.Dialog):
    def __init__(self, **params):
        title = gui.Label("Lista de IPs")

        width = 1000
        height = 600
        doc = gui.Document(width=width)

        space = title.style.font.size(" ")


        doc.block(align=-1)
        for word in """Nilda Gás - 162.189.56.241""".split(" "):
            doc.add(gui.Label(word))
            doc.space(space)
        doc.br(space[0])

        doc.block(align=-1)
        for word in """Feijoada do João - 32.37.21.33""".split(" "):
            doc.add(gui.Label(word))
            doc.space(space)
        doc.br(space[0])

        doc.block(align=-1)
        for word in """Banco Gold 1 - 208.188.188.102""".split(" "):
            doc.add(gui.Label(word))
            doc.space(space)
        doc.br(space[0])

        doc.block(align=-1)
        for word in """Drogaria Alfabeto - 0.112.44.55""".split(" "):
            doc.add(gui.Label(word))
            doc.space(space)
        doc.br(space[0])

        doc.block(align=-1)
        for word in """Arnaldo Segurança - 235.98.164.90""".split(" "):
            doc.add(gui.Label(word))
            doc.space(space)
        doc.br(space[0])

        doc.block(align=-1)
        for word in """Banco Gold 3 - 157.76.32.223""".split(" "):
            doc.add(gui.Label(word))
            doc.space(space)
        doc.br(space[0])

        doc.block(align=-1)
        for word in """Camacho Carpintaria - 154.123.89.87""".split(" "):
            doc.add(gui.Label(word))
            doc.space(space)
        doc.br(space[0])

        doc.block(align=-1)
        for word in """Disk Azeite - 84.81.242.40""".split(" "):
            doc.add(gui.Label(word))
            doc.space(space)
        doc.br(space[0])

        doc.block(align=-1)
        for word in """Banco Gold 2 - 144.30.230.64""".split(" "):
            doc.add(gui.Label(word))
            doc.space(space)
        doc.br(space[0])

        doc.block(align=-1)
        for word in """Lanchonete Seu Rango - 61.209.188.254""".split(" "):
            doc.add(gui.Label(word))
            doc.space(space)
        doc.br(space[0])

        gui.Dialog.__init__(self, title, gui.ScrollArea(doc, 0, height))

class Arquivo_Dados2(gui.Dialog):
    def __init__(self, **params):
        title = gui.Label("About Cuzco's Paint")

        width = 1000
        height = 600
        doc = gui.Document(width=width)

        space = title.style.font.size(" ")

        for i in range(0, 3):
            doc.block(align=-1)
            for word in """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce duiblandit eget 
            sodales nec, maximus volutpat lectus. Aliquam a.""".split(" "):
                doc.add(gui.Label(word))
                doc.space(space)
            doc.br(space[1])

        gui.Dialog.__init__(self, title, gui.ScrollArea(doc, 0, height))

class Arquivo_Dados3(gui.Dialog):
    def __init__(self, **params):
        title = gui.Label("About Cuzco's Paint")

        width = 1000
        height = 600
        doc = gui.Document(width=width)

        space = title.style.font.size(" ")

        for i in range(0, 3):
            doc.block(align=-1)

            for word in """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce duiblandit eget 
            sodales nec, maximus volutpat lectus. Aliquam a.""".split(" "):
                doc.add(gui.Label(word, color=(255,0,0)))
                doc.space(space)
            doc.br(space[1])

        gui.Dialog.__init__(self, title, gui.ScrollArea(doc, 0, height))








class Bin_Desk(gui.Dialog):
    def __init__(self, **params):
        title = gui.Label("Lixeira")

        width = 1100
        height = 700

        doc = gui.Container(width=width, height= height)
        img1 = gui.Image("img/desktop/notes.png")
        img1.connect(gui.CLICK, Arquivo_Lixo1().open, None)
        img2 = gui.Image("img/desktop/notes.png")
        img2.connect(gui.CLICK, Arquivo_Lixo2().open, None)
        img3 = gui.Image("img/desktop/notes.png")
        img3.connect(gui.CLICK, Arquivo_Lixo3().open, None)

        doc.add(img1, 50, 50)
        doc.add(img2, 150, 50)
        doc.add(img3, 250, 50)


        gui.Dialog.__init__(self, title, gui.ScrollArea(doc, 0, 0))

class Pasta_Desk(gui.Dialog):
    def __init__(self, **params):
        title = gui.Label("Dados")

        width = 1100
        height = 700




        doc = gui.Container(width=width, height= height)
        img1 = gui.Image("img/desktop/notes.png")
        img1.connect(gui.CLICK, Arquivo_Dados1().open, None)
        doc.add(img1, 50, 50)

        img2 = gui.Image("img/desktop/notes.png")
        img2.connect(gui.CLICK, Arquivo_Dados2().open, None)
        doc.add(img2, 150, 50)

        img3 = gui.Image("img/desktop/notes.png")
        img3.connect(gui.CLICK, Arquivo_Dados3().open, None)
        doc.add(img3, 250, 50)


        gui.Dialog.__init__(self, title, gui.ScrollArea(doc, 0, 0))


class Cmd_Desk(gui.Table):
    def __init__(self, **params):
        title = gui.Label("Log de Mensagens")

        width = 1100
        height = 700


        doc = gui.Input(width=width, height= height, color=(255,255,255), background=(255, 255, 255))

        def cb():
            texto = doc.value
            if texto == 'festa':
                print(texto)
            doc.value = ''

        doc.connect("activate", cb)





        gui.Dialog.__init__(self, title, gui.ScrollArea(doc, 0, 0))

##


if __name__ in '__main__':


    desktop = gui.Container(width=1200, height=800)


    bin_img = gui.Image("img/desktop/bin.png")
    bin_img.connect(gui.CLICK, Bin_Desk().open, None)

    pasta_img = gui.Image("img/desktop/pasta_dados.png")
    pasta_img.connect(gui.CLICK, Pasta_Desk().open, None)

    cmd_img = gui.Image("img/desktop/cmd.png")
    cmd_img.connect(gui.CLICK, Cmd_Desk().open, None)

    log_img = gui.Image("img/desktop/log.png")

    """notes_img = gui.Image("img/desktop/notes.png")
    notes_img.connect(gui.CLICK, Notes_Desk().open, None)"""

    bin = gui.Container(width=1000, height=700)
    ##

    desktop.add(bin_img, 100, 100)
    desktop.add(pasta_img, 100, 200)
    desktop.add(cmd_img, 100, 300)
    desktop.add(log_img, 100, 400)
    app = gui.Desktop()
    app.connect(gui.QUIT, app.quit, None)
    app.run(desktop)

