# Vinovare Medicina Personalizada — site institucional

Layout de apresentação do novo site da **Vinovare Medicina Personalizada**, clínica de dermatologia da
**Dra. Karinie Marinho** (CRM/DF 19437 · RQE 20108) na Asa Sul, em Brasília.

Site estático, responsivo e sem dependências de front-end (HTML + CSS + JavaScript puro), gerado a partir de
templates Jinja2. Pode ser publicado em qualquer hospedagem estática (GitHub Pages, Netlify, Vercel, servidor próprio).

## Páginas

| Página | Arquivo | Destaques |
| --- | --- | --- |
| Início | `index.html` | Hero com foto da Dra. + mini-vídeo da clínica, manifesto com palavras que "acendem" na rolagem, navegação interativa por áreas (colunas que revelam a imagem e expandem), carrossel de tratamentos, jornada do paciente, chamada para o questionário, mosaico da clínica, conteúdos, FAQ e mapa |
| Tratamentos | `tratamentos.html` | Filtro por área (Rosto, Corpo, Cabelo) com indicador animado, busca por tratamento/tecnologia, introdução de cada área |
| Procedimentos (29) | `procedimentos/*.html` | Página premium por procedimento: dados rápidos, indicações, passo a passo, tecnologias, FAQ, combinações e CTA com mensagem pré-preenchida no WhatsApp |
| A Dra. Karinie | `dra-karinie.html` | Trajetória em linha do tempo, formação e qualificações, filosofia de atendimento e vídeo |
| A Clínica | `clinica.html` | Hero em vídeo, tour horizontal fixo na rolagem, conforto e segurança, galeria com lightbox |
| Descubra seu cuidado | `descubra.html` | Questionário de 4 perguntas com resultado personalizado (tratamentos + leituras) — sem diagnóstico e sem armazenar dados |
| Conteúdos | `conteudos.html` + `conteudos/*.html` | Blog educativo com filtro por categoria, artigo com sumário automático e barra de progresso de leitura |
| Agendamento | `agendamento.html` | Formulário que abre o WhatsApp com a mensagem pronta + agenda online ilustrativa (dia e horário) |
| Contato | `contato.html` | Canais, mapa do Google, dicas para a primeira consulta e FAQ |

## Estrutura

```
build.py                 # gerador estático (Jinja2)
src/templates/           # base, parciais, páginas, procedimento.html, artigo.html
src/data/                # conteúdo: site_data.py, procedimentos.py, artigos.py
assets/css/              # main.css (design system + home) e pages.css (páginas internas)
assets/js/               # main.js (interações globais), pages.js, quiz.js
assets/img/, assets/video/  # mídia otimizada (WebP em 2 tamanhos, MP4 720p)
tools/                   # scripts de apoio (otimização de mídia e logo)
*.html                   # páginas geradas (prontas para publicar)
```

## Como editar e gerar

```bash
pip install jinja2
python build.py
```

- **Textos institucionais, telefone, endereço e horários:** `src/data/site_data.py`
- **Procedimentos:** `src/data/procedimentos.py` (cada item gera uma página em `procedimentos/`)
- **Artigos do blog:** `src/data/artigos.py`
- **Novas imagens:** `python tools/process_media.py <pasta-com-originais>` (gera WebP 800/1600 px e o `manifest.json`)

Para visualizar localmente: `python -m http.server 8000` e abrir `http://localhost:8000`.

## Identidade visual

- **Cores:** marfim `#FBF8F4`, creme `#F4ECE3`, cobre do logo `#C87C5C`, pêssego `#EBB393` e cacau `#4A2E22`
  (os tons marrons dos posts do Instagram).
- **Tipografia:** DM Serif Display (títulos, como nos posts), Montserrat (texto e rótulos espaçados, como no logo)
  e a assinatura original do logo "By Karinie Marinho" em SVG.
- **Elementos:** o "V" e o arco do logo aparecem como arcos nas fotos, anéis girando, marcas d'água e ícones.
- **Movimento:** abertura com o logo se desenhando, títulos revelados palavra a palavra, parallax, cursor
  personalizado, botões magnéticos e transições entre páginas — tudo respeita `prefers-reduced-motion`.

## Sobre as imagens e vídeos

- **Fotos da Dra. Karinie:** reais, retiradas do site atual (vinovare.com.br) e ampliadas para alta resolução
  (upscale, sem alterar o rosto).
- **Foto real da recepção:** do site atual (exibida no tour da clínica).
- **Demais fotos e os 2 vídeos:** gerados por IA (Higgsfield — Nano Banana Pro e Kling 3.0) para a apresentação
  do layout, inspirados na recepção real (madeira ripada, luminárias em cobre).

## Pendências para a versão final

- [ ] Substituir as imagens geradas por fotografias reais da clínica, dos equipamentos e da equipe.
- [ ] Gravar o vídeo institucional da Dra. Karinie (hoje há uma prévia no lugar).
- [ ] Confirmar com a Dra. dados de formação que não estão públicos (residência, sociedades, títulos).
- [ ] Conectar a "Agenda online" ao sistema real de agendamento (hoje os horários são ilustrativos e o pedido
      segue pelo WhatsApp).
- [ ] Conferir o pino do mapa e o domínio final (`SITE_URL` em `build.py`, usado em sitemap e metatags).
- [ ] Revisar os textos médicos com a Dra. (informativos e conservadores, sem promessa de resultado).
- Depoimentos e fotos de "antes e depois" foram deixados de fora de propósito, por causa das regras de publicidade
  médica do CFM.
