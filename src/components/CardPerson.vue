<template>
  <div class="card-container">
    <q-card class="my-card" bordered 
    style="background: linear-gradient(140deg, rgba(2,0,36,1) 0%, rgba(25,118,210,1) 0%, rgba(234,242,249,1) 0%, rgba(214,214,214,1) 100%);">
      <q-card-section horizontal>
        <q-img
          class="col-5 my-card-img"
          :src="props.data.img"
        />
        <q-card-section class="id-section">
          <div>
          <p><b>Nome:</b> {{ props.data.nome }}</p>
          <p><b>Nascimento:</b> {{ props.data.data_nasc }}</p>
          <p><b>Gênero musical predileto:</b> {{ props.data.genero_mus }}</p>
          <p><b>Artista preferido:</b> {{ props.data.artista }}</p>
          <p><b>Filme preferido:</b> {{ props.data.filme }}</p>
          <p><b>Frase preferida:</b> {{ props.data.frase }}</p>
          <!-- <p><b>Tema de Pesquisa:</b> {{ props.data.tema_pesquisa }}</p> -->
          </div>
          <div class="triangle-card"><img src="src/assets/nca_logo.png"></div>
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
.triangle-card{
  float: right;
  margin-top:-5em;
  margin-bottom: -1.5em;
}
.triangle-card > img{
  width: 10em;
  opacity: 0.3;
  /* height: 90px; */
}
.id-section > div{
  position: relative;
}
</style>