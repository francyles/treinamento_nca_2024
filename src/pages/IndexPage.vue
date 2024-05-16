<template>
  <q-page class="flex flex-center main-cards">
    <div v-for="d in data" :key="d">
      <CardPerson :data="d"></CardPerson>
    </div>
  </q-page>
</template>

<script setup>
import CardPerson from 'components/CardPerson.vue';
import data from 'assets/database.json'

defineOptions({
  name: 'IndexPage'
});

</script>
<style scoped>
.main-cards{
  justify-content: space-between;
}
</style>