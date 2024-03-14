# GU_High_ML_Project
to be updated

misc 
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Assuming actual2, predicted2, errors2, and order_type are predefined lists or arrays
actual2 = actual2
predicted2 = predicted2
errors2 = errors2  # Assuming errors2 is defined
order_type = order_type

df = pd.DataFrame({'Actual': actual2, 'Predicted': predicted2, 'Error': errors2, 'OrderType': order_type})

# Define your base title here
base_title = 'Baseline Model Prediction vs Actuals with Error Visualization'

# Assign colors to each order type - you might want to choose more distinct colors
unique_order_types = df['OrderType'].unique()
colors = px.colors.qualitative.Plotly
color_mapping = {order_type: color for order_type, color in zip(unique_order_types, colors)}

fig = go.Figure()

# Add scatter points
for ot in unique_order_types:
    df_filtered = df[df['OrderType'] == ot]
    fig.add_trace(go.Scatter(x=df_filtered['Actual'], y=df_filtered['Predicted'], mode='markers', 
                             name=ot, marker=dict(color=color_mapping[ot], opacity=0.5)))

# Adding error lines
for index, row in df.iterrows():
    fig.add_shape(
        type="line",
        x0=row['Actual'], y0=row['Predicted'],
        x1=row['Actual'], y1=row['Predicted'] + row['Error'],
        line=dict(color=color_mapping[row['OrderType']], width=1),
        visible='legendonly'  # Error lines are initially hidden
    )

# Use this section if you want to keep the error trend line (adjust as necessary)
# Adjusted to be hidden initially, not color-coded by order type
fig.add_trace(
    go.Scatter(
        x=df['Actual'],
        y=df['Error'],
        mode='lines',
        line=dict(dash='dot', color='grey', width=0.5),
        marker=dict(size=1, opacity=0),
        yaxis='y2',
        name='Errors Trend',
        visible=False  # Keep this trendline initially hidden
    )
)

# Update layout with dropdown (Adjust as necessary)
# Note: The color-coding dropdown logic needs to be adjusted if you want to color-code error trends as well

fig.update_layout(
    title=base_title,
    xaxis_title='Actual Values',
    yaxis_title='Predicted Values',
    legend_title='Order Type',
    yaxis2=dict(
        title='Error',
        overlaying='y',
        side='right',
        showgrid=False,
        showticklabels=True,
    )
)

fig.show()

Google Pixel 6 Pro
