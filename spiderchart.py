import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Set page title
st.title("📊 Spider Chart (Radar Chart) in Streamlit")

# Sample Data
categories = ["Personal Services", "Agriculture", "Construction", "Transportation", "Utility"]
values = [5, 4, 4.5, 3, 4.5]  # Example scores

# Make it a loop (Radar charts need to be a closed shape)
values += values[:1]
categories += categories[:1]

# Create the Radar Chart using Plotly
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values,  
    theta=categories,
    fill='toself',  
    name="Performance"
))

# Customize the layout
fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 5])
    ),
    showlegend=True
)

# Show chart in Streamlit
st.plotly_chart(fig)
