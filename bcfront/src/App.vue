<template>
  <div id="app">
    <h1>Search alcohol licenses in Finland</h1>
    <Search />
    
  </div>
</template>

<script>
import Search from './components/Search.vue'

export default {
  name: 'App',
  components: {
    Search
  }
}
</script>

<style>
#app {
  margin-left: 30px;
  margin-right: 30px;
}
h1 {
    text-align: center;
}
</style>
