<template>
  <v-container>
    <div class="codeZone">
      <textarea id="from-source" name="from-source"></textarea>
    </div>
    <div class="complieBtn d-flex flex-column justify-space-around">
      <Intro />
      <v-btn
          color="cyan"
          dark
          elevation="2"
          large
          :loading="loadingCompiling"
        >Compile</v-btn>
    </div>
    <div class="compileZone">
      <textarea id="to-asm" name="to-asm"></textarea>
    </div>
  </v-container>
</template>


<script lang="ts">
  import Vue from 'vue'
  import Intro from './Intro.vue'

  export default Vue.extend({
    name: 'HelloWorld',

    data: () => ({
        loadingCompiling: false,
      }
    ),
    components: {
      Intro,
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

  /* .title {
    grid-row: 1;
    grid-column: 1 / 4;
    background-color: red;
  } */

  .codeZone {
    grid-row: 1;
    grid-column: 1;

    background-color: teal;
    display: flex;
    flex-direction: column;
  }

  .complieBtn {
    grid-row: 1;
    grid-column: 2;
    background-color: rgb(147, 242, 255);
  }

  .compileZone {
    grid-row: 1;
    grid-column: 3;
    background-color: gray;
    display: flex;
    flex-direction: column;
  }

</style>
