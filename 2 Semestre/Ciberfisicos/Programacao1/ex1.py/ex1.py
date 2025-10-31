Python

#!/usr/bin/env python3

import threading
import time
import random

def minha_thread(n):
    t = random.randint(1, 3)
    time.sleep(t)
    print(f"Thread {n} acordou depois de {t}s")

# Lançando 10 threads
for i in range(10):
    threading.Thread(target=minha_thread, args=(i,)).start()

print("Threads lançadas")

 

HTML

<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Projeto Monitor-Sensores com Python</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    table { width: 100%; border-collapse: collapse; margin-bottom: 30px; }
    th, td { border: 1px solid #ccc; padding: 10px; }
    th { background-color: #f2f2f2; }
    pre { background: #f8f8f8; padding: 10px; border: 1px solid #ddd; overflow-x: auto; }
  </style>
</head>
<body>
  <h1>Introdução a Processos e Threads em Python</h1>

  <h2>Lançamento de uma Thread</h2>
  <pre>
import threading

t = threading.Thread(target=nome_da_função, args=(arg1,))
t.start()

# ou

threading.Thread(target=nome_da_função, args=(arg1, arg2)).start()
  </pre>

  <h2>Exemplo 1: Multithreading</h2>
  <pre>
#!/usr/bin/env python3

import threading
import time
import random

def minha_thread(n):
    t = random.randint(1, 3)
    time.sleep(t)
    print(f"Thread {n} acordou depois de {t}s")

for i in range(10):
    threading.Thread(target=minha_thread, args=(i,)).start()

print("Threads lançadas")
  </pre>

  <h3>Descrição</h3>
  <ul>
    <li>A função <code>minha_thread(n)</code> é lançada 10 vezes como thread.</li>
    <li>Ela dorme por tempo aleatório entre 1 e 3 segundos.</li>
    <li>Ao acordar, imprime seu número e o tempo dormido.</li>
    <li>O processo principal imprime "Threads lançadas" após iniciar todas.</li>
  </ul>

  <h2>Serialização do Código</h2>
  <p>O lançamento de uma thread <strong>não altera</strong> o fluxo do programa principal.</p>
  <p>O programa segue sua execução enquanto as threads rodam em paralelo.</p>

  <p><strong>Exemplo de uso de join() para sincronizar:</strong></p>
  <pre>
A = threading.Thread(target=func_A)
B = threading.Thread(target=func_B)

# Executar em paralelo
A.start()
B.start()
A.join()
B.join()
# continua após A e B terminarem

# Executar em série
A.start()
A.join()
B.start()
B.join()
# continua após A e B terminarem sequencialmente
  </pre>
</body>
</html>