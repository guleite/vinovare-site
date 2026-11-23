"""Gera variações do logo (inline, currentColor) a partir do SVG original."""
import re, sys, os
src, tpl_dir, img_dir = sys.argv[1], sys.argv[2], sys.argv[3]
lines = open(src, encoding='utf-8').read().splitlines()
def block(a, b):  # 1-indexed inclusive
    return '\n'.join(lines[a-1:b]).replace('class="st0" ', '')
mark, word, script, sub = block(8, 15), block(16, 31), block(32, 174), block(175, 215)
def svg(vb, body, cls, title=None, fill='currentColor'):
    t = f'<title>{title}</title>' if title else ''
    aria = f'role="img" aria-label="{title}"' if title else 'aria-hidden="true"'
    return f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="{fill}" {aria}>{t}{body}</svg>'
open(os.path.join(tpl_dir, 'logo.svg'), 'w', encoding='utf-8').write(svg('10 4 1056 282', mark + word + sub, 'logo', 'Vinovare Medicina Personalizada'))
open(os.path.join(tpl_dir, 'logo-full.svg'), 'w', encoding='utf-8').write(svg('10 4 1120 350', mark + word + sub + script, 'logo logo--full', 'Vinovare Medicina Personalizada by Karinie Marinho'))
open(os.path.join(tpl_dir, 'mark.svg'), 'w', encoding='utf-8').write(svg('12 6 248 278', mark, 'mark'))
open(os.path.join(tpl_dir, 'signature.svg'), 'w', encoding='utf-8').write(svg('348 236 780 122', script, 'signature', 'By Karinie Marinho'))
# arquivos estáticos (favicon / og)
open(os.path.join(img_dir, 'favicon.svg'), 'w', encoding='utf-8').write(svg('0 0 270 290', mark, 'mark', fill='#C87C5C'))
open(os.path.join(img_dir, 'logo.svg'), 'w', encoding='utf-8').write(svg('10 4 1120 350', mark + word + sub + script, 'logo', 'Vinovare', fill='#C87C5C'))
open(os.path.join(img_dir, 'logo-branco.svg'), 'w', encoding='utf-8').write(svg('10 4 1120 350', mark + word + sub + script, 'logo', 'Vinovare', fill='#FBF8F4'))
print('ok')
