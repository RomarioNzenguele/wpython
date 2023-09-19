'''
     * DESAFIO FIBONACCI
     *
     * Comeca-se a serie com 0 (zero) e 1 (um)
     * Obtem-se o proximo numero de Fibonacci
     * somando-se os dois anteriores e, assim,
     * sucessivamente (ate o infinito)
     *
     * 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ..
     '''
   
anterior = 0
proximo = 1

print(anterior)

while(proximo < 50):
    print(proximo)
    proximo += anterior
    anterior = proximo - anterior
