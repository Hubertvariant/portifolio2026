const usuarios = [
    {nome: "carlos", idade: 32},
    {nome: "ana", idade: 28},
    {nome: "felipe", idade: 40}
]


const ana = usuarios.find(usuarios => usuarios.nome === "ana")
console.log(ana)

const usuariosAcimaDe30 = usuarios.filter(usuarios => usuarios.idade > 30)
console.log(usuariosAcimaDe30)

const usuariosOrdenadosPorIdade = usuarios.sort((a, b) => a.idade - b.idade)
console.log(usuariosOrdenadosPorIdade)