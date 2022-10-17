bahan_makanan = ['ayam','ikan','daging','tahu','tempe']
makanan_yang_diinginkan = input('masukan makanan menggunakan huruf kecil :')

if (makanan_yang_diinginkan in bahan_makanan):
 print('makanan yang dinginkan tersedia!!')
else:
    print('bahan makanan tidak ada')
    