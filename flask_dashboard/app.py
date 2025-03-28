from flask import Flask, render_template, request
import plotly.express as px
import pandas as pd
import numpy as np
import json
import plotly

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    chart_type = request.form.get("chart_type", "bar")

    # Load coffee data
    df = pd.read_csv("coffee_exports.csv")
    df.columns = [col.strip() for col in df.columns]  # Sanitize headers
    df = df.dropna()

    # Chart selection logic
    if chart_type == "scatter":
        fig = px.scatter(
            df,
            x="Year",
            y="Export_Value_USD",
            color="Country",
            size="Export_Tons",
            title="Coffee Export Value Over Time",
            hover_name="Region"
        )
    elif chart_type == "box":
        fig = px.box(
            df,
            x="Region",
            y="Export_Tons",
            color="Region",
            title="Coffee Export Tons by Region"
        )
    else:  # Default bar
        df_grouped = df.groupby("Country")["Export_Value_USD"].sum().reset_index()
        fig = px.bar(
            df_grouped,
            x="Country",
            y="Export_Value_USD",
            title="Total Coffee Export Value by Country"
        )

    # Dark theme
    fig.update_layout(
        plot_bgcolor='#1a1c23',
        paper_bgcolor='#1a1c23',
        font_color='#ffffff',
        autosize=True,
        margin=dict(t=50, l=50, r=50, b=50),
        height=600
    )
    fig.update_xaxes(showgrid=False, color='#cccccc')
    fig.update_yaxes(showgrid=False, color='#cccccc')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", graphJSON=graphJSON, chart_type=chart_type)

if __name__ == "__main__":
    app.run(debug=True)
