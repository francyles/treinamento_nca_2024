<template>
  <q-page class="">
    <div class="flex flex-center">
    <CardPerson :data="data[0]"></CardPerson>
    </div>
    <br>
    <q-separator size="2px" inset/>
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
import data from 'assets/database.json'

defineOptions({
  name: 'IndexPage'
});

</script>
<style scoped>
.main-cards{
  margin-left: 16px;
  justify-content: space-between;
}
</style>