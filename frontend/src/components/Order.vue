<template>
    <b-button size="lg" variant="primary-outline" @click="order_change" class="mb-2">
        Order
      <b-icon  v-if="order=='asc'"  icon="arrow-up"></b-icon>
      <b-icon  v-else  icon="arrow-down"></b-icon>
    </b-button>
</template>

<script>
export default {
    data() {
        return {
            selected: 'elasticsearch'
        }
    },
    props: ['order'],
    methods: {
        order_change(){
            this.$emit('order_change')
        }
    }
}
</script>