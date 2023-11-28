function calcularSalario() {
    let salario = Number(document.getElementById(`salario`).value)
    let aumento = Number(document.getElementById(`aumento`).value)
    salario += salario * aumento/100
    document.getElementById(`resultadoSalario`).innerHTML = `O novo salário é de R$${salario.toFixed(2)}.`
}

function calcularTriangulo() {
    let base = document.getElementById(`base`).value
    let altura = document.getElementById(`altura`).value
    let area = (base * altura) / 2
    document.getElementById(`areaTriangulo`).value = `Área: ${area}.`
}

function calcularNota() {
    let nota1 = document.getElementById(`nota1`).value
    let nota2 = document.getElementById(`nota2`).value
    notaFinal = (nota1 * 0.3) + (nota2 * 0.7) / 1
    document.getElementById(`resultadoNota`).innerHTML = `A nota final é de: ${notaFinal.toFixed(0)}.`
}

function calcularIdade() {
    let anoNasc = document.getElementById(`nasc`).value
    let anoAtual = new Date().getFullYear()
    let idade = anoAtual - anoNasc
    let meses = idade * 12
    let dias = idade * 365
    let semanas = dias / 7
    let horas = dias * 24
    let minutos = horas * 60
    let idadeFutura = 2050 - anoNasc
    document.getElementById(`resultadoIdade`).innerHTML = `Resultado no console.`
    console.log(`Idade: ${idade}.\n Meses: ${meses}. \n Dias: ${dias}. \n Semanas: ${semanas.toFixed(0)}. \n Horas: ${horas}. \n Minutos: ${minutos}. \n Idade em 2050: ${idadeFutura}.`)
}

function consumoGasolina() {
    let distancia = document.getElementById(`distancia`).value
    let volume = document.getElementById(`volume`).value
    let consumo = distancia / volume
    document.getElementById(`consumoGasolina`).innerHTML = `O consumo médio é de ${consumo}.`
}

function calcularSalarioLiquido() {
    let salarioHR = document.getElementById(`salarioHR`).value
    let horasTrabalhadas = 62
    let horasNormais = salarioHR * 40
    let horasExtras = (horasTrabalhadas - 40) * salarioHR * 3
    let descontoRefeicao = (Math.ceil(62 / 8)) * 1.5
    let salarioBruto = horasNormais + horasExtras
    let salarioLiquido = horasNormais + horasExtras - descontoRefeicao
    document.getElementById(`salarioLiquido`).innerHTML = `O salário bruto é de R$${salarioBruto.toFixed(2)}.<br>O gasto em refeições foi de R$${descontoRefeicao.toFixed(2)}.<br>O salário líquido foi R$${salarioLiquido.toFixed(2)}.`
}

function numeroAleatorio() {
    const valor = Math.round(Math.random() * 1000) +1
    if (valor % 2 == 0) {
        document.getElementById(`numeroAleatorio`).innerHTML = `O número ${valor} é par.`
    }
    else {
        document.getElementById(`numeroAleatorio`).innerHTML = `O número ${valor} é impar.`
    }
}
