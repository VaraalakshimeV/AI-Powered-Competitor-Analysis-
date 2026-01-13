from flask import Flask, render_template, request, send_file,jsonify
import json
import pandas as pd
from pandas import json_normalize
import os
import ollama 
from io import BytesIO
import plotly.express as px

app = Flask(__name__)
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)
# Load dataset
file_path = "competitor_analysis.xlsx"
df = pd.read_excel(file_path)

# Data Processing
df["Years in Business"] = 2024 - df["Established Year"]

def extract_midpoint(emp_range):
    if "-" in str(emp_range):
        low, high = map(int, emp_range.replace(",", "").split("-"))
        return (low + high) // 2
    return int(str(emp_range).replace(",", ""))

df["Approx Employees"] = df["Number of Employees"].apply(extract_midpoint)
df["Market Share (%)"] = df["Market Share"].str.replace("%", "").astype(float)

# Insights
oldest_company = df.loc[df["Years in Business"].idxmax(), "Company Name"]
avg_market_share = df["Market Share (%)"].mean()

# Market Share Bar Chart
fig1 = px.bar(df, x="Company Name", y="Market Share (%)", title="Market Share Comparison")
chart1 = fig1.to_html(full_html=False)

# Employee Count Bar Chart
fig2 = px.bar(df, x="Company Name", y="Approx Employees", title="Employee Count Comparison")
chart2 = fig2.to_html(full_html=False)

# Pie Chart - Market Share Distribution
fig_pie = px.pie(df, names="Company Name", values="Market Share (%)", title="Market Share Distribution")
chart_pie = fig_pie.to_html(full_html=False)

# Scatter Plot - Employees vs. Market Share
fig_scatter = px.scatter(df, x="Approx Employees", y="Market Share (%)", color="Company Name",
                         size="Market Share (%)", title="Employees vs. Market Share")
chart_scatter = fig_scatter.to_html(full_html=False)

# Convert Turnover to numeric (if it's a range or string, handle appropriately)
df["Turnover (Cr)"] = pd.to_numeric(df["Turnover"], errors="coerce")
fig_turnover = px.histogram(df, x="Turnover (Cr)", nbins=10, title="Turnover Distribution")
chart_turnover = fig_turnover.to_html(full_html=False)

# Extract top customers (if available)
if "Customers" in df.columns:
    top_customers = df["Customers"].str.split(',').explode().str.strip().value_counts().head(10)
    fig_customers = px.bar(x=top_customers.index, y=top_customers.values,
                           title="Top Customers", labels={"x": "Customer", "y": "Frequency"})
    chart_customers = fig_customers.to_html(full_html=False)
else:
    chart_customers = ""


# Strengths & Weaknesses Bar Chart (If columns exist)
if "Strengths" in df.columns and "Weaknesses" in df.columns:
    strengths = df["Strengths"].str.split(',').explode().str.strip().value_counts().head(10)
    weaknesses = df["Weaknesses"].str.split(',').explode().str.strip().value_counts().head(10)
    fig_strengths = px.bar(x=strengths.index, y=strengths.values, title="Top Strengths")
    fig_weaknesses = px.bar(x=weaknesses.index, y=weaknesses.values, title="Top Weaknesses")
    chart_strengths = fig_strengths.to_html(full_html=False)
    chart_weaknesses = fig_weaknesses.to_html(full_html=False)
else:
    chart_strengths = chart_weaknesses = ""

def clean_numeric(value):
    """Convert Market Share & Turnover to numeric values for sorting."""
    if isinstance(value, str):
        value = value.replace(",", "")  # Remove commas
        value = value.replace("Billion", "e9").replace("Million", "e6")  # Convert Billion/Million
        value = value.replace("USD", "").replace("Euros", "").replace("%", "").strip()
        try:
            return float(eval(value))  # Convert "3e9" to 3000000000.0
        except:
            return None
    return value  

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get input values from form
        fields_req = request.form.get("fields_req")
        company_name = request.form.get("company_name")
        no_of_companies = int(request.form.get("no_of_companies"))
        other_companies = request.form.get("other_companies")
        inp_mkt = request.form.get("inp_mkt")
        inp_mkt_segment = request.form.get("inp_mkt_segment")
        inp_prd_segment = request.form.get("inp_prd_segment")
        inp_sub_segment = request.form.get("inp_sub_segment")
        inp_technology = request.form.get("inp_technology")


        # Handling "Others" input cases
        if inp_prd_segment == "Others":
            inp_sub_segment = ""
        if inp_sub_segment == "Others":
            inp_sub_segment = request.form.get("inp_sub_segment1")

        prd_input = f"{inp_sub_segment} in {inp_prd_segment}"
        if inp_technology:
            prd_input += f" using {inp_technology} technology"

        inp_mkt1 = "Indian" if inp_mkt == "Indian Market" else "Global"

        o_c = f". Excluding the top {no_of_companies} companies, include these companies as well: {other_companies}" if other_companies else ""

        # **Enhanced Prompt for Better Data Extraction**
        usr_input = (
            f"List the top {no_of_companies * 2} {inp_mkt1} companies manufacturing {prd_input} "
            f"Rank the companies based on **highest Market Share and Turnover**. "
            f"Ensure the output is in **VALID JSON format only** without extra text or explanations. "
            f"Each numerical value (Market Share, Turnover) should be enclosed in double quotes. "
            f"Required fields: Company Name, Headquarters, Established Year, Number of Employees, "
            f"Turnover, Market Share, Market Segment, Products, Customers, Strengths, Weaknesses, Website. "
            f"{o_c}"
        )

        # **Fetch Data using Ollama**
        context = f"I am an industrial expert in the automotive component manufacturing industry. I am doing automotive market research in {inp_mkt}."
        messages = [
            {"role": "user", "content": json.dumps({"context": context, "format": "json"})},
            {"role": "user", "content": usr_input},
        ]

        response = ollama.chat(model="mistral", messages=messages)
        obj = response["message"]["content"]

        # Ensure valid JSON response
        try:
            obj = obj.strip("```json").strip("```").strip()  # Remove Markdown if present
            lis = json.loads(obj)  # Convert JSON string to Python object
        except json.JSONDecodeError:
            print("Error: Response is not valid JSON. Received:", obj)  # Debugging
            return "Error: Received invalid JSON response from the API"

        df = pd.DataFrame(lis)

        df["Market Share"] = df["Market Share"].apply(clean_numeric)
        df["Turnover"] = df["Turnover"].apply(clean_numeric)

        df = df.sort_values(by=["Market Share", "Turnover"], ascending=[False, False])

        df = df.head(no_of_companies)

        # Convert DataFrame to Excel
        excel_data = BytesIO()
        with pd.ExcelWriter(excel_data, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False)
        excel_data.seek(0)

        return send_file(
            excel_data,
            download_name="competitor_analysis.xlsx",
            as_attachment=True,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", tables=df.to_html(classes="table table-striped"),
                           oldest_company=oldest_company, avg_market_share=avg_market_share,
                           chart1=chart1, chart2=chart2, chart_pie=chart_pie, chart_scatter=chart_scatter,
                           chart_turnover=chart_turnover, chart_customers=chart_customers,
                           chart_strengths=chart_strengths, chart_weaknesses=chart_weaknesses)

@app.route("/custom_prompt", methods=["GET", "POST"])
def custom_prompt():
    result = None  # Initialize result as None

    if request.method == "POST":
        user_prompt = request.form.get("user_prompt")  # Get user input
        print("User Input Received:", user_prompt)  

        if not user_prompt:  
            result = "Error: No input received."
        else:
            messages = [{"role": "user", "content": user_prompt}]
            try:
                response = ollama.chat(model="mistral", messages=messages)
                print("Ollama Response:", response)  # Debugging output
                
                if "message" in response:
                    result = response["message"]["content"]
                else:
                    result = "Error: No valid response from API."
            except Exception as e:
                print("Ollama API Error:", e)
                result = "Error processing request."

    # ✅ Ensure `result` is always passed to the template
    return render_template("custom_prompt.html", result=result)




if __name__ == "__main__":
    app.run(debug=True,port=5001)
