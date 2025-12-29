# SmartSight Project - Camera Test

# Notwendige Bibliotheken importieren
import cv2  # OpenCV für Bildverarbeitung und Videoaufnahme

# Pi-Kamera initialisieren
cap = cv2.VideoCapture(0)  # Pi-Kamera öffnen (Index 0)

# Überprüfen, ob die Kamera erfolgreich geöffnet wurde
if not cap.isOpened():
    print("[FEHLER] Zugriff auf die Kamera nicht möglich.")
    exit()

print("[INFO] Kamera funktioniert. Drücke 'q', um zu beenden.")

# Hauptschleife, um das Video aufzunehmen und anzuzeigen
while True:
    ret, frame = cap.read()  # Frame von der Kamera aufnehmen

    # Wenn das Frame nicht erfolgreich aufgenommen wurde, Schleife beenden
    if not ret:
        print("[FEHLER] Frame konnte nicht aufgenommen werden.")
        break

    # Das aufgenommene Frame anzeigen
    cv2.imshow('Kamera-Test - Drücke q zum Beenden', frame)

    # Schleife beenden, wenn 'q' gedrückt wird
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera freigeben und alle OpenCV-Fenster schließen
cap.release()
cv2.destroyAllWindows()
