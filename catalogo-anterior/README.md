# Tata Variedades – loja online
Site estático (GitHub Pages): https://ricksanches5567-art.github.io/tata-variedades/

- Categorias (`categoria` em `data/produtos.json`, gerado por `scripts/process.py`): `vidro`, `macarico`, `isqueiro`, `sexshop`. Códigos: vidros `T<pág>-<pos>` (ex.: T2-03), `T-MAC-nn`, `T-ISQ-nn`, `T-SEX-nn`.
- Preços: enquanto `preco` for `null` o item mostra "Preço em breve" e não pode ir para a sacola.
- Fotos de maçaricos, isqueiros e sex shop são ILUSTRATIVAS (Wikimedia Commons, licenças livres); créditos em `creditos.html` (`scripts/credits.py`). Trocar pelas fotos reais.
- Compra online: `vendasAtivas` em `config.js` (desligada). O servidor de pagamento é um Worker separado e só vende itens com preço > 0.
- Vídeo do topo: `scripts/film.py`. Páginas legais: `scripts/legal.py`.
- Site 18+: portão de idade, aviso do Ministério da Saúde (tabacaria), sem vapes/pods (Anvisa RDC 855/2024), embalagem discreta para sex shop.
- Nunca coloque senha, token ou dados de clientes neste repositório (é público).
