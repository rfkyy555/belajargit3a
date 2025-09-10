import time
import sys
import os

# Kode ANSI untuk warna teks
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """Membersihkan layar konsol."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.05, color=Colors.RESET, bold=False):
    """
    Mencetak teks satu huruf pada satu waktu dengan warna dan efek bold.
    """
    if bold:
        sys.stdout.write(Colors.BOLD)
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.RESET + '\n') # Reset warna dan bold setelah baris selesai

def display_lyrics_with_typing_effect():
    """
    Menampilkan lirik lagu 'Happy' oleh Skinnyfabs dengan efek ketikan per baris,
    penyesuaian timing, warna, dan efek pembersihan layar.
    """
    lyrics = [
        {"text": "Living all alone kinda forgot it's been that long", "color": Colors.CYAN, "delay": 0.05, "pause_after": 1.5},
        {"text": "Since someone's gone, I've been trying to be a little bit strong:>", "color": Colors.CYAN, "delay": 0.05, "pause_after": 1.5},
        {"text": "And it is not that easy to be exactly who I was", "color": Colors.CYAN, "delay": 0.05, "pause_after": 1.5},
        {"text": "My shit is done, now it's time for me try to moving on", "color": Colors.CYAN, "delay": 0.05, "pause_after": 2.0},
        {"text": "~~~~~~", "color": Colors.YELLOW, "delay": 0.1, "pause_after": 1.0, "is_separator": True},

        {"text": "'Cuz if you think I'm such a happy person, no you are wrong!", "color": Colors.RED, "delay": 0.08, "pause_before": 3.0, "pause_after": 2.0, "bold": True, "is_chorus_start": True}, # Chorus 1
        {"text": "By saying my laughter is louder than yours", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "Shut your freakin' mouth!!", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "No one knows what I feel and what i suffer, no they don't know", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "So keep your thoughts and stop assuming that", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "Someone is always fine...", "color": Colors.RED, "delay": 0.08, "pause_after": 2.5},
        {"text": "~~~~~~", "color": Colors.YELLOW, "delay": 0.1, "pause_after": 1.0, "is_separator": True},

        {"text": "I keep thinking why my friends left me, I can go insane", "color": Colors.BLUE, "delay": 0.05, "pause_after": 1.5}, # Verse 2
        {"text": "Mom was right about that and now I can't trust again", "color": Colors.BLUE, "delay": 0.05, "pause_after": 1.5},
        {"text": "But I think I don't really need no friends", "color": Colors.BLUE, "delay": 0.05, "pause_after": 1.5},
        {"text": "I'm alone and it's not that bad", "color": Colors.BLUE, "delay": 0.05, "pause_after": 1.5},
        {"text": "Then again it hurts me so bad and people just don't know that", "color": Colors.BLUE, "delay": 0.05, "pause_after": 2.0},
        {"text": "Maybe this time, I'ma take back what is mine", "color": Colors.BLUE, "delay": 0.05, "pause_after": 1.5},
        {"text": "All the smiles all the joys those are mine", "color": Colors.BLUE, "delay": 0.05, "pause_after": 1.5},
        {"text": "There will be no more cry, and", "color": Colors.BLUE, "delay": 0.05, "pause_after": 1.0},
        {"text": "There will be no more try, and", "color": Colors.BLUE, "delay": 0.05, "pause_after": 1.0},
        {"text": "These places I never belong", "color": Colors.BLUE, "delay": 0.05, "pause_after": 1.0},
        {"text": "'Cus this guy now is gone", "color": Colors.BLUE, "delay": 0.05, "pause_after": 2.0},
        {"text": "~~~~~~", "color": Colors.YELLOW, "delay": 0.1, "pause_after": 1.0, "is_separator": True},

        {"text": "If you think I'm such a happy person, no you are wrong!", "color": Colors.RED, "delay": 0.08, "pause_before": 3.0, "pause_after": 2.0, "bold": True, "is_chorus_start": True}, # Chorus 2
        {"text": "By saying my laughter is louder than yours", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "Shut your freakin' mouth!!", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "No one knows what I feel and what i suffer, no they don't know", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "So keep your thoughts and stop assuming that", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "Someone is always fine...", "color": Colors.RED, "delay": 0.08, "pause_after": 2.5},
        {"text": ".....", "color": Colors.YELLOW, "delay": 0.1, "pause_after": 1.0, "is_separator": True},

        {"text": "If you think I'm such a happy person, no you are wrong", "color": Colors.RED, "delay": 0.08, "pause_before": 3.0, "pause_after": 2.0, "bold": True, "is_chorus_start": True}, # Chorus 3
        {"text": "By saying my laughter is louder than yours", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "Shut your freakin' mouth", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "No one knows what I feel and what i suffer, no they don't know", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "So keep your thoughts and stop assuming that", "color": Colors.RED, "delay": 0.08, "pause_after": 1.5},
        {"text": "Someone is always fine.", "color": Colors.RED, "delay": 0.08, "pause_after": 2.5}
    ]

    print("-------------------------------")
    print("Now playing: Happy - Skinnyfabs")
    print("-------------------------------")
    time.sleep(3)
    clear_screen() # Membersihkan layar setelah header awal

    for line_data in lyrics:
        text = line_data["text"]
        color = line_data.get("color", Colors.RESET)
        delay = line_data.get("delay", 0.05)
        pause_before = line_data.get("pause_before", 0)
        pause_after = line_data.get("pause_after", 1.5)
        bold = line_data.get("bold", False)
        is_chorus_start = line_data.get("is_chorus_start", False) # Flag baru
        is_separator = line_data.get("is_separator", False)

        # Jeda sebelum baris mulai diketik
        time.sleep(pause_before)

        # Efek pulsasi hanya untuk baris awal chorus
        if is_chorus_start:
            for _ in range(2): # Jumlah kedipan
                clear_screen()
                type_text(text, delay=delay, color=color, bold=bold)
                time.sleep(0.3) # Teks terlihat
                clear_screen()
                time.sleep(0.2) # Teks tidak terlihat
            # Setelah kedipan, cetak teks terakhir kali dan biarkan di layar
            type_text(text, delay=delay, color=color, bold=bold)
        else:
            # Untuk lirik biasa atau separator, bersihkan layar dan ketik
            clear_screen()
            type_text(text, delay=delay, color=color, bold=bold)

        # Jeda setelah baris selesai diketik
        time.sleep(pause_after)

    clear_screen() # Membersihkan layar di akhir
    print("-----------------")
    print("-- End of song --")
    print("Thank u :) :) :)")
    print("-----------------")

if __name__ == "__main__":
    display_lyrics_with_typing_effect()