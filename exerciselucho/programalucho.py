
productos = [ "bebida" , "comida" , "ropa" ]
valores   = [  5 , 8 , 15 ]

def mostrarProductos():
 print("Elija el producto a comprar:\n")
 i = 1
 for prod in productos:   
    print(str(i)+ " - " + prod)
    i+=1

codigoproducto = -1
subtotal = 0
mostrarProductos()
while codigoproducto != 0:
  inputcodigo =  input("Ingrese el producto 0 para terminar) :\n")
  codigoproducto = int(inputcodigo)  
  if codigoproducto >= 0 and codigoproducto < len(productos)+1:
     if codigoproducto == 0:
        break
     subtotal += valores[codigoproducto-1]
     print("Producto elegido: "+productos[codigoproducto-1]+" -  precio: "+ str(valores[codigoproducto-1]) + " - subtotal: "+str(subtotal))
print("Total compra :"+ str(subtotal))

inputpago =  input("Ingrese el monto del pago:\n")
pago = int(inputpago)
if ( pago < subtotal ):
   print(" El pago es insuficiente\n")
else: 
   vuelto = pago - subtotal
   print("Su vuelto es "+ str(vuelto))
