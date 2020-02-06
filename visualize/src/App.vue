<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <div id="tabs">
      <input type="radio" value="1" id="tab1" v-model="isActive">
      <label for="tab1">タブ1</label>
      <input type="radio" value="2" id="tab2" v-model="isActive">
      <label for="tab2">タブ２</label>
    </div>
      <ul id="contents">
        <li v-if="isActive == '1'">
          <div class="scrollItem">
            <perfect-scrollbar>
              <VisualizeList/>
            </perfect-scrollbar>
          </div>
        </li>
        <li v-if="isActive == '2'">
          <VisualizeFront/>
        </li>
      </ul>
  </div>
</template>

<script>
import VisualizeFront from './components/VisualizeFront.vue'
import VisualizeList from './components/VisualizeList.vue'
import PerfectScrollbar from 'vue2-perfect-scrollbar'

export default {
  name: 'app',
  components: {
    VisualizeList,
    VisualizeFront,
    PerfectScrollbar
  },
  data() {
    return {
      isActive: '1'
    }
  }
}

</script>

<style src="vue2-perfect-scrollbar/dist/vue2-perfect-scrollbar.css"/>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
    font-size: 16px;
    font-family: Verdana, sans-serif;
}

ul {
  padding: 0;
  margin: 0;
}

li {
   list-style: none;
}

h1 {
  font-size : 16px;
  margin: 0;
}

p {
  margin: 0;
  font-size: 15px;
}

#tabs {
    overflow: hidden;
}

#tabs input {
  display: none;
}

#tabs label {
    display: inline-block;
    line-height: 40px;
    width: 120px;
    text-align: center;
    cursor: pointer;
    background: #eee;
    transition: 0.3s ease-in-out;
    border-radius: 10px 10px 0 0;
}

#tabs input:checked + label,
#tabs label:hover {
    background: #56B4BE;
    color: #fff;
}

#contents {
    width: 1400px;
    height: 600px;
    padding: 5px 10px;
    box-shadow: 1px 1px 1px 0 rgba(0,0,0,0.2);
    border: 1px solid #eee;
    border-top: 2px solid #56B4BE;
}

.scrollItem{
  position: relative;
  width: 1400px;
  height: 600px;
}
.scrollItem p{
  text-align: left;
}
.ps{
  position: absolute;
  overflow: hidden;
  width: 100%;
  height: 100%;
}
</style>
