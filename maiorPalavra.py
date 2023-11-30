texto = "Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker."

i = 0
contMaior = 0
listaTexto = texto.split()
maiorPalavra = ""

while i < len(texto):
    if len[maiorPalavra] > contMaior: 
        contMaior = len[maiorPalavra]
        

    tamanhoPalavra = len(listaTexto[i])    
    print(f"A palavra {listaTexto[i]} possui {tamanhoPalavra} caracteres")
    i += 1

# if len(temp) > m:
#     m = len(temp)
#     txt = tempo