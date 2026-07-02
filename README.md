# 🦎 KalangoEV

O **KalangoEV** é uma calculadora de **Valor Esperado (+EV)** desenvolvida para auxiliar apostadores a identificarem distorções matemáticas no mercado de apostas esportivas, utilizando conceitos de Odd Justa, Payout e o Critério de Kelly para gestão de banca.

---

## 🚀 Como Baixar e Executar (Sem precisar de Python)

Você não precisa instalar o Python ou configurar códigos para usar o sistema. O programa já vem pronto para uso na aba de lançamentos do GitHub.

1. No lado direito desta página, clique em **[Releases](https://github.com/)** (ou na versão mais recente, ex: `v1.0.0`).
2. Na seção de **Assets**, baixe o arquivo compactado (Ex: `KalangoEV-Windows.zip`).
3. Extraia o arquivo `.zip` em qualquer pasta do seu computador.
4. Abra a pasta extraída e dê um duplo clique no executável **`KalangoEV.exe`**.

---

## 📊 Conceitos Base do Sistema

Para extrair o máximo de valor da ferramenta, é importante entender os pilares matemáticos utilizados:

*   **Casas de Referência:** Utilize sempre mercados de casas que possuem alta liquidez e precisão em suas linhas, como **Pinnacle** ou **BM Bet**, para extrair as probabilidades mais fiéis da realidade.
*   **Juice:** É a taxa de lucro (comissão) embutida pelas casas de apostas. O KalangoEV calcula o **Payout** para remover essa taxa e encontrar a probabilidade real.
*   **Odd Justa:** É o preço real e purificado do evento. Se a **Odd Encontrada** (a que você vai apostar) for **maior** do que a **Odd Justa**, você encontrou uma aposta com **Valor Esperado Positivo (+EV)**.

---

## 🛠️ Como Utilizar o Aplicativo

O painel é intuitivo e dinâmico, adaptando-se à quantidade de mercados que você deseja analisar.

1. **Número de Mercados:** Escolha entre 2, 3 ou 4 mercados no menu suspenso. O app criará automaticamente os campos de preenchimento necessários.
2. **Odd Analisada:** Insira a odd da sua casa de referência (ex: Pinnacle). Se houver mais de um mercado correlacionado, preencha as *Odds Contrárias* que abrem dinamicamente.
3. **Odd Encontrada:** Insira a odd da linha desregulada que você encontrou na casa de destino (onde você de fato vai realizar a sua aposta).
4. **Clique em Calcular:** O sistema alterará a cor do painel principal para **Verde (EV+)** caso a aposta seja lucrativa no longo prazo, ou **Vermelho (EV-)** caso não tenha valor. Ele também exibirá a porcentagem exata da sua banca a ser utilizada usando o **Critério de Kelly**.

---

## 🧠 Guia Avançado: Apostas com Correlação (Uso de IA)

Quando você cria bilhetes combinados na mesma partida, os mercados influenciam uns aos outros (Correlação). Siga este método prático para precificar esses cenários:

1. **Descubra a Odd da Casa:** Vá na ferramenta *Criar Aposta* (ex: Bet365) e selecione os mercados desejados (Ex: *Gol HT + Gol Time A + Gol Time B*). Anote a odd final gerada pela casa (Exemplo: **2.20**).
2. **Calcule a Multiplicação Pura:** Multiplique as odds desses mesmos mercados de forma isolada (Ex: $1.28 \times 1.08 \times 1.72 = $ **2.38**).
3. **Identifique a Correlação:** Pergunte a uma Inteligência Artificial:
   > *"Qual a correlação negativa dessa aposta, caso multiplicado os três mercados dê 2.38, mas a casa pague 2.20?"*
   *Nesse cenário simulado, a IA apontará uma correlação negativa de aproximadamente **-7.7%**.*
4. **Aplique no App:** Pegue as odds puras e justas de cada mercado nas suas casas de referência (Pinnacle/BM Bet), multiplique-as e aplique o desconto da correlação encontrado pela IA (os -7.7%). Insira o resultado final no campo de **Odd Analisada** do KalangoEV para validar se a sua casa de destino ainda mantém valor acima dessa taxa.

---

## 💻 Tecnologias Utilizadas

*   [Python](https://www.python.org/)
*   [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Interface Gráfica Moderna)
*   [Pillow (PIL)](https://python-pillow.org/) (Processamento de Ícones)
