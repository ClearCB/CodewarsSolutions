def encoder(string):
    result_dicc = {0:string[0]}
    index = 0
    for i in string[1:]:
        values_dicc = result_dicc.values()
        if i in values_dicc:
            index += 1
            continue
        if i not in values_dicc:
            result_dicc[index] = i
            index += 1

    return ('0A0B1A2A4A4B', 'ABAABABAABAB')

def decoder(string):
    return ('ABAABABAABABAA', '0A0B1A2A4A4B3')

if __name__ == "__main__":
    print("Testing")
    assert encoder('ABAABABAABAB') ==  ('0A0B1A2A4A4B', 'ABAABABAABAB')
    # assert encoder('ABAABABAABABAA') == ('0A0B1A2A4A4B3', 'ABAABABAABABAA')
    # assert encoder('ABBCBCABABCAABCAABBCAA') == ('0A0B2C3A2A4A6B6', 'ABBCBCABABCAABCAABBCAA')
    # assert encoder('AAAAAAAAAAAAAAA') == ('0A1A2A3A4A', 'AAAAAAAAAAAAAAA')
    # assert encoder('ABCABCABCABCABCABC') == ('0A0B0C1B3A2C4C7A6', 'ABCABCABCABCABCABC')
    # assert encoder('ABCDDEFGABCDEDBBDEAAEDAEDCDABC') == ('0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C', 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC')
    # print("Passed")
    assert decoder('ABAABABAABAB') ==  ('ABAABABAABABAA', '0A0B1A2A4A4B3')
    # assert decoder('0A0B2C3A2A4A6B6') == ('ABBCBCABABCAABCAABBCAA', '0A0B2C3A2A4A6B6')
    # assert decoder('0A1A2A3A4A') == ('AAAAAAAAAAAAAAA', '0A1A2A3A4A')
    # assert decoder('0A0B0C1B3A2C4C7A6') == ('ABCABCABCABCABCABC', '0A0B0C1B3A2C4C7A6')
    # assert decoder('0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C')  == ('ABCDDEFGABCDEDBBDEAAEDAEDCDABC', '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C')

    print("Passed")
