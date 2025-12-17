import http.server
import socketserver
import json
import os

PORT = 80
WINNER_NAME = None

class DedSecHandler(http.server.SimpleHTTPRequestHandler):
    
    # --- GESTIONAR PETICIONES GET (Cargar webs o preguntar estado) ---
    def do_GET(self):
        global WINNER_NAME
        
        # 1. ¿Es la petición especial del panel del profesor?
        if self.path == '/check_winner_status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*') # Evita bloqueos CORS
            self.end_headers()
            response = {"winner": WINNER_NAME}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return # Cortamos aquí para no intentar buscar un archivo con este nombre

        # 2. Ignorar el icono del navegador (para ensuciar menos la consola)
        if self.path == '/favicon.ico':
            self.send_response(204)
            return

        # 3. Si no es nada de lo anterior, es un ARCHIVO (.html, .css, .js)
        # Imprimimos qué está pidiendo el alumno
        print(f"📥 Petición recibida: {self.path}")
        
        # Verificamos si el archivo existe antes de servirlo
        # (Quitamos la barra inicial '/' para buscar en la carpeta local)
        file_path = self.path.lstrip('/')
        if self.path == '/':
            file_path = 'index.html' # Si piden la raíz, buscamos index.html
            
        # Intentamos servirlo con el método estándar
        try:
            super().do_GET()
        except Exception as e:
            print(f"❌ ERROR CRÍTICO sirviendo {self.path}: {e}")

    # --- GESTIONAR PETICIONES POST (Cuando un alumno gana) ---
    def do_POST(self):
        global WINNER_NAME
        
        if self.path == '/game_over':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            team_name = post_data.decode('utf-8')
            
            response_msg = ""
            
            if WINNER_NAME is None:
                WINNER_NAME = team_name
                print(f"\n🚨🚨🚨 ¡GANADOR CONFIRMADO! Equipo: {team_name} 🚨🚨🚨\n")
                response_msg = "WINNER"
            else:
                print(f"⚠️ Llegada tardía: {team_name}")
                response_msg = "LATE"

            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_msg.encode('utf-8'))
        else:
            super().do_POST()

print(f"💀 SERVIDOR DEDSEC INICIADO EN: http://localhost:{PORT}")
print(f"📂 Sirviendo archivos desde: {os.getcwd()}")
print("---------------------------------------------------------")

# Configuración para permitir reutilizar el puerto si reinicias rápido
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), DedSecHandler) as httpd:
    httpd.serve_forever()