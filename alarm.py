import time
import winsound
import os
import datetime

print("=== Professional Alarm Clock ===\n")

# Alarm time input
alarm_time = input("Set alarm time (HH:MM:SS): ").strip()
print(f"✅ Alarm successfully set for {alarm_time}")

# Sound file
sound_file = "mixkit-facility-alarm-sound-999.wav"

# Check sound file
if not os.path.exists(sound_file):
    print(f"⚠️  Warning: {sound_file} not found! Put the sound file in same folder.")
else:
    print("✅ Alarm sound ready!")

print("\nWaiting for alarm... (Press Ctrl+C to stop)\n")

while True:
    current_time = time.strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    
    # Clean display
    print(f"Current Time: {current_time}  |  Date: {current_date}     ", end="\r")
    
    if current_time == alarm_time:
        print("\n\n" + "="*50)
        print("🚨 WAKE UP! WAKE UP! ALARM IS RINGING 🚨")
        print("="*50 + "\n")
        
        try:
            # Play sound continuously until stopped
            print("🔊 Playing alarm sound...")
            winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            
            # Keep ringing for 30 seconds or until manual stop
            for i in range(30):
                print(f"Alarm ringing... ({i+1}/30 seconds)")
                time.sleep(1)
            
            # Stop sound
            winsound.PlaySound(None, winsound.SND_PURGE)
            print("Alarm stopped automatically.")
            
        except Exception as e:
            print("Sound error:", e)
        
        break
    
    time.sleep(1)