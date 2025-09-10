import time
import sys

def type_text(text, delay=0.05):
    """
    Mencetak teks satu huruf pada satu waktu untuk efek ketikan.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() 
        time.sleep(delay)
    sys.stdout.write('\n') 

def display_lyrics_with_typing_effect():
    """
    Menampilkan lirik lagu 'Happy' oleh Skinnyfabs dengan efek ketikan per baris,
    termasuk penyesuaian timing untuk bagian-bagian tertentu.
    """
    lyrics = [
        "Living all alone kinda forgot it's been that long",
        "Since someone's gone, I've been trying to be a little bit strong:>",
        "And it is not that easy to be exactly who I was",
        "My shit is done, now it's time for me try to moving on",
        "~~~~~~", 

        "'Cuz if you think I'm such a happy person, no you are wrong!", 
        "By saying my laughter is louder than yours",
        "Shut your freakin' mouth!!",
        "No one knows what I feel and what i suffer, no they don't know",
        "So keep your thoughts and stop assuming that",
        "Someone is always fine...",
        "~~~~~~",

        "I keep thinking why my friends left me, I can go insane", 
        "Mom was right about that and now I can't trust again",
        "But I think I don't really need no friends",
        "I'm alone and it's not that bad",
        "Then again it hurts me so bad and people just don't know that",
        "Maybe this time, I'ma take back what is mine",
        "All the smiles all the joys those are mine",
        "There will be no more cry, and",
        "There will be no more try, and",
        "These places I never belong",
        "'Cus this guy now is gone",
        "~~~~~~", 

        "If you think I'm such a happy person, no you are wrong!", 
        "By saying my laughter is louder than yours",
        "Shut your freakin' mouth!!",
        "No one knows what I feel and what i suffer, no they don't know",
        "So keep your thoughts and stop assuming that",
        "Someone is always fine...",
        ".....", 

        "If you think I'm such a happy person, no you are wrong", 
        "By saying my laughter is louder than yours",
        "Shut your freakin' mouth",
        "No one knows what I feel and what i suffer, no they don't know",
        "So keep your thoughts and stop assuming that",
        "Someone is always fine..."
    ]

    print("-------------------------------")
    print("Now playing: Happy - Skinnyfabs")
    print("-------------------------------")
    time.sleep(3)

    
    in_special_section = False

    for line in lyrics:
       
        if line == "'Cuz if you think I'm such a happy person, no you are wrong" or \
           line == "If you think I'm such a happy person, no you are wrong":
            in_special_section = True
            time.sleep(3) 
            print("\n") 
            type_text(line, delay=0.08) 
            time.sleep(2) 
            continue 

       
        if in_special_section:
            if line.startswith("~"):
                print("\n")
                type_text(line, delay=3.0) 
                time.sleep(2)
            else:
                type_text(line, delay=0.08) 
                time.sleep() 
        else:
            if line == "": 
                time.sleep(1.5) 
                print("")
            elif line.startswith("~"): 
                print("\n")
                type_text(line, delay=0.05)
                time.sleep(1.5)
            else:
                type_text(line)
                time.sleep(1.5)

    print("---------------")
    print("--End of song--")
    print("Thank u :):):)")
    print("---------------")

if __name__ == "__main__":
    display_lyrics_with_typing_effect()