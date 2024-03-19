<script>
import { GridLayout, GridItem } from 'grid-layout-plus';
import { defineComponent } from 'vue';


export default defineComponent({
    components: {
        GridLayout,
        GridItem
    },
    data(){
      return{
        view: ''
      }
    },
    methods: {
      selected(){
        this.view = this.selected
        console.log(this.view)
      }
    }
  })
</script>

<script setup>
import { reactive } from 'vue'
import { ref } from 'vue'

let index = 5
let display = false

const draggable = ref(true)
const resizable = ref(true)
const colNum = ref(12)


const layout = reactive([

    { x: 2, y: 0, w: 2, h: 1, i: 'Prof 1', static: true },
    { x: 4, y: 0, w: 2, h: 1, i: 'Prof 2', static: true },
    { x: 6, y: 0, w: 2, h: 1, i: 'Prof 3', static: true },
    { x: 8, y: 0, w: 2, h: 1, i: 'Prof 4', static: true },
    { x: 10, y: 0, w: 2, h: 1, i: 'Prof 5', static: true },
    { x: 12, y: 0, w: 2, h: 1, i: 'Prof 6', static: true },
    { x: 0, y: 1, w: 2, h: 2, i: '8am', static: true },
    { x: 0, y: 3, w: 2, h: 2, i: '9am', static: true },
    { x: 0, y: 5, w: 2, h: 2, i: '10am', static: true },
    { x: 0, y: 7, w: 2, h: 2, i: '11am', static: true },
    { x: 0, y: 9, w: 2, h: 2, i: '12am', static: true },
    { x: 0, y: 11, w: 2, h: 2, i: '1pm', static: true },
    { x: 0, y: 13, w: 2, h: 2, i: '2pm', static: true },
    { x: 0, y: 15, w: 2, h: 2, i: '3pm', static: true },
    { x: 0, y: 17, w: 2, h: 2, i: '4pm', static: true },
    { x: 0, y: 19, w: 2, h: 2, i: '5pm', static: true },
    { x: 6, y: 8, w: 2, h: 2, i: 'Class1', static: false },
] )

function addItem(){

  layout.push({
    x: (layout.length ) % (colNum.value || 12),
    y: (3), // puts it at the bottom
    w: 2,
    h: 2,
    i: `${window.prompt('Enter the name of the Course', `Item ${index++}`)}\n${window.prompt('Enter the location of the Course', ``)}` ,
    static: false,
    moved: false
  })
}

function removeItem(id){
  const index = layout.findIndex(item => item.i === id)
  if (index > -1) {
    layout.splice(index, 1)
  }
}

function anchor(id){
  const index = layout.findIndex(item => item.i === id)
  if (index > -1) {
    layout[index].static = !layout[index].static
  }
}

function dispLayout(){
  display = !display
  console.log(JSON.stringify(layout))
}
</script>

<template>
      <div class="dropdown">
      <label for="views">Views:</label>
      <select id="views" name="views" v-model="selected">
        <option disabled value="">Please select one</option>
        <option value="1">Faculty vs Time</option>
        <option value="2">Faculty vs Course</option>
        <option value="3">Course vs Time</option>
        <option value="4">Course vs Location</option>
      </select>
    </div>
  <button type="button" @click="addItem" >Add Item</button>
  <button type="button" @click="dispLayout" >Save</button>


  <h3 >This is the View: </h3>
  <!-- <p v-if="display"> This is the layout: {{ layout }}</p> -->
  <GridLayout 
    v-model:layout="layout" 
    :row-height="30"
    :col-num="14"
    :vertical-compact=false
    prevent-collision>
    <template #item="{ item }">
      <span class="text">{{ `${item.i}` }}</span>
      <span class="remove" @click="removeItem(item.i)">-</span>
      <span class="anchor" @click="anchor(item.i)">⚓</span>
    </template>
  </GridLayout>
</template>

<style scoped>

.vgl-layout {
  background-color: #eee;
  border-radius: 5px;
  ;
}

:deep(.vgl-item:not(.vgl-item--placeholder)) {
  background-color: #02bd7e;
  border: 1px solid black;
  border-radius: 5px;
  color: white;
}

:deep(.vgl-item--resizing) {
  opacity: 90%;
}

:deep(.vgl-item--static) {
  background-color: #cce;
}

.text {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  margin: auto;
  font-size: calc(2vmin);
  text-align: center;
}

.vgl-layout::before {
  display: block;
  position: absolute;
  width: calc(100% - 5px);
  height: calc(100% - 5px);
  margin: 5px;
  content: '';
  background-image:
    linear-gradient(to right,black 1px,transparent 1px),
    linear-gradient(to bottom, black 1px, transparent 1px);
  background-repeat: repeat;
  background-size: calc(calc(100% - 5px) / 7) 40px;
}

button {
  margin: 1rem;
}

.remove {
  position: absolute;
  bottom: 2px;
  left: 6px;
  cursor: pointer;
}

.anchor {
  position: absolute;
  bottom: 4px;
  right: 6px;
  cursor: pointer;
  font-size: xx-small;
}

label {
    font-size: 1.5rem;
  }
  
select {
  font-size: 1.5rem;
  margin-left: 2rem;
}

.dropdown {
  /* Center items on page */
  display: block;
  align-items: center;

}
</style>