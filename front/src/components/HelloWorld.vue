<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        Code with ease
      </v-col>

      <v-col cols="8">
        <v-textarea
          solo
          :height="textAreaHeight"
          name="code"
          label="type code here"
        ></v-textarea>
        <v-row>
          <v-col cols="3">
            vanilla
          </v-col>
          <v-col cols="3">
            with reference
          </v-col>
          <v-col cols="3">
            if condition
          </v-col>
          <v-col cols="3">
            and much more
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="4">
        <v-textarea
          solo
          :height="textAreaHeight"
          name="compiled"
          label='the compiled code will appear here'
          readonly
        ></v-textarea>
        <v-btn
          class="d-flex justify-start"
          color="cyan"
          dark
          elevation="2"
          large
          :loading="loadingCompiling"
        >Compile</v-btn>
      </v-col>
    </v-row>
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
    mounted() {
      this.textAreaHeight = window.innerHeight * 0.80
    },
  })
</script>
