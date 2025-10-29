imfo_tienda=("Run fast",2010)
print(f"Bienvenidos a sonic games, esta es nuestra indo: {imfo_tienda} ")
inventario={
    "Sonic race":{"precio":50,"unidades": 5},
    "Sonic adventure":{"precio":30,"unidades": 2},
    "Sonic colors":{"precio":40,"unidades": 7}
}

print("Precio de sonic adventure: ",inventario["Sonic race"]["precio"])


inventario["Sonic race"]["unidades"]-=1

print(inventario)
 