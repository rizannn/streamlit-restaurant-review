import pickle
import streamlit as st

# load save model 
model = pickle.load(open('resto_model.sav', 'rb'))

# Judul Untuk Web
st.title('Data Mining Restaurant Review')

#buat kolom
col1, col2 = st.columns(2)

# Form Input
with col1:
 Taste = st.text_input('Masukan Nilai Taste[1-100]')

with col2:
 Ambiance = st.text_input('Masukan Nilai Ambiance[1-100]')

with col1:
 Service = st.text_input('Masukan  Nilai Service[1-100]')

with col2:
 Worth_the_price = st.text_input('Masukan Nilai Worth The price[1=ya, 0=no]')

with col1:
 Menu_variety = st.text_input('Masukan Nilai Menu Variety[1-100]')

with col2:
 Hygienic = st.text_input('Masukan Nilai Hygienic[1-100]')

with col1:
 Vegan_options = st.text_input('Masukan Nilai Vegan Option[1=ya; 0=no]')

with col2:
 Smoking_area = st.text_input('Masukan Nilai Smoking Area[1=ya, 0=no')

with col1:
 Parking = st.text_input('Masukan Nilai Parking[1=ya, 0=no')

with col2:
 Pet_friendly = st.text_input('Masukan Nilai Pet Friendly[1=ya, 0=no')

# kode Prediksi

pred_diagnosis = ' '

#Button Prediksi
if st.button('Test'):
    pred_prediction = model.predict([[Taste, Ambiance, Service , Worth_the_price, Menu_variety, Hygienic, Vegan_options, Smoking_area, Parking, Pet_friendly]])

    if(pred_prediction[0]==0):
        pred_diagnosis = 'Customer Tidak Akan Kembali'

    else:
         pred_diagnosis = 'Customer Akan Kembali'

st.success(pred_diagnosis)