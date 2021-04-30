var idade = 58
if (idade < 16){
    console.log('Não vota')
} else {
    if (idade < 18){
        console.log('Voto opcional')
    } else{
        if (idade < 60){
            console.log('Voto obrigadório')
        } else{
            console.log('Voto opcional maior de 60')
        }

    }
}