
# ONIA - Instalator Mediu AI 🧠🇷🇴

Acest proiect automatizează instalarea și verificarea completă a unui mediu Python pentru inteligență artificială, procesare de date și competiții educaționale (ex: ONIA).

---

## 📁 Fișiere incluse

| Fișier                       | Descriere                                                                 |
|------------------------------|---------------------------------------------------------------------------|
| `setupONIAenv.py`            | Script Python care instalează mediul virtual și pachetele necesare        |
| `requirements_3.txt`         | Lista tuturor pachetelor Python necesare                                  |
| `packages_to_check.py`       | Script de test pentru importul pachetelor                                 |
| `start_onia_env.cmd`         | Script CMD pentru activarea rapidă a mediului și setarea variabilelor     |
| `install_log.txt`            | (Generat automat) Jurnal al instalării și testelor                        |

---

## 🔧 Cerințe minime

- ✅ **Python 3.11.5** (versiune recomandată)
- ✅ Windows 10 / 11
- ✅ Conexiune la internet (pentru descărcarea pachetelor)
- ✅ Permisiuni de scriere în `C:\`

---

## 🔄 Instalare completă

Deschide un terminal CMD sau PowerShell în acest folder și rulează:

```
python setupONIAenv.py
```

Dacă nu ai versiunea exactă de Python 3.11.5, poți forța instalarea cu:

```
python setupONIAenv.py --ignore-version
```

Scriptul va:

1. Crea mediul virtual `C:\ONIAenv`
2. Instala toate pachetele din `requirements_3.txt`
3. Descărca toate datele NLTK
4. Păstra jurnalul în `install_log.txt`
5. Testa importurile și Jupyter Lab
6. Configura variabila `TF_ENABLE_ONEDNN_OPTS=0` pentru TensorFlow

---

## ✅ Verificarea mediului

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

## 🧠 Activarea mediului

Rulează:

```
start_onia_env.cmd
```

Acesta:

- Activează mediul virtual `C:\ONIAenv`
- Setează variabila `TF_ENABLE_ONEDNN_OPTS=0`
- Deschide un nou terminal activat

---

## ℹ️ Alte detalii

- Dacă TensorFlow afișează avertismente legate de oneDNN, acestea sunt gestionate automat.
- Toate acțiunile sunt salvate în `install_log.txt` pentru depanare.

---

© ONIA 2025 · Utilizare educațională · Universitatea din București 🇷🇴
