document.addEventListener("DOMContentLoaded", function() {
  const btn = document.querySelector(".btn2 button[type='submit']"); // Seleciona o botão "Publicar"
  const post = document.querySelector(".post");
  const widget = document.querySelector(".star-widget");
  const editBtn = document.querySelector(".edit");

  // Função para ocultar widget e exibir post
  const showPost = () => {
    widget.style.display = "none";
    post.style.display = "block";
  };

  // Função para exibir widget e ocultar post
  const showWidget = () => {
    widget.style.display = "block";
    post.style.display = "none";
  };

  // Adiciona evento de clique ao botão "Publicar"
  btn.addEventListener("click", () => {
    showPost(); // Chama a função para exibir post
  });

  // Adiciona evento de clique ao botão "Editar"
  editBtn.addEventListener("click", () => {
    showWidget(); // Chama a função para exibir widget
  });

  // Seleciona o botão "Voltar"
  const backBtn = document.querySelector("button[type='button']");

  // Adiciona evento de clique ao botão "Voltar"
  backBtn.addEventListener("click", () => {
    window.location.href = "index.html"; // Redireciona para index.html ao clicar em "Voltar"
  });
});
