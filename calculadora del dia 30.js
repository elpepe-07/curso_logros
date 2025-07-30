let ask = prompt("¿Qué quieres hacer? (suma, resta, multiplicación, división ,exponenciar, sacar modulo o calcular raiz : ):");
if (ask === "suma") {
    let num1 = Number(prompt("Introduce el primer número:"));
    let num2 = Number(prompt("Introduce el segundo número:"));
    console.log(`La suma de ${num1} y ${num2} es: ${num1 + num2}`);
} else if (ask === "resta") {
    let num1 = Number(prompt("Introduce el primer número:"));
    let num2 = Number(prompt("Introduce el segundo número:"));
    console.log(`La resta de ${num1} y ${num2} es: ${num1 - num2}`);
} else if (ask === "multiplicación") {
    let num1 = Number(prompt("Introduce el primer número:"));
    let num2 = Number(prompt("Introduce el segundo número:"));
    console.log(`La multiplicación de ${num1} y ${num2} es: ${num1 * num2}`);
} else if (ask === "división") {
    let num1 = Number(prompt("Introduce el primer número:"));
    let num2 = Number(prompt("Introduce el segundo número:"));
    if (num2 !== 0) {
        console.log(`La división de ${num1} y ${num2} es: ${num1 / num2}`);
    } else {
        console.log("No se puede dividir por cero.");
    }
} else if (ask === "exponenciar") {
    let base = Number(prompt("Introduce la base:"));
    let exponente = Number(prompt("Introduce el exponente:"));
    console.log(`El resultado de ${base} elevado a ${exponente} es: ${base ** exponente}`);
}
else if (ask === "sacar modulo") {
    let num1 = Number(prompt("Introduce el primer número:"));
    let num2 = Number(prompt("Introduce el segundo número:"));
    console.log(`El módulo de ${num1} y ${num2} es: ${num1 % num2}`);
}
else if (ask === "calcular raiz") {
    let num = Number(prompt("Introduce el número para calcular su raíz cuadrada:"));
    if (num >= 0) {
        console.log(`La raíz cuadrada de ${num} es: ${num ** 0.5}`);
    } else {
        console.log("No se puede calcular la raíz cuadrada de un número negativo.");
    }
}

