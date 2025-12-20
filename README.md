# DedSec-Classroom-Escape

# 💀 Operación: Aula Desconectada (DedSec Escape Room)

![Status](https://img.shields.io/badge/Status-Active-success)
![Tech](https://img.shields.io/badge/Tech-HTML%20%7C%20JS%20%7C%20Python%20%7C%20Arduino-blue)
![Theme](https://img.shields.io/badge/Theme-Watch_Dogs_%2F_DedSec-black)

> "No es seguridad, es vigilancia. Blume Corp quiere controlar el aula. Únete a DedSec."

## 📄 Descripción

Este proyecto es un **Escape Room Educativo (CTF - Capture The Flag)** diseñado para estudiantes de **Robótica e Informática**. Combina desafíos digitales (web hacking, criptografía, redes) con desafíos físicos (Arduino).

El objetivo es enseñar conceptos técnicos de una forma inmersiva y gamificada, donde los alumnos actúan como reclutas de la organización hacker **DedSec** para detener la implementación del sistema de vigilancia **ctOS 3.0** en su academia.

## 🎯 Competencias Trabajadas

* **Redes:** Direcciones IP, Puertos, Cliente-Servidor.
* **Hardware (Arduino):** Comunicación Serie (UART), Baud Rates.
* **Web:** HTML básico, Inspección de elementos, Parámetros URL (GET).
* **Ciberseguridad:** Hashing, Codificación Base64, Esteganografía.
* **Lógica:** Resolución de problemas y trabajo en equipo.

---

## 🛠️ Estructura del Juego (Niveles)

El juego consta de una serie de fases secuenciales:

1.  **Fase 0: La Inyección (Intro)** 🎥
    * El profesor proyecta una intro estilo hacker.
    * Script en Bash (`hack_ip.sh`) simula un hackeo en vivo para revelar la IP del servidor local.
2.  **Fase 1: Acceso al Portal (`index.html`)** 🔐
    * Login corporativo.
    * *Solución:* Encontrar la contraseña escrita en texto plano en el código usando inspeccionar.
3.  **Fase 2: Escalada de Privilegios (`dashboard.html`)** 🛡️
    * Panel de control bloqueado para "Becarios".
    * *Solución:* Modificar la URL de `?role=intern` a `?role=admin`.
4.  **Fase 3: Firewall Físico (`firewall.html`)** 📟
    * Bloqueo de seguridad que requiere un Token OTP de hardware.
    * *Solución:* Conectar un Arduino y leer el puerto serie. **Truco:** El Arduino baja la velocidad a 2400 baudios (Stealth Mode), obligando al alumno a configurar el IDE correctamente para leer la clave.
5.  **Fase 4: Base de Datos (`database.html`)** 🗄️
    * Comando encriptado en Base64.
    * *Solución:* Decodificar la cadena para obtener el comando de apagado.
6.  **Fase 5: Payload Final (`final_payload.html`)** 💥
    * Confirmación de borrado.
    * *Solución:* Encontrar la clave oculta en el código fuente (texto negro sobre fondo negro).

---

## 🚀 Instalación y Despliegue

### Requisitos
* **Profesor (Servidor):** PC con Python 3 instalado.
* **Alumnos (Clientes):** Navegador web y Arduino IDE.
* **Hardware:** 1 Placa Arduino (Uno/Nano) + Cable USB.

### Pasos para el Profesor (Game Master)
1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Miituberss/DedSec-Classroom-Escape.git](https://github.com/Miituberss/DedSec-Classroom-Escape.git)
    cd DedSec-Classroom-Escape
    ```
   > [!WARNING]
   > Debido al tamaño de los archivos multimedia de alta calidad, los videos no están incluidos directamente en el código fuente (Source code.zip).  
   > Para que el juego funcione correctamente:  
   > Descarga el código fuente (Source code).  
   > Descarga los archivos de video adjuntos en esta Release:  
   > 📥 DedSecIni.mp4  
   > 📥 DedSecFin.mp4  
   > Mueve ambos videos a la carpeta raíz del proyecto (donde están los archivos .html).  

2.  **Preparar el Arduino:**
    * Abre `arduino_code/Firewall.ino`.
    * Cárgalo en la placa que usarán los alumnos.

3.  **Iniciar el Servidor:**
    * Ejecuta el script de servidor (gestiona la leaderboard y redirecciones).
    * **Nota:** Asegúrate de que todos los `.html` están en la misma carpeta.
    ```bash
    python3 server.py
    ```

4.  **Lanzar la Intro (Proyector):**
    * Abre `intro.html` en el PC del profesor.
    * Ejecuta el script de "Hackeo de IP" en la terminal para dar ambiente:
    ```bash
    chmod +x hack_ip.sh
    ./hack_ip.sh
    ```
    * Introduce la IP mostrada en la web de intro.

5.  **Panel de Control:**
    * Abre `final.html` en una segunda pestaña/monitor. Esta pantalla mostrará automáticamente al equipo ganador cuando completen el juego.

---

## 🔒 Seguridad Anti-Trampas

Para evitar que los alumnos "listillos" simplemente miren el código fuente (`Ctrl+U` o F12) para sacar las contraseñas, el sistema utiliza **Hashing Matemático (SimpleHash)**.

* Las contraseñas no están en texto plano en el Javascript.
* El sistema calcula el hash de lo que escribe el alumno y lo compara con un hash numérico pre-calculado.
* *Ejemplo:* `BLUME` se convierte en `638491` (irreversible fácilmente en clase).

## 📂 Archivos Clave

| Archivo | Función |
| :--- | :--- |
| `server.py` | Servidor HTTP Python. Gestiona quién gana primero y bloquea a los segundos. |
| `hack_ip.sh` | Script Linux (Bash) decorativo para obtener la IP local con estilo Matrix. |
| `intro.html` | Pantalla de bienvenida y vídeo introductorio. |
| `winner.html` | Pantalla de victoria para el primer equipo. |
| `mission_complete.html` | Pantalla para los equipos que llegan tarde. |

## 📸 Capturas

<img width="1917" height="924" alt="image" src="https://github.com/user-attachments/assets/f83389d9-b8ec-4f6b-8376-c5c56bdd4d83" />

<img width="770" height="675" alt="image" src="https://github.com/user-attachments/assets/7fbc5fc8-2652-4d8e-b679-d2a525ef1e5e" />


## 🤝 Contribuciones

Si tienes ideas para nuevos puzzles o mejoras en el código Arduino, ¡haz un Fork y envía tu Pull Request!

---

## ⚖️ Legal & Disclaimer

This project is created for **educational purposes only** (Classroom Gamification).

* **Code:** The source code (HTML, JS, Python, Arduino) is licensed under the **MIT License**.
* **Assets:** "Watch Dogs", "DedSec", "Blume", "ctOS" and related logos/characters are trademarks of **Ubisoft Entertainment**. This project is not affiliated with, endorsed by, or connected to Ubisoft.
* **Usage:** This material is intended for non-commercial use in educational environments.

*Este proyecto ha sido creado únicamente con fines educativos. Todas las marcas registradas (Watch Dogs, DedSec) pertenecen a Ubisoft. No se pretende infringir derechos de autor, sino utilizar la temática bajo el concepto de "Fair Use" para la docencia.*
