<template>
    <v-btn-toggle
        v-model="choice"
        color="deep-purple accent-3"
        group
        class="d-flex flex-column"
      >
        <v-btn value="jumpRef">
          Jump Ref
        </v-btn>
        <v-btn value="if">
          If
        </v-btn>

        <v-btn value="fun">
          Function
        </v-btn>

        <v-btn value="module">
          Module
        </v-btn>

        <v-btn value="for">
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
