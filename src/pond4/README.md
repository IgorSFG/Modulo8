# Pesquisando com Llama!
Llama vem com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sisema contém uma interface gráfica e responde de forma sucinta e clara as suas requisições.

## Configurando Llama!
Para que o modelo de IA de Llama funcione, primeiro temos que instala-lo na sua máquina. Primeiro, confira se você tem `langchain`, `ollama` e o modelo `dolphin2.2-mistral` instalados. Então, em `Modulo8/src/pond4/pond4` rode:
```
chmod -R o+rx .
ollama create llama -f modelfile
cd ../../..
```

## Compilando Llama e determinando variáveis!
Llama foi criado como um pacote em ROS, que para funcionar, é necessário compilá-lo, para torná-lo pronto para a execução em sua versão mais recente, e ajustar suas variáveis para o ROS utilizar suas utilidades. No diretório `Modulo8`, rode os seguintes comandos:
```
colcon build --packages-select pond4
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
```

## Llama em Ação!
Para pesquisar normas de segurança com Llama, rode o seguinte comando:
```
ros2 run pond4 llama
```

### Vídeo do Llama!
Você pode conferir o funcionamento do llama no vídeo a seguir:



