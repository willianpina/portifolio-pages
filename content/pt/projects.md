<div class="projects-section">

  <!-- HEADER -->
  <div class="projects-header">
    <h2>Projetos</h2>
    <span class="section-accent"></span>
  </div>

  <!-- FILTERS -->
  <div class="projects-filters">
    <button class="active" data-filter="all">Todos</button>
    <button data-filter="geospatial">Geospatial AI</button>
    <button data-filter="cv">Visão Computacional</button>
    <button data-filter="ds">Data Science</button>
    <button data-filter="msc">Mestrado</button>
  </div>

  <!-- GRID -->
  <div class="projects-grid">

    <!-- PROJECT 1 — COVID 19 ANÁLISE DE IMPACTO USANDO LINGUAGEM R -->
    <div class="project-card" data-category="msc ds">
      <img src="images/projects/Analysis_of_the_Impacts_of_COVID_19.jpeg" alt="Master's Degree Project">

      <div class="project-overlay">
        <h3>Análise dos Impactos da COVID-19 nas Populações Globais</h3>

        <p class="project-description">
          Análise de dados globais da COVID-19, com foco em casos confirmados e óbitos,
          aplicada a países com população superior à do Brasil.
        </p>

        <p class="project-tags">
          Mestrado · Ciência de Dados · Estatística · Linguagem R
        </p>

        <div class="project-links">
          <a href="https://github.com/willianpina/MSDS_Colorado_Boulder/tree/main/Analysis%20of%20the%20Impacts%20of%20COVID-19" target="_blank">GitHub</a>
          <a href="https://github.com/CSSEGISandData/COVID-19" target="_blank">Conjunto de dados</a>
        </div>
      </div>
    </div>

    <!-- PROJECT 2 — BBC NEWS Classification-->
    <div class="project-card" data-category="msc ds nlp">
      <img src="images/projects/BBC_News_Classification.jpg" alt="BBC News Classification">

      <div class="project-overlay">
        <h3>Classificação de Notícias da BBC com Aprendizado Não Supervisionado</h3>

        <p class="project-description">
          Projeto acadêmico que explora técnicas de aprendizado não supervisionado, com ênfase em fatoração de matrizes, para identificar e classificar automaticamente
          categorias de notícias da BBC a partir de textos.
        </p>

        <p class="project-tags">
          Aprendizado Supervisionado · Matrix Factorização · NLP
        </p>

        <div class="project-links">
          <a href="https://github.com/willianpina/MSDS_Colorado_Boulder/tree/main/BBC%20News%20Classification" 
            target="_blank">GitHub</a>
        </div>
      </div>
    </div>

    <!-- PROJECT 3 — Detecção de Câncer -->
    <div class="project-card" data-category="msc cv">
      <img src="images/projects/Cancer_Detection.jpg" alt="Detecção de Câncer">

      <div class="project-overlay">
        <h3>Detecção de Câncer Metastático em Imagens de Patologia Digital</h3>

        <p class="project-description">
          Classificação binária de imagens histopatológicas para detecção de câncer metastático em patches de patologia digital.
        </p>

        <p class="project-tags">
          Visão Computacional · TensorFlow · Imagens Médicas
        </p>

        <div class="project-links">
          <a href="https://github.com/willianpina/MSDS_Colorado_Boulder/blob/main/CNN%20Cancer%20Detection%20Project/CNN_Cancer_Detection_Project.ipynb" target="_blank">GitHub</a>
        </div>
      </div>
    </div>

    <!-- PROJECT 4 — Análise do Mercado de Trabalho -->
    <div class="project-card" data-category="ds msc">
      <img src="images/projects/Data_Scientist_Job_Market_UK.jpg" alt="Job Market">

      <div class="project-overlay">
        <h3>Análise do Mercado de Trabalho para Cientistas de Dados no Reino Unido</h3>

        <p class="project-description">
          Análise exploratória de vagas para cientistas de dados no Reino Unido, 
          investigando variações salariais, habilidades mais demandadas e a relação entre avaliação das empresas, trabalho remoto e remuneração.
        </p>

        <p class="project-tags">
          Análise de Dados · Visualização de Dados · Análise de Mercado de Trabalho
        </p>

        <div class="project-links">
          <a href="https://github.com/willianpina/MSDS_Colorado_Boulder/blob/main/Data%20Scientist%20Job%20Market%20UK/Final_Project.ipynb" target="_blank">GitHub</a>
        </div>
      </div>
    </div>

    <!-- PROJECT 5 — ENEM 2022 -->
    <div class="project-card" data-category="ds msc">
      <img src="images/projects/Data_Scientist_Job_Market_UK.jpg" alt="Job Market">

      <div class="project-overlay">
        <h3>Análise Preditiva do Desempenho no ENEM 2022</h3>

        <p class="project-description">
          Aplicação de técnicas de aprendizado supervisionado para analisar e prever o
          desempenho de estudantes no ENEM 2022, considerando fatores demográficos, sociais e educacionais a partir de microdados oficiais do INEP.
        </p>

        <p class="project-tags">
          Aprendizado Supervisionado · Análise Educacional · Ciência de Dados
        </p>

        <div class="project-links">
          <a href="https://github.com/willianpina/MSDS_Colorado_Boulder/blob/main/Data%20Scientist%20Job%20Market%20UK/Final_Project.ipynb" target="_blank">GitHub</a>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ================= FILTER SCRIPT ================= -->
<script>
  const filterButtons = document.querySelectorAll(".projects-filters button");
  const projectCards = document.querySelectorAll(".project-card");

  filterButtons.forEach(button => {
    button.addEventListener("click", () => {
      // Active state
      filterButtons.forEach(btn => btn.classList.remove("active"));
      button.classList.add("active");

      const filter = button.dataset.filter;

      projectCards.forEach(card => {
        const categories = card.dataset.category;

        if (filter === "all" || categories.includes(filter)) {
          card.style.display = "block";
        } else {
          card.style.display = "none";
        }
      });
    });
  });
</script>
