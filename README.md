# 🎯 AI-Powered Competitor Analysis System
### *Customized Market Intelligence for Manufacturing | Ollama Mistral LLM Integration*

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![AI](https://img.shields.io/badge/AI-Ollama_Mistral-orange.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.17.0-purple.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

**Developed at TVS Sensing Solutions | Internship Project**

</div>

---

> **Note:** This is a portfolio project showcasing work completed during my Data Science internship at TVS Sensing Solutions. The repository is for demonstration purposes only.

---
## 💡 The Business Problem

At **TVS Sensing Solutions**, the business development team needed a tool to quickly generate competitor analysis for market positioning and strategic planning. The challenge was to create a customizable system that could:

- Generate competitor information based on specific product categories
- Focus on TVS's sensor manufacturing portfolio
- Provide structured, organized outputs for decision-making
- Deliver results faster than manual web research

**The Challenge:** Build a tool that generates product-specific competitor intelligence with automated data generation and visualization.

---

## ✨ My Solution

I designed and built an **AI-powered web application** that provides product-specific competitor intelligence tailored to TVS's manufacturing segments—from data collection to structured analysis and visualization.

### **What It Does:**
**Input:** User specifies product type (e.g., pressure sensors), market focus (Indian/Global), and competitor count  
**Process:** Feature Engineering → Dynamic Query Construction → Ollama Mistral LLM → Data Cleaning → Ranking Algorithm  
**Output:** Structured competitor profiles with interactive dashboard + Excel export

### **Key Innovation:**
Engineered intelligent **feature engineering and dynamic query construction** that transforms user inputs into precise AI prompts, ensuring the Ollama Mistral model generates structured, relevant competitor data. Implemented a sophisticated ranking algorithm that sorts competitors by market share and turnover to identify true market leaders.

---
 ## 📊 Business Impact

| Metric | Before | After | Result |
|--------|--------|-------|--------|
| **Analysis Tool** | Manual web research | AI-powered generation | **Faster results** |
| **Query Customization** | Generic searches | Product-specific prompts | **Targeted queries** |
| **Data Structure** | Unorganized notes | Structured DataFrames | **Analysis-ready** |
| **Output Format** | Manual compilation | Dashboard + Excel export | **Professional reports** |
| **Visualization** | Static notes | 6+ Interactive charts | **Better insights** |

**Real-World Results:**
- ✅ Built AI-powered system using Ollama Mistral LLM for competitor data generation
- ✅ Created product-specific prompt engineering for TVS's sensor portfolio
- ✅ Delivered interactive dashboard with 6+ Plotly visualizations
- ✅ Generated structured Excel reports for business presentations

---

## 🏗️ System Architecture

### **High-Level Architecture**

<div align="center">

<img width="1020" height="374" alt="System Architecture" src="https://github.com/user-attachments/assets/8120b217-b4e4-40e3-afd2-032cf0c4c1f7" />

</div>

<br>

**Architecture Overview:**
```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  Home Page   │  │ Input Form   │  │  Dashboard   │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   FLASK WEB APPLICATION                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Routes     │  │ Form Handler │  │ Template     │         │
│  │   (/index)   │  │   Validator  │  │  Renderer    │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                  PROMPT CONSTRUCTION MODULE                      │
│                                                                  │
│   Input: Product Type, Market, Sub-segment, Technology          │
│   Process: Combine → Format → Structure                         │
│   Output: "pressure sensors in automotive using MEMS"           │
│                                                                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│               DYNAMIC QUERY CONSTRUCTION                         │
│                                                                  │
│   Context: "I am an industrial expert in automotive..."         │
│   Query: "List top 10 Indian companies manufacturing..."        │
│   Format: JSON with 12 fields (Company, HQ, Market Share...)    │
│                                                                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    OLLAMA MISTRAL LLM                            │
│                                                                  │
│   Model: mistral                                                 │
│   Input: Structured prompt with context                         │
│   Output: JSON array of competitor objects                      │
│                                                                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│               DATA PROCESSING PIPELINE                           │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ JSON Parser  │→ │Data Cleaning │→ │Normalization │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                  │
│  • Remove markdown ```json``` tags                              │
│  • Convert "5%" → 5.0                                           │
│  • Convert "5 Billion USD" → 5000000000                         │
│  • Extract "500-1000 employees" → 750                           │
│                                                                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   RANKING ALGORITHM                              │
│                                                                  │
│   1. Sort by Market Share (descending)                          │
│   2. Then by Turnover (descending)                              │
│   3. Select Top N competitors                                   │
│                                                                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    OUTPUT GENERATION                             │
│                                                                  │
│  ┌──────────────────┐              ┌──────────────────┐        │
│  │  VISUALIZATIONS  │              │  EXCEL EXPORT    │        │
│  ├──────────────────┤              ├──────────────────┤        │
│  │ • Pie Chart      │              │ • XlsxWriter     │        │
│  │ • Bar Charts (3) │              │ • Formatted      │        │
│  │ • Scatter Plot   │              │ • All 12 fields  │        │
│  │ • Histogram      │              │ • Download ready │        │
│  └──────────────────┘              └──────────────────┘        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Five-Layer Architecture:**

**Layer 1: User Input** - Web form capturing product and market specifications  
**Layer 2: Flask Application** - Backend processing and routing  
**Layer 3: AI Engine** - Ollama Mistral for competitor data generation  
**Layer 4: Data Pipeline** - Cleaning, structuring, and ranking  
**Layer 5: Visualization** - Interactive Plotly dashboards and Excel export
---

## 🔄 System Workflow

### **Use Case Diagram**

<div align="center">
AI COMPETITOR ANALYSIS SYSTEM
ETITOR ANALYSIS SYSTEM
    ┌────────────────────────────────────────────────────────────┐
    │                                                            │
    │                                                            │
    │         ╔══════════════════════════════════╗               │
    │         ║   Input Product Specifications   ║               │
    │         ╚══════════════════════════════════╝               │
    │                      ▲                                     │
    │                      │                                     │
    │         ╔══════════════════════════════════╗               │
┌───┴───┐     ║  Generate Competitor Analysis    ║               │
│       │────▶╚══════════════════════════════════╝               │
│ User  │              ▲                                         │
│       │              │                                         │
└───┬───┘     ╔══════════════════════════════════╗              │
    │         ║   View Interactive Dashboard     ║              │
    │    ────▶╚══════════════════════════════════╝              │
    │                      ▲                                     │
    │                      │                                     │
    │         ╔══════════════════════════════════╗              │
    │         ║     Export Excel Report          ║              │
    │    ────▶╚══════════════════════════════════╝              │
    │                      ▲                                     │
    │                      │                                     │
    │         ╔══════════════════════════════════╗              │
    │         ║  Ask Custom Questions (Chatbot)  ║              │
    │    ────▶╚══════════════════════════════════╝              │
    │                                                            │
    │                                                            │
    └────────────────────────────────────────────────────────────┘


</div>

<br>

*Complete system capabilities showing user interactions and data flow*

<br><br>

### **Detailed Data Flow**

<div align="center">

External Entity          Process              Data Store
───────────────         ─────────            ───────────

                    ┌─────────────┐
    ┌──────┐        │   Capture   │
    │      │───────▶│User Inputs  │
    │ User │        │             │
    │      │        └──────┬──────┘
    └──────┘               │
                           ▼
                    ┌─────────────┐        ║════════════║
                    │   Feature   │───────▶║ Input Data ║
                    │ Engineering │        ║════════════║
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    Build    │
                    │ AI Prompt   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Ollama    │
                    │  Mistral    │
                    │     LLM     │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐        ║════════════║
                    │    Parse    │───────▶║   Raw      ║
                    │     JSON    │        ║ Competitor ║
                    └──────┬──────┘        ║   Data     ║
                           │               ║════════════║
                           ▼
                    ┌─────────────┐
                    │    Clean    │
                    │  & Normalize│
                    │     Data    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐        ║════════════║
                    │   Ranking   │───────▶║  Ranked    ║
                    │  Algorithm  │        ║ Competitor ║
                    └──────┬──────┘        ║   List     ║
                           │               ║════════════║
                ┌──────────┴──────────┐
                ▼                     ▼
         ┌─────────────┐       ┌─────────────┐
    ┌───│ Visualize   │       │   Export    │
    │   │  Dashboard  │       │    Excel    │
    │   └─────────────┘       └─────────────┘
    │          │                      │
    └──────────┴──────────────────────┘
               │
               ▼
           ┌──────┐
           │ User │
           └──────┘

</div>

<br>

*End-to-end processing pipeline from input to actionable insights*

---

## 🎬 Application Showcase

### **Home Page**

<div align="center">

<img width="1183" height="423" alt="Home Page" src="https://github.com/user-attachments/assets/96445ea8-8200-443a-86be-53b93665fbd1" />

</div>

<br>

*Landing page with navigation to analysis modules*

<br><br>

---

### **Input Form - Product Selection**

<div align="center">

<img width="1182" height="563" alt="Input Form 1" src="https://github.com/user-attachments/assets/5bdfa6a4-1dde-4da3-b7de-c9cf6df94c29" />

</div>

<br>

*User specifies market type, product segment, and competitor filters*

<br><br>

---

### **Input Form - Technology Details**

<div align="center">

<img width="1182" height="566" alt="Input Form 2" src="https://github.com/user-attachments/assets/804a9395-5b72-4aeb-b80d-e4a5a4ab89e0" />

</div>

<br>

*Additional filters for sub-segment and technology specifications*

<br><br>

---

### **Analytics Dashboard Overview**

<div align="center">

<img width="1183" height="496" alt="Dashboard" src="https://github.com/user-attachments/assets/bb255363-32f1-40de-9448-3f2aeaa816a1" />

</div>

<br>

*Interactive dashboard with multiple visualization types*

<br><br>

---

### **Market Share Distribution**

<div align="center">

<img width="1182" height="571" alt="Market Share Pie" src="https://github.com/user-attachments/assets/aed46273-b0c9-4c20-a748-dfc24dab1396" />

</div>

<br>

*Pie chart showing competitive landscape distribution*

<br><br>

---

### **Market Share Comparison**

<div align="center">

<img width="1182" height="543" alt="Market Share Bar" src="https://github.com/user-attachments/assets/74a4733f-3957-4444-b15a-9ce102b36036" />

</div>

<br>

*Bar chart comparing competitor market positions*

<br><br>

---

### **Employee Count Analysis**

<div align="center">

<img width="1182" height="551" alt="Employee Count" src="https://github.com/user-attachments/assets/9b83a202-ffec-4ce4-9a76-9566bae26d4a" />

</div>

<br>

*Organizational scale comparison across competitors*

<br><br>

---

### **Efficiency Matrix (Market Share vs Employees)**

<div align="center">

<img width="1182" height="548" alt="Efficiency Matrix" src="https://github.com/user-attachments/assets/0ec3348d-aafd-49d6-860d-5870bcdb7133" />

</div>

<br>

*Scatter plot identifying high-performing companies with optimal resource utilization*

<br><br>

---

### **AI Research Assistant (ComPIBOT)**

<div align="center">

<img width="1183" height="559" alt="Chatbot" src="https://github.com/user-attachments/assets/3e1e0e63-4eda-48d3-afa3-080e45801160" />

</div>

<br>

*Conversational interface for ad-hoc competitor research queries*

<br><br>

---

### **Excel Export Sample**

<div align="center">

<img width="948" height="561" alt="Excel Export" src="https://github.com/user-attachments/assets/7185e81f-5af6-459d-ae45-f8f0b20cd1d0" />

</div>

<br>

*Structured data export for business presentations and reports*

<br><br>

---

## ⚙️ Technical Architecture

### **Core Components I Built:**

**1. User Input Processing Module**
- Flask form handling for product specifications
- Market type selection (Indian/Global)
- Competitor count configuration
- Dynamic field validation

**2. Feature Engineering Engine**
- Product description builder
- Sub-segment combination logic
- Technology specification integration
- Structured query formation

**3. AI Integration Layer**
- Ollama Mistral LLM integration
- Context-aware prompt engineering
- JSON response parsing
- Error handling and retry logic

**4. Data Processing Pipeline**
- Market share normalization (%, Billion, Million, USD)
- Turnover standardization across currencies
- Employee range extraction (e.g., "500-1000" → 750)
- Missing data handling

**5. Ranking Algorithm**
- Dual-criteria sorting (Market Share × Turnover)
- Top N competitor selection
- Tie-breaking logic
- Data completeness scoring

**6. Visualization Module**
- 6+ distinct Plotly chart generators
- Market share pie charts
- Employee count bar charts
- Efficiency scatter plots
- Revenue distribution histograms
- Interactive HTML rendering

**7. Export Service**
- XlsxWriter integration
- Structured Excel formatting
- In-memory file generation
- Browser download handling

**8. Web Interface**
- Flask routing and template rendering
- Responsive Bootstrap UI
- Real-time dashboard updates
- Custom prompt chatbot interface

---

## 🛠️ Technology Stack

| Category | Technologies | Purpose |
|----------|-------------|---------|
| **Backend** | Python 3.11, Flask 3.0.0 | Web framework, API routing, business logic |
| **AI/NLP** | Ollama 0.6.2, Mistral LLM | Competitor insight generation, structured output |
| **Data Processing** | Pandas 2.1.1, NumPy | Data manipulation, cleaning, ranking algorithms |
| **Visualization** | Plotly 5.17.0 | Interactive charts and dashboards |
| **Export** | XlsxWriter | Professional Excel report generation |
| **Frontend** | HTML5, CSS3, Bootstrap, JavaScript | Responsive UI, dynamic interactions |

---

## 🎯 Key Features

### **What Makes This System Powerful:**

✅ **Product-Specific Intelligence** - Filters competitors based on TVS's exact manufacturing segments

✅ **AI-Powered Generation** - Ollama Mistral creates structured competitor profiles on demand

✅ **Smart Ranking Algorithm** - Dual-criteria sorting by market share and turnover

✅ **Interactive Dashboards** - 6+ visualizations for comprehensive analysis

✅ **Excel Export** - Professional reports ready for presentations

✅ **Customizable Filters** - Market type, product segment, sub-segment, technology

✅ **Real-Time Results** - Instant competitor intelligence generation

✅ **Chatbot Interface** - Ad-hoc research queries with conversational AI

---

## 💼 Real-World Impact

### **Internship Deployment Results:**

📈 **Automation:** Replaced manual competitor research with AI-powered generation

📊 **Relevance:** Product-specific filtering ensures only relevant competitors

🎯 **Speed:** Instant results vs hours of manual research

💡 **Structure:** Organized data ready for strategic planning

🔍 **Completeness:** 12 key metrics per competitor (vs 3-4 with manual methods)

⚡ **Scalability:** Analyze 5-50 competitors in single query

---

## 💻 Technical Skills Demonstrated

### **AI/ML Engineering:**
- Large Language Model (LLM) integration
- Prompt engineering for structured outputs
- JSON parsing and validation
- Context-aware query construction

### **Backend Development:**
- Flask web application development
- RESTful API design
- Dynamic form handling
- File generation and download

### **Data Engineering:**
- ETL pipeline development
- Multi-format data cleaning
- Currency and percentage normalization
- Ranking algorithm implementation

### **Data Visualization:**
- Business intelligence dashboard design
- Interactive Plotly charts
- Statistical visualization
- Export functionality

### **Full-Stack Development:**
- Frontend UI/UX design
- Backend logic implementation
- Database-less architecture
- End-to-end system integration

---

## 🚀 Development Process

### **How I Built This:**

**1. Requirements Gathering** - Met with TVS business team to understand competitor analysis needs

**2. System Design** - Architected AI-powered solution with Ollama Mistral integration

**3. Feature Engineering** - Built intelligent query construction from user inputs

**4. AI Integration** - Implemented LLM prompting with structured output validation

**5. Data Pipeline** - Developed cleaning and ranking algorithms for multiple data formats

**6. Visualization** - Created 6+ interactive dashboards for analysis

**7. Testing & Validation** - Comprehensive testing with TVS team feedback

---

## 📊 Results & Impact

- **Product-specific filtering** for TVS's sensor portfolio (pressure, speed, temperature, position)
- **6+ interactive visualizations** for comprehensive competitor analysis
- **12 key metrics** extracted per competitor (Company, HQ, Market Share, Products, etc.)
- **Excel export functionality** for business presentations
- **Real-time AI generation** replacing hours of manual research

---

## 🔮 Future Enhancements

- **Real-time web scraping:** Automated updates from competitor websites
- **Sentiment analysis:** Analyze customer reviews and social media
- **Predictive analytics:** Forecast competitor market share trends
- **Mobile app:** On-the-go competitor intelligence access

---

## 🤝 Let's Connect

I'm a **Data Analytics Engineering graduate student at Northeastern University** seeking **co-op/full-time Data Analyst or Data Scientist roles**.

This project demonstrates my ability to:
- ✅ Build AI-powered applications using Large Language Models
- ✅ Design interactive dashboards for business intelligence
- ✅ Develop product-specific analysis tools for manufacturing companies
- ✅ Work independently on end-to-end projects from requirements to deployment

**Interested in discussing how I can bring similar innovation to your team?**

<div align="center">

📧 **Email:** varaalakshime.l@northeastern.edu  
💼 **LinkedIn:** [https://www.linkedin.com/in/varaalakshime-v]  

**Available for Co-op:** May 2025 - December 2025

</div>

---

## 📄 Project Context

Developed during Data Scientist internship at **TVS Sensing Solutions Private Limited, Madurai** - A leading manufacturer of advanced sensing technologies and electronic components under the TVS Group, specializing in pressure sensors, speed sensors, temperature sensors, and position sensors for automotive and industrial applications.

**Internship Duration:** December 16, 2024 - April 23, 2025  
**Academic Program:** 5 Year Integrated M.Sc. (Data Science), Thiagarajar College of Engineering

---

## 📚 References & Standards

- **Ollama Documentation** - LLM integration and prompt engineering
- **Flask Documentation** - Web framework implementation
- **Plotly Documentation** - Interactive visualizations
- **Pandas Documentation** - Data manipulation and analysis

---

## 🙏 Acknowledgments

- **TVS Sensing Solutions Private Limited** - Internship opportunity and domain expertise
- **Dr. M. S. Sabitha** (External Guide) - Technical guidance and project mentorship
- **Dr. C. Mahadevi** (Internal Guide) - Academic supervision
- **Thiagarajar College of Engineering** - Academic support and resources

---

<div align="center">

**⭐ Built with Flask • Ollama Mistral • Plotly • Pandas ⭐**

*Transforming Market Research Through AI Automation*

### ⭐ If you found this project helpful, please star the repository!

**Built with ❤️ for competitive intelligence and AI-powered analytics**

</div>
