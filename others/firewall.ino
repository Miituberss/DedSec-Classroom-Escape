const int ledPin = 13;

void setup() {
  // --- FASE 1: VELOCIDAD ESTÁNDAR (9600) ---
  // Esto es lo que verán al principio
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  for (int i = 0; i < 10; i++) {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
  }

  Serial.println(">> INICIALIZANDO HARDWARE FIREWALL...");
  delay(1000);
  Serial.println(">> CONECTANDO CON SERVIDOR BLUME...");
  delay(1000);
  Serial.println(">> CONEXIÓN ESTABLECIDA.");
  delay(1000);
  
  // --- LA PISTA ---
  // Les damos un aviso antes de "desaparecer" en el ruido
  Serial.println(">> [ALERTA] INTRUSIÓN DETECTADA!!.");
  Serial.println(">> RECONFIGURANDO EN 3...");
  delay(1000);
  Serial.println(">> 2...");
  delay(1000);
  Serial.println(">> 1...");
  delay(1000);
  
  // --- EL TRUCO ---
  Serial.end();         // Cerramos la conexión de 9600
  delay(100);
  Serial.begin(2400); // Abrimos la conexión rápida
  digitalWrite(ledPin, HIGH);
  delay(1000);
}

void loop() {

  // --- FASE 2: VELOCIDAD ALTA (115200) ---
  // Si el alumno no cambia el monitor a 115200, verá: ⸮⸮⸮f⸮⸮ (Ruido)
  
  digitalWrite(ledPin, HIGH); // Parpadeo visual
  
  Serial.println(">> [CANAL SEGURO] TOKEN DE ACCESO:");
  Serial.println("BLUME_XMAS_OVERRIDE_99"); 
  Serial.println("------------------------------------------");
  
  digitalWrite(ledPin, LOW);
  
  // Enviamos cada 2 segundos
  delay(2000);
}