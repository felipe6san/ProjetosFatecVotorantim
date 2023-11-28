document.getElementById(`cep`)
elemento.addEventListener (async function () {
    var validacep = [0-9];
    var api = `https://viacep.com.br/ws/${cep}/json/`;
        let resposta = await fetch(api);
            dados = await resposta.json();
            document.getElementById(`dados`).innerText = dados.cidade

})
function calcularIdade() {
    let idade = Number(document.getElementById(`idade`).value)
    let somaIdade = Number(document.getElementById(`idade`).value) + 30
    alert(`Idade é de ${somaIdade}`)    
}

function termos(){
    let aceito = (document.getElementById(`termos`).value)
    if (aceito = 1){
        alert(`Cadastrado com Sucesso`)
    }
    else {
        alert (`Erro`)
    }
}