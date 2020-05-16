import pygame as pg
from pygame.locals import *
from pgu import gui


def name():

    #tempo


    # textos booleanos
    text_bool = []
    for i in range(12):
        text_bool.append(False)



    # Título e ícone
    pg.display.set_caption("O Hacker")
    icon = pg.image.load("img/icone/man.png")
    pg.display.set_icon(icon)

    # Background
    bg_desktop = pg.image.load('img/bg/bg1.png')

    bg_lixeira = pg.image.load('img/bg/bg_lixeira.png')
    bg_lixeira_doc1 = pg.image.load('img/bg/bg_lixeira_doc1.png')
    bg_lixeira_doc2 = pg.image.load('img/bg/bg_lixeira_doc2.png')
    bg_lixeira_doc3 = pg.image.load('img/bg/bg_lixeira_doc3.png')

    bg_dados = pg.image.load('img/bg/bg_dados.png')
    bg_dados_ip = pg.image.load('img/bg/bg_dados_ip.png')

    bg_cmd = pg.image.load('img/bg/bg_cmd.png')

    # posicoes dos textos
    pos0 = [100, 75]
    pos1 = [150, 675]


    # click_duplo = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((1200, 800))

    # textos
    simbolos = {".", '"', "/", ":", "@"}
    pre_text = ">>>>:"
    versao_cmd = "Prompt de comando Orange [versão 2.45.102]"
    name = ""
    save_name = []
    font = pg.font.Font(None, 26)

    # Mensagens do Hacker

    hacker = [] # 11
    hacker.append("TI@172.222.62.108: Eae tudo bem? Eu sou o cara novo de TI, comecei semana passada.")
    hacker.append("TI@172.222.62.108: Você estava doente semana passada né?")
    hacker.append("TI@172.222.62.108: Pois é, quem adoeceu essa semana fui eu. hahahahah")
    hacker.append("TI@172.222.62.108: Então, to trabalhando de casa.")
    hacker.append("TI@172.222.62.108: Você deve ta achando estranho eu usar o terminal pra falar com você.")
    hacker.append("TI@172.222.62.108: Isso é coisa comum entre o pessoal de TI, é normal.")
    hacker.append("TI@172.222.62.108: A gente gosta de usar fonte verde e usar o terminal porque lembra Matrix.")
    hacker.append("TI@172.222.62.108: Você já assistiu Matrix? Recomendo!")
    hacker.append("TI@172.222.62.108: Enfim, não era sobre isso que eu queria falar com você.")
    hacker.append("TI@172.222.62.108: Como você não veio semana passada ficou faltando ajustar umas coisas.")
    hacker.append("TI@172.222.62.108: Quando você vir essa mensagem fala qualquer coisa que eu digo o que preciso.")


    bool_chat1 = True
    chat1 = 0 # 10
    hacker.append("TI@172.222.62.108: Então cara, se você for na sua pasta de dados e abrir o primeiro arquivo")
    hacker.append("TI@172.222.62.108: Você vai ver uma lista de IP dos clientes.")
    hacker.append("TI@172.222.62.108: Eu preciso que você me conecte com 'Arnaldo Segurança'.")
    hacker.append("TI@172.222.62.108: Para fazer isso é simples basta digitar o comando 'connect [IP do cliente]'.")
    hacker.append("TI@172.222.62.108: Uma vez conectado eu vou precisar que voce faça o upload de um arquivo.")
    hacker.append("TI@172.222.62.108: É fácil. É só digitar 'upload [caminho/do/arquivo/arquivo.algo]'")
    hacker.append("TI@172.222.62.108: Depois é só digitar 'disconnect' e esperar meu contato.")
    hacker.append("TI@172.222.62.108: O arquivo está na pasta de dados e se chama 'CavaloDeEsparta.bat'.")
    hacker.append("TI@172.222.62.108: Esses cavalos de esparta servem pra fortalecer a defesa do cliente.")
    hacker.append("TI@172.222.62.108: Estarei monitorando, quando você terminar entrarei em contato.")


    chat2 = 0 #8
    hacker.append("TI@172.222.62.108: Muito bem! Com os cavalos de esparta, ninguém vai conseguir hackear a segurança!")
    hacker.append("TI@172.222.62.108: Percebi aqui que os dados do cliente 'Banco Gold' "
                  "também precisam de uma melhorada.")
    hacker.append("TI@172.222.62.108: Vou precisar que você use o comando download para baixar "
                  "os arquivos deste cliente.")
    hacker.append("TI@172.222.62.108: Você vai ter que baixar o arquivo 'confidencial.dat' de "
                  "cada um dos IPs deste cliente.")
    hacker.append("TI@172.222.62.108: Quando você tiver juntado os arquivos, é só me mandar que eu faço o resto.")
    hacker.append("TI@172.222.62.108: Para realizar o download é só fazer igual ao upload.")
    hacker.append("TI@172.222.62.108: Neste caso ao invés de upload é só digitar 'download [nome_do_arquivo]'.")
    hacker.append("TI@172.222.62.108: Vou voltar a fazer coisas de TI, quando você me mandar os "
                  "arquivos eu falo com você.")

    chat3 = 0 #
    hacker.append("TI@172.222.62.108: Serviço concluído com sucesso! os clientes do Banco Gold agradecem!")
    hacker.append("TI@172.222.62.108: Eu sei que eu estou te atrapalhando muito hoje.")
    hacker.append("TI@172.222.62.108: Mas vou precisar de mais um favor.")
    hacker.append("TI@172.222.62.108: Vou precisar que você me passe o arquivo 'apaga_rastro.rofl'.")
    hacker.append("TI@172.222.62.108: É só fazer o upload para o meu IP.")
    hacker.append("TI@172.222.62.108: Depois disso eu quero que você faça o download do arquivo 'Testa_de_Ferro.exe'.")
    hacker.append("TI@172.222.62.108: Quando terminar, dê disconnect e dê um 'execute Dados/Testa_de_Ferro.exe'.")
    hacker.append("TI@172.222.62.108: Depois disso, pode voltar ao trabalho, nos encontramos quando eu melhorar!")





    # Booleans
    desktop = True

    lixeira = False
    doc_lixeira1 = False
    doc_lixeira2 = False
    doc_lixeira3 = False

    cmd = False


    dados = False
    dados_ip = False

    # Booleans jogo

    Inicio = False

    Connect_Geral = False
    Disconnect_Geral = True

    Connect_Arnaldo = False
    Arnaldo_delay = False
    Upload_Arnaldo = False
    Disconnect_Arnaldo = False

    Connect_Banco = False
    Download_Banco = False
    Disconnect_Banco = False

    Connect_Hacker = False
    Download_Hacker = False
    Upload_Hacker = False
    Execute_Hacker = False
    Execute_Safe = False

    # funcao_bool
    def func_bool(b, save_name, screen):
        if save_name[b].find("TI@172.222.62.108:") == -1:
            screen.blit(font.render("user@home:", True, (255, 255, 255)), (100, 125 + (b * 50)))
            screen.blit(font.render(save_name[b], True, (255, 255, 255)), (215, 125 + (b * 50)))
        else:
            screen.blit(font.render(save_name[b], True, (96, 250, 7)), (100, 125 + (b * 50)))

    # funcao scroll
    def scroll():
        for i in range(10):
            save_name[i] = save_name[i + 1]

    for i in range(11):
        save_name.append(hacker[i])

    while True:
        while desktop is True:
            screen.blit(bg_desktop, (0, 0))

            for evt in pg.event.get():


                if evt.type == QUIT:
                    return

                if evt.type == pg.MOUSEBUTTONDOWN:

                    mx, my = pg.mouse.get_pos()
                    print(mx, my)
                    if 100 < mx < 160 and 90 < my < 160:
                        print("abrir lixeira")
                        lixeira = True
                        desktop = False
                    if 100 < mx < 160 and 190 < my < 260:
                        print("abrir pastadados")
                        dados = True
                        desktop = False
                    if 100 < mx < 160 and 290 < my < 360:
                        print("abrir cmd")
                        cmd = True
                        desktop = False


                pg.display.flip()

        while lixeira is True:
            screen.blit(bg_lixeira, (0, 0))
            for evt in pg.event.get():


                if evt.type == QUIT:
                    return

                if evt.type == pg.MOUSEBUTTONDOWN:
                    mx, my = pg.mouse.get_pos()
                    print(mx, my)
                    if 1135 < mx < 1150 and 39 < my < 54:
                        desktop = True
                        lixeira = False
                    if 105 < mx < 155 and 115 < my < 170:
                        doc_lixeira1 = True
                        lixeira = False
                    if 205 < mx < 255 and 115 < my < 170:
                        doc_lixeira2 = True
                        lixeira = False
                    if 305 < mx < 355 and 115 < my < 170:
                        doc_lixeira3 = True
                        lixeira = False
            pg.display.flip()


        while doc_lixeira1 is True:
            screen.blit(bg_lixeira_doc1, (0, 0))
            for evt in pg.event.get():


                if evt.type == QUIT:
                    return

                if evt.type == pg.MOUSEBUTTONDOWN:
                    mx, my = pg.mouse.get_pos()
                    print(mx, my)
                    if 1095 < mx < 1110 and 90 < my < 104:
                        lixeira = True
                        doc_lixeira1 = False
            pg.display.flip()

        while doc_lixeira2 is True:
            screen.blit(bg_lixeira_doc2, (0, 0))
            for evt in pg.event.get():


                if evt.type == QUIT:
                    return

                if evt.type == pg.MOUSEBUTTONDOWN:
                    mx, my = pg.mouse.get_pos()
                    print(mx, my)
                    if 1095 < mx < 1110 and 90 < my < 104:
                        lixeira = True
                        doc_lixeira2 = False
            pg.display.flip()

        while doc_lixeira3 is True:
            screen.blit(bg_lixeira_doc3, (0, 0))
            for evt in pg.event.get():


                if evt.type == QUIT:
                    return

                if evt.type == pg.MOUSEBUTTONDOWN:
                    mx, my = pg.mouse.get_pos()
                    print(mx, my)
                    if 1095 < mx < 1110 and 90 < my < 104:
                        lixeira = True
                        doc_lixeira3 = False
            pg.display.flip()

        while dados is True:
            screen.blit(bg_dados, (0, 0))
            for evt in pg.event.get():


                if evt.type == QUIT:
                    return

                if evt.type == pg.MOUSEBUTTONDOWN:
                    mx, my = pg.mouse.get_pos()
                    print(mx, my)
                    if 1135 < mx < 1150 and 39 < my < 54:
                        desktop = True
                        dados = False
                    if 105 < mx < 155 and 115 < my < 170:
                        dados_ip = True
                        dados = False
                        print(dados_ip)
                    """if 205 < mx < 255 and 115 < my < 170:
                        doc_lixeira2 = True
                        lixeira = False
                    if 305 < mx < 355 and 115 < my < 170:
                        doc_lixeira3 = True
                        lixeira = False"""
            pg.display.flip()

        while dados_ip is True:
            screen.blit(bg_dados_ip, (0, 0))
            for evt in pg.event.get():


                if evt.type == QUIT:
                    return

                if evt.type == pg.MOUSEBUTTONDOWN:
                    mx, my = pg.mouse.get_pos()
                    print(mx, my)
                    if 1095 < mx < 1110 and 90 < my < 104:
                        dados = True
                        dados_ip = False
            pg.display.flip()


        while cmd is True:
            screen.blit(bg_cmd, (0, 0))


            # texto digitado


            text0 = font.render(versao_cmd, True, (255, 255, 255))
            pre_text1 = font.render(pre_text, True, (255, 255, 255))
            text1 = font.render(name, True, (255, 0, 255))


            screen.blit(text0, pos0)
            screen.blit(pre_text1, (pos1[0] - 50, pos1[1]))
            screen.blit(text1, pos1)




            for evt in pg.event.get():


                if evt.type == QUIT:
                    return

                if evt.type == pg.USEREVENT:
                    if bool_chat1 == True:
                        scroll()
                        save_name[10] = hacker[11 + chat1]
                        chat1 += 1

                        if chat1 == 10:
                            pg.time.set_timer(pg.USEREVENT, 0)
                            bool_chat1 = False

                    if Arnaldo_delay == True:
                        scroll()
                        save_name[10] = 'Conexão estabelecida'
                        Arnaldo_delay = False

                    if Upload_Arnaldo == True:
                        scroll()
                        save_name[10] = 'Upload realizado com sucesso!'
                        Upload_Arnaldo = False


                if evt.type == pg.MOUSEBUTTONDOWN:
                    mx, my = pg.mouse.get_pos()
                    print(mx, my)
                    if 1140 < mx < 1155 and 35 < my < 50:
                        desktop = True
                        cmd = False

                    # leitura do teclado


                if evt.type == KEYDOWN:


                    if evt.unicode.isalpha():
                        name += evt.unicode
                    if evt.unicode.isnumeric():
                        name += evt.unicode
                    if evt.key == K_BACKSPACE:
                        name = name[:-1]
                    if evt.unicode in simbolos:
                        name += evt.unicode

                    if evt.key == K_SPACE:
                        name += " "
                    if evt.key == K_RETURN:

                        scroll()
                        save_name[10] = name
                        name = ""

                        if Disconnect_Geral == False:
                            if save_name[10] == 'disconnect':
                                scroll()
                                save_name[10] = 'As conexões foram encerradas!'
                                Disconnect_Geral = True


                        if Inicio is False:
                            pg.time.set_timer(pg.USEREVENT, 400)
                            Inicio = True

                        if Inicio is True:
                            if Disconnect_Geral is True:
                                if save_name[10] == ('connect 235.98.164.90'):
                                    Connect_Arnaldo = True

                                    scroll()
                                    save_name[10] = 'Estabelecendo conexão...'
                                    pg.time.set_timer(pg.USEREVENT, 3000)
                                    Arnaldo_delay = True

                                    Disconnect_Geral = False

                        if Connect_Arnaldo is True:
                            if save_name[10] == ('upload Dados/CavaloDeEsparta.bat'):
                                Upload_Arnaldo = True
                                scroll()
                                save_name[10] = 'Realizando upload de CavaloDeEsparta.bat...'
                                pg.time.set_timer(pg.USEREVENT, 3000)




            for i in range(11):
                func_bool(i, save_name, screen)


            pg.display.flip()



if __name__ == "__main__":
    name()
    pg.quit()

    """ # leitura do teclado
    if evt.type == KEYDOWN:

    if evt.unicode.isalpha():
        name += evt.unicode
    elif evt.key == K_BACKSPACE:
        name = name[:-1]
    elif evt.key == K_SPACE:
        name += " "
    elif evt.key == K_RETURN:
        save_name = name
        name = """""


