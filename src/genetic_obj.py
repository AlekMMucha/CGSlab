from enum import Enum

class Organism:
    def __init__(self, name, traits:list['Trait'],sex):
        self.traits = traits
        self.name = name
        self.sex = sex

class Trait:
    def __init__(self,trait, mode_of_inheritence, Genes:list['Gene'],possible_alleles:tuple,phenotype_map:dict[tuple[str]:str]):
        self.trait = trait
        self.genes = Genes
        self.mode_of_inheritence = mode_of_inheritence
        self.possible_alleles = possible_alleles
        self.phenotype_map = phenotype_map

class Gene:
    def __init__(self, name, alleles:tuple):
        self.name = name
        self.alleles = alleles