<template>
    <v-container>
        <div class="codeZone">
        <textarea id="code-source" name="code-source" style="background-color: rgb(180, 255, 251);"></textarea>
        </div>
        <div class="complieBtn d-flex flex-column justify-space-around">
        <Intro />
        <v-btn
            color="cyan"
            dark
            elevation="2"
            large
            :loading="loadingCompiling"
        >>> Compile >></v-btn>
        <ExempleCode v-on:choice="changeChoiceCode" />
        </div>
        <div class="compileZone">
        <textarea id="asm" name="asm"></textarea>
        </div>
    </v-container>
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
            if (choice == 'if') {
                this.setExemple(choice)
            }
        },
        setExemple(exemple: string) {
            fetch(`${exemple}.code`, { method: "GET" })
            .then(response => {
                let r = response.text()
                r.then(text => {
                    document.querySelector("#code-source").innerHTML = text
                })
            })
            fetch(`${exemple}.asm`, { method: "GET" })
            .then(response => {
                let r = response.text()
                r.then(text => {
                    document.querySelector("#asm").innerHTML = text
                })
            })
        }
    }
})
</script>


<style>
.container {
    height: 100%;
}

.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 10px;
    grid-auto-rows: minmax(100px, auto);
    grid-auto-columns: minmax(100px, auto);
}

textarea {
    resize: none !important;
    height: 80vh;
    flex-grow: 1;
    padding: 20px;
    margin: 10px;
}

.codeZone {
    grid-row: 1;
    grid-column: 1;
    display: flex;
    flex-direction: column;
}

.complieBtn {
    grid-row: 1;
    grid-column: 2;
    /* background-color: rgb(147, 242, 255); */
}

.v-btn__content {
    text-transform: none;
}

.compileZone {
    grid-row: 1;
    grid-column: 3;
    display: flex;
    flex-direction: column;
}
</style>
