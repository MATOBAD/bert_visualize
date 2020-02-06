<template>
  <div>
    <span v-for='i of len' v-bind:key='i'>
        <span class="word" v-bind:style="{ backgroundColor: calcWeight(weight[i-1]) }" v-bind:title="titleMessage(weight[i-1])">
          {{ sentence[i-1] }}
        </span>
    </span>
  </div>
</template>

<script>  
export default {
  props: {
    sentence: Array,
    weight: Array
  },
  data() {
    return {
        len: this.sentence.length
    }
  },
  methods: {
    calcWeight (weight) {
      const red = 255
      const green = Math.floor(255 * (1 - Number(weight)))
      const blue = Math.floor(255 * (1 - Number(weight)))
      return '#' + red.toString(16).toUpperCase().substring(0, 2) +
             green.toString(16).toUpperCase().substring(0, 2) +
             blue.toString(16).toUpperCase().substring(0, 2)
    },
    titleMessage (weight) {
      return 'weight：' + weight
    }
  }
}
</script>

<style scoped>
.word {
  cursor: default;
  font-size: 120%;
}
.word:hover {
  opacity: 0.6;
}
</style>
