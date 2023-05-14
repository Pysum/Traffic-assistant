# Traffic-assistant

This is a simple chatbot that provides the traffic status of a requested location. The chatbot is built using Python 3 and uses the Natural Language Toolkit (NLTK) to process user input.

# Requirements
Python 3
NLTK library
requests library
An API key for the traffic data API
Usage
Clone the repository
Install the required libraries
Add your API key in the params dictionary
Run the code using python traffic_chatbot.py
Enter a user input when prompted (e.g., "What is the traffic status of New York?")
The chatbot will process the user input and provide a response based on the keywords in the input
# Functionality
The chatbot can handle the following types of user inputs:

Who are you?
What can you do?
How do you work?
Why do you exist?
Where are you located?
When were you created?
Traffic status of a requested location

If the user input contains the keyword "traffic," the chatbot will extract the location from the input and call the traffic data API to retrieve the traffic status for the location. If the API call is successful, the chatbot will provide the traffic status for the location. If the API call fails, the chatbot will inform the user that it was unable to retrieve the traffic data for the requested location.

# Note
The code for calling the traffic data API has been commented out in the get_traffic_data() function. You will need to add the code to call the API and retrieve the traffic data for the location.







