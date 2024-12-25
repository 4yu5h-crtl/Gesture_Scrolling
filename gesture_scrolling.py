import cv2
import mediapipe as mp
import numpy as np
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5)
cv2.namedWindow("Gesture Control", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gesture Control", 640, 480)

def recognize_gesture(frame):
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if not results.multi_hand_landmarks:
        return None
    
    hand_landmarks = results.multi_hand_landmarks[0]
    tips = [8, 12]
    bases = [6, 10]
    raised_fingers = sum(
        1 for tip, base in zip(tips, bases)
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[base].y
    )
    return "scroll_up" if raised_fingers == 1 else "scroll_down" if raised_fingers == 2 else None

def scroll_up():
    pyautogui.scroll(100)

def scroll_down():
    pyautogui.scroll(-100)

def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        gesture = recognize_gesture(frame)
        if gesture == "scroll_up":
            scroll_up()
        elif gesture == "scroll_down":
            scroll_down()
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )
        cv2.imshow("Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
