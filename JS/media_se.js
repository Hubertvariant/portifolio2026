let aluno = "Robson";
let n1 = 99;
let n2 = 100;
let n3 = 99;
let n4 = 100;
let media = 0;
let result= "";
media = (n1 + n2 + n3 + n4) / 4;
if (media >= 70) {
    result = "Aprovado";
} 
else {
    result = "Reprovado";
}
console.log("A media do aluno", aluno, "é:", media);
console.log(result);