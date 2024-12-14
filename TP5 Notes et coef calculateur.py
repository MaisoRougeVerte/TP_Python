
note = []
coef = []
note_finale_totale = 0  

for i in range(5):
    noteetcoef = input("Rentre la note puis le coef (séparés par un espace) : ")
    valeur_des_notes, valeur_du_coef = noteetcoef.split()
    
    # Conversion en float pour les calculs
    valeur_des_notes = float(valeur_des_notes)
    valeur_du_coef = float(valeur_du_coef)
    
    note.append(valeur_des_notes)
    coef.append(valeur_du_coef)

    note_finale = valeur_des_notes * valeur_du_coef
    note_finale_totale += note_finale  
    print(f"Note pour cette entrée : {note_finale}")

moyenne = note_finale_totale / sum(coef)
print(f"Moyenne : {moyenne}")
