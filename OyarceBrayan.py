#BrayanOyarce
#Prueba3.
#BancoInternacional

import random
import statistics
import csv
from math import prod

def generar_saldos(nombres):
    saldos = {nombre: random.randint(300000, 600000) for nombre in nombres}
    return saldos

def clasificar_saldos(saldos):
    bajos = {nombre: saldo for nombre, saldo in saldos.items() if saldo < 200000}
    medios = {nombre: saldo for nombre, saldo in saldos.items() if 250000 <= saldo < 550000}
    altos = {nombre: saldo for nombre, saldo in saldos.items() if saldo >= 550000}
    return bajos, medios, altos

def calcular_media_geometrica(saldos):
    return int(prod(saldos) ** (1 / len(saldos)))

def calcular_estadisticas(saldos):
    saldo_mas_alto = max(saldos.values())
    saldo_mas_bajo = min(saldos.values())
    saldo_promedio = int(statistics.mean(saldos.values()))
    media_geometrica = calcular_media_geometrica(saldos.values())
    return saldo_mas_alto, saldo_mas_bajo, saldo_promedio, media_geometrica

def generar_reporte(saldos, filename='reporte_saldos.csv'):
    deducciones = {
        'impuesto': 0.25,
        'seguro': 0.15,
        'otros': 0.08
    }
    with open(filename, 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerow(['Cliente', 'Saldo Bruto', 'Impuesto', 'Seguro'])

        for nombre, saldo in saldos.items():
            impuesto = round(saldo * deducciones['impuesto'])
            seguro = round(saldo * deducciones['seguro'])

def mostrar_menu():
    print("Menu:")
    print("1. Entregar saldos aleatorios")
    print("2. Clasificacion de saldos")
    print("3. Indicar estadísticas")
    print("4. Generar reportes de saldos")
    print("5. Salir")

def ejecutar_opcion(opcion, saldos, nombres):
    if opcion == '1':
        saldos.clear()
        saldos.update(generar_saldos(nombres))
        print("Saldos generados:")
        for nombre, saldo in saldos.items():
            print(f'{nombre}: {saldo}')
    elif opcion == '2':
        if saldos:
            bajos, medios, altos = clasificar_saldos(saldos)
            print("Saldos bajos:")
            for nombre, saldo in bajos.items():
                print(f'{nombre}: {saldo}')
            print("Saldos medios:")
            for nombre, saldo in medios.items():
                print(f'{nombre}: {saldo}')
            print("Saldos altos:")
            for nombre, saldo in altos.items():
                print(f'{nombre}: {saldo}')
        else:
            print("Primero genere los saldos (opción 1).")
    elif opcion == '3':
        if saldos:
            saldo_mas_alto, saldo_mas_bajo, saldo_promedio, media_geometrica = calcular_estadisticas(saldos)
            print(f"Saldo más alto: {saldo_mas_alto}")
            print(f"Saldo más bajo: {saldo_mas_bajo}")
            print(f"Saldo promedio: {saldo_promedio}")
            print(f"Media geométrica: {media_geometrica}")
        else:
            print("Primero genere los saldos (opción 1).")
    elif opcion == '4':
        if saldos:
            generar_reporte(saldos)
            print("Reporte generado: reporte_saldos.csv")
        else:
            print("Primero, generar los saldos (opción 1).")
    elif opcion == '5':
        print("Gracias por visitar nuestro Banco, Buenas Tardes.")
        return False
    else:
        print("Opción invalida, Intente nuevamente.")
    return True
def main()
nombres = ['Cliente1', 'Cliente2', 'Cliente3', 'Cliente4', 'Cliente5', 'Cliente6', 'Cliente7', 'Cliente8', 'Cliente9', 'Cliente10']