# NICHVS-CONSOLIDADO.md
### Fonte única de verdade — Projeto Nichvs / CulturaFlow
*Última atualização: 27/06/2026 — consolidação de 6 conversas do projeto*

> **Como usar este documento:** mantenha este arquivo no **knowledge base do projeto** (não apenas na memória de chat). Assim toda nova sessão carrega o contexto completo automaticamente e evita inconsistências. A memória de chat é resumida e pode perder detalhes; este `.md` no knowledge base fica disponível por inteiro.

---

## 1. Identidade da empresa e produto

- **Fundador:** Luciano Kichalowski Simas
- **Empresa:** Nichvs Tecnologia ME
- **CNPJ:** 28.954.962/0001-07
- **Sede:** Florianópolis / SC
- **Produto central:** **CulturaFlow** — SaaS vertical para o setor cultural brasileiro

**Proposta de valor (4 dimensões):**
1. **Eliminar o imposto oculto sobre a criatividade** — reduzir de 60–80h para 4–8h o tempo por edital.
2. **Democratizar o acesso** — abrir recursos antes restritos a uma elite burocrática.
3. **Destravar capital ocioso** — recursos de fomento que não chegam a quem produz.
4. **Compliance-as-a-service** — padronização e conformidade como diferencial.

**O que o produto automatiza:** acesso a editais de fomento cultural, registro autoral (módulo F8) e licitações públicas B2B (Lei 14.133/2021).

---

## 2. Infraestrutura e stack

**Stack em produção:** React/Vite + Supabase + Netlify Functions + Anthropic Claude API + Cloudinary

**Supabase:**
- Produção: `pplwcohxwonnvnrhfyxy`
- Dev: `eujedqbxyxyhpcceacqi`
- Singleton do client em `src/lib/supabase.js` (resolve warning de múltiplas instâncias GoTrueClient)

**Repositórios (org GitHub `nichvscultural`):**
- `culturaflow` — app principal
- `nichvs-site` — landing/site institucional
- `nichvs-docs` — documentação (privado), 33+ documentos em 8 categorias (valuation, arquitetura, produto, comercial, marketing, jurídico, assets, site) com índice HTML navegável

**Domínios:**
- `nichvs.tech`
- `nichvs.studio` (DNS na Cloudflare; 4 A records GitHub Pages 185.199.108–111.153)
- `culturaflow.netlify.app`

**Notas de config:**
- `vite.config.js` usa `server.host: '0.0.0.0'` (resolveu problema de acesso localhost IPv6)
- `.env.local` deve apontar para o Supabase **dev**, não produção
- Chamadas à API Anthropic **nunca** direto do browser — sempre via Netlify Function serverless (`licitacao-ia`)

---

## 3. Módulos desenvolvidos

### Editais / Fomento cultural
- **Scraper cultural v2** — Joinville (`www.joinville.sc.gov.br/institucional/secult/`) e Florianópolis (PMF), perfil carregado do Supabase, campos **segmento/fonte** adicionados (commits `2734662`, `3a7b767`)
- Kanban de editais
- View `vw_editais_recentes` corrigida com `security_invoker=true`

### Licitações públicas (B2B, Lei 14.133/2021)
- **Scraper PNCP v1** — `api.pncp.gov.br/api/consulta/v1/contratacoes/publicacao`; formato de data `yyyyMMdd` obrigatório; `codigoModalidadeContratacao` obrigatório; itera modalidades **6/4/8/9**; ~46 licitações culturais salvas
- **useLicitacao v2** — remove chamada direta à API Anthropic do browser, roteia pelo serverless `licitacao-ia`; corrige bug de variável `err` indefinida em `handleSalvar`; `listarLicitacoes` usa `.or("user_id.eq." + userId + ",user_id.is.null")` para mostrar registros globais PNCP
- **RLS** atualizado na tabela `licitacoes` para permitir `user_id IS NULL`; coluna `user_id` tornada nullable
- **PainelLateralLicitacao** — 5 fases de habilitação (F1 Análise go/no-go, F2 Habilitação certidões, F3 Proposta BDI+IA, F4 Revisão checklist, F5 Envio protocolo), integrado ao **LicitacaoKanban** com sidebar flex e seleção automática de aba via map `ETAPA_ABA`
- Kanban de 6 estágios; checklist de 9 certidões com links diretos de emissão
- Geração de documentos jurídicos por IA (esclarecimentos/impugnações/análise de concorrentes) via `licitacao-ia.js`

### F8 Registro Autoral
- 9 categorias de obra alinhadas ao portal Biblioteca Nacional EDA/FBN
- Upload dual para música completa (áudio + letra)
- Validação de CPF
- Upload Cloudinary com `resource_type` dinâmico
- Spec real e acionável: schema, estimativa de 224h de sprint, matriz de risco, fluxos de UX

### Reel Generator
- Script Python (PIL + ffmpeg) gera vídeos MP4 9:16, com `server.py` (HTTP local) e interface HTML standalone
- **Pendente:** integrar como módulo em `src/modules/` no CulturaFlow

### CulturaFlow Estúdio
- Artifact React — plataforma de aprovação de identidade visual (B2B), workflow de aprovação de assets, mockups, geração de links seguros de download, painel de pacotes de serviço

### CI/CD
- GitHub Actions `scraper.yml` roda os dois scrapers de forma independente

---

## 4. Documentação estratégica e valuation

- **Blueprint Enterprise (PDF)** — estrutura correta (15 seções, pipeline de 16 estágios, 20 anexos), porém conteúdo ainda é placeholder; faltam regras de negócio reais
- **F8 Registro Autoral (DOCX)** — spec real e acionável
- **Roteiro de Automação** — mapeia atividades para colunas do kanban com níveis de automação (sistema/semi-auto/humano) e status (live/roadmap)
- **Startup Falcon** — valuation v3.0 a v4.2; score 84/100; R$4,5M–6,0M; ponto central **R$5,1M**
- **Equidam** — valuation por 5 métodos (DCF/Damodaran, múltiplos/Equidam Research, scorecard/Payne, VC Method/Sahlman, First Chicago/Metrick & Yasuda)
- **Technical Architecture Deep Dive v2.0** — neutro, sem marcas, em inglês
- **Architecture Infrastructure v2.1**
- **Medição de esforço** — 842 horas-equivalentes totais; custo de mercado R$224.720; gasto real <R$1.500; razão ~150×
- **nichvs-topologia.html v2.2** — 7 camadas, módulos F8/Licitações/Reel
- **nichvs-status.html** — dashboard de status de ambiente com check localhost em tempo real

---

## 5. Guia de habilitação em licitações públicas (5 fases)

Referência operacional para participação em licitações brasileiras, do edital ao envio:

1. **Fase 1 — Captura e leitura do edital** (Termo de Referência, Projeto Básico)
2. **Fase 2 — Habilitação jurídica e fiscal** (certidões, prazos de validade)
3. **Fase 3 — Proposta comercial** (composição de custos, BDI)
4. **Fase 4 — Revisão, assinatura e empacotamento** (assinatura digital, formatação de arquivos)
5. **Fase 5 — Upload e confirmação** (monitoramento de sessão)

Entregável gerado: **"Guia Completo de Habilitação em Licitações Públicas"** (.docx) com capa, tabela-resumo das 5 fases, grade de certidões com órgãos emissores e validades, callouts de alerta e checklist de 18 itens pré-envio.

**Referências legais:** Lei 14.133/2021, Lei 8.666/93, Lei Complementar 123/06; portal PNCP (`api.pncp.gov.br`); Biblioteca Nacional EDA/FBN (registro autoral).

---

## 6. Commits importantes

| Hash | Descrição |
|------|-----------|
| `2734662`, `3a7b767` | Scraper cultural v2 (segmento/fonte) |
| `77f40ce`, `eb7603e` | F8 dev |
| `ca45dfc` | Merge para main **(contém chave Anthropic exposta — já revogada)** |
| `75b9570` | Fix vite host |
| `5de9ef6` | Landing v3 |
| `d3f79c5` | Topologia v2.2 |

---

## 7. Nota de segurança ⚠️

O histórico git contém uma **chave da API Anthropic exposta** no commit `ca45dfc`. A chave **já foi revogada/rotacionada**, mas o histórico precisa ser **limpo** (ex.: `git filter-repo` ou BFG) **antes** de qualquer due diligence ou abertura do repositório. Item **crítico**.

---

## 8. Preferências de trabalho do Luciano

- Conversas em **português**
- **Mensagens muito curtas** (frequentemente 1–3 palavras); espera interpretação de comandos esparsos sem clarificações longas
- Cola **outputs de terminal** diretamente como método principal de feedback/debug
- Prefere **scripts prontos para rodar** a edição manual de arquivos
- **Heredocs longos** têm se mostrado **não confiáveis** no ambiente dele
- Trabalha **direto no terminal**, em **macOS**, usando **Safari** como browser principal (não Chrome)

---

## 9. Tarefas pendentes / roadmap

**Prioridade máxima:**
- 🔐 **Cofre de habilitação** — item de maior prioridade no roadmap

**Infra / governança:**
- 🔒 **Limpeza do histórico git** para remover a chave exposta no `ca45dfc` (crítico antes de due diligence)
- HTTPS enforcement em `nichvs.studio` (via `gh api -X PUT` com `https_enforced=true`, após `curl -sI` retornar 200)
- Registro **CNAE 6201-5/01** na Receita Federal

**Engenharia:**
- Modularização incremental do `App.jsx` monolítico (~900 linhas)
- Resolver auth da IA de licitações (`licitacao-ia.js`) — ~2–4h
- Converter `gerar-proposta.js` e `sign-url.js` de CommonJS para ESM
- Integrar Reel Generator como módulo em `src/modules/`
- Completar seletores do scraper para **Joinville/Blumenau**

**Bug ativo:**
- 🐞 CulturaFlow renderiza **em branco no Safari** (funciona no Chrome) — causa raiz não totalmente resolvida; provável incompatibilidade JS específica do Safari. *(Atenção: Luciano usa Safari como browser principal — este bug afeta diretamente a experiência dele.)*

---

## 10. Aprendizados e princípios

- **NICHVS-CONSOLIDADO.md** é a fonte única de verdade — deve ficar no **knowledge base do projeto** para disponibilidade automática em novas sessões.
- Chamadas à API Anthropic **a partir do browser** devem ser evitadas — sempre via Netlify Function serverless.
- A **busca por conversas do projeto por palavras-chave pode falhar**; listagem por recência (`recent_chats` com `sort_order=desc`) é a estratégia confiável para recuperar o histórico.
- O histórico git contém uma chave API exposta que precisa ser limpa antes de qualquer due diligence.
