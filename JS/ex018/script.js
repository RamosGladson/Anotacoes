let num = document.getElementById('numero')
let lista = document.querySelector('select#lista')
let res = document.querySelector('div#res')
let valores = []

function ehNumero(num) {
    if (num >= 1 && num <= 100) {
        return true
    } else {
        return false
    }
}

function naLista(num, lista){
    if (lista.indexOf(num) != -1) {
        return true
    } else{
        return false
    }
}

function adicionar(){
    if (ehNumero(Number(num.value)) && !naLista(Number(num.value), valores)){
        res.innerHTML = ''
        valores.push(Number(num.value))
        let item = document.createElement('option')
        let text = document.createTextNode(`Você adicionou o Nº ${num.value}`)
        item.appendChild(text)
        lista.appendChild(item)
    } else{
        alert('dados inválidos')
    }
    num.value = ''
    num.focus()
}

function finalizar(){
    if (valores.length == 0){
        alert('Adicione primeiro')
    } else{
        let menor = valores[0]
        let maior = valores[0]
        let soma = 0
        for(pos in valores){
            if (valores[pos] < menor){ 
                menor = valores[pos]
            }
            if (valores[pos] > maior){
                maior = valores[pos]
            }
            soma += valores[pos]
        }
        res.innerHTML = ''
        res.innerHTML += `<p>Você digitou ${valores.length} números</p>`
        res.innerHTML += `<p>O menor é ${menor}</p>`
        res.innerHTML += `<p>O maior é ${maior}</p>`
        res.innerHTML += `<p>A soma é ${soma}</p>`
        res.innerHTML += `<p>A média é ${soma/valores.length}</p>`
    }
}