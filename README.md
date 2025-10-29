 # 🤖 Jarvis - AI Voice Assistant

A real-time voice-based AI assistant powered by LiveKit and Google's Realtime Model, inspired by Iron Man's Jarvis. This intelligent assistant can help you with weather information, web searches, and sending emails through natural voice conversations.

## ✨ Features

- **🌤️ Weather Information**: Get current weather updates for any city worldwide
- **🔍 Web Search**: Search the web using DuckDuckGo integration
- **📧 Email Sending**: Send emails via Gmail with support for CC recipients
- **🎙️ Voice Interaction**: Real-time voice communication with noise cancellation
- **🎥 Video Support**: Video-enabled sessions for enhanced interaction

## 🛠️ Technologies Used

- **LiveKit**: Real-time communication framework
- **Google Realtime Model**: AI-powered voice assistant (Charon voice)
- **DuckDuckGo Search**: Privacy-focused web search
- **Python**: Core programming language
- **SMTP**: Email sending functionality

## 📋 Prerequisites

- Python 3.8 or higher
- Gmail account (for email functionality)
- LiveKit account and credentials
- Google API credentials

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Jarvis
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root with the following:
   ```env
   GMAIL_USER=your-email@gmail.com
   GMAIL_PASSWORD=your-app-password
   LIVEKIT_URL=your-livekit-url
   LIVEKIT_API_KEY=your-api-key
   LIVEKIT_API_SECRET=your-api-secret
   GOOGLE_API_KEY=your-google-api-key
   ```

   **Note**: For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.

## 💻 Usage

Run the assistant using:

```bash
python agents.py
```

Or use the LiveKit CLI:

```bash
livekit-agents start
```

## 🎯 Available Commands

Once the assistant is running, you can interact with it using voice commands:

- **Weather**: "What's the weather in New York?"
- **Web Search**: "Search for Python tutorials"
- **Send Email**: "Send an email to john@example.com with subject 'Meeting' and message 'Let's meet tomorrow'"

## 📁 Project Structure

```
Jarvis/
├── agents.py           # Main agent configuration and entry point
├── tools.py            # Tool functions (weather, search, email)
├── prompts.py          # Agent instructions and prompts
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in repo)
└── README.md          # This file
```

## 🔧 Configuration

### Agent Settings

The assistant uses the following configuration:
- **Voice**: Charon (Google Realtime Model)
- **Temperature**: 0.7 (for response variability)
- **Noise Cancellation**: BVC (Best Voice Cancellation)
- **Video**: Enabled

You can modify these settings in `agents.py`.

## 🛡️ Security Notes

- Never commit your `.env` file to version control
- Use App Passwords for Gmail authentication
- Keep your API keys secure
- Review email recipients before sending

## 🐛 Troubleshooting

### Email Not Sending
- Verify Gmail credentials in `.env`
- Ensure you're using an App Password, not your regular password
- Check if "Less secure app access" is enabled (if applicable)

### Weather API Issues
- Check your internet connection
- The weather service (wttr.in) might be temporarily unavailable

### LiveKit Connection Issues
- Verify your LiveKit credentials in `.env`
- Check if your LiveKit server is running

## 📝 To-Do

- [ ] Add more tools (calendar, reminders, etc.)
- [ ] Implement conversation history
- [ ] Add support for multiple languages
- [ ] Create a web interface
- [ ] Add unit tests

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a beginner Python project to learn about AI assistants and real-time communication.

## 🙏 Acknowledgments

- Inspired by Marvel's Jarvis from Iron Man
- Built with LiveKit and Google's AI technologies
- Thanks to the open-source community

---

**Note**: This is a learning project. Use it responsibly and ensure you comply with all relevant terms of service for the APIs used.
