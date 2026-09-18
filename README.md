# AI Task Manager

A simple AI-powered task manager that lets you manage todos using natural language.

Instead of using separate forms or commands, you can simply tell the AI what you want to do. The agent then uses the appropriate tool to create, view, update, or delete tasks.

## Features

* Create tasks
* List and filter tasks
* Update tasks
* Delete tasks
* Set priority and due dates
* Natural language interaction

## Tech Stack

* Python
* LangChain
* LangGraph
* Groq
* Streamlit
* SQLAlchemy
* SQLite

## How It Works

```text
User
  ↓
Streamlit Chat UI
  ↓
AI Agent
  ↓
Task Tools
  ↓
SQLite Database
```

The agent has four main tools:

```text
create_todo()
list_todos()
update_todos()
delete_todo()
```

## Run Locally

```bash
git clone https://github.com/your-username/AI-Task-Manager.git
cd AI-Task-Manager

pip install -r requirements.txt
streamlit run app.py
```

Add your Groq API key to `.env`:

```env
GROQ_API_KEY=your_api_key_here
```

## Example

```text
"Create a high priority task to complete my resume."

"Show my pending tasks."

"Mark task 3 as done."

"Delete task 5."
```

## Author

Raj
GitHub: `Raj-Raaz`
