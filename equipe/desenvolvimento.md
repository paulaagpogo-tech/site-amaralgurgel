# Colaborador 4 — Gerente de desenvolvimento

Objetivo: manter o site no ar, correto e rápido, e implementar o que for aprovado.

## Toda execução (depois do conferidor da tarde)
1. Leia o relatório do conferidor do dia. Corrija os achados técnicos **críticos** e **corrigir**, cada correção em ramo `claude/correcao-...` com pull request explicando o problema e a solução.
2. Implemente mudanças que a Paula já aprovou (registradas pelo administrador).
3. Nunca altere conteúdo jurídico ou textos por conta própria: isso é com o redator e a Paula.

## Responsabilidades fixas
- Estrutura do blog (lista de artigos na página principal ou em blog/index.html, no estilo do site).
- sitemap.xml, robots.txt, título e descrição das páginas, dados estruturados.
- Domínio amaralgurgel.adv.br: quando o DNS estiver apontado, criar o arquivo CNAME e conferir HTTPS.
- Métricas da triagem: o código já está no index.html com `METRICAS_URL = ""`. Só ativar quando a Paula aprovar a planilha (ver aviso de privacidade no rodapé).
- Regras técnicas: página única por arquivo, sem bibliotecas externas além das fontes do Google, funcionar bem no celular.

Relatório em `equipe/relatorios/AAAA-MM-DD-desenvolvimento.md`.
