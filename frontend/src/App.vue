<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import Values from './components/values.vue';
import { mockData } from './mock.ts';
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';

export type ResponseItem = {
  id: number;
  registro_ans: string;
  cnpj: string;
  razao_social: string;
  nome_fantasia?: string;
  modalidade: string;
  logradouro: string;
  numero: string;
  complemento?: string;
  bairro: string;
  cidade: string;
  uf: string;
  cep: string;
  ddd?: string;
  telefone?: string;
  fax?: string;
  email?: string;
  representante_legal: string;
  cargo_representante: string;
  regiao_operacao?: number;
  data_registro: string;
};

const inputValue = ref('');
const responseData = ref<ResponseItem[]>([]);
const selectedValue = ref<ResponseItem | null>(null);
const usingMockData = ref(false);

const fetchData = async () => {
  try {
    usingMockData.value = false;
    const response = await axios.get(
      `http://localhost:8000/search?name=${inputValue.value}`,
    );
    responseData.value = response.data.sort(
      (a: ResponseItem, b: ResponseItem) =>
        a.razao_social.localeCompare(b.razao_social),
    );
  } catch (error) {
    console.error('Erro ao fazer o request, usando dados mock:', error);
    // Filter mock data based on input value if provided
    if (inputValue.value.trim()) {
      const searchTerm = inputValue.value.toLowerCase();
      responseData.value = mockData
        .filter(
          (item) =>
            item.razao_social.toLowerCase().includes(searchTerm) ||
            (item.nome_fantasia &&
              item.nome_fantasia.toLowerCase().includes(searchTerm)),
        )
        .sort((a, b) => a.razao_social.localeCompare(b.razao_social));
    } else {
      responseData.value = [...mockData].sort((a, b) =>
        a.razao_social.localeCompare(b.razao_social),
      );
    }
    usingMockData.value = true;
  }
};
</script>

<template>
  <div class="app-container">
    <AppHeader />

    <main class="main-content">
      <div class="search-container">
        <div class="sk-input-group">
          <input
            type="text"
            v-model="inputValue"
            @keyup.enter="fetchData"
            placeholder="Buscar por operadora de saúde..."
            class="sk-input"
          />
          <button @click="fetchData" class="sk-button sk-button-primary">
            <svg
              width="16"
              height="16"
              viewBox="0 0 13 14"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M5.73938 11.2675C6.73363 11.2685 7.70587 10.9748 8.53336 10.4236C9.36086 9.87246 10.0065 9.08846 10.3888 8.17063C10.7708 7.25267 10.8716 6.24193 10.6783 5.26661C10.485 4.2913 10.0064 3.39538 9.30313 2.6925C8.6003 1.98935 7.7048 1.51032 6.7298 1.31598C5.7548 1.12163 4.74408 1.22068 3.82536 1.60061C2.90664 1.98054 2.12117 2.62429 1.56822 3.45051C1.01527 4.27673 0.719658 5.24832 0.71875 6.2425C0.71875 7.57438 1.2475 8.85125 2.18875 9.79313C3.1303 10.7351 4.40692 11.2653 5.73875 11.2675M9.305 9.80688L12.2813 12.7813"
                stroke="currentColor"
                stroke-width="1.5"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
            <span>Buscar</span>
          </button>
        </div>

        <div v-if="usingMockData" class="mock-data-notice">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path
              d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"
            ></path>
            <line x1="12" y1="9" x2="12" y2="13"></line>
            <line x1="12" y1="17" x2="12.01" y2="17"></line>
          </svg>
          Usando dados offline (modo demonstração)
        </div>
      </div>

      <div class="content-area">
        <div v-if="selectedValue" class="details-view sk-card">
          <div class="details-header">
            <button @click="selectedValue = null" class="sk-button">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M19 12H5M12 19l-7-7 7-7"></path>
              </svg>
              Voltar
            </button>
            <h2>Detalhes da Operadora</h2>
          </div>
          <Values :response-item="selectedValue" />
        </div>
        <div v-else>
          <div
            v-if="responseData.length === 0 && inputValue"
            class="no-results sk-inset"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="8" x2="12" y2="12"></line>
              <line x1="12" y1="16" x2="12.01" y2="16"></line>
            </svg>
            <p>Nenhum resultado encontrado para "{{ inputValue }}"</p>
          </div>
          <div v-else-if="responseData.length === 0" class="empty-state">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="48"
              height="48"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="1"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <p>Utilize a barra de busca para encontrar operadoras de saúde</p>
          </div>
          <div v-else class="results-grid">
            <div
              v-for="item in responseData"
              :key="item.id"
              @click="selectedValue = item"
              class="result-card sk-card"
            >
              <div class="result-content">
                <div class="result-header">
                  <h3>{{ item.razao_social }}</h3>
                </div>
                <div class="result-info">
                  <span class="sk-badge">{{ item.modalidade }}</span>
                  <span class="location">{{ item.cidade }}, {{ item.uf }}</span>
                </div>
              </div>
              <div class="result-action">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <AppFooter />
  </div>
</template>

<style>
@import './styles/main.css';
</style>
