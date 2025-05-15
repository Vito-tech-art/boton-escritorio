# Botón-Escritorio

¡Un ejecutable divertido que pone a prueba tu paciencia (y tu puntería)!

Este pequeño programa muestra un botón escurridizo que dice "Haz clic aquí"... pero no es tan fácil como parece. Cada vez que el ratón se acerca, el botón huye. Pero, ¡no te preocupes!: como todos nosotros, el botón también se cansa... 😩

## 🧠 ¿Cómo funciona?

- El botón huye cuando el cursor se acerca.
- Tiene **10 puntos de energía**.
- Cuando se le acaba la energía, se **queda quieto durante 5 segundos** para descansar. 😩
- Luego vuelve a moverse como si nada.
- Si logras hacer clic en él, te dice: **¡Lo lograste!**
- Una vez que lo logras puedes hacer clic en la X para cerrar el botón y el ejecutable.

## 🛠️ Compilación automática

Este repositorio incluye un flujo de trabajo con **GitHub Actions** que:

1. Instala las dependencias necesarias (`pyqt5` y `pyinstaller`)
2. Compila automáticamente el archivo `boton_escritorio.py` en un `.exe`
3. Sube el archivo ejecutable como artefacto descargable

## 🚀 Ejecutable

Cuando el flujo de trabajo se complete, podrás descargar el `.exe` desde la pestaña **Actions → Artifacts** en GitHub.

## 📦 Requisitos

Si quieres ejecutarlo localmente (sin compilar):

- Python 3.x
- PyQt5

```bash
pip install pyqt5
python boton_escritorio.py
```

## 😄 ¿Por qué?

Porque a veces un poco de humor en el escritorio es justo lo que necesitamos.

---

Hecho con ❤️ y un poco de cansancio.
