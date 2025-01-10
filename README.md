# **Teaching Assistant Project**

A scalable and AI-driven teaching assistant application designed to generate personalized teaching content, quizzes, and feedback using LangChain and modern AI technologies.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Folder Structure](#folder-structure)
7. [API Endpoints](#api-endpoints)
8. [Contributing](#contributing)
9. [License](#license)

---

## **Project Overview**
The Teaching Assistant Project uses advanced AI technologies to streamline the educational process by:
- Generating topic-specific teaching plans.
- Creating personalized quizzes.
- Providing constructive feedback for student responses.
- Supporting API integrations for seamless communication (e.g., via LINE Bot).

---

## **Features**
- **Teaching Plan Generation**: Generates detailed plans for teaching specific topics.
- **Quiz Creation**: Creates multiple-choice quizzes tailored to the input topic.
- **Feedback Mechanism**: Provides insightful feedback on student responses.
- **LangChain Integration**: Implements modular workflows and reusable prompts.
- **LINE Bot Support**: Enables user interaction through a conversational interface.

---

## **Tech Stack**
- **Programming Language**: Python (3.12+)
- **Frameworks**: Flask, LangChain
- **Database**: MySQL
- **Tools**: Poetry, dotenv, Git, GitHub Actions
- **AI Model**: OpenAI (or Gemini) API integration

---

## **Installation**

### **Prerequisites**
1. Python 3.12+
2. Git installed on your system
3. MySQL installed and running
4. Environment variables configured in a `.env` file

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/abbyyyli/teaching_assistant_project.git
   cd teaching_assistant_project
   ```

2. Set up the Python environment:
   ```bash
   poetry install
   ```

3. Configure the `.env` file:
   ```plaintext
   LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
   LINE_CHANNEL_SECRET=your_line_channel_secret
   GEMINI_API_KEY=your_gemini_api_key
   MYSQL_USER=root
   MYSQL_PASSWORD=your_password
   MYSQL_DB=teaching_assistant
   ```

4. Run database migrations:
   ```bash
   mysql -u root -p < migrations/001_create_tables.sql
   ```

5. Start the Flask application:
   ```bash
   poetry run python app/app.py
   ```

---

## **Usage**

### **Local Development**
1. Access the application via:
   ```plaintext
   http://127.0.0.1:5000/
   ```

2. Use tools like Postman or cURL to test API endpoints (see [API Endpoints](#api-endpoints)).

---

## **Folder Structure**
```plaintext
teaching_assistant_project/
├── app/
│   ├── api/
│   │   ├── content_generator.py
│   │   ├── quiz_generator.py
│   │   ├── feedback_generator.py
│   │   └── __init__.py
│   ├── prompts/
│   │   ├── teaching_prompt.json
│   │   ├── quiz_prompt.json
│   │   ├── feedback_prompt.json
│   │   └── __init__.py
│   ├── utils/
│   │   ├── database.py
│   │   ├── memory_manager.py
│   │   ├── logger.py
│   │   └── validators.py
│   └── app.py
├── migrations/
│   └── 001_create_tables.sql
├── tests/
│   ├── test_content_generator.py
│   ├── test_quiz_generator.py
│   ├── test_feedback_generator.py
│   └── __init__.py
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## **API Endpoints**
### **1. Teaching Content Generator**
- **Endpoint**: `/generate-teaching-content`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "topic": "Introduction to Machine Learning"
  }
  ```
- **Response**:
  ```json
  {
      "teaching_plan": "Detailed teaching plan for Machine Learning..."
  }
  ```

### **2. Quiz Generator**
- **Endpoint**: `/generate-quiz`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "topic": "Python Loops"
  }
  ```
- **Response**:
  ```json
  {
      "quiz": [
          {
              "question": "What is the syntax for a for loop in Python?",
              "options": ["for x in y", "for x : y"],
              "answer": "for x in y"
          }
      ]
  }
  ```

### **3. Feedback Generator**
- **Endpoint**: `/generate-feedback`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "response": "I think AI is just a tool."
  }
  ```
- **Response**:
  ```json
  {
      "feedback": "Good thought! AI is indeed a tool, but it also learns from data..."
  }
  ```

---

## **Contributing**
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to your forked repository:
   ```bash
   git push origin feature/your-feature
   ```
5. Create a pull request on the original repository.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

