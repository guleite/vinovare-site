"""Conteúdo dermatológico educativo (blog). Textos informativos, sem caráter de diagnóstico."""

CATEGORIAS = ['Pele', 'Prevenção', 'Cabelo', 'Tratamentos']


def A(slug, titulo, categoria, resumo, img, leitura, data, corpo, relacionados=()):
    return {'slug': slug, 'titulo': titulo, 'categoria': categoria, 'resumo': resumo, 'img': img,
            'leitura': leitura, 'data': data, 'corpo': corpo, 'relacionados': list(relacionados)}


ARTIGOS = [
    A('barreira-cutanea', 'Barreira cutânea: por que ela é tão importante para a sua pele?', 'Pele',
      'Ela protege, hidrata e mantém o equilíbrio da pele. Entenda o que enfraquece a barreira cutânea e como cuidar '
      'dela no dia a dia.',
      'colageno-3d', 5, '18 nov 2026', """
<p class="lead">Ardência ao passar um creme, vermelhidão, sensação de repuxar depois do banho, descamação que não melhora. Esses sinais costumam ter a mesma origem: uma <strong>barreira cutânea comprometida</strong>.</p>
<h2 id="o-que-e">O que é a barreira cutânea</h2>
<p>É a camada mais externa da pele — o estrato córneo — formada por células unidas por uma “argamassa” de lipídios, como ceramidas, colesterol e ácidos graxos. Uma boa imagem é a de um muro de tijolos: as células são os tijolos e os lipídios, o cimento.</p>
<p>Quando esse muro está íntegro, ele cumpre duas funções essenciais: impede a perda excessiva de água e dificulta a entrada de irritantes, alérgenos e microrganismos.</p>
<h2 id="o-que-enfraquece">O que enfraquece a barreira</h2>
<ul>
<li>Banhos muito quentes e demorados;</li>
<li>Sabonetes agressivos e excesso de esfoliação;</li>
<li>Uso simultâneo de muitos ácidos e ativos sem orientação;</li>
<li>Clima seco — como o de Brasília em boa parte do ano;</li>
<li>Exposição solar sem proteção e poluição;</li>
<li>Condições como dermatite atópica e rosácea.</li>
</ul>
<blockquote>Mais produtos não significam mais cuidado. Muitas vezes, o primeiro passo para tratar a pele é simplificar a rotina.</blockquote>
<h2 id="como-cuidar">Como cuidar no dia a dia</h2>
<p>Algumas medidas simples fazem muita diferença: limpar a pele com produtos suaves, hidratar logo após o banho, preferir fórmulas com ceramidas, glicerina e niacinamida, e usar protetor solar diariamente.</p>
<p>Ativos potentes — como retinoides e ácidos — continuam sendo grandes aliados, mas precisam ser introduzidos no momento certo e na concentração adequada.</p>
<h2 id="quando-procurar">Quando procurar a dermatologista</h2>
<p>Se a sensibilidade persiste, se a pele reage a quase tudo ou se há vermelhidão e descamação frequentes, vale investigar. Na consulta, é possível identificar a causa e montar uma rotina que recupere a barreira antes de iniciar tratamentos mais intensos.</p>
""", ['protetor-solar-todos-os-dias', 'rotina-de-skincare']),

    A('regiao-dos-olhos', 'Por que a região dos olhos envelhece mais rápido?', 'Prevenção',
      'Pele mais fina, movimento constante e exposição ao sol: conheça os motivos e as formas de cuidar da área mais '
      'delicada do rosto.',
      'olhos', 4, '11 nov 2026', """
<p class="lead">É comum que os primeiros sinais do tempo apareçam ao redor dos olhos. Não é impressão: essa região tem características que a tornam mais vulnerável.</p>
<h2 id="pele-fina">Uma pele muito mais fina</h2>
<p>A pele das pálpebras é uma das mais finas do corpo, com menos glândulas sebáceas e menos sustentação. Por isso, perde hidratação com facilidade e mostra linhas mais cedo.</p>
<h2 id="movimento">Movimento o dia inteiro</h2>
<p>Piscamos milhares de vezes por dia, sorrimos, apertamos os olhos contra a luz. Essa movimentação constante, somada à perda gradual de colágeno, favorece o surgimento dos “pés de galinha” e de linhas finas.</p>
<h2 id="olheiras">Nem toda olheira é igual</h2>
<p>As olheiras podem ser pigmentares (escurecimento da pele), vasculares (vasos aparentes), estruturais (sulco e perda de volume) ou mistas. Cada tipo responde a abordagens diferentes — e é por isso que receitas genéricas costumam frustrar.</p>
<blockquote>O diagnóstico do tipo de olheira é o que define o tratamento: laser, preenchimento, ativos regenerativos ou a combinação deles.</blockquote>
<h2 id="prevencao">Prevenção que funciona</h2>
<ul>
<li>Óculos escuros e protetor solar adequados à região;</li>
<li>Hidratante específico para a área dos olhos;</li>
<li>Sono de qualidade e controle de alergias;</li>
<li>Evitar coçar e esfregar os olhos.</li>
</ul>
<h2 id="tratamentos">O que a dermatologia oferece</h2>
<p>Toxina botulínica para linhas dinâmicas, preenchimento do sulco lacrimal em casos selecionados, lasers para textura e flacidez, além de exossomas e PDRN para qualidade da pele. Tudo começa com uma avaliação cuidadosa.</p>
""", ['barreira-cutanea', 'protetor-solar-todos-os-dias']),

    A('protetor-solar-todos-os-dias', 'Protetor solar: como escolher e usar todos os dias', 'Prevenção',
      'O cuidado mais simples e mais eficaz contra manchas e envelhecimento. Veja como escolher a textura certa e '
      'aplicar a quantidade adequada.',
      'protetor-solar', 4, '04 nov 2026', """
<p class="lead">Se existe um único hábito capaz de transformar a sua pele ao longo dos anos, é o uso diário do protetor solar. Ele previne manchas, envelhecimento precoce e câncer de pele.</p>
<h2 id="fps">FPS, PPD e cor: o que observar</h2>
<p>O FPS indica a proteção contra a radiação UVB, responsável pelas queimaduras. O PPD (ou o selo UVA) indica a proteção contra a radiação UVA, ligada ao envelhecimento. Para quem tem melasma, protetores <strong>com cor</strong> são grandes aliados, pois ajudam a bloquear a luz visível.</p>
<h2 id="textura">A textura certa é a que você usa</h2>
<ul>
<li><strong>Pele oleosa:</strong> fluidos e géis de toque seco;</li>
<li><strong>Pele seca:</strong> loções e cremes mais hidratantes;</li>
<li><strong>Pele sensível:</strong> fórmulas com filtros minerais e sem fragrância.</li>
</ul>
<h2 id="quantidade">Quantidade e reaplicação</h2>
<p>Para o rosto, a referência prática é a medida de cerca de uma colher de chá — ou o equivalente a dois dedos de produto. Reaplique a cada duas a três horas de exposição, após suor intenso ou contato com a água.</p>
<blockquote>Protetor solar não é só para dias de praia: a radiação está presente mesmo em dias nublados e em ambientes internos próximos a janelas.</blockquote>
<h2 id="alem-do-rosto">Não esqueça pescoço, colo e mãos</h2>
<p>São áreas muito expostas e que costumam revelar a idade. Incluí-las na rotina é uma das formas mais simples de prevenir manchas e flacidez.</p>
""", ['barreira-cutanea', 'regiao-dos-olhos']),

    A('queda-de-cabelo', 'Queda de cabelo: quando é hora de procurar a dermatologista?', 'Cabelo',
      'Perder fios todos os dias é normal — até certo ponto. Saiba diferenciar a queda fisiológica de sinais que '
      'merecem investigação.',
      'capilar-tricoscopia', 5, '28 out 2026', """
<p class="lead">Perder fios faz parte do ciclo natural do cabelo. O problema começa quando a queda aumenta, persiste ou vem acompanhada de afinamento e falhas.</p>
<h2 id="normal">Quanto é normal perder?</h2>
<p>Em média, perdemos entre 50 e 100 fios por dia. Esse número pode variar com a estação do ano, a lavagem e o comprimento dos cabelos. Mais importante do que contar fios é observar mudanças no padrão.</p>
<h2 id="sinais">Sinais de alerta</h2>
<ul>
<li>Queda intensa por mais de três meses;</li>
<li>Rabo de cavalo mais fino ou couro cabeludo mais aparente;</li>
<li>Entradas aumentando ou rarefação no topo da cabeça;</li>
<li>Falhas arredondadas;</li>
<li>Coceira, ardor, descamação ou dor no couro cabeludo.</li>
</ul>
<h2 id="causas">As causas mais comuns</h2>
<p>Alterações hormonais, deficiências nutricionais, dietas restritivas, pós-parto, estresse, doenças da tireoide, uso de medicações e fatores genéticos estão entre as causas frequentes. Muitas vezes, há mais de um fator envolvido.</p>
<blockquote>Tratar a queda sem investigar a causa é como apagar um incêndio sem saber de onde vem o fogo.</blockquote>
<h2 id="consulta">Como é a investigação</h2>
<p>Na consulta capilar, a avaliação inclui conversa detalhada, exame do couro cabeludo com tricoscopia e, quando necessário, exames laboratoriais. A partir do diagnóstico, o protocolo pode combinar cuidados em casa, medicações e procedimentos como drug delivery e exossomas.</p>
""", ['rotina-de-skincare', 'flacidez-apos-emagrecer']),

    A('flacidez-apos-emagrecer', 'Emagreceu e ficou com flacidez? Veja como cuidar da sua pele', 'Tratamentos',
      'A perda de peso é uma conquista — e a pele também merece atenção nesse processo. Conheça as estratégias para '
      'devolver firmeza.',
      'corpo-silhueta', 5, '21 out 2026', """
<p class="lead">Perder peso é uma grande conquista para a saúde. Mas, especialmente quando o emagrecimento é rápido ou expressivo, a pele nem sempre acompanha a mudança na mesma velocidade.</p>
<h2 id="por-que">Por que a flacidez aparece</h2>
<p>A pele é sustentada por fibras de colágeno e elastina. Quando o volume diminui, essas fibras — que já estavam distendidas — podem não conseguir se retrair totalmente. A idade, a genética, a exposição solar e o número de variações de peso ao longo da vida influenciam o resultado.</p>
<h2 id="areas">Áreas mais afetadas</h2>
<ul>
<li>Abdome e flancos;</li>
<li>Parte interna dos braços e das coxas;</li>
<li>Glúteos;</li>
<li>Rosto e pescoço — com perda de volume e definição.</li>
</ul>
<h2 id="tratamentos">O que pode ser feito</h2>
<p>O tratamento costuma ser combinado. <strong>Bioestimuladores de colágeno</strong> melhoram a firmeza e a qualidade da pele; o <strong>ultrassom microfocado</strong> e o <strong>endolaser</strong> promovem retração dos tecidos; e a <strong>intradermoterapia</strong> pode auxiliar em gorduras localizadas residuais.</p>
<blockquote>O melhor momento para começar é quando o peso está estável — e a avaliação define a combinação ideal para o seu corpo.</blockquote>
<h2 id="habitos">Hábitos que ajudam</h2>
<p>Ingestão adequada de proteínas, treino de força, hidratação e sono de qualidade são aliados importantes da pele durante e depois do emagrecimento.</p>
""", ['barreira-cutanea', 'queda-de-cabelo']),

    A('rotina-de-skincare', 'Skincare: por que menos pode ser mais', 'Pele',
      'Rotinas com dez passos nem sempre são as melhores. Entenda como montar um cuidado essencial, eficiente e '
      'adequado ao seu tipo de pele.',
      'rotina-noturna', 4, '14 out 2026', """
<p class="lead">As redes sociais popularizaram rotinas extensas, com muitos produtos e ativos. Mas, para a maioria das pessoas, uma rotina enxuta e bem indicada traz resultados melhores — e menos irritação.</p>
<h2 id="essencial">O essencial da manhã</h2>
<ul>
<li><strong>Limpeza suave</strong>, adequada ao seu tipo de pele;</li>
<li><strong>Antioxidante</strong>, como vitamina C, quando indicado;</li>
<li><strong>Hidratante</strong>;</li>
<li><strong>Protetor solar</strong> — o passo que não pode faltar.</li>
</ul>
<h2 id="noite">O essencial da noite</h2>
<p>À noite, a pele está em modo de reparo. Depois da limpeza, é o momento dos ativos de tratamento — como retinoides, ácidos ou clareadores — seguidos de hidratação.</p>
<blockquote>Combinar ativos sem orientação é uma das causas mais comuns de sensibilidade e de barreira cutânea danificada.</blockquote>
<h2 id="personalizar">Por que personalizar</h2>
<p>Peles com acne, melasma, rosácea ou sensibilidade precisam de escolhas diferentes. Uma rotina prescrita leva em conta o seu diagnóstico, o clima, a sua disponibilidade e até os procedimentos que você está fazendo.</p>
<h2 id="consistencia">Consistência acima de tudo</h2>
<p>Os resultados de qualquer rotina aparecem com o tempo. Melhor uma rotina simples, feita todos os dias, do que uma rotina complexa abandonada na segunda semana.</p>
""", ['barreira-cutanea', 'protetor-solar-todos-os-dias']),
]

POR_SLUG = {a['slug']: a for a in ARTIGOS}
