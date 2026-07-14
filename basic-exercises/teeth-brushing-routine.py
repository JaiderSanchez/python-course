water: bool = True
toothbrush_clean: bool = True
toothpaste: bool = True
times_of_day: list[str] = ["morning", "afternoon", "night"]
time_of_day = "morning" # Only difference: 's' -> 'times' - 'time'.

for time_of_day in times_of_day:
    print(f"🌅 It's {time_of_day}. Time to brush your teeth! 🪥")
    if water and toothbrush_clean and toothpaste:
        print("🪥 Everything is ready. You can brush your teeth! 💧🦷")
        teeth_brushing_time = 0 # 2-minute brushing

        while teeth_brushing_time < 2:
            print(f"🪥 Brushing your teeth during the {time_of_day}... 🦷")
            teeth_brushing_time += 1
            answer = input("Have you finished brushing your teeth yet?: Yes or No: ").lower() # To accept any combination of uppercase and lowercase letters, use: .lower()
            if answer == "yes":
                print(f"🎉 Great job! You finished brushing your teeth this {time_of_day}. 😁✨")
                break
            else:
                print("🪥 Keep brushing! You're not finished yet. 😁")

else:
    print("⚠️ You can't brush your teeth. Something is missing! 🚱🪥")
