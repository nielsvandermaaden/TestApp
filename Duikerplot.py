import plotly.graph_objects as go
import numpy as np

class DuikerPlottingTool():
    def __init__(self, d: float = 0.5, bok: float = 11.3, verval_duiker=0.1):
        self.d = d
        self.bok = bok
        self.verval_duiker = verval_duiker

    def cirkel_omtrek(self):
        r = self.d/2
        theta = np.linspace(0, 2 * np.pi, 100)
        x_cirkel = r * np.cos(theta)
        y_cirkel = r * np.sin(theta)
        return x_cirkel, y_cirkel

    def cirkel_lagen(self, y_onderkant, y_bovenkant):
        width, y_onderkant, y_bovenkant = self.d, y_onderkant, y_bovenkant
        r = self.d/2
        x_block = np.linspace(-width/2, width/2, 100)
        y_block = np.linspace(y_onderkant, y_bovenkant, 100)

        X, Y = np.meshgrid(x_block, y_block)
        x_block_flatten = X.flatten()
        y_block_flatten = Y.flatten()
    
        x_inside = []
        y_inside = []
        for x, y in zip(x_block_flatten, y_block_flatten):
            if (x**2 + y**2) <= r**2:
                x_inside.append(x)
                y_inside.append(y)
    
        return x_inside, y_inside

# Creëer een instantie van de klasse
tool = DuikerPlottingTool()

# Creëer een Plotly figuur
fig = go.Figure()

r = tool.d / 2  # Definieer r hier

# Voeg de blok punten toe die binnen de cirkel liggen
x_inside, y_inside = tool.cirkel_lagen(y_onderkant=-r, y_bovenkant=(-r+0.1))
fig.add_trace(go.Scatter(x=x_inside, y=y_inside, mode='markers', marker=dict(color='brown', size=3), name="Slib"))

x_inside, y_inside = tool.cirkel_lagen(y_onderkant=(-r+0.1), y_bovenkant=(-r+0.4))
fig.add_trace(go.Scatter(x=x_inside, y=y_inside, mode='markers', marker=dict(color='blue', size=3), name="Water"))

# Voeg de cirkel toe
x_cirkel, y_cirkel = tool.cirkel_omtrek()
fig.add_trace(go.Scatter(x=x_cirkel, y=y_cirkel, mode='lines', line=dict(color='black', width=5), name="Duiker"))

# Stel de aspectverhouding in op 'gelijk'
fig.update_layout(
    title="Vooraanzicht duiker",
    #Cancel possibility to zoom
    autosize=False,
    # Set background colour
    plot_bgcolor='white',
    # Set axis options
    xaxis=dict(
        title="Breedte",
        showgrid=False, 
        scaleanchor="y", 
        scaleratio=1, 
        fixedrange=True,
        # Axis line: line
        showline=True, 
        linewidth=2,
        linecolor='black',
        # Axis line: ticks
        showticklabels=True,
        ticks='outside',
        ticklen=5,
        minor=dict(
            ticks='inside', 
            ticklen=2.5, 
            tickcolor='black', 
            tickmode='auto', 
            nticks=10, 
            showgrid=False
        ),
     ),
     yaxis=dict(
        title="Hoogte m+NAP",
        showgrid=False,
        scaleanchor="x", 
        scaleratio=1, 
        fixedrange=True,
        # Axis line: line
        showline=True, 
        linewidth=2,
        linecolor='black',
        # Axis line: ticks
        showticklabels=True,
        ticks='outside',
        ticklen=5,
        minor=dict(
            ticks='inside', 
            ticklen=2.5, 
            tickcolor='black', 
            tickmode='auto', 
            nticks=10, 
            showgrid=False
        ),
     ),
    # Set legend layout
    legend=dict(
        # Define legend text size
        font=dict(
            size=32
        ),
        # Set legend symbol same size as legend text
        itemsizing='constant',
        traceorder="reversed"
    ),
)
# Toon de figuur
fig.show()

                
