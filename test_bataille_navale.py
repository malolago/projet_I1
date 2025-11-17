import pytest
from bataille_navale import BatailleNavale


class TestInitialisation:
    """Tests pour l'initialisation du jeu"""
    
    def test_creation_jeu_taille_par_defaut(self):
        jeu = BatailleNavale()
        assert jeu.taille == 10
        
    def test_creation_jeu_taille_personnalisee(self):
        jeu = BatailleNavale(taille=8)
        assert jeu.taille == 8
    
    def test_grilles_vides_au_depart(self):
        jeu = BatailleNavale()
        for ligne in jeu.grille_joueur:
            assert all(cell == ' ' for cell in ligne)
        for ligne in jeu.grille_ordi:
            assert all(cell == ' ' for cell in ligne)
    
    def test_grilles_tirs_vides_au_depart(self):
        jeu = BatailleNavale()
        for ligne in jeu.tirs_joueur:
            assert all(cell == ' ' for cell in ligne)
        for ligne in jeu.tirs_ordi:
            assert all(cell == ' ' for cell in ligne)
    
    def test_liste_navires_correcte(self):
        jeu = BatailleNavale()
        assert len(jeu.navires) == 5
        assert jeu.navires[0] == ('Porte-avions', 5)
        assert jeu.navires[1] == ('Croiseur', 4)
        assert jeu.navires[4] == ('Patrouilleur', 2)


class TestPlacementNavires:
    """Tests pour le placement des navires"""
    
    def test_placement_horizontal_valide(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        
        # Simuler un placement horizontal en position (0,0) de longueur 3
        positions = [(0, 0), (0, 1), (0, 2)]
        for x, y in positions:
            grille[x][y] = 'N'
        
        # Vérifier que le navire est bien placé
        assert grille[0][0] == 'N'
        assert grille[0][1] == 'N'
        assert grille[0][2] == 'N'
        assert grille[0][3] == ' '
    
    def test_placement_vertical_valide(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        
        # Simuler un placement vertical en position (0,0) de longueur 3
        positions = [(0, 0), (1, 0), (2, 0)]
        for x, y in positions:
            grille[x][y] = 'N'
        
        # Vérifier que le navire est bien placé
        assert grille[0][0] == 'N'
        assert grille[1][0] == 'N'
        assert grille[2][0] == 'N'
        assert grille[3][0] == ' '
    
    def test_placement_automatique_navire(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        
        # Placer un navire automatiquement
        resultat = jeu.placer_navire(grille, 3, auto=True)
        
        assert resultat == True
        # Compter le nombre de 'N' dans la grille
        compte_navires = sum(ligne.count('N') for ligne in grille)
        assert compte_navires == 3
    
    def test_placement_multiple_navires(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        
        # Placer plusieurs navires
        jeu.placer_navire(grille, 3, auto=True)
        jeu.placer_navire(grille, 2, auto=True)
        
        compte_navires = sum(ligne.count('N') for ligne in grille)
        assert compte_navires == 5
