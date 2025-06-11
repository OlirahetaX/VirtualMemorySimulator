# Coordinador del experimento con distintos frames

from page_replacement import PageReplacementSimulator
from utils import calcular_EAT
from colorama import init, Fore, Style

def imprimir_mapa_memoria(estado_memoria, frames):
    print("Mapa de memoria:")
    print(f"[Total frames: {frames}]")
    if not estado_memoria:
        print("(Memoria vacía)")
        return
    # Imprimir páginas con su estado (S=dirty, L=clean)
    line = ''
    for pagina, estado in estado_memoria:
        line += f"{pagina}({estado}) "
    print(line.strip())
    print("-" * 40)

def correr_simulaciones(referencias):
    init(autoreset=True)
    estrategias = ['FIFO', 'LRU', 'OPT']
    frames_opciones = [10, 50, 100]

    for f in frames_opciones:
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.CYAN}         Simulación con {Fore.YELLOW}{f} frames{Fore.CYAN}")
        print(f"{Fore.CYAN}{'='*40}")

        sim = PageReplacementSimulator(f)

        for estrategia in estrategias:
            if estrategia == 'FIFO':
                pf, rep, disco = sim.simular_fifo(referencias)
            elif estrategia == 'LRU':
                pf, rep, disco = sim.simular_lru(referencias)
            elif estrategia == 'OPT':
                pf, rep, disco = sim.simular_opt(referencias)

            eat = calcular_EAT(pf, len(referencias))

            print(f"{Fore.GREEN}{estrategia}:")
            print(f"  {Fore.MAGENTA}Page Faults: {Fore.YELLOW}{pf}")
            print(f"  {Fore.MAGENTA}Reemplazos: {Fore.YELLOW}{rep}")
            print(f"  {Fore.MAGENTA}Escritos a disco: {Fore.YELLOW}{disco}")
            print(f"  {Fore.MAGENTA}EAT (ns): {Fore.YELLOW}{eat:.2f}")
            print(Style.RESET_ALL)