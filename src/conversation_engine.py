import re

CRISIS_PHRASES = [
    "i don't want to live anymore",
    "don't wanna live anymore",
    "i don't think this life is worth living",
    "what's even the point of all this",
    "jeene ka koi matlab nahi",
    "jeena nahi chahta",
    "bas sab khatam ho jaye",
    "I wish I could disappear.",
    "Everything feels hopeless.",
    "I can't do this anymore.",
    "No one would care if I was gone.",
    "I'm done with everything.",
    "Jeene ka koi matlab nahi lagta.",
    "Sab kuch khatam sa lag raha hai.",
    "Ab aur nahi seh sakta.",
    "Bas sab khatam ho jaye.",
    "Mujhe lagta hai sab bekaar hai.",
    "Mere jeene ka mann nhi karta",
    "sab khatam ho gaya"
]

COMFORT_PHRASES = [
    "Aaj mood bahut off hai.",
    "Aaj pura din bekaar gaya.",
    "Yaar bahut thak gaya hu.",
    "Aaj kuch acha nahi lag raha.",
    "Mera breakup ho gaya.",
    "Aaj exam kharab gaya.",
    "Mujhse nahi hoga.",
    "I feel lonely.",
    "Bahut stress hai.",
    "Meri tabiyat kharab hai.",
    "I don't have any friends.",
    "I just feel like a loser.",
    "Why does it always happen to me?",
    "Why can't I be good enough?",
    "I wish I could fix everything.",
    "I feel so alone.",
    "No one understands me.",
    "Mere paas baat karne wala koi nahi hai.",
    "I failed again.",
    "Main phir haar gaya.",
    "Kuch bhi sahi nahi ho raha.",
    "Lagta hai main kabhi successful nahi hounga.",
    "Bahut pressure hai.",
    "Everything feels too much.",
    "I feel overwhelmed.",
    "Dimaag bilkul kaam nahi kar raha.",
    "Main bahut thak gaya hu.",
    "I don't have energy anymore.",
    "Dil bahut bhaari hai.",
    "Uski bahut yaad aa rahi hai.",
    "It really hurt.",
    "Meri tabiyat theek nahi hai.",
    "Mujhe bukhar hai.",
    "Jukham ho gaya hai.",
    "Headache ho raha hai.",
    "I don't feel well today.",
    "I don't think I'm good enough.",
    "I keep disappointing everyone.",
    "I always mess things up.",
    "Mujhe apne upar bharosa nahi hai."
]


CELEBRATE_PHRASES = [
    "I got selected.",
    "I passed the exam.",
    "I cracked the interview.",
    "Finally got the internship.",
    "I got the job.",
    "Promotion mil gaya.",
    "Rank aa gayi.",
    "Scholarship mil gayi.",
    "I won the competition.",
    "I did it!",
    "My code finally worked.",
    "Bug fix ho gaya.",
    "Project finally run ho gaya.",
    "Finally deployed my website.",
    "PR merge ho gaya.",
    "First contribution accepted.",
    "100-day streak complete.",
    "Finally GitHub green ho gaya. 😆",
    "Finally bought a new laptop.",
    "New phone le liya.",
    "Guitar aa gaya.",
    "Cooler aa gaya.",
    "Dream complete ho gaya.",
    "Finally ghar aa gaya.",
    "New room mil gaya.",
    "Papa maan gaye.",
    "Mom liked my project.",
    "Mere dost ne surprise diya.",
    "Bahut din baad sab mile.",
    "Aaj family ke saath bahut maza aaya.",
    "Hurrayyyyy!!",
    "Yayyyyy!!",
    "Woohoo!!",
    "Let's gooooo!!",
    "Finallyyyyy!!",
    "OMG I can't believe it!",
    "I'm so excited!",
    "This is the best day ever!",
    "I'm literally shaking with excitement!",
    "Finally everything is over.",
    "At last ho gaya.",
    "Thank God!",
    "Finally tension khatam.",
    "Ab chain ki saans aayi.",
    "It worked!",
    "Finally done!"
]


VENT_PHRASES = [
    "I'm so angry.",
    "Mujhe bahut gussa aa raha hai.",
    "Gussa control nahi ho raha.",
    "I hate this.",
    "I hate everyone.",
    "I'm furious.",
    "I'm pissed off.",
    "This is so frustrating.",
    "Sab bakwaas hai.",
    "Dimag kharab ho gaya hai.",
    "Sab kuch ulta ho raha hai.",
    "Kya bakwaas chal rahi hai.",
    "Had ho gayi yaar.",
    "Kitna irritating hai.",
    "Usne mera mood kharab kar diya.",
    "Sab bewakoof hain.",
    "Nobody listens to me.",
    "Mujhe ignore kar diya.",
    "Mujhe bahut irritate kar diya.",
    "I can't stand this person.",
    "Mujhe usse baat bhi nahi karni.",
    "Assignment ne jaan le li.",
    "Boss ne dimaag kharab kar diya.",
    "College wale pagal hain.",
    "Kitna kaam de diya.",
    "Deadline maar degi.",
    "Traffic ne pagal kar diya.",
    "Internet phir chala gaya.",
    "Laptop hang ho gaya.",
    "Phone toot gaya.",
    "Light chali gayi.",
    "Bhai had ho gayi.",
    "Bas yaar ab aur nahi.",
    "Kya bakwaas hai.",
    "Dimag ka dahi ho gaya.",
    "Pak gaya hu.",
    "Tang aa gaya hu.",
    "Sar dard ho gaya inse."
]


EXPLAIN_PHRASES = [
    "What is AI?",
    "Explain machine learning.",
    "What is Java?",
    "What is Python?",
    "What is recursion?",
    "Blockchain kya hota hai?",
    "Internet kaise kaam karta hai?",
    "GPU kya hota hai?",
    "How does this work?",
    "Kaise kaam karta hai?",
    "Ye kaise hota hai?",
    "Mujhe samjhao.",
    "Can you explain this?",
    "Explain in simple words.",
    "Easy language mein batao.",
    "Difference between Java and Python.",
    "Array vs Vector.",
    "Stack vs Queue.",
    "CPU vs GPU.",
    "React vs Angular.",
    "Iska meaning kya hai?",
    "Iska use kya hai?",
    "Example do.",
    "Definition batao.",
    "Notes bana do.",
    "Short mein samjhao.",
    "Why is the sky blue?",
    "Why do we sleep?",
    "Fever kyu hota hai?",
    "Rain kaise hoti hai?",
    "Earth round kyu hai?"
]

MOTIVATE_PHRASES = [
    "Kal se start karunga.",
    "Mujhe start karna hai.",
    "Kaise shuru karu?",
    "I want to begin.",
    "Let's do this.",
    "Time to work.",
    "Aaj se serious.",
    "Consistent kaise rahu?",
    "Discipline nahi ban raha.",
    "Roz break ho jata hai.",
    "I keep procrastinating.",
    "Focus nahi ho raha.",
    "Main give up kar deta hu.",
    "Motivation chahiye.",
    "Exam aa rahe hain.",
    "Padhna hai.",
    "Mujhe push karo.",
    "Aaj bahut padhna hai.",
    "Chalo padhte hain.",
    "I need to study.",
    "Gym start karna hai.",
    "Workout ka mann nahi.",
    "Weight lose karna hai.",
    "Running shuru karni hai.",
    "DSA restart karni hai.",
    "Lucy pe kaam karna hai.",
    "Project complete karna hai.",
    "Coding shuru karte hain.",
    "Build something today.",
    "Push me.",
    "Encourage me.",
    "Motivate me.",
    "Cheer me up.",
    "Let's go!",
    "Ready hoon.",
    "I can do this."
]


LOVE_PHRASES = [
    "I love my parents.",
    "I miss my friend.",
    "I have a crush.",
    "I think I like someone.",
    "Thank you.",
    "I'm grateful.",
    "You helped me a lot.",
    "Family ke saath time spend kiya.",
    "I really appreciate you.",
    "I miss my sister.",
    "Dil ki baat karni hai.",
    "Relationship advice chahiye.",
    "Someone special entered my life."
]


CASUAL_CHAT_PHRASES = [
    "Hi",
    "Hello",
    "Hey",
    "Good morning",
    "Good night",
    "What's up?",
    "Kaise ho?",
    "Aur batao.",
    "Kya chal raha hai?",
    "Nice to see you.",
    "Long time no see.",
    "Haha 😂",
    "LOL",
    "Bored ho raha hu.",
    "Tell me something interesting.",
    "Ek joke sunao."
]


MODES = [
    ("crisis", CRISIS_PHRASES),
    ("vent", VENT_PHRASES),
    ("comfort", COMFORT_PHRASES),
    ("celebrate", CELEBRATE_PHRASES),
    ("love", LOVE_PHRASES),
    ("motivate", MOTIVATE_PHRASES),
    ("explain", EXPLAIN_PHRASES),
]





def normalize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return " ".join(text.split())

def detect_mode(text):
    text_norm = normalize(text)

    for mode, phrases in MODES:
        for phrase in phrases:
            phrase_norm = normalize(phrase)
            if phrase_norm in text_norm:
                print(f"Matched: {phrase} -> {mode}")
                return mode

    return "casual"
