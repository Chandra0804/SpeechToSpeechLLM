import tkinter as tk
from utils.speech_to_text import capture_speech
from utils.generate_response import generate_response
from utils.text_to_speech import speak_respone

def run_bot():
    user_text = capture_speech()
    if user_text:
        bot_reply = generate_response(user_text)
        speak_respone(bot_reply)
        display_var.set(f"Bot: {bot_reply}")

root = tk.Tk()
root.title("Voice Interactive Assistant")

display_var = tk.StringVar()
display_var.set("Press 'Speak' to start interaction.")

tk.Label(root, textvariable=display_var, wraplength=300).pack(pady=10)
tk.Button(root, text="Speak", command=run_bot).pack(pady=10)

root.mainloop()
