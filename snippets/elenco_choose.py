# crea un compito dalle domande
import os

elenco = os.listdir()
[print(n,i) for n,i in enumerate(elenco) if i.endswith(".txt")]
_range = f"0-{len(elenco)-1}"
scelta = int(input(f"------\n>Scegli compito num.[{_range}]>>>"))
print(elenco[scelta])
