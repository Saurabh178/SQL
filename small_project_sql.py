import streamlit as st
from db_helper import DB
import plotly.graph_objects as go
import plotly.express as px

db=DB()

st.sidebar.title('Flights Analytics')
user_option=st.sidebar.selectbox('Menu', ['None', 'Check Flights', 'Analytics'])

if user_option=='Check Flights':
    st.title('Check Flights')
    col1, col2=st.columns(2)

    city=db.fetch_city_name()

    with col1:
        source=st.selectbox('Source', sorted(city))

    with col2:
        destination=st.selectbox('Destination', sorted(city))

    if st.button('Search'):
        result=db.fetch_all_flights(source, destination)
        
        if source==destination:
            st.subheader("Source and Destination can not be same!")
        elif result[0]==0:
            st.subheader("No Flight exists in this route!")
        else:
            st.dataframe(result[1])

elif user_option=='Analytics':
    airline, freq=db.fetch_airline_freq()

    fig=go.Figure(
        go.Pie(
            labels=airline,
            values=freq,
            hoverinfo="label+percent",
            textinfo="value"
        )
    )

    st.header("Pie Chart for Flights:")
    st.plotly_chart(fig)

    city, freq1=db.fetch_busy_airport()

    fig=px.bar(
        x=city,
        y=freq1,
        color=city
    )

    st.header("Bar Chart for Busy City Airport:")
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

    doj, freq2=db.fetch_daily_flight_freq()

    fig=px.line(
        x=doj,
        y=freq2,
    )

    st.header("Line Graph for Number of flights per day:")
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

else:
    st.title('About Project:')
    st.write('1. This is a small project where we show some analysis.')
    st.write('2. In this, we show most number of planes by company, by airport and flight schedule between source and destination.')