#Repositorio PW

🧠 VISÃO FINAL DA BD

🎓 Licenciatura
-UCs
-Imagem


UCs
-Apresentação
-Projetos
-Imagem
-Docentes
-Semestres
-ECTS

🧑‍🏫 Docentes
-Nome
-Imagem
-Link pagina pessoal Lusofona


📁 Projetos
-Nome
-UC
-Descrição
-imagem
-Link GitHub

🛠️ Tecnologias
-Tipo
-Nome
-Logo
-Link
-Nivel de Interesse

🧪 TFC
-Nome
-Resumo
-tecnologias
-Imagem
-Docente

Competências
-Nome
-Nivel
-Formação
-Tecnologia

📈 Formação
-Nome
-Data
-Descrição

🎬 MakingOf
-Nome
-data
-imagem
-Descrição




____________________________________________________________________________________________________________________________________________________________________

DER (Diagrama Entidade-Relacionamento)

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
   └── 1:N → Competência

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

