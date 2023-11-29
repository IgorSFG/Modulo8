# Pesquisando com Llama!
Llama vem com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sisema contém uma interface gráfica, concebido pela biblioteca em python `gradio` e responde de forma sucinta e clara graças ao Large Language Model (LLM) `orca-mini`.

## Configurando Llama!
É recomendado para o pleno funcionamento do Llama 8GB de RAM. Para utilizar o LLM, primeiro temos que instala-lo na sua máquina. Antes de mais nada, confira se você tem `langchain`, `ollama` e o modelo `orca-mini` instalados. Então, em `Modulo8` rode:
```
cd src/pond4/pond4
chmod -R o+rx .
ollama create llama -f modelfile
cd ../../..
```

## Compilando Llama e determinando variáveis!
Llama foi criado como um pacote em ROS, que para funcionar, é necessário compilá-lo, para torná-lo pronto para a execução em sua versão mais recente, e ajustar suas variáveis para o ROS utilizar suas funções. No diretório `Modulo8`, rode os seguintes comandos:
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
Você pode conferir o funcionamento do llama no vídeo a seguir (o vídeo foi editado afim de dinamizar os processos das respostas do LLM):

https://drive.google.com/file/d/1Ag2HqNkmgHrPEb0N_OcxD8q8SRnU-KXH/view?usp=sharing


