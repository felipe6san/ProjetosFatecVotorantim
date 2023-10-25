let valorPacote;
let adicionais;
let totalFinal;

function calcularTotalViagem() {
    calcularPacotes();
    calcularAdicionais();
    console.log(adicionais)
    totalFinal = valorPacote + adicionais;
    alert(`O Total da viagem é de R$${totalFinal}.`)
}
function calcularAdicionais() {
    adicionais = 0;
    let adicional = document.querySelectorAll("input[type='checkbox']");
    for (let i = 0; i < adicional.length; i++) {
        if (adicional[i].checked) {
            //console.log(adicional[i].value);
            adicionais += Number(adicional[i].value);
        }
    }
}
function calcularPacotes() {
    valorPacote = 0
    let qntPacotes = document.querySelectorAll("input[name='pacotes']").length
    let pacotes = document.querySelectorAll("input[name='pacotes']");
    for (let i = 0; i < qntPacotes; i++) {
        if (pacotes[i].checked == true) {
            console.log(pacotes[i].value);
            valorPacote = Number(pacotes[i].value);
            break;
        }
    }
}