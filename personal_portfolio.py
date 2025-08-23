import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Omkar Sutar — Power BI Developer",
    page_icon="📊",
    layout="wide"
)

# ---------- BASIC PROFILE DATA ----------
PROFILE = {
    "name": "Omkar Sutar",
    "tagline": "Power BI Developer | Data Analyst | Microsoft Fabric",
    "location": "Kurla, Mumbai, India",
    "email": "omkarsutar9702@gmail.com",
    "phone": "+91-8169975505",
    "github": "https://github.com/omkarsutar9702",
    "summary": (
        "- 🚀 Results-driven Power BI Developer / Data Analyst with 2.5+ years of experience in:\n"
        "- 📊 Designing enterprise dashboards | ⚡ Building automated data pipelines | ☁️ Implementing Microsoft Fabric solutions\n"
        "- 🛠️ Skilled in Power BI | SQL | Python | M Query | DAX\n"
        "- 📈 Proven track record of automations handling 400k+ rows/month\n"
        "- 🏆 Delivered insights that won awards & improved decision-making\n"
        "- ✨ Turning raw data ➝ smart decisions!\n"
    ),
    "skills": {
        "Business Intelligence": ["Power BI (Reports, Dashboards, KPI Scorecards)", "Power Automate", "SharePoint", "Power Point"],
        "Data Engineering & Analysis": ["Microsoft Fabric", "PySpark", "Medallion Architecture", "Dataflow", "Semantic Model"],
        "Programming": ["SQL", "Pyspark","Python", "M Query", "DAX"],
        "Tools": ["SSMS", "VS Code", "GitHub", "Office 365", "SAP"]
    },
    "experience": [
        {
            "company": "L&T Energy Hydrocarbon",
            "title": "Power BI Developer",
            "period": "Mar 2023 – Present | Mumbai, India",
            "highlights": [
                "Led Microsoft Fabric implementation; designed end-to-end data architecture integrating SQL, SharePoint and other sources.",
                "Built KPI dashboards in Power BI + SQL + Python + Power Automate to automate processing of 400,000+ records/month, reducing manual work by 50%.",
                "Developed Auctions Analytics dashboard: 2,000+ auctions worth ₹3,000 Cr+, covering 1,000+ suppliers; contributed to winning the L&T Icons Award.",
                "Created PO Lifecycle Tracker with Power Query to monitor 4000+ POs; enabled proactive actions on delays from a unified view.",
                "Designed SES Tracker (300k+ rows across multiple tables) with SQL; improved report latency by ~40% and reduced approval cycle time."
            ]
        },
        {
            "company": "TheOther2Thirds Consulting LLP",
            "title": "Data Analyst (Contract)",
            "period": "Oct 2022 – Dec 2022 | Mumbai, India",
            "highlights": [
                "Connected data sources, performed transformations and developed business reports.",
                "Built Excel-based KPI scorecards and visual reports for client BI needs."
            ]
        },
        {
            "company": "Integreon",
            "title": "Excel Expert",
            "period": "Jul 2022 – Oct 2022 | Mumbai, India",
            "highlights": [
                "Automated Excel-based data integration and reporting with advanced formulas and macros."
            ]
        }
    ],
    "projects": [
        {
            "name": "[SharePoint-Utils (Python package)](https://github.com/omkarsutar9702/SharePoint-Utilizes-)",
            "desc": "Fabric-integrated utility to simplify SharePoint file handling and ingestion into Lakehouse, boosting analytics workflow efficiency.",
            "tech": ["Python", "Fabric", "SharePoint", "Lakehouse"]
        },
        {
            "name": "[Text Insights: Sentiment Analysis & Summarization](https://github.com/omkarsutar9702/Text-Insights-Sentiment-Analysis-Summarization)",
            "desc": "Text Insights! This application allows you to analyze the sentiment of a given text and get a concise summary of it. It leverages pre-trained models for sentiment analysis and summarization.",
            "tech": ["Python", "Pandas" , "Streamlit"]
        },
        {
            "name": "[Prompt to Youtube Short](https://github.com/omkarsutar9702/Prompt-to-Youtube-Short)",
            "desc": "This program converts any topic into 1 minute long youtube short.",
            "tech": ["Python", "Pandas" , "Streamlit"]
        },
        {
            "name": "[employee engagement plot and app](https://github.com/omkarsutar9702/employee-engagement-plot-and-app)",
            "desc": "An interactive dashboard to visualize employee engagement metrics over time.",
            "tech": ["Python", "Pandas" , "Streamlit"]
        },


    ],
    "education": [
        {"degree": "M.Sc., S.K Somaiya College, Mumbai", "score": "CGPA: 8.48", "years": "2020 – 2022"},
        {"degree": "B.Sc., G.N Khalsa College, Mumbai", "score": "CGPA: 6.39", "years": "2017 – 2020"}
    ],
    "certs": [
        "Power BI for Data Analysis — ATLNext",
        "Data Visualization with Python — IBM",
        "Time Series Analysis — State University of New York",
        "Basic Six Sigma Statistics — ATLNext",
        "Investment Analysis & Portfolio Management — Finladder",
        "Key Accounting Concepts & Principles — ATLNext"
    ]
}

RESUME_PATHS = [Path('/mnt/data/Resume.pdf'), Path('Resume_Omkar_Sutar.pdf')]

def find_resume():
    for p in RESUME_PATHS:
        if p.exists():
            return p
    return None

# ---------- HEADER ----------
st.markdown(
    f"""
    <div>
      <div>
        <h1 style='text-align: center;'>{PROFILE['name']}</h1>
        <p style='text-align: center; margin-top:4px;font-size:1.05rem;color:#808080'>{PROFILE['tagline']}</p>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- ABOUT ----------
st.subheader("📌 About Me" , divider='rainbow')
st.write(PROFILE["summary"])

st.code("")
# ---------- EXPERIENCE ----------
st.subheader("🧭 Experience", divider='rainbow')
for exp in PROFILE["experience"]:
    with st.expander(f"{exp['title']} — {exp['company']}  |  {exp['period']}", expanded=True):
        for h in exp["highlights"]:
            st.write(f"- {h}")

st.code("")
# ---------- PROJECTS ----------
st.subheader("📦 Projects" , divider='rainbow')
for p in PROFILE["projects"]:
    st.markdown(f"**{p['name']}**  \n{p['desc']}")
    st.caption("Tech: " + ", ".join(p["tech"]))
    st.divider()

# ---------- SKILLS ----------
st.subheader("🛠️ Skills" ,  divider='rainbow')
for k, v in PROFILE["skills"].items():
    st.markdown(f"**{k}:** " + ", ".join(v))

st.code("")
# ---------- EDUCATION ----------
st.subheader("🎓 Education")
for ed in PROFILE["education"]:
    st.write(f"- {ed['degree']} ({ed['years']}) — {ed['score']}")

st.code("")
# ---------- CERTIFICATIONS ----------
st.subheader("📜 Certifications")
for c in PROFILE["certs"]:
    st.write(f"- {c}")
st.code("")
# ---------- CONTACT ----------
st.subheader("✉️ Contact")
st.write("I’m open to opportunities as a **Power BI Developer / Data Analyst** ")
st.write(f"- 📧 Email: {PROFILE['email']}")
st.write(f"- 📍 Location: {PROFILE['location']}")
st.write(f"- 🐙 [GitHub]({PROFILE['github']})")
st.write(f"- 📞 Phone: ({PROFILE['phone']})")

resume = find_resume()
if resume:
    with open(resume, "rb") as f:
        st.download_button("⬇️ Download Resume (PDF)", f, file_name="Resume_Omkar_Sutar.pdf")
else:
    st.info("Resume file not found. Place Resume.pdf alongside this app to enable download.")

st.success("✅ Thanks for visiting! Feel free to reach out.")
