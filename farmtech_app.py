
"""
FarmTech Solutions - Agricultura Digital (Python CLI)
Culturas: Café (área circular) e soja (área retangular)

Requisitos atendidos:
- Vetores (listas) para armazenar dados
- Cálculo de área por cultura (figuras geométricas distintas)
- Cálculo de manejo de insumos (por metro de rua e por hectare)
- Menu com: entrada, saída, atualização, deleção, exportação e sair
- Estruturas de repetição e decisão
"""
import math
import csv
from typing import List, Dict

# Estrutura de dados (vetores)
cafe_plots: List[Dict] = []         # Cada item: {"raio_m": float, "area_m2": float}
soja_plots: List[Dict] = []         # Cada item: {"compr_m": float, "larg_m": float, "area_m2": float}

# Utilidades
def m2_to_ha(area_m2: float) -> float:
    return area_m2 / 10_000.0

def input_float(msg: str, min_val: float = 0.0) -> float:
    while True:
        try:
            v = float(input(msg).replace(",", "."))
            if v < min_val:
                print(f"Valor deve ser >= {min_val}.")
                continue
            return v
        except ValueError:
            print("Entrada inválida. Digite um número.")

def print_header(title: str):
    print("\n" + "-" * 60)
    print(title)
    print("-" * 60)

def total_area_m2(vetor: List[Dict]) -> float:
    return sum(x["area_m2"] for x in vetor)

# Entrada de dados
def add_cafe_plot():
    print_header("Adicionar Talhão - Café (área circular)")
    r = input_float("Informe o raio do talhão em metros (m): ", 0.01)
    area = math.pi * r * r
    cafe_plots.append({"raio_m": r, "area_m2": area})
    print(f"Talhão de café adicionado. Área = {area:.2f} m² ({m2_to_ha(area):.4f} ha)")

def add_cana_plot():
    print_header("Adicionar Talhão - Cana-de-açúcar (área retangular)")
    c = input_float("Comprimento do talhão em metros (m): ", 0.01)
    l = input_float("Largura do talhão em metros (m): ", 0.01)
    area = c * l
    cana_plots.append({"compr_m": c, "larg_m": l, "area_m2": area})
    print(f"Talhão de cana adicionado. Área = {area:.2f} m² ({m2_to_ha(area):.4f} ha)")

def entrada_dados():
    print_header("Entrada de Dados")
    print("1) Café (círculo)")
    print("2) Cana-de-açúcar (retângulo)")
    op = input("Escolha a cultura (1-2): ").strip()
    if op == "1":
        add_cafe_plot()
    elif op == "2":
        add_cana_plot()
    else:
        print("Opção inválida.")