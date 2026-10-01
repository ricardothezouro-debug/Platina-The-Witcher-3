"""Conteúdo estrutural do guia.

O arquivo descreve relações e prazos. A interface apenas apresenta esses dados.
"""
from __future__ import annotations

GUIDE_ID = "witcher3-base"
GAME_NAME = "The Witcher 3: Wild Hunt"
GAME_SUBTITLE = "PS5 Remastered | jogo base | uma campanha na Marcha da Morte"
ACCENT = "#37F2FF"
FOOTER = "Guia não oficial do jogo base para PS5 Remastered"

INTRO = (
    "Explore no seu ritmo. Na aba Agora, escolha sua fase da história e resolva "
    "primeiro os alertas antes de continuar. Marque apenas o que realmente fez. "
    "Regiões organiza a exploração; Gwent reúne compras, partidas e cartas de missão. "
    "Os itens concluídos podem ser desmarcados a qualquer momento."
)

GWENT_PRIMER = [
    "Você precisa vencer duas das três rodadas. Pode passar uma rodada de propósito "
    "para guardar cartas e vencer as duas seguintes.",
    "Antes de jogar por uma carta única, monte um baralho enxuto: use as melhores "
    "unidades, cartas de espião e algumas Iscas. Espiões dão cartas extras; Isca "
    "permite recuperar uma carta da mesa.",
    "O primeiro triunfo contra um jogador comum costuma dar uma carta aleatória. "
    "Repetir o mesmo adversário não substitui vencer jogadores novos.",
    "No torneio Grandes Apostas, confirme seu baralho antes da inscrição. Se perder "
    "uma partida, a carta daquela rodada pode ficar inacessível na campanha atual.",
]

SECTIONS = [
    {"key": "now", "label": "Agora"},
    {"key": "regions", "label": "Regiões"},
    {"key": "gwent", "label": "Gwent"},
    {"key": "trophies", "label": "Troféus"},
    {"key": "builds", "label": "Marcha da Morte"},
]

# Imagens oficiais do site e do press kit da CD PROJEKT RED. O guia baixa cada
# arquivo apenas uma vez e mantém uma cópia no cache para as próximas aberturas.
SECTION_IMAGES = {
    "now": "https://public.cdn.cdpr.app/common/news/ec517a01feb6d9f49c9e7b822722e41f_q90_1920x1080.png",
    "regions": "https://public.cdn.cdpr.app/thewitcher/website/build/2893623026-0cd871f4/_next/static/media/3.214jklslg-ajt.jpg",
    "gwent": "https://public.cdn.cdpr.app/thewitcher/website/build/2893623026-0cd871f4/_next/static/media/gwent.1yf-j8ef-53ad.png",
    "trophies": "https://public.cdn.cdpr.app/thewitcher/website/build/2893623026-0cd871f4/_next/static/media/1.1v2rkvnnck1vb.jpg",
    "builds": "https://public.cdn.cdpr.app/thewitcher/website/build/2893623026-0cd871f4/_next/static/media/skill_m.0ycaagwxnfhfz.jpg",
}

PHASES = [
    {
        "id": "white_orchard",
        "title": "Pomar Branco",
        "en": "White Orchard",
        "summary": "Prólogo, preparação básica e primeiro contato com Gwent.",
    },
    {
        "id": "vizima",
        "title": "Palácio Real de Vizima",
        "en": "Royal Palace of Vizima",
        "summary": "Audiência com Emhyr e simulação do save de The Witcher 2.",
    },
    {
        "id": "velen",
        "title": "Velen",
        "en": "Velen",
        "summary": "Barão Sanguinário, Keira Metz, contratos e primeiros grandes blocos livres.",
    },
    {
        "id": "novigrad",
        "title": "Novigrad",
        "en": "Novigrad",
        "summary": "Triss, Dandelion, cadeia política, torneios, corridas e Gwent.",
    },
    {
        "id": "skellige",
        "title": "Skellige",
        "en": "Skellige",
        "summary": "Sucessão do trono, aliados, contratos e fechamento do baralho.",
    },
    {
        "id": "kaer_morhen",
        "title": "Kaer Morhen e a preparação",
        "en": "Kaer Morhen and preparation",
        "summary": "A Maldição de Uma, aliados e auditoria antes da Ilha das Brumas.",
    },
    {
        "id": "isle_of_mists",
        "title": "Ilha das Brumas",
        "en": "The Isle of Mists",
        "summary": "Ponto de corte principal. Parte das missões secundárias já precisa estar encerrada.",
    },
    {
        "id": "post_kaer_morhen",
        "title": "Depois da batalha de Kaer Morhen",
        "en": "After the Battle of Kaer Morhen",
        "summary": "Último ato, Preparativos Finais e fechamento da cadeia de Radovid.",
    },
    {
        "id": "endgame",
        "title": "Fim da campanha e limpeza",
        "en": "Endgame and cleanup",
        "summary": "Contratos, exploração, nível 35 e desafios de combate que ainda estiverem abertos.",
    },
]

REGIONS = [
    {"id": "white_orchard", "title": "Pomar Branco", "en": "White Orchard"},
    {"id": "vizima", "title": "Vizima", "en": "Vizima"},
    {"id": "velen", "title": "Velen", "en": "Velen"},
    {"id": "novigrad", "title": "Novigrad e Oxenfurt", "en": "Novigrad and Oxenfurt"},
    {"id": "skellige", "title": "Skellige", "en": "Skellige"},
    {"id": "kaer_morhen", "title": "Kaer Morhen", "en": "Kaer Morhen"},
    {"id": "global", "title": "Objetivos globais", "en": "Global objectives"},
]

TASKS = [
    {
        "id": "start_death_march",
        "region": "white_orchard",
        "phase": "white_orchard",
        "title": "Comece na Marcha da Morte",
        "en": "Start on Death March",
        "summary": "Escolha Marcha da Morte ao criar a campanha e não reduza a dificuldade.",
        "detail": "No menu do jogo, confirme a dificuldade de combate antes de sair do tutorial e depois de qualquer alteração de opções. A dificuldade de Gwent é uma configuração separada e pode ser reduzida sem mexer na Marcha da Morte.",
        "tags": ["necessária", "perdível"],
        "trophies": ["walked_path", "ran_gauntlet", "passed_trial"],
    },
    {
        "id": "white_orchard_power",
        "region": "white_orchard",
        "phase": "white_orchard",
        "title": "Ative os cinco tipos de Local de Poder",
        "en": "Activate all five Place of Power types",
        "summary": "Pomar Branco tem seis pedras e cinco tipos de Sinal. Abra o mapa abaixo e ative Aard, Igni, Axii, Quen e Yrden na mesma volta.",
        "detail": "Encontrar as pedras não basta: absorva o poder de cada uma. Limpe os inimigos antes de iniciar a volta. O troféu exige os cinco bônus simultâneos, não só cinco visitas registradas. O segundo Quen não é necessário.",
        "tags": ["necessária", "exploração"],
        "trophies": ["power_overwhelming"],
    },
    {
        "id": "simulate_letho",
        "region": "vizima",
        "phase": "vizima",
        "title": "Na simulação, confirme que Letho está vivo",
        "en": "Keep Letho alive in the simulated save",
        "summary": "A resposta abre uma missão e permite convidar Letho para Kaer Morhen.",
        "detail": "Letho não é exigido por Rapaziada, mas esta configuração libera mais conteúdo sem colocar a platina em risco. As outras respostas podem seguir sua preferência.",
        "tags": ["útil", "spoiler"],
        "spoiler": "A missão liberada é A Queda da Casa de Reardon (The Fall of the House of Reardon), seguida por Fantasmas do Passado (Ghosts of the Past). Ao terminar, convide Letho para Kaer Morhen.",
        "trophies": [],
    },
    {
        "id": "keira_chain",
        "region": "velen",
        "phase": "velen",
        "deadline": "isle_of_mists",
        "title": "Conclua toda a trama de Keira Metz",
        "en": "Complete Keira Metz's subplot",
        "summary": "Faça o convite, Uma Torre Cheia de Ratos, Um Favor para uma Amiga e Pelo Avanço da Ciência.",
        "detail": "Na conversa final, convença Keira a ir para Kaer Morhen. Não a mate e não permita que ela procure Radovid.",
        "tags": ["necessária", "perdível", "spoiler"],
        "spoiler": "Pergunte sobre as anotações, diga que Radovid nunca esquece, explique que o plano é suicídio e proponha Kaer Morhen. Essa é a única saída segura para Rapaziada.",
        "trophies": ["friends_benefits", "full_crew"],
    },
    {
        "id": "roche_ves",
        "region": "novigrad",
        "phase": "novigrad",
        "deadline": "isle_of_mists",
        "title": "Conclua Olho por Olho e mantenha Ves viva",
        "en": "Complete An Eye for an Eye and keep Ves alive",
        "summary": "A missão prepara Roche e Ves para o recrutamento em Irmãos de Armas.",
        "detail": "Durante a batalha, proteja Ves. Depois, peça ajuda a Roche quando Irmãos de Armas: Novigrad estiver disponível.",
        "tags": ["necessária", "perdível"],
        "trophies": ["full_crew", "assassin_kings"],
    },
    {
        "id": "triss_subplot",
        "region": "novigrad",
        "phase": "novigrad",
        "deadline": "isle_of_mists",
        "title": "Conclua a trama de Triss em Novigrad",
        "en": "Complete Triss's Novigrad subplot",
        "summary": "Faça Uma Questão de Vida ou Morte e Agora ou Nunca antes da Ilha das Brumas.",
        "detail": "A escolha romântica é livre. Triss participa da defesa de Kaer Morhen sem exigir romance, desde que sua trama seja concluída.",
        "tags": ["necessária", "perdível", "spoiler"],
        "spoiler": "Você pode deixá-la partir ou pedir que fique. A decisão muda o romance, não a obtenção de Rapaziada.",
        "trophies": ["full_crew"],
    },
    {
        "id": "skellige_ruler",
        "region": "skellige",
        "phase": "skellige",
        "deadline": "isle_of_mists",
        "title": "Escolha um governante para Skellige",
        "en": "Choose Skellige's ruler",
        "summary": "Conclua Possessão e O Senhor de Undvik, depois ajude Cerys ou Hjalmar em A Aposta do Rei.",
        "detail": "Não abandone os dois durante A Aposta do Rei. Depois da Coroação, Hjalmar poderá integrar o grupo de Kaer Morhen.",
        "tags": ["necessária", "perdível", "spoiler"],
        "spoiler": "Ajude Cerys ou Hjalmar e conclua a Coroação. Assim você preserva Realeza e o recrutamento de Hjalmar.",
        "trophies": ["kingmaker", "full_crew"],
    },
    {
        "id": "recruit_core_allies",
        "region": "global",
        "phase": "kaer_morhen",
        "deadline": "isle_of_mists",
        "title": "Recrute os sete aliados exigidos",
        "en": "Recruit the seven required allies",
        "summary": "Keira, Triss, Roche, Ves, Zoltan, Ermion e Hjalmar precisam estar garantidos.",
        "detail": "Em Velen, envie Keira para Kaer Morhen. Em Novigrad, conclua Agora ou Nunca para Triss, Olho por Olho para Roche e Ves e fale com Zoltan. Em Skellige, finalize a Coroação e convide Hjalmar, depois fale com Ermion. Use Irmãos de Armas para fazer os convites disponíveis. Letho, Vigi e Folan podem ajudar, mas não são exigidos pelo troféu.",
        "tags": ["necessária", "perdível"],
        "trophies": ["full_crew"],
    },
    {
        "id": "assassination_setup",
        "region": "novigrad",
        "phase": "novigrad",
        "deadline": "isle_of_mists",
        "title": "Prepare a cadeia do assassinato de Radovid",
        "en": "Prepare the Radovid assassination chain",
        "summary": "Conclua Olho por Olho, O Mais Procurado da Redânia e Uma Conspiração Mortal antes da Ilha das Brumas.",
        "detail": "Essas missões mantêm disponível a continuação política no último ato.",
        "tags": ["necessária", "perdível", "spoiler"],
        "spoiler": "O troféu exige participar da missão Razão de Estado (Reason of State). A cadeia ainda possui uma escolha crítica em Cegamente Óbvio.",
        "trophies": ["assassin_kings"],
    },
    {
        "id": "blindingly_obvious_safe",
        "region": "novigrad",
        "phase": "post_kaer_morhen",
        "title": "Não use força contra Dijkstra em Cegamente Óbvio",
        "en": "Do not use force on Dijkstra in Blindingly Obvious",
        "summary": "Escolha a conversa diplomática e entregue informação sobre os planos de Emhyr.",
        "detail": "A opção de empurrar Dijkstra à força encerra a cadeia e impede Razão de Estado.",
        "tags": ["necessária", "perdível", "spoiler"],
        "spoiler": "Escolha a alternativa equivalente a dizer que Dijkstra valoriza informações. Não escolha Empurre Dijkstra para o lado. À força.",
        "trophies": ["assassin_kings"],
    },
    {
        "id": "woodland_spirit_choice",
        "region": "skellige",
        "phase": "skellige",
        "title": "Em No Coração da Floresta, siga Sven",
        "en": "Side with Sven in In the Heart of the Woods",
        "summary": "A solução de Sven leva ao confronto exigido por Espírito do bosque.",
        "detail": "Apoiar Harald resolve a missão sem a luta necessária para o troféu.",
        "tags": ["necessária", "perdível", "spoiler"],
        "spoiler": "Aceite eliminar o leshen e conclua todas as etapas da rota de Sven.",
        "trophies": ["woodland_spirit"],
    },
    {
        "id": "even_odds_two_contracts",
        "region": "global",
        "phase": "velen",
        "title": "Reserve dois contratos para O que é justo, é justo",
        "en": "Reserve two contracts for Even Odds",
        "summary": "Mate dois alvos de contrato sem Sinais, poções, mutagênicos, óleos ou bombas.",
        "detail": "Antes de cada luta final, remova mutagênicos e confirme que não há óleo na espada. Use somente espada, esquiva, bloqueio e besta. Faça um save antes do primeiro alvo.",
        "tags": ["necessária", "perdível"],
        "trophies": ["even_odds"],
    },
    {
        "id": "all_contracts",
        "region": "global",
        "phase": "endgame",
        "title": "Conclua todos os contratos do jogo base",
        "en": "Complete every base-game witcher contract",
        "summary": "Marque os 25 contratos na aba Regiões: 11 em Velen, 8 em Novigrad e 6 em Skellige.",
        "detail": "Poço do Diabo, em Pomar Branco, pode ser feito por experiência, mas não é exigido por Geralt: bruxo profissional nas versões atuais. Contratos das expansões também não contam. Confirme a conclusão no diário, não apenas a morte do monstro.",
        "tags": ["necessária"],
        "trophies": ["professional", "shrieker", "vampire_slayer", "fiend_foe", "ashes", "doppler"],
    },
    {
        "id": "vegelbud_races",
        "region": "novigrad",
        "phase": "novigrad",
        "title": "Vença as três corridas do Derby Vegelbud antes do baile",
        "en": "Win the three Vegelbud Derby races before the ball",
        "summary": "Leia o aviso do Derby e procure a pista fora da propriedade Vegelbud. Vença as três disputas antes de Uma Questão de Vida ou Morte.",
        "detail": "As vitórias liberam o convite de Cleaver para o Páreo de Palio. Faça essa corrida também assim que surgir. Essas quatro provas são a parte de Novigrad de A todo gás.",
        "tags": ["necessária", "perdível"],
        "trophies": ["fast_furious"],
    },
    {
        "id": "doppler_chase",
        "region": "novigrad",
        "phase": "novigrad",
        "title": "Não deixe o dúplice fugir em Ladrão Esquivo",
        "en": "Do not let the doppler escape in An Elusive Thief",
        "summary": "Pegue o contrato na Praça do Hierarca, investigue o ladrão e alcance-o durante a perseguição. Se ele escapar, o contrato e o troféu podem falhar.",
        "detail": "Após alcançá-lo, vença o combate e volte ao contratante para fechar o diário. A escolha final de matar ou poupar não altera o troféu.",
        "tags": ["necessária", "perdível", "spoiler"],
        "spoiler": "Poupar rende coroas e um diagrama. Matar permite saquear o mutagênico e o troféu de monstro. As duas escolhas preservam Dois é demais.",
        "trophies": ["doppler", "professional"],
    },
    {
        "id": "all_races",
        "region": "global",
        "phase": "novigrad",
        "deadline": "isle_of_mists",
        "title": "Vença todas as corridas antes de avançar demais em Novigrad",
        "en": "Win every horse race",
        "summary": "Vença 11 corridas: três no Poleiro do Corvo, três no Derby Vegelbud, o Páreo de Palio e quatro em Skellige.",
        "detail": "Em Skellige, vença as três seletivas de A Perseguição dos Heróis e a final contra Astrid. Em Novigrad, termine as três corridas de Vegelbud antes de Uma Questão de Vida ou Morte e aceite o Páreo de Palio quando Cleaver convidar. Faça save antes de cada final.",
        "tags": ["necessária", "perdível"],
        "trophies": ["fast_furious"],
    },
    {
        "id": "all_brawls",
        "region": "global",
        "phase": "skellige",
        "title": "Conclua as três sequências de luta",
        "en": "Complete all fistfight quest lines",
        "summary": "Feche as lutas de Velen, Novigrad e Skellige, incluindo Olaf.",
        "detail": "Garanta Na raça antes de terminar todas as lutas de punhos: escolha um adversário inicial, esquive sem levar golpes e vença. Assim você não depende de encontrar outra luta válida depois.",
        "tags": ["necessária", "perdível"],
        "trophies": ["brawl_master", "brawler", "south_star"],
    },
    {
        "id": "skellige_nests",
        "region": "skellige",
        "phase": "skellige",
        "title": "Destrua todos os ninhos de monstros de Skellige",
        "en": "Destroy every monster nest in Skellige",
        "summary": "Dedetização exige todos os cinco ninhos de Skellige ou todos os de Velen e Novigrad.",
        "detail": "Use bombas em todos. Para Bomba, bomba, olha a bomba!, destrua mais cinco ninhos em Velen ou Novigrad: os cinco de Skellige não bastam.",
        "tags": ["necessária", "exploração"],
        "trophies": ["pest_control"],
    },
    {
        "id": "ten_nests",
        "region": "global",
        "phase": "endgame",
        "title": "Destrua dez ninhos com bombas no total",
        "en": "Destroy ten monster nests with bombs in total",
        "summary": "Depois dos cinco ninhos de Skellige, complete a contagem em Velen ou Novigrad.",
        "detail": "Este troféu é separado de Dedetização. Conte dez ninhos destruídos com bombas, não apenas dez ícones descobertos.",
        "tags": ["necessária", "exploração"],
        "trophies": ["fire_hole"],
    },
    {
        "id": "witcher_gear_set",
        "region": "global",
        "phase": "endgame",
        "title": "Encontre e equipe um conjunto completo de bruxo",
        "en": "Find and equip one complete witcher gear set",
        "summary": "Escolha uma escola e complete somente a caça ao tesouro necessária para espada de aço, espada de prata, armadura, luvas, calças e botas do mesmo conjunto.",
        "detail": "Não é preciso fabricar todos os conjuntos. Griffin é uma escolha natural para quem usa Sinais; Gato e Urso atendem estilos diferentes.",
        "tags": ["necessária"],
        "trophies": ["armed_dangerous"],
    },
    {
        "id": "combat_cleanup",
        "region": "global",
        "phase": "endgame",
        "title": "Feche os desafios acumulativos de combate",
        "en": "Finish cumulative combat challenges",
        "summary": "Use oportunidades naturais durante a campanha e deixe apenas a limpeza final para depois.",
        "detail": "Os mais demorados são Atirador de elite, Exagero, O inimigo do meu inimigo, Sai de baixo e Maldade pouca é bobagem.",
        "tags": ["necessária"],
        "trophies": ["enemy_enemy", "humpty_dumpty", "environmental", "evilest_thing", "overkill", "master_marksman"],
    },
]

GWENT_TASKS = [
    {
        "id": "teacher_white_orchard",
        "region": "white_orchard",
        "title": "Aprenda Gwent com o estudioso da taverna",
        "en": "Learn Gwent from the tavern scholar",
        "summary": "Jogue e vença a partida inicial. Em versões atuais há rota alternativa para a carta, mas resolver aqui é mais simples.",
        "detail": "A recompensa é Zoltan Chivay. Se você já saiu de Pomar Branco sem ganhá-la, procure a carta sob a Árvore dos Enforcados em Velen. Mesmo com essa saída, aprenda a jogar cedo para começar a coleção.",
        "tags": ["necessária", "útil"],
    },
    {
        "id": "buy_white_orchard",
        "region": "white_orchard",
        "title": "Compre todas as cartas da taverna de Pomar Branco",
        "en": "Buy every card sold at the White Orchard inn",
        "summary": "Confira o estoque da estalajadeira antes de deixar a região. Se ela já saiu, procure o comerciante próximo à ponte.",
        "tags": ["necessária"],
    },
    {
        "id": "vizima_noble",
        "region": "vizima",
        "title": "Derrote o nobre nilfgaardiano em Vizima",
        "en": "Defeat the Nilfgaardian nobleman in Vizima",
        "summary": "Ele fica no pátio do palácio e concede Foltest: The Siegemaster. Se o baralho inicial for fraco, você pode voltar depois.",
        "tags": ["necessária"],
    },
    {
        "id": "velen_players",
        "region": "velen",
        "title": "Conclua Gwent: Jogadores de Velen",
        "en": "Complete Gwent: Velen Players",
        "summary": "Vença o Barão Sanguinário, Haddy em Midcopse, o barqueiro de Oreton e o sábio de Benek.",
        "detail": "Confira as recompensas: Sigismund Dijkstra, Vernon Roche, Letho of Gulet, Crone: Weavess e o líder Eredin: Destroyer of Worlds. Se o Barão sair de cena, procure a carta no escritório dele no Poleiro do Corvo.",
        "tags": ["necessária", "perdível"],
    },
    {
        "id": "claywich_merchant",
        "region": "velen",
        "title": "Liberte o comerciante preso e compre suas cartas em Claywich",
        "en": "Rescue the captive merchant and buy his cards in Claywich",
        "summary": "O comerciante está em uma Pessoa em Perigo numa ilha a leste de Oreton. Depois do resgate, encontre-o em Claywich durante o dia.",
        "tags": ["necessária", "perdível"],
    },
    {
        "id": "playing_innkeeps",
        "region": "novigrad",
        "title": "Conclua Gwent: Jogando com Estalajadeiros",
        "en": "Complete Gwent: Playing Innkeeps",
        "summary": "Jogue com o estalajadeiro da Encruzilhada, Stjepan em Oxenfurt e Olivier no Martim-pescador.",
        "detail": "As cartas da cadeia são Menno Coehoorn, Yennefer of Vengerberg e Tibor Eggebracht. Se Olivier já não estiver no local, procure a carta no quarto junto ao bar.",
        "tags": ["necessária"],
    },
    {
        "id": "big_city_players",
        "region": "novigrad",
        "title": "Conclua Gwent: Grandes Jogadores da Cidade",
        "en": "Complete Gwent: Big City Players",
        "summary": "Vivaldi, Marquise Serenity, Dijkstra e o comerciante scoia'tael formam a cadeia.",
        "detail": "Confirme Vesemir, Morvran Voorhis, Esterad Thyssen, Cirilla Fiona Elen Riannon e o líder Francesca Findabair: The Beautiful ao concluir a missão.",
        "tags": ["necessária", "perdível"],
    },
    {
        "id": "matter_life_death_tournament",
        "region": "novigrad",
        "title": "Vença as três partidas no baile de Uma Questão de Vida ou Morte",
        "en": "Win all three matches during A Matter of Life and Death",
        "summary": "O torneio está numa área lateral do baile. Termine as três partidas antes de seguir a missão.",
        "tags": ["necessária", "perdível", "spoiler"],
        "spoiler": "As recompensas incluem Milva, Bruxa Vampira e Dandelion. Sair do baile sem vencê-las falha a coleta.",
    },
    {
        "id": "dangerous_game_cards",
        "region": "novigrad",
        "title": "Em Um Jogo Perigoso, escolha as cartas como recompensa",
        "en": "Choose the cards as the reward in A Dangerous Game",
        "summary": "A recompensa segura para a coleção são as três cartas, não o dinheiro.",
        "tags": ["necessária", "perdível", "spoiler"],
        "spoiler": "As cartas são Fringilla Vigo, Isengrim Faoiltiarna e John Natalis.",
    },
    {
        "id": "old_pals",
        "region": "novigrad",
        "title": "Conclua Gwent: Velhos Amigos e jogue com Lambert",
        "en": "Complete Gwent: Old Pals and play Lambert",
        "summary": "Jogue contra Zoltan, Roche, Lambert e Thaler. Não deixe Lambert para depois da Ilha das Brumas.",
        "detail": "Confirme Eithné, Saesenthessis, Triss Merigold e Geralt of Rivia. Lambert pode ser encontrado durante Seguindo o Fio ou mais tarde em Kaer Morhen; Thaler fica na Estalagem dos Sete Gatos.",
        "tags": ["necessária", "perdível"],
    },
    {
        "id": "high_stakes",
        "region": "novigrad",
        "title": "Prepare um baralho forte e vença Grandes Apostas",
        "en": "Build a strong deck and win High Stakes",
        "summary": "Faça um save manual antes de entrar. Vença as quatro partidas do torneio no Passiflora.",
        "detail": "As quatro recompensas são os líderes Foltest: The Steel-Forged, Emhyr var Emreis: The Relentless, Francesca Findabair: Queen of Dol Blathanna e Eredin: Bringer of Death. Se perder uma partida, carregue o save anterior.",
        "tags": ["necessária", "perdível"],
    },
    {
        "id": "skellige_style",
        "region": "skellige",
        "title": "Conclua Gwent: Estilo de Skellige",
        "en": "Complete Gwent: Skellige Style",
        "summary": "Vença Crach, Ermion, Gremist, Lugos e Sjusta antes de seguir a história.",
        "detail": "Confira Draug, Leshen, Mysterious Elf, Vampire: Katakan, Yaevinn e o líder Emhyr var Emreis: The White Flame ao concluir a missão.",
        "tags": ["necessária", "perdível"],
    },
    {
        "id": "shock_therapy",
        "region": "skellige",
        "title": "Conclua Terapia de Choque",
        "en": "Complete Shock Therapy",
        "summary": "A recompensa é a carta Iorveth, necessária para a coleção do jogo base.",
        "tags": ["necessária", "perdível"],
    },
    {
        "id": "following_thread_nekker",
        "region": "skellige",
        "title": "Em Seguindo o Fio, saqueie o corpo de Hammond",
        "en": "Loot Hammond during Following the Thread",
        "summary": "A missão de Lambert começa em Novigrad e leva a Faroe, em Skellige. Pegue a carta Nekker no corpo de Hammond antes de sair.",
        "detail": "Ela é uma das cópias de Nekker. A missão pode falhar com o avanço da história e o corpo pode desaparecer; confira a carta no inventário antes de encerrar a etapa.",
        "tags": ["necessária", "perdível"],
    },
    {
        "id": "merchant_cards",
        "region": "global",
        "title": "Compre as cartas dos vendedores pelo caminho",
        "en": "Buy cards from vendors along the way",
        "summary": "Use os 18 pontos de venda de referência listados nesta aba. Confira também qualquer outra loja que encontrar.",
        "detail": "A lista mostra até 76 ofertas de referência, incluindo cópias repetidas. O estoque pode variar por versão e algumas cartas já podem estar no baralho inicial. Para Colecionador de cartas, basta um exemplar de cada tipo, mas comprar tudo evita procurar depois.",
        "tags": ["necessária"],
    },
    {
        "id": "random_pool",
        "region": "global",
        "title": "Esgote o conjunto de cartas aleatórias",
        "en": "Exhaust the random card reward pool",
        "summary": "Vença comerciantes, ferreiros, armeiros e herbalistas novos até o Guia Milagroso indicar zero cartas de jogadores sem renome.",
        "detail": "O oponente comum entrega carta aleatória só na primeira vitória. Quando a recompensa deixar de ser carta, passe ao próximo. A lista de vendedores cobre compras, mas não substitui essas vitórias.",
        "tags": ["necessária"],
    },
    {
        "id": "final_audit",
        "region": "global",
        "title": "Faça a auditoria final antes da Ilha das Brumas",
        "en": "Run the final audit before The Isle of Mists",
        "summary": "Abra o Guia Milagroso de Gwent. Só marque este bloco quando cada região e os jogadores sem renome estiverem em zero.",
        "detail": "Confirme também todas as recompensas de missões, o baile de Vegelbud, Grandes Apostas, Seguindo o Fio e as 18 lojas. Se o livro ainda indicar cartas, não navegue para a Ilha das Brumas.",
        "tags": ["necessária", "perdível"],
    },
    {
        "id": "geralt_and_friends",
        "region": "global",
        "title": "Vença uma rodada usando apenas cartas neutras",
        "en": "Win a round using only neutral cards",
        "summary": "Monte a rodada com cartas neutras já obtidas e faça isso contra um oponente fraco. Cartas de facção jogadas em outras rodadas não invalidam o troféu.",
        "tags": ["necessária"],
    },
    {
        "id": "all_in",
        "region": "global",
        "title": "Use três cartas de herói na mesma rodada e vença a partida",
        "en": "Play three hero cards in one round and win the match",
        "summary": "Guarde três heróis na mão, use os três na mesma rodada e confirme a vitória da partida, não apenas da rodada.",
        "tags": ["necessária"],
    },
]

# Os 25 contratos exigidos por Geralt: bruxo profissional após o patch 1.07.
# Poço do Diabo, em Pomar Branco, é útil, mas não é exigido por esse troféu.
# Os nomes de missão em inglês servem como identificadores inequívocos, pois a
# tradução do diário pode variar entre as edições do jogo.
CONTRACTS = [
    {"id": "jenny_woods", "region": "velen", "en": "Jenny o' the Woods"},
    {"id": "missing_brother", "region": "velen", "en": "Missing Brother"},
    {"id": "mysterious_tracks", "region": "velen", "en": "Mysterious Tracks"},
    {"id": "patrol_gone_missing", "region": "velen", "en": "Patrol Gone Missing"},
    {"id": "phantom_trade_route", "region": "velen", "en": "Phantom of the Trade Route"},
    {"id": "shrieker", "region": "velen", "en": "Shrieker"},
    {"id": "swamp_thing", "region": "velen", "en": "Swamp Thing"},
    {"id": "griffin_highlands", "region": "velen", "en": "The Griffin from the Highlands"},
    {"id": "merry_widow", "region": "velen", "en": "The Merry Widow"},
    {"id": "byways_murders", "region": "velen", "en": "The Mystery of the Byways Murders"},
    {"id": "woodland_beast", "region": "velen", "en": "Woodland Beast"},
    {"id": "deadly_delights", "region": "novigrad", "en": "Deadly Delights"},
    {"id": "doors_slamming", "region": "novigrad", "en": "Doors Slamming Shut"},
    {"id": "elusive_thief", "region": "novigrad", "en": "An Elusive Thief"},
    {"id": "lord_wood", "region": "novigrad", "en": "Lord of the Wood"},
    {"id": "oxenfurt_drunk", "region": "novigrad", "en": "The Oxenfurt Drunk"},
    {"id": "apiarian_phantom", "region": "novigrad", "en": "The Apiarian Phantom"},
    {"id": "oxenfurt_forest", "region": "novigrad", "en": "The Creature from Oxenfurt Forest"},
    {"id": "white_lady", "region": "novigrad", "en": "The White Lady"},
    {"id": "dragon", "region": "skellige", "en": "Dragon"},
    {"id": "here_comes_groom", "region": "skellige", "en": "Here Comes the Groom"},
    {"id": "missing_son", "region": "skellige", "en": "Missing Son"},
    {"id": "muire_dyaeblen", "region": "skellige", "en": "Muire D'yaeblen"},
    {"id": "phantom_eldberg", "region": "skellige", "en": "The Phantom of Eldberg"},
    {"id": "strange_beast", "region": "skellige", "en": "Strange Beast"},
]

SKIPPABLE_BY_REGION = {
    "white_orchard": (
        "Não é preciso limpar todos os pontos de interrogação. Priorize os Locais de Poder, "
        "as cartas da taverna e recursos suficientes para atravessar o início na Marcha da Morte."
    ),
    "vizima": (
        "Não há varredura de colecionáveis para a platina. Resolva o jogador de Gwent e escolha "
        "a simulação de Letho se quiser manter todo o conteúdo opcional disponível."
    ),
    "velen": (
        "A maioria dos tesouros e pontos de interrogação pode ficar para trás. Não pule a trama "
        "de Keira, os contratos do jogo base, as corridas e os jogadores de Gwent indicados."
    ),
    "novigrad": (
        "Missões secundárias não listadas são opcionais para troféus, mas rendem experiência. "
        "As cadeias de Triss, Roche, Radovid, corridas e Gwent não entram nessa dispensa."
    ),
    "skellige": (
        "Os muitos pontos no mar não são exigidos. Skellige é uma boa região para Dedetização: "
        "destrua todos os ninhos daqui e não será necessário limpar também Velen e Novigrad."
    ),
    "kaer_morhen": (
        "Não existe exigência de limpar o mapa. O que importa é chegar à Ilha das Brumas com "
        "os aliados, as missões perdíveis e a auditoria de Gwent já resolvidos."
    ),
    "global": (
        "As expansões, seus contratos, cartas e troféus não entram nesta platina. Caças ao "
        "tesouro são opcionais, salvo a linha de um conjunto completo de equipamento de bruxo."
    ),
}

GATES = [
    # Os seis pontos sem volta da campanha base, mais os dois prazos de carta que
    # não são missão principal. "fails" é o que morre exatamente ali, escrito por
    # extenso e com o nome em inglês ao lado, porque é a razão de o guia existir.
    {
        "id": "leave_white_orchard",
        "phase": "white_orchard",
        "title": "Antes da Audiência Imperial (Imperial Audience)",
        "summary": "Terminar essa missão tira você de Pomar Branco e derruba quase todas as secundárias da região.",
        "required": [
            "task:start_death_march",
            "gwent:teacher_white_orchard",
            "gwent:buy_white_orchard",
        ],
        "fails": [
            "Uma Frigideira Limpinha (A Frying Pan, Spick and Span)",
            "Desaparecido em Combate (Missing in Action)",
            "No Leito de Morte (On Death's Bed)",
            "Carga Preciosa (Precious Cargo)",
            "Incendiário Perverso (Twisted Firestarter)",
        ],
        "safe": (
            "Amigo Fiel (Faithful Friend) é a única secundária de Pomar Branco que "
            "sobrevive a este corte. O contrato O Diabo do Poço (Devil by the Well) "
            "também continua vivo: dá para voltar a Pomar Branco depois, e ele só "
            "morre no fim da campanha, em Gelo Fino."
        ),
    },
    {
        "id": "ugly_baby_checkpoint",
        "phase": "velen",
        "title": "Antes de Bebê Feio (Ugly Baby)",
        "summary": "Corte curto, mas definitivo: duas missões somem quando essa principal avança.",
        "required": [],
        "fails": [
            "Seguindo o Rastro (Following the Thread)",
            "O Último Desejo (The Last Wish), e com ela a linha romântica da Yennefer",
        ],
        "safe": "Feche as duas antes de levar a Uma para Kaer Morhen.",
    },
    {
        "id": "vegelbud_ball_checkpoint",
        "phase": "novigrad",
        "title": "Antes de sair da propriedade dos Vegelbud",
        "summary": "Três cartas de Gwent existem só aqui dentro, no torneio do baile, e não têm segunda fonte.",
        "required": [
            "gwent:matter_life_death_tournament",
            "task:vegelbud_races",
        ],
        "fails": [
            "Carta Dandelion (Jaskier)",
            "Carta Milva",
            "Carta Vampiro: Bruxa (Vampire: Bruxa)",
        ],
        "safe": (
            "As três saem de vencer os oponentes do torneio durante Uma Questão de "
            "Vida ou Morte (A Matter of Life and Death). Quando você sai da "
            "propriedade elas desaparecem para sempre: não há loja, saque ou missão "
            "que as devolva. Salve antes de entrar no baile. Resolva também as "
            "corridas da propriedade nesta mesma ida."
        ),
    },
    {
        "id": "high_stakes_checkpoint",
        "phase": "novigrad",
        "title": "Antes e durante Grandes Apostas (High Stakes)",
        "summary": "As quatro cartas de líder do torneio não têm segunda chance, e perder uma partida encerra tudo.",
        "required": [
            "gwent:playing_innkeeps",
            "gwent:big_city_players",
        ],
        "fails": [
            "Foltest: O Forjado em Aço, de vencer Bernard Tulle",
            "Emhyr var Emreis: O Implacável, de vencer a Madame Sasha",
            "Francesca Findabair: Rainha de Dol Blathanna, de vencer Finneas",
            "Eredin: Portador da Morte, de vencer o Conde Tybalt",
        ],
        "safe": (
            "Perder uma partida falha o torneio e as cartas que faltavam ficam "
            "inalcançáveis. Salve manualmente entre cada rodada e entre com um "
            "baralho montado, nunca com o inicial. O troféu Mestre do Gwent depende "
            "de vencer o Tybalt no fim."
        ),
    },
    {
        "id": "isle_of_mists_checkpoint",
        "phase": "kaer_morhen",
        "title": "Antes de navegar para a Ilha das Brumas (The Isle of Mists)",
        "summary": "O maior corte do jogo inteiro. Faça um save manual separado, com nome, antes de embarcar.",
        "required": [
            "task:keira_chain",
            "task:roche_ves",
            "task:triss_subplot",
            "task:skellige_ruler",
            "task:recruit_core_allies",
            "task:assassination_setup",
            "task:all_races",
            "gwent:matter_life_death_tournament",
            "gwent:dangerous_game_cards",
            "gwent:old_pals",
            "gwent:skellige_style",
            "gwent:shock_therapy",
            "gwent:following_thread_nekker",
            "gwent:final_audit",
        ],
        "fails": [
            "Toda a linha da Keira Metz: Um Convite de Keira Metz, Uma Torre Cheia de Ratos, Um Favor para uma Amiga, Pelo Avanço do Conhecimento e Lâmpada Mágica",
            "O Quarto de Ciri (Ciri's Room)",
            "A Queda da Casa Reardon (The Fall of the House of Reardon)",
            "Fantasmas do Passado (Ghosts of the Past)",
            "Retorno ao Pântano Retorcido (Return to Crookback Bog)",
            "Uma Questão de Vida ou Morte (A Matter of Life and Death) e Agora ou Nunca (Now or Never)",
            "A linha do assassinato inteira: Um Plano Mortal (A Deadly Plot), Olho por Olho (An Eye for an Eye) e Os Mais Procurados da Redânia (Redania's Most Wanted)",
            "Um Jogo Perigoso (A Dangerous Game), a missão de Gwent do Zoltan",
            "Cabaré (Cabaret), Pecados Carnais (Carnal Sins), Aulas de Esgrima (Fencing Lessons) e A Espada de Berengar (Berengar's Blade)",
        ],
        "safe": (
            "Dois troféus morrem aqui se você embarcar cedo demais. Tripulação "
            "Completa (Full Crew) exige os aliados já recrutados, e Assassino de "
            "Reis (Assassin of Kings) depende da linha do assassinato inteira: sem "
            "ela, Razão de Estado nunca chega a existir."
        ),
    },
    {
        "id": "kings_gambit_checkpoint",
        "phase": "skellige",
        "title": "Antes do Gambito do Rei (King's Gambit)",
        "summary": "Começar essa missão derruba duas secundárias de Skellige na hora.",
        "required": [],
        "fails": [
            "Estranho em Terra Estranha (Stranger in a Strange Land)",
            "A Caverna dos Sonhos (The Cave of Dreams)",
        ],
        "safe": "Feche as duas antes de aceitar o convite do banquete em Kaer Trolde.",
    },
    {
        "id": "battle_preparations_checkpoint",
        "phase": "kaer_morhen",
        "title": "Antes dos Preparativos de Batalha (Battle Preparations)",
        "summary": "Último corte de Skellige. Depois daqui não se volta para resolver a ilha.",
        "required": ["task:skellige_ruler"],
        "fails": [
            "O Senhor de Undvik (The Lord of Undvik)",
            "Possessão (Possession)",
            "Gambito do Rei (King's Gambit)",
            "Coroação (Coronation)",
        ],
        "safe": (
            "São essas quatro que decidem quem senta no trono de Skellige, e o "
            "troféu Fazedor de Reis (Kingmaker) morre junto com elas."
        ),
    },
    {
        "id": "blindingly_obvious_checkpoint",
        "phase": "post_kaer_morhen",
        "title": "Antes e durante Cegamente Óbvio (Blindingly Obvious)",
        "summary": "A última janela da campanha, e ela tem uma escolha de diálogo que vale um troféu.",
        "required": ["task:blindingly_obvious_safe"],
        "fails": [
            "Razão de Estado (Reason of State)",
            "Contrato: O Diabo do Poço (Contract: Devil by the Well), lá em Pomar Branco",
        ],
        "safe": (
            "No fim de Cegamente Óbvio, falando com Dijkstra e Philippa, escolha a "
            "PRIMEIRA opção de diálogo. É ela que mantém Razão de Estado viva, e sem "
            "essa missão não existe o troféu Assassino de Reis. Se o contrato de "
            "Pomar Branco ainda estiver aberto, vá fazer agora: Gelo Fino (On Thin "
            "Ice) é a última chance."
        ),
    },
]

BUILDS = [
    {
        "id": "sword_survival",
        "title": "Espadachim resistente",
        "best_for": "Quem quer um combate direto e previsível.",
        "priorities": [
            "Ataques rápidos e geração de adrenalina",
            "Redução de dano e tolerância a erros",
            "Quen como proteção, sem depender dele para causar dano",
            "Armadura de bruxo compatível com o peso escolhido",
        ],
        "note": "É o estilo mais simples para a primeira campanha: invista primeiro em sobreviver e em dominar esquiva e contra-ataque. Na árvore do Remastered, suba cada habilidade até o nível que destrava a seguinte antes de abrir um ramo novo.",
    },
    {
        "id": "sign_control",
        "title": "Sinais e controle",
        "best_for": "Quem prefere controlar grupos e criar janelas seguras.",
        "priorities": [
            "Recuperação de vigor",
            "Aard e Yrden para controle",
            "Igni para pressão e queimadura",
            "Ataques de espada curtos entre conjurações",
        ],
        "note": "Ajuda em vários troféus de combate, mas precisa ser DESLIGADA nas duas lutas reservadas para O que é justo, é justo: esse troféu exige matar sem Sinais, óleos, poções, bombas nem decocções.",
    },
    {
        "id": "alchemy_hybrid",
        "title": "Alquimia híbrida",
        "best_for": "Quem gosta de preparação, óleos e alta eficiência contra monstros.",
        "priorities": [
            "Toxicidade segura",
            "Poções e decocções adequadas ao alvo",
            "Bombas para controle e ninhos",
            "Dano de espada apoiado por preparação",
        ],
        "note": "É forte em contratos e combina com a fantasia de bruxo. Remova mutagênicos, óleos e consumíveis nas duas lutas de O que é justo, é justo.",
    },
]

HERO_STATS = [
    {"value": "53", "label": "troféus"},
    {"value": "120", "label": "cartas únicas"},
    {"value": "1", "label": "campanha"},
    {"value": "3", "label": "estilos"},
]


# ── O que o Remastered (patch 5.0, 28/09/2026) mudou ──────────────────────
# Importa para o guia porque o jogador chega aqui vindo de material escrito
# para a versao antiga. Tudo abaixo esta nas notas oficiais do patch; o que
# ainda nao da para afirmar com seguranca esta marcado como tal em REMASTER_OPEN.
REMASTER_CHANGES = [
    {
        "title": "A árvore de habilidades foi refeita, e seus pontos foram zerados",
        "detail": (
            "As habilidades agora ficam numa árvore e cada uma tem TRÊS níveis. "
            "Desbloquear uma exige ter as habilidades pré-requisito, em vez de só "
            "acumular pontos investidos. Os valores, efeitos e sinergias foram "
            "rebalanceados e algumas mudaram de nome. Se você tinha um save antigo, "
            "os pontos voltaram para a sua mão para serem redistribuídos."
        ),
        "impact": "Qualquer build escrita antes de 28/09/2026 fala de uma árvore que não existe mais.",
    },
    {
        "title": "Combate dos monstros comuns refeito",
        "detail": (
            "Padrões de ataque, contra-ataques, movimentação, reações e esquiva de "
            "todos os monstros comuns foram revisados. Entrou também uma câmera "
            "dinâmica de combate e uma troca de alvo melhor ao mover a câmera."
        ),
        "impact": "Na Marcha da Morte, o tempo de esquiva que você decorou em vídeo antigo pode não bater.",
    },
    {
        "title": "Recuar do combate virou uma ação",
        "detail": "Segure a esquiva e depois corra para sair de uma luta.",
        "impact": "Saída de emergência real na Marcha da Morte, onde fugir às vezes é a jogada certa.",
    },
    {
        "title": "Reforja de equipamento",
        "detail": (
            "Com a Yoana ou o Hattori dá para mudar a aparência de uma peça sem "
            "mexer nos atributos dela."
        ),
        "impact": "Puramente cosmético, não interfere em troféu.",
    },
    {
        "title": "Coleta montado e meditação sem tela",
        "detail": (
            "Dá para recolher itens sem desmontar do Carpeado, e a meditação passa "
            "o tempo na tela do jogo em vez de abrir uma interface."
        ),
        "impact": "Economiza tempo nas voltas de coleta, que são boa parte desta platina.",
    },
    {
        "title": "O que NÃO mudou: a lista de troféus",
        "detail": (
            "O Remastered é uma atualização gratuita da versão que você já tem, não "
            "um produto novo. Não existe lista de troféus separada, nem platina "
            "nova, e os troféus que você já tinha continuam desbloqueados."
        ),
        "impact": "O guia vale igual para quem começou antes e para quem começa agora.",
    },
]

# Pontos que o patch mexeu e cuja consequencia pratica ainda nao esta clara.
# Preferimos registrar a duvida a inventar recomendacao.
REMASTER_OPEN = (
    "O patch saiu em 28 de setembro de 2026. As notas oficiais dizem que os "
    "valores e as sinergias das habilidades foram rebalanceados, mas não publicam "
    "a árvore nova habilidade por habilidade, e ainda não existe consenso da "
    "comunidade sobre qual distribuição é a melhor. Por isso os três estilos "
    "abaixo falam de PRIORIDADES, não de uma lista fechada de habilidades: "
    "recomendar nomes agora seria chutar. Quando a árvore estiver mapeada, esta "
    "aba ganha as distribuições concretas."
)

def phase_index(phase_id: str) -> int:
    for index, phase in enumerate(PHASES):
        if phase["id"] == phase_id:
            return index
    return 0


def item_by_key(key: str) -> dict | None:
    kind, _, item_id = key.partition(":")
    sources = {"task": TASKS, "gwent": GWENT_TASKS, "gate": GATES}
    for item in sources.get(kind, []):
        if item["id"] == item_id:
            return item
    return None


def phase_title(phase_id: str) -> str:
    """Nome legível de uma fase, para os avisos de portão."""
    for phase in PHASES:
        if phase["id"] == phase_id:
            return phase.get("title") or phase_id
    return phase_id
