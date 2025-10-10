total_compras_exitosas=0
saldo= 0
monto=0
terminar= False
saldo= int(input("Indique el saldo inicial: "))

while not terminar:
    monto=int(input("Cuanto desea invertir para esta cripto?: "))
    if monto<= saldo:
        total_compras_exitosas= total_compras_exitosas+1
        saldo= saldo-monto
        print ("Se realizo la compra")
    elif saldo== 0: 
        terminar= True
    else: 
        print("No se pudo realizar la compra")
        terminar= True
print("El total de compras exitosas es:", total_compras_exitosas)
print("Dinero que sobro sin usar: ", saldo)