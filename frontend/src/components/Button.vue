<template>
    <div>
          <b-button @click="search" pill variant="outline-success">Search</b-button>
    </div>
</template>

<script>
export default {
    methods: {
        search(){
            this.$emit('search')
        }
    }
}
</script>

