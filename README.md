# 🏥 Healthcare Bot

A modern, interactive healthcare chatbot with a beautiful glassmorphism UI design that helps users collect and analyze their medical symptoms through an intuitive chat interface.

[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/ShoyebRampure/Healthcare_bot)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue)](https://github.com/ShoyebRampure/Healthcare_bot)
[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/ShoyebRampure/Healthcare_bot)

## ✨ Features

- **Modern UI Design**: Glassmorphism interface with animated gradients and smooth transitions
- **Interactive Chat Interface**: Real-time messaging with typing indicators and animations
- **Symptom Collection**: Systematic collection of user symptoms for medical analysis
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Processing**: Instant responses and dynamic user interaction
- **Beautiful Animations**: Smooth micro-interactions and visual feedback

## 🎨 UI Highlights

- **Glassmorphism Design**: Semi-transparent elements with backdrop blur effects
- **Vibrant Gradients**: Eye-catching color schemes with animated backgrounds
- **Interactive Elements**: Hover effects, loading states, and smooth transitions
- **Message Avatars**: Visual indicators for bot and user messages
- **Status Indicators**: Real-time connection status display
- **Custom Scrollbars**: Styled scrollbars for better user experience

## 🚀 Getting Started

### Prerequisites

- Web browser (Chrome, Firefox, Safari, etc.)
- Basic web server (for API endpoints)
- Node.js (if running backend services)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShoyebRampure/Healthcare_bot.git
   cd Healthcare_bot
   ```

2. **Open the HTML file**
   ```bash
   # Option 1: Direct file opening
   open index.html
   
   # Option 2: Using a local server
   python -m http.server 8000
   # Then visit http://localhost:8000
   ```

3. **Set up backend (if required)**
   ```bash
   # Install dependencies
   npm install
   
   # Start the server
   npm start
   ```

## 💡 Usage

1. **Start Conversation**: Open the chat interface in your browser
2. **Enter Name**: Provide your name when prompted
3. **Describe Symptoms**: Enter your symptoms one by one as requested
4. **Get Analysis**: The bot processes your symptoms and provides feedback

### User Flow

```
User Opens Chat → Enters Name → Symptom 1 → Symptom 2 → Symptom 3 → Analysis
```

## 🏗️ Project Structure

```
Healthcare_bot/
├── index.html              # Main chat interface
├── styles/
│   ├── main.css            # Core styling
│   └── animations.css      # Animation definitions
├── scripts/
│   ├── chat.js             # Chat functionality
│   └── api.js              # API interactions
├── backend/
│   ├── app.py              # Flask/FastAPI backend
│   └── models/             # ML models
└── README.md               # Project documentation
```

## 🔧 Configuration

### API Endpoints

The chat interface expects the following endpoints:

```javascript
// Get bot response
POST /get_response
{
  "message": "user_input"
}

// Send symptoms for analysis
POST /send_symptoms
{
  "symptoms": ["symptom1", "symptom2", "symptom3"]
}
```

### Customization

**Colors**: Modify the CSS gradient variables in the `<style>` section:
```css
:root {
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --secondary-gradient: linear-gradient(135deg, #ff6b6b, #4ecdc4);
}
```

**Animations**: Adjust animation timing in the CSS:
```css
.chat-message {
  animation: messageSlide 0.4s ease-out;
}
```

## 🤖 Bot Logic

The healthcare bot follows this conversation flow:

1. **Greeting**: Welcomes user and requests name
2. **Symptom Collection**: Systematically collects 3 symptoms
3. **Processing**: Sends symptoms to ML model/API for analysis
4. **Response**: Provides health insights or recommendations

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with Glassmorphism effects
- **Fonts**: Google Fonts (Inter)
- **Icons**: Unicode emojis for avatars
- **Backend**: Python Flask/FastAPI (configurable)
- **ML Integration**: Compatible with various ML frameworks

## 📱 Browser Support

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🔮 Future Enhancements

- [ ] Voice input/output capabilities
- [ ] Multi-language support
- [ ] Medical report generation
- [ ] Integration with medical databases
- [ ] Appointment scheduling
- [ ] Dark/Light theme toggle
- [ ] Export chat history
- [ ] Advanced symptom analysis

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow semantic commit messages
- Maintain consistent code formatting
- Add comments for complex logic
- Test across different browsers
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Shoyeb Rampure**
- Email: [shoyebrampure@gmail.com](mailto:shoyebrampure@gmail.com)
- GitHub: [@ShoyebRampure](https://github.com/ShoyebRampure)
- LinkedIn: [Shoyeb Rampure](https://linkedin.com/in/shoyebrampure)

## 🙏 Acknowledgments

- Thanks to the open-source community for inspiration
- Medical professionals for guidance on healthcare chatbot design
- UI/UX designers for modern design patterns
- Beta testers for valuable feedback

## 📞 Support

If you encounter any issues or have questions:

1. **Check existing issues**: [GitHub Issues](https://github.com/ShoyebRampure/Healthcare_bot/issues)
2. **Create new issue**: Describe the problem with steps to reproduce
3. **Email support**: [shoyebrampure@gmail.com](mailto:shoyebrampure@gmail.com)

---

**⚠️ Medical Disclaimer**: This chatbot is for informational purposes only and should not replace professional medical advice. Always consult with qualified healthcare providers for medical concerns.

**🌟 Star this repository if you found it helpful!**
