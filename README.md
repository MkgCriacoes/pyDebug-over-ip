# pyDebug-over-ip
Depurar aplicações python através de outro PC (via internet)
Usando Flask e requests

- Uma boa para quando for fazer sistemas de automação, ou outro script que precise que ninguém mexa no PC durante o processo
- Apenas um PC, roda a aplicação principal; mas
- Dois PCs exibem o print

## Para usá-lo é simples:
### Instalar dependencias
- Instale usando o pip:
```python
pip install -r requeriments.txt
```
- Ou simplesmente, copie o env, e ative com:
```console
env\Scripts\activate
```

### No computador que deseja ver apenas os prints
- Execute o arquivo python "debug_server.py"
- E verifique o ip desse PC, através do comando:

(linux e mac)
```console
ifconfig
```
(windows)
```cmd
ipconfig
```

### No computador que deseja iniciar a aplicação
- Modifique o arquivo python "debug.py"
- Procure pela linha, e substitua "localhost" pelo ip do computador mestre:
```python
host = "localhost:8080"
```
- Substitua a ultima linha, pelo nome do script principal
- Execute o debug.py, e sua aplicação será iniciada:
```console
python debug.py
```

## Obs: No momento só consegue interpretar execuções do metodo print
