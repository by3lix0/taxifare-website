import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
import streamlit as st
import requests

# Display a title and some information using Markdown
st.markdown('''
# Taxi Fare Prediction App

Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions.
''')

# Section for user inputs
st.markdown('''
## Select Ride Parameters

Please provide the following details for your ride to retrieve a fare prediction:
''')

# Collecting user inputs using Streamlit widgets
pickup_date = st.date_input("Select pickup date")
pickup_time = st.time_input("Select pickup time")
pickup_longitude = st.number_input("Pickup Longitude", format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", format="%.6f")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, step=1)

# Combine date and time into a datetime string
pickup_datetime = f"{pickup_date} {pickup_time}"

# Button to submit
if st.button("Get Fare Prediction"):
    # API URL
    url = 'https://taxifare.lewagon.ai/predict'

    # Parameters to send to the API
    params = {
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    # Call the API using the requests package
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        prediction = response.json().get('fare', 'No prediction available')
        st.success(f"Predicted Fare: ${prediction}")
    else:
        st.error("Failed to retrieve prediction. Please try again.")

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
