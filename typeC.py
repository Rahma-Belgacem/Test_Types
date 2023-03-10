import os 
import sys
# Ouvrir le fichier en lecture seule
fichier = open('tbu1.c', "r")
# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lignes = fichier.readlines()
# fermez le fichier après avoir lu les lignes
fichier.close()
# Itérer sur les lignes
Type_def = "int"
for ligne in lignes:
   if Type_def in ligne:  #affichage de type du variable 
     
        match Type_def :
             case "int":
                print("variable de type INT" , ligne)
             case "long int":
                print("variable de type Long INT" , ligne)
             case "unsigned long int":
                print("variable de type Unsigned Long INT" , ligne)
             case "unsigned int":
                print("variable de type Unsigned INT" , ligne)
             case "short int":
                print("variable de type Short INT" , ligne)
             case "unsigned short int":
                print("variable de type Unsigned Short INT" , ligne)
             case "char":
                print("variable de type Char" , ligne)
             case "unsigned char":
                print("variable de type Unsigned Char" , ligne)
             case "boolean":
                print("variable de type Boolean" , ligne)
             case "byte":
                print("variable de type Byte" , ligne)
             case "short":
                print("variable de type Short" , ligne)
             case "long":
                print("variable de type Long" , ligne)
             case "long double":
                print("variable de type Long Double" , ligne)
             case "float":
                print("variable de type Float" , ligne)
             case "double":
                print("variable de type Double" , ligne)
             case Default:
                print("Variable de type inconnu " , ligne)

                
#Condition si le variable a deux types différents
                
variable = "NewIntType"
for ligne in lignes:
  if variable in ligne :
    print("le type du variable est " , ligne)
