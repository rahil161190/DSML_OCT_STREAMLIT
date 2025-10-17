import pandas as pd
import streamlit as st
import pickle
# we always have to import pickle in order to run the model, #car pred is a pickle file
# we have to encode everytime run the model for streamlit and encoding can be done manually in the code (shown below)
# or we can paste data frame of encoded colume also
cars_df = pd.read_csv('cars24-car-price.csv')
st.write("""
# Car Price Prediction App """)
st.dataframe(cars_df)

kms =  st.number_input("Enter the number of kilometers travelled")
engine = st.slider("Select the engine", 500, 5000, step=100)
Year =  st.slider("Select the year", 2000, 2025, step=1)
mileage =  st.slider("Select the mileage", 5,30,step =1)
seats =  st.slider("Select the seats", 1,8,step =1)
transmission_type = st.selectbox("Select the transmission type", ["Manual","Automatic"])
fuel_type =st.selectbox("Select the fuel type",['Diesel','Petrol','CNG','Electric','LPG'])

encode_dict = {"fuel_type": {'Diesel' : 1,'Petrol' : 2,'CNG' : 3,'Electric' : 4,'LPG' : 5},
               "transmission_type": {'Manual' : 1,'Automatic' : 2},}

fuel_type_encoded = encode_dict['fuel_type'][fuel_type]
transmission_type_encoded = encode_dict['transmission_type'][transmission_type]

def model_predict(kms,fuel_type_encoded,transmission_type_encoded,engine):
    with open ("car_pred", 'rb') as file:
        loaded_model = pickle.load(file)
        input_features = [[Year,1,kms,fuel_type_encoded ,transmission_type_encoded,mileage,engine,100,seats]]
        return loaded_model.predict(input_features)

if st.button("Predict"):
    price = model_predict(kms,fuel_type_encoded,transmission_type_encoded,engine)
    st.text("Predicted car price" + str(price))





