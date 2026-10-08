"""A arvore de habilidades do Remastered (patch 5.0), com as ligacoes de cada no.

Fonte: Game8, "List of All Abilities: New Remastered Skill Trees", atualizada
em 06/10/2026. As camadas de Combate, Sinais e Alquimia batem com a ordem por
nivel publicada pelo Hack The Minotaur; a de Gerais so a Game8 publica.

Nenhuma fonte diz se o jogo pede TODAS as ligacoes ou basta uma. Por isso
`unlock_order` devolve o caminho do pior caso, que funciona nos dois jeitos.
"""

# nome em ingles (como aparece na tela do jogo) -> (arvore, ligacoes)
SKILLS = {
    # Combate
    "Muscle Memory": ("Combate", ()),
    "Arrow Deflection": ("Combate", ()),
    "Cold Blood": ("Combate", ("Arrow Deflection",)),
    "Strength Training": ("Combate", ("Muscle Memory",)),
    "Three Strikes": ("Combate", ("Muscle Memory", "Strength Training")),
    "Resolve": ("Combate", ("Arrow Deflection", "Cold Blood")),
    "Undying": ("Combate", ("Three Strikes", "Resolve")),
    "Crushing Blow": ("Combate", ("Strength Training",)),
    "Razor Focus": ("Combate", ("Three Strikes",)),
    "Fleet-Footed": ("Combate", ("Undying",)),
    "Lightning Reflexes": ("Combate", ("Resolve",)),
    "Anatomical Knowledge": ("Combate", ("Cold Blood",)),
    "Whirl": ("Combate", ("Fleet-Footed",)),
    "Rend": ("Combate", ("Crushing Blow", "Razor Focus", "Whirl")),
    "Counterattack": ("Combate", ("Whirl", "Lightning Reflexes", "Anatomical Knowledge")),
    "Sunder Armor": ("Combate", ("Crushing Blow",)),
    "Crippling Strike": ("Combate", ("Whirl",)),
    "Maiming Shot": ("Combate", ("Anatomical Knowledge",)),
    "Deadly Precision": ("Combate", ("Rend", "Crippling Strike")),
    "Flood of Anger": ("Combate", ("Crippling Strike", "Counterattack")),
    # Sinais
    "Far-Reaching Aard": ("Sinais", ()),
    "Melt Armor": ("Sinais", ()),
    "Sustained Glyphs": ("Sinais", ()),
    "Exploding Shield": ("Sinais", ()),
    "Delusion": ("Sinais", ()),
    "Aard Sweep": ("Sinais", ("Far-Reaching Aard",)),
    "Firestream": ("Sinais", ("Melt Armor",)),
    "Magic Trap": ("Sinais", ("Sustained Glyphs",)),
    "Active Shield": ("Sinais", ("Exploding Shield",)),
    "Puppetmaster": ("Sinais", ("Delusion",)),
    "Supercharged Glyphs": ("Sinais", ("Firestream", "Magic Trap", "Active Shield")),
    "Shockwave": ("Sinais", ("Aard Sweep", "Firestream", "Magic Trap")),
    "Domination": ("Sinais", ("Magic Trap", "Active Shield", "Puppetmaster")),
    "Catalyst": ("Sinais", ("Shockwave", "Supercharged Glyphs")),
    "Fortify Signs": ("Sinais", ("Supercharged Glyphs", "Domination")),
    "Chain Reaction": ("Sinais", ("Catalyst", "Fortify Signs")),
    "Focus": ("Sinais", ("Catalyst",)),
    "Sidestep": ("Sinais", ("Fortify Signs",)),
    "Aftershock": ("Sinais", ("Focus", "Chain Reaction", "Sidestep")),
    "Resonance": ("Sinais", ("Aftershock",)),
    # Alquimia
    "Refreshment": ("Alquimia", ()),
    "Efficiency": ("Alquimia", ()),
    "Frenzy": ("Alquimia", ()),
    "Adaptability": ("Alquimia", ("Refreshment",)),
    "Endure Pain": ("Alquimia", ("Frenzy",)),
    "Pyrotechnics": ("Alquimia", ("Refreshment", "Efficiency", "Adaptability")),
    "Hunter Instinct": ("Alquimia", ("Refreshment", "Efficiency", "Frenzy")),
    "Poisoned Blades": ("Alquimia", ("Efficiency", "Frenzy", "Endure Pain")),
    "Protective Coating": ("Alquimia", ("Pyrotechnics",)),
    "Acquired Tolerance": ("Alquimia", ("Hunter Instinct",)),
    "Toxic Shock": ("Alquimia", ("Poisoned Blades",)),
    "Tissue Transmutation": ("Alquimia", ("Protective Coating", "Acquired Tolerance", "Toxic Shock")),
    "Delayed Recovery": ("Alquimia", ("Tissue Transmutation",)),
    "High Tolerance": ("Alquimia", ("Tissue Transmutation",)),
    "Volatile Compound": ("Alquimia", ("Protective Coating", "Delayed Recovery")),
    "Debilitating Poison": ("Alquimia", ("Toxic Shock", "High Tolerance")),
    "Fast Metabolism": ("Alquimia", ("Delayed Recovery", "High Tolerance")),
    "Cluster Bombs": ("Alquimia", ("Volatile Compound",)),
    "Side Effects": ("Alquimia", ("Fast Metabolism",)),
    "Potent Sting": ("Alquimia", ("Debilitating Poison",)),
    # Gerais: as seis tecnicas de escola ficam livres desde o comeco
    "Cat School Techniques": ("Gerais", ()),
    "Wolf School Techniques": ("Gerais", ()),
    "Bear School Techniques": ("Gerais", ()),
    "Griffin School Techniques": ("Gerais", ()),
    "Manticore School Techniques": ("Gerais", ()),
    "Viper School Techniques": ("Gerais", ()),
    "Attack is the Best Defense": ("Gerais", ("Cat School Techniques", "Wolf School Techniques", "Bear School Techniques")),
    "Gourmand": ("Gerais", ("Bear School Techniques", "Griffin School Techniques")),
    "Advanced Pyrotechnics": ("Gerais", ("Viper School Techniques",)),
    "Element of Surprise": ("Gerais", ("Advanced Pyrotechnics", "Griffin School Techniques", "Viper School Techniques", "Manticore School Techniques")),
    "Sun and Stars": ("Gerais", ("Cat School Techniques", "Wolf School Techniques", "Bear School Techniques")),
    "Adrenaline Burst": ("Gerais", ("Cat School Techniques",)),
    "Anger Management": ("Gerais", ("Bear School Techniques", "Griffin School Techniques")),
    "Survival Instinct": ("Gerais", ("Adrenaline Burst", "Sun and Stars", "Anger Management")),
    "Metabolic Control": ("Gerais", ("Griffin School Techniques", "Viper School Techniques", "Manticore School Techniques")),
    "Metabolic Boost": ("Gerais", ("Viper School Techniques",)),
    "Synergy": ("Gerais", ("Metabolic Boost", "Metabolic Control", "Anger Management")),
    "Battle Frenzy": ("Gerais", ("Cat School Techniques",)),
    "Strong Back": ("Gerais", ("Battle Frenzy", "Attack is the Best Defense", "Gourmand")),
    "Elemental Attunement": ("Gerais", ("Gourmand", "Element of Surprise")),
}

TREE_ORDER = ("Combate", "Sinais", "Alquimia", "Gerais")


def tree_of(name: str) -> str:
    return SKILLS[name][0]


def links_of(name: str) -> tuple[str, ...]:
    return SKILLS[name][1]


def unlock_order(targets: list[str]) -> list[str]:
    """Tudo o que precisa ser comprado para chegar nos alvos, na ordem.

    Pior caso: considera que o jogo exige todas as ligacoes. A ordem respeita
    as ligacoes e, entre opcoes livres, segue a ordem dos alvos, para o
    jogador fechar primeiro o que vai usar primeiro.
    """
    order: list[str] = []
    seen: set[str] = set()

    def visit(name: str) -> None:
        if name in seen:
            return
        seen.add(name)
        for link in links_of(name):
            visit(link)
        order.append(name)

    for target in targets:
        visit(target)
    return order
