let combo;
let adicionais;
let valorEntrega;

function calcularTotal() {
    calcularLanche();
    calcularAdicionais();
    calcularEntrega();
    totalCombo = combo + adicionais + valorEntrega;
    nome = document.getElementById("nomeCliente").value
    document.getElementById("totalPagar").value = `Total a pagar é de: R$${totalCombo}`
    document.getElementById("descricaoPedido").value = `${nome} Seu combo custará ${combo}R$ com ${adicionais}R$ de adicionais e ${valorEntrega}R$ de taxa de entrega!!!`
}

function calcularLanche() {
    combo = Number(document.getElementById("combos").value);
}

function calcularAdicionais() {
    adicionais = 0;
    let adicional = document.querySelectorAll("input[type='checkbox']");
    for (let i = 0; i < adicional.length; i++) {
        if (adicional[i].checked) {
            adicionais += Number(adicional[i].value);
        }
    }
}
function calcularEntrega() {
    let entrega = document.querySelectorAll("input[type='radio']");
    for (let i = 0; i < entrega.length; i++) {
        if (entrega[i].checked) {
            valorEntrega = Number(entrega[i].value);
            break
        }
    }



}