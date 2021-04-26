<template>
    <div>
        <b-form-checkbox-group @change="$emit('option', $event)" v-model="selected" :options="options" class="mx-3" value-field="item" text-field="name" disabled-field="notEnabled"></b-form-checkbox-group>
    </div>
</template>


<script>
export default {
    data() {
        return {
            selected: [],
            options: [
                { item: 'highlight', name: 'Highlight' },
                { item: 'all', name: 'Title & Body'}
            ]
        }
    }
}
</script>