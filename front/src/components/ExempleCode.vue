<template>
    <v-btn-toggle
        v-model="choice"
        color="#94ebcd"
        group
        class="d-flex flex-column"
      >
        <v-btn value="jump">
          Jump Ref
        </v-btn>
        <v-btn value="if">
          If
        </v-btn>

        <v-btn value="function">
          Function
        </v-btn>

        <v-btn value="module">
          Module
        </v-btn>

        <v-btn value="forLoop">
          For loop
        </v-btn>
      </v-btn-toggle>
</template>

<script>
export default {
    data() {
        return {
            choice: null,
        }
    },
    watch: {
        choice() {
            this.$emit('choice', this.choice)
        }
    }
}
</script>

<style>

</style>
