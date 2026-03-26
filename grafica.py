import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [26**1, 26**2, 26**3, 26**4, 26**5]

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', color='red', linewidth=2, label='Combinaciones (26^n)')


plt.yscale('log') 
plt.title('Crecimiento Exponencial de Fuerza Bruta', fontsize=14)
plt.xlabel('Longitud de la Contraseña', fontsize=12)
plt.ylabel('Intentos Necesarios (Escala Log)', fontsize=12)
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()

plt.show() 
