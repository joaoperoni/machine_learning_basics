def convert_C_to_F(temperature_celsius):
    far = (9*temperature_celsius+160)/5
    print(f"Temperatura convertida = {far}ºF")

if __name__=="__main__":

    temp_celsius = int(input("Qual a temperatura em celsius? "))
    convert_C_to_F(temp_celsius)