# test_qr.py
from app.utils.qr import open_qr_scanner

data = open_qr_scanner()
if data:
    print(f"✅ Código leído: {data}")
else:
    print("❌ No se detectó ningún QR.")