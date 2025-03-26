<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import Values from "./components/values.vue";

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



}

const inputValue = ref('');
const responseData = ref<ResponseItem[]>([]);
const selectedValue = ref<ResponseItem | null>(null);

const fetchData = async () => {
  try {
    const response = await axios.get(`http://localhost:8000/search?name=${inputValue.value}`);
    responseData.value = response.data.sort((a: ResponseItem, b: ResponseItem) => a.razao_social.localeCompare(b.razao_social));
  } catch (error) {
    console.error('Erro ao fazer o request:', error);
  }
};
</script>

<template>
  <div class="Horizontal Search">
    <input type="text" v-model="inputValue" @keyup.enter="fetchData" />
    <button @click="fetchData">
      <svg width="13" height="14" viewBox="0 0 13 14" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M5.73938 11.2675C6.73363 11.2685 7.70587 10.9748 8.53336 10.4236C9.36086 9.87246 10.0065 9.08846 10.3888 8.17063C10.7708 7.25267 10.8716 6.24193 10.6783 5.26661C10.485 4.2913 10.0064 3.39538 9.30313 2.6925C8.6003 1.98935 7.7048 1.51032 6.7298 1.31598C5.7548 1.12163 4.74408 1.22068 3.82536 1.60061C2.90664 1.98054 2.12117 2.62429 1.56822 3.45051C1.01527 4.27673 0.719658 5.24832 0.71875 6.2425C0.71875 7.57438 1.2475 8.85125 2.18875 9.79313C3.1303 10.7351 4.40692 11.2653 5.73875 11.2675M9.305 9.80688L12.2813 12.7813" stroke="white" stroke-opacity="0.6" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
  </div>
  <div class="results">
    <div v-if="selectedValue">
      <button @click="selectedValue = null">Voltar</button>
      <Values :response-item="selectedValue" />
      <!-- Adicione mais campos conforme necessário -->
    </div>
    <div v-else v-for="item in responseData" :key="item.id" @click="selectedValue = item">
        {{ item.razao_social }}
    </div>
  </div>
</template>

<style scoped>
input {
  outline: none;
  border: none;
  height: 100%;
  border-radius: 6px;
  width: 20%;
  padding-left: 10px;
}

.Search {

  height: 40px;
  border-radius: 5px;
  column-gap: 12px;
}



.results {
  margin-top: 20px;
  overflow-y: auto;
  max-height: 800px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  width: 98vw;
}

.results > div{
  width: 60%;
  padding: 10px;
  border-bottom: 1px solid #ccc;
  cursor: pointer;
}

.results > div:last-child {
  border-bottom: none;
}

.results > div:hover {
  background-color: #868686;
}



</style>