<template>
  <div class="box" v-scroll="handleScroll">
    <span v-for="attention in attentionList" v-bind:key="attention">
      <span v-for="compose in attention" v-bind:key="compose">
        <VisualizeBack :sentence="compose.sentence"
         :weight="compose.attention_weight" />
        <br><br>
      </span>
    </span>
  </div>
</template>

<script>
import VisualizeBack from './VisualizeBack.vue'


export default {
  components: {
    VisualizeBack
  },
  data() {
    return {
      attentionList: require("../assets/features_ver2.json")
    }
  }
}
</script>
<style scoped>

</style>
