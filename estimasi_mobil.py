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

# Load model
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

# Input pengguna (dalam konteks Indonesia)
year = st.number_input('Tahun Mobil', min_value=1990, max_value=2025)
km = st.number_input('Jarak Tempuh Odometer')
tax_idr = st.number_input('Pajak Mobil)')
kml = st.number_input('Konsumsi BBM (KM per Liter)')
engine_cc = st.number_input('Kapasitas Mesin (CC)')

predict = ''

# --- Konversi ke format Inggris sesuai model ---
# 1. Mileage: KM → MILES (1 mile = 1.60934 km)
mileage_miles = km / 1.60934

# 2. Tax: IDR → POUND (misal 1 pound = 19.000 IDR)
tax_pound = tax_idr / 19000

# 3. Fuel consumption: KM/L → MPG (1 kml = 2.35215 mpg)
mpg = kml * 2.35215

# 4. Engine size: CC → Liter
engine_liter = engine_cc / 1000

# --- Prediksi ---
if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage_miles, tax_pound, mpg, engine_liter]]
    )[0]

    st.subheader('Hasil Estimasi')

    st.write(f"Estimasi harga mobil bekas dalam Pounds: £{predict:,.2f}")

    harga_idr = predict * 19000
    st.write(f"Estimasi harga mobil bekas dalam Rupiah: Rp {harga_idr:,.0f}")

