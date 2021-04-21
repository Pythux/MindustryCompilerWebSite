<template>
  <v-container>
    <div class="title">Code with ease</div>
    <div class="codeZone">
      <v-textarea
          solo
          :height="textAreaHeight"
          name="code"
          label="type code here"
        ></v-textarea>
    </div>
    <div class="compileZone">
      <v-textarea
          solo
          :height="textAreaHeight"
          name="compiled"
          label='the compiled code will appear here'
          readonly
        ></v-textarea>
    </div>
    <div class="compileBottom">
      <v-btn
          color="cyan"
          dark
          elevation="2"
          large
          :loading="loadingCompiling"
        >Compile</v-btn>
    </div>
    <div class="codeBottom">
        <div>
          vanilla
        </div>
        <div>
          with reference
        </div>
        <div>
          if condition
        </div>
        <div>
          and much more
        </div>
    </div>
  </v-container>
</template>


<script lang="ts">
  import Vue from 'vue'

  export default Vue.extend({
    name: 'HelloWorld',

    data: () => ({
        loadingCompiling: false,
        textAreaHeight: 10,
      }
    ),
    // mounted() {
    //   this.textAreaHeight = window.innerHeight * 0.80
    // },
  })
</script>


<style>
    html,
    body,
    .container {
      height: 100vh;
      text-align: center;
    }

    .container {
      display: grid;
      grid-template-areas:
        "title title title"
        "codeZone codeZone compileZone"
        "codeBottom codeBottom compileBottom";
    }

    .title {
      grid-area: title;
      background-color: red;
    }

    .codeZone {
      grid-area: codeZone;
      background-color: teal;
    }

    .compileZone {
      grid-area: compileZone;
      background-color: gray;
    }

    .codeBottom {
      grid-area: codeBottom;
      background-color: tomato;
    }

    .compileBottom {
      grid-area: compileBottom;
      background-color: yellow;
    }

</style>
