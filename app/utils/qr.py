import cv2
from pyzbar.pyzbar import decode
from PIL import Image

def open_qr_scanner():
    """
    Abre la cámara del PC y detecta códigos QR.
    Presiona 'q' para cerrar la cámara.
    """
    cap = cv2.VideoCapture(0)  # 0 = cámara por defecto
    found_data = None

    print("[INFO] Escaneando código QR... (presiona 'q' para salir)")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] No se pudo acceder a la cámara.")
            break

        for barcode in decode(frame):
            data = barcode.data.decode('utf-8')
            print(f"[QR DETECTADO] {data}")
            found_data = data
            cap.release()
            cv2.destroyAllWindows()
            return found_data

        cv2.imshow("Lector QR", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return found_data