import plotly.express as px

# Different shades of green for bars and pie
GREEN_SHADES = ['#006400', '#228B22', '#32CD32', '#7CFC00', '#ADFF2F']

def sales_by_region(df):
    data = df.groupby("Region")["Sales"].sum().reset_index()
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
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='black'),
        autosize=True,
        height=400
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
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='black'),
        autosize=True,
        height=400
    )
    return fig

def gender_pie(df):
    fig = px.pie(
        df,
        names="Customer Gender",
        hole=0.4,
        title="Customer Gender Split",
        color="Customer Gender",
        color_discrete_map={"Male": "#228B22", "Female": "#7CFC00"}
    )
    fig.update_layout(
        margin=dict(t=40, b=20, l=20, r=20),
        font=dict(color='black'),
        autosize=True,
        height=350
    )
    return fig
