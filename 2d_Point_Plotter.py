import matplotlib.pyplot as plt

# coordenadas dos pontos

x = [
10.955384,
10.953061,
10.949575,
10.943768,
10.943768,
10.936797,
10.930988,
10.928665,
10.91821,
10.905432,
10.891491,
10.889168,
10.876389,
10.860125,
10.858963,
10.840376,
10.826436,
10.819466,
10.797393,
10.786938,
10.772998,
10.74744,
10.743955,
10.71956,
10.696325,
10.642887,
10.585964,
10.524393,
10.459338,
10.388474,
10.352462,
10.34433,
10.338522,
10.335036,
10.316449,
9.135,
]

y = [
25.361,
25.417923,
25.473684,
25.53177,
25.529446,
25.58637,
25.628191,
25.642132,
25.697893,
25.752493,
25.808254,
25.81871,
25.861692,
25.911646,
25.916292,
25.968569,
26.00342,
26.022007,
26.074284,
26.094032,
26.125399,
26.176514,
26.182322,
26.226467,
26.267126,
26.348446,
26.428602,
26.505276,
26.577301,
26.64584,
26.67953,
26.687662,
26.692308,
26.695793,
26.712057,
27.739,
]

# rótulos dos pontos
labels = [f'P{i+1}' for i in range(len(x))]

# plota os pontos
plt.scatter(x, y)

# adiciona os rótulos aos pontos
for i, txt in enumerate(labels):
    plt.annotate(txt, (x[i], y[i]))

# exibe o gráfico
plt.show()