import os
from trace_loader import cargar_traza
from simulator import correr_simulaciones
from colorama import init, Fore, Style

init(autoreset=True)

def listar_trazas():
    carpeta = 'traces'
    archivos = [f for f in os.listdir(carpeta) if f.endswith('.trace')]
    return archivos

def seleccionar_traza():
    archivos = listar_trazas()
    if not archivos:
        print(f"{Fore.RED}❌ No se encontraron archivos .trace en la carpeta 'traces'.")
        exit(1)

    print(f"\n{Fore.CYAN}{'='*40}")
    print(f"{Fore.YELLOW}📂 Archivos disponibles para simular:")
    print(f"{Fore.CYAN}{'='*40}")
    for i, archivo in enumerate(archivos):
        print(f"{Fore.GREEN}{i+1}. {archivo}")

    while True:
        try:
            seleccion = int(input(f"\n{Fore.BLUE}👉 Seleccione el número del archivo a cargar: "))
            if 1 <= seleccion <= len(archivos):
                return os.path.join('traces', archivos[seleccion-1])
            else:
                print(f"{Fore.RED}Número inválido, intente de nuevo.")
        except ValueError:
            print(f"{Fore.RED}Por favor ingrese un número válido.")

def main():
    print(f"{Fore.MAGENTA}{'='*50}")
    print(f"{Fore.MAGENTA}🧠 Simulador de Reemplazo de Páginas - UNITEC")
    print(f"{Fore.MAGENTA}{'='*50}\n")

    ruta = seleccionar_traza()
    print(f"\n{Fore.YELLOW}📥 Cargando archivo: {Fore.CYAN}{ruta}")
    referencias = cargar_traza(ruta)
    print(f"{Fore.YELLOW}✅ Cargadas {Fore.CYAN}{len(referencias)} {Fore.YELLOW}referencias.\n")
    correr_simulaciones(referencias)

if __name__ == '__main__':
    main()

