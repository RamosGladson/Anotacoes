function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = window.document.getElementById('txtano').value
    var res = window.document.getElementById('res')
    if (fano.length == 0 || fano > ano) {
        window.alert('[Erro] Verifique os dados e tente novamente')
    } else{
        var fsex = window.document.getElementsByName('radsex')
        var idade = ano - fano
        var genero = ''
        var imagem = document.createElement('img')
        imagem.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            genero = 'homem'
            if (idade <= 10) {
                //criança
                //Foto de Denafi Sy no Pexels
                //https://www.pexels.com/pt-br/foto/crianca-de-short-cinza-sentada-na-estrada-786220/
                imagem.setAttribute('src', '_imagens/meninobb.png')
            } else if (idade <= 30) {
                //jovem
                //Foto de Andres Ayrton no Pexels
                //https://www.pexels.com/pt-br/foto/ativo-movimentado-atleta-esportista-6551136/
                imagem.setAttribute('src', '_imagens/homemjovem.png')
            } else if (idade <= 60) {
                //adulto
                //Foto de Andrea Piacquadio no Pexels
                //https://www.pexels.com/pt-br/foto/homem-em-fotografia-de-moletom-com-gola-redonda-941693/
                imagem.setAttribute('src', '_imagens/homem.png')
            } else {
                //senhor
                //Foto de Andrea Piacquadio no Pexels
                //https://www.pexels.com/pt-br/foto/homem-sentado-na-cadeira-ao-lado-da-mesa-834863/
                imagem.setAttribute('src', '_imagens/senhor.png')
            }

        } else if (fsex[1].checked) {
            genero = 'mulher'
            if (idade <= 10){
                //criança
                //Foto de Singkham no Pexels
                //https://www.pexels.com/pt-br/foto/bebe-sentado-na-grama-ao-lado-do-urso-de-pelucia-durante-o-dia-1166473/
                imagem.setAttribute('src', '_imagens/meninabb.png')
            } else if (idade <= 30) {
                //jovem
                //Foto de Gabb Tapic no Pexels
                //https://www.pexels.com/pt-br/foto/mulher-usando-minivestido-branco-3568546/
                imagem.setAttribute('src', '_imagens/mulherjovem.png')
            } else if (idade <= 60) {
                //mulher
                //Foto de Pixabay no Pexels
                //https://www.pexels.com/pt-br/foto/fotografia-de-mulher-em-tons-de-cinza-276064/
                imagem.setAttribute('src', '_imagens/mulher.png')
            } else {
                //senhora
                //Foto de Nashua Volquez-Young no Pexels
                //https://www.pexels.com/pt-br/foto/mulher-usando-chapeu-vermelho-e-oculos-de-sol-1729931/
                imagem.setAttribute('src', '_imagens/senhora.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos`
        res.appendChild(imagem)
    }
}