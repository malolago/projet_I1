import random
import os

class BatailleNavale:
    def __init__(self, taille=10):
        self.taille = taille
        self.grille_joueur = [[' ' for _ in range(taille)] for _ in range(taille)]
        self.grille_ordi = [[' ' for _ in range(taille)] for _ in range(taille)]
        self.tirs_joueur = [[' ' for _ in range(taille)] for _ in range(taille)]
        self.tirs_ordi = [[' ' for _ in range(taille)] for _ in range(taille)]
        self.navires = [
            ('Porte-avions', 5),
            ('Croiseur', 4),
            ('Destroyer', 3),
            ('Sous-marin', 3),
            ('Patrouilleur', 2)
        ]
        
    def afficher_grille(self, grille, masquer=False):
        print('  ' + ' '.join([str(i) for i in range(self.taille)]))
        for i, ligne in enumerate(grille):
            affichage = []
            for cell in ligne:
                if masquer and cell == 'N':
                    affichage.append(' ')
                else:
                    affichage.append(cell)
            print(f"{i} {' '.join(affichage)}")
    
    def placer_navire(self, grille, longueur, auto=False):
        while True:
            if auto:
                orientation = random.choice(['H', 'V'])
                if orientation == 'H':
                    x = random.randint(0, self.taille - 1)
                    y = random.randint(0, self.taille - longueur)
                else:
                    x = random.randint(0, self.taille - longueur)
                    y = random.randint(0, self.taille - 1)
            else:
                try:
                    print(f"\nPlacement d'un navire de longueur {longueur}")
                    x = int(input("Ligne (0-9): "))
                    y = int(input("Colonne (0-9): "))
                    orientation = input("Orientation (H=horizontal, V=vertical): ").upper()
                    
                    if x < 0 or x >= self.taille or y < 0 or y >= self.taille:
                        print("Position invalide!")
                        continue
                    if orientation not in ['H', 'V']:
                        print("Orientation invalide!")
                        continue
                except ValueError:
                    print("Entrée invalide!")
                    continue
            
            # Vérifier si le placement est possible
            valide = True
            positions = []
            
            for i in range(longueur):
                if orientation == 'H':
                    nx, ny = x, y + i
                else:
                    nx, ny = x + i, y
                
                if nx >= self.taille or ny >= self.taille:
                    valide = False
                    break
                if grille[nx][ny] != ' ':
                    valide = False
                    break
                positions.append((nx, ny))
            
            if valide:
                for nx, ny in positions:
                    grille[nx][ny] = 'N'
                return True
            elif not auto:
                print("Placement impossible à cet endroit!")
    
    def initialiser_jeu(self):
        print("=== PLACEMENT DE VOS NAVIRES ===\n")
        for nom, longueur in self.navires:
            self.afficher_grille(self.grille_joueur)
            print(f"\n{nom} (longueur {longueur})")
            self.placer_navire(self.grille_joueur, longueur)
            os.system('cls' if os.name == 'nt' else 'clear')
        
        # Placement automatique des navires de l'ordinateur
        for nom, longueur in self.navires:
            self.placer_navire(self.grille_ordi, longueur, auto=True)
    
    def tirer(self, grille, grille_tirs, x, y):
        if grille[x][y] == 'N':
            grille_tirs[x][y] = 'X'
            grille[x][y] = 'X'
            return True
        else:
            grille_tirs[x][y] = 'O'
            return False
    
    def partie_terminee(self, grille):
        for ligne in grille:
            if 'N' in ligne:
                return False
        return True
    
    def jouer(self):
        self.initialiser_jeu()
        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== VOS TIRS ===")
            self.afficher_grille(self.tirs_joueur)
            print("\n=== VOS NAVIRES ===")
            self.afficher_grille(self.grille_joueur)
            
            # Tour du joueur
            try:
                x = int(input("\nVotre tir - Ligne (0-9): "))
                y = int(input("Votre tir - Colonne (0-9): "))
                
                if x < 0 or x >= self.taille or y < 0 or y >= self.taille:
                    print("Position invalide!")
                    input("Appuyez sur Entrée...")
                    continue
                
                if self.tirs_joueur[x][y] != ' ':
                    print("Vous avez déjà tiré ici!")
                    input("Appuyez sur Entrée...")
                    continue
                
                if self.tirer(self.grille_ordi, self.tirs_joueur, x, y):
                    print("🎯 TOUCHÉ!")
                else:
                    print("💦 À l'eau!")
                
                input("Appuyez sur Entrée...")
                
                if self.partie_terminee(self.grille_ordi):
                    print("\n🎉 VICTOIRE! Vous avez coulé tous les navires ennemis!")
                    break
                
            except ValueError:
                print("Entrée invalide!")
                input("Appuyez sur Entrée...")
                continue
            
            # Tour de l'ordinateur
            while True:
                x = random.randint(0, self.taille - 1)
                y = random.randint(0, self.taille - 1)
                if self.tirs_ordi[x][y] == ' ':
                    break
            
            if self.tirer(self.grille_joueur, self.tirs_ordi, x, y):
                print(f"💥 L'ennemi a touché votre navire en ({x}, {y})!")
            else:
                print(f"L'ennemi a tiré en ({x}, {y}) - raté!")
            
            input("Appuyez sur Entrée...")
            
            if self.partie_terminee(self.grille_joueur):
                print("\n💀 DÉFAITE! Tous vos navires ont été coulés!")
                break

# Lancer le jeu
if __name__ == "__main__":
    jeu = BatailleNavale()
    jeu.jouer()
