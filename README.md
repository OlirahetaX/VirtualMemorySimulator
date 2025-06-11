# 📦 Simulador de Reemplazo de Páginas

Este proyecto es un simulador educativo en Python que implementa y compara tres algoritmos clásicos de reemplazo de páginas: **FIFO**, **LRU** y **Óptimo (OPT)**. Analiza cómo se comportan con distintos tamaños de memoria usando archivos de trazas reales.

## 🧠 Algoritmos implementados

- FIFO (First-In First-Out)
- LRU (Least Recently Used)
- OPT (Óptimo, basado en conocimiento futuro)

## 📊 ¿Qué analiza?

- Fallos de página (*page faults*)
- Número de reemplazos
- Escritos a disco
- Tiempo efectivo de acceso (EAT)

## 🚀 Cómo usar

1. Coloca archivos `.trace` en la carpeta `traces/`.
2. Ejecuta el programa con:

   ```bash
   python main.py
