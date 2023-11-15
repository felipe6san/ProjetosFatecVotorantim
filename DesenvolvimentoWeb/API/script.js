elemento = document.getElementById("pesquisa");

elemento.addEventListener('click', async function () {
    document.getElementById('resultado').innerText = ""
    var valor = document.getElementById("cep").value
    if (valor == '')
        alert("Informe o CEP");
    else {
        var cep = valor.replace(/\D/g, '');
        var validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            var api = `https://viacep.com.br/ws/${cep}/json/`;
            let resposta = await fetch(api);
            dados = await resposta.json();
            console.log(dados);
            if (dados.erro)
                document.getElementById('resultado').innerText = "CEP Não Existe";
            else
                document.getElementById('resultado').innerText = "Logradouro: " + dados.logradouro + " " + "Bairro: " + dados.bairro + " " + "Cidade: " + dados.localidade + " " + "UF: " + dados.uf + " " + "DDD: " + dados.ddd


        }
        else
            //if (!(resposta.ok))
            alert("cep inválido");
    }
})