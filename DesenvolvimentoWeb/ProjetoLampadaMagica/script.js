let lampada = document.getElementById(`lampada`);

function ligar (){
    lampada.src="luzLigada.gif"
}

function desligar(){
    lampada.src="luzDesligada.gif"
}

function alternar(){
    if (lampada.getAttribute("src") == "luzLigada.gif"){
        desligar();
    }
    else if (lampada.getAttribute("src") == "luzDesligada.gif"){
        ligar();
    }
}

function sumir(){
        lampada.hidden = true;
        document.getElementById("titulo").style.color = "red";
}

function aparecer(){
        lampada.hidden = false;
        document.getElementById("titulo").style.color = "blue";
}

function piscar(){
        alternar()
        
} 
setInterval(piscar, 500);