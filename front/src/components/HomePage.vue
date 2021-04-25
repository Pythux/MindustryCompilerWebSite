<template>
    <v-row>
        <v-col cols="6" class="d-flex">
            <textarea id="code-source" name="code-source"></textarea>
        </v-col>
        <v-col cols="3" class="complieBtn d-flex flex-column justify-space-around">
            <Intro />
            <v-btn
                color="#6ddccf"
                dark
                elevation="2"
                large
                :loading="loadingCompiling"
                @click="compileCode"
            >>> Compile >></v-btn>
            <ExempleCode v-on:choice="changeChoiceCode" />
        </v-col>
        <v-col cols="3" class="d-flex">
            <textarea id="asm" name="asm" readonly></textarea>
        </v-col>
    </v-row>
</template>


<script lang="ts">
import Vue from 'vue'
import Intro from './Intro.vue'
import ExempleCode from './ExempleCode.vue'

export default Vue.extend({
    data: () => (
        {
            loadingCompiling: false,
            choiceCode: null,
        }
    ),
    components: {
        Intro,
        ExempleCode,
    },
    methods: {
        changeChoiceCode(choice: string | null) {
            if (choice === null || choice === undefined) {
                document.querySelector("#code-source").innerHTML = '// code stuff here'
                document.querySelector("#asm").innerHTML = ''
            }
            else {
                this.setExemple(choice)
            }
        },
        setExemple(exemple: string) {
            fetch(`exemples/${exemple}.code`, { method: "GET" })
            .then(response => {
                let r = response.text()
                r.then(text => {
                    document.querySelector("#code-source").innerHTML = text
                })
            })
            fetch(`exemples/${exemple}.asm`, { method: "GET" })
            .then(response => {
                let r = response.text()
                r.then(text => {
                    document.querySelector("#asm").innerHTML = text
                })
            })
        },
        compileCode() {
            let location = window.location
            let domain = location.protocol + '//' + location.hostname
            let port = 5000
            let url = `${domain}:${port}/`
            this.loadingCompiling = true
            fetch(url + 'api/compile', {
                method: "POST",
                body: JSON.stringify({ data: document.querySelector("#code-source").value }),
                headers: {'Content-Type': 'application/json', },
            })
            .then(response => {
                response.json().then(data => {
                    document.querySelector("#asm").innerHTML = data.asm
                    }
                )
                // end waiting for an awnser
                this.loadingCompiling = true
            })
            .catch(error => {
                console.warn(error)
                // end waiting for an awnser
                this.loadingCompiling = true
            })
        }
    }
})
</script>


<style>
/* .container {
    height: 100%;
    max-width: none !important;
} */

.row {
    height: 100%;
}

textarea {
    resize: none !important;
    /* height: 100%; */
    flex-grow: 1;
    padding: 20px;
    margin: 10px;
    width: 100%;
}

.v-btn__content {
    text-transform: none;
}

</style>
