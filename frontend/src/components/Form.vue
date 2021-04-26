<template>
  <div>
    <b-form-input @input="$emit('query', $event)" v-model="query" class="p-3" placeholder="Enter your query"></b-form-input>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        query: ''
      }
    }
  }
</script>