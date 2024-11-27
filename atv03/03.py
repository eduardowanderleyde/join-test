def organize_object(obj):
    result = {}
    for item in obj:
        key = item['element_dictionary']
        if key not in result:
            result[key] = []
        result[key].append(item['element'])
    return [result]  # Encapsula o dicionário em uma lista

# Teste com o objeto fornecido
obj = [{
"message_tag": "TEMPERATURE_MIN",
"element_dictionary": "INMET",
"element": "MIN_AIR_TEMP_2M_C"
}, {
"message_tag": "RELATIVE_HUMIDITY_MIN",
"element_dictionary": "INMET",
"element": "MIN_REL_HUMIDITY_2M_PCT"
}, {
"message_tag": "temperature",
"element": "AVG_AIR_TEMP_2M_C",
"element_dictionary": "METAR"
}, {
"message_tag": "PrecMin",
"element_dictionary": "SIMEPAR_MET",
"element": "DISCARDED",
}, {
"message_tag": "Prec",
"element_dictionary": "SIMEPAR_MET",
"element": "ACCUM_PRECIP_2M_MM",
}]
organized_data = organize_object(obj)
print(organized_data)
