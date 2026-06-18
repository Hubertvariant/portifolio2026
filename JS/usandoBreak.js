const ferramentas = ["martelo", "fita isolante", "chave", "alicate", "trena", "chave de fenda"]

for( let i = 0; i < ferramentas.length; i++){
    console.log("verificando: "+ ferramentas[i])
    if(ferramentas[i] === "chave"){
        console.log("chave encontrada. Parando a busca.")
        break
    }
}