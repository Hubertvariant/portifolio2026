let frutas = ["maça", "banana", "laranja"];

console.log(frutas);
console.log(frutas.length);
console.log("="*30);

frutas.push("manga");
console.log(frutas)
console.log(frutas.length);

frutas.pop();
frutas.pop();
frutas.pop();
frutas.pop();
console.log(frutas)
console.log(frutas.length);

frutas.push('uva')
frutas.push('amora')
frutas.push("mixirica","abacate","abacaxi")
console.log(frutas)
console.log(frutas.length);

console.log(frutas[1])
console.log("O total de registro é de",frutas.length)

frutas.unshift("cereja")
console.log(frutas)
console.log(frutas.length)
   