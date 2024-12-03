import numpy as np
frasecripto = ''
frase = ''
tabela_conversao = {"0": " ", "1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i", "10": "j", "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", "16": "p", "17": "q", "18": "r", "19": "s", "20": "t", "21": "u", "22": "v", "23": "w", "24": "x", "25": "y", "26": "z", "27": "à", "28": "â", "29": "á", "30": "ã", "31": "ç", "32": "é", "33": "ê", "34": "í", "35": "ó", "36": "ô", "37": "õ", "38": "ú", "39": "ü", "40": "A", "41": "B", "42": "C", "43": "D", "44": "E", "45": "F", "46": "G", "47": "H", "48": "I", "49": "J", "50": "K", "51": "L", "52": "M", "53": "N", "54": "O", "55": "P", "56": "Q", "57": "R", "58": "S", "59": "T", "60": "U", "61": "V", "62": "W", "63": "X", "64": "Y", "65": "Z", "66": "Á", "67": "À", "68": "Â", "69": "Ã", "70": "Ç", "71": "É", "72": "Ê", "73": "Í", "74": "Ó", "75": "Ô", "76": "Õ", "77": "Ú", "78": "Ü", "79": "0", "80": "1", "81": "2", "82": "3", "83": "4", "84": "5", "85": "6", "86": "7", "87": "8", "88": "9", "89": ":", "90": ";", "91": "<", "92": "=", "93": ">", "94": "?", "95": "@", "96": "!", "97": "'", "98": "#", "99": "$", "100": "%", "101": "&", "102": "'", "103": "(", "104": ")", "105": "*", "106": "+", "107": ",", "108": "-", "109": ".", "110": "/", "111": "[", "112": "c/", "113": "]", "114": "_", "115": "{", "116": "|", "117": "}"}

cod = np.array([[29,74,62,58,50,62,27,108,0,31,81,60,20,117,68,70,2,63,37,74,25,84,77],
[98,17,114,36,102,88,18,3,2,74,54,18,92,76,84,77,35,71,86,105,12,44,68],
[19,102,95,40,32,26,44,56,44,26,56,91,28,16,28,57,27,18,94,54,19,48,88],
[109,87,0,0,83,73,38,106,101,109,75,13,37,77,32,34,4,6,52,50,104,89,31],
[110,82,16,19,103,13,5,87,96,94,79,24,2,74,53,83,41,54,96,50,55,76,80],
[14,89,67,116,85,26,73,92,80,5,18,88,3,75,102,87,70,31,104,57,30,104,51],
[73,51,44,70,52,36,66,2,16,104,80,75,109,49,80,40,72,5,100,66,17,25,81],
[111,6,65,107,75,56,24,37,35,27,100,81,109,90,48,76,116,50,45,112,51,26,104],
[89,73,48,23,84,37,111,17,59,21,46,58,0,73,73,90,54,73,54,115,3,72,91],
[14,104,34,48,45,65,62,116,95,29,50,73,0,64,11,9,33,99,102,62,25,44,94],
[88,37,22,1,75,78,16,104,91,15,90,9,0,20,34,58,25,59,92,23,113,109,40],
[1,80,23,11,104,92,70,21,12,56,101,30,0,45,115,114,73,102,2,69,34,17,83],
[116,115,91,93,89,65,65,58,60,62,78,44,0,73,40,80,79,80,67,46,106,91,39],
[85,58,109,12,60,44,89,49,43,52,96,85,0,104,45,46,74,23,31,112,64,109,7],
[24,93,0,67,3,21,86,91,115,16,31,21,0,42,62,112,26,65,73,40,3,0,73],
[43,5,0,72,20,22,17,7,16,32,32,22,0,49,12,10,50,90,101,64,23,0,96],
[104,42,0,63,96,64,25,12,109,108,63,29,0,78,81,28,35,14,1,46,8,0,14],
[48,87,0,111,32,55,39,54,109,12,69,80,0,103,24,83,100,51,54,92,21,0,36],
[69,17,0,6,60,0,35,21,0,78,80,22,0,74,69,21,78,113,3,11,67,0,80],
[109,78,0,57,105,0,100,42,0,103,81,57,0,104,22,75,10,43,47,46,105,0,5],
[52,106,0,93,43,0,107,2,0,106,3,65,0,67,78,29,72,50,32,2,4,0,117],
[67,0,0,102,37,0,74,17,0,104,97,69,0,68,116,30,88,54,63,104,94,0,87],
[10,18,0,35,94,0,81,95,0,37,42,30,0,100,38,86,41,91,1,53,49,0,41],
[29,63,0,59,112,0,0,111,0,58,43,36,0,2,91,102,72,8,45,61,55,0,46],
[51,90,0,0,64,0,109,9,0,91,11,109,0,14,81,106,20,67,13,88,66,0,86],
[12,56,0,89,65,0,35,9,0,100,97,28,0,112,71,64,5,34,68,84,7,0,86],
[84,3,0,61,92,0,57,53,0,46,37,84,0,42,99,115,84,114,32,31,75,0,88],
[102,33,0,71,3,0,76,69,0,51,37,105,0,55,47,32,105,16,41,37,95,0,113],
[15,65,0,56,92,0,112,63,0,31,43,101,0,91,74,58,85,109,69,99,26,0,8],
[47,75,0,52,41,0,81,36,0,47,49,20,0,38,59,35,17,61,13,37,25,0,42],
[33,56,0,23,17,0,28,16,0,32,18,1,0,4,53,17,16,34,13,18,1,0,13],
[51,86,0,28,34,0,47,32,0,33,18,2,0,8,106,33,32,54,22,23,2,0,18]])

decod = np.array([[7,6,1,2,7,6,1,2,5,4,5,4,3,2,1,6,7,6,1,2,7,6,1,2,5,4,5,4,3,2,1,6],
[1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,7,1,1,1,3,1,1,1,3,1,1,1,1,1,1,1,7],
[0,0,1,2,0,0,1,2,0,0,1,4,0,0,1,6,0,0,1,2,0,0,1,2,0,0,1,4,0,0,1,6],
[0,0,1,3,0,0,1,3,0,0,1,5,0,0,1,7,0,0,1,3,0,0,1,3,0,0,1,5,0,0,1,7],
[0,0,0,0,1,8,1,8,0,0,0,0,3,2,1,6,0,0,0,0,1,8,1,8,0,0,0,0,3,2,1,6],
[0,0,0,0,1,9,1,9,0,0,0,0,1,1,1,7,0,0,0,0,1,9,1,9,0,0,0,0,1,1,1,7],
[0,0,0,0,0,0,1,7,0,0,0,0,0,0,1,6,0,0,0,0,0,0,1,7,0,0,0,0,0,0,1,6],
[0,0,0,0,0,0,1,8,0,0,0,0,0,0,1,7,0,0,0,0,0,0,1,8,0,0,0,0,0,0,1,7],
[0,0,0,0,0,0,0,0,5,4,5,4,3,2,1,6,0,0,0,0,0,0,0,0,5,4,5,4,3,2,1,6],
[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,7,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,7],
[0,0,0,0,0,0,0,0,0,0,1,4,0,0,1,6,0,0,0,0,0,0,0,0,0,0,1,4,0,0,1,6],
[0,0,0,0,0,0,0,0,0,0,1,5,0,0,1,7,0,0,0,0,0,0,0,0,0,0,1,5,0,0,1,7],
[0,0,0,0,0,0,0,0,0,0,0,0,3,2,1,6,0,0,0,0,0,0,0,0,0,0,0,0,3,2,1,6],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,7,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,7],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,6],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,7],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,1,8,2,1,1,5,1,8,1,8,2,1,1,5],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,9,1,9,1,1,1,6,1,9,1,9,1,1,1,6],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,7,0,0,1,5,0,0,1,7,0,0,1,5],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,0,0,1,6,0,0,1,8,0,0,1,6],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,5,0,0,0,0,2,1,1,5],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,6,0,0,0,0,1,1,1,6],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,1,5],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,6,0,0,0,0,0,0,1,6],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,3,1,3,4,3,1,3],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,4,1,1,1,4],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,0,0,1,3],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,0,0,1,4],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,5,6,5],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]])

decodinv = np.linalg.inv(decod).round(0).astype(int)

matriz = np.matmul(decodinv, cod)

matriz = matriz % 118

matriz = matriz.round(0).astype(int)

matriz = matriz.astype(str)

linhas = len(matriz)
colunas = len(matriz[0])

for coluna in range(colunas):
    for linha in range(linhas):
        frasecripto = frasecripto + ' ' + matriz[linha][coluna]

frasecripto = frasecripto.split()
print(frasecripto)

for i in frasecripto:
    frase = frase + tabela_conversao[i]

print(frase)




    