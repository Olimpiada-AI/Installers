
# OlimpiadaAI - Instalator Windows 
(in mare parte compatibil si cu Mac/Ubuntu; todo next)

Acest proiect automatizează instalarea și verificarea completă a unui mediu Python pentru inteligență artificială, procesare de date și competiții educaționale.

---

## 📁 Fișiere incluse

| Fișier                       | Descriere                                                                 |
|------------------------------|---------------------------------------------------------------------------|
| `setupONIAenv.py`            | Script Python care instalează mediul virtual și pachetele necesare        |
| `requirements_3.txt`         | Lista tuturor pachetelor Python necesare                                  |
| `packages_to_check.py`       | Script de test pentru importul pachetelor                                 |
| `start_onia_env.cmd`         | Script CMD pentru activarea rapidă a mediului și setarea variabilelor     |
| `install_oni_utils.bat`      | Script pentru instalare python 3.11.5 si VSCode                           |

---
## 🔄 Instalare completă
- Cloneaza sau downloadeaza acest repository
- Deschide un terminal PowerShell/CMD în acest folder (ca administrator)
 
- Daca nu ai nici o versiune de Python sau nici VSCode, ruleaza intai:
- ```install_oni_utils.bat``` din terminal. Daca deja sunt instalate (ATENTIE, nu este nevoie pe PC-uri la FMI) se poate da skip acest pas.
   Altfel, se va instalat local python 3.11.5 si VSCode.

- Apoi ruleaza: 
  ```
  python setupONIAenv.py
  ```
  
- Cerinte: **Python 3.11.5**  - versiune recomandată la momentul actual. Daca exista orice alta versiune se va instala, daca sunteti de acord aceasta versiune automat (va trebui insa sa inchideti terminalul si sa rulati scriptul din nou).
  (In mod deosebit PC-urile din FMI au instalat deja 3.13, asa ca se va instala aditional noua versiune).
```
[2025-05-14 15:30:57] [ERROR] Versiunea Python 3.11.5 este necesară. Detectat: 3.13.1
❓ Vrei să instalăm automat Python 3.11.5 acum? [y/n]: y
[2025-05-14 15:31:01] [INFO] Descărcare installer Python 3.11.5...
[2025-05-14 15:31:09] [OK] Installer descărcat.
[2025-05-14 15:31:09] [INFO] Instalare Python 3.11.5 în mod silențios...
[2025-05-14 15:31:32] [OK] Python 3.11.5 instalat.
[2025-05-14 15:31:32] [INFO] Vă rugăm să închideți și să redeschideți terminalul înainte de a continua.
PS C:\Users\Student\Installers-main> python .\setupONIAenv.py
```

Pentru dezintalare sau reluarea procesului in caz de eroare:
```
python setupONIAenv.py --clean
```


##  Activarea mediului

Rulează:

```
start_onia_env.cmd
```
TODO: ar fi bine sa punem o poza cum se foloseste si din VSCode.


## Detalii tehnice (optionale):

Scriptul va:

1. Crea mediul virtual `C:\ONIAenv`
2. Instala toate pachetele din `requirements_3.txt`
3. Descărca toate datele NLTK
4. Păstra jurnalul în `install_log.txt`
5. Testa importurile și Jupyter Lab
6. Configura variabila `TF_ENABLE_ONEDNN_OPTS=0` pentru TensorFlow
7. Instaleaza plugin-ul de jupyter pentru VSCode.
---

Acesta va:

- Activează mediul virtual `C:\ONIAenv`
- Setează variabila `TF_ENABLE_ONEDNN_OPTS=0`
- Deschide un nou terminal activat

- Dacă TensorFlow afișează avertismente legate de oneDNN, acestea sunt gestionate automat.
- Toate acțiunile sunt salvate în `install_log.txt` pentru depanare.

---

© ONIA 2025 · Utilizare educațională · Universitatea din București 🇷🇴
