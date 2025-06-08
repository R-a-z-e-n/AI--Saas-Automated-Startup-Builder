import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import cv2
import torch
import transformers
from transformers import pipeline

def load_startup_ideas():
    data = {
        'idea': [
            "AI-powered chatbot for customer service.",
            "Blockchain-based voting system.",
            "Subscription box for eco-friendly products."
        ],
        'category': ['AI', 'Blockchain', 'E-commerce']
    }
    df = pd.DataFrame(data)
    return df

def analyze_sentiments(texts):
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    return [sia.polarity_scores(text) for text in texts]

def generate_startup_idea(prompt):
    generator = pipeline("text-generation", model="gpt2")
    result = generator(prompt, max_length=30, num_return_sequences=1)
    return result[0]['generated_text']

def ml_predict(input_data):
    prompt = input_data.get('prompt', '')
    generated_idea = generate_startup_idea(prompt)
    sentiment = analyze_sentiments([generated_idea])[0]
    
    response = {
        "generated_idea": generated_idea,
        "sentiment_analysis": sentiment,
        "confidence_score": sentiment['compound']
    }
    
    return response