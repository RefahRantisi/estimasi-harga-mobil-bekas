#import pickle
#import streamlit as st
#
#model = pickle.load(open('estimasi_mobil.sav', 'rb'))
#
#st.title('estimasi harga mobil bekas')
#
#year = st.number_input('input tahun mobil')
#mileage = st.number_input('input km mobil')
#tax = st.number_input('input pajak mobil')
#mpg = st.number_input('input konsumsi bbm mobil')
#engineSize = st.number_input('input engine size')
#
#predict = ''
#
#if st.button('estimasi harga'):
#    predict = model.predict(
#        [[year, mileage, tax, mpg, engineSize]]
#    )
#    st.write('estimasi harga mobil bekas dalam pounds: ', predict)
#    st.write('estimasi harga mobil bekas dalam idr (juta):', predict*19000)

import pickle
import streamlit as st

st.set_page_config(
    page_title="Estimasi Harga Mobil Bekas",
    layout="centered"
)

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Tahun Mobil', min_value=1990, max_value=2025, value=2015)
km = st.number_input('Jarak Tempuh Odometer', value=50000)
tax_idr = st.number_input('Pajak Mobil (IDR)', value=3000000)
kml = st.number_input('Konsumsi BBM (KM per Liter)', value=12.0)
engine_cc = st.number_input('Kapasitas Mesin (CC)', value=1500)

if st.button('Estimasi Harga'):
    mileage_miles = km / 1.60934
    tax_pound = tax_idr / 19000
    mpg = kml * 2.35215
    engine_liter = engine_cc / 1000

    predict = model.predict(
        [[year, mileage_miles, tax_pound, mpg, engine_liter]]
    )[0]

    harga_idr = predict * 19000
    st.subheader('Hasil Estimasi')
    st.write(f"Estimasi harga mobil bekas: Rp {harga_idr:,.0f}")

st.write("© 2025 Estimasi Harga Mobil Bekas")







