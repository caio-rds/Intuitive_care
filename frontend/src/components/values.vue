<script setup lang="ts">
import { defineProps } from 'vue';
import type { ResponseItem } from '../App.vue';

defineProps<{
  responseItem: ResponseItem;
}>();
</script>

<template>
  <div class="details-container">
    <div class="details-sections">
      <div class="sk-section primary-section">
        <div class="sk-section-header">
          <h3 class="sk-section-title">Informações Principais</h3>
        </div>
        <div class="sk-section-content">
          <div class="detail-grid">
            <div class="detail-item">
              <div class="detail-label">Razão Social</div>
              <div class="detail-value emphasis">
                {{ responseItem.razao_social }}
              </div>
            </div>
            <div class="detail-item">
              <div class="detail-label">CNPJ</div>
              <div class="detail-value">{{ responseItem.cnpj }}</div>
            </div>
            <div class="detail-item" v-if="responseItem.nome_fantasia">
              <div class="detail-label">Nome Fantasia</div>
              <div class="detail-value">{{ responseItem.nome_fantasia }}</div>
            </div>
            <div class="detail-item">
              <div class="detail-label">Modalidade</div>
              <div class="detail-value">
                <span class="sk-badge">{{ responseItem.modalidade }}</span>
              </div>
            </div>
            <div class="detail-item">
              <div class="detail-label">Registro ANS</div>
              <div class="detail-value">{{ responseItem.registro_ans }}</div>
            </div>
            <div class="detail-item">
              <div class="detail-label">Data de Registro</div>
              <div class="detail-value">
                {{ new Date(responseItem.data_registro).toLocaleDateString() }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="details-row">
      <div class="sk-section">
        <div class="sk-section-header">
          <h3 class="sk-section-title">Endereço</h3>
        </div>
        <div class="sk-section-content">
          <div class="sk-inset address-content">
            <div class="detail-grid">
              <div class="detail-item">
                <div class="detail-label">Logradouro</div>
                <div class="detail-value">
                  {{ responseItem.logradouro }}, {{ responseItem.numero }}
                </div>
              </div>
              <div class="detail-item" v-if="responseItem.complemento">
                <div class="detail-label">Complemento</div>
                <div class="detail-value">{{ responseItem.complemento }}</div>
              </div>
              <div class="detail-item">
                <div class="detail-label">Bairro</div>
                <div class="detail-value">{{ responseItem.bairro }}</div>
              </div>
              <div class="detail-item">
                <div class="detail-label">Cidade / UF</div>
                <div class="detail-value">
                  {{ responseItem.cidade }} / {{ responseItem.uf }}
                </div>
              </div>
              <div class="detail-item">
                <div class="detail-label">CEP</div>
                <div class="detail-value">{{ responseItem.cep }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="sk-section">
        <div class="sk-section-header">
          <h3 class="sk-section-title">Contato</h3>
        </div>
        <div class="sk-section-content">
          <div class="sk-inset contact-content">
            <div class="detail-grid">
              <div class="detail-item" v-if="responseItem.telefone">
                <div class="detail-label">Telefone</div>
                <div class="detail-value contact-value">
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
                      d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
                    ></path>
                  </svg>
                  {{ responseItem.ddd ? `(${responseItem.ddd})` : '' }}
                  {{ responseItem.telefone }}
                </div>
              </div>
              <div class="detail-item" v-if="responseItem.fax">
                <div class="detail-label">Fax</div>
                <div class="detail-value contact-value">
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
                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                  </svg>
                  {{ responseItem.fax }}
                </div>
              </div>
              <div class="detail-item" v-if="responseItem.email">
                <div class="detail-label">Email</div>
                <div class="detail-value contact-value">
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
                      d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"
                    ></path>
                    <polyline points="22,6 12,13 2,6"></polyline>
                  </svg>
                  <a :href="`mailto:${responseItem.email}`">{{
                    responseItem.email
                  }}</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="sk-section">
      <div class="sk-section-header">
        <h3 class="sk-section-title">Representação</h3>
      </div>
      <div class="sk-section-content">
        <div class="detail-grid">
          <div class="detail-item">
            <div class="detail-label">Representante Legal</div>
            <div class="detail-value">
              {{ responseItem.representante_legal }}
            </div>
          </div>
          <div class="detail-item">
            <div class="detail-label">Cargo</div>
            <div class="detail-value">
              {{ responseItem.cargo_representante }}
            </div>
          </div>
          <div class="detail-item" v-if="responseItem.regiao_operacao">
            <div class="detail-label">Região de Operação</div>
            <div class="detail-value">{{ responseItem.regiao_operacao }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@import '../styles/main.css';
</style>
