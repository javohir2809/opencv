import cv2
import numpy as np

# Ovozni aniqlash uchun funktsiya
def detect_voice(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Ovozni aniqlash uchun kerakli logika va ishlar

    return voice_detected

# Videofaylni ochish
video = cv2.VideoCapture(0)  # 0 - kamera uchun indeks

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Ovozni aniqlash
    voice_detected = detect_voice(frame)

    # Natijani ekranga chiqarish
    if voice_detected:
        cv2.putText(frame, "Ovoz aniqlandi!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Ovqatlanuvchini ekraning o'ng yuqorisiga chiqarish
    cv2.imshow("Ovoz bilan boshqariladi", frame)

    # "q" tugmasini bosganda dasturdan chiqish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Barcha resurslarni tozalash
video.release()
cv2.destroyAllWindows()