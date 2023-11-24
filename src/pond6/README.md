# Logicando com Logictron!
Logictron foi desenvolvido como uma aplicação em python baseado em perceptrons, os primeiros modelos de neurônios artificiais que serviram de conceito fundamental no campo da inteligência artificial. Logictron é capaz, através de um treinamento prévio, simular o comportamento das portas lógicas AND, OR, NAND e XOR e suas utilizações.

## Configurando Logictron!
Éssa é a parte fácil, as suas dependências são quase nulas! Apenas garanta que você tem a linguagem de programação python instalada em seu computador, e a biblioteca `numpy`.

## Logictron em Ação!
Mais fácil do que conferir as dependências, para logicar com Logictron, só precisa rodar o comando no diretório `Modulo8/src/pond6`:
```
./logictron.py
```

### Vídeo do Logictron!
Você pode conferir o funcionamento do Logictron no vídeo a seguir:

https://drive.google.com/file/d/1D3GnBAxG4xk96Rlbggdd_dQY_qJkwfLN/view?usp=sharing

## ERRO GRAVE em Logictron?
Se você viu o vídeo, percebeu que o Logictron falhou conceitualmente em simular a porta lógica XOR. Mas por que isso aconteceu?

### Motivo do erro
O erro ocorre devido a natureza linear do perceptron. Pela porta XOR inserir um problema a ele, que não é linearmente separável, o modelo não consegue traçar uma única linha reta (ou um hiperplano em espaços com mais dimensões) para separar os exemplos positivos dos exemplos negativos.

### Resolvendo o problema
O problema pode ser superado com a utilização de redes neurais mais complexas, como as redes neurais multicamadas, que são capazes de aprender funções não linearmente separáveis e, portanto, podem representar com sucesso a lógica da porta XOR.

Após o erro, foi usada uma lógica parecida, utilizando agora 2 Logictrons para simular a porta XOR. Um foi responsável pela simulação da porta NAND e o outro pela AND. A predição conjunta dessas duas portas, no final, faz o mesmo efeito da porta lógica XOR, e assim o erro foi contornado e superado por mais inserções de neurônios artificiais.



