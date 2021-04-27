<template>
    <v-row>
        <v-col cols="6" md="5" class="d-flex">
            <textarea id="code-source" name="code-source"></textarea>
        </v-col>
        <v-col cols="12" md="4" class="complieBtn d-flex flex-column justify-space-around align-center">
            <v-alert
                v-model="alertVisible"
                border="left"
                colored-border
                dismissible
                elevation="6"
                type="error"
            >{{compilError}}</v-alert>
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
        <v-col cols="6" md="3" class="d-flex">
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
            alertVisible: false,
            compilError: null,
        }
    ),
    components: {
        Intro,
        ExempleCode,
    },
    methods: {
        changeChoiceCode(choice: string | null) {
            this.alertVisible = false
            if (choice === null || choice === undefined) {
                document.querySelector("#code-source").value = '// code stuff here'
                document.querySelector("#asm").value = ''
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
                    document.querySelector("#code-source").value = text
                })
            })
            fetch(`exemples/${exemple}.asm`, { method: "GET" })
            .then(response => {
                let r = response.text()
                r.then(text => {
                    document.querySelector("#asm").value = text
                })
            })
        },
        async compileCode() {
            this.alertVisible = false
            this.loadingCompiling = true
            let url = this.serverUrl()
            try {
                let response = await this.post(`${url}/api/compile`, { data: document.querySelector("#code-source").value })
                let data = await response.json()
                this.handleCompileResponce(data)

            } catch (error) {
                console.warn("fail to request API")
                console.log(error)
            } finally {
                // end waiting for an awnser
                this.loadingCompiling = false
            }
        },
        handleCompileResponce(data) {
            if ('asm' in data) {
                document.querySelector("#asm").value = data.asm
            } else if ('error' in data) {
                this.compilError = data.error
                this.alertVisible = true
            } else {
                console.warn('bad data recv')
            }
        },
        serverUrl() {
            console.log(process.env.VUE_APP_BACK)
            let location = window.location
            let domain = location.protocol + '//' + location.hostname
            let port = 5000
            let url = `${domain}:${port}`
            return url
        },
        post(url, content) {
            return fetch(url, {
                method: "POST",
                body: JSON.stringify(content),
                headers: {'Content-Type': 'application/json', },
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
    min-height: 250px;
}

.v-btn__content {
    text-transform: none;
}


@media only screen and (max-width: 960px) {
  .complieBtn {
      order: -1;  /* put this first in list */
  }
}


</style>
