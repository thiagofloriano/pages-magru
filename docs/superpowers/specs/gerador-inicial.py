#!/usr/bin/env python3
# Gerador usado UMA VEZ, em 2026-09-15, para escrever os HTML iniciais a partir do
# conteúdo extraído do WordPress. O site NÃO tem build: a fonte da verdade são os
# arquivos .html do repositório. Este script fica aqui só como registro — rodá-lo
# de novo sobrescreve qualquer edição feita à mão.

import json, os, html, pathlib

RAIZ = pathlib.Path("/home/floriano/thiagofloriano/magru")
SITE = "https://magru.com.br"
WP = "https://blog.magru.com.br"
SIZES = json.load(open(os.path.join(os.path.dirname(__file__), "sizes.json")))

SECOES = [
    dict(slug="literatura", nome="Literatura", cor="--literatura", f=".58", ang="25deg", lado="dir", periodo="64s",
         resumo="Poesia, crítica e o ofício de escrever", n=12),
    dict(slug="artes", nome="Artes", cor="--artes", f=".66", ang="85deg", lado="dir", periodo="88s",
         resumo="Xilogravura e fotografia de Itajaí", n=2),
    dict(slug="blog", nome="Blog", cor="--blog", f=".74", ang="145deg", lado="esq", periodo="116s",
         resumo="Textos novos, publicados semana a semana", n=0),
    dict(slug="historia", nome="História", cor="--historia", f=".83", ang="205deg", lado="esq", periodo="148s",
         resumo="A fundação, o nome e a memória da cidade", n=8),
    dict(slug="ensaios", nome="Ensaios", cor="--ensaios", f=".91", ang="265deg", lado="esq", periodo="184s",
         resumo="Tempo, política, sociedade e método", n=8),
    dict(slug="imprensa", nome="Imprensa", cor="--imprensa", f="1", ang="325deg", lado="dir", periodo="224s",
         resumo="Jornalismo regional e cultura pesqueira", n=4),
]

W = "/wp/wordpress/wp-content/uploads/2015/01/"
U = "/web/wp-content/uploads/"

ACERVO = {
"literatura": dict(
    titulo="Literatura",
    subtitulo="Poesia, crítica literária e o ofício de escrever",
    meta="Os seis livros de poesia de Magru Floriano e seus ensaios sobre literatura catarinense, todos em PDF de leitura livre.",
    lead="Seis livros de poesia e seis trabalhos sobre o ofício de escrever. A obra poética de Magru Floriano vai da militância declarada dos primeiros títulos à observação íntima dos últimos, e vem acompanhada do inventário e da crítica que ele dedicou aos autores da região da foz do rio Itajaí-Açu.",
    obras=[
    ("Saudades", "Itajaí: Brisa Utópica, 2025. Poesia.",
     "Um livro inteiro dedicado a uma palavra. Magru Floriano persegue a saudade poema a poema, testando as definições que a prosa não alcança, no vocabulário afetivo de quem escreve do litoral de Santa Catarina.",
     U+"2025/04/magru-floriano_saudades.pdf"),
    ("Há cais", "Itajaí: Brisa Utópica, 2020; Itajaí: Ipêamarelo, 2023. Poesia.",
     "Poesia de porto e de maré. O cais, o casco, a rede e a gente que vive do mar entram no livro pelo vocabulário de quem cresceu na foz do rio Itajaí-Açu, onde a cidade e a navegação nunca se separaram.",
     U+"2025/04/magru-floriano_ha-cais.pdf"),
    ("Cotidianas: poesias de um cidadão oprimido", "Itajaí: Brisa Utópica, 1999. Poesia.",
     "O primeiro livro de poemas do autor. Escrito na voz do cidadão comum diante do poder, reúne a matéria do dia a dia — trabalho, cidade, injustiça miúda — na linguagem direta que marcaria toda a sua poesia.",
     W+"cotidianas.pdf"),
    ("Fogo-fátuo: o diário de um poeta triste", "Itajaí: Brisa Utópica, 2001. Poesia.",
     "Poesia engajada em forma de diário. O livro acompanha o estado de espírito de um poeta que não consegue separar a tristeza pessoal do desconforto político, e faz das duas a mesma escrita.",
     W+"fogo_fatuo.pdf"),
    ("O grito universal: o grito da terra e outros gritos", "Itajaí: Brisa Utópica, 2009; 2.ed. 2011. Poesia.",
     "O livro em que o autor mergulha de vez no mundo político. É a ponte entre arte e militância, e a confirmação de uma poesia que se recusa a ser decorativa.",
     W+"grito_universal.pdf"),
    ("Pia-máter & Insight", "Itajaí: Brisa Utópica, 2008; 2.ed. 2011. Poesia.",
     "Poemas mais suaves, escritos quando o autor começa a abandonar o engajamento radical. A tensão política cede lugar à observação íntima, sem que o olhar crítico desapareça.",
     W+"pia_mater.pdf"),
    ("Aprendendo a fazer poesia com autores catarinenses", "Itajaí: Brisa Utópica, 2002. Ensaio.",
     "Uma oficina montada sobre a obra de poetas de Santa Catarina. Magru Floriano lê versos alheios atrás dos procedimentos que os fazem funcionar, e entrega ao aprendiz os macetes que encontrou.",
     W+"aprendendo_poesia.pdf"),
    ("Como faço poesia", "Itajaí: Brisa Utópica, 2001. Ensaio.",
     "Um esboço reflexivo sobre método. O autor descreve como seus próprios poemas nascem, do primeiro registro à versão final, e transforma a prática em algo que pode ser ensinado.",
     W+"como_poesia.pdf"),
    ("Inventário bibliográfico dos autores da região da foz do rio Itajahy até 2010", "Itajaí: Brisa Utópica, 2011. Pesquisa documental.",
     "Um banco de dados sobre os escritores da região. Continua o levantamento iniciado em 2001 com Quem escreve em Itajaí, e é hoje uma das fontes de referência para quem estuda a literatura do litoral catarinense.",
     W+"inventario_bibliografico.pdf"),
    ("Literatura: crítica literária", "Itajaí: Brisa Utópica, 2004. Ensaio.",
     "Cinco textos de crítica, entre eles a análise de dois livros de Lausimar Laus: Ofélia dos Navios e O guarda-roupa alemão. Leitura atenta de uma obra central da literatura catarinense.",
     W+"critica_literaria.pdf"),
    ("Poesia engajada: o papel social da literatura", "Itajaí: Brisa Utópica. Ensaio.",
     "Texto breve sobre o compromisso do escritor com a sociedade. Uma defesa da literatura que responde ao seu tempo, contra a arte alienada e descontextualizada.",
     W+"poesia_engajada.pdf"),
    ("Autor do mês", "Itajaí: Brisa Utópica, 2022. Coletânea.",
     "Reunião dos textos que o autor publicou na revista Literatura Papa-Siri, apresentando mês a mês escritores e obras da região.",
     U+"2022/07/magru-floriano-autor-do-mes.pdf"),
    ]),

"ensaios": dict(
    titulo="Ensaios",
    subtitulo="Tempo, política, sociedade e método",
    meta="Oito ensaios de Magru Floriano sobre tempo e história, análise de conjuntura, sociologia, cinema e poder. PDF de leitura livre.",
    lead="Oito ensaios escritos ao longo de duas décadas de docência em Sociologia e Filosofia na Univali, quando o autor tinha o hábito de transformar em texto tudo aquilo que precisava explicar em aula.",
    obras=[
    ("O tempo da história: reflexões sobre tempo, memória e história", "Itajaí: Brisa Utópica, 2024. Ensaio.",
     "Uma tentativa de pôr ordem em anos de leitura sobre a relação entre tempo e história. Nasce do incômodo de encontrar História e Filosofia entrelaçadas em conceitos como permanência e ruptura, sem que ninguém os separasse com clareza.",
     U+"2025/01/magru-floriano_o-tempo-da-historia_16dez2024.pdf"),
    ("Roteiro cultural de São Paulo", "Itajaí: Brisa Utópica, 2019. Ensaio.",
     "Esboço fenomenológico de uma incursão na terra bandeirante. O autor saiu às ruas de São Paulo com lapiseira e bloco de notas para registrar, sem filtro, o que lhe passava pela cabeça diante de obras de arte, monumentos e pessoas.",
     U+"2025/01/magru-floriano_roteiro-cultural-de-sp_15dez2024.pdf"),
    ("Peão na sétima casa: o poder no tabuleiro de xadrez", "Itajaí: Brisa Utópica, 2022. Ensaio.",
     "Exercício livre de pensamento sobre as relações entre o jogo de xadrez e o jogo político. Abertura, meio-jogo e final lidos como estratégias de poder.",
     U+"2022/03/Magru-Floriano-Peão-na-sétima-casa.pdf"),
    ("Ensaios de sociologia", "Itajaí: Brisa Utópica, 2004. Ensaio.",
     "Três textos independentes: a forma de pensar dos radicais envolvidos com seitas e religiões, um conceito atualizado de analfabetismo, e o hábito oligárquico de inscrever nomes próprios em ruas, praças e instituições.",
     W+"ensaios_sociologia.pdf"),
    ("A lógica do eleitor", "Itajaí: Brisa Utópica, 2011. Ensaio.",
     "Reflexão sobre o processo eleitoral de 2008 em Itajaí e sobre como o resultado de uma eleição serve de referência para a seguinte. Escrito antes de 2010, o texto previu a queda da esquerda no município.",
     W+"livro_eleitor.pdf"),
    ("Análise: esforço para compreender a realidade em que vivemos", "Itajaí: Brisa Utópica, 2011. Ensaio.",
     "Apresentação ampliada do método de análise de conjuntura, uma técnica para ler o processo social sem se perder no noticiário.",
     W+"livro_analise.pdf"),
    ("Política: texto referência para um diálogo aberto sobre a prática política", "Itajaí: Brisa Utópica, 2011. Ensaio.",
     "Um mapa das ideologias políticas, da esquerda à direita, escrito para servir de base comum a quem quer discutir política sem confundir os termos.",
     W+"livro_politica.pdf"),
    ("Ver cinema, ler cinema", "Itajaí: Brisa Utópica, 2001. Ensaio.",
     "Escrito quando o autor usava filmes para dar aulas de Sociologia e Filosofia na Univali. Propõe assistir ao cinema como quem lê um texto, atrás daquilo que o filme argumenta.",
     W+"vercinema.pdf"),
    ]),

"historia": dict(
    titulo="História",
    subtitulo="A fundação, o nome e a memória de Itajaí",
    meta="Oito livros de Magru Floriano sobre a história de Itajaí: a fundação da cidade, a origem do nome, o incêndio de 1965 e a historiografia regional. PDF livre.",
    lead="A história de Itajaí em oito livros: a fundação da cidade, o significado do seu nome, o incêndio de 1965 e o inventário de quem escreveu essa história antes. Mais de vinte anos de pesquisa em arquivos, jornais e acervos do litoral de Santa Catarina.",
    obras=[
    ("Itajaí em chamas", "Itajaí: Alternativa, 2002; com Ivan Rupp, 2006. Grande reportagem.",
     "Reconstituição jornalística do incêndio do navio gaseiro Petrobras Norte nos terminais Liquigás e Heliogás, em Cordeiros, no dia 2 de fevereiro de 1965. Fatos e fotos de um dos maiores desastres da história da cidade.",
     U+"2017/10/Itajai_em_chamas.pdf"),
    ("A lenda do Monte Tayó", "Itajaí: Alternativa; Blumenau: Nova Letra, 2012. História.",
     "Contribuição à discussão centenária sobre o significado do nome Itajaí. O texto recolhe todas as interpretações já propostas e sugere uma nova, à luz de evidências históricas recentes.",
     U+"2017/10/Lenda_do_monte_tayo.pdf"),
    ("Itajaí: uma cidade em busca do seu fundador", "3.ed. Itajaí: Brisa Utópica. Pesquisa documental.",
     "Cinquenta e três textos publicados na imprensa regional sobre a fundação de Itajaí, compilados e organizados. O dossiê de uma polêmica que a cidade nunca encerrou.",
     U+"2018/11/itajai_fundador.pdf"),
    ("Ensaios: história", "Itajaí: Brisa Utópica, 2004. Ensaio.",
     "Textos sobre a história de Itajaí publicados em revistas e jornais da região. Destaque para o relato da captação dos primeiros sinais de televisão na cidade, pelos Schiefler.",
     W+"ensaios_historia.pdf"),
    ("A fundação de Itajaí: historiografia anotada e comentada", "Itajaí: Brisa Utópica, 2018. Ensaio.",
     "Levantamento comentado de tudo o que se escreveu sobre a fundação de Itajaí, com as anotações críticas de quem leu as fontes uma a uma.",
     U+"2018/11/itajai_fundacao.pdf"),
    ("Histórias de Itajaí", "Itajaí: Brisa Utópica, 2020; Itajaí: Ipêamarelo, 2024. Pesquisa histórica.",
     "Episódios da história itajaiense contados um a um, do porto às ruas, no tom de quem passou décadas garimpando arquivo e jornal velho.",
     U+"2017/10/HISTORIAS-DE-ITAJAI-.pdf"),
    ("A história da história de Itajaí, vol. 1", "Itajaí: Brisa Utópica, 2022. Inventário historiográfico.",
     "Inventário de quem escreveu a história de Itajaí e de como a escreveu. Um livro sobre os historiadores, antes de ser sobre a cidade.",
     U+"2022/07/magru-floriano-historiografia11abril2022.pdf"),
    ("As histórias que contei no Anuário de Itajaí, vol. 1", "Itajaí: Brisa Utópica, 2023. Ensaios históricos.",
     "Reunião dos ensaios que o autor publicou ano a ano no Anuário de Itajaí, da Fundação Genésio Miranda Lins.",
     U+"2023/08/historias_anuario_vol1.pdf"),
    ]),

"imprensa": dict(
    titulo="Imprensa",
    subtitulo="Jornalismo regional e cultura pesqueira",
    meta="Quatro livros de Magru Floriano sobre a imprensa da Grande Itajaí e a pesca da tainha no litoral de Santa Catarina. PDF de leitura livre.",
    lead="Quatro livros sobre jornalismo e cultura popular no litoral catarinense, escritos por quem trabalha em redação desde 1975 e fundou o curso de Jornalismo da Univali.",
    obras=[
    ("História da imprensa em Itajaí, vol. 1, tomo 1: jornal e revista", "Itajaí: Brisa Utópica, 2021. Pesquisa documental.",
     "Inventário dos jornais e revistas publicados em Itajaí, título a título. Base documental para qualquer estudo sobre a comunicação na região da foz do rio Itajaí-Açu.",
     U+"2021/05/Magru-Floriano-História-da-imprensa-vol-I-tomo-I.pdf"),
    ("Artigos & crônicas", "Itajaí: Brisa Utópica. Crônica.",
     "Cinquenta e dois textos publicados na imprensa regional sobre os mais diversos temas. Muitas dessas crônicas foram escritas para serem lidas no rádio, e guardam o ritmo da voz.",
     W+"artigos.pdf"),
    ("Imprensa: textos sobre a imprensa regional", "Itajaí: Brisa Utópica, 2004. Ensaio.",
     "Textos sobre a imprensa da Grande Itajaí, alguns publicados no Anuário de Itajaí e outros inéditos, entre eles a história do Clube da Imprensa e o inventário dos veículos da região.",
     W+"ensaios_imprensa.pdf"),
    ("Tainha: a tradição da pesca da tainha no litoral de Santa Catarina", "Itajaí: Brisa Utópica, 2016. Grande reportagem.",
     "História oral e jornalismo a serviço da cultura pesqueira catarinense. Pescadores, armadores e líderes classistas contam a safra; o livro traz ainda um dicionário das expressões usadas no mar e o inventário das canoas da foz do rio Itajaí.",
     U+"2017/10/Magru-Floriano-Tainha.pdf"),
    ]),

"artes": dict(
    titulo="Artes",
    subtitulo="Xilogravura e fotografia",
    meta="Xilogravuras do patrimônio histórico de Itajaí e o ensaio fotográfico de Magru Floriano, em PDF de leitura livre.",
    lead="Xilogravura e fotografia. As duas obras reunidas aqui são o trabalho visual de um autor que expõe desde 1974 e mantém ateliê próprio em Itajaí desde 2022.",
    obras=[
    ("O passado presente", "Itajaí: Brisa Utópica, 2025, edição limitada; 2026, edição digital. Xilogravura.",
     "Xilogravuras do patrimônio histórico edificado de Itajaí. Os casarões, as igrejas e os prédios que a cidade ainda tem, e alguns que já perdeu, cortados na madeira.",
     U+"2026/01/magru-floriano_o-passado-presente.pdf"),
    ("Meu olhar na fotografia", "Itajaí: Brisa Utópica, 2025. Ensaio fotográfico.",
     "Reunião do trabalho fotográfico do autor e do raciocínio por trás dele: o que procura no enquadramento e por que fotografa o que fotografa.",
     U+"2026/02/magru-floriano_meu-olhar-na-foto.pdf"),
    ]),
}

DIREITOS = ("Os livros podem ser baixados, lidos e usados para fins educacionais e jornalísticos, desde que citada a fonte. "
            "Os direitos de reprodução, alteração e comercialização são reservados ao autor.")

EXTERNOS = [
    ("Blog do Magru", WP + "/web/blog/", "Textos novos, no WordPress"),
    ("Itajaipedia", "https://itajaipedia.com.br", "Enciclopédia digital itajaiense"),
    ("Fotografias no Flickr", "https://www.flickr.com/photos/magru-floriano/", "Arquivo fotográfico"),
    ("Canal no WhatsApp", "https://magru.com.br/whatsapp", "Avisos de novas publicações"),
    ("Grupo no Telegram", "https://t.me/blogdomagru", "Conversa aberta"),
    ("Facebook", "https://www.facebook.com/florianomagru", "Itajaí de Antigamente"),
]


def tamanho(caminho):
    b = SIZES.get(caminho, 0)
    mb = b / 1048576
    if mb >= 1:
        return f"{mb:.1f}".replace(".", ",") + " MB"
    return f"{round(b / 1024)} KB"


def e(s):
    return html.escape(s, quote=False)


def cabecalho(atual, rel):
    itens = []
    for s in SECOES:
        href = WP + "/web/blog/" if s["slug"] == "blog" else f"{rel}{s['slug']}/index.html"
        marca = ' aria-current="page"' if s["slug"] == atual else ""
        itens.append(f'      <li><a href="{href}"{marca}>{e(s["nome"])}</a></li>')
    marca_cv = ' aria-current="page"' if atual == "curriculo" else ""
    itens.append(f'      <li><a href="{rel}curriculo/index.html"{marca_cv}>Currículo</a></li>')
    return f"""<a class="pular" href="#conteudo">Ir para o conteúdo</a>
<header class="topo">
  <div class="envelope">
    <div class="topo__interno">
      <a class="marca" href="{rel}index.html"><span class="marca__astro" aria-hidden="true"></span>Universo do Magru</a>
      <button class="menu-botao" type="button" aria-controls="rota" hidden>Seções</button>
    </div>
    <ul class="rota" id="rota">
{chr(10).join(itens)}
    </ul>
  </div>
</header>"""


def rodape(rel):
    links = "\n".join(
        f'          <li><a href="{u}">{e(n)}</a></li>' for n, u, _ in EXTERNOS
    )
    secoes = "\n".join(
        f'          <li><a href="{rel}{s["slug"]}/index.html">{e(s["nome"])}</a></li>'
        for s in SECOES if s["slug"] != "blog"
    )
    return f"""<footer class="rodape">
  <div class="envelope">
    <div class="rodape__grade">
      <div>
        <h2>Acervo</h2>
        <ul>
{secoes}
          <li><a href="{rel}curriculo/index.html">Currículo</a></li>
        </ul>
      </div>
      <div>
        <h2>Em outros lugares</h2>
        <ul>
{links}
        </ul>
      </div>
    </div>
    <p class="rodape__nota" id="direitos"><b>Direitos de uso.</b> {DIREITOS}</p>
    <p class="rodape__bio">Universo do Magru reúne a obra de Hélio Floriano dos Santos, o Magru Floriano, escritor, historiador e xilogravurista nascido em Itajaí em 1956.</p>
  </div>
</footer>"""


def pagina(titulo, descricao, url, corpo, jsonld, atual="", cor=None, classe="", prof=0, base=None):
    # Caminhos relativos: o site funciona tanto na raiz de magru.com.br quanto
    # num subcaminho, como o thiagofloriano.github.io/pages-magru/ do GitHub Pages.
    # O 404 é a exceção: como é servido a partir de qualquer caminho, precisa de
    # endereços absolutos.
    rel = base if base is not None else "../" * prof
    estilo = f' style="--acento: var({cor})"' if cor else ""
    ld = "\n".join(
        '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + "</script>"
        for j in jsonld
    )
    return f"""<!doctype html>
<html lang="pt-BR"{estilo}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)}</title>
<meta name="description" content="{html.escape(descricao)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Universo do Magru">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{html.escape(titulo)}">
<meta property="og:description" content="{html.escape(descricao)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{rel}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT,WONK@9..144,300..600,0..100,0..1&display=swap">
<link rel="stylesheet" href="{rel}assets/css/magru.css">
{ld}
</head>
<body{f' class="{classe}"' if classe else ""}>
{cabecalho(atual, rel)}
{corpo}
{rodape(rel)}
<script src="{rel}assets/js/magru.js" defer></script>
</body>
</html>
"""


def escrever(caminho, conteudo):
    destino = RAIZ / caminho
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(conteudo, encoding="utf-8")
    print("escrito", caminho, len(conteudo))


# ---------- home ----------

def home():
    aneis, orbitas, cartoes = [], [], []
    for s in SECOES:
        href = WP + "/web/blog/" if s["slug"] == "blog" else f"{s['slug']}/index.html"
        aneis.append(f'    <div class="anel" style="--f: {s["f"]}"></div>')
        orbitas.append(
            f'    <div class="orbita" style="--f: {s["f"]}; --angulo: {s["ang"]}">\n'
            f'      <a class="planeta" href="{href}" style="--cor: var({s["cor"]})"><span>{e(s["nome"])}</span></a>\n'
            f"    </div>"
        )
        conta = f"<em>{s['n']} obras em PDF</em>" if s["n"] else "<em>no WordPress</em>"
        cartoes.append(
            f'    <li><a href="{href}" style="--cor: var({s["cor"]})">\n'
            f'      <b>{e(s["nome"])}</b>\n'
            f'      <span>{e(s["resumo"])}</span>\n'
            f"      {conta}\n"
            f"    </a></li>"
        )

    corpo = f"""<main id="conteudo">
  <div class="envelope abertura">
    <h1>Cinquenta anos escrevendo sobre a mesma cidade</h1>
    <p>Poesia, história, imprensa e xilogravura. A obra de Magru Floriano gira em torno da foz do rio Itajaí-Açu desde 1975. Trinta e quatro livros e ensaios, todos em PDF de leitura livre.</p>
  </div>

  <nav class="sistema" aria-label="Áreas do acervo">
{chr(10).join(aneis)}
    <p class="sol">Magru Floriano</p>
{chr(10).join(orbitas)}
  </nav>

  <div class="envelope">
    <ul class="orbitas">
{chr(10).join(cartoes)}
    </ul>
  </div>

  <div class="envelope prosa">
    <h2>Quem é Magru Floriano</h2>
    <p>Hélio Floriano dos Santos nasceu em Itajaí em 13 de agosto de 1956. Começou na imprensa em 1975, editando o jornal alternativo <em>Atire a Primeira Pedra</em>, e desde então foi repórter do Jornal de Santa Catarina, professor da Univali por 28 anos, fundador do curso de Jornalismo e da Rádio Univali FM, presidente da Academia Itajaiense de Letras e do Clube da Imprensa de Itajaí, e idealizador da <a href="https://itajaipedia.com.br">Itajaipedia</a>.</p>
    <p>Graduado em Pedagogia e em História pela Univali e mestre em Educação pela Furb, publicou mais de quarenta títulos entre poesia, ensaio, pesquisa histórica e grande reportagem. Expõe xilogravura e fotografia desde 1974 e mantém ateliê na Rua Conceição, no bairro São João, desde 2022.</p>
    <p><a href="curriculo/index.html">Ver o currículo completo</a></p>
  </div>
</main>"""

    pessoa = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Magru Floriano",
        "alternateName": "Hélio Floriano dos Santos",
        "birthDate": "1956-08-13",
        "birthPlace": {"@type": "Place", "name": "Itajaí, Santa Catarina, Brasil"},
        "jobTitle": ["Escritor", "Historiador", "Jornalista", "Xilogravurista"],
        "url": SITE + "/",
        "sameAs": [u for _, u, _ in EXTERNOS] + ["https://itajaipedia.com.br/artigos/helio-floriano-dos-santos/"],
    }
    site = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Universo do Magru",
        "url": SITE + "/",
        "inLanguage": "pt-BR",
        "about": "Obra de Magru Floriano sobre a história de Itajaí, imprensa regional, poesia e xilogravura",
        "copyrightHolder": {"@type": "Person", "name": "Magru Floriano"},
        "copyrightNotice": DIREITOS,
    }
    escrever("index.html", pagina(
        "Universo do Magru — obra de Magru Floriano: história de Itajaí, poesia e xilogravura",
        "Acervo digital de Magru Floriano: 34 livros e ensaios em PDF sobre a história de Itajaí, imprensa regional, poesia e xilogravura. Leitura livre.",
        SITE + "/", corpo, [pessoa, site]))


# ---------- seções ----------

def secao(slug):
    d = ACERVO[slug]
    s = next(x for x in SECOES if x["slug"] == slug)
    itens, ld_itens = [], []
    for i, (titulo, ficha, texto, pdf) in enumerate(d["obras"], 1):
        url = WP + pdf
        itens.append(f"""      <li class="obra">
        <h2>{e(titulo)}</h2>
        <p>{e(texto)}</p>
        <p class="obra__ficha">{e(ficha)}</p>
        <a class="baixar" href="{url}" type="application/pdf" aria-label="Ler em PDF ({tamanho(pdf)}): {e(titulo)}">Ler em PDF ({tamanho(pdf)})</a>
      </li>""")
        ld_itens.append({
            "@type": "ListItem", "position": i,
            "item": {"@type": "Book", "name": titulo, "author": {"@type": "Person", "name": "Magru Floriano"},
                     "inLanguage": "pt-BR", "url": url, "encodingFormat": "application/pdf",
                     "abstract": texto,
                     "isAccessibleForFree": True,
                     "copyrightHolder": {"@type": "Person", "name": "Magru Floriano"},
                     "copyrightNotice": DIREITOS},
        })

    corpo = f"""<main id="conteudo">
  <div class="envelope cabeca">
    <p class="migalhas"><a href="../index.html">Universo do Magru</a> / <b>{e(d["titulo"])}</b></p>
    <h1>{e(d["subtitulo"])}</h1>
    <p>{e(d["lead"])}</p>
    <p class="nota-direitos">{e(DIREITOS)}</p>
  </div>
  <div class="envelope">
    <ul class="acervo">
{chr(10).join(itens)}
    </ul>
  </div>
</main>"""

    url = f"{SITE}/{slug}/"
    colecao = {
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": d["titulo"], "url": url, "inLanguage": "pt-BR",
        "description": d["meta"],
        "mainEntity": {"@type": "ItemList", "numberOfItems": len(d["obras"]), "itemListElement": ld_itens},
    }
    migalhas = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Universo do Magru", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": d["titulo"], "item": url},
        ],
    }
    escrever(f"{slug}/index.html", pagina(
        f"{d['titulo']} — {d['subtitulo']} | Magru Floriano",
        d["meta"], url, corpo, [colecao, migalhas], atual=slug, cor=s["cor"], prof=1))


# ---------- currículo ----------

def curriculo():
    dados = json.load(open(os.path.join(os.path.dirname(__file__), "curriculo.json")))
    par = dados["paragrafos"]
    listas = dados["listas"]
    anuario = [l for l in listas if l[:4].isdigit()]
    obra = [l for l in listas if not l[:4].isdigit()]

    # Os títulos vinham em caixa alta no WordPress; aqui viram headings de verdade.
    TITULOS = {
        "REPRESENTAÇÃO ESTUDANTIL": "Representação estudantil",
        "REPRESENTAÇÃO": "Representação institucional",
        "DOCÊNCIA": "Docência",
        "IMPRENSA": "Imprensa",
        "ARTES VISUAIS": "Artes visuais",
    }

    secoes_cv = []
    for p in par[1:]:
        rotulo = p.split(":")[0].strip()
        if rotulo in TITULOS:
            corpo_txt = p.partition(":")[2].strip()
            corpo_txt = corpo_txt[:1].upper() + corpo_txt[1:]
            secoes_cv.append(f"    <h2>{e(TITULOS[rotulo])}</h2>\n    <p>{e(corpo_txt)}</p>")
        elif p.startswith("HÉLIO"):
            intro = p.replace("HÉLIO FLORIANO DOS SANTOS", "Hélio Floriano dos Santos", 1)
            secoes_cv.insert(0, f"    <p>{e(intro)}</p>")

    anuario_html = "\n".join(f"      <li>{e(x)}</li>" for x in anuario)
    obra_html = "\n".join(f"      <li>{e(x)}</li>" for x in obra)

    corpo = f"""<main id="conteudo">
  <div class="envelope cabeca">
    <p class="migalhas"><a href="../index.html">Universo do Magru</a> / <b>Currículo</b></p>
    <h1>Magru Floriano</h1>
    <p>Cinco décadas de imprensa, docência, pesquisa histórica e artes visuais no litoral de Santa Catarina.</p>
  </div>
  <div class="envelope prosa">
{chr(10).join(secoes_cv)}
    <h2>Artigos no Anuário de Itajaí</h2>
    <p>Publicações na revista anual da Fundação Genésio Miranda Lins.</p>
    <ul>
{anuario_html}
    </ul>
    <h2>Obra publicada</h2>
    <p>Mídia impressa, xerografada e digital. Os títulos disponíveis em PDF estão nas seções de <a href="../literatura/index.html">literatura</a>, <a href="../ensaios/index.html">ensaios</a>, <a href="../historia/index.html">história</a>, <a href="../imprensa/index.html">imprensa</a> e <a href="../artes/index.html">artes</a>.</p>
    <ul>
{obra_html}
    </ul>
    <p>Veja também o verbete sobre Magru Floriano na <a href="https://itajaipedia.com.br/artigos/helio-floriano-dos-santos/">Itajaipedia</a>.</p>
  </div>
</main>"""

    url = SITE + "/curriculo/"
    ld = {
        "@context": "https://schema.org", "@type": "ProfilePage", "url": url, "inLanguage": "pt-BR",
        "mainEntity": {
            "@type": "Person", "name": "Magru Floriano", "alternateName": "Hélio Floriano dos Santos",
            "birthDate": "1956-08-13", "birthPlace": {"@type": "Place", "name": "Itajaí, Santa Catarina, Brasil"},
            "jobTitle": ["Escritor", "Historiador", "Jornalista", "Xilogravurista"],
            "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Univali"},
                         {"@type": "CollegeOrUniversity", "name": "Furb"}],
            "url": url,
        },
    }
    migalhas = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Universo do Magru", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Currículo", "item": url},
        ],
    }
    escrever("curriculo/index.html", pagina(
        "Currículo de Magru Floriano — escritor, historiador e jornalista de Itajaí",
        "Trajetória de Hélio Floriano dos Santos, o Magru Floriano: imprensa desde 1975, docência na Univali, pesquisa histórica sobre Itajaí, xilogravura e obra publicada.",
        url, corpo, [ld, migalhas], atual="curriculo", prof=1))


def erro404():
    corpo = f"""<main id="conteudo">
  <div class="envelope perdido">
    <h1>Essa página saiu de órbita</h1>
    <p>O endereço não existe mais, ou nunca existiu. O acervo inteiro continua a um clique daqui.</p>
    <p><a href="{SITE}/">Voltar ao centro do sistema</a></p>
  </div>
</main>"""
    escrever("404.html", pagina("Página não encontrada — Universo do Magru",
                               "O endereço pedido não existe no Universo do Magru.",
                               SITE + "/404.html", corpo, [], base=SITE + "/"))


def extras():
    urls = ["/", "/curriculo/"] + [f"/{s['slug']}/" for s in SECOES if s["slug"] != "blog"]
    corpo = "\n".join(
        f"  <url><loc>{SITE}{u}</loc><changefreq>monthly</changefreq>"
        f"<priority>{'1.0' if u == '/' else '0.8'}</priority></url>" for u in urls)
    escrever("sitemap.xml",
             '<?xml version="1.0" encoding="UTF-8"?>\n'
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + corpo + "\n</urlset>\n")
    escrever("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    # Sem CNAME: o domínio personalizado só entra quando a migração do DNS for
    # aprovada. Escrever o arquivo aqui derruba a URL de preview do GitHub Pages.
    escrever("assets/favicon.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
<rect width="32" height="32" fill="#0a1020"/>
<circle cx="16" cy="16" r="13" fill="none" stroke="#ede6d8" stroke-opacity=".3"/>
<circle cx="16" cy="16" r="7" fill="url(#s)"/>
<circle cx="29" cy="16" r="2.4" fill="#9bc4e2"/>
<defs><radialGradient id="s" cx=".38" cy=".32"><stop offset="0" stop-color="#ffe3a8"/><stop offset=".45" stop-color="#f0a830"/><stop offset="1" stop-color="#e2582a"/></radialGradient></defs>
</svg>
""")


home()
for slug in ACERVO:
    secao(slug)
curriculo()
erro404()
extras()
print("pronto")
