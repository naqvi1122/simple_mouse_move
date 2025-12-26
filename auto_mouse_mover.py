import pyautogui
import time
import sys
import random
from datetime import datetime

def move_mouse():
    print("Auto Mouse Mover started.")
    print("Press Ctrl+C to stop.")
    
    try:
        # Get screen size
        screen_width, screen_height = pyautogui.size()
        
        while True:
            # Generate random position within screen bounds
            # We keep a margin of 100 pixels to avoid corners (FailSafe)
            target_x = random.randint(100, screen_width - 100)
            target_y = random.randint(100, screen_height - 100)
            
            # Move mouse to the random position
            # duration=1 makes the movement smooth and visible
            pyautogui.moveTo(target_x, target_y, duration=1.0)
            
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"[{current_time}] Moved mouse to ({target_x}, {target_y})")
            
            # Wait for 5 seconds before next move (faster than before since it's "freely" moving)
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
        sys.exit(0)
    except pyautogui.FailSafeException:
        print("\nFailSafe triggered from mouse corner. Stopping.")
        sys.exit(0)

if __name__ == "__main__":
    move_mouse()
