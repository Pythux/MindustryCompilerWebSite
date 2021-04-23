<template>
  <v-container>
    <div class="title">Code with ease</div>
    <div class="codeZone">
      <textarea id="from-source" name="from-source"></textarea>
      <!-- <v-textarea
          solo
          no-resize
          name="code"
          label="type code here"
        ></v-textarea> -->
    </div>
    <div class="complieBtn">
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

  export default Vue.extend({
    name: 'HelloWorld',

    data: () => ({
        loadingCompiling: false,
      }
    ),
  })
</script>


<style>

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  .container {
    height: 100%;
  }

  .container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 10px;
    grid-auto-rows: minmax(100px, auto);
    grid-auto-columns: minmax(100px, auto);
    /* grid-template-areas:
      "title title title"
      "codeZone complieBtn compileZone"
      "codeZone complieBtn compileZone"
      "codeZone complieBtn compileZone"
      "codeZone complieBtn compileZone" */
  }

  textarea {
    resize: none !important;
    /* height: 100%; */
    height: 80vh;
    flex-grow: 1;
    /* width: 100%; */
    padding: 20px;
    margin: 10px;
  }

  .title {
    /* grid-area: title; */
    grid-row: 1;
    grid-column: 1 / 4;
    background-color: red;
    /* max-height: 150px; */
  }

  .codeZone {
    /* grid-area: codeZone; */
    grid-row: 2;
    grid-column: 1;

    background-color: teal;
    display: flex;
    flex-direction: column;
  }

  .complieBtn {
    /* grid-area: complieBtn; */
    grid-row: 2;
    grid-column: 2;
    background-color: rgb(147, 242, 255);
  }

  .compileZone {
    /* grid-area: compileZone; */
    grid-row: 2;
    grid-column: 3;
    background-color: gray;
  }

</style>
