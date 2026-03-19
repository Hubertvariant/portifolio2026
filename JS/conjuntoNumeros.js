function Media(numeros){
    let soma = 0
    for(let i = 0; i < numeros.length; i++){
        soma += numeros[i]
    }
    return soma / numeros.length
}

console.log(Media([10,20,30]))

