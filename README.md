# 🧠 nlingua² – Any Language to Any Language

Ferramenta de linha de comando para transcrição e tradução de legendas `.srt` usando modelos de IA **offline** (OpenAI Whisper + Meta NLLB).

---

## ✨ Funcionalidades

- 🎙️ Transcreve arquivos de áudio ou vídeo para `.srt` com timestamps
- 🌍 Traduz legendas `.srt` entre mais de 200 idiomas usando NLLB
- 🧰 Tudo local, sem dependência de nuvem (além dos models, óbvio)
- ✅ Valida arquivos, caminhos, idiomas e evita sobrescrita acidental
- 🧪 CLI poderosa via `argparse` com comandos simples e extensíveis

---

## ⚙️ Instalação com [uv](https://github.com/astral-sh/uv)

Se você já usa UV, faça como o de costume (`uv sync`).

```bash
uv venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
uv pip install -e .
```

> Requer Python 3.11. `sentencepiece` ainda não suporta 3.12+. Algumas libs não instalam.

---

## 🚀 Como usar

### 🔤 Ver idiomas disponíveis

```bash
nlingua2 show_languages
```

---

### 🗣️ Transcrever vídeo para legenda `.srt`

Os caminhos não precisam ser locais, você pode usar caminhos completos do seu computador para entrada e saída.

```bash
nlingua2 transcribe \
  --input videos/aula01.mp4 \
  --from portuguese \
  --output srt/aula01.srt
```

---

### 🌐 Traduzir legenda `.srt` para outro idioma

```bash
nlingua2 translate \
  --input srt/aula01.srt \
  --from portuguese \
  --to english \
  --output srt-ready/aula01-en.srt
```

---

### 🧠 Transcrever e já traduzir na sequência

```bash
nlingua2 transcribe \
  --input videos/aula01.mp4 \
  --from portuguese \
  --output srt/aula01.srt \
  --translate_srt_to english
```

> Isso gera dois arquivos:
>
> - `srt/aula01.srt` (transcrição original)
> - `srt/aula01-en.srt` (versão traduzida)

---

## ⚠️ Flags úteis

- `--force` → sobrescreve arquivos de saída existentes
- `--from` / `--to` → aceita nomes como `english`, `portuguese`, `french`, etc
- `--input` / `--output` → caminho completo para os arquivos `.mp4` ou `.srt`

---

## 📁 Estrutura sugerida

Isso é só para ficar tudo organizado dentro da pasta do projeto. Mas eu mesmo tenho usado muito com caminhos completos (absolutos). Exemplo de um comando que acabei de usar para transcrever um vídeo que gravei para o Youtube:

```sh
nlingua2 transcribe -i "/Users/luizotavio/Desktop/three_ALTERED.mp4" -f portuguese -o "/Users/luizotavio/Desktop/three_ALTERED.srt"
```

```
.
├── videos/              # Seus vídeos de entrada (.mp4, .mkv, etc)
├── srt/                 # Legendas originais transcritas (.srt)
├── srt-ready/           # Legendas traduzidas (.srt)
├── src/nlingua2/        # Código-fonte do projeto
├── pyproject.toml       # Configuração de dependências e CLI
└── README.md
```

---

## 📃 Licença

MIT — Faça o que quiser 😎

---

## 💬 Autor

Feito por [Luiz Otávio Miranda](https://otaviomiranda.com.br), com carinho por código limpo e ódio por dependência de nuvem em IA local 🧠🔥
