# Python Basico

## Que es un algoritmo?

Serie de pasos ordenados para resolver un problema, siendo esete finito y no es ambiguo lo cual tiene un proceso especifico.



## Operadores aritméticos

Primero, para iniciar la consola interactiva de Python debemos escribir el comando **py **en Windows, pero en otros sistemas el comando es python3. Ahora, podemos comenzar. En la consola nos permite escribir operaciones matemáticas como 5 + 5 sin escribir nada más, pero en el editor de código debemos “imprimir” el resultado, de la siguiente manera: print(5 + 5). Con esto obtendremos el resultado. Ahora veamos como se realiza cada operación aritmética:

**PEMDAS:** Parentesis, exponentes, multiplicación, división, adicción y substración

- Suma: 5 + 5
- Resta: 5 - 5
- Multiplicación: 5 * 5
- División (con decimales): 5 / 5
- División (sin decimales): 21 // 5
- Resto de la división: 21 % 5
- Potencia: 2 ** 2
- Raíz cuadrada: math.sqrt(9)     

```
>>>math.sqrt(9)     
 3.0
 
>>>math.sqrt(11.11)   }
 3.3331666624997918

>>>math.sqrt(Decimal('6.25'))     
 2.5
 ```

Python respeta la separaciónde términos, por lo que si escribimos 5 + 5 * 2 multiplicará primero 5 x 2. 

En el caso deque quisiéramos que primero sume 5 + 5 ponemos paréntesis: 

```
(5 + 5) * 2
```

## Variables

En programación, una variable es una especie de caja que contiene datos (números, texto) que posee un identificador (nombre de la variable). Estas se pueden usar para múltiples cosas y hay unas reglas que seguir:

- El identificador de mi variable no puede comenzar con un número, debe estar en minúsculas y las palabras de l mismo se separan con un guión bajo(_).
- Las variables tampoco pueden llevar los nombres que ya Python tiene reservado.

A continuación, un ejemplo:

```
var presente = 2020
var pasado = 1920
var diferencia_de_años = presente - pasado
diferencia de años = 80
```
*Las variables guardan todos los datos que les atribuyas.*

*El "=" sirve para atribuir algo, no significa igualdad.*