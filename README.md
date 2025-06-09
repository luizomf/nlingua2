# 🧠 nlingua² - Any Language to Any Language

A command-line tool to **transcribe and translate `.srt` subtitles** using fully offline AI models (OpenAI Whisper + Meta NLLB).

---

## ✨ Features

- 🎙️ Transcribes audio or video files to `.srt` subtitles with timestamps
- 🌍 Translates `.srt` subtitles between 200+ languages using NLLB
- 🧰 100% local, no cloud required (besides downloading the models)
- ✅ Validates files, paths, languages and prevents accidental overwrites
- 🧪 Clean CLI built with `argparse`, extensible and robust

---

## ⚙️ Install with [uv](https://github.com/astral-sh/uv)

If you're already using UV, just do your usual `uv sync`. E.g.,:

```sh
uv sync
uv run nlingua2 --help
# Or
nlingua2 --help
```

Or even:

```bash
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -e .
uv run nlingua2 --help
# Or
nlingua2 --help
````

> Requires Python 3.11. (Some libs like `sentencepiece` don't install on 3.12+)

---

## 🚀 How to Use

### 🔤 Show available languages

```bash
nlingua2 show_languages
```

---

### 🗣️ Transcribe a video file into `.srt`

You can use relative or absolute paths, both work.

```bash
nlingua2 transcribe \
  --input videos/aula01.mp4 \
  --from portuguese \
  --output srt/aula01.srt
```

---

### 🌐 Translate a `.srt` file

```bash
nlingua2 translate \
  --input srt/aula01.srt \
  --from portuguese \
  --to english \
  --output srt-ready/aula01-en.srt
```

---

### 🧠 Transcribe and translate in a single command

```bash
nlingua2 transcribe \
  --input videos/aula01.mp4 \
  --from portuguese \
  --output srt/aula01.srt \
  --translate_srt_to english
```

> This will generate two files:
>
> * `srt/aula01.srt` (original transcription)
> * `srt/aula01-en.srt` (translated version)

---

## ⚠️ Useful flags

* `--force` → overwrite existing output files
* `--from` / `--to` → language names like `english`, `portuguese`, `french`, etc
* `--input` / `--output` → full path to your `.mp4` or `.srt` file

---

## 📁 Suggested folder structure

This is optional, just a nice way to keep your project organized. You can also pass full absolute paths.

Example of a real command I just ran:

```bash
nlingua2 transcribe -i "/Users/luizotavio/Desktop/three_ALTERED.mp4" -f portuguese -o "/Users/luizotavio/Desktop/three_ALTERED.srt"
```

```
.
├── videos/              # Your input videos (.mp4, .mkv, etc)
├── srt/                 # Transcribed original subtitles (.srt)
├── srt-ready/           # Translated subtitle versions (.srt)
├── src/nlingua2/        # Source code
├── pyproject.toml       # CLI and dependency setup
└── README.md
```

---

## 📃 License

MIT — Do what you want 😎

---

## 💬 Author

Created by [Luiz Otávio Miranda](https://otaviomiranda.com.br), driven by clean code and a hatred for unnecessary cloud dependencies 🧠🔥

---

# Em Português - PT-BR

---

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
