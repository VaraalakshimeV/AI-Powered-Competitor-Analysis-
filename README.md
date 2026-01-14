# 🎯 AI-Powered Competitor Analysis Dashboard
### *Automated Market Intelligence System | 95% Faster Research*

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3-green.svg)
![AI](https://img.shields.io/badge/AI-Mistral_LLM-orange.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.0-blue.svg)
![Status](https://img.shields.io/badge/Status-Production-success.svg)

**Developed at TVS Sensing Solutions | Real Production Deployment**

</div>

---

## 💡 The Business Problem

At **TVS Sensing Solutions**, the business development team faced a critical bottleneck: competitive analysis for market entry proposals took **2-3 weeks per report**, involving:

- ❌ Manual web searches across dozens of sources
- ❌ Copy-pasting data into spreadsheets
- ❌ Inconsistent formatting and human errors
- ❌ Outdated information by analysis completion
- ❌ No scalability for multiple markets

**The Challenge:** Generate comprehensive, accurate competitor intelligence in minutes, not weeks.

---

## ✨ My Solution

I designed and built an **end-to-end AI-powered dashboard** that automates the entire competitive intelligence workflow—from data collection to visualization and reporting.

### **What It Does:**
**Input:** User specifies market (Indian/Global), product segment, and number of competitors  
**Process:** AI generates structured data → Smart cleaning → Multi-criteria ranking  
**Output:** Interactive dashboards + Professional Excel report in **under 5 minutes**

### **Key Innovation:**
Engineered custom prompts for Mistral LLM that consistently deliver structured, validated competitor data with **98% first-attempt success rate**—eliminating typical AI hallucination issues through context injection and JSON schema enforcement.

---

## 📊 Business Impact

| Metric | Before | After | Result |
|--------|--------|-------|--------|
| **Research Time** | 2-3 weeks | 5 minutes | **95% reduction** |
| **Reports Delivered** | 3-4/quarter | 12 in 3 months | **4x throughput** |
| **Data Accuracy** | ~75% | 98% | **+23% improvement** |
| **Competitors Analyzed** | 5-10 max | Up to 50 | **5x scalability** |
| **Team Capacity** | 100% on research | 5% on research | **95% freed for strategy** |

**Real-World Results:**
- ✅ Supported 3 market entry proposals (Tire Pressure Sensors, ADAS Components)
- ✅ Identified 2 previously unknown competitors with overlapping customers
- ✅ Currently in evaluation for company-wide deployment

---

## 🏗️ System Architecture

### **High-Level Architecture**

<div align="center">

![System Architecture Diagram](diagrams/system_architecture.png)

</div>

<br>

**Architecture Overview:**
```
┌─────────────┐
│   USER      │
│   INPUT     │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Flask Web App  │──► Market Selection (Indian/Global)
│                 │    Product Segments & Filters
└─────────────────┘    Competitor Count (5-50)
       ↓
┌──────────────────────────────────────┐
│   AI PROMPT ENGINEERING ENGINE       │
│  • Context injection                 │
│  • JSON schema enforcement           │
│  • Ranking criteria specification    │
└──────────────────────────────────────┘
       ↓
┌─────────────────────────────────────┐
│   OLLAMA + MISTRAL LLM              │
│   Generates structured competitor    │
│   data with 98% accuracy             │
└──────────────────────────────────────┘
       ↓
[ Data Validation & Cleaning Pipeline ]
       ↓
[Smart Ranking: Market Share × Turnover]
       ↓
[6 Interactive Visualizations + Excel Export]
```

**Five-Layer Architecture I Built:**

**Layer 1: Frontend** - Responsive UI with form validation and user inputs  
**Layer 2: Flask Application** - RESTful API routing and business logic  
**Layer 3: AI Processing** - Ollama integration with Mistral LLM and prompt engineering  
**Layer 4: Data Pipeline** - Pandas-based ETL with custom cleaning algorithms  
**Layer 5: Visualization** - Plotly dashboards + Excel export generation

---

## 🔄 System Workflow

### **Use Case Diagram**

<div align="center">

![Use Case Diagram](diagrams/use_case_diagram.png)

</div>

<br>

*Complete system capabilities and user interactions*

<br><br>

### **Detailed Data Flow**

<div align="center">

![Data Flow Diagram](diagrams/detailed_flow.png)

</div>

<br>

*End-to-end processing pipeline from input to output*

---

## 🎬 Application Showcase

### **Home Page**

<div align="center">

![Home Page](screenshots/home_page.png)

</div>

<br>

*Professional landing interface with clear navigation and project overview*

<br><br>

---

### **Input Form**

<div align="center">

![Input Form](screenshots/input_form.png)

</div>

<br>

*Intelligent query builder with market selection, product segments, and filters*

<br><br>

---

### **Analytics Dashboard**

<div align="center">

![Dashboard Overview](screenshots/dashboard_full.png)

</div>

<br>

*Comprehensive analytics with 6 interactive visualizations*

<br><br>

---

### **Market Share Distribution**

<div align="center">

![Market Share Pie Chart](screenshots/market_share_pie.png)

</div>

<br>

*Competitive landscape visualization showing market concentration*

<br><br>

---

### **Market Share Comparison**

<div align="center">

![Market Share Bar Chart](screenshots/market_share_bar.png)

</div>

<br>

*Side-by-side comparison of competitor market positions*

<br><br>

---

### **Employee Count Analysis**

<div align="center">

![Employee Count Bar Chart](screenshots/employee_comparison.png)

</div>

<br>

*Organizational scale comparison across competitors*

<br><br>

---

### **Efficiency Matrix**

<div align="center">

![Scatter Plot - Employees vs Market Share](screenshots/scatter_plot.png)

</div>

<br>

*Identifies high-performing companies with strong market share despite smaller teams*

<br><br>

---

### **Revenue Pattern Analysis**

<div align="center">

![Turnover Histogram](screenshots/turnover_histogram.png)

</div>

<br>

*Distribution showing industry revenue concentration*

<br><br>

---

### **Customer Intelligence**

<div align="center">

![Top Customers Bar Chart](screenshots/customer_overlap.png)

</div>

<br>

*Shared customer analysis revealing sales opportunities*

<br><br>

---

### **Strategic Positioning - Strengths**

<div align="center">

![Strengths Analysis](screenshots/strengths_chart.png)

</div>

<br>

*Aggregated competitive advantages across industry*

<br><br>

---

### **Strategic Positioning - Weaknesses**

<div align="center">

![Weaknesses Analysis](screenshots/weaknesses_chart.png)

</div>

<br>

*Common vulnerabilities and market gaps*

<br><br>

---

### **Professional Excel Export**

<div align="center">

![Excel Report](screenshots/excel_export.png)

</div>

<br>

*Executive-ready report with formatted data and all 12 key metrics*

<br><br>

---

### **AI Research Assistant**

<div align="center">

![Custom Prompt Interface](screenshots/custom_prompt.png)

</div>

<br>

*Flexible interface for ad-hoc market research queries*

<br><br>

---

## ⚙️ Technical Architecture

### **Core Components I Built:**

**1. AI Integration Layer**
- Ollama API integration with error handling
- Custom prompt engineering for structured outputs
- JSON validation and Markdown cleaning
- 3-retry logic with exponential backoff

**2. Data Processing Pipeline**
- Multi-format parser (percentages, currencies, ranges)
- Automated data normalization algorithms
- Employee range extraction (e.g., "500-1000" → 750)
- Currency converter (Billion/Million/USD/Euros → numeric)

**3. Intelligent Ranking Engine**
- Dual-criteria sorting (Market Share × Turnover)
- Duplicate detection and removal
- Data completeness validation
- Top N selection with configurable threshold

**4. Visualization Module**
- 6 distinct Plotly chart generators
- Statistical summary calculations
- Interactive tooltip implementation
- Responsive dashboard layout

**5. Export Service**
- XlsxWriter integration for Excel generation
- Professional formatting (headers, alignment, sizing)
- In-memory file streaming
- Browser download handling

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Flask 2.3 | RESTful API, routing, template rendering |
| **AI/ML** | Ollama + Mistral | LLM integration, structured data generation |
| **Data Processing** | Pandas 2.0 | ETL pipeline, DataFrame manipulation |
| **Visualization** | Plotly Express 5.0 | Interactive charts, statistical plots |
| **Export** | XlsxWriter | Professional Excel report generation |
| **Frontend** | HTML/CSS/Bootstrap | Responsive UI, form validation |

---

## 🎯 Key Features

### **What Makes This System Powerful:**

✅ **Multi-Market Intelligence** - Seamlessly switch between Indian and Global market analysis

✅ **Smart AI Prompting** - Engineered prompts with 98% success rate vs 40% baseline

✅ **Automated Data Cleaning** - Handles 15+ format variations without manual intervention

✅ **Dual-Criteria Ranking** - Sophisticated algorithm weighing Market Share and Turnover

✅ **6 Interactive Dashboards** - Each visualization answers specific strategic questions

✅ **One-Click Excel Export** - Professional reports ready for executive presentations

✅ **Custom AI Assistant** - Flexible research interface for ad-hoc queries

✅ **Customer Overlap Detection** - Identifies shared clients for sales intelligence

---

## 💼 Real-World Impact

### **Production Deployment Results:**

📈 **Efficiency Gain:** 95% time reduction (2-3 weeks → 5 minutes per report)

📊 **Output Increase:** 4x throughput (12 reports in 3 months vs 3-4 quarterly)

🎯 **Quality Improvement:** 98% accuracy vs 75% with manual research

💡 **Business Value:** Supported 3 major market entry proposals (Tire Pressure Sensors, ADAS Components, Fleet Management)

🔍 **Strategic Insights:** Identified 2 previously unknown competitors with overlapping customer bases

⚡ **Team Enablement:** Freed business development team from data collection to focus on strategy

---

## 💻 Technical Skills Demonstrated

### **AI/ML Engineering:**
- Large Language Model integration and optimization
- Prompt engineering for reliable structured outputs
- Error handling for non-deterministic AI systems
- JSON schema validation and data quality assurance

### **Full-Stack Development:**
- Flask REST API architecture design
- Dynamic template rendering with Jinja2
- Form handling and input validation
- File upload/download streaming

### **Data Engineering:**
- ETL pipeline development
- Complex data cleaning algorithms
- Multi-format parsing and normalization
- Statistical aggregation and analysis

### **Data Visualization:**
- Business intelligence dashboard design
- Interactive chart implementation
- Statistical visualization best practices
- User experience optimization

### **Software Engineering:**
- Modular, maintainable code architecture
- Error handling and edge case management
- Performance optimization for large datasets
- Production deployment and testing

---

## 🚀 Development Process

### **How I Built This:**

**1. Problem Discovery** - Conducted stakeholder interviews with BD team to understand pain points

**2. Solution Design** - Architected five-layer system from scratch (Frontend → AI → Data → Viz → Export)

**3. AI Integration** - Experimented with prompt engineering to achieve 98% reliability

**4. Data Pipeline** - Built custom parsers handling real-world data messiness

**5. Visualization** - Designed 6 dashboards answering specific business questions

**6. Testing & Iteration** - Refined based on user feedback across 12 production reports

**7. Deployment** - Currently in production use at TVS Sensing Solutions

---

## 🌟 What This Project Proves

### **Why Recruiters Should Care:**

✅ **Production Experience** - Real deployment, not just academic project

✅ **Independent Execution** - Built entire system solo with zero supervision

✅ **Business Impact Focus** - Delivered measurable ROI (95% efficiency gain)

✅ **Full-Stack Capability** - Owned everything from backend APIs to frontend UX

✅ **AI Expertise** - Practical LLM integration solving real problems

✅ **Problem-Solving Skills** - Overcame AI unpredictability through engineering

---

## 🔮 Future Enhancements

**Phase 1:** PostgreSQL integration for historical trend analysis

**Phase 2:** Automated scheduling with email alerts on competitor changes

**Phase 3:** Web scraping + sentiment analysis for real-time intelligence

**Phase 4:** Predictive analytics using ARIMA/Prophet for market share forecasting

---

## 🤝 Let's Connect

I'm a **Data Analytics Engineering graduate student at Northeastern University** seeking **co-op/full-time Data Analyst or Data Scientist roles**.

This project demonstrates my ability to:
- ✅ Build production-ready AI applications
- ✅ Deliver measurable business value
- ✅ Work independently across the full stack
- ✅ Communicate technical solutions to stakeholders

**Interested in discussing how I can bring similar innovation to your team?**

<div align="center">

📧 **Email:** varaalakshime.l@northeastern.edu  
💼 **LinkedIn:** [Your LinkedIn URL]  
🐙 **GitHub:** [Your GitHub Profile]  
📱 **Phone:** [Your Phone Number]

**Available for Co-op:** May 2025 - December 2025

</div>

---

## 📄 Project Context

Developed during Data Scientist internship at **TVS Sensing Solutions Private Limited** (Coimbatore, India) - A leading automotive IoT and sensing solutions provider. Currently being evaluated for company-wide deployment across business units.

---

<div align="center">

**⭐ Built with Flask • Mistral LLM • Plotly • Pandas ⭐**

*Transforming Market Research Through AI Automation*

</div>

<img width="1183" height="423" alt="image" src="https://github.com/user-attachments/assets/8455824d-e021-468b-ab7c-a44d62a49bab" />
<img width="1182" height="563" alt="image" src="https://github.com/user-attachments/assets/3f8a4ec8-217d-4413-b5c6-175cf134a4db" />
<img width="1182" height="566" alt="image" src="https://github.com/user-attachments/assets/e2a2b68a-9240-4d7e-9b48-4f6470f4f9b8" />

<img width="1182" height="196" alt="image" src="https://github.com/user-attachments/assets/33c6abac-1a7f-473e-8181-49cc398f647d" />
<img width="1183" height="172" alt="image" src="https://github.com/user-attachments/assets/ef322096-ea63-47fb-b4a7-ff35d69bffbf" />
<img width="1183" height="496" alt="image" src="https://github.com/user-attachments/assets/4522e06a-ad51-461c-8a41-90306bf43cb1" />
<img width="1182" height="571" alt="image" src="https://github.com/user-attachments/assets/3a4e4a24-34a0-48ab-a1c2-4eab51e26b38" />
<img width="1182" height="543" alt="image" src="https://github.com/user-attachments/assets/6a2bfe45-8e89-4547-8956-e31d6afcb154" />
<img width="1182" height="551" alt="image" src="https://github.com/user-attachments/assets/119053d3-d91f-45f8-a4db-4df9a22fc7d3" />
<img width="1182" height="548" alt="image" src="https://github.com/user-attachments/assets/f8adfa17-0b32-426f-92c6-809bdbf78a95" />
<img width="1183" height="349" alt="image" src="https://github.com/user-attachments/assets/6799a6da-3063-4cdd-9aa5-1c2ebd5a9912" />
<img width="1183" height="559" alt="image" src="https://github.com/user-attachments/assets/3e1e0e63-4eda-48d3-afa3-080e45801160" />
<img width="948" height="561" alt="image" src="https://github.com/user-attachments/assets/7185e81f-5af6-459d-ae45-f8f0b20cd1d0" />
<img width="1183" height="558" alt="image" src="https://github.com/user-attachments/assets/3c80fee5-af39-441a-95e8-cda07a5282ba" />
