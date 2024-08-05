weather_c={
    "monday":12,
    "tuesday":14,
    "wednesday":15,
    "thursday":14,
    "friday":21,
    "saturday":22,
    "sunday":24,
}

weather_f={day:(temp_c*9/5)+32 for (day,temp_c) in weather_c.items()}
print(weather_f)