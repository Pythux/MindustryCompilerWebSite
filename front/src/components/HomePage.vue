<template>
    <div class="gridContent">
        <div id="codeDiv">
            <textarea id="code-source" name="code-source"></textarea>
        </div>
        <div class="menuDiv d-flex flex-column justify-center align-center">
            <Intro id="intro" />
            <ExempleCode v-on:choice="changeChoiceCode" class="exempleCode" />
            <v-btn
                id="compileButton"
                class="mt-10 mb-6"
                color="#6ddccf"
                dark
                elevation="2"
                large
                :loading="loadingCompiling"
                @click="compileCode"
            >>> Compile >></v-btn>
            <v-alert
                v-model="alertVisible"
                border="left"
                colored-border
                dismissible
                elevation="6"
                type="error"
            >{{compilError}}</v-alert>
        </div>
        <div id="asmDiv" class="d-flex">
            <textarea id="asm" name="asm" readonly></textarea>
        </div>
    </div>
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
            let url = process.env.VUE_APP_BACK
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
                document.querySelector("#asm").value = ''
                this.compilError = data.error
                this.alertVisible = true
            } else {
                console.warn('bad data recv')
            }
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

.codeDiv {
    grid-area: codeDiv;
}
.menuDiv {
    grid-area: menuDiv;
}
.asmDiv {
    grid-area: asmDiv;
}

.gridContent {
    height: 100%;
    display: grid;
    grid-template-rows: 1fr;  /* key rule */
    grid-template-columns: 1fr auto 1fr;
    grid-template-areas: "codeDiv menuDiv asmDiv";
}

textarea {
    resize: none !important;
    padding: 20px;
    margin: 10px;
    width: 100%;
    border: 2px solid #ffeabd;
    border-radius: 8px;
    height: calc(100% - 20px);
}

.v-btn__content {
    text-transform: none;
}

.exempleCode {
    flex-direction: column;
}


@media only screen and (max-width: 960px) {
    .exempleCode {
        flex-direction: row;
        flex-wrap: wrap;
    }
    #intro {
        display: none;
    }
    .gridContent {
        display: grid;
        grid-template-rows: auto 1fr;  /* key rule */
        grid-template-columns: 1fr 1fr;
        grid-template-areas: "menuDiv menuDiv"
                              "codeDiv asmDiv";
    }
    textarea {
        margin: 2px;
        padding: 4px;
        line-height: 1;
        height: calc(100% - 4px);
    }
    #codeDiv {
        padding: 3px;
    }
    #asmDiv {
        padding: 3px;
    }
    .exempleCode button {
        height: 28px !important;
    }
}


</style>
