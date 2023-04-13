import numpy as np
import matplotlib.pyplot as plt

# criando o sinal original
t = np.linspace(0, 8*np.pi, 200)
sinal = np.sin(t)

# adicionando ruído com SNR escolhido pelo usuário
SNR = float(input("Digite o valor do SNR desejado: "))
Pruido = np.var(sinal) / (10**(SNR/10))
ruido = np.random.normal(0, np.sqrt(Pruido), sinal.shape)
sinal_ruidoso = sinal + ruido

# plotando o gráfico
fig, ax = plt.subplots(figsize=(10,5))

ax.plot(t, sinal_ruidoso, label='SNR = {} dB'.format(SNR), linestyle='-', linewidth=2)
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Amplitude')
ax.legend()

plt.tight_layout()
plt.show()
