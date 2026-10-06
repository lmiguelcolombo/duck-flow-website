# Duck Flow — website novo

Versão estática independente, baseada em `../../brand/design-system-v2.html`. O site anterior continua em `website/`.

Abra `index.html` no navegador ou sirva esta pasta com um servidor estático. O formulário valida os dados e abre uma conversa no WhatsApp com a mensagem preenchida. Não há backend nem armazenamento de dados.

Antes de publicar em `duckflow.com.br`, revise o número de WhatsApp: `../_memoria/empresa.md` registra o dígito adicional do celular como pendente de confirmação. Os metadados canônicos e o sitemap já apontam para o domínio final.


## Design e movimento

`../../brand/design-system-v2.html` é a fonte de verdade para tokens, tipografia, cores e estados dos componentes. `assets/css/site.css` usa os mesmos tokens e apenas cores presentes nesse arquivo.

`assets/js/text-motion.js` adapta a revelação de palavras e a entrada de textos do site anterior. Preserva os elementos de destaque e as quebras de linha, dispensa CDN e respeita `prefers-reduced-motion`.

## Sincronização com o design system

`../../brand/design-system-v2.html` documenta a iconografia e os exemplos de mensagem usados no site. Ao mudar um ícone, atualize os mesmos `<symbol id="icon-*">` e os tamanhos nos dois arquivos. As amostras de “Gestão contínua” e “Atendimento direto” no DS devem acompanhar a copy publicada. Revise os dois lados na mesma alteração.

## Favicon

A arte-fonte da cara do pato é `../../brand/logos/logo-reduzida-2.png`. Os ícones exportados em `assets/favicons/` devem permanecer idênticos aos de `../../brand/assets-v2/favicons/`; `favicon.ico` na raiz do site é o fallback para navegadores e links legados. Ao atualizar o símbolo, regenere os formatos para navegador, iPhone e Android e ajuste os links em `index.html` e no design system.

## Páginas de serviço

`servicos/` (visão geral) e `servicos/<slug>/` são geradas por `tools/gerar-servicos.py`. Edite a copy no script e rode `python3 tools/gerar-servicos.py` na raiz do site; não edite os HTML gerados à mão. O script copia o sprite de ícones do `index.html`. Ao criar ou renomear um serviço, atualize também os cards e o rodapé do `index.html`, o `sitemap.xml` e o `llms.txt`.

As páginas usam URLs limpas (`/servicos/agentes-de-ia/`), então os links entre elas só funcionam com um servidor estático (por exemplo `python3 -m http.server`), não abrindo o arquivo direto no navegador.
