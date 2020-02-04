<template>
  <div class="attentionList">
    <span v-for="attention in attentionList" v-bind:key="attention">
      <li v-for="s in attention" v-bind:key="s">
        {{ s }}
      </li>
    </span>
  </div>
</template>

<script>
import VisualizeBack from './VisualizeBack.vue'

export default {
  components: {
    //VisualizeBack
  },
  data() {
    return {
      attentionList: require("../assets/features.json")
    }
  }
}
</script>
