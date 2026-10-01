"""Vendedores de cartas do jogo base, revisados por região.

Base factual: gwentcards/gwentcards.github.io, cards.csv (versão 4.03).
O estoque pode variar na versão Remastered; compre todas as cartas visíveis.
"""

VENDORS = [
    {"id":"crow_perch_trader","region":"velen","title":"Poleiro do Corvo, comerciante","en":"Crow's Perch trader","cards":["Albrich","Impera Brigade Guard","Nausicaa Cavalry Rider","Zerrikanian Fire Scorpion"]},
    {"id":"arinbjorn","region":"skellige","title":"Arinbjorn, estalajadeiro","en":"Arinbjorn innkeeper","cards":["Arachas","Crone: Whispess","Fiend","Thaler"]},
    {"id":"urialla","region":"skellige","title":"Vila Urialla, estalajadeiro","en":"Urialla Village innkeeper","cards":["Arachas","Elven Skirmisher","Scorch","Werewolf"]},
    {"id":"svorlag","region":"skellige","title":"Svorlag, estalajadeiro","en":"Svorlag innkeeper","cards":["Arachas","Foglet","Ice Giant","Vampire: Ekimmara"]},
    {"id":"golden_sturgeon","region":"novigrad","title":"Esturjão Dourado, estalajadeiro","en":"Golden Sturgeon innkeeper","cards":["Barclay Els","Dol Blathanna Scout","Mahakaman Defender","Siege Technician"]},
    {"id":"claywich","region":"velen","title":"Claywich, comerciante resgatado","en":"Claywich rescued trader","cards":["Black Infantry Archer","Crinfrid Reavers Dragon Hunter","Etolian Auxiliary Archers","Puttkammer","Sweers"]},
    {"id":"lindenvale","region":"velen","title":"Lindenvale, comerciante","en":"Lindenvale merchant","cards":["Black Infantry Archer","Etolian Auxiliary Archers","Heavy Zerrikanian Fire Scorpion","Poor Fucking Infantry","Rainfarn"]},
    {"id":"white_orchard_inn","region":"white_orchard","title":"Taverna de Pomar Branco, estalajadeira","en":"White Orchard innkeeper","cards":["Blue Stripes Commando","Catapult","Crinfrid Reavers Dragon Hunter","Decoy","Foltest: Lord Commander of the North"]},
    {"id":"new_port","region":"skellige","title":"Porto de Kaer Trolde, taverna Novo Porto","en":"New Port Inn","cards":["Botchling","Earth Elemental","Eredin: Commander of the Red Riders","Scorch"]},
    {"id":"passiflora","region":"novigrad","title":"Passiflora, Marquise Serenity","en":"Passiflora, Marquise Serenity","cards":["Catapult","Commander's Horn","Dol Blathanna Archer","Mahakaman Defender"]},
    {"id":"crossroads_inn","region":"velen","title":"Estalagem da Encruzilhada","en":"Inn at the Crossroads","cards":["Commander's Horn","Emhyr var Emreis: Emperor of Nilfgaard","Impera Brigade Guard","Nausicaa Cavalry Rider","Siege Engineer"]},
    {"id":"alchemy_inn","region":"novigrad","title":"Oxenfurt, Estalagem da Alquimia","en":"The Alchemy Inn","cards":["Commander's Horn","Dwarven Skirmisher","Mahakaman Defender","Vrihedd Brigade Veteran"]},
    {"id":"midcopse","region":"velen","title":"Midcopse, comerciante","en":"Midcopse shopkeeper","cards":["Crinfrid Reavers Dragon Hunter","Morteisen","Poor Fucking Infantry"]},
    {"id":"crow_perch_quartermaster","region":"velen","title":"Poleiro do Corvo, intendente do barão","en":"Crow's Perch quartermaster","cards":["Cynthia","Decoy","Nausicaa Cavalry Rider"]},
    {"id":"seven_cats","region":"novigrad","title":"Estalagem dos Sete Gatos","en":"Seven Cats Inn","cards":["Decoy","Havekar Smuggler","Impera Brigade Guard","Mahakaman Defender","Young Emissary"]},
    {"id":"cunny_goose","region":"novigrad","title":"Estalagem do Ganso","en":"Cunny of the Goose","cards":["Francesca Findabair: Daisy of the Valley","Havekar Healer","Impera Brigade Guard","Scorch","Young Emissary"]},
    {"id":"harviken","region":"skellige","title":"Harviken, estalajadeiro","en":"Harviken innkeeper","cards":["Ghoul","Harpy","Nekker","Vampire: Fleder"]},
    {"id":"kingfisher","region":"novigrad","title":"Estalagem do Martim-pescador, Olivier","en":"Kingfisher Inn","cards":["Havekar Healer","Havekar Smuggler","Mahakaman Defender","Vrihedd Brigade Veteran"]},
]


# As cartas que TÊM segunda chance. As sete sem nenhuma estão nos portões de
# segurança, porque ali o aviso precisa chegar antes; estas vêm aqui porque a
# informação útil é outra: perdeu, pega onde.
#
# "confianca" é honestidade sobre a fonte, não enfeite. Só "confirmado" aparece
# em duas fontes independentes. Em "fonte única" e "inconsistente" o guia manda
# ganhar a carta na primeira chance e trata o resgate como sorte, não como plano.
GWENT_FALLBACKS = [
    {
        "card": "Zoltan Chivay",
        "win": "Vença Aldert Geert na taverna de Pomar Branco, durante Lilases e Groselhas.",
        "deadline": "Sair de Pomar Branco",
        "fallback": "No cadáver sob a Árvore dos Enforcados, em Velen.",
        "confianca": "confirmado",
    },
    {
        "card": "Sigismund Dijkstra",
        "win": "Vença o Barão Sanguinário, no Poleiro do Corvo.",
        "deadline": "Começar Retorno ao Pântano Retorcido",
        "fallback": "No escritório dele, no Poleiro do Corvo.",
        "confianca": "confirmado",
    },
    {
        "card": "Tibor Eggebracht",
        "win": "Vença o Olivier, estalajadeiro do Martim-Pescador, em Novigrad.",
        "deadline": "Agora ou Nunca, missão em que o Olivier morre",
        "fallback": "Na sala ao lado do balcão do Martim-Pescador.",
        "confianca": "confirmado",
    },
    {
        "card": "Triss Merigold",
        "win": "Vença o Lambert, na missão Gwent: Velhos Amigos.",
        "deadline": "A Ilha das Brumas",
        "fallback": "Saqueando perto da cama dele, no salão principal de Kaer Morhen.",
        "confianca": "confirmado",
    },
    {
        "card": "Vampiro: Katakan",
        "win": "Vença o Lugos, o Louco, na missão Gwent: Estilo Skellige.",
        "deadline": "Zarpar no início dos Preparativos de Batalha, a não ser que o Svanrige vire rei",
        "fallback": "Se você perder a janela, aparece um objetivo para saquear a carta dele.",
        "confianca": "confirmado",
    },
    {
        "card": "Fringilla Vigo, Isengrim Faoiltiarna e John Natalis",
        "win": "Aceite a oferta do Zoltan em Um Jogo Perigoso.",
        "deadline": "A Ilha das Brumas",
        "fallback": "Com o Carcereiro, durante A Grande Fuga.",
        "confianca": "fonte única",
    },
    {
        "card": "Saesenthessis",
        "win": "Vença o Vernon Roche, no esconderijo dele.",
        "deadline": "Razão de Estado",
        "fallback": "Nas Anotações de Roche, no esconderijo.",
        "confianca": "fonte única",
    },
    {
        "card": "Draug",
        "win": "Vença o Crach an Craite, em Kaer Trolde.",
        "deadline": "Gelo Fino",
        "fallback": "Relato de que ela entra sozinha no baralho depois da missão.",
        "confianca": "fonte única",
    },
    {
        "card": "Geralt de Rívia",
        "win": "Vença o Thaler, na Estalagem dos Sete Gatos. É a carta de unidade mais forte do jogo.",
        "deadline": "Razão de Estado",
        "fallback": "Há relato de saque na própria estalagem, mas inconsistente entre jogadores.",
        "confianca": "inconsistente",
    },
    {
        "card": "Esterad Thyssen",
        "win": "Vença o Dijkstra na casa de banhos.",
        "deadline": "Razão de Estado",
        "fallback": "Há relato de a carta ser concedida se ele morre, mas não confirmado.",
        "confianca": "inconsistente",
    },
    {
        "card": "Foltest: O Mestre de Cerco",
        "win": "Vença o Nobre Nilfgaardiano, no Palácio Real de Vizima.",
        "deadline": "Nenhum: ele continua lá",
        "fallback": "Volte ao palácio e jogue de novo quando quiser.",
        "confianca": "confirmado",
    },
]
