# Arduino LED Control

Esse projeto foi feito usando Python 3.11 e PyQt


<div align="justify">
Através da conexão USB é possível enviar comandos para o Arduino (ou outro microcontrolador) e então acionar ou ler suas portas. 
Nesse exemplo foi implementado uma lista suspensa com as portas COM disponíveis, um botão para Refresh na qual atualiza a lista caso você tenha conectado/desconectado um novo dispositivo e uma segunda lista com os baudrates que mais uso em meus projetos.
</div>

<br>

<div align="center">
<img src = "https://user-images.githubusercontent.com/93883349/214727183-10fc58c7-aa70-40c9-86b8-0c63a2af31cd.gif"/>
</div>

<br>

<div align="justify">
Assim que selecionar a COM e o baud correto e clicar em “Connect”, a conexão será estabelecida e os botões “LED ON” e “LED OFF” serão habilitados. Ao serem clicados, o comando correspondente é enviado ao Arduino e o LED da placa (ou da porta escolhida) acenderá ou apagará. Ao clicar em "Desconnect" a conexão será encerrada. 
</div>

<br>

<div align="center">
<img src = "https://user-images.githubusercontent.com/93883349/214727467-bfd7ff19-bb8b-40f8-82c4-05b9289b2988.gif"/>
</div>

# Pré requisisitos para rodar

* Python 3.11 ou mais recente
* Instalar PyQt (pip install PyQt6)
* Arduino Uno, Nano ou semelhantes
