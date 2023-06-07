import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import io


#to run it: python3 -m streamlit run app.py
# https://docs.streamlit.io/library/get-started

uploaded_file = None
if uploaded_file is None:
   max_title = st.title('Max\'s streamlit application')
   max_description = st.markdown('**interact with the side columns and imported data**')

st.sidebar.title('Type of Analysis:')

side_check = st.sidebar.checkbox('Data Analysis')
if side_check:
  uploaded_file = st.sidebar.file_uploader("Choose a file")
  if uploaded_file is not None:
     #wherever 'file-like' object is accepted:
     df = pd.read_csv(uploaded_file)
     show_df = st.checkbox("Show Data Frame", key = "disabled")
     if show_df:
        st.write(df)
     show_df_stats = st.checkbox("Show Statistics")
     if show_df_stats:
        data_types = df.dtypes

        #creating objects for stats df

        categorical_columns = data_types[data_types == 'object']
        num_categorical = len(categorical_columns)
        
        numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
        num_numeric = len(numeric_columns)

        num_bool = sum(data_types == 'bool')
        num_rows = df.shape[0]
        num_cols = df.shape[1]

        date_columns = data_types[data_types == 'datetime64[ns]']
        num_date_time = len(date_columns)
        
        #creating stats dataframe and importing
        stats_df = pd.DataFrame(df, columns = ['Rows', 'Columns', 'Categorical', 'Numerical', 'Boolean', 'Date/Time'])
        stats_df.loc[0, 'Rows'] = num_rows
        stats_df.loc[0, 'Columns'] = num_cols
        stats_df.loc[0, 'Categorical'] = num_categorical
        stats_df.loc[0, 'Numerical'] = num_numeric
        stats_df.loc[0, 'Boolean'] = num_bool
        stats_df.loc[0, 'Date/Time'] = num_date_time
        st.write(stats_df.head(1))

     #select column type
     column_type = st.sidebar.selectbox('Select Your Data Type', ("Numerical", "Categorical"))
     if column_type == "Numerical":
        numerical_column_1 = st.sidebar.selectbox('Select Your First Column', df.select_dtypes(include=['int64', 'float64']).columns)
        numerical_column_2 = st.sidebar.selectbox('Select Your Second Column', df.select_dtypes(include=['int64', 'float64']).columns)
        #five number summary
        numeric_col_1_summary = df[numerical_column_1].describe()
        numeric_col_2_summary = df[numerical_column_2].describe()
        show_col_1_summary = st.checkbox("Show "+ numerical_column_1 +" Five Number Summary", key = "num_1_col_5")
        if show_col_1_summary:
            st.write(numeric_col_1_summary)
        show_col_2_summary = st.checkbox("Show "+ numerical_column_2 +" Five Number Summary", key = "num_2_col_5")
        if show_col_2_summary:
            st.write(numeric_col_2_summary)
        #customizing plot
        choose_color = st.color_picker('Pick a Color', '#a2abe8')
        boxplot_color = [choose_color]
        boxplot_title = st.text_input('Set Title', 'Boxplot')
        #creating boxplot - title customization?
        sns.boxplot(x = numerical_column_1, y = numerical_column_2, data = df, palette = boxplot_color)
        plt.title(boxplot_title)
        st.pyplot(plt)

        #saving the plot
        filename = 'plot.png'
        plt.savefig(filename, dpi = 300)

        #Display download button
        with open("plot.png", "rb") as file:
           button = st.download_button(
              label = "Download image",
              data = file,
              file_name = boxplot_title+".png",
              mime="image/png"
           )        


     if column_type == "Categorical":
        categorical_column_1 = st.sidebar.selectbox('Select Your First Column', df.select_dtypes(include=['object']).columns)
        column_types = df.dtypes
        column_types_df = pd.DataFrame({'Column Name': column_types.index, 'Data Type': column_types.values}) 
        categorical_colums = df.select_dtypes(include = 'object').columns
        for col in categorical_colums:
           proportions = df[col].value_counts(normalize=True)
           proportions_df = pd.DataFrame({"Category": proportions.index, "Proportion": proportions.values})
        show_proportions = st.checkbox("Show Object Proportions")
        if show_proportions:
           st.table(proportions_df)
        #barplot code
        choose_color_barplot = st.color_picker('Pick a Color', '#a2abe8')
        barplot_color = [choose_color_barplot]
        barplot_title = st.text_input('Set Title', 'Barplot')
        df[categorical_column_1].value_counts().plot(kind='bar', color=barplot_color, xlabel = categorical_column_1, title = barplot_title);
        st.pyplot(plt)
        #saving the plot
        filename = 'plot.png'
        plt.savefig(filename, dpi = 300)

        #Display download button
        with open("plot.png", "rb") as file:
           button = st.download_button(
              label = "Download image",
              data = file,
              file_name = barplot_title+".png",
              mime="image/png"
           )        
        
        
        # and create a customized barplot. (using the categorical levels.)
