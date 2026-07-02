# 🦎 KalangoEV

Calculadora de **Valor Esperado (+EV)** para identificar distorções matemáticas em mercados e bilhetes de apostas esportivas.

---

## Como Baixar e Usar

1. No menu lateral direito, acesse **[Releases](https://github.com/)**.
2. Baixe o arquivo `.zip` (ex: `KalangoEV-Windows.zip`).
3. Extraia a pasta em seu computador.
4. Execute o arquivo **`KalangoEV.exe`**.

---

## Funcionamento Base

*   **Casas de Referência:** Use mercados de alta liquidez (**Pinnacle** / **BM Bet**) para obter as odds puras.
*   **Odd Justa:** O app remove o *Juice* (taxa da casa) para encontrar o preço real do evento.
*   **Decisão:** Se a **Odd Encontrada** for maior que a **Odd Justa**, o painel fica **Verde (+EV)** indicando valor, além de calcular a porcentagem de stake ideal via **Critério de Kelly**.

---

##  Método para Apostas Correlacionadas

Para calcular bilhetes combinados que se influenciam mutuamente:

1. **Pegue a Odd da Casa:** Monte a múltipla no "Criar Aposta" (ex: Bet365) e anote a odd final (Ex: **2.20**).
2. **Multiplique Isolado:** Multiplique as odds dos mesmos mercados individualmente (Ex: $1.28 \times 1.08 \times 1.72 =$ **2.38**).
3. **Descubra a Correlação:** Pergunte à IA: *"Qual a correlação negativa se a multiplicação dá 2.38 mas a casa paga 2.20?"* (Resultado: **-7.7%**).
4. **Aplique no App:** Vá na Pinnacle, pegue as odds justas dos mercados, multiplique-as, aplique o desconto da IA (-7.7%) e insira o valor final no campo **Odd Analisada** para validar a sua aposta.

---
