"""
Método de Newton-Raphson para encontrar raíces de funciones

Este programa implementa el método numérico de Newton-Raphson para encontrar
las raíces de una función. El método utiliza la derivada de la función para
aproximar la raíz de manera iterativa.

Autor: Andrew Tran
Fecha: 10/05/2025
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, diff, lambdify
import os

def clear_screen():
    """Limpia la pantalla de la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def newton_raphson(f_expr, df_expr, x0, tol=1e-6, max_iter=100):
    """
    Implementación del método de Newton-Raphson para encontrar raíces de funciones.
    
    Parámetros:
    -----------
    f_expr : función lambdificada
        La función de la cual se busca la raíz
    df_expr : función lambdificada
        La derivada de la función
    x0 : float
        Valor inicial para comenzar la iteración
    tol : float
        Tolerancia para el criterio de parada (por defecto 1e-6)
    max_iter : int
        Número máximo de iteraciones permitidas (por defecto 100)
        
    Retorna:
    --------
    x : float
        La aproximación a la raíz
    iteraciones : list
        Lista de tuplas (iteración, valor_x, f(x), error)
    convergencia : bool
        True si el método convergió, False si no
    """
    x = x0
    iteraciones = []
    
    for i in range(max_iter):
        f_x = f_expr(x)
        df_x = df_expr(x)
        
        # Verificar si la derivada es cercana a cero para evitar división por cero
        if abs(df_x) < 1e-10:
            print("\nDerivada cercana a cero. El método puede diverger.")
            return x, iteraciones, False
        
        # Calcular el siguiente valor de x
        x_next = x - f_x / df_x
        
        # Calcular el error
        error = abs(x_next - x)
        
        # Almacenar la información de esta iteración
        iteraciones.append((i+1, x, f_x, error))
        
        # Actualizar x para la siguiente iteración
        x = x_next
        
        # Verificar criterio de convergencia
        if error < tol:
            return x, iteraciones, True
    
    print("\nSe alcanzó el número máximo de iteraciones sin convergencia.")
    return x, iteraciones, False

def mostrar_resultados(raiz, iteraciones, convergencia, f_expr):
    """
    
    
    Parámetros:
    -----------
    raiz : float
        La aproximación a la raíz encontrada
    iteraciones : list
        Lista de tuplas (iteración, valor_x, f(x), error)
    convergencia : bool
        Si el método convergió o no
    f_expr : función lambdificada
        La función original
    """
    print("\n" + "="*60)
    print("RESULTADOS DEL MÉTODO DE NEWTON-RAPHSON")
    print("="*60)
    
    # Mostrar iteraciones paso a paso
    print("\nIteraciones paso a paso:")
    print("-"*70)
    print(f"{'Iteración':^10} | {'x_i':^15} | {'f(x_i)':^15} | {'Error':^15}")
    print("-"*70)
    
    for iter_num, x_val, f_val, error in iteraciones:
        print(f"{iter_num:^10} | {x_val:^15.8f} | {f_val:^15.8f} | {error:^15.8f}")
    
    # Mostrar resultado final
    print("\nResultado Final:")
    print("-"*60)
    if convergencia:
        estado = "CONVERGIÓ"
    else:
        estado = "NO CONVERGIÓ"
        
    print(f"Estado: El método {estado} en {len(iteraciones)} iteraciones")
    print(f"Aproximación de la raíz: {raiz:.10f}")
    print(f"Valor de la función en la raíz: {f_expr(raiz):.10f}")
    print("-"*60)

def graficar_funcion(f_expr, raiz, iteraciones, x_min, x_max):
    """
    
    
    Parámetros:
    -----------
    f_expr : función lambdificada
        La función de la cual se busca la raíz
    raiz : float
        La aproximación a la raíz encontrada
    iteraciones : list
        Lista de tuplas (iteración, valor_x, f(x), error)
    x_min, x_max : float
        Límites para el eje x de la gráfica
    """
    # Crear un arreglo de puntos x para graficar la función
    x = np.linspace(x_min, x_max, 1000)
    y = [f_expr(val) for val in x]
    
    # Crear la figura y los ejes
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Graficar la función
    ax1.plot(x, y, 'b-', label=f'f(x)')
    ax1.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax1.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.set_title('Gráfica de la función y su raíz')
    
    # Marcar la raíz encontrada
    ax1.plot(raiz, 0, 'ro', label=f'Raíz: x ≈ {raiz:.6f}')
    
    # Graficar la convergencia del método
    x_valores = [x for _, x, _, _ in iteraciones]
    errores = [error for _, _, _, error in iteraciones]
    
    ax2.semilogy(range(1, len(errores)+1), errores, 'g-o')
    ax2.set_xlabel('Número de iteración')
    ax2.set_ylabel('Error (escala logarítmica)')
    ax2.set_title('Convergencia del método')
    ax2.grid(True, alpha=0.3)
    
    # Ajustes finales
    ax1.legend()
    plt.tight_layout()
    
    # Guardar la gráfica como archivo
    plt.savefig('newton_raphson_resultados.png')
    print("\nGráfica guardada como 'newton_raphson_resultados.png'")
    
    # Mostrar la gráfica
    plt.show()

def main():
    """Función principal que maneja la interfaz con el usuario."""
    clear_screen()
    print("="*60)
    print("MÉTODO DE NEWTON-RAPHSON PARA ENCONTRAR RAÍCES DE FUNCIONES")
    print("="*60)
    print("\nEste programa implementa el método de Newton-Raphson para encontrar")
    print("raíces de funciones. El método utiliza la derivada de la función para")
    print("aproximar la raíz de manera iterativa.")
    print("\nNota: Utilice la sintaxis de Python para ingresar la función.")
    print("Ejemplos: x**2 - 4, sin(x) + x**2, exp(x) - 2")
    
    try:
        # Obtener la función del usuario
        funcion_str = input("\nIngrese la función f(x): ")
        
        # Crear símbolos y expresiones simbólicas
        x = symbols('x')
        f_sym = sympify(funcion_str)
        df_sym = diff(f_sym, x)  # Derivada simbólica
        
        # Convertir expresiones simbólicas a funciones Python
        f = lambdify(x, f_sym, 'numpy')
        df = lambdify(x, df_sym, 'numpy')
        
        # Mostrar la derivada calculada
        print(f"\nLa derivada calculada es: {df_sym}")
        
        # Solicitar el valor inicial
        x0 = float(input("\nIngrese el valor inicial (x0): "))
        
        # Solicitar tolerancia y máximo de iteraciones (opcional)
        usar_valores_default = input("\n¿Desea usar valores por defecto para tolerancia (1e-6) y máximo de iteraciones (100)? (s/n): ").lower() == 's'
        
        if usar_valores_default:
            tol = 1e-6
            max_iter = 100
        else:
            tol = float(input("Ingrese la tolerancia deseada: "))
            max_iter = int(input("Ingrese el número máximo de iteraciones: "))
        
        # Aplicar el método de Newton-Raphson
        raiz, iteraciones, convergencia = newton_raphson(f, df, x0, tol, max_iter)
        
        # Mostrar los resultados
        mostrar_resultados(raiz, iteraciones, convergencia, f)
        
        # Solicitar límites para la gráfica
        print("\nPara generar la gráfica, por favor ingrese los límites del eje x:")
        x_min = float(input("Valor mínimo de x: "))
        x_max = float(input("Valor máximo de x: "))
        
        # Generar la gráfica
        graficar_funcion(f, raiz, iteraciones, x_min, x_max)
        
    except Exception as e:
        print(f"\nError: {e}")
        print("Por favor, verifique su entrada e intente nuevamente.")

if __name__ == "__main__":
    main()