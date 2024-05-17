<template>
  <div class="card-container">
    <q-card class="my-card" flat bordered>
      <q-card-section horizontal>
        <q-img
          class="col-5 my-card-img"
          :src="props.data.img"
        />
        <q-card-section>
          <p>Nome: {{ props.data.nome }}</p>
          <p>Nascimento: {{ props.data.data_nasc }}</p>
          <p>Gênero musical predileto: {{ props.data.genero_mus }}</p>
          <p>Artista preferido: {{ props.data.artista }}</p>
          <p>Filme preferido: {{ props.data.filme }}</p>
          <p>Frase preferida: {{ props.data.frase }}</p>
        </q-card-section>

      </q-card-section>
    </q-card>
  </div>
</template>

<script setup>

defineOptions({
  name: 'CardPerson'
})

const props = defineProps({
  data: {
    type: Object,
    required: true
  },
})
</script>

<style scoped>
.card-container{
  width: 500px;
  /* height: 50%; */
  display: flex;
  margin-top: 10px;
}
/* .my-card-img{
  width: 100%;
  height: 100%;
} */
</style>