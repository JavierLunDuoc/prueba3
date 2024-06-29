#se define una variable para registrar los productos por nombre, categoria, cantidad y presio
def registroProd(productos):
    try:
        nom = input("Ingrese el nombre del producto que desee ingresar: ")
        cat = input("Ingrese la categoria del producto: ")
        cant = int(input("ingrese la cantidad del producto: "))
        pres = random.uniform(10, 1000)

        producto = {
            "Nombre": nom,
            "Categoria": cat,
            "Cantidad": cant,
            "Presio": pres
        }
        producto.append(producto)
        print("Se a agregado el producto")
    except ValueError:
        print("Favor de agregar los datos que se piden en el orden en que se piden")

#Una variable para mostrar los productos de la lista antes creada
def listaProds(productos):
    if productos:
        print("Nombre: \t\t Categoria: \t\t Cantidad: \t\t Precio: ")
        for producto in productos:
            print(f"{producto["Nombre"]} \t\t {producto["Cateogria"]} \t\t {producto["Cantidad"]} \t\t {producto["presio"]}")
        else:
            print("No se ha encontrado ningun producto")

def buscarCat(productos):
    categoria = input("Ingrese la categoria que le gustaria buscar")