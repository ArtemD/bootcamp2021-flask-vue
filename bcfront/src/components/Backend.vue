<template>
    <div id="results">        
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
    name: 'Backend',
    data(){
            return {
                licenses: null
            }

    },
    created: function(){
        axios.get('https://heroku-bootcamp-a3255.ondigitalocean.app/api/all').then(res=> {
            this.licenses = res.data.data;
        })
    }
}
</script>

<style scoped>

</style>