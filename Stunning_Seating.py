#======================== Stunning Seating =========================
print()
print("======================== Stunning Seating =========================")
print("Welcome to Jade Mountain Academy, I am Tsunami the PRINCIPAL! (it is always so fun to say that! I AM PRINCIPAL!)")
print()
print("="*35)
print()

def total_bill(bill_amount, tip_PRINCIPAL):
    tip_PRINCIPAL= int(input("How much of your payment is a tip (1 to 100): "))
    TOTAl = bill_amount * (1 + 0.01 * tip_PRINCIPAL)
    TOTAl = round(TOTAl, 2)
    print(f"Please pay ${TOTAl}")
    return TOTAl
 
# PART 2: Call the function with positional arguments
total_bill(150, 20)
 
 
# PART 3: Define a recursive function with a docstring
def seating_arrangements(guests):
    '''Now we shall observe how I PEACEFULLY arrange the seating of Queen Snowfall (YESSSS peacefully and me they can go together Glory! (reaallllllly - Glory))'''
 
    if guests == 0 or guests == 1:
        return 1
 
    # Recursive case
    else:
        return guests * seating_arrangements(guests - 1)
 
 
# PART 4: Access and print the docstring
print(seating_arrangements.__doc__)
 
# PART 5: Display seating arrangement results
print("Seating arrangements for 1 guest:", seating_arrangements(1))
print("Seating arrangements for 2 guests:", seating_arrangements(2))
print("Seating arrangements for 3 guests:", seating_arrangements(3))
print("Seating arrangements for 5 guests:", seating_arrangements(5))

print("I TOLD YOU I COULD BE PEACEFULL. TAKE THAT!- Tsunami ")
print("You're supposed to say bye to our guests not assualt Glory! - Clay  ")
print("But she started it- Tsunami")
print("DID NOT- Glory, I am busy ruling TWO tribes- Glory")
print("fiiiiiiiiiiiine BYE see i can be polite- Tsunami")
print("That was not polite- Peril who walked into the room")
print("PERIL! she tried- murmuring Clay s Tsunami wouldnt hear")
print("What did you say?- Tsunami, I said She's totally polite- Clay")
print("Bye from Tsunami's side- Sunny")