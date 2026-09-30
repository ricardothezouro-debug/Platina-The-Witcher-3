"""Instruções de localização junto aos objetivos, disponíveis offline."""
CONTRACT_STARTS = {
    "jenny_woods": "Quadro de Midcopse.",
    "missing_brother": "Quadro da Estalagem da Encruzilhada (Inn at the Crossroads).",
    "mysterious_tracks": "Quadro de Lindenvale.",
    "patrol_gone_missing": "Quadro do acampamento central nilfgaardiano.",
    "phantom_trade_route": "Refugiados de Benkelham.",
    "shrieker": "Quadro do Poleiro do Corvo (Crow's Perch).",
    "swamp_thing": "Aldeão a oeste do orfanato do Pântano Retorcido.",
    "griffin_highlands": "Poleiro do Corvo, durante a missão de mestre armeiro.",
    "merry_widow": "Quadro de Lindenvale.",
    "byways_murders": "Quadro de Oreton.",
    "woodland_beast": "Quadro do Posto de Fronteira (Border Post).",
    "deadly_delights": "Quadro da Praça do Hierarca (Hierarch Square).",
    "doors_slamming": "Quadro da Praça do Hierarca.",
    "elusive_thief": "Quadro da Praça do Hierarca.",
    "lord_wood": "Quadro da Estalagem do Ganso (Cunny of the Goose).",
    "oxenfurt_drunk": "Quadro do porto de Oxenfurt.",
    "apiarian_phantom": "Quadro de Beanston.",
    "oxenfurt_forest": "Quadro de Oxenfurt.",
    "white_lady": "Quadro ao sul das muralhas de Novigrad.",
    "dragon": "Quadro de Fyresdal.",
    "here_comes_groom": "Quadro de Svorlag.",
    "missing_son": "Quadro de Rannvaig.",
    "muire_dyaeblen": "Quadro do porto de Kaer Trolde.",
    "phantom_eldberg": "Quadro de Arinbjorn.",
    "strange_beast": "Quadro de Larvik.",
}

DETAIL_GUIDES = {
    "white_orchard_power": {
        "title": "Onde ficam as seis pedras de Pomar Branco",
        "visual": "white-orchard-power.svg",
        "map_url": "https://cdn.mos.cms.futurecdn.net/8anNKDBk2QJvzHLafRNdCF.jpg",
        "source": "https://game8.co/games/Witcher3/archives/278569",
        "credit": "Capturas do jogo: CD Projekt Red, via Game8",
        "intro": (
            "São seis pedras aqui, mas o troféu pede os CINCO Sinais ativos ao "
            "mesmo tempo: Aard, Igni, Axii, Quen e Yrden. Duas das seis são Quen, "
            "então uma delas é só ponto de habilidade extra. Cada bônus dura até "
            "você usar o Sinal correspondente, então limpe os inimigos de cada "
            "pedra ANTES de absorver, e não medite no meio do caminho."
        ),
        "steps": [
            {
                "text": (
                    "Igni, poste do Moinho (Mill). Siga direto ao norte até o "
                    "Cemitério de Pomar Branco. A pedra está em frente à entrada do "
                    "Tesouro Guardado. Tem uma aparição rondando."
                ),
                "image": "https://img.game8.co/3227495/4fafbea0f4a22d912f7271f52881aaf6.jpeg/show",
            },
            {
                "text": (
                    "Aard, poste do Moinho. Continue para o norte depois da pedra "
                    "de Igni. Esta fica ao lado de um ninho de monstros, cercada de "
                    "carniçais: mate-os primeiro."
                ),
                "image": "https://img.game8.co/3227499/a7c8f80db748e5a1222a74b61fc301c9.jpeg/show",
            },
            {
                "text": (
                    "Axii, poste do Moinho. Vá para oeste até passar a pontezinha "
                    "de madeira e siga oeste, entrando na floresta. Cercada de lobos."
                ),
                "image": "https://img.game8.co/3227498/c5d28a9abaf754ae31b9dfebaaa38d0d.jpeg/show",
            },
            {
                "text": (
                    "Quen, poste da Ponte Quebrada (Broken Bridge). Vá para o sul "
                    "da ponte, perto da borda do mapa. Esta é a Quen que entra na "
                    "conta do troféu."
                ),
                "image": "https://img.game8.co/3227494/9b5bd86aea649de28565edd4da2113f6.jpeg/show",
            },
            {
                "text": (
                    "Yrden, poste da Vila Abandonada (Abandoned Village). Vá para "
                    "leste até o Sítio Abandonado e depois direto ao sul. Tem um "
                    "urso guardando: ele mata rápido na Marcha da Morte, use "
                    "armadilha de Yrden e ataques rápidos pelas costas."
                ),
                "image": "https://img.game8.co/3227497/a4deaf0eda9d1093b696e5abc4c5a7f9.jpeg/show",
            },
            {
                "text": (
                    "Quen extra, poste da Ponte Cackler (Cackler Bridge). Bem a "
                    "leste, passando a ponte, também cercada de carniçais. Repete o "
                    "Sinal, então NÃO é necessária para o troféu: pegue pelo ponto "
                    "de habilidade, quando quiser."
                ),
                "image": "https://img.game8.co/3227493/c0fc33d173c7794f7f5d5c82c1f19c28.jpeg/show",
            },
            (
                "Ordem sugerida: Igni e Aard na mesma subida ao norte do Moinho, "
                "depois Axii a oeste, Quen na Ponte Quebrada e Yrden por último. "
                "Com os cinco bônus ativos ao mesmo tempo o troféu estoura sozinho."
            ),
        ],
    },
    "skellige_nests": {
        "title": "Os cinco ninhos de Skellige",
        "visual": "skellige-nests.svg",
        "steps": [
            "1. Ard Skellig: no naufrágio a oeste/sudoeste de Encruzilhada (Crossroads), perto da praia onde Geralt desembarca.",
            "2. Ard Skellig: siga a costa para sul/sudeste da mesma Encruzilhada. O ninho de afogadores fica ao norte/noroeste de Rannvaig.",
            "3. Ard Skellig: na Estalagem em Ruínas (Ruined Inn), na costa leste.",
            "4. Ard Skellig: Forte Grymmdjarr (Fort Grymmdjarr), a sudoeste de Fyresdal.",
            "5. An Skellig: norte da Baía dos Ventos (Bay of Winds).",
            "Leve bombas próprias para ninhos, como Samum ou Colmeia (Grapeshot). Elimine os guardas, interaja com o ninho e confirme a explosão. Descobrir o ícone não conta como destruí-lo. Estes cinco fecham Dedetização; destrua mais cinco no continente para chegar aos dez do outro troféu.",
        ],
    },
    "witcher_gear_set": {
        "title": "Uma rota concreta: conjunto básico do Grifo",
        "visual": "griffin-gear.svg",
        "steps": [
            "Compre e leia o primeiro mapa de Edwin Greloff no armeiro de Midcopse. Selecione a caça ao tesouro Escola do Grifo (Griffin School Gear) no diário para seguir os marcadores.",
            "Hindhold: procure o andar superior da torre. Ali está o diagrama da espada de aço.",
            "Lornruk: procure o diagrama da espada de prata no complexo do farol. A entrada submersa permite chegar ao interior quando a ponte está levantada.",
            "Gruta do Matador de Dragões (Dragonslayer's Grotto): explore a cripta, derrote a ekimmara e saqueie os quatro diagramas de armadura.",
            "Leve os diagramas e materiais a um armeiro e um ferreiro com nível suficiente. Fabrique armadura, luvas, calças, botas e as duas espadas. Equipe as seis peças juntas quando alcançar o nível exigido. Ter somente os diagramas não basta.",
        ],
    },
}
