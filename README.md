# Universo do Magru

Site estático da obra de Magru Floriano — HTML, CSS e JavaScript puro, sem build e sem dependências. Hospedado no GitHub Pages em `magru.com.br`.

O blog e os arquivos PDF continuam no WordPress, em `blog.magru.com.br`.

## Estrutura

```
index.html          home, com o diagrama orbital
curriculo/          currículo completo
literatura/         12 obras          ensaios/     8 obras
historia/            8 obras          imprensa/    4 obras
artes/               2 obras
404.html
assets/css/magru.css
assets/js/magru.js
assets/favicon.svg
sitemap.xml  ·  robots.txt  ·  CNAME
```

Para editar qualquer página, abra o `.html` e escreva. Não há passo de compilação. O cabeçalho e o rodapé estão repetidos nos oito arquivos: mudou um, mude os outros.

## Ver o site na sua máquina

Dê dois cliques no `index.html`. Todos os caminhos são relativos, então o site renderiza e navega direto do disco, sem servidor — e pela mesma razão funciona tanto na raiz de um domínio quanto num subcaminho como `thiagofloriano.github.io/pages-magru/`.

Se preferir um servidor:

```bash
python3 -m http.server 8777
```

Os links internos apontam para `pasta/index.html` em vez de `pasta/`, que é o que faz a navegação funcionar no `file://`. As URLs limpas continuam sendo as canônicas: cada página declara `rel="canonical"` para `https://magru.com.br/secao/`, e é essa que o sitemap lista e o Google indexa.

## Publicar

1. Em Settings → Pages do repositório, escolha "Deploy from a branch", branch `main`, pasta `/`.
2. Ainda em Pages, no campo de domínio personalizado, coloque `magru.com.br`. O arquivo `CNAME` já está no repositório.
3. No DNS do domínio, aponte `magru.com.br` para o GitHub Pages: quatro registros A para `185.199.108.153`, `185.199.109.153`, `185.199.110.153` e `185.199.111.153`, e um CNAME de `www` para `<usuário>.github.io`.
4. Marque "Enforce HTTPS" quando o certificado sair.

## Antes de trocar o DNS

O WordPress precisa estar respondendo em `blog.magru.com.br`, com a árvore de arquivos intacta — tanto `/web/wp-content/uploads/` quanto `/wp/wordpress/wp-content/uploads/`. Os 34 links de PDF deste site apontam para lá.

Os endereços antigos, em `magru.com.br/web/...`, vão parar de funcionar assim que o DNS mudar. Foi uma decisão consciente; se um dia quiser recuperá-los, o caminho é um redirecionamento 301 no servidor do WordPress.

## Trocar o host dos PDFs

O endereço está escrito nos links de cada página. Para mudar todos de uma vez:

```bash
grep -rl 'blog.magru.com.br' --include='*.html' . | xargs sed -i 's|blog\.magru\.com\.br|NOVO.HOST|g'
```

## Direitos de uso

Os livros podem ser baixados, lidos e usados para fins educacionais e jornalísticos, desde que citada a fonte. Os direitos de reprodução, alteração e comercialização são reservados ao autor.

O texto aparece no rodapé de todas as páginas, num aviso acima da lista de obras em cada seção, e nos metadados estruturados de cada livro (`copyrightHolder`, `copyrightNotice`, `isAccessibleForFree`). Se mudar, mude nos três lugares.

## Adicionar uma obra

Copie um bloco `<li class="obra">` dentro da seção certa e troque título, descrição, ficha bibliográfica e o link do PDF. O tamanho do arquivo no texto do link é informação útil para quem está no celular — vale atualizar.

## Design

O tema é o heliocentrismo desenhado como carta celeste gravada: o Sol é o autor, as seis áreas do acervo são os planetas. Os anéis são hairlines de um traço, o fundo tem um estipulado de gravura, e a esfera inteira gira num período único para que os planetas nunca se alcancem. `prefers-reduced-motion` congela tudo.

O diagrama é navegação de verdade: cada planeta é um `<a>`. No celular os rótulos ficam disponíveis para leitor de tela e teclado, e os pontos servem de alvo — seis nomes girando não cabem em 390 px.

A decisão completa está em `docs/superpowers/specs/2026-09-15-site-heliocentrico-design.md`.
