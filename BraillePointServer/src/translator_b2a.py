transl = []

# init list
for i in range(256):
    transl.append(0)

transl[0b00000000] = 0x20; #/* (space)*/
#transl[0b00101110] = 0x21; #/* ! */
transl[0b00010110] = 0x21; #/* ! */
transl[0b00110110] = 0x22; #/* " */
transl[0b00111100] = 0x23; #/* # */
transl[0b00101011] = 0x24; #/* $ */
transl[0b00101001] = 0x25; #/* % */
transl[0b00101111] = 0x26; #/* & */
transl[0b00000100] = 0x27; #/* ' */
transl[0b00110111] = 0x28; #/* ( */
transl[0b00111110] = 0x29; #/* ) */
transl[0b00100001] = 0x2A; #/* * */
transl[0b00101100] = 0x2B; #/* + */
transl[0b00100000] = 0x2C; #/* , */
transl[0b00100100] = 0x2D; #/* - */
transl[0b00101000] = 0x2E; #/* . */
transl[0b00001100] = 0x2F; #/* / */

transl[0b10011010] = 0x30; #/* 0 */
transl[0b10000001] = 0x31; #/* 1 */
transl[0b10000011] = 0x32; #/* 2 */
transl[0b10001001] = 0x33; #/* 3 */
transl[0b10011001] = 0x34; #/* 4 */
transl[0b10010001] = 0x35; #/* 5 */
transl[0b10001011] = 0x36; #/* 6 */
transl[0b10011011] = 0x37; #/* 7 */
transl[0b10010011] = 0x38; #/* 8 */
transl[0b10001010] = 0x39; #/* 9 */

transl[0b00110001] = 0x3A; #/* : */
transl[0b00110000] = 0x3B; #/* ; */
transl[0b00100011] = 0x3C; #/* < */
transl[0b00111111] = 0x3D; #/* = */
transl[0b00011100] = 0x3E; #/* > */
transl[0b00111001] = 0x3F; #/* ? */
transl[0b00001000] = 0x40; #/* @ */

transl[0b11000001] = 0x41; #/* A */
transl[0b11000011] = 0x42; #/* B */
transl[0b11001001] = 0x43; #/* C */
transl[0b11011001] = 0x44; #/* D */
transl[0b11010001] = 0x45; #/* E */
transl[0b11001011] = 0x46; #/* F */
transl[0b11011011] = 0x47; #/* G */
transl[0b11010011] = 0x48; #/* H */
transl[0b11001010] = 0x49; #/* I */
transl[0b11011010] = 0x4A; #/* J */
transl[0b11000101] = 0x4B; #/* K */
transl[0b11000111] = 0x4C; #/* L */
transl[0b11001101] = 0x4D; #/* M */
transl[0b11011101] = 0x4E; #/* N */
transl[0b11010101] = 0x4F; #/* O */
transl[0b11001111] = 0x50; #/* P */
transl[0b11011111] = 0x51; #/* Q */
transl[0b11010111] = 0x52; #/* R */
transl[0b11001110] = 0x53; #/* S */
transl[0b11011110] = 0x54; #/* T */
transl[0b11100101] = 0x55; #/* U */
transl[0b11100111] = 0x56; #/* V */
transl[0b11111010] = 0x57; #/* W */
transl[0b11101101] = 0x58; #/* X */
transl[0b11111101] = 0x59; #/* Y */
transl[0b01110101] = 0x5A; #/* Z */

transl[0b01000001] = 0x41; #/* A */
transl[0b01000011] = 0x42; #/* B */
transl[0b01001001] = 0x43; #/* C */
transl[0b01011001] = 0x44; #/* D */
transl[0b01010001] = 0x45; #/* E */
transl[0b01001011] = 0x46; #/* F */
transl[0b01011011] = 0x47; #/* G */
transl[0b01010011] = 0x48; #/* H */
transl[0b01001010] = 0x49; #/* I */
transl[0b01011010] = 0x4A; #/* J */
transl[0b01000101] = 0x4B; #/* K */
transl[0b01000111] = 0x4C; #/* L */
transl[0b01001101] = 0x4D; #/* M */
transl[0b01011101] = 0x4E; #/* N */
transl[0b01010101] = 0x4F; #/* O */
transl[0b01001111] = 0x50; #/* P */
transl[0b01011111] = 0x51; #/* Q */
transl[0b01010111] = 0x52; #/* R */
transl[0b01001110] = 0x53; #/* S */
transl[0b01011110] = 0x54; #/* T */
transl[0b01100101] = 0x55; #/* U */
transl[0b01100111] = 0x56; #/* V */
transl[0b01111010] = 0x57; #/* W */
transl[0b01101101] = 0x58; #/* X */
transl[0b01111101] = 0x59; #/* Y */
transl[0b01110101] = 0x5A; #/* Z */

transl[0b00101010] = 0x5B; #/* [ */
transl[0b00110011] = 0x5C; #/* \ */
transl[0b00111011] = 0x5D; #/* [ */
transl[0b00011000] = 0x5E; #/* ^ */
transl[0b00111000] = 0x5F; #/* _ */

transl[0b00000001] = 0x61; #/* a */
transl[0b00000011] = 0x62; #/* b */
transl[0b00001001] = 0x63; #/* c */
transl[0b00011001] = 0x64; #/* d */
transl[0b00010001] = 0x65; #/* e */
transl[0b00001011] = 0x66; #/* f */
transl[0b00011011] = 0x67; #/* g */
transl[0b00010011] = 0x68; #/* h */
transl[0b00001010] = 0x69; #/* i */
transl[0b00011010] = 0x6A; #/* j */
transl[0b00000101] = 0x6B; #/* k */
transl[0b00000111] = 0x6C; #/* l */
transl[0b00001101] = 0x6D; #/* m */
transl[0b00011101] = 0x6E; #/* n */
transl[0b00010101] = 0x6F; #/* o */
transl[0b00001111] = 0x70; #/* p */
transl[0b00011111] = 0x71; #/* q */
transl[0b00010111] = 0x72; #/* r */
transl[0b00001110] = 0x73; #/* s */
transl[0b00011110] = 0x74; #/* t */
transl[0b00100101] = 0x75; #/* u */
transl[0b00100111] = 0x76; #/* v */
transl[0b00111010] = 0x77; #/* w */
transl[0b00101101] = 0x78; #/* x */
transl[0b00111101] = 0x79; #/* y */
transl[0b00110101] = 0x7A; #/* z */

def translate(data):
    return chr(transl[data])

