def calculate_green_score(transport, diet, energy):
    score = 100

    if transport.lower() == 'car':
        score -= 30
    elif transport.lower() == 'public':
        score -= 10
    elif transport.lower() == 'bicycle':
        score -= 0

    if diet.lower() == 'meat':
        score -= 20
    elif diet.lower() == 'vegetarian':
        score -= 5

    if energy > 300:
        score -= 25

    return score


# Example usage
transport_input = input("Enter your transport method (car/public/bicycle): ")
diet_input = input("Enter your diet type (meat/vegetarian): ")
energy_input = float(input("Enter your monthly energy usage in kWh: "))

green_score = calculate_green_score(transport_input, diet_input, energy_input)
print(" Your Green Score is:", green_score)
