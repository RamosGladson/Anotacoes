function carregar() {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var foto = window.document.getElementById('picture')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas`
    if (hora < 12){
        img.src = 'fotomanha.png'
        window.document.body.style.background = '#e2cd9f'
        //Foto de Artur Roman no Pexels
        foto.href = 'https://www.pexels.com/pt-br/foto/flor-petala-roxa-1167355/'
    } else if (hora < 18){
        img.src = 'fototarde.png'
        window.document.body.style.background = '#b9846f'
        //Foto de GEORGE DESIPRIS no Pexels
        foto.href = 'https://www.pexels.com/pt-br/foto/barco-navegando-no-corpo-d-agua-858241/'
    } else {
        img.src = 'fotonoite.png'
        window.document.body.style.background = '#515154'
        //Foto de Pixabay no Pexels
        foto.href = 'https://www.pexels.com/pt-br/foto/alvorecer-amanhecer-arvores-aurora-327308/'
    }
}
