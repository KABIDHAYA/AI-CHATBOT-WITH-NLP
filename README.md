# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KABILAN M

*INTERN ID*: CT04CH1571

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH



###  **Task Description: Simple Rule-Based Chatbot using Python (CodTechBot)**

####  **Objective:**

The task is to create a **rule-based chatbot** using Python's **Natural Language Toolkit (NLTK)**. The chatbot simulates simple human-like conversation using pre-defined patterns and responses.


###  **Technologies & Tools Used:**

* **Python**
* **NLTK Library** (`nltk.chat.util.Chat` and `reflections`)



###  **Functionality:**

1. **Pattern Matching:**

   * The bot uses regular expressions to match user input against a list of predefined patterns (called `pairs`).
   * For each pattern, the bot has one or more associated responses.

2. **Conversation Examples:**

   * **User:** *hi*, *hello* → **Bot:** *"Hello! How can I help you today?"*
   * **User:** *what is your name?* → **Bot:** *"I am CodTechBot, your assistant."*
   * **User:** *i need help with Python* → **Bot:** *"Sure, I can help you with Python. Please tell me more."*
   * **User:** *bye*, *quit* → **Bot:** *"Goodbye! Have a great day."*

3. **Default Response:**

   * If the input doesn't match any pattern, the bot replies:
     *"I'm sorry, I didn't understand that. Can you please rephrase?"*

4. **Reflections:**

   * NLTK's `reflections` is used to convert pronouns in responses (e.g., "I" to "you").


###  **How It Works:**

* When the script runs:

  * The bot greets the user.
  * It keeps taking user input until the user types `"quit"` or `"bye"`.
  * Responses are selected based on pattern matching using regular expressions.


###  **How to Run:**

1. Install NLTK if not already installed:

   ```bash
   pip install nltk
   ```
2. Run the Python script:

   ```bash
   python app.py
   ```
3. Interact with the chatbot in your terminal.



###  **Use Case:**

This chatbot is suitable as a **mini assistant** or **starter project** for learning chatbot logic, regular expressions, and basic NLP with NLTK.


##OUTPUT:
<img width="659" height="392" alt="Image" src="https://github.com/user-attachments/assets/e3111525-12ce-4f83-9437-e686bd9f91ef" />
