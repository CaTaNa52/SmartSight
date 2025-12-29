# SmartSight Project - Cat Detection

# Notwendige Bibliotheken importieren
import cv2                   # OpenCV für Bildverarbeitung und Videoaufnahme
import numpy as np           # NumPy für numerische Operationen

# Pi-Kamera initialisieren (Kameraindex 0 verwenden)
cap = cv2.VideoCapture(0)

# Überprüfen, ob die Kamera erfolgreich geöffnet wurde
if not cap.isOpened():
    print("[FEHLER] Zugriff auf die Kamera nicht möglich.")
    exit()

# Vorgefertigten Haar-Cascade-Klassifikator für Ganzkörpererkennung laden
# Stelle sicher, dass der Pfad zur haarcascade-Datei korrekt ist
cat_cascade = cv2.CascadeClassifier('./assets/haarcascade_fullbody.xml')

# Überprüfen, ob der Classifier korrekt geladen wurde
if cat_cascade.empty():
    print("[FEHLER] Haar-Cascade-Klassifikator konnte nicht geladen werden.")
    exit()

# Hauptschleife, um Frames aufzunehmen und Katzen zu erkennen
while True:
    # Frame von der Kamera aufnehmen
    ret, frame = cap.read()
    
    # Wenn das Frame nicht erfolgreich aufgenommen wurde, Schleife beenden
    if not ret:
        print("[FEHLER] Frame konnte nicht aufgenommen werden.")
        break

    # Frame in Graustufen umwandeln für die Erkennung
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Katzen (Ganzkörper) im Graustufenbild erkennen
    cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Rechtecke um erkannte Katzen zeichnen
    for (x, y, w, h) in cats:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blaues Rechteck

    # Das Ergebnisframe mit erkannten Katzen anzeigen
    cv2.imshow('SmartSight - Katzenerkennung', frame)

    # Schleife beenden, wenn 'q' gedrückt wird
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera freigeben und alle OpenCV-Fenster schließen
cap.release()
cv2.destroyAllWindows()
