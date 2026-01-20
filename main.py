#game secret number

secret_number = 111
tebakan = int(input("tebak angka"))

while secret_number != tebakan:
    print("Haha.. kamu terjebak dalam looping selamanya")
    print("coba tebak lagi")
    tebakan = int(input("tebak angka:"))

print("selamat anda benar!!")