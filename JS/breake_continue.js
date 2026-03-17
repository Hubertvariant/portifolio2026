let carros_estcionados = 0
const limitemaxiomo = 7
console.log('---iniciando verificação vagas---')
for (let vagas = 1; vagas <= limitemaxiomo; vagas++) {
    if(vagas===4 || vagas===7 || vagas===3){
        console.log(`vaga ${vagas}:[interditada]-pulando...`)
        continue
    }
    carros_estcionados++
    console.log(`vaga ${vagas}:[ocupada]-carros estacionados ${carros_estcionados}`)
    if(carros_estcionados===limitemaxiomo){
        console.log('---limite atingido! fechar portão---')
        break
    }
    console.log('---relatório encerrado---')
}