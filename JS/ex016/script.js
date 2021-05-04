function contar() {
    var inicio = document.getElementById('inicio').value
    var fim = document.getElementById('fim').value
    var passo = document.getElementById('passo').value
    var res = document.getElementById('res')
    res.innerHTML = 'Contando... '
    if (inicio.length == 0 || fim.length == 0 || passo.length == 0) {
        res.innerHTML = '[ERRO] Faltam dados'
    } else {
        if (passo < 0) {
            passo = passo  * (-1)
        }
        if (passo == 0) {
            passo = 1
        }
        if (inicio > fim ){
            for(var i = Number(inicio); i>=Number(fim); i -= Number(passo)){
                res.innerHTML += i + ' '
            }
        }
        if (inicio < fim) { 
            for(var i = Number(inicio); i<=Number(fim); i += Number(passo)){
                res.innerHTML += i + ` \u{1f449} `
        }
        res.innerHTML += `\u{1f3c1}`
        
        }
    }

}