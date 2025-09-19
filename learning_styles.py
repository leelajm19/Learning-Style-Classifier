import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

user_input = input("Tell me how you prefer to learn:")
tokens = word_tokenize(user_input.lower())

visual = ["video", "diagram", "see", "image", "picture", "seeing"]
auditory = ["listen", "hear", "lecture", "audio", "listening", "hearing"]
kinesthetic = ["do", "build", "practice", "move", "hands-on", "doing", "building", "moving"]

if any(word in tokens for word in visual):
    print("You are most likely a visual learner.")
elif any(word in tokens for word in auditory):
    print("You might be an auditory learner.")
elif any(word in tokens for word in kinesthetic):
    print("You are probably a kinesthetic learner.")
else:
    print("You may have a mix of learning styles.")