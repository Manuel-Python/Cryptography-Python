# A simple caesar cipher implementation using Udemy code as skeleton

plato = "Let me begin by observing first of all, that nine thousand was the sum of years" \
        " which had elapsed since the war which was said to have taken place between those " \
        "who dwelt outside the Pillars of Heracles and all who dwelt within them; this war I am " \
        "going to describe. Of the combatants on the one side, the city of Athens was reported to " \
        "have been the leader and to have fought out the war; the combatants on the other side were " \
        "commanded by the kings of Atlantis, which, as was saying, was an island greater in extent " \
        "than Libya and Asia, and when afterwards sunk by an earthquake, became an impassable " \
        "barrier of mud to voyagers sailing from hence to any part of the ocean. The progress of the" \
        " history will unfold the various nations of barbarians and families of Hellenes which then " \
        "existed, as they successively appear on the scene; but I must describe first of all " \
        "Athenians of that day, and their enemies who fought with them, and then the respective " \
        "powers and governments of the two kingdoms. Let us give the precedence to Athens. "

plato = plato.upper()

def generate_key(displacement):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .,;"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + displacement) % len(letters)]
        cnt += 1
    return key

def get_decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def character_count(cipher):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .,;"
    char_count = {}
    for le in letters:
        n = cipher.count(le)
        #print("{} * {}".format(le,n))
        char_count[le] = n
    return char_count



key = generate_key(3)
cipher = encrypt(key,plato)

char_count = character_count(cipher)
print(char_count)
