'use strict';

/**
 * navbar toggle
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
 * toggle navbar when click any navbar link
 */

const navbarLinks = document.querySelectorAll("[data-nav-link]");

for (let i = 0; i < navbarLinks.length; i++) {
  navbarLinks[i].addEventListener("click", function () {
    navbar.classList.remove("active");
  });
}


/**
 * header active when window scrolled down
 */

const header = document.querySelector("[data-header]");

window.addEventListener("scroll", function () {
  window.scrollY >= 50 ? header.classList.add("active")
    : header.classList.remove("active");
});




function openTab(tabName) {
  var i, tabContent;
  tabContent = document.getElementsByClassName("section-text");
  for (i = 0; i < tabContent.length; i++) {
    tabContent[i].style.display = "none";
  }
  document.getElementById(tabName + "Text").style.display = "block";
  
  var tabButtons = document.getElementsByClassName("tab-btn");
  for (i = 0; i < tabButtons.length; i++) {
    tabButtons[i].className = tabButtons[i].className.replace(" active", "");
    tabButtons[i].style.backgroundColor = "var(--platinum)"; // Resetting background color
  }
}

function openTab(tabName) {
  // Remove a classe 'active' de todos os botões
  var tabBtns = document.querySelectorAll('.tab-btn');
  tabBtns.forEach(function(btn) {
      btn.classList.remove('active');
  });

  // Adiciona a classe 'active' ao botão clicado
  var clickedBtn = document.querySelector('[onclick="openTab(\'' + tabName + '\')"]');
  clickedBtn.classList.add('active');

   // Oculta todos os textos
   var allTexts = document.querySelectorAll('.section-text');
   allTexts.forEach(function(text) {
       text.style.display = 'none';
   });

   // Mostra o texto correspondente ao botão clicado
   var selectedText = document.getElementById(tabName + 'Text');
   selectedText.style.display = 'block';
  
}



'use strict';

/** adiciona ouvinte de evento ao elemento */

const addEventonElem = function (elem, type, callback) {
    if (elem.length > 1) {
        for (let i = 0; i < elem.length; i++) {
            elem[i].addEventListener(type, callback);
        }
    } else {
        elem.addEventListener(type, callback);
    }
}



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



// Seleciona todos os elementos com a classe 'progress-value porcentagem da doação'
document.addEventListener('DOMContentLoaded', function() {
  // Seleciona todos os elementos com a classe 'progress-value'
  const progressValues = document.querySelectorAll('.progress-value');

  // Para cada elemento com a classe 'progress-value'
  progressValues.forEach(progress => {
      // Obtém o valor da porcentagem
      const percentage = parseInt(progress.getAttribute('value'));

      // Seleciona o elemento de barra de progresso associado a esse elemento de porcentagem
      const progressBar = progress.parentElement.nextElementSibling.querySelector('.progress');

      // Define a largura da barra de progresso com base na porcentagem
      progressBar.style.width = percentage + '%';
  });
});





//fazer com que o clique no link "Sobre" cause um efeito de rolagem suave até a seção "Sobre"//
document.getElementById('link-sobre').addEventListener('click', function(e) {
  e.preventDefault();
  document.getElementById('about').scrollIntoView({ behavior: 'smooth' });
});

//fazer com que o clique no link "Serviços" cause um efeito de rolagem suave até a seção "Serviços"//
document.getElementById('link-servicos').addEventListener('click', function(e) {
  e.preventDefault();
  document.getElementById('service').scrollIntoView({ behavior: 'smooth' });
});

//fazer com que o clique no link "Depoimentos" cause um efeito de rolagem suave até a seção "Depoimentos"//
document.getElementById('link-depoimentos').addEventListener('click', function(e) {
  e.preventDefault();
  document.getElementById('testimonial').scrollIntoView({ behavior: 'smooth' });
});

//fazer com que o clique no link "Doar" cause um efeito de rolagem suave até a seção "Doe"//
document.getElementById('link-doar').addEventListener('click', function(e) {
  e.preventDefault();
  document.getElementById('doacoes').scrollIntoView({ behavior: 'smooth' });
});

//fazer com que o clique no link "Sobre" cause um efeito de rolagem suave até a seção "Doe agora!" navbar//
document.addEventListener("DOMContentLoaded", function() {
  document.getElementById('doarBtn').addEventListener('click', function() {
      // Obter a posição da seção de doações
      var doacoesPos = document.getElementById('doacoes').offsetTop;
      
      // Animação de rolagem suave até a posição da seção de doações
      window.scrollTo({
          top: doacoesPos,
          behavior: 'smooth'
      });
  });
});

//fazer com que o clique no link "Sobre" cause um efeito de rolagem suave até a seção "Doe agora!" imgem de fundo//
document.addEventListener("DOMContentLoaded", function() {
  document.getElementById('doarBtn2').addEventListener('click', function() {
      // Obter a posição da seção de doações
      var doacoesPos = document.getElementById('doacoes').offsetTop;
      
      // Animação de rolagem suave até a posição da seção de doações
      window.scrollTo({
          top: doacoesPos,
          behavior: 'smooth'
      });
  });
});



