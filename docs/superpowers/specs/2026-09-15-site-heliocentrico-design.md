# Universo do Magru — site estático heliocêntrico

Data: 2026-09-15

## Objetivo

Substituir o WordPress em `magru.com.br/web` por um site estático (HTML + CSS + JavaScript vanilla) hospedado no GitHub Pages, com design heliocêntrico, mobile-first e foco em SEO. O WordPress continua existindo apenas para o blog e para servir os PDFs.

## Decisões tomadas

| Questão | Decisão |
|---|---|
| Domínio | `magru.com.br` passa a apontar para o GitHub Pages |
| WordPress | migra para `blog.magru.com.br`, mantendo blog e PDFs |
| Links antigos | aceita-se a quebra das URLs `magru.com.br/web/...` existentes |
| Metáfora | órbita interativa na home; linguagem solar nas páginas internas |
| Conteúdo | migrado do site atual e enriquecido para SEO |
| Imagens | apenas o que existe no site atual; design não depende de fotos |
| Currículo | sai da home e vira `/curriculo/` |

### Consequência aceita da mudança de domínio

Todo link externo para `https://magru.com.br/web/wp-content/uploads/...` e `http://www.magru.com.br/wp/wordpress/wp-content/uploads/...` deixará de funcionar quando o DNS mudar. Isso inclui citações em redes sociais, na Itajaipedia e em trabalhos acadêmicos. O usuário optou conscientemente por esse caminho.

Mitigação possível no futuro, fora do escopo deste trabalho: configurar redirecionamento 301 no servidor do WordPress de `/web/wp-content/uploads/*` para o novo host — só funciona para quem já resolver o subdomínio, não para o domínio raiz.

## Arquitetura

Site estático puro, sem etapa de build, sem dependências. Sete páginas HTML escritas à mão, um arquivo CSS, um arquivo JavaScript pequeno.

```
/                   index.html      home heliocêntrica
/curriculo/         index.html      currículo completo
/literatura/        index.html      12 obras
/ensaios/           index.html       8 obras
/historia/          index.html       8 obras
/imprensa/          index.html       4 obras
/artes/             index.html       2 obras
404.html
assets/css/magru.css
assets/js/magru.js
assets/img/          logo e imagens recuperadas do WP
sitemap.xml
robots.txt
CNAME               magru.com.br
```

Header e rodapé são duplicados nos sete arquivos. É duplicação deliberada: para sete páginas, manter cópias é mais barato que introduzir um gerador de site e a manutenção que ele carrega. Se o número de páginas crescer muito além disso, a troca por um gerador simples é o caminho de upgrade.

### Por que multi-página e não one-pager

Cada área vira uma URL indexável, com `<h1>`, `<title>`, meta description e JSON-LD próprios. Um one-pager concentraria tudo num único alvo de ranqueamento e desperdiçaria seis páginas de conteúdo denso e específico.

## A home heliocêntrica

O Sol é a pessoa e a obra do Magru. Os seis planetas em órbita são as áreas do acervo: Literatura, Ensaios, História, Imprensa, Artes e Blog.

Os planetas são elementos `<a>` dentro de um `<nav>`, posicionados por `transform: rotate()` e animados por `@keyframes` em CSS. Nada de canvas, nada de biblioteca. O crawler e o leitor de tela encontram uma lista de links comum; o visitante vê um sistema solar. Abaixo da órbita, a mesma navegação aparece como cards, sempre visível e nunca escondida atrás da animação.

No celular a órbita reduz de tamanho e os cards assumem o papel principal de navegação. `prefers-reduced-motion: reduce` congela toda a rotação.

Cada área tem uma cor de planeta própria, que reaparece como acento na página interna correspondente — é o fio que liga a home às seções.

Além dos planetas, a home traz atalhos para os destinos externos que já existem hoje: Fotos no Flickr, Itajaipedia, canal do WhatsApp, grupo do Telegram e Facebook.

## Páginas de acervo

Cada página lista suas obras como cards. Cada card tem título, descrição enriquecida e link direto para o PDF no host do WordPress. O inventário completo — 34 obras com texto original e URL de PDF — está em `inventario-obras.json`, neste mesmo diretório.

O host dos PDFs fica numa única constante, para que a troca de `blog.magru.com.br` por outro endereço seja uma edição em um lugar só.

Duas famílias de caminho legado convivem e ambas precisam ser preservadas:

- `/web/wp-content/uploads/AAAA/MM/arquivo.pdf` — 17 arquivos, de 2017 a 2026
- `/wp/wordpress/wp-content/uploads/2015/01/arquivo.pdf` — 17 arquivos, todos de 2015

## Identidade visual

- Fundo azul-noite profundo `#0B0E14`, com gradiente radial sugerindo a coroa solar.
- Sol em gradiente âmbar para coral.
- Texto em branco quente `#E8E6E1`.
- Seis cores de planeta, uma por área, todas com contraste AA sobre o fundo.
- Tipografia de display: Fraunces, variável, carregada do Google Fonts com `font-display: swap`. Corpo em `system-ui`, sem requisição adicional.
- Escala tipográfica fluida com `clamp()`. Layout em CSS Grid nativo. Media queries só onde o grid não resolve sozinho.

## SEO

- `lang="pt-BR"`, um `<h1>` por página, hierarquia de headings correta.
- `<title>` e meta description únicos por página, escritos com as palavras-chave reais do acervo: Itajaí, Santa Catarina, história regional, poesia, imprensa, xilogravura.
- `rel="canonical"` em todas as páginas.
- Open Graph e Twitter Card para compartilhamento.
- JSON-LD: `Person` para Magru Floriano na home e no currículo, `Book` ou `CreativeWork` para cada obra, `BreadcrumbList` nas páginas internas.
- `sitemap.xml` com as sete URLs e `robots.txt` apontando para ele.
- Links para PDF com `type="application/pdf"` e texto âncora descritivo, nunca "clique aqui".

## Direitos de uso

Os livros são de download e leitura livres, e podem ser usados para fins educacionais e jornalísticos desde que citada a fonte. Os direitos de reprodução, alteração e comercialização são reservados ao autor.

A condição aparece em três lugares: no rodapé de todas as páginas, num aviso logo acima da lista de obras em cada seção — onde a pessoa está prestes a baixar — e nos metadados estruturados de cada livro, em `copyrightHolder`, `copyrightNotice` e `isAccessibleForFree`.

## Acessibilidade

- Contraste AA em todo texto.
- Foco visível em todos os elementos interativos.
- A órbita é navegável por teclado porque seus planetas são links reais.
- A lista textual de navegação está sempre no DOM, independente da animação.
- `prefers-reduced-motion` respeitado.

## Performance

Sem framework e sem build, o custo da página é o HTML, um CSS, um JS pequeno e uma fonte. A meta é LCP abaixo de 1,5 s em 4G e nenhum layout shift — o Sol e os planetas têm dimensões declaradas.

## JavaScript

O único comportamento que exige JS é o menu de navegação no celular. A órbita é CSS. Se o JS falhar, o site continua inteiramente navegável.

## Verificação

- Um HTML válido por página, conferido no validador do W3C.
- Os 34 links de PDF conferidos por requisição HTTP, confirmando status 200 no novo host.
- Lighthouse em modo mobile nas sete páginas.
- Teste manual de navegação por teclado na home.

## Fora de escopo

- Migração do blog: continua no WordPress, em `blog.magru.com.br`.
- Redirecionamentos dos links antigos — decisão explícita do usuário.
- Busca no site, comentários, newsletter, analytics.
