function calcularDesconto()
{
    let qntPacotes = document.querySelectorAll("input[name='pacotes']").length
    console.log(qntPacotes);
    let pacotes = document.querySelectorAll("input[name='pacotes']");
    console.log(pacotes);
    for(let i= 0; i < qntPacotes; i++){
        console.log(pacotes[i].value)

    }
    //window.alert("Calculando...");
    //document.getElementById('nome').value;
    //document.querySelectorAll("input[name='pacotes']:checked")
}
