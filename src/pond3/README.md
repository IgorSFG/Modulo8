# Conversando com o Chatbot!
Chatbot tem como função responder as requisições dos usuários. Aqui, você manda o robô ir até um local e ele passa o feedback de estar indo até lá. O projeto foi desenvolvido como uma aplicação de pacote em ROS para simular a movimentação do robô via comandos no terminal.

## Compilação do pacote e determinando variáveis
Para que o pacote funcione, é necessário compilá-lo, para torná-lo pronto para a execução em sua versão mais recente, e ajustar suas variáveis para o ROS utilizar suas utilidades. No diretório `Modulo8`, rode os seguintes comandos:
```
colcon build --packages-select pond3
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
```

## Chatbot em Ação!
Para conversar com o chatbot, e direcionar o robô, rode o seguinte comando:
```
ros2 run pond3 chatbot
```

### Vídeo do Chatbot!
Você pode conferir o funcionamento do Chatbot no vídeo a seguir:

https://drive.google.com/file/d/1848-4krpegM1NLi1aeCP9FUqGI7zMQol/view?usp=sharing

