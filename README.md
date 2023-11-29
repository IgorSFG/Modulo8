# Modulo8
Repositório para as atividades do modulo 8 do Inteli.

## Instalação do Pacote ROS
Para a instalação do pacotes criados ao longo do Modulo8, reponsável pelas funcionalidades das atividades, devem ser seguidos os seguintes passos.

### Instalções necessárias para o funcionamento das Atividades:
```
Ubuntu
ROS
Nav2
```

### Clonar o Github e baixar dependências:
Rode os seguintes comandos para clonar o github e baixar as dependências:
```
git clone https://github.com/IgorSFG/Modulo8.git
rosdep install -i --from-path src --rosdistro humble -y
```

Caso necessite, baixe as seguintes bibliotecas:
```
sudo apt install git -y
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
pip install setuptools==58.2.0
```

## Atividades
Você pode conferir os projetos das atividades a seguir.

### [POND2: Mapeando e navegando com Tartabot!](https://github.com/IgorSFG/Modulo8/tree/main/src/pond2)
Tartabot tem a função de mapear um local e depois navegar por ele através de coorenadas previamente estabelecidas. Ele foi criado como uma aplicação utilizando de pacotes ROS e launchers.

### [POND3: Conversando com Chatbot!](https://github.com/IgorSFG/Modulo8/tree/main/src/pond3)
Chatbot tem como função responder as requisições dos usuários. Aqui, você manda o robô ir até um local e ele passa o feedback de estar indo até lá. O projeto foi desenvolvido como uma aplicação de pacote em ROS para simular a movimentação do robô via comandos no terminal.

### [POND4: Pesquisando com Llama!](https://github.com/IgorSFG/Modulo8/tree/main/src/pond4)
Llama vem com instruções customizadas para ajudar um usuário a pesquisar normas de segurança em ambientes industriais. O sisema contém uma interface gráfica, concebido pela biblioteca em python `gradio` e responde de forma sucinta e clara graças ao Large Language Model (LLM) `orca-mini`.

### [POND5: Pesquisando e Contextualizando com Llama5!](https://github.com/IgorSFG/Modulo8/tree/main/src/pond5)
Llama5 é uma evolução de [Llama](https://github.com/IgorSFG/Modulo8/tree/main/src/pond4). Ele ajuda na pesquisa de normas de segurança em ambientes industriais com a adição de contextualizar páginas web para ajudar na resposta final. O sisema contém uma interface gráfica, concebido pela biblioteca em python `gradio` e responde de forma sucinta e clara graças ao Large Language Model (LLM) `orca-mini`.

### [POND6: Logicando com Logictron!](https://github.com/IgorSFG/Modulo8/tree/main/src/pond6)
Logictron foi desenvolvido como uma aplicação em python baseado em perceptrons, os primeiros modelos de neurônios artificiais que serviram de conceito fundamental no campo da inteligência artificial. Logictron é capaz, através de um treinamento prévio, simular o comportamento das portas lógicas AND, OR, NAND e XOR e suas utilizações.

## Anotações
Anotações importantes decorretes do Modulo8.

### Comandos recorrentes
#### Teleop
```
ros2 run turtlebot3_teleop teleop_keyboard
```

#### Gazebo
```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

#### Cartographer
```
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True 
```
`use_sim_time:=False` para o robô real

#### SaveMap
```
ros2 run nav2_map_server map_saver_cli -f <nome-do-mapa>
```

#### Nav2
```
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=<arquivo-do-mapa>.yaml
```
