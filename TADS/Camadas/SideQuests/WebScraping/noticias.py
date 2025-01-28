import requests
from lxml import html

pagina = requests.get("http://www.globo.com")
# Eh Gerado uma variavel de nome conteudo com o HTML da pagina
conteudo = html.fromstring(pagina.content)
# noticias eh o resultado da busca pela class hui-premium__title
noticias = conteudo.xpath('//*[@id="destaque"]/div/div/div[1]/div[2]/div/ul/li/div/a/h2/text()')
for manchete in noticias:
    print(manchete)