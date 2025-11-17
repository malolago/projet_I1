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
        