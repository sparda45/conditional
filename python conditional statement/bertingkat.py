nilai = int(input('Masukkan nilai: '))
umur = int(input('Masukkan umur: '))

if nilai >= 75:
  if (umur < 15):
    print('Selamat adek, kamu lulus!')
  else:
    print('Selamat kakak, kamu lulus!')
else:
  if (umur < 15):
    print('Mohon maaf dek, coba lagi ya!')
  else:
    print('Mohon maaf kak, coba lagi ya!')