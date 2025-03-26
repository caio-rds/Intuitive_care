<script setup lang="ts">
import { defineProps } from 'vue';
import type { ResponseItem } from '../App.vue';

defineProps<{
  responseItem: ResponseItem;
}>();
</script>

<template>
  <div>
    <p>Razão Social: {{ responseItem.razao_social }}</p>
    <div class="Horizontal">
      <p>CNPJ: {{ responseItem.cnpj }}</p>
      <p v-if="responseItem.nome_fantasia">Nome Fantasia: {{ responseItem.nome_fantasia }}</p>
    </div>
    <p>Modalidade: {{ responseItem.modalidade }}</p>
    <p>Logradouro: {{ responseItem.logradouro }}</p>
    <p>Número: {{ responseItem.numero }}</p>
    <p v-if="responseItem.complemento">Complemento: {{ responseItem.complemento }}</p>
    <p>Bairro: {{ responseItem.bairro }}</p>
    <p>Cidade: {{ responseItem.cidade }}</p>
    <p>UF: {{ responseItem.uf }}</p>
    <p>CEP: {{ responseItem.cep }}</p>
    <div class="Horizontal" v-if="responseItem.telefone">
       <p v-if="responseItem.ddd">({{ responseItem.ddd }})</p>
       - {{ responseItem.telefone }}
    </div>
    <p v-if="responseItem.fax">Fax: {{ responseItem.fax }}</p>
    <p v-if="responseItem.email">Email: {{ responseItem.email }}</p>
    <p>Representante Legal: {{ responseItem.representante_legal }}</p>
    <p>Cargo do Representante: {{ responseItem.cargo_representante }}</p>
    <p v-if="responseItem.regiao_operacao">Região de Operação: {{ responseItem.regiao_operacao }}</p>
    <p>Data de Registro: {{ responseItem.data_registro }}</p>
  </div>
</template>

<style scoped>
/* Adicione seus estilos aqui */
</style>