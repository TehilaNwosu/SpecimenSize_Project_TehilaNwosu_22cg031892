UNIT_TO_METERS = {
    "m":  1,
    "cm": 1e-2,
    "mm": 1e-3,
    "um": 1e-6,
    "nm": 1e-9,
}

UNIT_SYMBOLS = {
    "m":  "m",
    "cm": "cm",
    "mm": "mm",
    "um": "μm",
    "nm": "nm",
}

def validate_inputs(image_size, magnification, input_unit, output_unit):
    if image_size <= 0:
        raise ValueError("Image size must be a positive number.")
    if magnification <= 0:
        raise ValueError("Magnification must be a positive number.")
    if input_unit not in UNIT_TO_METERS:
        raise ValueError(f"Input unit '{input_unit}' is not supported.")
    if output_unit not in UNIT_TO_METERS:
        raise ValueError(f"Output unit '{output_unit}' is not supported.")

def calculate_actual_size(image_size, magnification, input_unit, output_unit):
    validate_inputs(image_size, magnification, input_unit, output_unit)
    actual_size_in_input_unit = image_size / magnification
    actual_size_in_meters = actual_size_in_input_unit * UNIT_TO_METERS[input_unit]
    actual_size_in_output_unit = actual_size_in_meters / UNIT_TO_METERS[output_unit]
    symbol = UNIT_SYMBOLS[output_unit]
    return actual_size_in_output_unit, symbol
