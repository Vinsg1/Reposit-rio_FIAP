
"""
FarmTech Solutions - Agricultura Digital 
Culturas: Café (área circular) e soja (área retangular)

Requisitos:
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

# Saída de dados
def listar_plots():
    print_header("Saída de Dados - Talhões")
    # Café
    print(">> Café (círculo)")
    if not cafe_plots:
        print("Nenhum talhão de café cadastrado.")
    else:
        for i, p in enumerate(cafe_plots):
            print(f"[{i}] raio={p['raio_m']:.2f} m | área={p['area_m2']:.2f} m² ({m2_to_ha(p['area_m2']):.4f} ha)")
        area_total = total_area_m2(cafe_plots)
        print(f"Total Café: {area_total:.2f} m² ({m2_to_ha(area_total):.4f} ha)")
    print("-" * 60)
    # Soja
    print(">> Soja (retângulo)")
    if not cana_plots:
        print("Nenhum talhão de cana cadastrado.")
    else:
        for i, p in enumerate(cana_plots):
            print(f"[{i}] C={p['compr_m']:.2f} m x L={p['larg_m']:.2f} m | área={p['area_m2']:.2f} m² ({m2_to_ha(p['area_m2']):.4f} ha)")
        area_total = total_area_m2(cana_plots)
        print(f"Total Soja: {area_total:.2f} m² ({m2_to_ha(area_total):.4f} ha)")

# Atualização de dados
def atualizar_dados():
    print_header("Atualização de Dados")
    print("1) Café   2) Cana-de-açúcar")
    op = input("Escolha a cultura (1-2): ").strip()
    if op == "1":
        if not cafe_plots:
            print("Sem dados para atualizar.")
            return
        idx = input_float("Índice do talhão a atualizar: ", 0)
        idx = int(idx)
        if idx < 0 or idx >= len(cafe_plots):
            print("Índice inválido.")
            return
        r = input_float("Novo raio (m): ", 0.01)
        area = math.pi * r * r
        cafe_plots[idx] = {"raio_m": r, "area_m2": area}
        print("Talhão de café atualizado.")
    elif op == "2":
        if not cana_plots:
            print("Sem dados para atualizar.")
            return
        idx = input_float("Índice do talhão a atualizar: ", 0)
        idx = int(idx)
        if idx < 0 or idx >= len(cana_plots):
            print("Índice inválido.")
            return
        c = input_float("Novo comprimento (m): ", 0.01)
        l = input_float("Nova largura (m): ", 0.01)
        area = c * l
        cana_plots[idx] = {"compr_m": c, "larg_m": l, "area_m2": area}
        print("Talhão de cana atualizado.")
    else:
        print("Opção inválida.")

