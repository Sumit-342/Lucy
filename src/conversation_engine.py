import re
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

MODES = {
    "crisis": {
        "phrases": [
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
        ],
        "keywords": [
            "dont want to live",
            "live anymore",
            "worth living",
            "point of all this",
            "jeene ka koi matlab",
            "jeena nahi",
            "could disappear",
            "feels hopeless",
            "done with everything",
            "no one would care",
            "sab khatam",
            "nahi seh sakta",
            "jeene ka mann"
        ]
    },
    "comfort": {
        "phrases": [
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
        ],
        "keywords": [
            "mood off",
            "bekaar",
            "acha nahi",
            "dil bhaari",
            "hurt",
            "lonely",
            "alone",
            "no friends",
            "no one understands",
            "baat karne wala",
            "good enough",
            "loser",
            "nahi hoga",
            "failed",
            "haar",
            "bharosa nahi",
            "disappoint",
            "mess things up",
            "successful nahi",
            "stress",
            "pressure",
            "overwhelmed",
            "too much",
            "thak gaya",
            "energy",
            "kaam nahi kar raha",
            "tabiyat",
            "bukhar",
            "jukham",
            "headache",
            "feel well"
        ]
    },
    "celebrate": {
        "phrases": [
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
        ],
        "keywords": [
            "selected",
            "passed",
            "pass",
            "cracked",
            "internship",
            "job",
            "promotion",
            "rank",
            "scholarship",
            "won",
            "competition",
            "code",
            "worked",
            "bug",
            "fix",
            "deploy",
            "deployed",
            "merge",
            "contribution",
            "streak",
            "github",
            "laptop",
            "phone",
            "guitar",
            "cooler",
            "dream",
            "new room",
            "ghar",
            "papa",
            "mom",
            "family time",
            "family ke saath",
            "surprise",
            "mile",
            "yay",
            "woohoo",
            "hurray",
            "excited",
            "best day",
            "cant believe",
            "finally done",
            "thank god",
            "chain",
            "done!",
            "tension khatam",
            "at last"
        ]
    },
    "vent": {
        "phrases": [
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
        ],
        "keywords": [
            "angry",
            "gussa",
            "furious",
            "pissed off",
            "hate",
            "frustrating",
            "bakwaas",
            "irritating",
            "had ho gayi",
            "ulta",
            "ignore",
            "nobody listens",
            "irritate",
            "cant stand",
            "baat nahi karni",
            "assignment",
            "boss",
            "college",
            "deadline",
            "kaam de diya",
            "traffic",
            "internet chala gaya",
            "laptop hang",
            "phone toot ",
            "light chali",
            "pak gaya",
            "tang aa gaya",
            "ab aur nahi",
            "dimag kharab",
            "dimag ka dahi"
        ]
    },
    "explain": {
        "phrases": [
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
        ],
        "keywords": [
            "what is",
            "why",
            "how",
            "explain",
            "samjhao",
            "batao",
            "kaise kaam karta",
            "kaise hota",
            "definition",
            "meaning",
            "use",
            "example",
            "notes",
            "short",
            "easy language",
            "difference",
            "vs"
        ]
    },
    "motivate": {
        "phrases": [
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
        ],
        "keywords": [
            "start",
            "begin",
            "shuru",
            "lets do this",
            "time to work",
            "consistent",
            "discipline",
            "procrastinating",
            "focus nahi",
            "give up",
            "exam aa rahe",
            "study",
            "padhna",
            "gym",
            "workout",
            "weight",
            "running",
            "dsa",
            "lucy",
            "project complete",
            "coding shuru",
            "building something",
            "motivate",
            "push",
            "encourage",
            "cheer me up",
            "ready",
            "i can do this"
        ]
    },
    "love": {
        "phrases": [
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
        ],
        "keywords": [
            "parents",
            "family",
            "sister",
            "friend",
            "miss",
            "crush",
            "like someone",
            "relationship",
            "someone special",
            "thank",
            "grateful",
            "appreciate",
            "helped me",
            "dil ki baat"
        ]
    },
    "casual": {
        "phrases": [
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
        ],
        "keywords": [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good night",
            "whats up",
            "kaise ho",
            "aur batao",
            "kya chal raha",
            "nice to see you",
            "long time",
            "haha",
            "lol",
            "joke",
            "interesting",
            "bored"
        ]
    }
}



def normalize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return " ".join(text.split())

def rule_detect_mode(text):
    text_norm = normalize(text)

    for mode, data in MODES.items():
        for phrase in data["phrases"]:
            phrase_norm = normalize(phrase)
            if phrase_norm in text_norm:
                print(f"Matched: {phrase} -> {mode}")
                return mode

    scores = {}
    for mode, data in MODES.items():
        score = 0
        for keyword in data["keywords"]:
            if keyword in text_norm:
                score += 1
        scores[mode] = score

    print(scores)

    winner = max(scores , key=scores.get)

    if scores[winner] == 0 :
        return "casual"

    return winner


VALID_MODES = {
    "crisis",
    "comfort",
    "celebrate",
    "vent",
    "love",
    "motivate",
    "explain",
    "casual",
}

# --------------------------------------------------
# Conversation Mode Classification Prompt
# --------------------------------------------------

# SYSTEM_PROMPT = """
# You are a conversation mode classifier.

# Return ONLY one of these words:

# crisis
# comfort
# celebrate
# vent
# love
# motivate
# explain
# casual

# Do not explain.
# Do not write sentences.
# Return exactly one word.
# """

# #----------------------------------------------------------
# #----------------------------------------------------------

# def qwen_detect_mode(text):
#     response = client.chat.completions.create(
#         model="qwen/qwen3-next-80b-a3b-instruct",
#         messages=[
#             {"role": "system", "content": SYSTEM_PROMPT},
#             {"role": "user", "content": text}
#         ],
#         temperature=0
#     )

#     mode = response.choices[0].message.content.strip().lower()

#     if mode not in VALID_MODES:
#         raise ValueError(f"Invalid mode returned: {mode}")

#     return mode


# def detect_mode(text) :
#     try :
#         return qwen_detect_mode(text)
#     except Exception as e :
#         print(f"Qwen Failed : {e}")
#         print("Using Rule Engine...")

#         return rule_detect_mode(text)

