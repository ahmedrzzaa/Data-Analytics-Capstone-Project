import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns


# URL of Dataset
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"

# Set page configuration
st.set_page_config(page_title="Developer Trends", layout="wide")

# Loading Dataset
st.spinner(text='Loading the dataset...')
@st.cache_data
def load_data():
    try:
        return pd.read_csv(url)
    except FileNotFoundError:
        st.error("Dataset not found.")
        return pd.DataFrame()

data = load_data()

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.title("Navigation")

    # Adding some styling to the sidebar
    st.sidebar.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f2f5;
    }
    </style>
    """, unsafe_allow_html=True)

    # Using radio buttons for navigation with icons
    section = st.sidebar.radio("Go to", [ "📖 Introduction", "🛠️ Methodology", "📊 Results",
        "📈 Programming Language Trends", "💾 Database Trends", "📊 Dashboard", "🔮 Future Technology Trend",
        "👥 Demographics", "🏠 Executive Summary","📝 Concluding Remarks", "🔚 Conclusion"])

    # Adding a link to GitHub
    st.sidebar.markdown("[View Source code on GitHub](https://github.com/ahmedrzzaa/Data-Analytics-Capstone-Project.git)")

    return section

# Sections
def executive_summary():
    st.title("Executive Summary")
    st.title("Programming Languages and Technologies in Demand")

# Adding a section for programming languages
    st.header("Top Programming Languages in Demand")
    programming_languages = ["JavaScript", "HTML/CSS", "SQL", "Bash/Shell/PowerShell", "Python"]
    st.markdown("• " + "\n• ".join(programming_languages))

# Adding a section for database skills
    st.header("Top Database Skills in Demand")
    database_skills = ["MySQL", "Microsoft SQL Server", "PostgreSQL", "SQLite", "MongoDB"]
    st.markdown("• " + "\n• ".join(database_skills))

# Adding a section for popular platforms
    st.header("Popular Platforms")
    popular_platforms = ["Windows", "Linux", "Docker", "AWS", "Slack"]
    st.markdown("• " + "\n• ".join(popular_platforms))

# Adding a section for popular web frameworks
    st.header("Popular Web Frameworks")
    web_frameworks = ["jQuery", "Angular/Angular.js", "React.js", "ASP.NET", "Express"]
    st.markdown("• " + "\n• ".join(web_frameworks))

# Adding a section for future technology trends
    st.header("Future Technology Trends")
    future_trends = ["Python takes the third row, followed by SQL and TypeScript",
    "Redis and Elasticsearch also place in Top 5", "Android is in the Top 5 demanded platforms, the rest remains",
    "React.js takes the first row and Vue.js is the latest addition as the last"]
    st.markdown("• " + "\n• ".join(future_trends))


def introduction():
    st.title("Introduction")


    st.markdown("""
    In the realm of programming and technology, several key trends have emerged in recent years. 
    These insights shed light on the evolving landscape of programming languages, web frameworks, and the demographics of professional developers.

    **Key Highlights:**
    - **Inclusive Survey**: Stack Overflow conducts an inclusive survey of individuals engaged in coding globally.
    - **Wide Array of Topics**: The survey covers a wide array of topics from preferred technologies to career aspirations.
    - **9th Consecutive Year**: 2019 marks the 9th consecutive year of survey publication.
    - **High Participation**: Nearly **90,000 developers** participated in the 20-minute survey in 2019.

    Let's explore some of the notable findings!
    """)

def methodology():
    st.title("Methodology")

    # Introduction
    st.markdown("""
    The data presented in this analysis is based on a survey conducted by **Stack Overflow** from **January 23 to February 14**, involving **88,883 software developers** from **179 countries**.
    """)


    st.header("Key Steps in the Methodology")
    st.markdown("""
    - **Familiarization with the Dataset**: 
        - Completed IBM labs on Coursera, covering topics such as:
            - Web Scraping
            - Dataset Exploration
            - Data Wrangling
            - Exploratory Data Analysis
            - Data Visualization

    - **Data Analysis and Visualization**: 
        - Conducted using **Python** and its powerful libraries.
    """)


def results():
    st.title("Results")

    st.markdown("""
    Here are some key findings from the survey:

    - **Python** has overtaken Java, becoming the **5th most preferred language** with significant growth. It stands as the **fastest-growing major programming language**.
    - **JavaScript** remains the **most used programming language**.
    - **jQuery** is the most widely used among web frameworks, with **React.js** surpassing **Angular** in developer usage this year.
    - Globally, **men represent approximately 90%** of respondents, with higher female representation among students than professional developers in regions like the **US**, **India**, and the **UK**.
    - Around **3/4 of professional developers** globally hold at least a **bachelor's degree**, aligning with past findings.
    - **3/4 of survey respondents** in professional developer roles are under **35 years old**.
    """)


# Visualization Functions

def language_trends(df_filtered):
    st.title("Programming Language Trends")

    # Extracting current and future languages
    current_languages = df_filtered['LanguageWorkedWith'].dropna().str.split(';').explode()
    future_languages = df_filtered['LanguageDesireNextYear'].dropna().str.split(';').explode()

    # Top 10 languages currently used
    top_current_languages = current_languages.value_counts().head(10).reset_index()
    top_current_languages.columns = ['Language', 'Usage']

    # Top 10 desired languages
    top_future_languages = future_languages.value_counts().head(10).reset_index()
    top_future_languages.columns = ['Language', 'Usage']

    # Creating a bar chart for Top 10 Languages Currently Used
    fig1 = px.bar(top_current_languages, x='Language', y='Usage', title="Top 10 Languages Currently Used", color='Usage',
                  color_continuous_scale=px.colors.sequential.Viridis)
    fig1.update_yaxes(range=[0, 8000])  # Set y-axis range from 0 to 8000
    st.plotly_chart(fig1)

    # Creating a bar chart for Top 10 Desired Languages
    fig2 = px.bar(top_future_languages, x='Language', y='Usage', title="Top 10 Desired Languages", color='Usage',
                  color_continuous_scale=px.colors.sequential.Plasma)
    fig2.update_yaxes(range=[0, 8000])  # Set y-axis range from 0 to 8000
    st.plotly_chart(fig2)

def findings_and_implications():
    st.title("Findings and Implications")

    # Creating two columns for side-by-side layout
    col1, col2 = st.columns(2)

    with col1:
        st.header("Findings")
        st.markdown("""
        - **JavaScript** and **HTML/CSS** emerge as the most used programming languages among all respondents.
        - **SQL** also maintains a significant presence.
        - **Python** just edged out **Java** in overall ranking.
        - The dominance of JavaScript and HTML/CSS underscores their indispensability in modern web development, highlighting the importance of mastering them for developers.
        - The high usage of SQL emphasizes the critical role of data management and querying in modern software applications, across both web and non-web environments.
        - The rise of Python might also reflect its versatility and ease of use, attracting developers across various domains from data science to software development.
        """)


    with col2:
        st.header("Implications")
        st.markdown("""
        - Developers should prioritize mastering **JavaScript** and **HTML/CSS** to remain competitive in the job market.
        - Understanding **SQL** is essential for anyone involved in data management, as it is a critical skill across various applications.
        - The growing popularity of **Python** suggests that learning this language can open up opportunities in diverse fields, including data science, machine learning, and web development.
        - Organizations should consider investing in training programs for their developers to enhance skills in these key areas, ensuring they stay relevant in a rapidly evolving tech landscape.
        - As the demand for web applications continues to rise, proficiency in modern web technologies will be crucial for developers aiming to create effective and efficient solutions.
        """)


def database_trends(df_filtered):
    st.title("Database Trends")

    # Bar chart for top 10 databases currently used
    current_databases = df_filtered['DatabaseWorkedWith'].dropna().str.split(';').explode()
    top_current_databases = current_databases.value_counts().head(10).reset_index()
    top_current_databases.columns = ['Database', 'Usage']

    fig_current_db = px.bar(top_current_databases, x='Database', y='Usage', title="Top 10 Databases Currently Used", color='Usage',
                            color_continuous_scale=px.colors.sequential.Viridis)
    fig_current_db.update_yaxes(range=[0, 8000])  # Set y-axis range from 0 to 8000
    st.plotly_chart(fig_current_db)

    # Bar chart for top 10 desired databases
    future_databases = df_filtered['DatabaseDesireNextYear'].dropna().str.split(';').explode()
    top_future_databases = future_databases.value_counts().head(10).reset_index()
    top_future_databases.columns = ['Database', 'Usage']

    fig_future_db = px.bar(top_future_databases, x='Database', y='Usage', title="Top 10 Desired Databases", color='Usage',
                            color_continuous_scale=px.colors.sequential.Plasma)
    fig_future_db.update_yaxes(range=[0, 8000])  # Set y-axis range from 0 to 8000
    st.plotly_chart(fig_future_db)


def database_findings_and_implications():
    st.title("Database Findings and Implications")

    # Creating two columns for side-by-side layout
    col1, col2 = st.columns(2)


    with col1:
        st.header("Findings")
        st.markdown("""
        - **MySQL** remains the most widely used database management system (DBMS), indicating its strong foothold in the industry.
        - **PostgreSQL** and **Microsoft SQL Server** are also highly favored, showcasing the continued reliance on relational databases for structured data management.
        - **MongoDB** has established itself as the leading NoSQL database, reflecting a shift towards flexible data models that accommodate unstructured data.
        - The presence of **Redis** and **Elasticsearch** highlights the growing importance of in-memory data stores and search engines in modern applications.
        - The future trends indicate a potential rise in the usage of **PostgreSQL** and **MongoDB**, suggesting that developers are increasingly recognizing the value of these databases for both relational and NoSQL needs.
        - The diverse range of databases utilized by developers emphasizes the necessity of selecting the right tool based on specific project requirements, including data structure, scalability, and performance.
        """)


    with col2:
        st.header("Implications")
        st.markdown("""
        - Organizations should invest in training and resources for **MySQL**, **PostgreSQL**, and **Microsoft SQL Server** to maximize the benefits of relational databases in their operations.
        - The growing popularity of **MongoDB** indicates that developers should enhance their skills in NoSQL databases to effectively handle modern data challenges.
        - It is crucial for developers to evaluate project requirements carefully, including data structure and scalability, to select the most appropriate database system for their applications.
        - As data complexity increases, understanding the distinctions between relational and NoSQL databases will be vital for effective data management and application performance.
        - Companies should adopt a hybrid database strategy, leveraging both relational and NoSQL databases to create a robust data architecture that meets diverse application needs and enhances overall performance.
        """)


def dashboard(data):
    st.title("Dashboard")

    # Checking if the required columns are in the dataset
    if 'LanguageWorkedWith' in data.columns and 'DatabaseWorkedWith' in data.columns and 'DatabaseDesireNextYear' in data.columns and 'PlatformWorkedWith' in data.columns and 'WebFrameWorkedWith' in data.columns:
        # Creating a 2x2 grid layout
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        # 1st Graph: Top 10 Languages Worked With (Bar Chart)
        current_languages = data['LanguageWorkedWith'].dropna().str.split(';').explode()
        top_languages = current_languages.value_counts().head(10)
        with col1:
            fig1 = plt.figure()
            sns.barplot(y=top_languages.index, x=top_languages.values)
            plt.title("Top 10 Languages Worked With")
            plt.xlabel("Count")
            plt.ylabel("Languages")
            st.pyplot(fig1)

        # 2nd Graph: Top 10 Databases Worked With (Bar Chart)
        top_current_databases = data['DatabaseWorkedWith'].dropna().str.split(';').explode().value_counts().head(10)
        with col2:
            fig2 = plt.figure()
            sns.barplot(x=top_current_databases.values, y=top_current_databases.index)
            plt.title("Top 10 Databases Worked With")
            plt.xlabel("Count")
            plt.ylabel("Databases")
            st.pyplot(fig2)

        # 3rd Graph: Platforms Worked With (Word Cloud)
        platforms = data['PlatformWorkedWith'].dropna().str.split(';').explode()
        wordcloud = WordCloud(width=800, height=400).generate(' '.join(platforms))
        with col3:
            fig3 = plt.figure(figsize=(8, 4))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.title("Platforms Worked With")
            st.pyplot(fig3)

        # 4th Graph: Top 10 Web Frameworks Worked With (Bubble Chart)
        top_web_frameworks = data['WebFrameWorkedWith'].dropna().str.split(';').explode().value_counts().head(10)
        bubble_data = pd.DataFrame({
            'Framework': top_web_frameworks.index,
            'Count': top_web_frameworks.values,
            'Size': top_web_frameworks.values  # Size can be based on count
        })
        with col4:
            fig4 = plt.figure()
            plt.scatter(bubble_data['Framework'], bubble_data['Count'], s=bubble_data['Size'] * 10, alpha=0.5)
            plt.title("Top 10 Web Frameworks Worked With")
            plt.xlabel("Web Frameworks")
            plt.ylabel("Count")
            plt.xticks(rotation=45)
            st.pyplot(fig4)

    else:
        st.error("Required columns 'LanguageWorkedWith', 'DatabaseWorkedWith', 'DatabaseDesireNextYear', 'PlatformWorkedWith', or 'WebFrameWorkedWith' not found in the dataset.")


def future_technology_trends(data):
    st.title("Future Technology Trends")

    # Checking if the required columns are in the dataset
    if 'LanguageDesireNextYear' in data.columns and 'DatabaseDesireNextYear' in data.columns and 'PlatformDesireNextYear' in data.columns and 'WebFrameDesireNextYear' in data.columns:
        # Creating a 2x2 grid layout
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        # 1st Graph: Top 10 Desired Languages (Bar Chart)
        desired_languages = data['LanguageDesireNextYear'].dropna().str.split(';').explode()
        top_desired_languages = desired_languages.value_counts().head(10)
        with col1:
            fig1 = plt.figure()
            sns.barplot(y=top_desired_languages.index, x=top_desired_languages.values)
            plt.title("Top 10 Desired Languages")
            plt.xlabel("Count")
            plt.ylabel("Languages")
            st.pyplot(fig1)

        # 2nd Graph: Top 10 Desired Databases (Bar Chart)
        desired_databases = data['DatabaseDesireNextYear'].dropna().str.split(';').explode()
        top_desired_databases = desired_databases.value_counts().head(10)
        with col2:
            fig2 = plt.figure()
            sns.barplot(x=top_desired_databases.values, y=top_desired_databases.index)
            plt.title("Top 10 Desired Databases")
            plt.xlabel("Count")
            plt.ylabel("Databases")
            st.pyplot(fig2)

        # 3rd Graph: Platforms Desired (Word Cloud)
        desired_platforms = data['PlatformDesireNextYear'].dropna().str.split(';').explode()
        wordcloud = WordCloud(width=800, height=400).generate(' '.join(desired_platforms))
        with col3:
            fig3 = plt.figure(figsize=(8, 4))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.title("Desired Platforms")
            st.pyplot(fig3)

        # 4th Graph: Top 10 Desired Web Frameworks (Bubble Chart)
        desired_web_frameworks = data['WebFrameDesireNextYear'].dropna().str.split(';').explode()
        top_desired_web_frameworks = desired_web_frameworks.value_counts().head(10)
        bubble_data = pd.DataFrame(
            {'Framework': top_desired_web_frameworks.index, 'Count': top_desired_web_frameworks.values,
                'Size': top_desired_web_frameworks.values  # Size can be based on count
            })
        with col4:
            fig4 = plt.figure()
            plt.scatter(bubble_data['Framework'], bubble_data['Count'], s=bubble_data['Size'] * 10, alpha=0.5)
            plt.title("Top 10 Desired Web Frameworks")
            plt.xlabel("Web Frameworks")
            plt.ylabel("Count")
            plt.xticks(rotation=45)
            st.pyplot(fig4)

    else:
        st.error("Required columns 'LanguageDesireNextYear', 'DatabaseDesireNextYear', 'PlatformDesireNextYear', or 'WebFrameworkDesireNextYear' not found in the dataset.")

def demographics(data):
    st.title("Demographics")

    # 1st Graph: Gender Breakdown (Pie Chart)
    if 'Gender' in data.columns:
        gender_count = data['Gender'].value_counts()
        fig1 = px.pie(names=gender_count.index, values=gender_count.values, title="Gender Breakdown")
        st.plotly_chart(fig1)

    # 2nd Graph: Respondent Count by Country (Choropleth Map)
    if 'Country' in data.columns:
        country_count = data['Country'].value_counts()
        fig2 = px.choropleth(locationmode="country names", locations=country_count.index,
                              color=country_count.values, title="Respondent Count by Country",
                              color_continuous_scale=px.colors.sequential.Plasma)
        st.plotly_chart(fig2)

    # 3rd Graph: Respondent Count by Age (Line Plot)
    if 'Age' in data.columns:
        age_count = data['Age'].value_counts().sort_index()  # Count respondents by age
        fig3 = px.line(x=age_count.index, y=age_count.values, title="Respondent Count by Age",
                        labels={'x': 'Age', 'y': 'Count'})
        st.plotly_chart(fig3)

    # 4th Graph: Respondent Count by Education Level (Bar Chart)
    if 'EdLevel' in data.columns:
        combined_count = data.groupby(['Gender', 'EdLevel']).size().reset_index(name='Count')
        fig4 = px.bar(combined_count, x='EdLevel', y='Count', color='Gender',
                      title="Respondent Count by Gender and Education Level", barmode='group')

        # Updating layout for better readability
        fig4.update_layout(xaxis_title="Education Level", yaxis_title="Count", xaxis_tickangle=-45,
            # Rotate x-axis labels
            height=600,  # Increase height for better spacing
            font=dict(size=12),  # Increase font size
            legend_title_text='Gender',  # Legend title
            hovermode="x unified"  # Unified hover mode
        )
        st.plotly_chart(fig4)





def concluding_remarks():
    st.title("Concluding Remarks")

    st.markdown("""
    ### Key Insights

    - **Technology Trends**: 
      The dominance of JavaScript and HTML/CSS emphasizes the necessity for developers to stay updated with the latest trends in web development. These technologies are foundational for creating dynamic and interactive web applications.

    - **Data Management**: 
      The prevalence of MySQL, PostgreSQL, and Microsoft SQL Server highlights the critical importance of effective data management in software development. Choosing the right database system is essential for ensuring data integrity and accessibility.

    - **Diversity of Tools**: 
      The wide array of programming languages and database systems utilized by developers underscores the importance of understanding the strengths and weaknesses of different tools. This knowledge enables developers to select the most appropriate technologies for their specific projects.

    - **Web Dominance**: 
      The widespread usage of JavaScript and HTML/CSS indicates the dominance of web development within the programming ecosystem. This trend reflects the growing importance of online platforms and digital experiences in today’s technology landscape.

    - **Database Diversity**: 
      The variety of database management systems in use highlights the need for flexibility and adaptability in data storage solutions. Organizations must consider factors such as data structure, scalability, and performance when selecting a database system to meet their needs.

    - **Industry Standardization**: 
      The popularity of certain technologies, such as JavaScript and MySQL, suggests a degree of industry standardization. These tools have become widely adopted due to their proven reliability and effectiveness, simplifying collaboration and interoperability within the developer community.
    """)



def conclusion():
    st.title("Conclusion")

    st.markdown("""
    ### Key Takeaways

    - The findings underscore the dynamic nature of the programming landscape and the critical role of technology in driving innovation across industries.

    - As developers navigate this ever-changing terrain, it is essential to have:
        - A keen understanding of diverse programming languages.
        - Proficiency in various database systems to meet the demands of modern applications.
        - The ability to ensure optimal outcomes in software development projects.
    """)


# Main App
if __name__ == '__main__':
    section = sidebar_navigation()

    if section == "🏠 Executive Summary":
        executive_summary()
    elif section == "📖 Introduction":
        introduction()
    elif section == "🛠️ Methodology":
        methodology()
    elif section == "📊 Results":
        results()
    elif section == "📈 Programming Language Trends":
        language_trends(data)
        findings_and_implications()
    elif section == "💾 Database Trends":
        database_trends(data)
        database_findings_and_implications()
    elif section == "📊 Dashboard":
        dashboard(data)
    elif section == "🔮 Future Technology Trend":
        future_technology_trends(data)
    elif section == "👥 Demographics":
        demographics(data)
    elif section == "📝 Concluding Remarks":
        concluding_remarks()
    elif section == "🔚 Conclusion":
        conclusion()
