# -*- coding: utf-8 -*-

import csv
import os
import pandas

# Primeiro é necessário abrir o arquivo de posts
#   Abrir um post
#   Escreve o cabeçalho e o post no html
# Segundo - Pegar o ID do post que foi escrito
#   Procurar por comentarios
#   Escrever os comentarios


# Função para escrever os comentários filhos
def child_comment(comment_text, likes, post_id):
    # comment_text = comment_text.replace('$', '\$')
    comment_text = comment_text.replace('\\n', '<br/>')
    # comment_text = comment_text
    # comment_text = comment_text.replace('%', '\%')
    # comment_text = comment_text.replace('#', '\#')
    # comment_text = comment_text.replace('&', '\&')
    # os.chdir(original_path)
    with open(post_id + '.html', 'a') as post_file:
        post_file.write('<div class="container_child_comment"> \n'
                        '<div class="upvote_lateral_child" alt="Likes" > ')
        post_file.write(str(likes))
        post_file.write('</div> \n')
        post_file.write('<img class="seta_upvote_lateral_child" src="../arrow_up.png" alt="arrow_up"> \n')
        post_file.write('<div class="child_c"> ')
        post_file.write(comment_text)
        post_file.write('</div> \n </div>')


# Função para escrever os comentarios parent
def parent_coment_write(comment_text, likes, post_id):
    # comment_text = comment_text.replace('$', '\$')
    comment_text = comment_text.replace('\\n', '<br/>')
    # comment_text = comment_text.replace('%', '\%')
    # comment_text = comment_text.replace('#', '\#')
    # comment_text = comment_text.replace('&', '\&')
    # os.chdir(original_path)
    with open(post_id + '.html', 'a') as post_file:
        post_file.write('<div class="container_parent_comment"> \n'
                        '<div class="upvote_lateral" alt="Likes" > ')
        post_file.write(str(likes))
        post_file.write('</div> \n')
        post_file.write('<img class="seta_upvote_lateral" src="../arrow_up.png" alt="arrow_up"> \n')
        post_file.write('<div class="parent_c"> ')
        post_file.write(comment_text)
        post_file.write('</div> \n </div>')


# Função para escrever a primeira parte do arquivo html
def post_maker(id, mensagem, like, dia):
    # Abrir o arquivo em branco para escrever a primeira parte
    with open(id + '.html', 'w') as html_header:
        html_header.write('<DOCTYPE html> \n <head> \n <title>Backup Preparty - Relatos</title> \n'
                    '<link rel="stylesheet" href="../application.css"> \n </head> \n <body> \n <main> \n'
                    '<div class="topnav"> \n'
                    '<a href="../index.html">Home</a> \n'
                    '<a href="../posts_duvida_final.html">Dúvidas</a> \n'
                    '<a href="../posts_relatos_final.html">Relatos</a> \n'
                    '<a href="../posts_colab_final.html">Colab.</a> \n '
                    '<a href="../posts_off_final.html">OFF</a> \n '
                    '<a href="../posts_discussao_final.html">Discussão</a> \n '
                    '<a href="../posts_testes_final.html">Testes/Alertas</a> \n '
                    '<a href="../posts_info_final.html">Informação</a> \n '
                    '<a href="../posts_enquetes_final.html">Enquetes</a> \n'
                    '<a href="../posts_outras_final.html">Outras</a> \n'
                          
                   '</object> \n' \
                   '</div> \n' \
                   '<img id="logo_barra" src="../prep_logo_new.png" alt="Logo"> \n')

        html_header.write('<p class="post">')
        html_header.write(mensagem)
        html_header.write('</p> \n')
        html_header.write('<p class="likes_post"> Likes: ')
        html_header.write(str(like))
        html_header.write('</p> \n')
        html_header.write('<p class="data_post"> ')
        html_header.write(dia)
        html_header.write('</p> \n')

        html_header.write('<hr> \n')
        html_header.write('<h4 class="comment"> Comentários </h4> \n')
        html_header.write('<hr> \n')


# Abrindo arquivo de posts
with open('RELATOS_cronologico.csv', "rb") as csv_posts:
    colnames = ['Numero post', 'postID', 'Mensagem', 'Reacoes', 'Comentarios', 'Dia', 'Horario']
    data = pandas.read_csv(csv_posts, delimiter='¿', skiprows=1, names=colnames)

    lista_post_id = data.postID.tolist()
    lista_post_id_split = [i.split('_')[1] for i in lista_post_id]

    lista_mensagem = data.Mensagem.tolist()
    lista_like = data.Reacoes.tolist()
    lista_dia = data.Dia.tolist()

    # Abrir arquivo de comentários
    with open('lista_comments_sem_repeticoes.csv', "rb") as csv_com:
        colunas = ['Numero', 'id', 'Mensagem', 'Data', 'Likes', 'postId', 'parentCommentId']
        data = pandas.read_csv(csv_com, delimiter='¿', skiprows=1, names=colunas)

        lista_comentarios = data.Mensagem.tolist()
        lista_likes_comentarios = data.Likes.tolist()
        lista_data_comen = data.Data.tolist()
        lista_post_id_comen = data.postId.tolist()
        lista_post_id_comen_split = [i.split('_')[1] for i in lista_post_id_comen]

        lista_parent_comen_id = data.parentCommentId.tolist()
        lista_comentario_id = data.id.tolist()

        for i in range(len(lista_post_id_split)):
            mensagem = lista_mensagem[i]
            mensagem = mensagem.replace('\\n', '<br/>')
            id = lista_post_id_split[i]
            like = lista_like[i]
            dia = lista_dia[i]

            # Entrar na funcão de escrever o cabecalho e post
            post_maker(id, mensagem, like, dia)

            # Escrever comentários

            for j in range(len(lista_comentario_id)):
                post_id_coment = lista_post_id_comen_split[j]
                parent_comment_id = lista_parent_comen_id[j]
                comentario_id = lista_comentario_id[j]

                if post_id_coment == id and parent_comment_id == 0:
                    comment_text = lista_comentarios[j]
                    likes = lista_likes_comentarios[j]
                    # Se for verdade é parent
                    # Entra na funcao de parent
                    parent_coment_write(comment_text, likes, id)

                    # Agora que escreveu o comentário parent deve-se escrever o child
                    for k in range(len(lista_comentario_id)):
                        # comment_id = lista_comentario_id[k]
                        parent_comment_id = lista_parent_comen_id[k]

                        if parent_comment_id == comentario_id and post_id_coment == id:
                            mensagem_child = lista_comentarios[k]
                            likes_child = lista_likes_comentarios[k]
                            # print row[3]
                            child_comment(mensagem_child, likes_child, id)


#
#
# def post():
#     count = 0
#     with open('lista_post_sem_repeticoes_novo.csv', "rb") as csv_posts:
#         colnames = ['Numero post', 'postID', 'Mensagem', 'Reacoes', 'Comentarios', 'Dia', 'Horario']
#         data = pandas.read_csv(csv_posts, delimiter='¿', skiprows=1, names=colnames)
#         # your_list = list(data)
#         # your_list.pop(0)
#         mensagem_l = data.Mensagem.tolist()
#         likes_l = data.Reacoes.tolist()
#         dia_n = data.Dia.tolist()
#         print likes_l
#         # print data_l
#         post_id_l = data.postID.tolist()
#
#         for line in range(len(mensagem_l)):
#             # print line
#             # numero = line[0]
#             mensagem = mensagem_l[line]
#             print mensagem
#             # if '[DUVIDA]' in mensagem:
#             #     print 'buga doida', mensagem
#             #     if not os.path.exists('/media/cleyson/Data/Python Codes/PreParty/Backups/DUVIDAS'):
#             #         os.makedirs('/media/cleyson/Data/Python Codes/PreParty/Backups/DUVIDAS')
#             #         os.chdir('/media/cleyson/Data/Python Codes/PreParty/Backups/DUVIDAS')
#             #     os.chdir('/media/cleyson/Data/Python Codes/PreParty/Backups/DUVIDAS')
#                 # os.mkdir('test')
#                 # a = input('asa')
#                 # autor = line[5]
#             post_id = post_id_l[line]
#             count += 1
#             print count
#             likes = likes_l[line]
#             # print line[3]
#             # print data_l[line], 'data'
#             # dia_n = data_l[line].split('T')[0]
#             dia_j = dia_n[line].split('-')
#             # dia = '1'
#             # print dia_j
#             # print dia_n
#             # print dia_j
#             dia = dia_j[2] + '/' + dia_j[1] + '/' + dia_j[0]
#             print line
#
#             print dia
#             mensagem = mensagem_l[line].replace('\\n', '<br/>')
#             # input('a')
#
#             with open(post_id + ".html", "w") as file:
#                 file.write('<DOCTYPE html> \n <html> <head>' \
#                 '<title>Backup - Preparty - Post</title>' \
#                 '<link rel="stylesheet" href="application.css">' \
#                 '</head> <body> <main> <div class="topnav">' \
#                 '<a class="active" href="#home">Home</a>' \
#                 '<a href="#duvidas">Dúvidas</a>' \
#                 '<a href="#relatos">Relatos</a>' \
#                 '<a href="#colab">Colaboração</a>'
#                 '<a href="#discussao">Discussão</a>'
#                 '<a href="#alertas">Alertas</a>' \
#                 '<a href="#testes">Testes</a>' \
#                 '<a href="#off">OFF</a>' \
#                 '<a href="#outros">Outros</a>' \
#                 '</object>' \
#                 '</div>' \
#                 '<img id="logo_barra" src="prep_logo_new.png" alt="Logo">')
#
#                 file.write('<p class="post">')
#                 file.write(mensagem)
#                 file.write('</p>')
#                 file.write('<p class="likes_post"> Likes: ')
#                 file.write(str(likes))
#                 file.write('</p>')
#                 file.write('<p class="data_post"> ')
#                 file.write(dia)
#                 file.write('</p>')
#
#                 file.write('<hr>')
#                 file.write('<h4 class="comment"> Comentários </h4>')
#                 file.write('<hr>')
#
#     return post_id
#
#
# def parent_coment(comment_text, likes):
#     # comment_text = comment_text.replace('$', '\$')
#     comment_text = comment_text.replace('\\n', '<br/>')
#     # comment_text = comment_text.replace('%', '\%')
#     # comment_text = comment_text.replace('#', '\#')
#     # comment_text = comment_text.replace('&', '\&')
#     # os.chdir(original_path)
#     with open(post_id + '.html', 'a') as post_file:
#         post_file.write('<div class="container_parent_comment"> \n'
#                         '<div class="upvote_lateral" alt="Likes" > ')
#         post_file.write(str(likes))
#         post_file.write('</div> \n')
#         post_file.write('<img class="seta_upvote_lateral" src="arrow_up.png" alt="arrow_up"> \n')
#         post_file.write('<div class="parent_c"> ')
#         post_file.write(comment_text)
#         post_file.write('</div> \n </div>')
#
#
# def child_comment(comment_text, likes):
#     # comment_text = comment_text.replace('$', '\$')
#     comment_text = comment_text.replace('\\n', '<br/>')
#     # comment_text = comment_text
#     # comment_text = comment_text.replace('%', '\%')
#     # comment_text = comment_text.replace('#', '\#')
#     # comment_text = comment_text.replace('&', '\&')
#     # os.chdir(original_path)
#     with open(post_id + '.html', 'a') as post_file:
#         post_file.write('<div class="container_child_comment"> \n'
#                         '<div class="upvote_lateral_child" alt="Likes" > ')
#         post_file.write(str(likes))
#         post_file.write('</div> \n')
#         post_file.write('<img class="seta_upvote_lateral_child" src="arrow_up.png" alt="arrow_up"> \n')
#         post_file.write('<div class="child_c"> ')
#         post_file.write(comment_text)
#         post_file.write('</div> \n </div>')
#
#     # print texto_comentario_filho
#
# original_path = os.getcwd()
# print original_path
# post_id = post()
#
#
# # Abrir arquivo comentarios
# n = 0
# with open('lista_comments_sem_repeticoes.csv', "rb") as csv_com:
#     colnames = ['Numero', 'id', 'Mensagem', 'Data', 'Likes', 'postId', 'parentCommentId']
#     data = pandas.read_csv(csv_com, delimiter='¿', skiprows=1, names=colnames)
#     # your_list = list(data)
#     # your_list.pop(0)
#     mensagem_l = data.Mensagem.tolist()
#     likes_l = data.Likes.tolist()
#     dia_n = data.Data.tolist()
#     postid_l = data.postId.tolist()
#     parent_comment_id_l = data.parentCommentId.tolist()
#     comment_id_l = data.id.tolist()
#
#     for i in range(len(mensagem_l)):
#         # print line
#         # Checar se eh comentario do postId
#         # likes = line[4]
#         if postid_l[i] == post_id and parent_comment_id_l[i] == 0:
#             # Checar se o comentario eh mae
#             parent_comment_id = parent_comment_id_l[i]
#             # print parent_comment_id
#             parent_coment(mensagem_l[i], likes_l[i])
#             # print line[3]
#             comment_id = comment_id_l[i]
#             for j in range(len(mensagem_l)):
#                 # print 'ParentID ', row[7]
#                 n += 1
#                 # print n
#                 # print 'CommentID ', comment_id
#                 if parent_comment_id_l[j] == comment_id and postid_l[j] == post_id:
#                     # print row[3]
#                     child_comment(mensagem_l[j], likes_l[j])
#             # Comentar os filhos
#
# print n