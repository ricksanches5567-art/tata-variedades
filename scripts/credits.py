# Fonte única dos créditos (usada por legal.py e gerada em /workspace/tata-cat/fontes.txt)
W = 'https://commons.wikimedia.org/wiki/'
LIC = {'CC0': 'https://creativecommons.org/publicdomain/zero/1.0', 'CC BY 2.0': 'https://creativecommons.org/licenses/by/2.0', 'CC BY 2.5': 'https://creativecommons.org/licenses/by/2.5',
       'CC BY 3.0': 'https://creativecommons.org/licenses/by/3.0', 'CC BY-SA 3.0': 'https://creativecommons.org/licenses/by-sa/3.0', 'CC BY-SA 4.0': 'https://creativecommons.org/licenses/by-sa/4.0', 'PD': ''}
# (códigos, descrição, autor, arquivo no Commons, licença, observação)
CREDITOS = [
 ('T-SEX-01', 'Gel lubrificante aromatizado', 'Sciencia58', 'Lubricant_-_Gleitgel.jpg', 'CC0', 'redimensionada'),
 ('T-SEX-02', 'Vibrador cápsula rosa com controle', 'Otakuonaa', 'File:一個粉紅色的跳蛋.JPG', 'CC BY-SA 4.0', 'recortada'),
 ('T-SEX-03', 'Algemas rosa de metal', 'Campco Photos', 'UZI_Chain_Handcuff_-_Pink_(9449382848).jpg', 'CC BY 2.0', 'redimensionada'),
 ('T-SEX-04', 'Venda de olhos preta', 'User:Henna', 'Blindfolds.jpg', 'CC BY-SA 4.0', 'recortada'),
 ('T-SEX-05', 'Máscaras de olhos de cetim (kit)', 'User:Mattes', 'Different_Blindfolds_for_sleeping_and_resting.JPG', 'CC BY-SA 3.0', 'recortada'),
 ('T-SEX-06', 'Dados coloridos para casais', 'Diacritica', '6sided_dice.jpg', 'CC BY-SA 3.0', 'redimensionada'),
 ('T-SEX-07', 'Cinta-liga de renda branca', 'Another Energy', 'White_lace_garter_belt.jpg', 'CC BY-SA 4.0', 'redimensionada'),
 ('T-SEX-08', 'Cinta-liga preta com renda dourada', 'Antique Rose', 'Garter_belt.jpg', 'CC BY 2.5', 'redimensionada'),
 ('T-SEX-09', 'Cinta-liga rosa e preta', 'Tornado9923', '14_Strap_Suspender_Belt.jpg', 'CC BY-SA 4.0', 'recortada'),
 ('T-SEX-10', 'Cinta-liga branca delicada', 'Tender Rosebud', 'Lingerie_garter_belt.jpg', 'CC BY-SA 3.0', 'recortada'),
 ('T-SEX-11', 'Pluma de penas para carícias', 'freebie.photography', 'Ostrich_Feather_Duster.jpg', 'CC BY 3.0', 'recortada'),
 ('T-SEX-12', 'Vela romântica em coração de sal', 'Olga Ernst', 'Heart-shaped_tea-light_candle_holder,_Himalayan_salt.jpg', 'CC BY-SA 4.0', 'recortada'),
 ('T-MAC-01', 'Maçarico tipo lápis', 'Omegatron', 'Small_butane_torch.jpg', 'CC BY-SA 3.0', ''),
 ('T-MAC-02', 'Maçarico de bancada', 'MeMaria', 'Newport-zero-mini-butane-torch-lighter-silver.jpg', 'CC BY-SA 4.0', 'recortada'),
 ('T-ISQ-01', 'Isqueiro descartável azul', 'Creative Tools (Halmstad, Suécia)', 'CreativeTools.se_-_PackshotCreator_-_Bl%C3%A5_t%C3%A4ndare_(5077886065)_(cropped).jpg', 'CC BY 2.0', ''),
 ('T-ISQ-02', 'Isqueiros coloridos (sortidos)', 'Ready Elements', 'Colorful_lighters_on_white_background_(41903831300).jpg', 'CC0', ''),
 ('T-ISQ-03', 'Isqueiro de metal preto', 'Adhish Bhargava', 'Zippoclosed.JPG', 'PD', 'domínio público'),
]
def url(f): return f if f.startswith('http') else W + (f if f.startswith('File:') else 'File:' + f)
