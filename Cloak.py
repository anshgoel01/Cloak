import cv2
import numpy as np
import time

# Open the webcam (default index = 0)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Could not access the camera. Try using index 1 or 2.")
    exit()

# Give the camera a moment to adjust
time.sleep(2)

# --- Capture the background (without the cloak) ---
print("📸 Capturing background... please stay still")
for _ in range(60):
    ret, bg = cap.read()
    if ret:
        bg = cv2.flip(bg, 1)
print("✅ Background captured")

# --- Start reading frames in real-time ---
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # mirror view
    
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define green color range in HSV
    # Green typically ranges from 40-80 in hue
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    
    # Create mask for green areas
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Refine mask to remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)
    
    mask_inv = cv2.bitwise_not(mask)
    
    # Replace green cloak region with background
    cloak_area = cv2.bitwise_and(bg, bg, mask=mask)
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)
    
    # Show results
    cv2.imshow("🪄 Invisibility Cloak", final)
    cv2.imshow("🎭 Cloak Mask (debug)", mask)
    
    # Keyboard controls
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC to quit
        break
    elif key == ord('b'):  # recapture background
        print("♻ Re-capturing background...")
        for _ in range(60):
            ret, bg = cap.read()
            if ret:
                bg = cv2.flip(bg, 1)
        print("✅ Background updated")

cap.release()
cv2.destroyAllWindows()
