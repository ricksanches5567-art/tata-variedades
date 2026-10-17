# Tata Variedades — gera imagens e data/produtos.json + CSV de preços.
# Vidros/maçaricos/isqueiros: imagens-base dos vidros/maçaricos/isqueiros (renomeadas para o prefixo T).
# Sex shop: fotos ilustrativas de licença livre (ver /workspace/tata-cat/fontes.txt e creditos.html).
import os, json, csv, glob, shutil
from PIL import Image, ImageFilter, ImageEnhance
G = '/workspace/tata-cat/base'; SRC = '/workspace/tata-cat/src'
base = json.load(open(f'{G}/produtos.json'))
prods = []
def novo_id(i): return i.replace('G-MAC', 'T-MAC').replace('G-ISQ', 'T-ISQ') if i.startswith('G-') else 'T' + i[1:]
for p in base:
  nid = novo_id(p['id'])
  for d in ('p', 't'): shutil.copy(f"{G}/{d}/{p['id']}.webp", f'img/{d}/{nid}.webp')
  q = dict(p); q.update({'id': nid, 'img': nid, 'codigo': nid})
  if p['categoria'] == 'vidro': q['nome'] = f'Peça de vidro {nid}'
  prods.append(q)

def salvar(im, pid):
  for d, w in (('p', 900), ('t', 480)):
    x = im.copy(); x.thumbnail((w, w * 2)); x.save(f'img/{d}/{pid}.webp', quality=84 if d == 'p' else 80)
def quadro(path, pid, crop=None, ratio=0.73, modo='fit', foco=(0.5, 0.5), zoom=1.0):
  # modo 'fit': foto larga na largura toda, bordas de cima/baixo esmaecidas sobre o próprio fundo desfocado
  # modo 'cover': recorte retrato (proporção fixa) centrado em `foco`
  im = Image.open(path).convert('RGB')
  if crop: im = im.crop((int(crop[0]*im.width), int(crop[1]*im.height), int(crop[2]*im.width), int(crop[3]*im.height)))
  H = 1250; W = int(H * ratio)
  if modo == 'cover':
    ch = im.height / zoom; cw = ch * ratio
    if cw > im.width: cw = im.width; ch = cw / ratio
    x0 = min(max(foco[0]*im.width - cw/2, 0), im.width - cw); y0 = min(max(foco[1]*im.height - ch/2, 0), im.height - ch)
    out = im.crop((int(x0), int(y0), int(x0+cw), int(y0+ch))).resize((W, H), Image.LANCZOS); salvar(out, pid); return W, H
  import numpy as np
  t = im.resize((W, int(im.height * W / im.width)), Image.LANCZOS)
  arr = np.asarray(t, dtype=np.float32); k = max(3, t.height // 20)
  ct = np.median(arr[:k].reshape(-1, 3), axis=0); cb = np.median(arr[-k:].reshape(-1, 3), axis=0)
  yy = np.linspace(0, 1, H)[:, None, None]; g = ct[None, None, :] * (1 - yy) + cb[None, None, :] * yy
  bg = Image.fromarray(np.broadcast_to(g, (H, W, 3)).astype(np.uint8))
  m = Image.new('L', t.size, 255); px = m.load(); f = max(4, int(t.height*.12))
  for y in range(t.height):
    a = min(1, y/f, (t.height-1-y)/f)
    for x in range(t.width): px[x, y] = int(255*a)
  bg.paste(t, (0, (H-t.height)//2), m); salvar(bg, pid); return W, H
# (id, nome, arquivo, recorte (frações), descrição curta)
SEX = [
  ('T-SEX-01', 'Gel lubrificante aromatizado', 'Lubricant_Gleitgel_jpge0ad', None, dict(modo='fit')),
  ('T-SEX-02', 'Vibrador cápsula rosa com controle', '_JPG', (0.04, 0.08, 0.94, 0.88), dict(modo='fit')),
  ('T-SEX-03', 'Algemas rosa de metal', 'UZI_Chain_Handcuff_Pink_9449382848_jpg', None, dict(modo='fit')),
  ('T-SEX-04', 'Venda de olhos preta', 'Blindfolds_jpg', (0.0, 0.2, 1.0, 0.95), dict(modo='fit')),
  ('T-SEX-05', 'Máscaras de olhos de cetim (kit)', 'Different_Blindfolds_for_sleeping_and_re', None, dict(modo='cover', foco=(0.38, 0.5), zoom=1.0)),
  ('T-SEX-06', 'Dados coloridos para casais', '6sided_dice_jpg', None, dict(modo='fit')),
  ('T-SEX-07', 'Cinta-liga de renda branca', 'White_lace_garter_belt_jpgb312', None, dict(modo='fit')),
  ('T-SEX-08', 'Cinta-liga preta com renda dourada', 'Garter_belt_jpgdf0d', None, dict(modo='fit')),
  ('T-SEX-09', 'Cinta-liga rosa e preta', '14_Strap_Suspender_Belt_jpgd0f6', None, dict(modo='cover', foco=(0.5, 0.45), zoom=1.0)),
  ('T-SEX-10', 'Cinta-liga branca delicada', 'Lingerie_garter_belt_jpg6d71', (0.0, 0.14, 1.0, 1.0), dict(modo='fit')),
  ('T-SEX-11', 'Pluma de penas para carícias', 'Ostrich_Feather_Duster_jpgca05', None, dict(modo='cover', foco=(0.5, 0.62), zoom=1.0)),
  ('T-SEX-12', 'Vela romântica em coração de sal', 'Heart_shaped_tea_light_candle_b088', (0.1, 0.0, 0.95, 1.0), dict(modo='fit')),
]
for i, (pid, nome, fn, crop, kw) in enumerate(SEX):
  w, h = quadro(f'{SRC}/{fn}.jpg', pid, crop, **kw)
  prods.append({'id': pid, 'categoria': 'sexshop', 'pagina': 0, 'posicao': i + 1, 'nome': nome, 'preco': None, 'img': pid, 'w': w, 'h': h, 'codigo': pid, 'tamanhos': [], 'cores': [], 'ilustrativa': True, 'adulto': True})
json.dump(prods, open('data/produtos.json', 'w'), ensure_ascii=False, indent=1)
os.makedirs('/workspace/tata-cat', exist_ok=True)
with open('/workspace/tata-cat/precos-template.csv', 'w', newline='', encoding='utf-8-sig') as fh:
  w = csv.writer(fh, delimiter=';')
  w.writerow(['id', 'categoria', 'nome_atual', 'imagem', 'nome', 'preco', 'peso_kg', 'comprimento_cm', 'largura_cm', 'altura_cm', 'observacao'])
  for p in prods:
    ph = 'foto ILUSTRATIVA (online, licença livre) - trocar pela foto real' if p.get('ilustrativa') else ''
    w.writerow([p['id'], p['categoria'], p['nome'], f"img/p/{p['id']}.webp", '', '', '', '', '', '', ph])
from collections import Counter
print(len(prods), Counter(p['categoria'] for p in prods))
