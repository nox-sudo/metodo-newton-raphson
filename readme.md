# Método de Newton-Raphson para encontrar raíces de funciones

Este repositorio contiene la implementación del método numérico de Newton-Raphson para encontrar raíces de funciones. El proyecto es parte de la evaluación del curso de Métodos Numéricos.

## Descripción del método

El método de Newton-Raphson es un algoritmo iterativo para encontrar aproximaciones a las raíces (o ceros) de una función real. Utiliza la primera derivada de la función para construir aproximaciones sucesivas a la raíz.

La fórmula iterativa del método es:

```
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
```

donde:
- x_n es la aproximación actual
- f(x_n) es el valor de la función en el punto x_n
- f'(x_n) es el valor de la derivada de la función en el punto x_n

El método converge cuadráticamente cuando la función es suficientemente suave cerca de la raíz y la derivada no se anula en la raíz.

## Características del programa

- Implementación completa del método de Newton-Raphson
- Cálculo automático de la derivada utilizando SymPy
- Visualización gráfica de la función y la convergencia del método
- Resultados paso a paso de cada iteración
- Manejo de errores y verificación de convergencia

## Requisitos

Para ejecutar este programa necesitarás:

- Python 3.6 o superior
- Las siguientes bibliotecas de Python:
  - NumPy
  - Matplotlib
  - SymPy

Puedes instalar todas las dependencias con el siguiente comando:

```bash
pip install numpy matplotlib sympy
```

## Instrucciones de uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/[tu-usuario]/metodo-newton-raphson.git
   cd metodo-newton-raphson
   ```

2. Ejecuta el programa:
   ```bash
   python metodo_newton_raphson.py
   ```

3. Sigue las instrucciones en pantalla:
   - Ingresa la función para la cual deseas encontrar la raíz (usando sintaxis de Python)
   - Proporciona un valor inicial para comenzar las iteraciones
   - Opcionalmente, ajusta la tolerancia y el número máximo de iteraciones
   - Define los límites para visualizar la gráfica

## Ejemplo de uso

```
Ingrese la función f(x): x**2 - 4
La derivada calculada es: 2*x

Ingrese el valor inicial (x0): 3

¿Desea usar valores por defecto para tolerancia (1e-6) y máximo de iteraciones (100)? (s/n): s

RESULTADOS DEL MÉTODO DE NEWTON-RAPHSON
=======================================

Iteraciones paso a paso:
----------------------------------------------------------------------
 Iteración  |       x_i       |     f(x_i)      |      Error      
----------------------------------------------------------------------
     1      |    3.00000000   |    5.00000000   |    0.83333333   
     2      |    2.16666667   |    0.69444444   |    0.16025641   
     3      |    2.00641026   |    0.02566694   |    0.00640026   
     4      |    2.00001000   |    0.00004000   |    0.00001000   
     5      |    2.00000000   |    0.00000000   |    0.00000000   

Resultado Final:
------------------------------------------------------------
Estado: El método CONVERGIÓ en 5 iteraciones
Aproximación de la raíz: 2.0000000000
Valor de la función en la raíz: 0.0000000000
------------------------------------------------------------
```

## Implementación y visualización

El programa incluye:
- Una función principal para el método de Newton-Raphson
- Manejo de errores para casos de no convergencia
- Visualización gráfica que muestra:
  - La función y la raíz encontrada
  - La convergencia del método (error vs. iteraciones)

![Ejemplo de visualización](newton_raphson_resultados.png)

## Contribuir

Si deseas contribuir a este proyecto, por favor:
1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Autor

Andrew Tran

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.