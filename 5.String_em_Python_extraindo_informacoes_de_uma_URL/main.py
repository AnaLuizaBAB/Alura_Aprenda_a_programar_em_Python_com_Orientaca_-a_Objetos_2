url = 'http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

'''Separa a base e os parÂmetros'''
indice_do_ponto_de_interrogacao = url.find("?")
url_base = url[:indice_do_ponto_de_interrogacao]
url_parametros = url[indice_do_ponto_de_interrogacao+1:]


'''Procura/informa o valor dos parâmetros'''
parametro_busca = 'moedaOrigem'
indice_parametro_busca = url.find(parametro_busca)
indice_valor_do_parametro_busca = indice_parametro_busca + len(parametro_busca) + 1
indice_do_ecomercial = url.find("&", indice_valor_do_parametro_busca)
if indice_do_ecomercial == -1:
    valor_do_parametro_busca = url[indice_valor_do_parametro_busca:]
else:
    valor_do_parametro_busca = url[indice_valor_do_parametro_busca:indice_do_ecomercial]
print(valor_do_parametro_busca)