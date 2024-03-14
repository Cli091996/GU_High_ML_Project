# GU_High_ML_Project
to be updated

misc 

import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Assuming actual2, predicted2, errors2, and order_type are predefined lists or arrays
# For demonstration, let's create some dummy data
np.random.seed(42)  # For reproducible results
actual2 = np.random.rand(100) * 100
predicted2 = actual2 + np.random.normal(0, 10, 100)  # Adding some noise
errors2 = np.random.rand(100) * 10
order_type = np.random.choice(['Buy', 'Sell', 'Hold'], 100)

df = pd.DataFrame({'Actual': actual2, 'Predicted': predicted2, 'Error': errors2, 'OrderType': order_type})

# Define your base title here
base_title = 'Baseline Model Prediction vs Actuals with Error Visualization'

# Initial scatter plot with the base title
fig = px.scatter(df, x='Actual', y='Predicted', color='OrderType', opacity=0.5,
                 labels={'Actual': 'Actual Values', 'Predicted': 'Predicted Values'},
                 title=base_title)

# Adding error lines for each point
error_shapes = []
for index, row in df.iterrows():
    error_shapes.append(
        dict(
            type="line",
            x0=row['Actual'],
            y0=row['Predicted'],
            x1=row['Actual'],
            y1=row['Predicted'] + row['Error'],
            line=dict(color='red', width=1),
            visible=False  # Initially set all error bars to invisible
        )
    )

fig.update_layout(shapes=error_shapes)

# Dropdown menus
order_types = df['OrderType'].unique()
dropdown_buttons = []

for ot in order_types:
    # This determines which scatter points are visible based on the order type
    scatter_visibility = [(row['OrderType'] == ot) for _, row in df.iterrows()]
    # Now we need to adjust the visibility of error bars alongside scatter points
    error_visibility = [(row['OrderType'] == ot) for _, row in df.iterrows()]
    # Combine scatter and error bar visibility
    combined_visibility = scatter_visibility + error_visibility
    
    dropdown_buttons.append(
        dict(label=ot,
             method='update',
             args=[{'visible': combined_visibility},
                   {'title': f'{base_title} - Order Type: {ot}'}])
    )

# Adding a button for showing all data points and their error bars
all_visibility = [True] * len(df) * 2  # First part for scatter points, second part for error bars
dropdown_buttons.insert(
    0, dict(label='All',
            method='update',
            args=[{'visible': all_visibility},
                  {'title': f'{base_title} - All Order Types'}])
)

# Update layout with dropdown
fig.update_layout(
    updatemenus=[
        dict(
            buttons=dropdown_buttons,
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.11,
            xanchor="left",
            y=1.15,
            yanchor="top"
        ),
    ]
)

fig.show()
