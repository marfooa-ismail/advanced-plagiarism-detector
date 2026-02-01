# 🔍 Advanced NLP Plagiarism Detection System

[![Vercel Deploy](https://img.shields.io/badge/Vercel-Deploy-black?logo=vercel)](https://vercel.com)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

A modern, AI-powered plagiarism detection system with a stunning 3D glassmorphic interface. Built with advanced Natural Language Processing (NLP) techniques using Transformer AI models for accurate similarity detection.

![Advanced Plagiarism Detector](https://img.shields.io/badge/Status-Production-green)

## ✨ Features

### 🧠 **Advanced NLP Engine**
- **Transformer AI Model** - State-of-the-art sentence embeddings
- **Semantic Understanding** - Goes beyond simple word matching
- **Context-Aware Analysis** - Understands meaning and context
- **Multi-Algorithm Detection** - Combines multiple techniques for accuracy

### 📄 **Flexible Input Options**
- **Text Input** - Paste or type text directly
- **PDF Upload** - Automatic extraction from PDF documents
- **Batch Processing** - Compare multiple documents
- **Real-time Analysis** - Instant results as you type

### 📊 **Rich Visualizations**
- **Interactive Charts** - Visual representation of similarity scores
- **Detailed Reports** - Comprehensive analysis breakdown
- **Color-Coded Results** - Easy-to-understand severity indicators
- **Export Options** - Save results for later reference

### 🎨 **Modern UI/UX**
- **3D Glassmorphic Design** - Beautiful, modern interface
- **Responsive Layout** - Works on all devices
- **Smooth Animations** - Enhanced user experience
- **Dark Theme** - Eye-friendly design
- **Accessibility** - WCAG compliant

### 🔒 **Privacy & Security**
- **Client-Side Processing** - All analysis happens in your browser
- **No Data Upload** - Your documents never leave your device
- **No Server Required** - Pure client-side application
- **Secure Headers** - XSS and clickjacking protection

## 🚀 Quick Start

### Option 1: Use the Live Demo
Simply visit the deployed application and start using it immediately!

### Option 2: Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/marfooa-ismail/advanced-plagiarism-detector.git
   cd advanced-plagiarism-detector
   ```

2. **Open in browser**
   ```bash
   # Open the HTML file directly in your browser
   open advanced-plagiarism-detector.html
   # or on Windows
   start advanced-plagiarism-detector.html
   # or on Linux
   xdg-open advanced-plagiarism-detector.html
   ```

3. **Or use a local server** (recommended for full functionality)
   ```bash
   # Using Python 3
   python -m http.server 8000
   
   # Using Node.js
   npx http-server
   
   # Then open http://localhost:8000 in your browser
   ```

## 📖 Usage

### Text Comparison

1. **Switch to Text Mode** - Click the "Text Input" tab
2. **Enter Original Text** - Paste or type the original content in the left panel
3. **Enter Comparison Text** - Paste or type the text to check in the right panel
4. **Analyze** - Click the "🔍 Detect Plagiarism" button
5. **Review Results** - View similarity scores and detailed analysis

### PDF Comparison

1. **Switch to PDF Mode** - Click the "PDF Upload" tab
2. **Upload First PDF** - Click to select the original PDF document
3. **Upload Second PDF** - Click to select the document to check
4. **Analyze** - Click the "🔍 Detect Plagiarism" button
5. **Review Results** - View comprehensive similarity report

### Understanding Results

The system provides multiple similarity metrics:

- **Overall Similarity Score** - General similarity percentage (0-100%)
- **Semantic Similarity** - Contextual meaning comparison
- **Structural Similarity** - Document structure analysis
- **Lexical Similarity** - Word-level comparison

**Severity Levels:**
- 🟢 **Low** (0-30%) - Minimal similarity detected
- 🟡 **Medium** (31-60%) - Moderate similarity found
- 🟠 **High** (61-80%) - Significant similarity detected
- 🔴 **Critical** (81-100%) - Potential plagiarism

## 🛠️ Technology Stack

| Technology | Purpose |
|-----------|---------|
| **HTML5** | Application structure |
| **CSS3** | Modern styling & animations |
| **JavaScript (ES6+)** | Core functionality |
| **PDF.js** | PDF parsing and text extraction |
| **Chart.js** | Data visualization |
| **Transformer AI** | NLP sentence embeddings |
| **TF-IDF** | Text analysis algorithm |
| **Cosine Similarity** | Similarity measurement |

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         User Interface Layer            │
│  (3D Glassmorphic UI, Responsive)       │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│       Input Processing Layer            │
│  (Text Input / PDF Parser)              │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      NLP Analysis Engine                │
│  • Tokenization                         │
│  • Sentence Embeddings (Transformer)    │
│  • TF-IDF Vectorization                 │
│  • N-gram Analysis                      │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│     Similarity Computation              │
│  • Cosine Similarity                    │
│  • Jaccard Index                        │
│  • Semantic Distance                    │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      Results & Visualization            │
│  (Charts, Reports, Metrics)             │
└─────────────────────────────────────────┘
```

## 📦 Deployment

### Deploy to Vercel

The easiest way to deploy this application:

1. **Fork/Clone the repository**
2. **Sign up/Login to [Vercel](https://vercel.com)**
3. **Import the repository** from GitHub
4. **Deploy** - Vercel will automatically detect and deploy

For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

### Deploy to GitHub Pages

1. Go to repository Settings → Pages
2. Select branch and root folder
3. Save and wait for deployment
4. Access at `https://yourusername.github.io/advanced-plagiarism-detector/`

### Deploy to Netlify

1. Sign up/Login to [Netlify](https://netlify.com)
2. Drag and drop the project folder
3. Or connect GitHub repository for automatic deployments

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow existing code style and conventions
- Test thoroughly before submitting
- Update documentation for new features
- Keep commits focused and descriptive

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **PDF.js** - Mozilla's PDF parsing library
- **Chart.js** - Simple yet flexible JavaScript charting
- **Transformer Models** - For advanced NLP capabilities
- **Open Source Community** - For inspiration and support

## 📧 Contact & Support

- **Author**: Marfooa Ismail
- **Repository**: [github.com/marfooa-ismail/advanced-plagiarism-detector](https://github.com/marfooa-ismail/advanced-plagiarism-detector)
- **Issues**: [GitHub Issues](https://github.com/marfooa-ismail/advanced-plagiarism-detector/issues)

## 🎯 Roadmap

- [ ] Multi-language support
- [ ] Browser extension
- [ ] API integration options
- [ ] Advanced reporting features
- [ ] Document history tracking
- [ ] Batch processing improvements
- [ ] Machine learning model fine-tuning

## ⚠️ Disclaimer

This tool is designed to assist in detecting potential plagiarism. It should be used as a supplementary tool and not as the sole method for determining plagiarism. Always use human judgment and additional resources when making important decisions.

---

<div align="center">

**Made with ❤️ by Marfooa Ismail**

⭐ Star this repository if you find it helpful!

</div>
