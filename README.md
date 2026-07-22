#Formula de prestamos

Este proyecto es una aplicación de escritorio desarrollada con **Tkinter**.

## Table of content
1. [Overview](https://github.com/daviidco/FormulaPrestmo/src/master/#Overview)  
2. [Requirements](https://github.com/daviidco/FormulaPrestmo/src/master/#Requirements)
3. [Download](https://github.com/daviidco/FormulaPrestmo/src/master/#Download)
4. [Distributing](https://github.com/daviidco/FormulaPrestmo/src/master/#Distributing)
5. [Run project](https://github.com/daviidco/FormulaPrestmo/src/master/#Run_project")
6. [Troubleshooting](https://github.com/daviidco/FormulaPrestmo/src/master/#Troubleshooting)

## 	📜 Overview

Es una herramienta basica para calcular el costo de un prestamo. 
Fue desarrollada con **Python** como lenguaje de principal y con **Tkinter**
como libreria par ser usada como aplicación de escritorio.

La fórmula para calcular cuota fija mensual préstamo:


![equation](ecuation.png)
## ✅ Requirements

1. Python (version 3.9.5)
   
Tools to develop
1. PyCharm 2021.1.1 (Community Edition)



## ⬇️ Download
Clone project with ssh key:
```
git@github.com:daviidco/FormulaPrestmo.git
```
or clone project using https:
```
https://github.com/daviidco/FormulaPrestmo.git
```


## ⚙️ Distributing


## ▶️ Run project

```
python main.py
```

## 🛠️ Troubleshooting

### macOS: `ModuleNotFoundError: No module named '_tkinter'`

Si al ejecutar `python main.py` en macOS obtienes:

```
File ".../lib/python3.13/tkinter/__init__.py", line 38, in <module>
    import _tkinter
ModuleNotFoundError: No module named '_tkinter'
```

**Causa:** el Python instalado (típicamente vía `pyenv`) se compiló sin soporte para Tcl/Tk, porque la librería `tcl-tk` no estaba instalada en el sistema al momento de compilar. Tkinter depende de la extensión nativa `_tkinter`, que solo se genera si el compilador la encuentra durante el build de Python.

**Solución:**

1. Instala `tcl-tk` con Homebrew:
   ```
   brew install tcl-tk
   ```

2. Reinstala la versión de Python con pyenv, indicándole dónde está `tcl-tk` (ajusta la ruta si usas Apple Silicon: `/opt/homebrew/opt/tcl-tk`):
   ```
   export PATH="/usr/local/opt/tcl-tk/bin:$PATH"
   export LDFLAGS="-L/usr/local/opt/tcl-tk/lib"
   export CPPFLAGS="-I/usr/local/opt/tcl-tk/include"
   export PKG_CONFIG_PATH="/usr/local/opt/tcl-tk/lib/pkgconfig"

   pyenv uninstall 3.13.7
   pyenv install 3.13.7
   ```

3. Verifica que tkinter quedó disponible:
   ```
   python3 -c "import tkinter; print('tkinter OK')"
   ```

> ⚠️ Reinstalar la versión de Python con pyenv borra los paquetes `pip` instalados en ese entorno. Si esa versión de Python la usas también en otros proyectos (entorno global), haz un respaldo antes con `pip freeze > backup.txt` y restáuralo después con `pip install -r backup.txt`.

### Al restaurar paquetes con `pip install -r backup.txt`: `No matching distribution found for torch`

Si tu entorno global tenía instalado `sentence-transformers` (u otro paquete que dependa de `torch`), al restaurar el backup puede fallar así:

```
ERROR: Could not find a version that satisfies the requirement torch>=1.11.0 (from sentence-transformers)
ERROR: No matching distribution found for torch
```

**Causa:** `pip install -r archivo.txt` instala todo en una sola transacción — si un solo paquete no tiene wheel disponible, **aborta la instalación completa** y no se instala nada del archivo. En Macs Intel (x86_64) esto ocurre porque PyTorch dejó de publicar wheels para esa arquitectura en versiones recientes.

**Solución:** excluye del archivo de backup el/los paquetes problemáticos e instala el resto por separado:

```
grep -v "^sentence-transformers==" backup.txt > backup-filtrado.txt
pip install -r backup-filtrado.txt
```

El paquete excluido (`sentence-transformers` en este caso) solo podrá reinstalarse si existe una versión de `torch` compatible con tu arquitectura y versión de Python.