
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

---

## 🔧 Cerințe minime

- ✅ **Python 3.11.5** (versiune recomandată la momentul actual, se poate instala cu scriptul automat vedeti mai jos)
- ✅ Windows 10 / 11
- ✅ Conexiune la internet (pentru descărcarea pachetelor)
- ✅ Permisiuni de scriere în `C:\`


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

---

## 🔄 Instalare completă
- Cloneaza sau downloadeaza acest repository
- Deschide un terminal CMD sau PowerShell în acest folder (ideal ca administrator) și rulează:

```
python setupONIAenv.py
```
  Daca nu aveti instalat Python 3.11.5, o sa vi se ceara acordul pentru instalare, apoi trebuie sa inchdeti terminalul si sa deschideti unul nou cu aceeasi comanda.

Pentru dezintalare sau reluarea procesului in caz de eroare:
```
python setupONIAenv.py --clean
```

Scriptul va:

1. Crea mediul virtual `C:\ONIAenv`
2. Instala toate pachetele din `requirements_3.txt`
3. Descărca toate datele NLTK
4. Păstra jurnalul în `install_log.txt`
5. Testa importurile și Jupyter Lab
6. Configura variabila `TF_ENABLE_ONEDNN_OPTS=0` pentru TensorFlow

---

## ✅ Verificarea mediului (Optional, deja se efectueaza in pasul anterior)
Poți verifica manual dacă totul funcționează cu:

```cmd
C:\ONIAenv\Scripts\python.exe packages_to_check.py
C:\ONIAenv\Scripts\python.exe -m jupyter lab
```

sau poți rula din nou:

```
python setupONIAenv.py
```

---

##  Activarea mediului

Rulează:

```
start_onia_env.cmd
```

Acesta va:

- Activează mediul virtual `C:\ONIAenv`
- Setează variabila `TF_ENABLE_ONEDNN_OPTS=0`
- Deschide un nou terminal activat

---

## ℹ️ Alte detalii

- Dacă TensorFlow afișează avertismente legate de oneDNN, acestea sunt gestionate automat.
- Toate acțiunile sunt salvate în `install_log.txt` pentru depanare.

---

© ONIA 2025 · Utilizare educațională · Universitatea din București 🇷🇴
