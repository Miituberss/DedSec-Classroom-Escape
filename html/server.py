import http.server
import socketserver
import json
import os
import threading

PORT = 80
WINNER_NAME = None
# Creamos un 'candado' para que dos hilos no escriban el ganador a la vez (Race Condition)
winner_lock = threading.Lock()

# --- CLASE PARA GESTIONAR HILOS (ESTA ES LA MAGIA) ---
class ThreadingSimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class DedSecHandler(http.server.SimpleHTTPRequestHandler):
    
    # --- GET: Para servir webs y que el profe consulte estado ---
    def do_GET(self):
        global WINNER_NAME
        
        # Panel del profesor preguntando estado
        if self.path == '/check_winner_status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*') 
            self.end_headers()
            response = {"winner": WINNER_NAME}
            try:
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except BrokenPipeError:
                pass # Si el navegador cierra rápido, ignoramos el error
            return

        if self.path == '/favicon.ico':
            self.send_response(204)
            return

        # Logs en consola (Opcional: puedes comentarlo si hay mucho spam)
        # print(f"📥 [{self.client_address[0]}] Pide: {self.path}")
        
        # Corrección de ruta raíz
        if self.path == '/':
            self.path = '/index.html'
            
        try:
            super().do_GET()
        except (ConnectionResetError, BrokenPipeError):
            pass # Ignoramos errores de desconexión habituales

    # --- POST: Cuando un alumno gana ---
    def do_POST(self):
        global WINNER_NAME
        
        if self.path == '/game_over':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                team_name = post_data.decode('utf-8')
                
                response_msg = ""
                
                # Usamos el candado para asegurar que solo UNO sea el primero
                with winner_lock:
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
            except Exception as e:
                print(f"Error en POST: {e}")
        else:
            super().do_POST()

print(f"💀 SERVIDOR DEDSEC (MULTIHILO) ACTIVO EN: http://localhost:{PORT}")
print(f"📂 Sirviendo archivos desde: {os.getcwd()}")
print("---------------------------------------------------------")

# Configuración para reutilizar puerto rápido
socketserver.TCPServer.allow_reuse_address = True

# AQUI ESTÁ EL CAMBIO: Usamos ThreadingSimpleServer en vez de TCPServer
with ThreadingSimpleServer(("", PORT), DedSecHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido manualmente.")
