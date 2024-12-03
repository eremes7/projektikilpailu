

# Avaa tiedosto lukutilassa
with open("outputData.txt", "r") as file:
    # Lue ensimmäinen rivi
    first_line = file.readline()

# Kirjoita tiedostoon takaisin vain ensimmäinen rivi
with open("outputData.txt", "w") as file:
    file.write(first_line)









