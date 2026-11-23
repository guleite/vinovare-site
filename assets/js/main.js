/* ==========================================================================
   VINOVARE — interações globais
   Sem dependências. Respeita prefers-reduced-motion.
   ========================================================================== */
(() => {
  'use strict';

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const html = document.documentElement;
  const body = document.body;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const lerp = (a, b, t) => a + (b - a) * t;

  /* ------------------------------------------------------------ Intro */
  const introSeen = html.classList.contains('intro-seen');
  try { sessionStorage.setItem('vv-intro', '1'); } catch (e) { /* modo privado */ }
  const introDelay = introSeen || reduced ? 120 : 2250;

  /* ------------------------------------------------------------ Split de títulos */
  function splitWords(el) {
    let idx = 0;
    const walk = (node) => {
      [...node.childNodes].forEach((child) => {
        if (child.nodeType === 3) {
          const frag = document.createDocumentFragment();
          child.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
            const w = document.createElement('span');
            w.className = 'w';
            const i = document.createElement('span');
            i.className = 'w__i';
            i.textContent = part;
            i.style.setProperty('--wi', idx++);
            w.appendChild(i);
            frag.appendChild(w);
          });
          child.replaceWith(frag);
        } else if (child.nodeType === 1 && child.tagName !== 'BR') {
          walk(child);
        }
      });
    };
    walk(el);
  }
  $$('[data-split]').forEach(splitWords);

  /* ------------------------------------------------------------ Palavras do manifesto */
  const wordBlocks = $$('[data-words]').map((el) => {
    const words = [];
    const walk = (node) => {
      [...node.childNodes].forEach((child) => {
        if (child.nodeType === 3) {
          const frag = document.createDocumentFragment();
          child.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
            const s = document.createElement('span');
            s.className = 'mw';
            s.textContent = part;
            words.push(s);
            frag.appendChild(s);
          });
          child.replaceWith(frag);
        } else if (child.nodeType === 1 && child.classList.contains('pill-img')) {
          child.classList.add('mw');
          words.push(child);
        } else if (child.nodeType === 1) {
          walk(child);
        }
      });
    };
    walk(el);
    return { el, words };
  });

  /* ------------------------------------------------------------ Revelação ao rolar */
  const revealTargets = () => $$('[data-reveal], [data-split], .diff, [data-journey], [data-count]');
  let io;
  function startReveal() {
    body.classList.add('is-ready');
    if (reduced || !('IntersectionObserver' in window)) {
      revealTargets().forEach((el) => el.classList.add('is-in'));
      return;
    }
    io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        en.target.classList.add('is-in');
        if (en.target.hasAttribute('data-count')) countUp(en.target);
        io.unobserve(en.target);
      });
    }, { threshold: 0.14, rootMargin: '0px 0px -6% 0px' });
    revealTargets().forEach((el) => io.observe(el));
  }
  setTimeout(startReveal, introDelay);

  function countUp(el) {
    const end = parseFloat(el.dataset.count);
    if (reduced || Number.isNaN(end)) return;
    const t0 = performance.now();
    const dur = 1600;
    const tick = (t) => {
      const p = clamp((t - t0) / dur, 0, 1);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  /* ------------------------------------------------------------ Header */
  const hdr = $('[data-hdr]');
  let lastY = window.scrollY;
  function onScrollHeader() {
    const y = window.scrollY;
    if (!hdr) return;
    hdr.classList.toggle('is-scrolled', y > 30);
    const goingDown = y > lastY + 4;
    const goingUp = y < lastY - 4;
    if (goingDown && y > 320 && !body.classList.contains('menu-open') && !hdr.matches(':hover')) hdr.classList.add('is-hidden');
    else if (goingUp || y < 120) hdr.classList.remove('is-hidden');
    lastY = y;
  }

  /* ------------------------------------------------------------ Menu mobile */
  const burger = $('[data-burger]');
  const menu = $('[data-menu]');
  if (burger && menu) {
    $$('.menu__list li', menu).forEach((li, i) => li.style.setProperty('--mi', i));
    const setMenu = (open) => {
      body.classList.toggle('menu-open', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
      menu.setAttribute('aria-hidden', String(!open));
      if (open) hdr.classList.remove('is-hidden');
    };
    burger.addEventListener('click', () => setMenu(!body.classList.contains('menu-open')));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
    $$('a', menu).forEach((a) => a.addEventListener('click', () => setTimeout(() => setMenu(false), 200)));
  }

  /* ------------------------------------------------------------ Áreas interativas */
  $$('[data-areas]').forEach((wrap) => {
    const items = $$('.area', wrap);
    const closeAll = () => {
      wrap.classList.remove('is-open');
      items.forEach((a) => {
        a.classList.remove('is-active');
        $('.area__trigger', a).setAttribute('aria-expanded', 'false');
      });
    };
    items.forEach((a) => {
      const trig = $('.area__trigger', a);
      trig.addEventListener('click', () => {
        const wasActive = a.classList.contains('is-active');
        closeAll();
        if (wasActive) return;
        wrap.classList.add('is-open');
        a.classList.add('is-active');
        trig.setAttribute('aria-expanded', 'true');
        if (window.innerWidth <= 900) {
          setTimeout(() => a.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' }), 80);
        }
        setTimeout(() => $('.area__close', a).focus({ preventScroll: true }), 700);
      });
      $('.area__close', a).addEventListener('click', (e) => {
        e.stopPropagation();
        closeAll();
        trig.focus({ preventScroll: true });
      });
    });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && wrap.classList.contains('is-open')) closeAll(); });
  });

  /* ------------------------------------------------------------ Carrossel com arraste */
  $$('[data-carousel]').forEach((c) => {
    const track = $('[data-carousel-track]', c);
    if (!track) return;
    const prog = $('[data-carousel-progress]', c);
    const prev = $('[data-carousel-prev]', c);
    const next = $('[data-carousel-next]', c);
    const step = () => {
      const card = track.firstElementChild;
      return card ? card.getBoundingClientRect().width + 26 : 320;
    };
    const update = () => {
      const max = track.scrollWidth - track.clientWidth;
      const p = max > 0 ? track.scrollLeft / max : 1;
      if (prog) prog.style.setProperty('--p', Math.max(0.08, p).toFixed(3));
      if (prev) prev.disabled = track.scrollLeft < 8;
      if (next) next.disabled = track.scrollLeft > max - 8;
    };
    prev && prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
    next && next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();

    let down = false; let startX = 0; let startLeft = 0; let moved = false;
    track.addEventListener('pointerdown', (e) => {
      if (e.pointerType !== 'mouse' || e.button !== 0) return;
      down = true; moved = false; startX = e.clientX; startLeft = track.scrollLeft;
    });
    window.addEventListener('pointermove', (e) => {
      if (!down) return;
      const dx = e.clientX - startX;
      if (!moved && Math.abs(dx) > 6) { moved = true; track.classList.add('is-dragging'); }
      if (moved) track.scrollLeft = startLeft - dx;
    });
    window.addEventListener('pointerup', () => {
      if (!down) return;
      down = false;
      setTimeout(() => track.classList.remove('is-dragging'), 30);
    });
    track.addEventListener('click', (e) => { if (moved) { e.preventDefault(); moved = false; } }, true);
  });

  /* ------------------------------------------------------------ Parallax ao rolar */
  const parallaxEls = $$('[data-parallax]');
  function onScrollParallax() {
    if (reduced) return;
    const vh = window.innerHeight;
    parallaxEls.forEach((el) => {
      const host = el.parentElement;
      const r = host.getBoundingClientRect();
      if (r.bottom < -100 || r.top > vh + 100) return;
      const f = parseFloat(el.dataset.parallax) || 0.08;
      const off = (r.top + r.height / 2 - vh / 2) * -f;
      el.style.transform = `translate3d(0, ${off.toFixed(1)}px, 0)`;
    });
  }

  /* ------------------------------------------------------------ Manifesto: palavras acendem */
  function onScrollWords() {
    const vh = window.innerHeight;
    wordBlocks.forEach(({ el, words }) => {
      const r = el.getBoundingClientRect();
      const p = clamp((vh * 0.82 - r.top) / (r.height + vh * 0.3), 0, 1);
      const n = Math.round(p * words.length);
      words.forEach((w, i) => w.classList.toggle('on', i < n));
    });
  }

  /* ------------------------------------------------------------ Jornada: etapa ativa */
  const journey = $('[data-journey]');
  const jsteps = journey ? $$('.jstep', journey) : [];
  let jTimer = null;
  function journeyMode() {
    if (!journey) return;
    clearInterval(jTimer);
    jsteps.forEach((s) => s.classList.remove('is-active'));
    if (window.innerWidth > 1100 && !reduced) {
      let k = 0;
      jTimer = setInterval(() => {
        if (!journey.classList.contains('is-in')) return;
        jsteps.forEach((s, i) => s.classList.toggle('is-active', i === k));
        k = (k + 1) % jsteps.length;
      }, 1500);
    }
  }
  function onScrollJourney() {
    if (!journey || window.innerWidth > 1100) return;
    const line = window.innerHeight * 0.62;
    jsteps.forEach((s) => s.classList.toggle('is-active', s.getBoundingClientRect().top < line));
  }
  journeyMode();
  window.addEventListener('resize', journeyMode);

  /* ------------------------------------------------------------ Loop de rolagem */
  let ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      onScrollHeader();
      onScrollParallax();
      onScrollWords();
      onScrollJourney();
      document.dispatchEvent(new CustomEvent('vv:scroll'));
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();

  /* ------------------------------------------------------------ Profundidade com o mouse */
  if (finePointer && !reduced) {
    $$('[data-hero-visual], .qt__visual, .about__visual').forEach((zone) => {
      const layers = $$('[data-depth]', zone);
      if (!layers.length) return;
      const host = zone.closest('section') || zone;
      let tx = 0; let ty = 0; let cx = 0; let cy = 0; let raf = null;
      const loop = () => {
        cx = lerp(cx, tx, 0.08); cy = lerp(cy, ty, 0.08);
        layers.forEach((l) => {
          const d = parseFloat(l.dataset.depth) || 1;
          l.style.translate = `${(cx * d * 12).toFixed(2)}px ${(cy * d * 12).toFixed(2)}px`;
        });
        raf = (Math.abs(cx - tx) > 0.001 || Math.abs(cy - ty) > 0.001) ? requestAnimationFrame(loop) : null;
      };
      host.addEventListener('mousemove', (e) => {
        const r = host.getBoundingClientRect();
        tx = ((e.clientX - r.left) / r.width - 0.5) * 2;
        ty = ((e.clientY - r.top) / r.height - 0.5) * 2;
        if (!raf) raf = requestAnimationFrame(loop);
      });
      host.addEventListener('mouseleave', () => { tx = 0; ty = 0; if (!raf) raf = requestAnimationFrame(loop); });
    });
  }

  /* ------------------------------------------------------------ Cursor personalizado */
  const cursor = $('.cursor');
  if (cursor && finePointer && !reduced) {
    const label = $('.cursor__label', cursor);
    let mx = -100; let my = -100; let x = -100; let y = -100;
    window.addEventListener('mousemove', (e) => { mx = e.clientX; my = e.clientY; cursor.classList.add('is-visible'); }, { passive: true });
    document.addEventListener('mouseleave', () => cursor.classList.remove('is-visible'));
    const loop = () => {
      x = lerp(x, mx, 0.2); y = lerp(y, my, 0.2);
      cursor.style.transform = `translate3d(${x}px, ${y}px, 0)`;
      requestAnimationFrame(loop);
    };
    loop();
    document.addEventListener('mouseover', (e) => {
      const lab = e.target.closest('[data-cursor]');
      const link = e.target.closest('a, button, summary, label, input, select, textarea');
      cursor.classList.toggle('is-label', !!lab);
      cursor.classList.toggle('is-link', !lab && !!link);
      label.textContent = lab ? lab.dataset.cursor : '';
    });
  }

  /* ------------------------------------------------------------ Botões magnéticos */
  if (finePointer && !reduced) {
    $$('[data-magnetic]').forEach((el) => {
      el.addEventListener('mousemove', (e) => {
        const r = el.getBoundingClientRect();
        const dx = e.clientX - (r.left + r.width / 2);
        const dy = e.clientY - (r.top + r.height / 2);
        el.style.translate = `${dx * 0.18}px ${dy * 0.3}px`;
      });
      el.addEventListener('mouseleave', () => { el.style.translate = '0 0'; });
    });
  }

  /* ------------------------------------------------------------ FAQ (acordeão suave) */
  $$('.faq__item').forEach((d) => {
    const sum = $('summary', d);
    const panel = $('.faq__a', d);
    sum.addEventListener('click', (e) => {
      if (reduced || !panel.animate) return;
      e.preventDefault();
      const ease = 'cubic-bezier(.22,1,.36,1)';
      if (d.open) {
        d.classList.add('is-closing');
        const h = panel.offsetHeight;
        panel.animate([{ height: `${h}px`, opacity: 1 }, { height: '0px', opacity: 0 }], { duration: 420, easing: ease })
          .onfinish = () => { d.open = false; d.classList.remove('is-closing'); };
      } else {
        d.open = true;
        const h = panel.offsetHeight;
        panel.animate([{ height: '0px', opacity: 0 }, { height: `${h}px`, opacity: 1 }], { duration: 560, easing: ease });
      }
    });
  });

  /* ------------------------------------------------------------ Modal (vídeo / galeria) */
  const modal = $('[data-modal]');
  const modalBody = modal && $('[data-modal-body]', modal);
  let lastFocus = null;
  let gallery = null;
  function openModal(content) {
    if (!modal) return;
    lastFocus = document.activeElement;
    modalBody.innerHTML = '';
    modalBody.appendChild(content);
    modal.hidden = false;
    body.classList.add('modal-open');
    $('.modal__close', modal).focus({ preventScroll: true });
  }
  function closeModal() {
    if (!modal || modal.hidden) return;
    modal.hidden = true;
    modalBody.innerHTML = '';
    body.classList.remove('modal-open');
    gallery = null;
    if (lastFocus) lastFocus.focus({ preventScroll: true });
  }
  window.vvModal = { open: openModal, close: closeModal };
  if (modal) {
    $$('[data-modal-close]', modal).forEach((b) => b.addEventListener('click', closeModal));
    document.addEventListener('keydown', (e) => {
      if (modal.hidden) return;
      if (e.key === 'Escape') closeModal();
      if (gallery && e.key === 'ArrowRight') showSlide(gallery.i + 1);
      if (gallery && e.key === 'ArrowLeft') showSlide(gallery.i - 1);
    });
  }
  document.addEventListener('click', (e) => {
    const v = e.target.closest('[data-video]');
    if (!v) return;
    e.preventDefault();
    const wrap = document.createElement('div');
    const video = document.createElement('video');
    video.src = v.dataset.video;
    video.controls = true; video.autoplay = true; video.playsInline = true; video.muted = false;
    if (v.dataset.poster) video.poster = v.dataset.poster;
    wrap.appendChild(video);
    if (v.dataset.caption) {
      const p = document.createElement('p');
      p.className = 'modal__caption';
      p.textContent = v.dataset.caption;
      wrap.appendChild(p);
    }
    openModal(wrap);
  });

  function showSlide(i) {
    if (!gallery) return;
    const n = gallery.items.length;
    gallery.i = (i + n) % n;
    const item = gallery.items[gallery.i];
    const img = $('img', modalBody);
    const cap = $('.modal__caption', modalBody);
    img.src = item.dataset.full || $('img', item).currentSrc;
    img.alt = $('img', item).alt;
    cap.textContent = `${gallery.i + 1} / ${n}${item.dataset.caption ? ' — ' + item.dataset.caption : ''}`;
  }
  document.addEventListener('click', (e) => {
    const item = e.target.closest('[data-lightbox]');
    if (!item) return;
    e.preventDefault();
    const group = item.dataset.lightbox;
    const items = $$(`[data-lightbox="${group}"]`);
    gallery = { items, i: items.indexOf(item) };
    const wrap = document.createElement('div');
    wrap.innerHTML = `<img alt=""><p class="modal__caption"></p>
      <button class="modal__nav modal__nav--prev" type="button" aria-label="Anterior"><svg class="i"><use href="#i-arrow-left"></use></svg></button>
      <button class="modal__nav modal__nav--next" type="button" aria-label="Próxima"><svg class="i"><use href="#i-arrow"></use></svg></button>`;
    openModal(wrap);
    const g = gallery;
    gallery = g;
    $('.modal__nav--prev', wrap).addEventListener('click', () => showSlide(gallery.i - 1));
    $('.modal__nav--next', wrap).addEventListener('click', () => showSlide(gallery.i + 1));
    showSlide(gallery.i);
  });

  /* ------------------------------------------------------------ Vídeos sob demanda */
  const videos = $$('video[autoplay]');
  if ('IntersectionObserver' in window && videos.length) {
    const vio = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        const v = en.target;
        if (en.isIntersecting) {
          const src = $('source[data-src]', v);
          if (src) { src.src = src.dataset.src; src.removeAttribute('data-src'); v.load(); }
          if (!reduced) v.play().catch(() => {});
        } else {
          v.pause();
        }
      });
    }, { rootMargin: '200px 0px' });
    videos.forEach((v) => vio.observe(v));
  }

  /* ------------------------------------------------------------ Transições entre páginas */
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a');
    if (!a || e.defaultPrevented || reduced) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
    const href = a.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) return;
    if (a.target === '_blank' || a.hasAttribute('download') || a.hasAttribute('data-video') || a.hasAttribute('data-lightbox')) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin) return;
    if (url.pathname === location.pathname && url.search === location.search) return;
    e.preventDefault();
    body.classList.add('is-leaving');
    setTimeout(() => { location.href = a.href; }, 380);
  });
  window.addEventListener('pageshow', (e) => { if (e.persisted) body.classList.remove('is-leaving'); });

  /* ------------------------------------------------------------ Ano / utilidades */
  document.dispatchEvent(new CustomEvent('vv:ready'));
})();
