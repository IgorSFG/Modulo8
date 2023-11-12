# Modulo8
Repositório para as atividades do modulo 8 do Inteli.

## Atividades
Você pode conferir os projetos das atividades a seguir.

### [POND2: Mapenado e navegando com Tartabot!](https://github.com/IgorSFG/Modulo8/tree/main/src/pond2)
Tartabot tem a função de mapear um local e depois navegar por ele através de coorenadas previamente estabelecidas. Ele foi criado como uma aplicação utilizando de pacotes ROS e launchers.

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
