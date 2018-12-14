# -*- coding: utf-8 -*-

import csv
import os
import pandas


with open('posts_discussao_final.html', 'w') as finalhtml:
    finalhtml.write('<DOCTYPE html> \n <head> \n <title>Backup Preparty - OFF </title> \n'
                    '<link rel="stylesheet" href="testes.css"> \n </head> \n <body> \n <main> \n'
                    '<div class="topnav"> \n'
                    '<a href="index.html">Home</a> \n'
                    '<a href="posts_duvida_final.html">Dúvidas</a> \n'
                    '<a href="posts_relatos_final.html">Relatos</a> \n'
                    '<a href="posts_colab_final.html">Colab.</a> \n '
                    '<a href="posts_off_final.html">OFF</a> \n '
                    '<a href="posts_discussao_final.html">Discussão</a> \n '
                    '<a href="posts_testes_final.html">Testes/Alertas</a> \n '
                    '<a href="posts_info_final.html">Informação</a> \n '
                    '<a href="posts_enquetes_final.html">Enquetes</a> \n'
                    '<a href="posts_outras_final.html">Outras</a> \n'
                    
                    '</object> \n </div> \n <img id="logo_barra" src="prep_logo_new.png" alt="Logo"> \n <hr>'
                    '<h4 class="topic_name"> DISCUSSÃO </h4> \n <hr>')

# abrir o arquivo de posts e ler
n = 0
with open('discussao_cronologico.csv', 'rb') as csv_post:
    colnames = ['Numero_post', 'postID', 'Mensagem', 'Reacoes', 'Comentarios', 'Dia', 'Horario']
    data = pandas.read_csv(csv_post, delimiter='¿', names=colnames, skiprows=1, index_col=False)
    # post_list = list(data)
    # post_list.pop(0)
    id_list = data.postID.tolist()
    print id_list
    id_list_split = [i.split('_')[1] for i in id_list]
    message_list = data.Mensagem.tolist()
    dia_list = data.Dia.tolist()
    likes_list = data.Reacoes.tolist()

    lista_done = [''] * len(id_list)

    for i in range(len(id_list)):

        if id_list_split[i] not in lista_done:
            lista_done[i] = id_list_split[i]
            # print row
            mensagem = message_list[i]
            mensagem = mensagem.replace('\\n', '<br/>')
            # mensagem = row[2]

            dia_n = dia_list[i].split('-')
            dia = dia_n[2] + '/' + dia_n[1] + '/' + dia_n[0]

            # postid = row[1]

            reacoes = likes_list[i]
            # reacoes = row[3]
            # print reacoes
            # dia = row[-2]
            # dia = dia_list[i].split('T')[]
            n += 1
            print n
            print i, 'i'
            print dia, 'dia'
            print reacoes, 'likes'
            print mensagem, 'mensagem'

            ref = 'discussao/' + id_list_split[i] + '.html'

            with open('posts_discussao_final.html', 'a') as html_duvidas:
                html_duvidas.write('<div \n class ="container_posts" > \n <div \n class ="numero_post" >' + str(n)
                                + '</div>  \n <div \n class ="data_lateral">' + dia + '</div> <div '
                                'class ="upvote_lateral">' + str(reacoes) + '</div> \n <img class ="seta_upvote_lateral"'
                                'src="arrow_up.png" alt="arrow_up"> \n <div class ="multiline-ellipsis"> '
                                '<a href="' + ref + '">' + mensagem + '</a> </div>  </div>')

with open('posts_discussao_final.html', 'a') as rodape:
    rodape.write('\n </main> \n </body> \n </html>')

# def post():
#     count = 0
#     with open('/media/cleyson/Data/Python Codes/PreParty/Backups/outubro/posts.csv', "rb") as csv_posts:
#         data = csv.reader(csv_posts)
#         your_list = list(data)
#
#         for line in your_list:
#             mensagem = line[3]
#             if '[DUVIDA]' in mensagem:
#                 print 'buga doida', mensagem
#                 if not os.path.exists('/media/cleyson/Data/Python Codes/PreParty/Backups/DUVIDAS'):
#                     os.makedirs('/media/cleyson/Data/Python Codes/PreParty/Backups/DUVIDAS')
#                     os.chdir('/media/cleyson/Data/Python Codes/PreParty/Backups/DUVIDAS')
#                 os.chdir('/media/cleyson/Data/Python Codes/PreParty/Backups/DUVIDAS')
#                 # os.mkdir('test')
#                 # a = input('asa')
#                 # autor = line[5]
#                 post_id = line[0]
#                 count += 1
#                 print count
#
#                 mensagem = mensagem.replace('\\n', '<br/>')
#
#                 with open("" + post_id + ".html", "w") as file:
#                     # print count
#                     # file.write(autor_linha)
#                     file.write('<DOCTYPE html>')
#                     # file.write('<html lang='pt'>')
#                     file.write('<head>')
#                     file.write('<title>Backup Preparty')
#                     file.write('</title>')
#                     file.write('<link rel="stylesheet" href="application.css">')
#                     file.write('</head>')
#                     file.write('<body> <main>')
#                     file.write('<p class="post">')
#                     file.write(mensagem)
#                     file.write('</p>')
#                     file.write('<hr>')
#                     file.write('<h4 class="comment"> Comentarios </h4>')
#                     file.write('<hr>')
#     return post_id
#
#
# def parent_coment(comment_text):
#     # comment_text = comment_text.replace('$', '\$')
#     comment_text = comment_text.replace('\\n', '<br/>')
#     # comment_text = comment_text.replace('%', '\%')
#     # comment_text = comment_text.replace('#', '\#')
#     # comment_text = comment_text.replace('&', '\&')
#     os.chdir(original_path)
#     with open(post_id + '.html', 'a') as post_file:
#         post_file.write('<p class="parent_c">' + comment_text + '</p> \n')
#
#
# def child_comment(comment_text):
#     # comment_text = comment_text.replace('$', '\$')
#     comment_text = comment_text.replace('\\n', '<br/>')
#     # comment_text = comment_text
#     # comment_text = comment_text.replace('%', '\%')
#     # comment_text = comment_text.replace('#', '\#')
#     # comment_text = comment_text.replace('&', '\&')
#     os.chdir(original_path)
#     with open(post_id + '.html', 'a') as post_file:
#         post_file.write('<p class="child_c">' + comment_text + '</p> \n')
#
#     # print texto_comentario_filho
#
# original_path = os.getcwd()
# print original_path
# post_id = post()
#
#
# # Abrir arquivo comentarios
#
# n = 0
# with open('/media/cleyson/Data/Python Codes/PreParty/Backups/outubro/comments.csv', "rb") as csv_com:
#     data = csv.reader(csv_com)
#     list_com = list(data)
#
#     for line in list_com:
#         # print line
#         # Checar se eh comentario do postId
#         if line[6] == post_id and line[7] == '':
#             # Checar se o comentario eh mae
#             parent_comment_id = line[7]
#             # print parent_comment_id
#             parent_coment(line[3])
#             # print line[3]
#             comment_id = line[0]
#             for row in list_com:
#                 # print 'ParentID ', row[7]
#                 n += 1
#                 # print n
#                 # print 'CommentID ', comment_id
#                 if row[7] == comment_id and row[6] == post_id:
#                     # print row[3]
#                     child_comment(comment_text=row[3])
#             # Comentar os filhos
#
# print n