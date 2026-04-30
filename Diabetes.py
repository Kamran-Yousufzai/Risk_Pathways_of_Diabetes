import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px 
import seaborn as sns
import io 

# Function to summarize dataset
def about_df(df):
    df_simple = df.head(10)
    shape = df.shape
    
    buffer = io.StringIO()
    df.info(buf=buffer)
    info = buffer.getvalue()

    dtype = df.dtypes
    null_value = df.isnull().sum()
    duplicate_value = df.duplicated().sum()
    stat = df.describe(include='all')

    return df_simple, shape, info, dtype, null_value, duplicate_value, stat
 
 # second fucntion foa a Statistics
def Statistics(df):
    average_Age = df.iloc[:, 0].mean()
    average_Bmi = df.iloc[:, 1].mean()
    average_chol = df.iloc[:, 2].mean()
    average_fast = df.iloc[:, 3].mean()
    average_post = df.iloc[:, 4].mean()
    average_Hba1c = df.iloc[:, 5].mean()
    average_Heart = df.iloc[:, 6].mean()
    average_Glucose = df.iloc[:, 7].mean()
    average_Vitamin = df.iloc[:, 8].mean()
    average_Protein = df.iloc[:, 9].mean()

    statistics = {
        "Average Age": average_Age,
        "Average BMI": average_Bmi,
        "Average Glucose_Level": average_chol,
        "Average Blood_Pressure": average_fast,
        "Average Insulin": average_post,
        "Average Cholesterol_Level": average_Hba1c,
        "Average Skin_Thickness": average_Heart,
        "Average Pregnancies": average_Glucose,
        "Average Physical_Activity": average_Vitamin,
        "Average SleepHours": average_Protein   
    }
    return statistics

# Third Function Display Charts
def Ages_Distribution(df):
    bins = [20, 40, 60, 80]   
    labels = ['21-40', '41-60', '61-80']
    
    # Group ages into bins
    Count = df.groupby(pd.cut(df['Age'], bins=bins, labels=labels, right=False)).size()
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10,5))
    
    # Barplot
    sns.barplot(
        x=Count.index,
        y=Count.values,
        color='#1f76b5',
        edgecolor="black",
        ax=ax
    )
    # Add labels on bars
    for container in ax.containers:
        ax.bar_label(container)
    
    # Titles and formatting
    ax.set_title('Age Distribution')
    ax.set_xlabel('Age Group')
    ax.set_ylabel('Count')
    return fig

# second chart============
def Diabetes_Distribution(df):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10,5))
    
    # Violin plot
    sns.violinplot(
        x='Diabetes_Status',
        y='Blood_Pressure',
        data=df,
        hue='Diabetes_Status',
        ax=ax
    )
    # Titles and labels
    ax.set_title('Distribution of Blood_Pressure by Diabetes Status')
    ax.set_xlabel('Diabetes Status')
    ax.set_ylabel('Blood_Pressure')
    return fig

# Third Chart=================================
def Smoking_Distribution(df):
    # Value counts
    count = df['Diabetes_Status'].value_counts()
    
    # Create subplots
    fig, axes = plt.subplots(1, 1, figsize=(3,3))
    
    # axes is a single Axes object when nrows=1, ncols=1
    axes.pie(
        count,
        labels=count.index,
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops={'edgecolor': 'white'}
    )
    axes.set_title('Diabetes Patients')
    
    # Legend
    axes.legend()
    return fig

# Fourth chart Biaraite===============================
def Gender_Distribution(df):
    # Grouped counts
    count = df.groupby(['Gender','Diabetes_Status']).size().unstack(fill_value=0)
    counts = df.groupby(['Family_History','Diabetes_Status']).size().unstack(fill_value=0)
    
    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(10,5)) 
    
    # Bar plots
    num = count.plot(kind="bar", ax=axes[0])
    nums = counts.plot(kind="bar", ax=axes[1])
    
    # Add labels inside bars
    for container in num.containers:
        num.bar_label(container, label_type='center')
    for container in nums.containers:
        nums.bar_label(container, label_type='center')
    
    # Titles and formatting
    axes[0].tick_params(axis='x', rotation=0)
    axes[0].set_title('Gender Count by Diabetes')
    
    axes[1].tick_params(axis='x', rotation=0)
    axes[1].set_title('Family_History Count by Diabetes')
    
    plt.tight_layout()
    return fig
 
# Fivth Chart==================================================================
def age_Distribution(df):
    # Define age bins and labels
    bins = [20, 40, 60, 80]
    labels = ['21-40', '41-60', '61-80']

    # Create AgeGroup column
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    # Group data
    count = df.groupby(['AgeGroup', 'Diabetes_Status']).size().unstack(fill_value=0)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot stacked bar chart
    count.plot(kind="bar", stacked=True, ax=ax)

    # Add labels
    for container in ax.containers:
        ax.bar_label(container, label_type="center")

    # Formatting
    ax.set_title('Age Count by Diabetes')
    ax.tick_params(axis='x', rotation=0)
    plt.tight_layout()

    return fig

# Sixth chart =========================================================
def smoking_Distribution(df):
    # Grouping data
    count = df.groupby(['Smoking_Status', 'Diabetes_Status']).size().unstack(fill_value=0)
    counts = df.groupby(['Diet_Type', 'Diabetes_Status']).size().unstack(fill_value=0)

    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plot Smoking_Status
    num = count.plot(kind="bar", ax=axes[0])
    for x in num.containers:
        num.bar_label(x, label_type="center")
    axes[0].set_title('Smoking_Status Count by Diabetes')
    axes[0].tick_params(axis='x', rotation=0)

    # Plot Physical_Activity
    nums = counts.plot(kind="bar", ax=axes[1])
    for y in nums.containers:
        nums.bar_label(y, label_type="center")
    axes[1].set_title('Diet_Type Count by Diabetes')
    axes[1].tick_params(axis='x', rotation=0)

    # Layout adjustment
    plt.tight_layout()
    return fig

# Seventh Chart====================================================================
def Heart_Distribution(df):
    # Define heart rate bins and labels
    bins = [60, 80, 100, 130]
    labels = ['60-80', '81-100', '101-130']

    # Create Heart_rate group column
    df['blood_Pressure'] = pd.cut(df['Blood_Pressure'], bins=bins, labels=labels, right=False)

    # Group data
    count = df.groupby(['blood_Pressure', 'Diabetes_Status']).size().unstack(fill_value=0)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot stacked bar chart
    count.plot(kind="bar", stacked=True, ax=ax)

    # Add labels
    for container in ax.containers:
        ax.bar_label(container, label_type="center")

    # Formatting
    ax.set_title('Blood_Pressure Count by Diabetes')
    ax.tick_params(axis='x', rotation=0)
    plt.tight_layout()

    return fig

#  Eight Chart=====================================================================
def Bmi_Distribution(df):
    bins = [20,25,30,40]
    labels = ['20-25','26-30','31-40']
    df['BMi'] = pd.cut(df['BMI'], bins=bins, labels=labels, right=False)

    # Group data
    count = df.groupby(['BMi', 'Diabetes_Status']).size().unstack(fill_value=0)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot stacked bar chart
    count.plot(kind="bar", stacked=True, ax=ax)

    # Add labels
    for container in ax.containers:
        ax.bar_label(container, label_type="center")

    # Formatting
    ax.set_title('BMi Count by Diabetes')
    ax.tick_params(axis='x', rotation=0)
    plt.tight_layout()

    return fig
# Ninght Chart=============================================================
def Pregnancies_Distribution(df):
    count = df.groupby(['Pregnancies', 'Diabetes_Status']).size().unstack(fill_value=0)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot stacked bar chart
    count.plot(kind="barh", stacked=True, ax=ax)

    # Add labels
    for container in ax.containers:
        ax.bar_label(container, label_type="center")

    # Formatting
    ax.set_title('Pregnancies Count by Diabetes')
    ax.tick_params(axis='x', rotation=0)
    plt.tight_layout()

    return fig

# Thewel Chart=====================================================
def line_plots(df):
    # Create figure with multiple subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plot Heart Rate vs Age
    sns.lineplot(data=df,x='Age', y='Insulin',hue="Diabetes_Status"
                 , ax=axes[0])
    axes[0].set_title("Age vs Insulin")

    # Plot BMI vs Age
    sns.lineplot(data=df,x='Age', y='BMI',hue="Diabetes_Status"
                 , ax=axes[1])
    axes[1].set_title("BMI vs Age")

    # Layout adjustment
    plt.tight_layout()
    return fig

# Thirteen Chart=======================================================
def scatter_plots(df):
    # Create a figure with 4 subplots
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Scatterplot: Cholesterol vs BMI
    sns.scatterplot(data=df,x='Cholesterol_Level',y='Physical_Activity',hue="Diabetes_Status"
                    , ax=axes[0])
    axes[0].set_title("Cholesterol vs BMI")

    # Scatterplot: Fasting Blood Sugar vs Cholesterol
    sns.scatterplot(data=df,x='BMI', y='Cholesterol_Level',hue="Diabetes_Status"
                    , ax=axes[1])
    axes[1].set_title("BMI vs Cholesterol")

    plt.tight_layout()
    return fig


#Chart plot===================================================
def plot_distributions(df):
    fig = plt.figure(figsize=(15, 20))

    variables = [
        'Age', 'BMI', 'Glucose', 'Blood_Pressure',
        'Insulin', 'Cholesterol_Level', 'Skin_Thickness', 'Pregnancies'
    ]

    for num, var in enumerate(variables, start=1):
        ax = fig.add_subplot(4, 2, num)
        sns.histplot(df[var], kde=True, color='red', ax=ax)
        ax.set_title(f'Distribution of {var}', fontsize=12)
        ax.set_xlabel(var)
        ax.set_ylabel('Count')

    plt.tight_layout()
    return fig

# Outlier Chart======================================================
def plot_boxplots(df):
    fig = plt.figure(figsize=(15, 20))

    variables = [
        'Age', 'BMI', 'Glucose', 'Blood_Pressure',
        'Insulin', 'Cholesterol_Level', 'Skin_Thickness', 'Pregnancies'
    ]

    for num, var in enumerate(variables, start=1):
        ax = fig.add_subplot(4, 2, num)
        sns.boxplot(x=df[var], color='red', ax=ax)
        ax.set_title(f'Boxplot of {var}', fontsize=12)
        ax.set_xlabel(var)

    plt.tight_layout()
    return fig

# Heatmap plot==================================================
def plot_heatmap(df):
    fig, ax = plt.subplots(figsize=(10, 5))

    # Select only numerical columns
    numerical_df = df.select_dtypes(include='number')

    # Correlation matrix
    corr = numerical_df.corr()

    sns.heatmap(
        corr,
        annot=True,           # Show correlation values
        fmt='.2f',            # 2 decimal places
        cmap='coolwarm',      # Color scheme
        linewidths=0.5,       # Grid lines
        linecolor='white',
        square=True,          # Square cells
        ax=ax
    )

    ax.set_title('Correlation Heatmap', fontsize=16)
    plt.tight_layout()
    return fig

# Dynamic plots

def dashboard(df2, selected_status):        
    # Two columns for charts
    col1, col2 = st.columns(2)

    # Stacked bar chart (Gender vs Diabetes)
    with col1:
        count = df2.groupby(['Gender','Diabetes_Status']).size().unstack(fill_value=0)
        count = count.reset_index()

        count_melted = count.melt(
            id_vars="Gender", 
            value_vars=count.columns[1:], 
            var_name="Diabetes_Status", 
            value_name="Count"
        )

        fig = px.bar(
            count_melted,
            x="Gender",
            y="Count",
            color="Diabetes_Status",
            barmode="stack",
            text="Count",
            title="Gender vs Diabetes Status",
            color_discrete_map={"Yes": "#ff7e0e", "No": "#ffcb2e"}
        )
        fig.update_traces(textposition="inside")
        st.plotly_chart(fig, use_container_width=True)

    # Pie chart (distribution of Yes vs No)
    with col2:
        pie_data = df2['Diabetes_Status'].value_counts().reset_index()
        pie_data.columns = ["Diabetes_Status", "Count"]

        fig = px.pie(
            pie_data,
            values="Count",
            names="Diabetes_Status",
            hole=0.5,
            title="Distribution of Diabetes Status (Yes vs No)",
            color="Diabetes_Status",
            color_discrete_map={"Yes": "#ff7e0e", "No": "#ffcb2e"}
        )
        fig.update_traces(textinfo="percent+label")
        st.plotly_chart(fig, use_container_width=True)

    # ── Scatter Plot ──────────────────────────────────────────────
       

    # Scatter plot (Age vs Insulin)
         

    st.subheader('Age Trends by Diabetes Status')
    fig = px.scatter(
    df2.groupby(["Age", "Diabetes_Status"]).size().reset_index(name="Count"),
    x="Age",
    y="Count",                                       
    color="Diabetes_Status",        
    color_discrete_map={"Yes": "#ff7e0e", "No": "#ffcb2e"},
    opacity=0.7,
    size="Count",                                    
    size_max=15,
    hover_data=["Age", "Diabetes_Status"]             
)
    fig.update_traces(marker=dict(line=dict(width=0.5, color='white')))
    fig.update_layout(
    xaxis_title="Age",                                
    yaxis_title="Count",                              
    legend_title="Diabetes Status"
)
    st.plotly_chart(fig, use_container_width=True)


    fig = px.scatter(
        df2,
        x="Glucose",
        y="BMI",
        color="Diabetes_Status",
        title="Glucose vs BMI by Diabetes Status",
        color_discrete_map={"Yes": "#ff7e0e", "No": "#ffcb2e"},
        opacity=0.7,
        size_max=15,
        hover_data=["Glucose", "BMI"]        # Show on hover
    )
    fig.update_traces(marker=dict(line=dict(width=0.5, color='white')))
    fig.update_layout(
        xaxis_title="Glucose Level",
        yaxis_title="BMI",
        legend_title="Diabetes Status"
    )
    st.plotly_chart(fig, use_container_width=True)


    st.markdown("### Pregnancies by Diabetes_Status")
    count = df2.groupby(['Pregnancies','Diabetes_Status']).size().unstack(fill_value=0)
    count = count.reset_index()

# Melt for Plotly Express
    count_melted = count.melt(
      id_vars="Pregnancies",   # fixed: removed trailing space
      value_vars=count.columns[1:], 
      var_name="Diabetes_Status", 
      value_name="Count"
)

# Horizontal bar chart
    fig = px.bar(
      count_melted,
      y="Pregnancies",   # category on y-axis
      x="Count",                 # values on x-axis
      color="Diabetes_Status",
      orientation="h",           # horizontal bars
      text="Count",
      color_discrete_map={"Yes": "#ff7e0e", "No": "#ffcb2e"}
)
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)


# Select numeric columns + Diabetes_Status
    st.markdown("### Count All Numeric Variables by Diabetes_Status")

    # Select numeric columns + Diabetes_Status
    numeric_cols = df2.select_dtypes(include="number").columns.tolist()
    df_numeric = df2[numeric_cols + ["Diabetes_Status"]]

    # Melt so each numeric variable is stacked
    df_melted = df_numeric.melt(
        id_vars="Diabetes_Status",
        var_name="Variable",
        value_name="Value"
    )

    # Group by Variable and Diabetes_Status → count
    summary = (
        df_melted.groupby(["Variable", "Diabetes_Status"])["Value"]
        .mean()
        .reset_index()
        .rename(columns={"Value": "Count"})   
    )
    # Bar plot
    fig = px.bar(
        summary,
        x="Variable",
        y="Count",
        color="Diabetes_Status",
        barmode="group",
        text="Count",
        title="Average Value of All Numeric Variables by Diabetes Status",
        color_discrete_map={"Yes": "#ff7e0e", "No": "#ffcb2e"}
    )

    fig.update_traces(textposition="inside")
    fig.update_layout(
        xaxis_title="Average_Value",
        yaxis_title="Count",
        height=600,
        xaxis_tickangle=-45       # Tilt labels so they don't overlap
    )
    st.plotly_chart(fig, use_container_width=True)


# Main page
st.set_page_config(layout="wide")
st.title("❣️Risk Pathways in Diabetes✨")
st.subheader("📈Diabetes Data Analysis To Find Some Insights With Visualization")
st.write("________________________________________________________________________________")

# Sidebar
st.sidebar.title("Diabetes Analysis")
file_upload = st.sidebar.file_uploader("Choose a CSV file", type="csv")

df = pd.DataFrame() 
if file_upload is not None:
    df = pd.read_csv(file_upload)

#@st.cache_data
#def load_data():
    #return pd.read_csv("large_dataset.csv")

#df = load_data()
#st.write(df.head())

if st.sidebar.header("Dashboard"):
    st.title("📊Diabetes Dashboard")

    # Sidebar filter
    status_options = df['Diabetes_Status'].unique().tolist()
    selected_status = st.sidebar.multiselect("Select Diabetes Status", status_options)

    # If nothing selected, show all data
    if not selected_status:
        df2 = df.copy()
    else:
        df2 = df[df["Diabetes_Status"].isin(selected_status)]

    # Call the dashboard function
    dashboard(df2, selected_status)


# Diabetes Insight Button
if st.sidebar.button("Diabetes Insight"):
    st.subheader("Diabetes Problems")
    st.write("Diabetes is a growing global health challenge, leading to serious " \
    "complications such as heart disease, kidney failure, vision loss, and reduced quality of life." \
    " Its rising prevalence places a heavy burden on healthcare systems and economies worldwide.")
    st.subheader("Diabetes Risk Facters")
    st.write('People most at risk of developing diabetes include those with obesity, ' \
    'sedentary lifestyles, poor dietary habits, or a family history of the disease. ' \
    'High blood pressure, advancing age, and chronic stress further increase vulnerability.' \
    ' Socioeconomic challenges, such as limited access to healthcare or healthy food, also heighten risk.')
    st.subheader("Major Risk Variables for Diabetes")
    st.write("Age: Risk increases after age 45 to 55")
    st.write("Family History: Having a parent or sibling with diabetes raises Risks.")
    st.write('Blood_Pressure — high range (101–120) heavily skewed toward diabetics (6,015 vs 4,315) high diabetic Risks')
    st.write('BMI — obese range (31–40) shows 3:1 diabetic dominance; declines with age but gap never closes increase high diabetes Risks')
    st.write('Physical_Activity: Less than 150 minutes of weekly activity raises risk.')
    st.write('Cholesterol_Level — strongest predictor (0.57 correlation); diabetics consistently show elevated levels like 200-250 Increase Diabetes Risks')
    st.write('Glucose — classic clinical marker with moderate-strong correlation (0.42) and High Level 180-250 Heavy Risk for Diabetes Patiences')
    st.write('Insulin - High Effected Facter is like Smoking , Skin_Thickness , Alcohol_Intake , Sleep_Hours to Increase Diabetes Risks' )
    st.write('Pregnancies — higher count progressively increases diabetes risk')
    st.write("Diet Habits: High intake of refined carbs, sugar, and processed foods, Eat good food to raises Diabetes Risks")


# Button to show dataset details
if st.sidebar.button("About Dataset") and not df.empty:
    st.subheader("About Dataset")
    df_simple, shape, info, dtype, null_value, duplicate_value, stat = about_df(df)

    # Display dataset details
    st.subheader("Dataset (First 10 Rows)")
    st.write(df_simple)

    st.subheader("Dataset Size")
    st.write(shape)
   
    st.subheader("Dataset Information")
    st.text(info)   # use st.text for info string
   
    st.subheader("Data Types")
    st.write(dtype) 

    st.subheader("Null Values")
    st.write(null_value)
    
    st.subheader("Duplicate Values")
    st.write(duplicate_value)

    st.subheader("Dataset Statistics")
    st.write(stat)

# Second Function Button of Statistics
if st.sidebar.button("Diabetes Statistics"):
    st.subheader("Diabetes Statistics")
    totals = Statistics(df)
    for key,value in totals.items():
      st.write(f"{key}: {round(value,2)}")

# Third Function Button of Data Cleaning 
if st.sidebar.button("Data Cleaning"):
    st.title("Data Cleaning")
    
    st.subheader("One Step Perform in Data Cleaning")
    
    st.subheader("Add the Missing values")
    st.write('Some Missing_Values in the Diet_Type and Exercise_Level Columns Not Match the Diabetes Dataset')
    st.write("Mode imputation fills missing values in categorical columns using the most frequently occurring value in that column.")
    st.write('like in this columns Missing Values')
    st.write('Diet_Type (1050)')
    st.write('Exercise_Level (900)')

    st.subheader("Remove the Outliers For Predict the ML Model")
    st.write("The IQR method was applied to remove outliers from six key variables:")
    st.write("BMI")
    st.write('Glucose')
    st.write('Blood')
    st.write('Pressure')
    st.write('Insulin')
    st.write('Cholesterol Level')
    st.write('Skin Thickness')


#Four Function Button of Outliers
if st.sidebar.button("Diabetes Model"):
    st.title("Daibetes Machine Learning Model")
    st.subheader("#First Step")
    st.subheader("Feature Engineering for ML Model")
    st.write("Label Encoding of Output Variable like Diabetes Status")

    st.subheader("#Second Step")
    st.subheader("One Hot Encoding")
    st.write("Features of Nominal Categorical Nominal Columns")
    st.write("Gender")
    st.write("Family_History")
    st.write("Diet_Type")
    st.write("Smoking_Status")
    st.write("Exercise_Level")


    st.subheader("#Third Step")
    st.subheader("Data Train Test Split for the ML Model")
    st.write("X_train.shape : (12000, 17)")
    st.write("y_train.shape : (12000,)")

    st.subheader("#Fourth Step")
    st.subheader("Standardization Method for Logistics Regression")
    st.write("Rescalling Values Between Mean and Standard Deviation 0 and 1")
    st.write("Standarize the Data to Become Numpy Array")
    st.write("Numpy Array to convert in the Orignal Dataframe")

    st.subheader("Fiveth Step")
    st.subheader("Train Machine Learning Model")
    st.write("Use Logistics Regression Model Because Output Variable is Categorical Ordinal Column")

    st.subheader("Sixth Step")
    st.subheader("Find the Accuracy of Predicting Data from Model")
    st.write("Predict Test Model")
    st.write("Actual : 0.8796666666666667")
    st.write('Scaled : 0.9603333333333334')
    st.subheader('Model Performance Very Strong')
    st.write("Diabetes_Status Prediction:")
    st.write("Training on raw (unscaled) features achieved 88.0% accuracy, which is already strong.")
    st.write("After applying feature scaling, accuracy jumped to 96.0% — a significant +8 point improvement,")
    st.write("indicating that distance-sensitive algorithms (such as SVM, or Logistic Regression) benefit greatly from normalized input ranges.")
    st.write("The scaled model correctly classifies 96 out of every 100 patients, making it a highly reliable predictor of Diabetes_Status.")
    
    st.subheader('Diabetes Prediction System Performance:')
    st.write("A machine learning prediction system was successfully built to classify Diabetes_Status with 90% accuracy.")
    st.write("The model leverages key risk factors")
    st.write("Including Age, BMI, insulin levels,Glucose,cholesterol, blood pressure, and family history to reliably identify diabetic and non-diabetic individuals.")
    st.write("With 9 out of 10 predictions correct.")
    st.write("The system demonstrates strong clinical potential as an early-warning screening tool to support timely diabetes diagnosis and intervention.")












# Five Function Button of EDA Dashboard    
if st.sidebar.button("EDA Dashboard"):
    fig = Ages_Distribution(df)
    st.title("Univariate Dashboard")
    st.subheader("Age_Distribution")
    st.pyplot(fig)
    st.write("How ages are distributed across two groups.All " \
    "three age groups are nearly equally represented (~5,000 each), " \
    "with the 41–60 group slightly leading at 4,926.The minimal difference of " \
    "just 90 records across groups confirms a well-balanced dataset")

    fig = Diabetes_Distribution(df)
    st.subheader('Distribution of Blood Pressure by Diabetes Status')   
    st.pyplot(fig)  
    st.write('Diabetic patients (Yes) show a slightly higher and more' \
    ' concentrated blood pressure distribution centered around 90–95,while ' \
    'non-diabetics (No) are centered slightly lower around 85–90 with a wider, ' \
    'flatter spread.Both groups share a similar overall range (55–138), ' \
    'but the diabetic groups denser mid-sectionsuggests consistently elevated blood pressure '
    'is more common among diabetics —pointing to blood pressure as a potentially meaningful feature for diabetes prediction.')           

    fig = Smoking_Distribution(df)
    st.subheader('Distribution of Diabetes Status')
    st.pyplot(fig)
    st.write('Distribution Diabetes_Status:Yes: 54.0% No: 46.0% ' \
    'The dataset shows a mild class imbalance with 54% diabetic (Yes) and 46% non-diabetic (No) cases')

    fig = Gender_Distribution(df)
    st.title('Bivariate Dashboard')
    st.subheader('Gender and Family_History Count by Diabetes')
    st.pyplot(fig)
    st.write('Gender: Diabetes (Yes) outnumbers non-diabetes (No) in both sexes — ' \
    'females (3,307 vs 3,867) and males (3,387 vs 3,968) — with a similar gap across genders, ' \
    'suggesting gender alone is not a strong differentiator for diabetes risk.Family History: ' \
    'This is a far stronger signal. Among those with family history, diabetics heavily outnumber non-diabetics'
    ' (4,104 vs 881), nearly a 4.5:1 ratio — while those without family history are predominantly non-diabetic '
    '(5,813 vs 3,7311). This makes family history one of the most discriminating features for diabetes prediction.')
    

    
    fig = age_Distribution(df)
    st.subheader('Age Count by Diabetes')
    st.pyplot(fig)
    st.write('Age is a strong and progressive diabetes risk factor.The youngest group (21–40) is' \
    ' predominantly non-diabetic (3,364 vs 1,423), the middle group (41–60) ' \
    'becomes nearly split (2,313 vs 2,613), and the oldest group (61–80) is overwhelmingly' \
    ' diabetic (3,799 vs 1,017).This clear age-driven escalation makes age one of the most powerful predictors in the dataset.')
    

    
    fig = smoking_Distribution(df)
    st.subheader('Smoking_Status and Diet_Type Count by Diabetes')
    st.pyplot(fig)
    st.write('Smoking Status: Diabetics outnumber non-diabetics in both smokers (2,222 vs 1,436) and non-smokers (5,613 vs 5,258), ' \
    'but the gap is notably wider among smokers, suggesting smoking amplifies diabetes risk.')
    st.write('Diet Type: ' \
    'A good diet shows the strongest protective effect — non-diabetics nearly double diabetics (2,112 vs 1,375). ' \
    'In contrast, average and poor diets both show diabetics outnumbering non-diabetics, with poor diet (3,006 vs 1,572) ' \
    'being the most concerning pattern. This makes diet quality a meaningful predictor, where better eating ' \
    'habits correlate clearly with lower diabetes prevalence.')
    
    fig = Bmi_Distribution(df)
    st.subheader('BMI Count by Diabetes')
    st.pyplot(fig)
    st.write('BMI reveals a strong and progressive diabetes risk pattern.In the healthy range (20–25), non-diabetics lead (2,257 vs 1,026).'\
             'The overweight range (26–30) becomes more competitive but still non-diabetic-leaning (2,656 vs 2,909 — nearly equal).'\
             'In the obese range (31–40), diabetics overwhelmingly dominate (3,755 vs 1,147) — a ratio of over 3:1.'\
             'This clear escalation makes BMI one of the strongest and most actionable predictors of diabetes in the dataset.')

    st.subheader("Pregnancies Distribution by Diabetes_status")
    fig = Pregnancies_Distribution(df)
    st.pyplot(fig)
    st.write('At 0 pregnancies, non-diabetics lead (550 vs 417), and at 4 pregnancies non-diabetics are closest to parity (691 vs 736).' \
    'This suggests higher pregnancy count is a meaningful escalating risk factor for diabetes.')


    fig = line_plots(df)
    st.subheader('Lineplot Age on Insulin and BMI level on Age')
    st.pyplot(fig)
    st.write('Age vs Insulin: Diabetics maintain consistently higher insulin (113–120) across all ages, ' \
    'while non-diabetics decline gradually from ~95 to ~80. The persistent gap confirms insulin as a stable, age-independent diabetes marker.')
    st.write('BMI vs Age: Diabetics start higher (~32) and decline slowly, while non-diabetics begin lower (27) and drop more steeply to 22 by age 80. ' \
    'The consistent separation across all age groups reinforces BMI as a reliable long-term diabetes differentiator.')

    fig = scatter_plots(df)
    st.subheader('Scattor_plot Cholesterol vs BMI and Physical_Activity vs Cholesterol')
    st.pyplot(fig)
    st.write('Cholesterol vs Physical Activity: Non-diabetics (orange) dominate higher activity levels with lower cholesterol (200–260), ' \
    'while diabetics (blue) cluster at zero activity and higher cholesterol (280–360) — confirming low activity + high cholesterol as a key diabetes risk combination.')
    st.write('BMI vs Cholesterol: Diabetics (blue) occupy the high BMI (28–42) and high cholesterol (290–365) zone, ' \
    'while non-diabetics (orange) concentrate at lower BMI and cholesterol. ' \
    'The clear diagonal separation makes this pair a strong visual discriminator for Diabetes_Status.')
    
    
    st.subheader("Histogram Numerical Feature Distributions")
    fig = plot_distributions(df)
    st.pyplot(fig)
    st.write('Normal Distribution Histogram Plot to Remove Some Outliers in the Dataset The IQR method was applied to remove outliers from six key variables: ' \
    'BMI, Glucose, Blood Pressure, Insulin, Cholesterol Level, and Skin Thickness.')

    st.subheader("Boxplot to Find Outliers in the Numeric Variables")
    fig = plot_boxplots(df)
    st.pyplot(fig)
    st.write("Normal Distribution Boxplot Not Any Outliers")
    
