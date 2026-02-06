# 🎯 AI-Powered Competitor Analysis System
### *Market Intelligence Tool with LLM Integration*

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![AI](https://img.shields.io/badge/AI-Ollama_Mistral-orange.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.17.0-purple.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

**Developed at TVS Sensing Solutions | Internship Project**

</div>

---

> **Note:** This is a portfolio project showcasing work completed during my Data Science internship at TVS Sensing Solutions.

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

I built an **AI-powered web application** using Flask and Ollama Mistral LLM that generates competitor profiles based on user-specified criteria.

### **What It Does:**
**Input:** User specifies product type (e.g., pressure sensors), market focus (Indian/Global), and number of competitors  
**Process:** Dynamic Query Construction → Ollama Mistral LLM → Data Processing → Ranking  
**Output:** Structured competitor profiles with interactive dashboard + Excel export

### **Key Innovation:**
Designed intelligent **prompt engineering** that transforms user inputs into structured queries for the Ollama Mistral model. Implemented data cleaning and a ranking algorithm that sorts generated competitor data by market share and turnover.

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
```
                    ┌──────────────────────────┐
                    │         USER             │
                    └───────────┬──────────────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
                ▼               ▼               ▼
    ┌──────────────────┐  ┌─────────────┐  ┌─────────────┐
    │ Input Product    │  │View         │  │Export Excel │
    │ Specifications   │  │Dashboard    │  │Report       │
    └──────────────────┘  └─────────────┘  └─────────────┘
                │
                ▼
    ┌──────────────────────┐
    │ Generate Competitor  │
    │ Analysis             │
    └──────────────────────┘
                │
                ▼
    ┌──────────────────────┐
    │ Ask Custom Questions │
    │ (Chatbot)            │
    └──────────────────────┘
```

*Complete system capabilities showing user interactions*

<br>

### **Detailed Data Flow Diagram**
```
                    ┌──────────┐
                    │   USER   │
                    └─────┬────┘
                          │
                          ▼
                 ┌────────────────┐
                 │  Input Form    │
                 │ • Product Type │
                 │ • Market       │
                 │ • Count        │
                 └────────┬───────┘
                          │
                          ▼
                 ┌────────────────┐
                 │ Build Prompt   │
                 │ Construction   │
                 └────────┬───────┘
                          │
                          ▼
                 ┌────────────────┐
                 │ Ollama Mistral │
                 │      LLM       │
                 └────────┬───────┘
                          │
                          ▼
                 ┌────────────────┐
                 │  Parse JSON    │
                 │   Response     │
                 └────────┬───────┘
                          │
                          ▼
                 ┌────────────────┐
                 │ Clean & Norm.  │
                 │     Data       │
                 └────────┬───────┘
                          │
                          ▼
                 ┌────────────────┐
                 │ Rank by Market │
                 │ Share/Turnover │
                 └────────┬───────┘
                          │
                ┌─────────┴─────────┐
                ▼                   ▼
         ┌─────────────┐     ┌─────────────┐
         │   Plotly    │     │   Excel     │
         │  Dashboard  │     │   Export    │
         └──────┬──────┘     └──────┬──────┘
                │                   │
                └─────────┬─────────┘
                          │
                          ▼
                    ┌──────────┐
                    │   USER   │
                    └──────────┘
```

*End-to-end processing pipeline from input to output*

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

### **Market Toggle & Excel Download**

<div align="center">

<img width="1182" height="196" alt="Toggle Switch" src="https://github.com/user-attachments/assets/e84acfc8-e6bd-4004-b897-70a819045c53" />

<img width="1183" height="172" alt="Excel Download" src="https://github.com/user-attachments/assets/03f0cced-4bf7-431a-882a-f0163ff5cbb9" />

</div>

<br>

*Indian/Global market toggle and instant Excel download functionality*

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

*Scatter plot identifying company size and market position*

<br><br>

---

### **AI Research Assistant (ComPIBOT)**

<div align="center">

<img width="1183" height="558" alt="Chatbot" src="https://github.com/user-attachments/assets/3a877b09-b059-43d5-b743-c83681ed6d52" />

</div>

<br>

*Conversational interface for ad-hoc queries*

<br><br>

---

### **Excel Export Sample**

<div align="center">

<img width="948" height="561" alt="Excel Export" src="https://github.com/user-attachments/assets/7185e81f-5af6-459d-ae45-f8f0b20cd1d0" />

</div>

<br>

*Structured data export for reports*

<br><br>

---

## ⚙️ Technical Architecture

### **Core Components I Built:**

**1. User Input Processing Module**
- Flask form handling for product specifications
- Market type selection (Indian/Global)
- Competitor count configuration
- Dynamic field validation

**2. Prompt Construction Engine**
- Product description builder
- Sub-segment combination logic
- Technology specification integration
- Structured query formation

**3. AI Integration Layer**
- Ollama Mistral LLM integration
- Context-aware prompt engineering
- JSON response parsing
- Error handling for invalid responses

**4. Data Processing Pipeline**
- Market share normalization (%, Billion, Million, USD)
- Turnover standardization across currencies
- Employee range extraction (e.g., "500-1000" → 750)
- Data type conversion and cleaning

**5. Ranking Algorithm**
- Dual-criteria sorting (Market Share × Turnover)
- Top N competitor selection
- Handles missing values

**6. Visualization Module**
- 6 distinct Plotly chart types
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
| **Backend** | Python 3.11, Flask 3.0.0 | Web framework, routing, business logic |
| **AI/NLP** | Ollama 0.6.2, Mistral LLM | Competitor data generation |
| **Data Processing** | Pandas 2.1.1 | Data manipulation, cleaning, ranking |
| **Visualization** | Plotly 5.17.0 | Interactive charts and dashboards |
| **Export** | XlsxWriter | Excel report generation |
| **Frontend** | HTML5, CSS3, Bootstrap | Responsive UI |
| **Testing** | Pytest | Unit testing |

---

## 🎯 Key Features

### **What This System Does:**

✅ **Dynamic Form Processing** - Captures user specifications for competitor analysis

✅ **LLM Integration** - Uses Ollama Mistral to generate structured competitor data

✅ **Smart Data Cleaning** - Normalizes multiple data formats from LLM responses

✅ **Ranking Algorithm** - Sorts competitors by market share and turnover

✅ **Interactive Dashboards** - 6 visualizations for data analysis

✅ **Excel Export** - Professional reports ready for download

✅ **Customizable Queries** - Market type, product segment, sub-segment, technology filters

✅ **Chatbot Interface** - Ad-hoc queries with conversational AI

---

## 💻 Technical Skills Demonstrated

### **AI/ML Engineering:**
- Large Language Model (LLM) integration
- Prompt engineering for structured outputs
- JSON parsing and validation
- Context-aware query construction

### **Backend Development:**
- Flask web application development
- Dynamic form handling
- File generation and download
- Error handling

### **Data Engineering:**
- Data cleaning pipeline
- Multi-format normalization
- Currency and percentage standardization
- Ranking algorithm implementation

### **Data Visualization:**
- Dashboard design
- Interactive Plotly charts
- Multiple visualization types
- Export functionality

### **Full-Stack Development:**
- Frontend UI/UX design
- Backend logic implementation
- Template rendering
- End-to-end system integration

---

## 🚀 Development Process

### **How I Built This:**

**1. Requirements Gathering** - Understood competitor analysis needs from TVS team

**2. System Design** - Designed Flask application with LLM integration

**3. Prompt Engineering** - Built dynamic query construction from user inputs

**4. AI Integration** - Implemented Ollama Mistral with structured output validation

**5. Data Pipeline** - Developed cleaning and ranking algorithms

**6. Visualization** - Created 6 interactive dashboards

**7. Testing** - Built pytest test suite for validation

---

## 🧪 Testing

Created test suite using pytest to validate:
- Page loading and routing
- Custom prompt functionality
- Response accuracy against expected outputs
```python
# Sample test structure
def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_response_accuracy():
    expected_output = ["Bosch", "TE Connectivity", "Sensata"]
    # Validate chatbot responses
```

---

## 🤝 Let's Connect

I'm a **Data Analytics Engineering graduate student at Northeastern University** seeking **co-op/full-time Data Analyst or Data Scientist roles**.

This project demonstrates my ability to:
- ✅ Build AI-powered applications using Large Language Models
- ✅ Design interactive dashboards for data visualization
- ✅ Develop end-to-end web applications
- ✅ Work independently on complete project lifecycle

**Interested in discussing this project?**

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

## 📚 References

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

*AI-Powered Competitor Analysis Tool*

### ⭐ If you found this project helpful, please star the repository!

</div>
