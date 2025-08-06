#include <iostream>
#include <cmath>
#include <string>

int main() {
    int num1, num2;
    char operador;
    std::cout << "Ingrese primer numero: ";
    std::cin >> num1;
    std::cout << "Ingrese segundo numero: ";
    std::cin >> num2;
    std::cout << "Elija operacion (+, -, *, /, %): ";
    std::cin >> operador;
    switch (operador) {
        case '+':
            std::cout << "Resultado : " << num1 + num2 << std::endl;
            break;
            
        case '-':
            std::cout << "Resultado : " << num1 - num2 << std::endl;
            break;
        
        case '*':
        std::cout<< "Resultado : " << num1 * num2 << std::endl;
        break;

        case '/':
        std::cout << "Resultado : "<<num1 / num2 << std::endl;
        break;

        case '%':
    if (num2 != 0) {
        std::cout << "Resultado: " << num1 % num2 << std::endl;
    } else {
        std::cout << "No se puede dividir por cero !!!" << std::endl;
    }
    break;
    }


    return 0;
}