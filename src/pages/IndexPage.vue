<template>
  <q-page>
    <h5 class="text-title">Professor</h5>
    <div class="flex flex-center">
    <CardPerson :data="data[0]"></CardPerson>
    </div>
    <br>
    <q-separator size="2px" inset/>
    <h5 class="text-title">Alunos</h5>
    <div v-show="data.length < 2"><h5 style="color:gray; opacity: 0.5; text-align: center;">Nenhum aluno cadastrado</h5></div>
    <div class="flex main-cards">
      <div v-for="d in data.slice(1,)" :key="d">
        <CardPerson :data="d"></CardPerson>
      </div>
    </div>
    
    <!--  -->
  </q-page>
</template>

<script setup>
import CardPerson from 'components/CardPerson.vue';
import data from 'src/utils/database.json'

defineOptions({
  name: 'IndexPage'
});

</script>
<style scoped>
.main-cards{
  margin-left: 16px;
  /* justify-content: space-between; */
}
.text-title{
  text-align: center;
}
</style>