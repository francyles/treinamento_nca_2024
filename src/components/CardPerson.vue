<template>
    <q-card class="my-card" flat bordered>
      <q-card-section horizontal>
        <q-img
          class="col-5"
          src="https://cdn.quasar.dev/img/parallax2.jpg"
        />
        <q-card-section>
          Nome: {{ props.data.nome }}
          Nascimento: {{ props.data.data_nasc }}
        </q-card-section>

      </q-card-section>
    </q-card>
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