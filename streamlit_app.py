# Import python packages
import altair as alt
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

user = 'arek313'

# Write directly to the app
st.title(f"Lichess Data")

# Get the current credentials
session = get_active_session()

# Get data
data = session.sql("select * from view_lichess_data").to_pandas()
#df_white = session.sql("select * from view_lichess_data_arek313_white").to_pandas()

st.write("✅ App loaded, liczba wszystkich gier:", data.columns)


# simple bar chart
#st.write(df)


# Filter
filter_color = st.sidebar.multiselect(
    "Select color",
    data['COLOR'].unique(),
    default=list(data['COLOR'].unique())
)

# filtered_data – jeśli z jakiegoś powodu lista jest pusta, bierz wszystko
if filter_color:
    filtered_data = data[data['COLOR'].isin(filter_color)]
else:
    filtered_data = data 


# Filter - Opening Family
filter_opening_family = st.sidebar.multiselect(
    "Select Opening",
    data["OPENING_FAMILY"].unique(),
    default=list(data['OPENING_FAMILY'].unique())
                )
#data_count_games_opening = session.sql(sql_count_games_opening).collect()[0][0]
#data_games_win = session.sql(sql_games_win).collect()[0][0]
#data_games_draw = session.sql(sql_games_draws).collect()[0][0]
#data_games_lose = session.sql(sql_games_loses).collect()[0][0]
#data_games_in_every_month = session.sql(sql_games_in_every_month).collect()
#df_data_games_openings = session.sql(sql_games_in_openings).to_pandas()
#df_data_games_opening_variations = session.sql(sql_games_in_openings_variations).to_pandas()

count_games = len(data)
win_rate = data[data['SCORE'].eq(1)] / len(data)

# metrics
col1, col2, col3, col4 = st.columns(4)


col1.metric(label="Number of games",
         value=count_games)

col2.metric(label="Wins", value=win_rate)
col3.metric(label="Draws", value=draw_rate)
col4.metric(label="Loses", value=loss_rate)

def create_combo_chart_opening_family():
    # DOKOŃCZ

    sort_by_games = alt.SortField(field="NUMBER_OF_GAMES", order="descending")

    bars = alt.Chart(df_data_games_openings).mark_bar(color="#4CAF50").encode(
                x = alt.X("OPENING_FAMILY:N", sort=sort_by_games),
                y = alt.Y("NUMBER_OF_GAMES", title="Number of games"), 
                order = alt.Order("NUMBER_OF_GAMES:Q", sort='descending'),
                tooltip=["OPENING_FAMILY:N","NUMBER_OF_GAMES:Q","SCORE:Q"])

    line = alt.Chart(df_data_games_openings).mark_line(point=True, color="#e6d91a").encode(
                x=alt.X("OPENING_FAMILY", sort=sort_by_games),
                y=alt.Y("SCORE", title="SCORE"))

    st.altair_chart((bars + line).resolve_scale(y="independent").properties(title="Opening Family - Performance"))

create_combo_chart_opening_family()


def create_combo_chart_opening_name():
    # DOKOŃCZ

    sort_by_games = alt.SortField(field="NUMBER_OF_GAMES", order="descending")

    bars = alt.Chart(df_data_games_opening_variations).mark_bar(color="#4CAF50").encode(
                x = alt.X("OPENING_NAME", sort=sort_by_games),
                y = alt.Y("NUMBER_OF_GAMES", title="Number of games"), 
                order = alt.Order("NUMBER_OF_GAMES:Q", sort='descending'),
                tooltip=["OPENING_NAME","NUMBER_OF_GAMES:Q","SCORE:Q"])

    line = alt.Chart(df_data_games_opening_variations).mark_line(point=True, color="#e6d91a").encode(
                x=alt.X("OPENING_NAME", sort=sort_by_games),
                y=alt.Y("SCORE", title="SCORE"))

    st.altair_chart((bars + line).resolve_scale(y="independent").properties(title="Opening Family - Performance"))


create_combo_chart_opening_name()


# DOKOŃCZ TĘ CZEŚĆ - BAR CHART
#data_count_games_opening = session.sql(sql_count_games_opening).collect()
#bar_pandas_df = pd.DataFrame(data_count_games_opening, columns=["number_of_games", "opening_name"])
#st.bar_chart(data=bar_pandas_df, x="opening_name", y="number_of_games")

#fig = px.bar(df_group_by_opening, x = "OPENING_FAMILY", y = "Count")


# # Use an interactive slider to get user input
# hifives_val = st.slider(
#   "Number of high-fives in Q3",
#   min_value=0,
#   max_value=90,
#   value=60,
#   help="Use this to enter the number of high-fives you gave in Q3",
# )

# #  Create an example dataframe
# #  Note: this is just some dummy data, but you can easily connect to your Snowflake data
# #  It is also possible to query data using raw SQL using session.sql() e.g. session.sql("select * from table")
# created_dataframe = session.create_dataframe(
#   [[50, 25, "Q1"], [20, 35, "Q2"], [hifives_val, 30, "Q3"]],
#   schema=["HIGH_FIVES", "FIST_BUMPS", "QUARTER"],
# )

# # Execute the query and convert it into a Pandas dataframe
# queried_data = created_dataframe.to_pandas()

# # Create a simple bar chart
# # See docs.streamlit.io for more types of charts
# st.subheader("Number of high-fives")
# st.bar_chart(data=queried_data, x="QUARTER", y="HIGH_FIVES")

# st.subheader("Underlying data")
# st.dataframe(queried_data, use_container_width=True)
