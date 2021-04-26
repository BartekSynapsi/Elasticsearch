<template>
    <div class="mx-3">
        <b-form-group label="Sort by" v-slot="{ ariaDescribedby }">
            <b-form-radio v-model="selected" @change="$emit('sort', $event)" :aria-describedby="ariaDescribedby" name="es-score" value="elasticsearch">Elasticsearch score</b-form-radio>
            <b-form-radio v-model="selected" @change="$emit('sort', $event)" :aria-describedby="ariaDescribedby" name="stac-score" value="stack">Stackoverflow score</b-form-radio>
        </b-form-group>
        <small>refetch</small>
    </div>
</template>

<script>
export default {
    data() {
        return {
            selected: 'elasticsearch'
        }
    }
}
</script>