<template>
    <div id="app">
        <h1>Stackoverflow questions</h1>
        <div class="d-flex justify-content-around">
            <b-form inline class="my-4">
                <Form @query="query" />
                <Sort @sort="sort" />
                <Order @order_change="order_change" :order="order" />
                <Options @option="option" />
                <Button @search="search" />
            </b-form>
        </div>
        <div v-if="resp !== null">
            <H3>Total {{ resp.hits.total.value }}</H3>
            <Answers :query_set="query_set" :highlight="highlight" :sort_="sort_" />
        </div>
        <div v-if="resp" v-observe-visibility="handleScrolledToBotoom"></div>
    </div>
</template>

<script>
import axios from 'axios';
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'


import Form from './components/Form.vue';
import Options from './components/Options.vue';
import Button from './components/Button.vue';
import Sort from './components/Sort.vue';
import Order from './components/Order.vue';
import Answers from './components/Answers.vue';



export default {
    name: 'App',
    components: {
        Form,
        Options,
        Button,
        Sort,
        Order,
        Answers
    },
    data() {
        return {
            resp: null,
            sort_: 'elasticsearch',
            query_: null,
            order: 'desc',
            highlight: false,
            from: 0,
            all: false,
        }
    },
    computed: {
        query_set: function() {
            if (this.order == 'desc') {
                return this.resp.hits.hits;
            }
            return this.resp.hits.hits.slice().reverse();
        }
    },
    methods: {
        option(e) {
            if (e.includes('highlight')) {
                this.highlight = true;
            } else {
                this.highlight = false;
            }
            if (e.includes('all')) {
                this.all = true;
            } else {
                this.all = false;
            }
        },
        query(e) {
            this.query_ = e;
        },
        sort(e) {
            this.sort_ = e;
            this.search();
        },
        search() {
            this.from = 0;
            axios
                .post('//localhost:8000/api/query/', { 'query': this.query_, 'sort_by': this.sort_, 'fields': this.all, 'from': this.from })
                .then(response => (this.resp = response.data))
        },
        order_change() {
            if (this.order === 'asc') {
                this.order = 'desc';
            } else {
                this.order = 'asc';
            }
        },
        handleScrolledToBotoom(isVisible) {
            if (!isVisible || this.order == 'asc') { return }

            this.from = this.from + 10
            axios
                .post('//localhost:8000/api/query/', { 'query': this.query_, 'sort_by': this.sort_, 'fields': 'all', 'from': this.from })
                .then(response => (this.resp.hits.hits.push(...response.data.hits.hits)))
        }
    }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
