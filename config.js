/* CONFIGURAÇÕES DA LOJA — Tata Variedades (arquivo PÚBLICO: nunca coloque senha ou token aqui) */
window.LOJA_CONFIG = {
  nomeLoja: "Tata Variedades",
  whatsappNumber: "5541991064167",
  instagram: "",
  // Servidor de pagamento (Cloudflare Worker separado: pedidos não se misturam)
  apiPagamento: "https://tata-variedades-pagamento.cwbmodafitness.workers.dev",
  // Compra online DESLIGADA até os preços serem cadastrados em data/produtos.json.
  // Mesmo ligada, só itens com preço > 0 podem ir para a sacola (o servidor também recusa itens sem preço).
  vendasAtivas: false,
  cidade: "Curitiba – PR",
  cnpj: "37.789.447/0001-00"
};
