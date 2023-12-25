from ELSA.TextProcessor import TextProcessor

txtprocessor = TextProcessor()
phrases = []
short_term_memory = []

while True:
    try:
        user_prompt = input("> ")
        phrases.append(user_prompt)
        print(f"Collected Data : {phrases}")
    except KeyboardInterrupt:
        break

for phrase in phrases:
    similarity_of_phrase = txtprocessor.phrase_similarity_extractor(phrases[0],phrase)
    if similarity_of_phrase >= 6.9:
        short_term_memory.append(phrase)

print("Learned data on session is = ",short_term_memory)
    