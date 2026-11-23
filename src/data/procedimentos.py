"""
Procedimentos e protocolos da Vinovare.

Lista baseada nos tratamentos divulgados em vinovare.com.br (facial, corporal e
capilar). Textos informativos e conservadores: indicação, número de sessões e
resultados são sempre definidos em consulta.
"""

AREAS = {
    'rosto': {
        'nome': 'Rosto',
        'titulo': 'Rejuvenescer com naturalidade',
        'slogan': 'Renovando peles, transformando vidas.',
        'texto': 'Tratamentos para linhas de expressão, flacidez, manchas, textura e contorno, sempre preservando '
                 'a sua identidade. Tecnologias e injetáveis combinados em protocolos individualizados.',
        'img': 'rosto-retrato',
    },
    'corpo': {
        'nome': 'Corpo',
        'titulo': 'Firmeza, contorno e qualidade da pele',
        'slogan': 'Defina seu poder, realce suas curvas.',
        'texto': 'Protocolos para flacidez, gordura localizada, celulite, pós-parto e rejuvenescimento de colo, '
                 'pescoço e mãos — com tecnologia e bioestimulação de colágeno.',
        'img': 'corpo-ombro',
    },
    'cabelo': {
        'nome': 'Cabelo',
        'titulo': 'Medicina capilar com investigação',
        'slogan': 'Dê vida nova ao seu cabelo!',
        'texto': 'Investigação das causas da queda, tricoscopia e protocolos que combinam cuidados em casa, '
                 'drug delivery, exossomas e tecnologias para fios mais fortes.',
        'img': 'cabelo-costas',
    },
}

FAQ_PADRAO = ('Preciso passar por consulta antes?',
              'Sim. Todo tratamento na Vinovare começa com uma avaliação médica integral. É nela que a Dra. Karinie '
              'confirma a indicação, define a técnica, o número de sessões e esclarece cuidados e contraindicações.')

PASSOS_PADRAO = [
    ('Avaliação', 'Consulta integral para entender sua queixa, seu histórico e suas expectativas.'),
    ('Plano sob medida', 'Definição das técnicas, da ordem e do intervalo entre as etapas do protocolo.'),
    ('Tratamento', 'Sessões realizadas pela Dra. Karinie, com conforto e segurança.'),
    ('Acompanhamento', 'Retornos para avaliar a evolução e ajustar o cuidado quando necessário.'),
]


def P(slug, nome, areas, tipo, img, img2, curto, lead, indicacoes, tecnologias, fatos,
      faq=(), passos=None, relacionados=()):
    return {
        'slug': slug, 'nome': nome, 'areas': areas, 'tipo': tipo, 'img': img, 'img2': img2,
        'curto': curto, 'lead': lead, 'indicacoes': indicacoes, 'tecnologias': tecnologias,
        'fatos': fatos, 'faq': list(faq) + [FAQ_PADRAO], 'passos': passos or PASSOS_PADRAO,
        'relacionados': list(relacionados),
    }


PROCEDIMENTOS = [
    # ---------------------------------------------------------------- ROSTO
    P('toxina-botulinica', 'Toxina botulínica', ['rosto'], 'Procedimento', 'toxina-marcacao', 'rosto-retrato',
      'Suaviza linhas de expressão relaxando a musculatura de forma controlada — sem “congelar” o rosto.',
      'A toxina botulínica é um dos procedimentos mais estudados da dermatologia. Aplicada em pontos precisos, '
      'reduz a contração dos músculos responsáveis pelas linhas de expressão, suaviza rugas dinâmicas e ajuda a '
      'prevenir que se aprofundem — com resultado natural, preservando a sua expressão.',
      ['Linhas da testa', 'Rugas entre as sobrancelhas (glabela)', '“Pés de galinha” ao redor dos olhos',
       'Prevenção de rugas dinâmicas', 'Contorno de mandíbula e pescoço (técnica Nefertiti)',
       'Hiperidrose — suor excessivo em axilas, mãos e pés'],
      ['Toxina botulínica tipo A', 'Mapeamento da mímica facial', 'Agulhas ultrafinas'],
      [('Sessão', 'Cerca de 30 minutos'), ('Recuperação', 'Retorno imediato às atividades'),
       ('Início do efeito', '3 a 7 dias, com pico em ~15 dias'), ('Duração média', '4 a 6 meses')],
      [('O resultado fica artificial?',
        'Não precisa ficar. A proposta é suavizar, preservando a expressão. Dose e pontos de aplicação são definidos '
        'de acordo com a sua anatomia, a força muscular e o resultado desejado.'),
       ('Quais cuidados devo ter depois?',
        'Nas primeiras horas, recomenda-se não deitar, não massagear a região e evitar atividade física intensa. '
        'Todas as orientações são passadas por escrito após o procedimento.'),
       ('Quem não pode fazer?',
        'Gestantes, lactantes e pessoas com algumas doenças neuromusculares, entre outras condições, não devem '
        'realizar o procedimento — por isso a avaliação prévia é indispensável.')],
      [('Avaliação da mímica', 'Análise dos movimentos do rosto, da anatomia e das suas expectativas.'),
       ('Planejamento dos pontos', 'Dose e distribuição individualizadas para um resultado natural.'),
       ('Aplicação', 'Microinjeções rápidas com agulhas ultrafinas e desconforto mínimo.'),
       ('Revisão', 'Reavaliação em cerca de 15 dias para ajustes finos, quando necessário.')],
      ['preenchimento-acido-hialuronico', 'rejuvenescimento-periocular', 'skinbooster']),

    P('preenchimento-acido-hialuronico', 'Preenchimento com ácido hialurônico', ['rosto'], 'Procedimento',
      'rosto-retrato', 'labios',
      'Repõe volumes, define contornos e suaviza sulcos com uma molécula naturalmente presente na pele.',
      'O ácido hialurônico é uma molécula presente naturalmente na pele, responsável por hidratação e sustentação. '
      'Com o tempo, sua produção diminui. O preenchimento repõe volumes perdidos, define contornos e suaviza sulcos, '
      'sempre respeitando as proporções e a harmonia do seu rosto.',
      ['Sulcos nasogenianos (“bigode chinês”)', 'Lábios: volume, contorno e hidratação',
       'Olheiras com sulco profundo, após avaliação', 'Maçãs do rosto e têmporas', 'Contorno de mandíbula e queixo',
       'Harmonização do perfil'],
      ['Ácido hialurônico de diferentes densidades', 'Microcânulas', 'Anestésico tópico e local'],
      [('Sessão', '30 a 60 minutos'), ('Recuperação', 'Inchaço leve por alguns dias'),
       ('Resultado', 'Imediato, refinado em cerca de 15 dias'), ('Duração média', '6 a 18 meses, conforme a região')],
      [('O preenchimento é reversível?',
        'O ácido hialurônico pode ser degradado com uma enzima específica (hialuronidase) quando há indicação médica, '
        'o que traz mais segurança ao procedimento.'),
       ('Vou ficar com hematomas?',
        'Pequenos roxos e inchaço podem ocorrer e costumam desaparecer em poucos dias. O uso de microcânulas ajuda a '
        'reduzir esse risco.'),
       ('Preenchimento e bioestimulador são a mesma coisa?',
        'Não. O preenchimento repõe volume de forma imediata; o bioestimulador estimula a produção do seu próprio '
        'colágeno, com efeito gradual. Muitas vezes os dois são combinados.')],
      [('Análise facial', 'Proporções, perda de volume e qualidade da pele.'),
       ('Escolha do produto', 'Densidades diferentes para cada região e objetivo.'),
       ('Aplicação', 'Com cânula ou agulha, associada a anestésico para mais conforto.'),
       ('Revisão', 'Acompanhamento para garantir um resultado harmônico e natural.')],
      ['bioestimuladores-de-colageno', 'rejuvenescimento-labial', 'contorno-facial-e-papada']),

    P('bioestimuladores-de-colageno', 'Bioestimuladores de colágeno', ['rosto', 'corpo'], 'Procedimento',
      'colageno-3d', 'rejuvenescimento',
      'Estimulam o seu próprio colágeno para mais firmeza e qualidade da pele — o conceito de “banco de colágeno”.',
      'Os bioestimuladores são substâncias injetáveis que ativam a produção de colágeno pelo próprio organismo. '
      'A ideia do “banco de colágeno” é investir na qualidade da pele ao longo do tempo: mais firmeza, sustentação e '
      'viço, com menor necessidade de preenchedores e um resultado gradual e natural.',
      ['Flacidez facial leve a moderada', 'Prevenção do envelhecimento', 'Perda de firmeza em pescoço e colo',
       'Flacidez de abdome, braços, coxas e glúteos', 'Flacidez após emagrecimento', 'Pele fina e sem sustentação'],
      ['Ácido poli-L-láctico', 'Hidroxiapatita de cálcio', 'Microcânulas'],
      [('Sessão', '30 a 60 minutos'), ('Recuperação', 'Rápida, com possível inchaço leve'),
       ('Resultados', 'Progressivos a partir de 30 a 60 dias'), ('Sessões', 'Em geral 1 a 3, conforme avaliação')],
      [('Quando vejo o resultado?',
        'O efeito é gradual: a pele ganha firmeza ao longo de semanas a meses, à medida que o novo colágeno é formado.'),
       ('Pode ser aplicado no corpo?',
        'Sim. Abdome, braços, coxas e glúteos estão entre as áreas mais tratadas, especialmente na flacidez após '
        'emagrecimento ou gestação.'),
       ('Preciso fazer massagem depois?',
        'Depende do produto utilizado. Quando indicado, você recebe orientações específicas para os dias seguintes.')],
      [('Avaliação', 'Análise da qualidade da pele e do grau de flacidez.'),
       ('Escolha do ativo', 'Definição do bioestimulador e do número de sessões.'),
       ('Aplicação', 'Com microcânulas, em pontos estratégicos de sustentação.'),
       ('Estímulo progressivo', 'O colágeno novo se forma ao longo das semanas seguintes.')],
      ['ultrassom-microfocado', 'fios-de-pdo', 'flacidez-corporal']),

    P('fios-de-pdo', 'Fios de PDO', ['rosto'], 'Procedimento', 'contorno-perfil', 'contorno-marcacao',
      'Fios absorvíveis que reposicionam e sustentam os tecidos para um efeito lifting sem cirurgia.',
      'Os fios de PDO (polidioxanona) são fios absorvíveis inseridos sob a pele com cânulas finas. Eles promovem '
      'sustentação imediata e estimulam a produção de colágeno ao seu redor, contribuindo para um efeito lifting '
      'natural — sem cortes e com recuperação rápida.',
      ['Flacidez leve a moderada do terço médio e inferior do rosto', 'Contorno da mandíbula',
       'Sustentação das sobrancelhas', 'Flacidez do pescoço', 'Complemento a bioestimuladores e preenchedores'],
      ['Fios de polidioxanona lisos e espiculados', 'Cânulas finas', 'Anestesia local'],
      [('Sessão', '45 a 60 minutos'), ('Recuperação', '3 a 7 dias de cuidados'),
       ('Resultados', 'Imediatos e progressivos'), ('Absorção do fio', 'Cerca de 6 a 8 meses')],
      [('O procedimento dói?',
        'É realizado com anestesia local. Pode haver desconforto leve nos dias seguintes, controlado com as '
        'orientações médicas.'),
       ('Os fios ficam aparentes?',
        'Não devem ficar. Eles são posicionados na camada adequada e absorvidos naturalmente pelo organismo.')],
      [('Mapeamento', 'Avaliação dos vetores de sustentação do rosto.'),
       ('Anestesia', 'Anestesia local nos pontos de entrada.'),
       ('Inserção', 'Fios posicionados com cânulas, sem cortes.'),
       ('Evolução', 'Sustentação imediata e estímulo de colágeno nas semanas seguintes.')],
      ['lifting-sem-cirurgia', 'bioestimuladores-de-colageno', 'ultrassom-microfocado']),

    P('ultrassom-microfocado', 'Ultrassom microfocado', ['rosto', 'corpo'], 'Tecnologia', 'ultrassom-microfocado',
      'contorno-perfil',
      'Energia de ultrassom nas camadas profundas para firmeza e efeito lifting, sem cortes ou agulhas.',
      'O ultrassom microfocado concentra energia em camadas profundas da pele — incluindo a camada muscular '
      'superficial trabalhada no lifting cirúrgico — gerando pontos de aquecimento que contraem os tecidos e '
      'estimulam colágeno novo. É uma opção não invasiva para firmeza e contorno.',
      ['Flacidez de rosto e pescoço', 'Papada e contorno mandibular', 'Elevação das sobrancelhas', 'Colo',
       'Flacidez corporal localizada: abdome, braços e joelhos'],
      ['Ultrassom microfocado com ponteiras de diferentes profundidades', 'Protocolos combinados'],
      [('Sessão', '30 a 90 minutos'), ('Recuperação', 'Retorno imediato às atividades'),
       ('Resultados', 'Progressivos, em até 90 dias'), ('Frequência', 'Não mais do que 3 vezes ao ano')],
      [('Sinto dor durante a sessão?',
        'Há uma sensação de calor e pequenas “agulhadas” nos pontos de disparo, geralmente bem tolerada. Os '
        'parâmetros são ajustados ao seu conforto.'),
       ('Quando o resultado aparece?',
        'Algumas pessoas notam firmeza logo após a sessão, mas o principal resultado surge de forma progressiva, '
        'à medida que o colágeno é produzido.')],
      [('Mapeamento', 'Definição das áreas e profundidades a tratar.'),
       ('Aplicação', 'Gel e disparos em diferentes camadas da pele.'),
       ('Sem pausa', 'Você retoma a rotina no mesmo dia.'),
       ('Resultado progressivo', 'Firmeza crescente ao longo de 2 a 3 meses.')],
      ['bioestimuladores-de-colageno', 'fios-de-pdo', 'contorno-facial-e-papada']),

    P('laser-co2-fracionado', 'Laser CO2 fracionado', ['rosto', 'corpo'], 'Tecnologia', 'laser-co2',
      'pele-hidratada',
      'Renovação profunda para textura, cicatrizes, poros e rugas finas com tecnologia fracionada.',
      'O laser de CO2 fracionado cria microcolunas de tratamento na pele, preservando áreas intactas ao redor que '
      'aceleram a recuperação. O resultado é uma renovação profunda: melhora de textura, cicatrizes de acne, poros '
      'dilatados, rugas finas e intenso estímulo de colágeno.',
      ['Cicatrizes de acne', 'Rugas finas e textura irregular', 'Poros dilatados',
       'Rejuvenescimento ao redor dos olhos e da boca', 'Estrias e cicatrizes corporais', 'Fotoenvelhecimento'],
      ['Laser CO2 fracionado (10.600 nm)', 'Anestesia tópica', 'Protocolo de cuidados pós-laser'],
      [('Sessão', '30 a 60 minutos'), ('Recuperação', '5 a 7 dias de vermelhidão e descamação'),
       ('Resultados', 'Progressivos por 3 a 6 meses'), ('Sessões', '1 a 3, conforme o objetivo')],
      [('CO2 ou outra tecnologia: qual é a melhor?',
        'A pergunta está errada! Não existe a melhor tecnologia isolada, e sim a mais adequada para o seu '
        'diagnóstico, tipo de pele e momento de vida. Essa definição acontece na consulta.'),
       ('Peles morenas podem fazer?',
        'Podem, com avaliação cuidadosa e parâmetros adequados para reduzir o risco de manchas pós-inflamatórias.')],
      [('Preparo', 'Preparo da pele em casa, quando indicado.'),
       ('Conforto', 'Anestésico tópico antes da sessão.'),
       ('Sessão', 'Parâmetros personalizados para a sua pele.'),
       ('Recuperação guiada', 'Hidratação e fotoproteção rigorosas nos dias seguintes.')],
      ['laser-lavieen', 'peeling-quimico', 'rejuvenescimento-labial']),

    P('laser-lavieen', 'Laser Lavieen', ['rosto', 'corpo'], 'Tecnologia', 'laser-lavieen', 'pele-hidratada',
      'Laser de Thulium que devolve viço, uniformiza o tom e melhora poros e textura com recuperação rápida.',
      'O Lavieen é um laser baseado na tecnologia de Thulium, que atua nas camadas mais superficiais da pele. '
      'Promove renovação, uniformiza o tom, melhora textura e poros e devolve luminosidade — o conhecido efeito de '
      '“pele de filtro” na vida real — com recuperação rápida.',
      ['Pele opaca e sem viço', 'Manchas superficiais e melasma, em protocolos combinados',
       'Poros dilatados e textura irregular', 'Linhas finas', 'Rejuvenescimento de colo, mãos e pescoço',
       'Drug delivery de ativos'],
      ['Laser de Thulium', 'Drug delivery', 'Fotoproteção pós-procedimento'],
      [('Sessão', '30 a 45 minutos'), ('Recuperação', '2 a 5 dias de pele áspera'),
       ('Resultados', 'Viço já nas primeiras semanas'), ('Sessões', '3 a 5, com intervalo de ~30 dias')],
      [('A pele fica vermelha?',
        'Pode ficar levemente avermelhada e, nos dias seguintes, com textura áspera e aspecto levemente bronzeado, '
        'que se renova em poucos dias.')],
      None,
      ['laser-co2-fracionado', 'skinbooster', 'tratamento-de-melasma']),

    P('laser-nd-yag-q-switched', 'Laser ND:YAG Q-Switched', ['rosto', 'corpo'], 'Tecnologia', 'paciente-consulta',
      'pele-uniforme',
      'Pulsos ultracurtos para manchas, melasma, uniformização do tom e remoção de tatuagens.',
      'O laser Nd:YAG Q-Switched emite pulsos de altíssima energia em nanossegundos, fragmentando pigmentos na pele. '
      'É uma ferramenta versátil para tratar manchas, auxiliar no controle do melasma, uniformizar o tom e remover '
      'tatuagens.',
      ['Melasma, em protocolos combinados', 'Manchas solares e lentigos', 'Uniformização e clareamento do tom',
       'Remoção de tatuagens', 'Poros e oleosidade', 'Manchas em axilas, virilhas e cotovelos'],
      ['Nd:YAG Q-Switched', 'Laser toning'],
      [('Sessão', '15 a 30 minutos'), ('Recuperação', 'Mínima, com vermelhidão leve'),
       ('Resultados', 'Progressivos a cada sessão'), ('Sessões', 'Protocolo seriado, definido em consulta')],
      [('Remove tatuagens coloridas?',
        'O laser atua melhor em alguns pigmentos do que em outros. A resposta depende das cores, da profundidade e do '
        'tempo da tatuagem — isso é avaliado em consulta.')],
      None,
      ['tratamento-de-melasma', 'fotoage-luz-intensa-pulsada', 'peeling-quimico']),

    P('skinbooster', 'Skinbooster', ['rosto'], 'Procedimento', 'pele-hidratada', 'colo-maos',
      'Hidratação profunda injetável que devolve viço, elasticidade e qualidade à pele.',
      'O skinbooster é um tratamento injetável à base de ácido hialurônico de baixa densidade, distribuído em '
      'microgotas na pele. Diferente do preenchimento, não tem objetivo de volume: hidrata profundamente, melhora a '
      'elasticidade e devolve o brilho saudável de uma pele bem cuidada.',
      ['Pele desidratada e opaca', 'Linhas finas', 'Rejuvenescimento de pescoço, colo e mãos',
       'Melhora de textura', 'Preparação da pele para eventos'],
      ['Ácido hialurônico não reticulado ou de baixa densidade', 'Microinjeções'],
      [('Sessão', '30 a 45 minutos'), ('Recuperação', 'Pequenas pápulas por 24 a 48 horas'),
       ('Resultados', 'Viço em poucas semanas'), ('Sessões', '2 a 3 iniciais, com manutenção')],
      [('Skinbooster aumenta volume?',
        'Não. O objetivo é a qualidade da pele — hidratação, elasticidade e luminosidade — e não o volume.')],
      None,
      ['exossomas-pdrn', 'laser-lavieen', 'bioestimuladores-de-colageno']),

    P('exossomas-pdrn', 'Exossomas + PDRN', ['rosto'], 'Procedimento', 'ampola-ativos', 'pele-hidratada',
      'Ativos regenerativos de nova geração para reparação, viço e qualidade da pele.',
      'Exossomas são vesículas que transportam sinais de comunicação entre as células; o PDRN '
      '(polidesoxirribonucleotídeo) é um ativo com ação regenerativa e anti-inflamatória. Juntos, formam uma '
      'estratégia moderna para reparar a pele, melhorar textura e viço e acelerar a recuperação após procedimentos.',
      ['Pele sensibilizada ou com barreira comprometida', 'Recuperação após lasers e procedimentos',
       'Textura, poros e viço', 'Rejuvenescimento global', 'Região dos olhos, conforme avaliação'],
      ['Exossomas', 'PDRN', 'Drug delivery com laser ou microagulhamento'],
      [('Sessão', '30 a 45 minutos'), ('Recuperação', 'Mínima'), ('Resultados', 'Progressivos'),
       ('Sessões', 'Protocolo médio de 3 a 4 sessões')],
      [('Pode ser associado a outros tratamentos?',
        'Sim, e costuma ser. Exossomas e PDRN potencializam a recuperação e os resultados de lasers, '
        'microagulhamento e outros protocolos.')],
      None,
      ['skinbooster', 'laser-lavieen', 'exossomas-capilares']),

    P('peeling-quimico', 'Peeling químico', ['rosto', 'corpo'], 'Procedimento', 'peeling-quimico',
      'pele-uniforme',
      'Renovação controlada com ácidos para manchas, acne, textura e luminosidade.',
      'O peeling químico utiliza ácidos em concentrações e combinações específicas para promover uma renovação '
      'controlada da pele. Pode ser superficial, médio ou profundo e é escolhido de acordo com o objetivo: clarear '
      'manchas, controlar acne e oleosidade, melhorar a textura e devolver luminosidade.',
      ['Manchas e melasma', 'Acne ativa e marcas de acne', 'Oleosidade e poros', 'Textura irregular',
       'Luminosidade e rejuvenescimento', 'Colo, mãos e axilas'],
      ['Ácidos glicólico, salicílico, retinoico, mandélico e outros', 'Peelings combinados'],
      [('Sessão', '20 a 40 minutos'), ('Recuperação', 'De nenhuma a 7 dias de descamação'),
       ('Resultados', 'Progressivos'), ('Sessões', 'Geralmente em série')],
      [('Vou descascar muito?',
        'Depende da profundidade escolhida. Peelings superficiais podem causar apenas uma descamação fina; os mais '
        'profundos, descamação mais evidente por alguns dias.')],
      None,
      ['tratamento-de-melasma', 'laser-lavieen', 'laser-nd-yag-q-switched']),

    P('fotoage-luz-intensa-pulsada', 'Fotoage — luz intensa pulsada', ['rosto'], 'Tecnologia', 'luz-pulsada',
      'pele-uniforme',
      'Luz intensa pulsada para manchas solares, vermelhidão, vasinhos e sinais do fotoenvelhecimento.',
      'O Fotoage é um tratamento com luz intensa pulsada, que emite diferentes comprimentos de onda para atingir '
      'pigmentos e vasos. É indicado para tratar os sinais do fotoenvelhecimento: manchas solares, vermelhidão '
      'difusa, vasinhos e tom irregular.',
      ['Manchas solares e sardas', 'Vermelhidão e rosácea', 'Vasinhos no rosto',
       'Fotoenvelhecimento de rosto, colo e mãos', 'Uniformização do tom'],
      ['Luz intensa pulsada', 'Filtros de comprimento de onda específicos'],
      [('Sessão', '20 a 40 minutos'), ('Recuperação', 'Mínima'), ('Resultados', 'A partir da 1ª sessão'),
       ('Sessões', '3 a 5, a cada ~30 dias')],
      [('As manchas escurecem depois?',
        'Sim, é esperado. As manchas tratadas costumam escurecer levemente e se desprender em alguns dias.')],
      None,
      ['laser-nd-yag-q-switched', 'tratamento-de-melasma', 'colo-pescoco-e-maos']),

    P('endolaser', 'Endolaser médico', ['rosto', 'corpo'], 'Tecnologia', 'contorno-marcacao', 'corpo-textura',
      'Laser aplicado sob a pele por fibra óptica para flacidez e gordura localizada, com mínima invasão.',
      'No endolaser, uma fibra óptica finíssima é introduzida sob a pele, após anestesia local, levando a energia do '
      'laser diretamente às camadas profundas. O calor promove retração dos tecidos, estímulo de colágeno e pode '
      'auxiliar na redução de pequenos acúmulos de gordura — sem cortes.',
      ['Papada e contorno da mandíbula', 'Flacidez de rosto e pescoço', 'Pequenas gorduras localizadas',
       'Flacidez de abdome, braços e parte interna das coxas'],
      ['Laser com fibra óptica', 'Anestesia local', 'Controle de temperatura'],
      [('Sessão', '60 a 90 minutos'), ('Recuperação', '3 a 7 dias de inchaço'),
       ('Resultados', 'Progressivos em 3 a 6 meses'), ('Sessões', 'Geralmente 1, conforme avaliação')],
      [('Fica cicatriz?',
        'A fibra é introduzida por microperfurações, que normalmente cicatrizam sem marcas aparentes.')],
      None,
      ['contorno-facial-e-papada', 'flacidez-corporal', 'ultrassom-microfocado']),

    P('rejuvenescimento-periocular', 'Rejuvenescimento da região dos olhos', ['rosto'], 'Protocolo', 'olhos',
      'rejuvenescimento',
      'Olheiras, linhas finas e flacidez na região mais delicada do rosto.',
      'Por que a região dos olhos envelhece mais rápido? A pele ali é significativamente mais fina, tem menos '
      'glândulas e se movimenta milhares de vezes por dia — por isso costuma mostrar os primeiros sinais do tempo. '
      'O protocolo combina tecnologias e injetáveis de acordo com o que mais incomoda: linhas, olheiras, flacidez ou '
      'textura.',
      ['“Pés de galinha”', 'Olheiras pigmentadas, vasculares ou de sulco', 'Flacidez das pálpebras',
       'Textura e linhas finas', 'Queda da sobrancelha'],
      ['Toxina botulínica', 'Preenchimento do sulco lacrimal', 'Exossomas + PDRN', 'Laser CO2 e Lavieen',
       'Bioestimuladores'],
      [('Formato', 'Protocolo combinado'), ('Recuperação', 'Variável conforme as técnicas'),
       ('Resultados', 'Progressivos'), ('Plano', 'Definido em consulta')],
      [('Todo tipo de olheira tem tratamento?',
        'Existem olheiras pigmentares, vasculares, estruturais e mistas. Cada tipo responde a abordagens diferentes, '
        'por isso o diagnóstico correto é o primeiro passo.')],
      None,
      ['toxina-botulinica', 'exossomas-pdrn', 'laser-co2-fracionado']),

    P('tratamento-de-melasma', 'Tratamento de melasma', ['rosto'], 'Protocolo', 'pele-uniforme', 'protetor-solar',
      'Abordagem contínua e combinada para controlar o melasma e manter a pele uniforme.',
      'O melasma é uma condição crônica, influenciada por sol, luz visível, calor, hormônios e genética. Não existe '
      'solução única: o controle vem de um plano contínuo que combina fotoproteção, cuidados em casa, medicações '
      'quando indicadas e tecnologias como Laser ND:YAG Q-Switched, peeling químico, Laser Lavieen e Fotoage.',
      ['Manchas acastanhadas na testa, maçãs do rosto e buço', 'Melasma que volta após tratamentos',
       'Manchas pós-inflamatórias', 'Tom irregular'],
      ['Laser ND:YAG Q-Switched', 'Peeling químico', 'Laser Lavieen', 'Fotoage',
       'Clareadores tópicos e orais, quando indicados'],
      [('Formato', 'Protocolo combinado e contínuo'), ('Recuperação', 'Geralmente mínima'),
       ('Resultados', 'Progressivos'), ('Manutenção', 'Fundamental para evitar recidivas')],
      [('Melasma tem cura?',
        'O melasma é crônico e tem tendência a voltar. Com tratamento adequado e manutenção, é possível controlá-lo '
        'muito bem e manter a pele uniforme.')],
      None,
      ['laser-nd-yag-q-switched', 'peeling-quimico', 'laser-lavieen']),

    P('rejuvenescimento-labial', 'Lábios e região peribucal', ['rosto'], 'Protocolo', 'labios', 'rosto-retrato',
      'Contorno, hidratação e suavização das linhas ao redor da boca com naturalidade.',
      'Você já percebeu como seus lábios mudam com o tempo? Eles perdem volume, contorno e hidratação, e surgem '
      'linhas ao redor da boca. O protocolo labial e peribucal pode combinar toxina botulínica, preenchimento, Laser '
      'CO2, skinbooster e peeling — sempre buscando lábios saudáveis, proporcionais e naturais.',
      ['Perda de volume e contorno', 'Lábios ressecados', 'Linhas ao redor da boca (“código de barras”)',
       'Cantos da boca caídos', 'Assimetrias'],
      ['Ácido hialurônico', 'Toxina botulínica', 'Laser CO2 fracionado', 'Skinbooster', 'Peeling'],
      [('Formato', 'Protocolo combinado'), ('Recuperação', 'Inchaço leve por alguns dias'),
       ('Resultados', 'Imediatos e progressivos'), ('Plano', 'Definido em consulta')],
      [('Vai ficar exagerado?',
        'A proposta da Vinovare é a naturalidade: respeitar as proporções do seu rosto e devolver aos lábios '
        'hidratação, contorno e volume na medida certa.')],
      None,
      ['preenchimento-acido-hialuronico', 'laser-co2-fracionado', 'skinbooster']),

    P('lifting-sem-cirurgia', 'Lifting sem cirurgia', ['rosto'], 'Protocolo', 'rejuvenescimento', 'contorno-perfil',
      'Tecnologias e injetáveis combinados para devolver sustentação ao rosto, sem cortes.',
      'O lifting sem cirurgia trabalha os pontos de sustentação do rosto. Em vez de uma única técnica, combina fios '
      'de PDO, ultrassom microfocado, endolaser, bioestimuladores e preenchimento para reposicionar tecidos, '
      'devolver firmeza e redefinir contornos de forma gradual e natural.',
      ['Flacidez facial', 'Perda de contorno mandibular', 'Sulcos e queda do terço médio', 'Flacidez do pescoço',
       'Prevenção da flacidez'],
      ['Fios de PDO', 'Ultrassom microfocado', 'Endolaser médico', 'Bioestimuladores', 'Ácido hialurônico'],
      [('Formato', 'Protocolo combinado'), ('Recuperação', 'Variável conforme as técnicas'),
       ('Resultados', 'Imediatos e progressivos'), ('Plano', 'Definido em consulta')],
      [('Substitui a cirurgia plástica?',
        'Não substitui em todos os casos. Para flacidez leve a moderada, o protocolo oferece ótimos resultados; em '
        'flacidez acentuada, a Dra. Karinie orienta sobre as alternativas mais adequadas.')],
      None,
      ['fios-de-pdo', 'ultrassom-microfocado', 'bioestimuladores-de-colageno']),

    P('contorno-facial-e-papada', 'Contorno facial e papada', ['rosto'], 'Protocolo', 'contorno-marcacao',
      'contorno-perfil',
      'Definição de mandíbula, queixo e pescoço com Nefertiti, bioplastia e tecnologias.',
      'Um contorno facial bem definido transmite jovialidade e harmonia. O protocolo trata papada (flacidez e gordura '
      'localizada), linha da mandíbula e queixo, podendo combinar o lifting Nefertiti com toxina botulínica, '
      'bioplastia com ácido hialurônico, endolaser e ultrassom microfocado.',
      ['Papada', 'Linha da mandíbula pouco definida', 'Queixo retraído', 'Bandas do pescoço', 'Harmonia do perfil'],
      ['Lifting Nefertiti (toxina botulínica)', 'Bioplastia', 'Endolaser médico', 'Ultrassom microfocado'],
      [('Formato', 'Protocolo combinado'), ('Recuperação', 'Variável conforme as técnicas'),
       ('Resultados', 'Imediatos e progressivos'), ('Plano', 'Definido em consulta')],
      [('O que é o lifting Nefertiti?',
        'É uma técnica que usa toxina botulínica no músculo do pescoço (platisma) para suavizar bandas e ajudar a '
        'definir a linha da mandíbula.')],
      None,
      ['endolaser', 'preenchimento-acido-hialuronico', 'ultrassom-microfocado']),

    # ---------------------------------------------------------------- CORPO
    P('harmonizacao-glutea', 'Harmonização glútea', ['corpo'], 'Protocolo', 'corpo-silhueta', 'corpo-textura',
      'Firmeza, contorno e textura para os glúteos com bioestimuladores e ácido hialurônico.',
      'A harmonização glútea melhora a firmeza, o contorno e a qualidade da pele da região, com bioestimuladores de '
      'colágeno e, quando indicado, preenchimento com ácido hialurônico. A proposta é valorizar suas curvas com '
      'naturalidade e segurança.',
      ['Flacidez glútea', 'Depressões laterais', 'Perda de projeção', 'Celulite e textura irregular',
       'Flacidez após emagrecimento'],
      ['Bioestimuladores de colágeno', 'Ácido hialurônico', 'Tecnologias complementares'],
      [('Sessão', '45 a 60 minutos'), ('Recuperação', 'Rápida, com cuidados por alguns dias'),
       ('Resultados', 'Progressivos'), ('Sessões', '1 a 3, conforme avaliação')],
      [('O resultado é imediato?',
        'Com ácido hialurônico, parte do resultado é imediata; com bioestimuladores, a melhora de firmeza e textura é '
        'gradual ao longo dos meses.')],
      None,
      ['bioestimuladores-de-colageno', 'flacidez-corporal', 'intradermoterapia']),

    P('flacidez-corporal', 'Flacidez e gordura localizada', ['corpo'], 'Protocolo', 'corpo-ombro', 'corpo-textura',
      'Emagreceu e ficou com flacidez? Protocolos para devolver firmeza e contorno ao corpo.',
      'Emagreceu e ficou com flacidez? Abdome, braços, coxas e glúteos podem perder firmeza após o emagrecimento, a '
      'gestação ou com o passar dos anos. O protocolo combina endolaser, bioestimuladores, ultrassom microfocado e '
      'intradermoterapia para devolver firmeza e melhorar o contorno.',
      ['Flacidez após emagrecimento', 'Flacidez abdominal', 'Braços e parte interna das coxas',
       'Gordura localizada resistente', 'Flacidez acima dos joelhos'],
      ['Endolaser corporal', 'Bioestimuladores', 'Ultrassom microfocado', 'Intradermoterapia'],
      [('Formato', 'Protocolo combinado'), ('Recuperação', 'Variável conforme as técnicas'),
       ('Resultados', 'Progressivos'), ('Plano', 'Definido em consulta')],
      [('Qual o melhor momento para tratar a flacidez após emagrecer?',
        'O ideal é iniciar quando o peso estiver estável. A avaliação define o melhor momento e a combinação de '
        'técnicas para o seu caso.')],
      None,
      ['endolaser', 'bioestimuladores-de-colageno', 'harmonizacao-glutea']),

    P('intradermoterapia', 'Intradermoterapia', ['corpo'], 'Procedimento', 'corpo-textura', 'textura-serum',
      'Microinjeções de ativos na derme para gordura localizada, celulite e flacidez.',
      'A intradermoterapia — também chamada de mesoterapia — consiste em microinjeções de ativos diretamente na '
      'derme, a camada da pele onde eles atuam. Os ativos são escolhidos de acordo com o objetivo: gordura '
      'localizada, celulite, flacidez ou qualidade da pele.',
      ['Gordura localizada', 'Celulite', 'Flacidez leve', 'Melhora da textura corporal'],
      ['Ativos lipolíticos e reestruturantes', 'Microagulhas'],
      [('Sessão', '20 a 40 minutos'), ('Recuperação', 'Imediata'), ('Resultados', 'Progressivos'),
       ('Sessões', 'Protocolo seriado')],
      [('Dói?', 'As agulhas são muito finas e o desconforto costuma ser leve e passageiro.')],
      None,
      ['flacidez-corporal', 'harmonizacao-glutea', 'bioestimuladores-de-colageno']),

    P('colo-pescoco-e-maos', 'Colo, pescoço e mãos', ['corpo'], 'Protocolo', 'colo-maos', 'maos-creme',
      'Rejuvenescimento das áreas que mais revelam a idade — e que costumam ser esquecidas.',
      'Colo, pescoço e mãos ficam expostos ao sol todos os dias e costumam receber menos cuidado do que o rosto — '
      'por isso revelam a idade. O protocolo trata manchas, linhas, flacidez e textura com lasers, skinbooster, '
      'bioestimuladores e peelings.',
      ['Manchas solares', 'Linhas do colo e do pescoço', 'Flacidez', 'Mãos com perda de volume',
       'Textura e ressecamento'],
      ['Laser Lavieen', 'Fotoage', 'Skinbooster', 'Bioestimuladores', 'Peeling químico'],
      [('Formato', 'Protocolo combinado'), ('Recuperação', 'Geralmente rápida'), ('Resultados', 'Progressivos'),
       ('Plano', 'Definido em consulta')],
      [], None,
      ['skinbooster', 'fotoage-luz-intensa-pulsada', 'bioestimuladores-de-colageno']),

    P('cuidados-pos-parto', 'Cuidados pós-parto', ['corpo', 'cabelo'], 'Protocolo', 'pos-parto', 'corpo-ombro',
      'Cuidado integral para pele, cabelo e bem-estar após a gestação, no seu tempo.',
      'A gestação traz mudanças importantes para o corpo: flacidez, estrias, manchas e queda de cabelo são queixas '
      'frequentes no pós-parto. O protocolo é construído no seu tempo, respeitando a amamentação e a recuperação, e '
      'pode incluir lasers, bioestimuladores e cuidados capilares.',
      ['Flacidez abdominal', 'Estrias', 'Manchas e melasma gestacional', 'Queda de cabelo pós-parto',
       'Retomada da rotina de cuidados'],
      ['Laser CO2 fracionado', 'Bioestimuladores', 'Laser Lavieen', 'Protocolos capilares'],
      [('Formato', 'Protocolo por etapas'), ('Início', 'Conforme liberação médica'),
       ('Amamentação', 'Técnicas compatíveis com a fase'), ('Plano', 'Definido em consulta')],
      [('Posso tratar enquanto amamento?',
        'Algumas abordagens são seguras durante a amamentação e outras devem aguardar. A Dra. Karinie organiza as '
        'etapas respeitando essa fase.')],
      None,
      ['flacidez-corporal', 'consulta-capilar', 'tratamento-de-melasma']),

    P('cuidados-masculinos', 'Cuidados masculinos', ['rosto', 'corpo', 'cabelo'], 'Protocolo', 'masculino',
      'capilar-masculino',
      'Tratamentos discretos e eficazes para pele, contorno e cabelo masculinos.',
      'Cada vez mais homens buscam cuidados dermatológicos com resultados naturais e discretos. O protocolo '
      'masculino trata flacidez facial, linhas de expressão, contorno e calvície, combinando preenchimento, '
      'bioestimuladores, toxina botulínica, lasers e terapias capilares.',
      ['Linhas de expressão', 'Flacidez e definição da mandíbula', 'Calvície e afinamento dos fios',
       'Oleosidade, poros e marcas de acne', 'Manchas'],
      ['Toxina botulínica', 'Preenchimento', 'Bioestimuladores', 'Lasers', 'Terapias capilares'],
      [('Formato', 'Protocolo personalizado'), ('Discrição', 'Técnicas com pouco tempo de recuperação'),
       ('Resultados', 'Naturais'), ('Plano', 'Definido em consulta')],
      [], None,
      ['toxina-botulinica', 'contorno-facial-e-papada', 'prevencao-da-calvicie']),

    # ---------------------------------------------------------------- CABELO
    P('consulta-capilar', 'Consulta capilar', ['cabelo'], 'Consulta', 'capilar-tricoscopia', 'cabelo-costas',
      'Avaliação completa do couro cabeludo e dos fios para descobrir a causa da queda.',
      'A queda de cabelo pode ter muitas causas — hormonais, nutricionais, genéticas, emocionais ou inflamatórias. '
      'A consulta capilar avalia couro cabeludo e haste dos fios com tricoscopia, solicita exames quando necessário '
      'e define um protocolo individualizado de tratamento.',
      ['Queda de cabelo intensa', 'Afinamento e rarefação', 'Entradas e coroa', 'Caspa, coceira ou oleosidade',
       'Queda após parto, dieta ou estresse'],
      ['Tricoscopia digital', 'Exames laboratoriais', 'Prescrição individualizada'],
      [('Duração', 'Cerca de 60 minutos'), ('Exames', 'Solicitados quando necessário'),
       ('Resultado', 'Diagnóstico e plano de tratamento'), ('Retornos', 'Programados para acompanhar')],
      [('Por que investigar a causa da queda?',
        'Porque tratamentos genéricos costumam falhar. Identificar a causa — ou as causas — permite escolher o que '
        'realmente funciona para você.')],
      [('Conversa detalhada', 'Histórico, rotina, alimentação, medicações e momento de vida.'),
       ('Tricoscopia', 'Exame ampliado do couro cabeludo e dos fios.'),
       ('Exames', 'Investigação laboratorial, quando indicada.'),
       ('Protocolo', 'Cuidados em casa, medicações e procedimentos combinados.')],
      ['drug-delivery-capilar', 'exossomas-capilares', 'prevencao-da-calvicie']),

    P('drug-delivery-capilar', 'Drug delivery capilar', ['cabelo'], 'Procedimento', 'capilar-serum', 'cabelo-macro',
      'Ativos levados diretamente ao couro cabeludo, potencializados por microagulhamento e lasers.',
      'O drug delivery capilar (intradermoterapia capilar) leva ativos diretamente à derme do couro cabeludo, onde '
      'estão os folículos. Pode ser associado a tecnologias como microagulhamento robótico e lasers, que abrem '
      'microcanais e potencializam a absorção dos ativos.',
      ['Queda de cabelo', 'Alopecia androgenética', 'Eflúvio telógeno', 'Fortalecimento dos fios',
       'Complemento ao tratamento em casa'],
      ['Intradermoterapia capilar', 'Microagulhamento robótico', 'Lasers', 'Ativos estimulantes'],
      [('Sessão', '30 a 45 minutos'), ('Recuperação', 'Imediata'), ('Resultados', 'A partir de 3 meses'),
       ('Sessões', 'Protocolo quinzenal ou mensal')],
      [('Quando começo a ver resultado?',
        'O ciclo do cabelo é lento: a redução da queda costuma ser percebida nos primeiros meses, e o ganho de '
        'densidade, de forma progressiva.')],
      None,
      ['exossomas-capilares', 'consulta-capilar', 'prevencao-da-calvicie']),

    P('exossomas-capilares', 'Exossomas capilares', ['cabelo'], 'Procedimento', 'cabelo-macro', 'capilar-serum',
      'Terapia regenerativa de última geração para estimular folículos e fortalecer os fios.',
      'Os exossomas são vesículas com sinais regenerativos que atuam na comunicação entre as células. No couro '
      'cabeludo, são utilizados para estimular folículos enfraquecidos e melhorar a densidade dos fios, podendo ser '
      'associados a outros tratamentos capilares.',
      ['Afinamento dos fios', 'Queda crônica', 'Alopecia androgenética, em associação', 'Após transplante capilar'],
      ['Exossomas', 'Microagulhamento', 'Protocolos combinados'],
      [('Sessão', '30 a 45 minutos'), ('Recuperação', 'Imediata'), ('Resultados', 'Progressivos'),
       ('Sessões', 'Definidas em consulta')],
      [], None,
      ['drug-delivery-capilar', 'protocolo-pos-transplante', 'consulta-capilar']),

    P('prevencao-da-calvicie', 'Prevenção da calvície', ['cabelo'], 'Protocolo', 'cabelo-costas',
      'capilar-tricoscopia',
      'Protocolo preventivo para preservar e melhorar a qualidade dos fios ao longo do tempo.',
      'Quanto antes a calvície é identificada, mais fios podem ser preservados. O protocolo preventivo, sempre '
      'iniciado com uma consulta capilar, combina tratamento em casa e procedimentos para melhorar a qualidade dos '
      'fios e retardar a progressão da queda.',
      ['Histórico familiar de calvície', 'Entradas ou coroa começando a rarear', 'Fios mais finos',
       'Queda persistente'],
      ['Tricoscopia', 'Drug delivery capilar', 'Exossomas', 'Tratamento domiciliar'],
      [('Formato', 'Protocolo contínuo'), ('Início', 'Após consulta capilar'), ('Resultados', 'Progressivos'),
       ('Plano', 'Definido em consulta')],
      [], None,
      ['consulta-capilar', 'drug-delivery-capilar', 'exossomas-capilares']),

    P('protocolo-pos-transplante', 'Protocolo pós-transplante', ['cabelo'], 'Protocolo', 'capilar-masculino',
      'cabelo-macro',
      'Manutenção dos fios transplantados e prevenção de novos focos de queda.',
      'O transplante capilar redistribui fios, mas não impede que a calvície continue avançando nas áreas não '
      'transplantadas. O protocolo pós-transplante cuida dos fios nativos, favorece a adaptação dos transplantados e '
      'ajuda a evitar novos focos de queda.',
      ['Após a liberação do cirurgião', 'Manutenção dos fios nativos', 'Prevenção de novas falhas'],
      ['Drug delivery capilar', 'Exossomas', 'Tratamento domiciliar'],
      [('Formato', 'Protocolo contínuo'), ('Início', 'Após liberação do cirurgião'), ('Resultados', 'Progressivos'),
       ('Plano', 'Definido em consulta')],
      [], None,
      ['exossomas-capilares', 'drug-delivery-capilar', 'consulta-capilar']),
]

POR_SLUG = {p['slug']: p for p in PROCEDIMENTOS}

# Destaques usados na home (ordem do carrossel)
DESTAQUES = ['toxina-botulinica', 'bioestimuladores-de-colageno', 'laser-co2-fracionado', 'ultrassom-microfocado',
             'harmonizacao-glutea', 'tratamento-de-melasma', 'consulta-capilar', 'rejuvenescimento-periocular']

# Principais protocolos por área (página de tratamentos / painéis da home)
PROTOCOLOS_AREA = {
    'rosto': ['rejuvenescimento-periocular', 'bioestimuladores-de-colageno', 'contorno-facial-e-papada',
              'tratamento-de-melasma', 'lifting-sem-cirurgia', 'rejuvenescimento-labial'],
    'corpo': ['harmonizacao-glutea', 'flacidez-corporal', 'colo-pescoco-e-maos', 'cuidados-pos-parto',
              'cuidados-masculinos', 'endolaser'],
    'cabelo': ['consulta-capilar', 'prevencao-da-calvicie', 'protocolo-pos-transplante', 'drug-delivery-capilar',
               'exossomas-capilares'],
}
