# Mapenado e navegando com Tartabot!
Tartabot consiste em um pacote ROS com a função de mapear um local e depois navegar por ele através de coorenadas previamente estabelecidas.

## Instalação do Pacote ROS
Para a instalação do pacote pond2, reponsável pelas funcionalidades do tartabot, devem ser seguidos os seguintes passos.

### Instalções necessárias para o funcionamento do Tartabot:
```
Ubuntu
ROS
Nav2
```

### Clonar o Github e baixar dependências:
Caso necessite, baixe as seguintes dependências:
```
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
pip install setuptools==58.2.0
```
Em seu workspace, no diretório `src`, rode os seguintes comandos:
```
git clone https://github.com/IgorSFG/Modulo8.git
cd ..
rosdep install -i --from-path src --rosdistro humble -y
```

### Compilação do pacote e determinando variáveis
Para que o pacote funcione, é necessário compilá-lo, para torná-lo pronto para a execução em sua versão mais recente, e ajustar suas vairiáveis para o ROS utilizar suas utilidades.
```
colcon build --packages-select pond2
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
```

## Tartabot em Ação!
O Tartabot consiste em duas etapas de funcionamento. Primeiro é feito o mapeamento do local, para que o robô saiba como se deslocar por ele, e depois é feita a navegação, onde o robô irá passar por alguns pontos do mapa.

### Antes de Começar!
Averigue se você está no diretório do pacote "pond2". Em seu workspace, vá até `src/Modulo8/src/pond2`.

### Mapeamento do Mundo:
A primeira etapa do Tartabot é o mapeamento do mundo virtual. Para fazer isso, vamos rodar um launchfile utilizado:
```
ros2 launch pond2 mapping_launch.py
```
Um launchfile é responsável por rodar diversos pacotes/nós. O `mapping_lauch.py` ativa o `turtlebot3_cartographer`, `turtlebot3_gazebo`, `turtlebot3_teleop` e `pond2_teleop`, encarregados de realizar o mapeamento, simular o local e o robô, criar os controles para a sua movimentação e salvar o mapa criado, respectivamente.

Com o terminal `turtlebot3_teleop` em foco, movimente o robô de forma cadenciada, até que o mapa, no simulador `Rviz`, esteja completamente preenchido. Então, vá para o terminal do `pond2_teleop` e salve o mapa como instruído.

### Navegando pelo Mundo!
A segunda e última etapa do Tartabot é a navegação pelo mapa. Utilize o seguinte comando para rodar o próximo launchfile:
```
ros2 launch pond2 tarta_launch.py
```
O `tarta_launch.py` ativa o `turtlebot3_navigation2`, `turtlebot3_gazebo` e `pond2_tartabot`, encarregados de navegar pelo mapa designado, simular o ambiente e enviar as coordenadas de deslocamento, respectivamente.

### Vídeo do Tartabot!
Você pode conferir o funcionamento do Tartabot no vídeo a seguir: 

