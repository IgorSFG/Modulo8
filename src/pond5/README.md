# Pesquisando e Contextualizando com Llama5!
Llama5 é uma evolução de [Llama](https://github.com/IgorSFG/Modulo8/tree/main/src/pond4). Ele ajuda na pesquisa de normas de segurança em ambientes industriais com a adição de contextualizar páginas web para ajudar na resposta final. O sisema contém uma interface gráfica, concebido pela biblioteca em python `gradio` e responde de forma sucinta e clara graças ao Large Language Model (LLM) `orca-mini`.

## Configurando Llama5!
Llama é o modelo de linguagem utilizado em Llama5, e é recomendado para o seu pleno funcionamento 8GB de RAM. Para utilizar o LLM, primeiro temos que instala-lo na sua máquina. Antes de mais nada, confira se você tem `langchain`, `ollama` e o modelo `orca-mini` instalados. Então, em `Modulo8` rode:
```
cd src/pond5/pond5
chmod -R o+rx .
ollama create llama -f modelfile
cd ../../..
```

## Compilando Llama5 e determinando variáveis!
Llama5 foi criado como um pacote em ROS, que para funcionar, é necessário compilá-lo, para torná-lo pronto para a execução em sua versão mais recente, e ajustar suas variáveis para o ROS utilizar suas funções. No diretório `Modulo8`, rode os seguintes comandos:
```
colcon build --packages-select pond5
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
```

## Llama5 em Ação!
Para pesquisar normas de segurança utilizando contextualizações com Llama5, rode o seguinte comando:
```
ros2 run pond5 llama5
```

### Vídeo do Llama5!
Você pode conferir o funcionamento do llama no vídeo a seguir (o vídeo foi editado afim de dinamizar os processos das respostas do LLM):

https://drive.google.com/file/d/1FROB28lxUmECIpg_ZljsWkoUtVyGjsw8/view?usp=sharing


