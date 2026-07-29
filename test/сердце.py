import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)

x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
 
plt.figure(figsize=(7, 6))

plt.plot(x, y, color='red', linewidth=3, label='Math is Beautiful')

# Настройка внешнего вида
plt.title('Heart built with python & math', fontsize=14, fontweight='bold', color='navy')
plt.grid(True, linestyle=':', alpha=0.6, color='blue')

# Смещаем легенду вниз
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05))

# Ограничиваем оси, чтобы было пропорционально
plt.axis('equal')

plt.show()
