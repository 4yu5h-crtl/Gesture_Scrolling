import cv2
import mediapipe as mp
import numpy as np
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5)

# OpenCV window setup
cv2.namedWindow("Gesture Control", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gesture Control", 640, 480)

def recognize_gesture(frame):
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if not results.multi_hand_landmarks:
        return None
    
    hand_landmarks = results.multi_hand_landmarks[0]
    
    # Get index finger tip and middle point coordinates
    index_tip = np.array([hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y])
    index_pip = np.array([hand_landmarks.landmark[6].x, hand_landmarks.landmark[6].y])
    
    # Calculate direction vector
    direction = index_tip[1] - index_pip[1]  # Compare y-coordinates
    
    # Recognize gestures based on finger direction
    threshold = 0.05
    if direction < -threshold:  # Finger pointing up
        return "up"
    elif direction > threshold:  # Finger pointing down
        return "down"
    else:
        return None

def scroll_up():
    print("Scrolling up")
    pyautogui.press("up")  # Simulates Arrow Up key press
    
def scroll_down():
    print("Scrolling down")
    pyautogui.press("down")  # Simulates Arrow Down key press
    
def main():
    cap = cv2.VideoCapture(0)
    
    # Add status variable to track if scrolling is active
    scrolling_active = True
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frame = cv2.flip(frame, 1)
        gesture = recognize_gesture(frame)
        
        # Handle different gestures
        if scrolling_active:
            if gesture == "up":
                scroll_up()
            elif gesture == "down":
                scroll_down()
        
        # Draw hand landmarks
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS)
        
        # Display status on frame
        status_text = "ACTIVE" if scrolling_active else "STOPPED"
        cv2.putText(frame, f"Status: {status_text}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if scrolling_active else (0, 0, 255), 2)
        
        cv2.imshow("Gesture Control", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()