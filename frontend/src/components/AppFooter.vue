<script setup lang="ts">
const currentYear = new Date().getFullYear();
</script>

<template>
  <footer class="app-footer">
    <div class="footer-content">
      <div class="footer-top">
        <div class="footer-logo">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
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
          <span>Sistema de Consulta</span>
        </div>
        <div class="footer-links">
          <div class="footer-column">
            <h3>Links Rápidos</h3>
            <a href="#">Início</a>
            <a href="#">Sobre</a>
            <a href="#">Contato</a>
          </div>
          <div class="footer-column">
            <h3>Recursos</h3>
            <a href="#">Documentação</a>
            <a href="#">FAQ</a>
            <a href="#">Suporte</a>
          </div>
          <div class="footer-column">
            <h3>Legal</h3>
            <a href="#">Termos</a>
            <a href="#">Privacidade</a>
            <a href="#">Cookies</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>
          © {{ currentYear }} Sistema de Consulta. Todos os direitos reservados.
        </p>
      </div>
    </div>
  </footer>
</template>

<style>
/* Importing the main CSS which already imports footer.css */
@import '../styles/main.css';
</style>
