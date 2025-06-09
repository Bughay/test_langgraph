# Langgraph simple bot

A simple LangGraph-based chat bot that responds to user messages and can fetch the current UTC time when asked. This task demonstrates stateless conversation handling and tool usage with a single `get_current_time` function.

## How to Run

### 1. **Clone the Repository**
   ```bash
   git clone https://github.com/Bughay/test_langgraph
   cd test_langgraph
   ```

### 2. **Set Up a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

### 3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### 4. **Launch the Application**
   ```bash
   langgraph dev
   ```

## Testing the Bot

- The bot will respond to any message you send.
- To test the time functionality, ask:  
  **"What time is it?"**  
  The bot will call the `get_current_time` tool and return the current UTC time in ISO-8601 format.

![image](https://github.com/user-attachments/assets/052ac455-a32b-48ae-a10b-c134a639453a)

the bot even succesfully answers the time when asked indirectly ' what happens when i look at the clock ?'

---





![image](https://github.com/user-attachments/assets/dfd09904-946e-4b91-9537-c0e64d0c7d07)
