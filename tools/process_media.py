"""
Otimiza as imagens e vídeos originais (gerados/baixados) para a web.

Uso:
    python tools/process_media.py <pasta_originais>

A pasta de originais deve conter os PNGs numerados (00.png ... 39.png),
as fotos da Dra. ampliadas (up1/up3/up5/up6.png), os recortes originais
(dl/dra_solta*.png, usados como máscara de transparência), a foto real
da clínica (dl/interior_clinica.jpg) e os vídeos (v50.mp4, v51.mp4).

Saída: assets/img/*.webp (800 e 1600 px), assets/img/manifest.json,
assets/video/*.mp4 (+ poster .webp).
"""
import json
import os
import subprocess
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_OUT = os.path.join(ROOT, 'assets', 'img')
VID_OUT = os.path.join(ROOT, 'assets', 'video')

NAMES = {
    '00': 'rosto-retrato', '01': 'corpo-ombro', '02': 'cabelo-costas',
    '03': 'clinica-recepcao', '04': 'clinica-sala-procedimentos',
    '05': 'clinica-consultorio', '06': 'textura-serum', '07': 'colageno-3d',
    '08': 'peeling-quimico', '09': 'laser-co2', '10': 'labios', '11': 'olhos',
    '12': 'contorno-perfil', '13': 'ultrassom-microfocado', '14': 'toxina-marcacao',
    '15': 'pele-hidratada', '16': 'ampola-ativos', '17': 'colo-maos',
    '18': 'corpo-silhueta', '19': 'pos-parto', '20': 'masculino',
    '21': 'capilar-tricoscopia', '22': 'capilar-serum', '23': 'pele-uniforme',
    '24': 'protetor-solar', '25': 'skincare-flatlay', '26': 'rotina-noturna',
    '27': 'clinica-detalhe', '28': 'clinica-corredor', '29': 'clinica-sala-dourada',
    '30': 'maos-creme', '31': 'paciente-consulta', '32': 'laser-lavieen',
    '33': 'luz-pulsada', '34': 'corpo-textura', '35': 'cabelo-macro',
    '36': 'capilar-masculino', '37': 'rejuvenescimento', '38': 'seda-fundo',
    '39': 'contorno-marcacao',
}
# foto ampliada -> (recorte original para máscara, nome final)
DRA = {
    'up5': ('dra_solta5.png', 'dra-apresentando'),
    'up1': ('dra_solta.png', 'dra-ativo'),
    'up6': ('dra_solta6.png', 'dra-retrato'),
    'up3': ('dra_solta3.png', 'dra-fio'),
}
WIDTHS = (800, 1600)


def save_variants(im, name, manifest, quality=80, widths=WIDTHS):
    entry = {'w': im.width, 'h': im.height, 'sizes': []}
    for w in widths:
        if w > im.width:
            w = im.width
        h = round(im.height * w / im.width)
        out = im.resize((w, h), Image.LANCZOS) if w != im.width else im
        path = os.path.join(IMG_OUT, f'{name}-{w}.webp')
        out.save(path, 'WEBP', quality=quality, method=6)
        entry['sizes'].append(w)
    manifest[name] = entry
    print(f'{name:32s} {im.width}x{im.height} -> {entry["sizes"]}')


def main(src):
    os.makedirs(IMG_OUT, exist_ok=True)
    os.makedirs(VID_OUT, exist_ok=True)
    manifest = {}

    for key, name in NAMES.items():
        p = os.path.join(src, f'{key}.png')
        if os.path.exists(p):
            save_variants(Image.open(p).convert('RGB'), name, manifest)

    # Fotos reais da Dra. Karinie: upscale + máscara alfa do recorte original
    for key, (mask_file, name) in DRA.items():
        up = Image.open(os.path.join(src, f'{key}.png')).convert('RGB')
        alpha = Image.open(os.path.join(src, 'dl', mask_file)).convert('RGBA').split()[-1]
        alpha = alpha.resize(up.size, Image.LANCZOS)
        rgba = up.copy()
        rgba.putalpha(alpha)
        save_variants(rgba, name, manifest, quality=86, widths=(700, 1400))

    # Foto real da recepção (baixa resolução: mantém tamanho original)
    real = Image.open(os.path.join(src, 'dl', 'interior_clinica.jpg')).convert('RGB')
    save_variants(real, 'clinica-real', manifest, quality=84, widths=(real.width,))

    with open(os.path.join(IMG_OUT, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=1)

    # Vídeos: H.264 720p, sem áudio, faststart + poster
    try:
        import imageio_ffmpeg
        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        print('imageio-ffmpeg não instalado; vídeos ignorados')
        return
    for key, name in (('v50', 'sala-tratamento'), ('v51', 'recepcao-tour')):
        src_v = os.path.join(src, f'{key}.mp4')
        if not os.path.exists(src_v):
            continue
        out_v = os.path.join(VID_OUT, f'{name}.mp4')
        subprocess.run([ffmpeg, '-y', '-loglevel', 'error', '-i', src_v, '-an',
                        '-vf', 'scale=1280:-2,fps=24', '-c:v', 'libx264', '-preset', 'slow',
                        '-crf', '27', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out_v],
                       check=True)
        poster_png = os.path.join(VID_OUT, f'{name}-poster.png')
        subprocess.run([ffmpeg, '-y', '-loglevel', 'error', '-i', out_v, '-frames:v', '1',
                        poster_png], check=True)
        Image.open(poster_png).convert('RGB').save(
            os.path.join(VID_OUT, f'{name}-poster.webp'), 'WEBP', quality=78)
        os.remove(poster_png)
        print(f'video {name}: {os.path.getsize(out_v) / 1e6:.1f} MB')


if __name__ == '__main__':
    main(sys.argv[1])
