"""
Este programa determina las soluciones de una ecuación de segundo grado en todos sus casos.
Autores:
Fecha:
"""
from math import sqrt;
from cmath import sqrt as sqrtComplex;

def main():
    print(__doc__)
    print("Teniendo en cuenta que la estructura de la fuci�n es la siguiente: ax� + bx + c")
    a = float(input("Escribe el valor de a: "));
    b = float(input("Escribe el valor de b: "));
    c = float(input("Escribe el valor de c: "));
    
    #Ecuaci�n completa
    if a != 0 and b != 0 and c != 0:
        #Resultados reales
        if (b**2-4*a*c) > 0:
            x1 = (-b+sqrt(b**2-4*a*c))/2*a;
            x2 = (-b-sqrt(b**2-4*a*c))/2*a;
            print("Las soluciones son:", x1, "y", x2);
            
        #Resultados complejos
        else: 
            x1 = complex((-b+sqrtComplex(b**2-4*a*c))/(2*a));
            x2 = complex((-b-sqrtComplex(b**2-4*a*c))/(2*a));
            print("Las soluciones son:", x1, "y", x2);
            print("Resultado complejo");
    #Ecuaci�n sin x
    elif a==0 and b == 0:
        if c == 0:
            print("0 = 0 siempre es cierto");
        else:
            print(c,"= 0 no tiene respuesta");
            
    #Ecuaci�n sin termino independiente
    elif c == 0 and (a != 0 and b != 0):
        print("Las soluciones son 0 y",-b/a)

    #Ecuaci�n con solo x o x cuadrado
    elif c == 0 and (a != 0 or b != 0):
        print("La soluci�n es: 0");
    
    #Ecuaci�n sin x cuadrado
    elif c != 0 and a == 0 and b != 0:
        print("La soluci�n es:",-c/b)
        
    #Ecuaci�n si x
    elif c != 0 and a != 0 and b == 0:
        #Resultados reales
        if -c/a > 0:
            x = sqrt(-c/a);
            print("Las soluciones son:",x , "y", -x);
        #Resultados complejos
        else:
            x = sqrtComplex(-c/a);
            print("Las soluciones son:",x , "y", -x);
    
    
if __name__ == "__main__":
    main();