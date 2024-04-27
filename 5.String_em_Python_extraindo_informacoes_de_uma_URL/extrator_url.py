import re

class Extrator_URL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url (self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError("URL vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")
        else:
            print("A URL é válida")
        
    def get_url_base(self):
        indice_do_ponto_de_interrogacao = self.url.find("?")
        url_base = self.url[:indice_do_ponto_de_interrogacao]
        return url_base

    def get_url_parametro(self):
        indice_do_ponto_de_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_do_ponto_de_interrogacao+1:]
        return url_parametros

    def get_valor_do_parametro(self, parametro_busca):
        indice_parametro_busca = self.url.find(parametro_busca)
        indice_valor_do_parametro_busca = indice_parametro_busca + len(parametro_busca) + 1
        indice_do_ecomercial = self.url.find("&", indice_valor_do_parametro_busca)
        if indice_do_ecomercial == -1:
            valor_do_parametro_busca = self.url[indice_valor_do_parametro_busca:]
        else:
            valor_do_parametro_busca = self.url[indice_valor_do_parametro_busca:indice_do_ecomercial]
        return valor_do_parametro_busca      

    def __len__(self):
        return len(self.url)
    
    def __str__ (self):
        return self.url + "\n" + "- URL Parâmetros:" + self.get_url_parametro() + "\n" + "- URL Base: " + self.get_url_base()
    
    def __eq__ (self, other):
        return self.url == other.url

extrator_url = Extrator_URL("http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
valor_parametro_quantidade = extrator_url.get_valor_do_parametro("quantidade")
print(f"O ramanhado da url é: {len(extrator_url)}")
print(extrator_url)
print (valor_parametro_quantidade)