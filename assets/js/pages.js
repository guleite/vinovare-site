/* ==========================================================================
   VINOVARE — interações das páginas internas
   ========================================================================== */
(() => {
  'use strict';

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const WA = document.body.dataset.wa || '5561991744080';
  const waLink = (text) => `https://wa.me/${WA}?text=${encodeURIComponent(text)}`;
  const onScroll = (fn) => {
    let t = false;
    const run = () => { if (t) return; t = true; requestAnimationFrame(() => { fn(); t = false; }); };
    window.addEventListener('scroll', run, { passive: true });
    window.addEventListener('resize', run);
    fn();
  };

  /* ------------------------------------------------------------ Tratamentos: filtro por área + busca */
  const trat = $('[data-trat]');
  if (trat) {
    const seg = $('[data-seg]', trat);
    const ind = $('.seg__ind', seg);
    const btns = $$('.seg__btn', seg);
    const cards = $$('.trat__card', trat);
    const intros = $$('[data-intro]', trat);
    const search = $('[data-search]', trat);
    const empty = $('[data-empty]', trat);
    let area = 'todos';

    const moveInd = (btn) => {
      ind.style.width = `${btn.offsetWidth}px`;
      ind.style.transform = `translateX(${btn.offsetLeft}px)`;
    };
    const apply = () => {
      const q = (search.value || '').trim().toLowerCase();
      let shown = 0;
      cards.forEach((c, i) => {
        const okArea = area === 'todos' || c.dataset.areas.split(' ').includes(area);
        const okText = !q || c.dataset.name.includes(q);
        const show = okArea && okText;
        if (show) {
          shown++;
          c.classList.remove('is-gone');
          requestAnimationFrame(() => { c.style.transitionDelay = `${Math.min(i, 12) * 30}ms`; c.classList.remove('is-out'); });
        } else {
          c.classList.add('is-out', 'is-gone');
        }
      });
      intros.forEach((el) => { el.hidden = el.dataset.intro !== area || !!q; });
      empty.hidden = shown > 0;
    };
    const setArea = (a, push) => {
      area = ['rosto', 'corpo', 'cabelo'].includes(a) ? a : 'todos';
      btns.forEach((b) => {
        const on = b.dataset.filter === area;
        b.classList.toggle('is-active', on);
        b.setAttribute('aria-selected', String(on));
        if (on) moveInd(b);
      });
      apply();
      if (push) history.replaceState(null, '', area === 'todos' ? location.pathname : `#${area}`);
    };
    btns.forEach((b) => b.addEventListener('click', () => {
      setArea(b.dataset.filter, true);
      const top = trat.getBoundingClientRect().top + window.scrollY - 10;
      if (window.scrollY > top + 40) window.scrollTo({ top, behavior: reduced ? 'auto' : 'smooth' });
    }));
    search.addEventListener('input', apply);
    window.addEventListener('resize', () => moveInd($('.seg__btn.is-active', seg)));
    window.addEventListener('hashchange', () => setArea(location.hash.slice(1), false));
    setArea(location.hash.slice(1), false);
    if (document.fonts) document.fonts.ready.then(() => moveInd($('.seg__btn.is-active', seg)));
  }

  /* ------------------------------------------------------------ Procedimento: subnavegação ativa */
  const subnav = $('[data-subnav]');
  if (subnav) {
    const links = $$('a[href^="#"]', subnav);
    const targets = links.map((a) => $(a.getAttribute('href'))).filter(Boolean);
    onScroll(() => {
      const line = window.innerHeight * 0.35;
      let current = targets[0];
      targets.forEach((t) => { if (t.getBoundingClientRect().top < line) current = t; });
      links.forEach((a) => a.classList.toggle('is-active', current && a.getAttribute('href') === `#${current.id}`));
    });
  }

  /* ------------------------------------------------------------ Dra.: linha do tempo */
  const tl = $('[data-timeline]');
  if (tl) {
    const fill = $('[data-timeline-fill]', tl);
    const list = $('.timeline', tl);
    onScroll(() => {
      const r = list.getBoundingClientRect();
      const vh = window.innerHeight;
      const p = clamp((vh * 0.85 - r.top) / (r.height + vh * 0.25), 0, 1);
      fill.parentElement.style.setProperty('--tl', p.toFixed(3));
    });
  }

  /* ------------------------------------------------------------ Clínica: tour horizontal fixo */
  const tour = $('[data-htour]');
  if (tour) {
    const track = $('[data-tour-track]', tour);
    const prog = $('[data-tour-progress]', tour);
    const cur = $('[data-tour-current]', tour);
    const slides = $$('.tour__slide', tour);
    onScroll(() => {
      if (window.innerWidth <= 980) {
        track.style.transform = '';
        return;
      }
      const r = tour.getBoundingClientRect();
      const total = tour.offsetHeight - window.innerHeight;
      const p = clamp(-r.top / total, 0, 1);
      const max = track.scrollWidth - window.innerWidth;
      track.style.transform = `translate3d(${(-p * max).toFixed(1)}px, 0, 0)`;
      prog.style.setProperty('--tp', p.toFixed(3));
      cur.textContent = String(Math.min(slides.length, Math.floor(p * slides.length) + 1)).padStart(2, '0');
    });
  }

  /* ------------------------------------------------------------ Conteúdos: filtro por categoria */
  const blog = $('[data-blog]');
  if (blog) {
    const chips = $$('.blog__filters .chip', blog);
    const items = $$('.feature, .blog__cell', blog);
    chips.forEach((c) => c.addEventListener('click', () => {
      chips.forEach((x) => x.classList.toggle('is-active', x === c));
      const cat = c.dataset.cat;
      items.forEach((it) => {
        const show = cat === 'todos' || it.dataset.cat === cat;
        it.classList.toggle('is-gone', !show);
        if (show) { it.classList.remove('is-in'); requestAnimationFrame(() => it.classList.add('is-in')); }
      });
    }));
  }

  /* ------------------------------------------------------------ Artigo: sumário, progresso de leitura, copiar link */
  const prose = $('[data-prose]');
  if (prose) {
    const toc = $('[data-toc]');
    const heads = $$('h2', prose);
    heads.forEach((h, i) => {
      if (!h.id) h.id = `secao-${i + 1}`;
      const li = document.createElement('li');
      li.innerHTML = `<a href="#${h.id}"></a>`;
      li.firstChild.textContent = h.textContent;
      toc.appendChild(li);
    });
    const tocLinks = $$('a', toc);
    const bar = $('[data-read-progress]');
    onScroll(() => {
      const r = prose.getBoundingClientRect();
      const p = clamp(-r.top / (r.height - window.innerHeight * 0.6), 0, 1);
      bar.parentElement.style.setProperty('--rp', p.toFixed(3));
      let current = null;
      heads.forEach((h) => { if (h.getBoundingClientRect().top < window.innerHeight * 0.3) current = h; });
      tocLinks.forEach((a) => a.classList.toggle('is-active', current && a.getAttribute('href') === `#${current.id}`));
    });
    const copy = $('[data-copy-link]');
    copy && copy.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(location.href); copy.textContent = 'Link copiado!'; }
      catch (e) { copy.textContent = location.href; }
      setTimeout(() => { copy.textContent = 'Copiar link'; }, 2200);
    });
  }

  /* ------------------------------------------------------------ Agendamento */
  const book = $('[data-book]');
  if (book) {
    // Abas
    const tabs = $('.tabs', book);
    const tabBtns = $$('.tabs__btn', book);
    const panels = $$('[data-panel]', book);
    const setTab = (id) => {
      tabs.dataset.active = id;
      tabBtns.forEach((b) => { const on = b.dataset.tab === id; b.classList.toggle('is-active', on); b.setAttribute('aria-selected', String(on)); });
      panels.forEach((p) => { p.hidden = p.dataset.panel !== id; p.classList.toggle('is-active', p.dataset.panel === id); });
    };
    tabBtns.forEach((b) => b.addEventListener('click', () => setTab(b.dataset.tab)));
    if (location.hash === '#agenda') setTab('cal');

    // Formulário → WhatsApp
    const form = $('[data-wa-form]', book);
    const areaSel = $('[data-area-select]', form);
    const tratSel = $('[data-trat-select]', form);
    areaSel.addEventListener('change', () => {
      const a = areaSel.value;
      $$('option', tratSel).forEach((o) => {
        if (!o.value) return;
        o.hidden = !!a && !o.dataset.areas.split(' ').includes(a);
      });
      if (tratSel.selectedOptions[0] && tratSel.selectedOptions[0].hidden) tratSel.value = '';
    });
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const nome = form.nome.value.trim();
      if (!nome) { form.nome.classList.add('is-invalid'); form.nome.focus(); return; }
      form.nome.classList.remove('is-invalid');
      const area = areaSel.value ? areaSel.selectedOptions[0].textContent : 'Ainda não sei';
      const linhas = [
        `Olá! Meu nome é ${nome} e gostaria de agendar uma avaliação com a Dra. Karinie Marinho.`,
        `• Área de interesse: ${area}`,
        tratSel.value ? `• Tratamento: ${tratSel.value}` : null,
        `• Melhor período: ${form.periodo.value}`,
        form.msg.value.trim() ? `• Mensagem: ${form.msg.value.trim()}` : null,
      ].filter(Boolean);
      window.open(waLink(linhas.join('\n')), '_blank', 'noopener');
    });

    // Calendário
    const cal = $('.cal', book);
    const monthEl = $('[data-cal-month]', cal);
    const daysEl = $('[data-cal-days]', cal);
    const slotsEl = $('[data-cal-slots]', cal);
    const labelEl = $('[data-cal-label]', cal);
    const summary = $('[data-cal-summary]', cal);
    const choiceEl = $('[data-cal-choice]', cal);
    const send = $('[data-cal-send]', cal);
    const prevBtn = $('[data-cal-prev]', cal);
    const nextBtn = $('[data-cal-next]', cal);
    const today = new Date(); today.setHours(0, 0, 0, 0);
    const minDate = new Date(today); minDate.setDate(minDate.getDate() + 1);
    const maxDate = new Date(today); maxDate.setDate(maxDate.getDate() + 60);
    let view = new Date(today.getFullYear(), today.getMonth(), 1);
    let selDate = null; let selSlot = null;
    const fmtMonth = new Intl.DateTimeFormat('pt-BR', { month: 'long', year: 'numeric' });
    const fmtDay = new Intl.DateTimeFormat('pt-BR', { weekday: 'long', day: 'numeric', month: 'long' });
    const WEEK = ['08:30', '09:30', '10:30', '11:30', '14:00', '15:00', '16:00', '17:00'];
    const SAT = ['09:00', '10:00', '11:00'];
    // Disponibilidade ilustrativa (determinística por data) — substituir pela API da agenda da clínica.
    const busy = (d, i) => ((d.getDate() * 7 + d.getMonth() * 3 + i * 5) % 9) < 3;

    const renderSlots = () => {
      slotsEl.innerHTML = '';
      summary.hidden = true;
      if (!selDate) { labelEl.textContent = 'Selecione um dia disponível'; return; }
      const sat = selDate.getDay() === 6;
      labelEl.textContent = sat ? 'Sábado — horários mediante agendamento' : 'Horários disponíveis';
      (sat ? SAT : WEEK).forEach((h, i) => {
        const b = document.createElement('button');
        b.type = 'button'; b.className = 'slot'; b.textContent = h; b.style.setProperty('--oi', i);
        if (busy(selDate, i)) { b.disabled = true; b.style.opacity = '.35'; b.title = 'Indisponível'; }
        b.addEventListener('click', () => {
          selSlot = h;
          $$('.slot', slotsEl).forEach((x) => x.classList.toggle('is-selected', x === b));
          const txt = `${fmtDay.format(selDate)} · ${h}`;
          choiceEl.textContent = txt.charAt(0).toUpperCase() + txt.slice(1);
          send.href = waLink(`Olá! Gostaria de solicitar uma avaliação com a Dra. Karinie Marinho na ${fmtDay.format(selDate)}, às ${h}. Esse horário está disponível?`);
          summary.hidden = false;
        });
        slotsEl.appendChild(b);
      });
    };
    const renderCal = () => {
      const mtxt = fmtMonth.format(view);
      monthEl.textContent = mtxt.charAt(0).toUpperCase() + mtxt.slice(1);
      daysEl.innerHTML = '';
      const first = new Date(view.getFullYear(), view.getMonth(), 1);
      const last = new Date(view.getFullYear(), view.getMonth() + 1, 0);
      for (let i = 0; i < first.getDay(); i++) {
        const s = document.createElement('span'); s.className = 'cal__day is-empty'; daysEl.appendChild(s);
      }
      for (let d = 1; d <= last.getDate(); d++) {
        const date = new Date(view.getFullYear(), view.getMonth(), d);
        const b = document.createElement('button');
        b.type = 'button'; b.className = 'cal__day'; b.textContent = d;
        b.setAttribute('aria-label', fmtDay.format(date));
        if (date.getTime() === today.getTime()) b.classList.add('is-today');
        if (date.getDay() === 6) b.classList.add('is-sat');
        if (date < minDate || date > maxDate || date.getDay() === 0) b.disabled = true;
        if (selDate && date.getTime() === selDate.getTime()) b.classList.add('is-selected');
        b.addEventListener('click', () => {
          selDate = date; selSlot = null;
          $$('.cal__day', daysEl).forEach((x) => x.classList.toggle('is-selected', x === b));
          renderSlots();
        });
        daysEl.appendChild(b);
      }
      const thisMonth = new Date(today.getFullYear(), today.getMonth(), 1);
      prevBtn.disabled = view <= thisMonth;
      nextBtn.disabled = new Date(view.getFullYear(), view.getMonth() + 1, 1) > maxDate;
    };
    prevBtn.addEventListener('click', () => { view = new Date(view.getFullYear(), view.getMonth() - 1, 1); renderCal(); });
    nextBtn.addEventListener('click', () => { view = new Date(view.getFullYear(), view.getMonth() + 1, 1); renderCal(); });
    renderCal();
    renderSlots();
  }
})();
