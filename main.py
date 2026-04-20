from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import io
import time
import os

def clear_screen():
    # Clears the terminal screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

def final_translator():
    pygame.mixer.init()
    clear_screen()
    
    # --- Professional Header ---
    print("========================================")
    print("    WELCOME TO BHAASHA-CONNECT v1.0     ")
    print("       Created by: Meenakshi            ")
    print("========================================")
    print("💡 Instructions:")
    print("   1. Type your English sentence.")
    print("   2. Wait for the Kannada translation.")
    print("   3. Type 'end' to close the app.")
    print("========================================")

    while True:
        english_text = input("\n📝 Enter English text: ").strip()

        # Exit Logic
        if english_text.lower() in ['end', 'exit', 'bye']:
            print("\n✨ ಧನ್ಯವಾದಗಳು! (Thank you!)")
            print("🚀 Ending conversation... Have a great day!")
            time.sleep(1.5)
            break

        if not english_text:
            continue

        try:
            print("🔍 Translating...")
            kannada_text = GoogleTranslator(source='en', target='kn').translate(english_text)
            
            print(f"✅ Kannada: {kannada_text}")
            print("🔊 Playing Audio...")

            # Voice Output Logic
            tts = gTTS(text=kannada_text, lang='kn')
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            
            pygame.mixer.music.load(fp)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(0.05)

        except Exception:
            print("📡 Error: Check your internet connection.")

    pygame.mixer.quit()

if __name__ == "__main__":
    final_translator()