class Node:
    def __init__(self, coefficient, degree):
        self.coefficient = coefficient
        self.degree = degree
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def add_term(self, coefficient, degree):
        if coefficient == 0:
            return  # Si el coeficiente es 0, no se agrega el termino 

        new_node = Node(coefficient, degree)
        if not self.head or degree > self.head.degree:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            while current and current.degree >= degree:
                if current.degree == degree:
                    current.coefficient += coefficient  # Si el término ya existe, solo se suman 
                    if current.coefficient == 0:
                        if prev:
                            prev.next = current.next  # si el coeficiente se vuelve cero se eliminamos
                        else:
                            self.head = current.next
                    return
                prev = current
                current = current.next

            prev.next = new_node  # se agrega el termino nuevo 

    def display(self, operation=None):
        current = self.head
        polynomial_str = ""
        while current:
            polynomial_str += f"{current.coefficient}x^{current.degree} + " if current.coefficient != 0 else ""
            current = current.next
        if operation:
            print(f"Resultado de {operation}: {polynomial_str.rstrip(' + ')}")
        else:
            print(polynomial_str.rstrip(" + "))

    def display_polynomials(self):
        print("Estado actual de los polinomios:")
        print("a =", end=" ")
        self.display()
        print("b =", end=" ")
        self.display()

    def add(self, other_poly):
        result_poly = Polynomial()
        current_self = self.head
        current_other = other_poly.head

        while current_self and current_other:
            if current_self.degree > current_other.degree:
                result_poly.add_term(current_self.coefficient, current_self.degree)
                current_self = current_self.next
            elif current_self.degree < current_other.degree:
                result_poly.add_term(current_other.coefficient, current_other.degree)
                current_other = current_other.next
            else:
                result_poly.add_term(current_self.coefficient + current_other.coefficient, current_self.degree)
                current_self = current_self.next
                current_other = current_other.next

        while current_self:
            result_poly.add_term(current_self.coefficient, current_self.degree)
            current_self = current_self.next

        while current_other:
            result_poly.add_term(current_other.coefficient, current_other.degree)
            current_other = current_other.next

        return result_poly

    def subtract(self, other_poly):
        result_poly = Polynomial()
        current_self = self.head
        current_other = other_poly.head

        while current_self and current_other:
            if current_self.degree > current_other.degree:
                result_poly.add_term(current_self.coefficient, current_self.degree)
                current_self = current_self.next
            elif current_self.degree < current_other.degree:
                result_poly.add_term(-current_other.coefficient, current_other.degree)
                current_other = current_other.next
            else:
                result_poly.add_term(current_self.coefficient - current_other.coefficient, current_self.degree)
                current_self = current_self.next
                current_other = current_other.next

        while current_self:
            result_poly.add_term(current_self.coefficient, current_self.degree)
            current_self = current_self.next

        while current_other:
            result_poly.add_term(-current_other.coefficient, current_other.degree)
            current_other = current_other.next

        return result_poly

    def evaluate(self, x):
        result = 0
        current = self.head
        while current:
            result += current.coefficient * (x ** current.degree)
            current = current.next
        return result

def menu():
    print("Menú:")
    print("1. Definir polinomios a y b")
    print("2. Mostrar estado actual de los polinomios")
    print("3. Suma y resta de polinomios")
    print("4. Evaluar polinomios")
    print("5. Salir")
    return input("Ingrese el número de la acción que desea realizar: ")

if __name__ == "__main__":
    a = Polynomial()
    b = Polynomial()

    while True:
        choice = menu()

        if choice == "1":
            print("Definición del polinomio a:")
            while True:
                coefficient = int(input("Ingrese el coeficiente del término (o 0 para terminar): "))
                if coefficient == 0:
                    break
                degree = int(input("Ingrese el grado del término: "))
                a.add_term(coefficient, degree)

            print("Definición del polinomio b:")
            while True:
                coefficient = int(input("Ingrese el coeficiente del término (o 0 para terminar): "))
                if coefficient == 0:
                    break
                degree = int(input("Ingrese el grado del término: "))
                b.add_term(coefficient, degree)

        elif choice == "2":
            a.display_polynomials()

        elif choice == "3":
            a.display_polynomials()
            operation = input("Ingrese la operación que desea realizar (suma/resta): ")
            if operation == "suma":
                c = a.add(b)
                c.display("suma")
            elif operation == "resta":
                c = a.subtract(b)
                c.display("resta")
            else:
                print("Operación no válida")

        elif choice == "4":
            a.display_polynomials()
            poly_choice = input("Ingrese el nombre del polinomio que desea evaluar (a/b): ")
            x = int(input("Ingrese el valor de x: "))
            if poly_choice == "a":
                result = a.evaluate(x)
                print(f"El resultado de evaluar el polinomio a en x={x} es: {result}")
            elif poly_choice == "b":
                result = b.evaluate(x)
                print(f"El resultado de evaluar el polinomio b en x={x} es: {result}")
            else:
                print("Opción no válida")

        elif choice == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")
