// Único comportamento que exige JavaScript: abrir e fechar a navegação no celular.
// Sem JS, a lista fica visível e o site continua inteiramente navegável.

const botao = document.querySelector(".menu-botao");
const rota = document.getElementById("rota");

if (botao && rota) {
  rota.hidden = true;
  botao.hidden = false;
  botao.setAttribute("aria-expanded", "false");

  botao.addEventListener("click", () => {
    rota.hidden = !rota.hidden;
    botao.setAttribute("aria-expanded", String(!rota.hidden));
  });
}
