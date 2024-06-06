'use strict';

/**
 * alternância da barra de navegação
 */

const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbar = document.querySelector("[data-navbar]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");

const navElemArr = [navOpenBtn, navCloseBtn];

for (let i = 0; i < navElemArr.length; i++) {
  navElemArr[i].addEventListener("click", function () {
    navbar.classList.toggle("active");
  });
}

/**
 * alternar a barra de navegação ao clicar em qualquer link da barra de navegação
 */

const navbarLinks = document.querySelectorAll("[data-nav-link]");

for (let i = 0; i < navbarLinks.length; i++) {
  navbarLinks[i].addEventListener("click", function () {
    navbar.classList.remove("active");
  });
}

/**
 * cabeçalho ativo quando a janela rola para baixo
 */

const header = document.querySelector("[data-header]");

window.addEventListener("scroll", function () {
  window.scrollY >= 50 ? header.classList.add("active")
    : header.classList.remove("active");
});

// DEIXAR O MENU PÁGINAS MAIS SUAVE NA EXIBIÇÃO//

// Selecione o menu de páginas e seu submenu
const menuPaginas = document.querySelector('header ul li.has-submenu');
const submenu = document.querySelector('.submenu');

// Adicione um ouvinte de evento para quando o mouse entrar no item do menu de páginas
menuPaginas.addEventListener('mouseenter', function() {
    // Posicione o submenu abaixo do item "Páginas"
    const rect = menuPaginas.getBoundingClientRect();
    submenu.style.display = 'block';
    submenu.style.left = rect.left + 'px';
    submenu.style.top = rect.bottom + 'px';

    // Ajuste a altura do submenu gradualmente
    submenu.style.height = '0px'; // Comece com uma altura de 0
    let height = submenu.scrollHeight; // Altura total do submenu
    submenu.style.height = height + 'px'; // Ajuste a altura para a altura total com animação
});

// Adicione um ouvinte de evento para quando o mouse sair do item do menu de páginas
menuPaginas.addEventListener('mouseleave', function() {
    // Oculte o submenu
    submenu.style.height = '0px'; // Reduza a altura para 0 com animação
    // Defina um atraso para garantir que a animação seja concluída antes de ocultar o submenu
    setTimeout(function() {
        submenu.style.display = 'none'; // Oculte o submenu após a animação
    }, 300); // Ajuste o atraso conforme necessário (300ms é o mesmo tempo de duração da animação)
});


document.addEventListener('DOMContentLoaded', function () {
    // Verifica se a página está na seção Entre em contato
    if (window.location.href.includes("contato")) {
        // Adiciona um ouvinte de evento de clique ao link "Sobre" no menu
        document.getElementById('link-sobre').addEventListener('click', function (event) {
            // Previne o comportamento padrão do link
            event.preventDefault();
            // Redireciona para a tela index.html
            window.location.href = "index.html";
            // Aguarda um pequeno atraso para garantir que a página index.html seja carregada
            setTimeout(function () {
                // Obtém a posição vertical do elemento "Sobre" e rola até ele
                var sobreElement = document.getElementById('about');
                if (sobreElement) {
                    sobreElement.scrollIntoView({ behavior: 'smooth' });
                }
            }, 500);
        });
    }
});