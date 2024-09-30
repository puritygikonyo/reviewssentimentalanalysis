import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image

# Load model
model = pickle.load(open('sentiment_analysis.pkl', 'rb'))

# Create title
st.title('Text Prediction Analysis Model')

# Option for Single Review or Batch Processing
option = st.selectbox(
    'Choose Input Method',
    ('Single Review', 'Batch Processing (Excel File)')
)

# Single Review Processing
if option == 'Single Review':
    # Text input for single review
    review = st.text_input('Enter your review:')
    submit = st.button('Predict')

    if submit:
        # Perform sentiment analysis on the input review
        prediction = model.predict([review])

        # Display the result
        if prediction[0] == 'positive':
            st.success('Positive Review')
        else:
            st.warning('Negative Review')

# Batch Processing for Excel File
if option == 'Batch Processing (Excel File)':
    uploaded_file = st.file_uploader("Upload an Excel file with reviews", type=["xlsx"])

    if uploaded_file is not None:
        # Read the uploaded Excel file into a DataFrame
        df = pd.read_excel(uploaded_file)

        # Display the first few rows of the uploaded file
        st.write("### Uploaded Data Preview")
        st.write(df.head())

        # Ensure that the file contains a 'review' column
        if 'review' not in df.columns:
            st.error("The uploaded file must contain a 'review' column.")
        else:
            # Process each review through the model
            df['Sentiment'] = df['review'].apply(lambda x: model.predict([x])[0])

            # Display the DataFrame with the new Sentiment column
            st.write("### Sentiment Analysis Results")
            st.write(df.head())

            # Save the result to a new Excel file
            output_file = "output_with_sentiment.xlsx"
            df.to_excel(output_file, index=False)

            # Provide a download button for the updated Excel file
            st.download_button(
                label="Download Excel with Sentiment",
                data=open(output_file, "rb").read(),
                file_name=output_file,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            # Overview of the Reviews Section
            st.write("### Overview of the Reviews")

            # Total number of reviews
            total_reviews = len(df)
            st.write(f"**Total Reviews:** {total_reviews}")

            # Count positive and negative reviews
            positive_reviews = df[df['Sentiment'] == 'positive'].shape[0]
            negative_reviews = df[df['Sentiment'] == 'negative'].shape[0]

            # Calculate percentages
            positive_percentage = (positive_reviews / total_reviews) * 100
            negative_percentage = (negative_reviews / total_reviews) * 100

            st.write(f"**Positive Reviews:** {positive_reviews} ({positive_percentage:.2f}%)")
            st.write(f"**Negative Reviews:** {negative_reviews} ({negative_percentage:.2f}%)")

            # Display example reviews from both categories
            st.write("### Example Positive Reviews:")
            st.write(df[df['Sentiment'] == 'positive']['review'].head(3))

            st.write("### Example Negative Reviews:")
            st.write(df[df['Sentiment'] == 'negative']['review'].head(3))

            # Add Pie Chart and Word Cloud Side by Side
            col1, col2 = st.columns(2)

            with col1:
                st.write("Pie Chart")
                fig1, ax1 = plt.subplots()
                ax1.pie([positive_reviews, negative_reviews], labels=['Positive', 'Negative'], autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
                ax1.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
                st.pyplot(fig1)

            with col2:
                st.write("### Word Cloud")
                # Combine all reviews into a single string
                text = ' '.join(df['review'])
                
                # Generate a word cloud
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

                # Display the word cloud
                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')  # No axes for the word cloud
                st.pyplot(plt)

            # Add a redirect button to the comprehensive dashboard page
            if st.button('Go to Comprehensive Dashboard'):
                st.write("# Comprehensive Dashboard")
                
                # You can add more detailed KPIs and visualizations here
                st.write("**Sentiment Summary**")
                st.write(f"**Positive Reviews:** {positive_reviews}")
                st.write(f"**Negative Reviews:** {negative_reviews}")
                
                # Add more visualizations and analyses in the dashboard as needed
                st.write("### Other KPIs and Detailed Visualizations")
                st.write("You can include additional charts like review lengths, most common words in positive/negative reviews, etc.")
