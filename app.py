import streamlit as st
from core.calculation_engine import calculate_actual_size, UNIT_TO_METERS

st.set_page_config(page_title="Microscopy Specimen Analyzer", page_icon="🔬", layout="centered")
st.title("🔬 Microscopy Specimen Analysis System")
st.markdown("Calculate the **real-life size** of a biological specimen from microscope image measurements.")
st.divider()
st.subheader("Enter Measurement Details")

magnification = st.number_input("Magnification Factor (e.g. 400 for 400x)", min_value=0.0, value=100.0, step=10.0)
image_size = st.number_input("Measured Image Size", min_value=0.0, value=2.0, step=0.1)
units = list(UNIT_TO_METERS.keys())
input_unit = st.selectbox("Unit of the Image Measurement", options=units, index=3)
output_unit = st.selectbox("Desired Output Unit", options=units, index=3)
st.divider()

if st.button("🔍 Calculate Actual Size"):
    try:
        result, symbol = calculate_actual_size(image_size, magnification, input_unit, output_unit)
        st.success(f"✅ The actual size of the specimen is **{result:.4f} {symbol}**")
        with st.expander("Show calculation steps"):
            st.markdown(f"""
            - **Formula:** Actual Size = Image Size ÷ Magnification
            - **Step 1:** {image_size} {input_unit} ÷ {magnification} = {image_size/magnification:.6f} {input_unit}
            - **Step 2:** Convert to meters, then to {output_unit}
            - **Result:** {result:.6f} {symbol}
            """)
    except ValueError as e:
        st.error(f"❌ Input Error: {e}")
