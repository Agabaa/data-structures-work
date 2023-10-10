def is_uganda_martyr(name):
    uganda_martyr_names = [
        "St. Charles Lwanga",
        "St. Matthias Murumba",
        "St. Kizito",
        "St. Balikuddembe",
        "St. Mukasa Kiriwawanvu",
        "St. Denis Ssebuggwawo Wasswa",
        "St. Andrew Kaggwa",
        "St. Ponsiano Ngondwe",
        "St. Anatoli Kiriggwajjo",
        "St. Achilleus Kiwanuka"
    ]

    return name in uganda_martyr_names

input_name = "St. Charles Lwanga"
result = is_uganda_martyr(input_name)
print(result) 