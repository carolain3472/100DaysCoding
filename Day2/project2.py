#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

factura= float(input("¿Cual es el valor de la factura?"))

personas= int(input("¿Cuantas personas pagaran la cuenta?"))

porcentaje= float(input("¿Cuanto es el pocentaje de la propina para brindar?"))

propina_individual= round((factura*(1+porcentaje/100))/personas,1)

print(f"La propina que debe dar cada uno es de: {propina_individual}")
