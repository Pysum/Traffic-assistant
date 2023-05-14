import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests
import json


# Define the API endpoint and parameters
endpoint = "https://api.example.com/traffic"
location = "New York City"

# Define the API headers and query parameters
headers = {'Content-Type': 'application/json'}
params = {
    'location': location,
    'api_key': 'your_api_key'
}

# Call the API and get the response
response = requests.get(endpoint, headers=headers, params=params)

# Parse the response JSON data
data = json.loads(response.text)

# Get the traffic status from the parsed data
if 'traffic_status' in data:
    traffic_status = data['traffic_status']
    print(f"The traffic status in {location} is {traffic_status}.")
else:
    print("Unable to retrieve traffic data.")

# Defining the input text
input_text = "Hi, I am ChatGPT. I am a large language model trained by OpenAI. I can answer questions and provide information on various topics."

# Tokenizing the input text and removing stopwords
tokens = word_tokenize(input_text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if not token.lower() in stop_words]

# Defining the responses to user inputs
responses = {
    "who": "I am traffic assistant",
    "what": "I can help you with traffic status of your required place",
    "how": "I am able to provide relevant responses based on the keywords in your questions.",
    "why": "Because I have been programmed to do so!",
    "where": "I am not located anywhere in particular, I exist only in the digital world.",
    "when": "I was created by me in 2023.",
    "traffic": "The traffic status of your requested location is {status}.",
    "default": "I'm sorry, I don't understand. Could you please rephrase your question?"
}

# Defining the chatbot function
def chatbot(input_sentence):
    # Tokenizing the input sentence and removing stopwords
    input_tokens = word_tokenize(input_sentence)
    input_filtered_tokens = [token for token in input_tokens if not token.lower() in stop_words]

 # Checking for relevant keywords and providing responses
    for token in input_filtered_tokens:
        if token.lower() == "traffic":
            location = input_sentence.replace("traffic", "").strip() # Extracting the location from user input
            traffic_data = get_traffic_data(location) # Get traffic data for the location
            if traffic_data:
                return responses["traffic"].format(status=traffic_data)
            else:
                return "I'm sorry, I could not retrieve the traffic data for your requested location."
        elif token.lower() in responses:
            return responses[token.lower()]
  # If no relevant keywords are found, return the default response
    return responses["default"]

# Function to get traffic data for a location using a traffic data API
def get_traffic_data(location):
    # Add code here to call the traffic data API and retrieve the traffic status for the location
    # You may need to sign up for an API key and use the requests library to make API calls
    # Here's an example of what the code might look like:
    # url = "https://api.trafficdata.com/traffic?location={}".format(location)
    # response = requests.get(url, headers={"Authorization": "Bearer API_KEY"})
    # if response.status_code == 200:
    #     return response.json()["status"]
    # else:
      #     return None
    pass

# Mock user input
user_input = "What is the traffic status of New York?"

# Get response from chatbot
chatbot_response = chatbot(user_input)

# Print response
print(chatbot_response)

