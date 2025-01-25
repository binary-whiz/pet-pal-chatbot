import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from difflib import get_close_matches

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def load_dataset(file_name):
    """Load the dataset from a text file."""
    with open(file_name, "r") as file:
        data = file.read()
    return data

def preprocess_text(text):
    """Preprocess the text: tokenize, remove stopwords, and lemmatize."""
    lemmatizer = WordNetLemmatizer()  # Create an instance of the lemmatizer
    # Tokenize the input text and convert it to lowercase
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))  # Get list of stopwords
    # Lemmatize the words and filter out stopwords and non-alphabetic tokens
    filtered_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word.isalpha()]
    return filtered_tokens

def get_answer(question, dataset):
    """Find the best answer for the user's question using tokenization."""
    # Preprocess the user question
    question_tokens = preprocess_text(question)

    # Extract all questions from the dataset and preprocess them
    dataset_blocks = [block.split("A:")[0][3:].strip() for block in dataset.split("\n\n") if block.startswith("Q:")]
    dataset_questions_tokens = [preprocess_text(q) for q in dataset_blocks]

    # Use fuzzy matching to find the closest question
    best_match = None
    max_similarity = 0
    for idx, dataset_tokens in enumerate(dataset_questions_tokens):
        similarity = len(set(question_tokens).intersection(set(dataset_tokens))) / float(len(set(question_tokens).union(set(dataset_tokens))))
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = idx

    if best_match is not None:
        # Get the answer for the best matching question
        answer = dataset.split("\n\n")[best_match].split("A:")[1].strip()
        return answer
    else:
        return "Sorry, I don't know the answer to that."

if __name__ == "__main__":
    # Load the dataset from the file
    dataset = load_dataset("dataset.txt")
    print("PetPal is ready! Type your questions or 'exit' to quit.")

    while True:
        # Take user input for the chatbot
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        # Get the chatbot response for the input
        response = get_answer(user_input, dataset)
        print(f"PetPal: {response}")
