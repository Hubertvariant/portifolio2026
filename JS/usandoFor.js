import frutaLista from "./array.js"

"use strict"

let notas = [8, 7, 6, 9, 10]
let soma = 0

for (let i = 0; i < notas.length; i++){
    soma += notas[i]
}

let media = soma / notas.length
console.log("A media das notas é:",media)

console.log('='*30)

for (let i = 1; i <= 5; i++){
    console.log('contando', i)
}


console.log('='*30)
console.log('Tabuada')

for (let cont = 1; cont <= 10; cont++){
    console.log(`2 x ${cont} = ${2*cont}`)
}

console.log('=' * 30)

const frutas = ['banana', 'laranja', 'maca', 'pera']

for(const fruta of frutas){
    console.log(fruta)
}