function taboada() {
    let numtab = document.getElementById('numtaboada').value
    let res = document.getElementById('res')
    res.innerHTML = ''
    if (numtab.length == 0){
        res.innerHTML = 'Digite um numero para calcular a taboada'
    } else {
        for (let c = 0; c <= 10; c++){
            let paragraf = document.createElement('p')
            let txt = document.createTextNode(`${numtab} X ${c} = ${numtab*c}`)
            paragraf.appendChild(txt)
            res.appendChild(paragraf)
        }
    }
}