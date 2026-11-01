from src.genetic_obj import Organism, Trait, Gene

def test_organism_initialization():
    gene1 = Gene("Gene1", ("A", "a"))
    trait1 = Trait("eye colour","single-gene" ,[gene1], ("a","A"), {("A", "A"): "Brown", ("A", "a"): "Brown", ("a", "a"): "Blue"})
    organism = Organism("TestOrganism", [trait1], "Male")
    assert organism.name == "TestOrganism"
    assert organism.traits[0].trait == "eye colour"
    assert organism.traits[0].genes[0].name == "Gene1"