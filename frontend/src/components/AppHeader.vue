<script setup lang="ts">
// Removed scroll detection logic
</script>

<template>
  <header class="app-header">
    <div class="header-content">
      <div class="logo">
        <div class="logo-icon">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="42"
            height="42"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
            <path d="M2 17l10 5 10-5"></path>
            <path d="M2 12l10 5 10-5"></path>
          </svg>
        </div>
        <div class="logo-text">
          <span>Sistema de Consulta</span>
          <div class="logo-subtitle">
            Plataforma de Informações de Operadoras de Saúde
          </div>
        </div>
      </div>
      <div class="header-actions">
        <slot name="actions"></slot>
      </div>
    </div>
    <div class="header-banner">
      <div class="banner-content">
        <h2>Encontre informações sobre operadoras de saúde</h2>
        <p>Consulte detalhes sobre empresas, representantes, contatos e mais</p>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header-content {
  max-width: var(--content-max-width);
  margin: 0 auto;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2rem;
}

.logo {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logo-text {
  display: flex;
  flex-direction: column;
}

.logo-text span {
  font-size: 2rem;
  font-weight: 700;
  color: var(--primary-dark);
  line-height: 1.1;
  transition: all var(--transition-slow);
}

.logo-subtitle {
  font-size: 0.9rem;
  color: var(--text-secondary);
  transition: opacity var(--transition-fast);
}

.header-banner {
  width: 100%;
  max-width: var(--content-max-width);
  margin: 0 auto;
  padding: 1rem 2rem;
  margin-top: 0.5rem;
  transition: all var(--transition-slow);
}

.banner-content {
  color: var(--text-secondary);
}

.banner-content h2 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: var(--primary-dark);
}

.banner-content p {
  font-size: 1rem;
  color: var(--text-secondary);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

@media (max-width: 768px) {
  .logo-text span {
    font-size: 1.5rem;
  }

  .logo-subtitle {
    display: none;
  }

  .banner-content h2 {
    font-size: 1.25rem;
  }

  .banner-content p {
    font-size: 0.875rem;
  }
}
</style>
