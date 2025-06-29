import plotly.express as px

# Consistent green palette for all visuals
GREEN_SHADES = ['#006400', '#228B22', '#32CD32', '#7CFC00', '#ADFF2F']

def sales_by_region(df):
    data = df.groupby("Region", as_index=False)["Sales"].sum()
    fig = px.bar(
        data,
        x="Region",
        y="Sales",
        title="Sales by Region",
        text_auto=True,
        color="Region",
        color_discrete_sequence=GREEN_SHADES
    )
    fig.update_layout(
        margin=dict(t=40, b=20, l=20, r=20),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#222'),
        autosize=True,
        height=400,
        showlegend=False
    )
    fig.update_traces(textfont_size=12)
    return fig

def age_distribution(df):
    fig = px.histogram(
        df,
        x="Customer Age",
        color="Customer Gender",
        title="Customer Age Distribution",
        nbins=20,
        color_discrete_map={"Male": "#006400", "Female": "#32CD32"}
    )
    fig.update_layout(
        margin=dict(t=40, b=20, l=20, r=20),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#222'),
        autosize=True,
        height=400,
        barmode='overlay'
    )
    fig.update_traces(opacity=0.85)
    return fig

def gender_pie(df):
    gender_counts = df["Customer Gender"].value_counts().reset_index()
    gender_counts.columns = ["Customer Gender", "Count"]
    fig = px.pie(
        gender_counts,
        names="Customer Gender",
        values="Count",
        hole=0.4,
        title="Customer Gender Split",
        color="Customer Gender",
        color_discrete_map={"Male": "#228B22", "Female": "#7CFC00"}
    )
    fig.update_layout(
        margin=dict(t=40, b=20, l=20, r=20),
        font=dict(color='#222'),
        autosize=True,
        height=350,
        showlegend=True,
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff'
    )
    fig.update_traces(textinfo='percent+label', pull=[0.03, 0.03])
    return fig
