def encoder(data):

    index_dicc = 1
    data_dicc = {0:""}
    data_dicc_values = data_dicc.values()
    old_i = ""
    data_string = ""
    last_coincidence = "0"

    for i in data:
        
        new_i = old_i + i

        if new_i in data_dicc_values:


            last_coincidence = list(data_dicc_values).index(new_i)
            old_i = new_i
            continue

        if new_i not in data_dicc_values:
            

            data_string += (str(last_coincidence) + i)
            old_i = ""
            data_dicc[index_dicc] = new_i
            index_dicc = index_dicc + 1

    return data_string

# def decoder(data_string):

#     index_dicc = 1
#     data_dicc = {}
#     data_dicc_values = data_dicc.values()
#     data_dicc_values_list = list(data_dicc_values)
#     old_i = ""
#     decoded_data = ""
    
#     for i in data_string:

#         new_i = old_i + i

#         if new_i in data_dicc_values:
            
#             old_i = new_i
#             continue
        
#         if new_i not in data_dicc_values:

#             old_i = ""
#             data_dicc[index_dicc] = new_i
#             index_dicc = index_dicc + 1
    
#     for i in data_dicc_values:

#         decoded_data += i

#     return decoded_data



# assert decoder('ABCDDEFGABCDEDBBDEAAEDAEDCDABC') == '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C'

assert encoder('ABCDDEFGABCDEDBBDEAAEDAEDCDABC') == '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C'

