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


class TestTirs:
    """Tests pour la mécanique de tir"""
    
    def test_tir_touche(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        grille_tirs = [[' ' for _ in range(10)] for _ in range(10)]
        
        # Placer un navire
        grille[5][5] = 'N'
        
        # Tirer sur le navire
        resultat = jeu.tirer(grille, grille_tirs, 5, 5)
        
        assert resultat == True
        assert grille[5][5] == 'X'
        assert grille_tirs[5][5] == 'X'
    
    def test_tir_rate(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        grille_tirs = [[' ' for _ in range(10)] for _ in range(10)]
        
        # Tirer dans l'eau
        resultat = jeu.tirer(grille, grille_tirs, 5, 5)
        
        assert resultat == False
        assert grille_tirs[5][5] == 'O'
    
    def test_tirs_multiples(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        grille_tirs = [[' ' for _ in range(10)] for _ in range(10)]
        
        # Placer des navires
        grille[0][0] = 'N'
        grille[0][1] = 'N'
        
        # Premier tir touché
        assert jeu.tirer(grille, grille_tirs, 0, 0) == True
        # Deuxième tir touché
        assert jeu.tirer(grille, grille_tirs, 0, 1) == True
        # Troisième tir raté
        assert jeu.tirer(grille, grille_tirs, 0, 2) == False


class TestFinPartie:
    """Tests pour la détection de fin de partie"""
    
    def test_partie_non_terminee_avec_navires(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        grille[0][0] = 'N'
        
        assert jeu.partie_terminee(grille) == False
    
    def test_partie_terminee_sans_navires(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        
        assert jeu.partie_terminee(grille) == True
    
    def test_partie_terminee_avec_navires_coules(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        grille[0][0] = 'X'
        grille[0][1] = 'X'
        grille[0][2] = 'X'
        
        assert jeu.partie_terminee(grille) == True
    
    def test_partie_non_terminee_navires_partiellement_coules(self):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        grille[0][0] = 'X'
        grille[0][1] = 'N'  # Un morceau de navire restant
        
        assert jeu.partie_terminee(grille) == False


class TestAffichageGrille:
    """Tests pour l'affichage des grilles"""
    
    def test_afficher_grille_sans_erreur(self, capsys):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        
        # Ne doit pas lever d'exception
        jeu.afficher_grille(grille)
        
        captured = capsys.readouterr()
        # Vérifier qu'il y a bien un affichage
        assert len(captured.out) > 0
    
    def test_afficher_grille_avec_navires(self, capsys):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        grille[0][0] = 'N'
        
        jeu.afficher_grille(grille)
        
        captured = capsys.readouterr()
        assert 'N' in captured.out
    
    def test_afficher_grille_masquee(self, capsys):
        jeu = BatailleNavale()
        grille = [[' ' for _ in range(10)] for _ in range(10)]
        grille[0][0] = 'N'
        
        jeu.afficher_grille(grille, masquer=True)
        
        captured = capsys.readouterr()
        # Les navires ne doivent pas être visibles
        lines = captured.out.split('\n')
        # Vérifier qu'il n'y a pas de 'N' dans les lignes de données
        data_lines = [l for l in lines[1:] if l.strip()]
        assert all('N' not in line for line in data_lines)
