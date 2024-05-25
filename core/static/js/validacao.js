document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("payment-form").addEventListener("submit", function(event) {
        // Impede o envio padrão do formulário
        event.preventDefault();

        // Validar o campo de e-mail
        var emailInput = document.getElementById("email");
        var email = emailInput.value.trim();
        if (!validateEmail(email)) {
            alert("Por favor, insira um endereço de e-mail válido.");
            emailInput.focus();
            return false;
        }

        // Remover "-" do campo de CEP
        var cepInput = document.getElementById("cep");
        var cep = cepInput.value.trim().replace(/-/g, "");
        
        // Validar o campo de CEP
        if (!validateCEP(cep)) {
            alert("Por favor, insira um CEP válido com 8 dígitos.");
            cepInput.focus();
            return false;
        }

        // Validar o campo do ano de vencimento do cartão
        var anoVencInput = document.getElementById("ano-venc");
        var anoVenc = anoVencInput.value.trim();
        if (!validateAnoVencimento(anoVenc)) {
            alert("Por favor, insira um ano de vencimento válido com 4 dígitos.");
            anoVencInput.focus();
            return false;
        }

        // Validar o campo do CVV
        var cvvInput = document.getElementById("cvv");
        var cvv = cvvInput.value.trim();
        if (!validateCVV(cvv)) {
            alert("Por favor, insira um CVV válido com 3 dígitos.");
            cvvInput.focus();
            return false;
        }

        // Redireciona para validacaoconcluida.html
        window.location.href = "validacaoconcluida.html";
    });
});

// Função para validar o formato de e-mail
function validateEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Função para validar o formato do CEP
function validateCEP(cep) {
    var cepRegex = /^\d{8}$/;
    return cepRegex.test(cep);
}

// Função para validar o ano de vencimento do cartão
function validateAnoVencimento(anoVenc) {
    var anoVencRegex = /^\d{4}$/;
    return anoVencRegex.test(anoVenc);
}

// Função para validar o formato do CVV
function validateCVV(cvv) {
    var cvvRegex = /^\d{3}$/;
    return cvvRegex.test(cvv);
}
