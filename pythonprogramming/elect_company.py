# 1.2
# An electric power distribution company charges domestic customers as
# follows: Consumption unit Rate of charge:
# 1.2.1. 0-200 Rs. 0.50 per unit
# 1.2.2. 201-400 Rs. 0.65 per unit in excess of 200
# 1.2.3. 401-600 Rs 0.80 per unit excess of 400
# 1.2.4. 601 and above Rs 1.00per unit excess of 600
# 1.2.5. If the bill exceeds Rs. 400, then a surcharge of 15% will be charged,
# and the minimum bill should be Rs. 100/-

def main():

    Cusnm=input("Cusntomer nm")
    unit_consumed=int(input("the unit consumed by " +Cusnm+" is:"))

    amt=0
    

    if unit_consumed<200:
        amt = unit_consumed *0.50
    elif unit_consumed<=400:
        amt = (200*0.50) +(unit_consumed-200)*0.65
    elif unit_consumed<=600:
        amt = (200*0.50) +(200*0.65) +(unit_consumed-400)*0.80
    elif unit_consumed>=600:
        amt =(200*0.50) +(200*0.65) + (200*0.80)+ (unit_consumed-600)*1.00
    else:
        amt = (200*0.50)+(200*0.65)+(200+0.80)+(unit_consumed-600) * 1.00

    if amt>400:
        surcharge= amt * 0.15
    else:
        surcharge=0

    total_amount = amt + surcharge

    if total_amount < 100:
        total_amount = 100

    print("\n\t\t\tElectricity Bill\n")
    print(f"Customer Name: {Cusnm}")
    print(f"Units Consumed: {unit_consumed}")
    print(f"Amount Charges: {amt:.2f}")
    print(f"Surcharge Amount: {surcharge:.2f}")
    print(f"Net Amount Paid By the Customer: {total_amount:.2f}")

if __name__ == "__main__":
    main()

