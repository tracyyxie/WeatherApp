import streamlit as st
import requests

# get data from api

apiKey = "bb181c527469e8b3992a860ab07a3a4a"

def find_weather(apiKey, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
    r = requests.get(url)
    data = r.json()
    return data

# get user input and display information

def display():
    # NEW
    left,mid,right = st.columns([1,6,1])
    with mid:
        st.image("images/icons.jpg")
    st.header("Find Your Current Weather!")
    # NEW
    city = st.text_input("Your city:").lower()
    # NEW
    units = st.selectbox("Select units:",["Celsius", "Fahrenheit"])
    # NEW
    if st.button("Search"):
        try:
            weatherData = find_weather(apiKey, city)
            if weatherData["cod"] == 200:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.header(f"Weather in {weatherData['name']}:")
                    st.subheader(f"{weatherData['weather'][0]['main']}")
                    icon = weatherData['weather'][0]['icon']
                    st.image(f"https://openweathermap.org/img/wn/{icon}@2x.png")
                with col2:
                    st.write("\n")
                    st.write("\n")
                    st.write("\n")
                    if units == "Celsius":
                        temp = weatherData['main']['temp'] - 273
                        st.metric(label = "Temperature", value=f"{round(temp,1)} °C")
                        feel = weatherData['main']['feels_like'] - 273
                        st.metric(label = "Feels Like", value=f"{round(feel,1)} °C")
                    else:
                        temp = ((weatherData['main']['temp'] - 273) * (9/5)) + 32
                        st.metric(label = "Temperature", value=f"{round(temp,1)} °F")
                        feel = ((weatherData['main']['feels_like'] - 273) * (9/5)) + 32
                        st.metric(label = "Feels Like", value=f"{round(feel,1)} °F")
                with col3:
                    st.write("\n")
                    st.write("\n")
                    st.write("\n")
                    weather = weatherData['weather'][0]['main']
                    if weather == "Clear":
                        st.image("images/clear.jpg")
                    elif weather == "Clouds":
                        st.image("images/cloudy.jpg")
                    elif weather == "Thunderstorm":
                        st.image("images/thunderstorm.jpg")
                    elif weather == "Snow":
                        st.image("images/snow.jpg")
                    elif weather == "Rain" or weather == "Drizzle":
                        st.image("images/rain.jpg")
                    else:
                        st.image("images/fog.jpg")
            else:
                st.write("City not found. Please check the city name.")
        except Exception as e:
            st.write("An error occurred. Please try again.")
                

display()


