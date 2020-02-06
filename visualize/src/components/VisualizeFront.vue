<template>
  <div class="visualize">
    <button class="container" v-on:click="nextId">next</button>
    <button class="container" v-on:click="backId">back</button>
    <transition appear>
      <div v-show="show">
        <VisualizeBack :sentence="attention[currentId].sentence"
         :weight="attention[currentId].attention_weight" />
      </div>
    </transition>
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
      currentId: 0,
      attention: require("../assets/features.json"),
      show: true
    }
  },
  methods: {
    nextId: function () {
      if (this.currentId == this.attention.length - 1) {
        console.log(this.currentId)
        this.currentId = 0
      }else{
        console.log(this.currentId)
        this.currentId += 1
      }
    },
    backId: function () {
      if (this.currentId != 0){
        console.log(this.currentId)
        this.currentId -= 1
      }else{
        console.log(this.currentId)
        this.currentId = this.attention.length - 1
      }
    }
  }
}
</script>

<style scoped>

.container {
  font-family: "Yu Gothic", YuGothic, Verdana, 'Hiragino Kaku Gothic ProN','Hiragino Kaku Gothic Pro', 'ヒラギノ角ゴ Pro W3', 'メイリオ', Meiryo, sans-serif;
  text-align: left;
  cursor: pointer;
}
.container:hover{
  opacity: 0.6;
}
</style>
