def attire_suggest(temperature,weather):
    #Weather conditions like sunny, rainy, snowy, and windy
    attire = ""

    if temperature <= 0:
        attire += "Wear heavy winter clothing like a thick coat, gloves, and a scarf.\n"

        if weather == "snowy":
            attire += "Don't forget your boots and snow gear!\n"

    elif temperature >= 1 and temperature <= 10:
        attire += "Wear a warm jacket, sweater, and jeans.\n"
        
        if weather == "rainy":
            attire += "Carry an umbrella and wear waterproof boots.\n"
    
    elif temperature >=11 and temperature <= 20:
        attire += "Wear a light jacket or sweater, and comfortable pants.\n"

        if weather == "rainy":
            attire += "An umbrella would be a good choice.\n"
    
    elif temperature >=21 and temperature <= 30:
        attire += "Wear light clothing like a t-shirt, shorts, or light pants.\n"
        if weather == "sunny":
            attire += "Wear sunglasses and sunscreen.\n"
    else:
        attire += "Wear very light clothing like shorts, tank tops, and flip-flops.\n"
        if weather == "sunny":
            attire += "Definitely wear sunglasses and sunscreen.\n"

    if weather == "windy":
        attire += "A windbreaker or jacket would be ideal for windy conditions.\n"
    elif weather == "rainy":
        attire += "Wear a waterproof jacket and carry an umbrella.\n"
    elif weather == "snowy":
        attire += "Wear insulated boots, a warm coat, and mittens.\n"

    return attire

temperature = int(input("Enter the temperature (in Celsius): "))
weather= input("Enter the weather condition (sunny, rainy, snowy, windy): ")

# Get attire suggestion
suggested_attire = attire_suggest(temperature, weather)

# Display the suggested attire
print("\nSuggested Attire:")
print(suggested_attire)
