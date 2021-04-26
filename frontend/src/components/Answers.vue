<template>
  <ul class="list-unstyled w-50 mx-auto ">
    <b-media class="mt-3" tag="li" v-for="item in query_set" :key="item._id">
      <template #aside>
        <b v-if="sort_ == 'elasticsearch' ">ES score <br>{{ item._score }}</b>
        <b v-else>Stack score <br>{{ item._source.score }}</b>
      </template>
      <h5 class="mt-0 mb-1 text-justify" v-if="highlight && item.highlight.title"><span v-html="item.highlight.title[0]"></span></h5>
      <h5 class="mt-0 mb-1 text-justify" v-else>{{ item._source.title}}</h5>
      <p class="mb-0 text-justify" v-if="highlight && item.highlight.body">
         <span v-html="item.highlight.body[0]"></span>
      </p>
        <p class="mb-0 text-justify" v-else>
         {{ item._source.body }}
       </p>
    </b-media>
  </ul>
</template>

<script>
export default {
    props: ['query_set', 'highlight', 'sort_']
}
</script>

<style>

</style>