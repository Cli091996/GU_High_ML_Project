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
errors2 = errors2  # Make sure you have defined errors2 somewhere in your code
order_type = order_type

df = pd.DataFrame({'Actual': actual2, 'Predicted': predicted2, 'Error': errors2, 'OrderType': order_type})

# Define your base title here
base_title = 'Baseline Model Prediction vs Actuals with Error Visualization'

# Initial scatter plot with the base title
fig = px.scatter(df, x='Actual', y='Predicted', color='OrderType', opacity=0.5,
                 labels={'Actual': 'Actual Values', 'Predicted': 'Predicted Values'},
                 title=base_title)

# Adding error lines using iterrows
for index, row in df.iterrows():
    fig.add_shape(
        go.layout.Shape(
            type="line",
            x0=row['Actual'],
            y0=row['Predicted'],
            x1=row['Actual'],
            y1=row['Actual'] + row['Error'],
            line=dict(color='red', width=1, dash='solid'),
        )
    )

# Add error trend on secondary y-axis
fig.add_trace(
    go.Scatter(
        x=df['Actual'],
        y=df['Error'],
        mode='lines',
        line=dict(dash='dot', color='red', width=.0001),
        marker=dict(color='red', size=1, opacity=0.1),
        yaxis='y2',
        name='Errors Trend',
        visible=False  # Ensure the trendline is initially hidden
    )
)

# Dropdown menus
order_types = df['OrderType'].unique()
dropdown_buttons = [
    dict(label='All',
         method='update',
         args=[{'visible': True] * (len(df) + 1) + [False] * len(order_types) * 2,
               {'title': f'{base_title} - All Order Types', 'yaxis2.title': 'Error', 'yaxis2.overlaying': 'y', 'yaxis2.side': 'right'}])
]

# New code to handle visibility based on selected order type
for ot in order_types:
    # Create a filtered DataFrame for this order type
    df_filtered = df[df['OrderType'] == ot]

    # Define visibility for scatter points and error lines
    visible = [True] * len(df_filtered) + [
        False for _ in range(len(df) - len(df_filtered))
    ] * 2

    # Define visibility for error trendline (only for "Sell" type)
    errors_trend_visibility = (ot == "Sell")

    dropdown_buttons.append(
        dict(label=ot,
             method='update',
             args=[{'visible': visible},
                   {'title': f'{base_title} - Order Type: {ot}',
                    'yaxis2.title': 'Error',
                    'yaxis2.overlaying': 'y',
                    'yaxis2.side': 'right'}])
    )

# Update layout with dropdown and ensure the secondary Y-axis is correctly configured
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
    ],
    yaxis2=dict(
        title='Error',
        overlaying='y',
        side='right',
        showgrid=False,
        showticklabels=True,
    )
)

fig.show()
