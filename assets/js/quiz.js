/* ==========================================================================
   VINOVARE — "Descubra seu cuidado"
   Questionário de orientação (sem diagnóstico, sem armazenamento de dados).
   ========================================================================== */
(() => {
  'use strict';
  const root = document.querySelector('[data-quiz]');
  if (!root) return;

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const DATA = JSON.parse($('#quiz-data').textContent);
  const BASE = document.body.dataset.root || '';
  const WA = document.body.dataset.wa || '5561991744080';
  const stage = $('[data-quiz-stage]', root);
  const bar = $('[data-quiz-bar]', root);
  const stepEl = $('[data-quiz-step]', root);
  const back = $('[data-quiz-back]', root);
  const slides = $$('[data-slide]', root);

  const icon = (n) => `<svg class="i" aria-hidden="true"><use href="#i-${n}"></use></svg>`;
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  /* ------------------------------------------------------------ Perguntas */
  const AREAS = [
    { v: 'rosto', label: 'Rosto', desc: 'Linhas, flacidez, manchas, viço', ico: 'leaf', slide: 1 },
    { v: 'corpo', label: 'Corpo', desc: 'Firmeza, contorno, pós-parto', ico: 'heart', slide: 2 },
    { v: 'cabelo', label: 'Cabelo e couro cabeludo', desc: 'Queda, afinamento, prevenção', ico: 'drop', slide: 3 },
    { v: 'pele', label: 'Saúde da pele', desc: 'Sensibilidade, acne, rotina', ico: 'shield', slide: 4 },
  ];
  const INTERESTS = {
    rosto: [
      { v: 'linhas', label: 'Linhas de expressão e rugas', procs: ['toxina-botulinica', 'rejuvenescimento-periocular', 'laser-co2-fracionado', 'skinbooster'], arts: ['regiao-dos-olhos'] },
      { v: 'flacidez', label: 'Flacidez e contorno do rosto', procs: ['bioestimuladores-de-colageno', 'lifting-sem-cirurgia', 'ultrassom-microfocado', 'fios-de-pdo', 'contorno-facial-e-papada'], arts: ['rotina-de-skincare'] },
      { v: 'manchas', label: 'Manchas e tom irregular', procs: ['tratamento-de-melasma', 'laser-nd-yag-q-switched', 'fotoage-luz-intensa-pulsada', 'peeling-quimico'], arts: ['protetor-solar-todos-os-dias'] },
      { v: 'textura', label: 'Textura, poros e viço', procs: ['laser-lavieen', 'skinbooster', 'exossomas-pdrn', 'laser-co2-fracionado'], arts: ['barreira-cutanea', 'rotina-de-skincare'] },
      { v: 'olhos', label: 'Olheiras e região dos olhos', procs: ['rejuvenescimento-periocular', 'exossomas-pdrn', 'toxina-botulinica'], arts: ['regiao-dos-olhos'] },
      { v: 'labios', label: 'Lábios e contorno da boca', procs: ['rejuvenescimento-labial', 'preenchimento-acido-hialuronico', 'skinbooster'], arts: ['rotina-de-skincare'] },
    ],
    corpo: [
      { v: 'flacidez', label: 'Flacidez da pele', procs: ['flacidez-corporal', 'bioestimuladores-de-colageno', 'ultrassom-microfocado'], arts: ['flacidez-apos-emagrecer'] },
      { v: 'gordura', label: 'Gordura localizada', procs: ['endolaser', 'intradermoterapia', 'flacidez-corporal'], arts: ['flacidez-apos-emagrecer'] },
      { v: 'gluteos', label: 'Glúteos e celulite', procs: ['harmonizacao-glutea', 'intradermoterapia', 'bioestimuladores-de-colageno'], arts: ['flacidez-apos-emagrecer'] },
      { v: 'colo', label: 'Colo, pescoço e mãos', procs: ['colo-pescoco-e-maos', 'skinbooster', 'fotoage-luz-intensa-pulsada'], arts: ['protetor-solar-todos-os-dias'] },
      { v: 'posparto', label: 'Cuidados no pós-parto', procs: ['cuidados-pos-parto', 'flacidez-corporal', 'consulta-capilar'], arts: ['queda-de-cabelo', 'flacidez-apos-emagrecer'] },
      { v: 'estrias', label: 'Estrias e cicatrizes', procs: ['laser-co2-fracionado', 'laser-lavieen', 'bioestimuladores-de-colageno'], arts: ['barreira-cutanea'] },
    ],
    cabelo: [
      { v: 'queda', label: 'Queda de cabelo', procs: ['consulta-capilar', 'drug-delivery-capilar', 'exossomas-capilares'], arts: ['queda-de-cabelo'] },
      { v: 'afinamento', label: 'Fios finos e falhas', procs: ['consulta-capilar', 'exossomas-capilares', 'prevencao-da-calvicie'], arts: ['queda-de-cabelo'] },
      { v: 'calvicie', label: 'Entradas e calvície', procs: ['prevencao-da-calvicie', 'drug-delivery-capilar', 'cuidados-masculinos'], arts: ['queda-de-cabelo'] },
      { v: 'transplante', label: 'Fiz ou vou fazer transplante', procs: ['protocolo-pos-transplante', 'exossomas-capilares', 'consulta-capilar'], arts: ['queda-de-cabelo'] },
      { v: 'couro', label: 'Coceira, caspa ou oleosidade', procs: ['consulta-capilar', 'drug-delivery-capilar'], arts: ['queda-de-cabelo', 'rotina-de-skincare'] },
    ],
    pele: [
      { v: 'sensivel', label: 'Pele sensível ou irritada', procs: ['exossomas-pdrn', 'skinbooster', 'laser-lavieen'], arts: ['barreira-cutanea', 'rotina-de-skincare'] },
      { v: 'acne', label: 'Acne e marcas de acne', procs: ['peeling-quimico', 'laser-co2-fracionado', 'laser-lavieen'], arts: ['rotina-de-skincare'] },
      { v: 'prevencao', label: 'Prevenção do envelhecimento', procs: ['bioestimuladores-de-colageno', 'skinbooster', 'toxina-botulinica'], arts: ['protetor-solar-todos-os-dias', 'barreira-cutanea'] },
      { v: 'rotina', label: 'Montar uma rotina de cuidados', procs: ['skinbooster', 'laser-lavieen', 'peeling-quimico'], arts: ['rotina-de-skincare', 'protetor-solar-todos-os-dias'] },
      { v: 'masculino', label: 'Cuidados masculinos', procs: ['cuidados-masculinos', 'toxina-botulinica', 'prevencao-da-calvicie'], arts: ['rotina-de-skincare'] },
    ],
  };
  const MOMENTS = [
    { v: 'prevenir', label: 'Quero prevenir', desc: 'Cuidar antes que os sinais apareçam', ico: 'leaf', txt: 'com foco em prevenção' },
    { v: 'primeiros', label: 'Notei os primeiros sinais', desc: 'Mudanças sutis que começaram a aparecer', ico: 'search', txt: 'agora que notou os primeiros sinais' },
    { v: 'tratar', label: 'Já me incomoda há algum tempo', desc: 'Busco tratar algo mais evidente', ico: 'plan', txt: 'e sente que é hora de tratar' },
    { v: 'especial', label: 'Momento especial', desc: 'Pós-parto, pós-emagrecimento ou um evento', ico: 'heart', txt: 'em um momento especial da sua vida' },
  ];
  const PREFS = [
    { v: 'rapido', label: 'Rotina corrida', desc: 'Prefiro pouco tempo de recuperação', ico: 'clock' },
    { v: 'tecnologia', label: 'Tecnologias e lasers', desc: 'Tenho interesse em equipamentos modernos', ico: 'tech' },
    { v: 'natural', label: 'Resultados graduais', desc: 'Busco mudanças naturais, passo a passo', ico: 'drop' },
    { v: 'entender', label: 'Quero entender tudo', desc: 'Prefiro conhecer as opções antes de decidir', ico: 'plan' },
  ];
  const QUICK = ['toxina-botulinica', 'skinbooster', 'ultrassom-microfocado', 'laser-lavieen', 'fotoage-luz-intensa-pulsada',
    'laser-nd-yag-q-switched', 'drug-delivery-capilar', 'intradermoterapia', 'exossomas-pdrn', 'exossomas-capilares', 'consulta-capilar'];
  const GRADUAL = ['bioestimuladores-de-colageno', 'skinbooster', 'exossomas-pdrn', 'consulta-capilar', 'prevencao-da-calvicie',
    'exossomas-capilares', 'colo-pescoco-e-maos', 'lifting-sem-cirurgia', 'flacidez-corporal'];

  const state = { area: null, interest: null, moment: null, pref: null };
  const history = [];
  let current = 'intro';

  /* ------------------------------------------------------------ Render */
  const optBtn = (o, i, selected) => `
    <button class="opt ${selected ? 'is-selected' : ''}" type="button" data-value="${o.v}" style="--oi:${i}">
      ${o.ico ? `<span class="opt__ico">${icon(o.ico)}</span>` : ''}
      <span class="opt__label">${esc(o.label)}${o.desc ? `<small style="display:block;font-weight:400;color:var(--muted);font-size:.78rem;margin-top:2px">${esc(o.desc)}</small>` : ''}</span>
      <span class="opt__arrow">${icon('arrow')}</span>
    </button>`;

  const SCREENS = {
    q1: () => ({
      step: 1,
      html: `<p class="eyebrow"><span class="eyebrow__mark"></span>Pergunta 1</p>
        <h2 class="qscreen__q" tabindex="-1">O que você gostaria de cuidar primeiro?</h2>
        <p class="qscreen__hint">Escolha a área que mais chama a sua atenção hoje.</p>
        <div class="qopts">${AREAS.map((o, i) => optBtn(o, i, state.area === o.v)).join('')}</div>`,
      key: 'area', next: 'q2',
    }),
    q2: () => ({
      step: 2,
      html: `<p class="eyebrow"><span class="eyebrow__mark"></span>Pergunta 2</p>
        <h2 class="qscreen__q" tabindex="-1">O que mais chama a sua atenção?</h2>
        <p class="qscreen__hint">Selecione o tema que você mais gostaria de entender.</p>
        <div class="qopts">${INTERESTS[state.area].map((o, i) => optBtn(o, i, state.interest === o.v)).join('')}</div>`,
      key: 'interest', next: 'q3',
    }),
    q3: () => ({
      step: 3,
      html: `<p class="eyebrow"><span class="eyebrow__mark"></span>Pergunta 3</p>
        <h2 class="qscreen__q" tabindex="-1">Qual é o seu momento?</h2>
        <p class="qscreen__hint">Não existe resposta certa — é só para entendermos o seu contexto.</p>
        <div class="qopts">${MOMENTS.map((o, i) => optBtn(o, i, state.moment === o.v)).join('')}</div>`,
      key: 'moment', next: 'q4',
    }),
    q4: () => ({
      step: 4,
      html: `<p class="eyebrow"><span class="eyebrow__mark"></span>Pergunta 4</p>
        <h2 class="qscreen__q" tabindex="-1">Como você prefere conduzir o seu cuidado?</h2>
        <p class="qscreen__hint">Assim mostramos primeiro o que combina com o seu estilo.</p>
        <div class="qopts">${PREFS.map((o, i) => optBtn(o, i, state.pref === o.v)).join('')}</div>`,
      key: 'pref', next: 'result',
    }),
    result: () => ({ step: 5, html: resultHTML() }),
  };

  function pick(list, v) { return list.find((o) => o.v === v); }

  function resultHTML() {
    const area = pick(AREAS, state.area);
    const it = pick(INTERESTS[state.area], state.interest);
    const mo = pick(MOMENTS, state.moment);
    const pr = pick(PREFS, state.pref);
    let procs = it.procs.slice();
    if (state.pref === 'tecnologia') procs.sort((a, b) => (DATA.procs[b].tipo === 'Tecnologia') - (DATA.procs[a].tipo === 'Tecnologia'));
    if (state.pref === 'rapido') procs.sort((a, b) => QUICK.includes(b) - QUICK.includes(a));
    if (state.pref === 'natural') procs.sort((a, b) => GRADUAL.includes(b) - GRADUAL.includes(a));
    procs = procs.slice(0, 3).map((s) => DATA.procs[s]).filter(Boolean);
    const arts = it.arts.map((s) => DATA.arts[s]).filter(Boolean).slice(0, 2);
    const titles = { rosto: 'pelo <em>rosto</em>', corpo: 'pelo <em>corpo</em>', cabelo: 'pelos <em>seus fios</em>', pele: 'pela <em>saúde da pele</em>' };
    const msg = `Olá! Fiz o "Descubra seu cuidado" no site da Vinovare.\n• Área: ${area.label}\n• Interesse: ${it.label}\n• Momento: ${mo.label}\n• Preferência: ${pr.label}\nGostaria de agendar uma avaliação com a Dra. Karinie Marinho.`;
    const img = (name) => `${BASE}assets/img/${name}-800.webp`;

    return `
      <p class="eyebrow"><span class="eyebrow__mark"></span>Seu resultado</p>
      <h2 class="qscreen__title" tabindex="-1">Seu cuidado começa ${titles[state.area]}</h2>
      <div class="qresult__chips">${[area.label, it.label, mo.label, pr.label].map((c) => `<span>${esc(c)}</span>`).join('')}</div>
      <p class="qscreen__lead">Você quer cuidar de <strong>${esc(it.label.toLowerCase())}</strong> ${esc(mo.txt)}. Estes são alguns caminhos que a Dra. Karinie pode avaliar com você — a indicação final sempre acontece na consulta.</p>
      <p class="qresult__label">Tratamentos para conhecer</p>
      <div class="qresult__procs">
        ${procs.map((p, i) => `
          <a class="rcard" href="${BASE}procedimentos/${p.slug}.html" style="--oi:${i}">
            <div class="rcard__img"><img src="${img(p.img)}" alt="" loading="lazy"></div>
            <div class="rcard__body"><small>${esc(p.tipo)}</small><strong>${esc(p.nome)}</strong><p>${esc(p.curto)}</p></div>
          </a>`).join('')}
      </div>
      ${arts.length ? `<p class="qresult__label">Leituras recomendadas</p>
      <div class="qresult__arts">
        ${arts.map((a) => `
          <a class="qart" href="${BASE}conteudos/${a.slug}.html">
            <img src="${img(a.img)}" alt="" loading="lazy">
            <span><small>${esc(a.categoria)} · ${a.leitura} min</small><strong>${esc(a.titulo)}</strong></span>
          </a>`).join('')}
      </div>` : ''}
      <div class="qresult__cta">
        <p>Que tal transformar isso em um plano feito para você?<small>Na avaliação, a Dra. Karinie analisa sua pele, seu histórico e seus objetivos antes de indicar qualquer tratamento.</small></p>
        <a class="btn btn--light" href="https://wa.me/${WA}?text=${encodeURIComponent(msg)}" target="_blank" rel="noopener">
          <span class="btn__label">Agendar avaliação</span><span class="btn__ico">${icon('whatsapp')}</span>
        </a>
      </div>
      <button class="qresult__restart" type="button" data-quiz-restart>${icon('arrow-left')} Refazer o questionário</button>`;
  }

  function setSlide(i) {
    slides.forEach((s) => s.classList.toggle('is-active', Number(s.dataset.slide) === i));
  }

  function show(id, dir = 1) {
    const prev = $('.qscreen.is-active', stage);
    let el;
    if (id === 'intro') {
      el = $('[data-screen="intro"]', stage);
    } else {
      const def = SCREENS[id]();
      el = document.createElement('div');
      el.className = 'qscreen';
      el.dataset.screen = id;
      el.innerHTML = def.html;
      el.dataset.key = def.key || '';
      el.dataset.next = def.next || '';
      el.dataset.step = def.step;
    }
    const swap = () => {
      if (prev && prev !== el) {
        prev.classList.remove('is-active', 'is-leaving');
        if (prev.dataset.screen !== 'intro') prev.remove();
      }
      if (!el.isConnected) stage.appendChild(el);
      el.classList.add('is-active');
      current = id;
      wire(el);
      const step = Number(el.dataset.step || 0);
      bar.style.width = `${id === 'intro' ? 0 : Math.min(step, 4) / 4 * 100}%`;
      stepEl.textContent = id === 'intro' ? '' : step <= 4 ? `Pergunta ${step} de 4` : 'Resultado';
      back.hidden = id === 'intro';
      const area = pick(AREAS, state.area);
      setSlide(id === 'intro' || id === 'q1' ? 0 : id === 'result' ? (area ? area.slide : 5) : (area ? area.slide : 0));
      const focusEl = $('[tabindex="-1"]', el);
      if (focusEl) focusEl.focus({ preventScroll: true });
      if (window.innerWidth <= 1100) root.querySelector('.quiz__main').scrollIntoView({ behavior: 'smooth', block: 'start' });
    };
    if (prev && prev !== el && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
      prev.classList.add('is-leaving');
      setTimeout(swap, 320);
    } else swap();
  }

  function go(id) { history.push(current); show(id); }

  function wire(el) {
    $$('.opt', el).forEach((b) => b.addEventListener('click', () => {
      const key = el.dataset.key;
      if (!key) return;
      if (key === 'area' && state.area !== b.dataset.value) state.interest = null;
      state[key] = b.dataset.value;
      $$('.opt', el).forEach((x) => x.classList.toggle('is-selected', x === b));
      setTimeout(() => go(el.dataset.next), 280);
    }));
    const restart = $('[data-quiz-restart]', el);
    restart && restart.addEventListener('click', () => {
      Object.keys(state).forEach((k) => { state[k] = null; });
      history.length = 0;
      history.push('intro');
      show('q1');
    });
  }

  $('[data-quiz-start]', root).addEventListener('click', () => go('q1'));
  back.addEventListener('click', () => { if (history.length) show(history.pop(), -1); });

  // Entrada direta pela home (?area=rosto)
  const param = new URLSearchParams(location.search).get('area');
  if (param && INTERESTS[param]) {
    state.area = param;
    history.push('intro', 'q1');
    show('q2');
  }
})();
