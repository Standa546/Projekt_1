print("indexování"[0:5])
print("indexování"[-5:])
print("indexování"[::3])




kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

kg_pocet = 80
km_pocet = 54
l_pocet = 5

vypocet_kg = kg_pocet * kg_lb
vypocet_km = km_mile * km_pocet
vypocet_litry = l_gal * l_pocet

print(kg_pocet, "kg je" , vypocet_kg , "lb")
print(km_pocet, "km je", vypocet_km, "mil")
print(l_pocet, "l je", vypocet_litry, "gal")




mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

sleva_merc = 5000
cena_2_merc = mercedes*2
cena_merc_a_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou = (rolls_royce * 2) + (vybava *2)
cena_merc_s_vybavou = mercedes + vybava
merc_se_slevou = mercedes - sleva_merc

print("Sleva na Mercedes:", sleva_merc)
print("Cena za dva Mercedesy je:", cena_2_merc)
print("Cena za Mercedes a Rolls-Royce:", cena_merc_a_rolls)
print("Cena za dva Rolls-Royce s příplatkovou výbavou:", cena_2_rolls_s_vybavou )
print("Cena za Mercedes s příplatkovou výbavou", cena_merc_s_vybavou)
print("Cena za Mercedes po slevě", merc_se_slevou)



jmeno = "Lukas"
prijmeni = "Dvorak"
cele_jmeno = jmeno + " " +prijmeni
delka_jmena = len(cele_jmeno)


print("Celé jméno:" , cele_jmeno)
print("Délka jména:", delka_jmena)
print("=" * delka_jmena,)
print(cele_jmeno)
print("=" * delka_jmena)
print(f'{jmeno} {prijmeni}')

