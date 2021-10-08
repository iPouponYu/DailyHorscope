possible_horoscopes = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

print('Hello which horoscope would you like to know?')
horoscope = input()
for horoscopes in possible_horoscopes:
    if horoscopes == horoscope:
        print("Your daily horoscope for: " + horoscope + " is: ")