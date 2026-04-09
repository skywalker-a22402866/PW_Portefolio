# 📚 Repositório PW — Estrutura da Base de Dados

## 🧠 Visão Geral

### 🎓 Licenciatura
- UCs
- Imagem

### 📖 UCs (Unidades Curriculares)
- Apresentação
- Projetos
- Imagem
- Docentes
- Semestres
- ECTS

### 🧑‍🏫 Docentes
- Nome
- Imagem
- Link página pessoal Lusófona

### 📁 Projetos
- Nome
- UC
- Descrição
- Imagem
- Link GitHub

### 🛠️ Tecnologias
- Tipo
- Nome
- Logo
- Link
- Nível de Interesse

### 🧪 TFC
- Nome
- Resumo
- Tecnologias
- Imagem
- Docente

### 🧠 Competências
- Nome
- Nível
- Formação
- Tecnologia

### 📈 Formação
- Nome
- Data
- Descrição

### 🎬 Making Of
- Nome
- Data
- Imagem
- Descrição

---

## 🗂️ DER (Diagrama Entidade-Relacionamento)

```
[Licenciatura]
├── nome
├── imagem
│
│ 1:N
↓
[UnidadeCurricular]
├── nome
├── apresentacao
├── semestre
├── ects
│
├── 1:N → [Projeto]
├── 1:N → [Imagem]
└── N:M → [Docente]

[Docente]
├── nome
├── imagem
├── link_lusofona
│
├── N:M → UnidadeCurricular
└── 1:N → TFC

[Projeto]
├── nome
├── descricao
├── imagem
├── github
│
└── N:1 → UnidadeCurricular

[TFC]
├── nome
├── resumo
├── imagem
│
├── N:1 → Docente
└── N:M → Tecnologia

[Tecnologia]
├── nome
├── tipo
├── logo
├── link
├── nivel_interesse
│
├── N:M → TFC
└── 1:N → Competencia

[Formacao]
├── nome
├── data
├── descricao
│
└── 1:N → Competencia

[Competencia]
├── nome
├── nivel
│
├── N:1 → Formacao
└── N:1 → Tecnologia

[MakingOf]
├── nome
├── data
├── imagem
├── descricao
```

