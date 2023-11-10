# Mapenado e movimentando com TARTABOT!

## Instalação do Pacote ROS
Para a instalação do pacote pond2, reponsável pelas funcionalidades do tartabot, devem ser seguidos os seguintes passos.

### Dependências:
```
Ubuntu
ROS
Nav2
Workspace
rosdep
setuptools
```

### Clonar o Github e baixar dependências:
Em seu workspace, no diretório `src`, rode os seguintes comandos:
```
git clone https://github.com/IgorSFG/Modulo8.git
cd ..
rosdep install -i --from-path src --rosdistro humble -y
```

### Compilação do pacote e determinando variáveis
Para que o pacote funcione, é necessário compilá-lo, para torná-lo pronto para a execução em sua versão mais recente, e ajustar suas vairiáveis necessárias para o ROS utilizar das suas utilidades.
```
colcon build --packages-select pond2
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
```

### Mapeamento do Mundo:
```
ros2 launch pond2 mapping_launch.py
```
