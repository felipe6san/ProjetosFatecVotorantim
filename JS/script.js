elemento = document.getElementById("pesquisa");
pesquisaClima = document.getElementById("pesquisaClima");

// pesquisa clima - botão lupa
// adicionado o evento da pesquisa ao clicar, puxando a função abaixo. A função deve ser assincrona. SEMPRE ABRE E FECHA OS PARENTESES.
pesquisaClima.addEventListener('click', async function () {

    // pega o valor dentro do input cidade
    cidade = document.getElementById("cidade").value;
    // as funções dentro do url variam conforme o resultado esperado. path do api de clima
    const apiClimaURL = `https://api.openweathermap.org/data/2.5/weather?q=${cidade}&units=metric&appid=${apiKey}&lang=pt_br`;
    // requisição dentro do path da api. DEVE SER AWAIT (pois espera para retornar o resultado) e fetch 
    let respostaClima = await fetch(apiClimaURL)
    // tranforma a resposta que esta em json em js
    let objdados = await respostaClima.json()
    if (objdados.cod === "404") {
        alert("Cidade Inválida")
    }
    else {
        // pega a temp/humidity/wind.speed que esta dentro do objeto "objdados" e guarda nas variáveis
        let temperatura = parseFloat(objdados.main.temp) + "º"; //&deg;C
        let humidade = parseFloat(objdados.main.humidity) + "%";
        let vento = parseFloat(objdados.wind.speed) + "km/h";
        let descricao = objdados.weather[0].description;
        // traz o retorno escrevendo em um p do html
        document.getElementById('resultado').innerText = `Hoje está ${temperatura} -  ${descricao} - ${humidade} - ${vento}`
    }
})

// pesquisa CEP - botão pesquisar
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
                document.getElementById('resultado').innerText = dados.logradouro + ", " + dados.bairro + " - " + dados.localidade + ", " + dados.uf
        }
        else
            if (!(resposta.ok))
                alert("cep inválido");
    }
}
)

// apiKey = digite sua API Key aqui