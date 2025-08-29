# Cloak
🪄 Invisibility Cloak using OpenCV
This project creates a Harry Potter-style invisibility cloak using Python and OpenCV. A green cloth is detected in the webcam feed and replaced with the background, making it look invisible.

🚀 How it Works
Capture background without cloak

Convert each frame to HSV color space

Detect cloak color (green) using HSV ranges

Replace cloak pixels with background

Display final output in real-time

▶️ Run the Project
Install dependencies:
bashpip install opencv-python numpy
Run:
bashpython cloak.py
Controls:

ESC → Exit
b → Recapture background

✨ Key Code Steps
pythoncap = cv2.VideoCapture(0)  # Open webcam
bg = cv2.flip(cap.read()[1], 1)  # Capture background
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert to HSV
mask = cv2.inRange(hsv, lower_green, upper_green)  # Detect green cloak
cloak = cv2.bitwise_and(bg, bg, mask=mask)
rest = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
final = cv2.addWeighted(cloak, 1, rest, 1, 0)  # Merge
🎨 Color Detection
The green cloak is detected using HSV color ranges:

Lower Green: [40, 50, 50] - captures yellowish-green
Upper Green: [80, 255, 255] - extends to bluish-green

📸 Example

Without cloak → background captured
With green cloak → cloak disappears, background shows through

💡 Tips

Use a bright green fabric for best detection
Ensure good lighting conditions
Avoid green clothing or background objects
Press b to recapture background if lighting changes
