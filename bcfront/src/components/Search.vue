<template>
    <div id="search">
        <label for="keyword">Search database</label>
        <input v-model="keyword" type="text" placeholder="Search something here" name="key">
        Keyword is: {{ keyword }}
            <table>
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Business ID</th>
                    <th scope="col">City</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="license in licenses" :key="license.id">
                    <th scope="row">{{ license[1]}}</th>
                    <td>{{license[7]}}</td>
                    <td>{{license[4]}}</td>
                </tr>
            </tbody>
        </table>
        </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Search',
    data(){
        return {
            keyword: null,
            licenses: null,
            url: null
            }

    },
    watch: {
        keyword: function (){
            this.url='https://heroku-bootcamp-a3255.ondigitalocean.app/api/search/'+ this.keyword;
            axios.get(this.url).then(res=> {
            this.licenses = res.data.data;
        })
    }
    }
}
</script>

<style scoped>

</style>