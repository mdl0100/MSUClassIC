<script setup>
import { reactive, ref, computed } from 'vue';
import { GridLayout, GridItem } from 'grid-layout-plus';
import { useStore } from 'vuex';

const store = useStore();




// Reactive state for grid layout and column number
// const example = reactive([
// { x: 2, y: 0, w: 2, h: 1, i: 'Prof 1', static: true },
// { x: 4, y: 0, w: 2, h: 1, i: 'Prof 2', static: true },
// { x: 6, y: 0, w: 2, h: 1, i: 'Prof 3', static: true },
// { x: 8, y: 0, w: 2, h: 1, i: 'Prof 4', static: true },
// { x: 10, y: 0, w: 2, h: 1, i: 'Prof 5', static: true },
// { x: 12, y: 0, w: 2, h: 1, i: 'Prof 6', static: true },
// { x: 0, y: 1, w: 2, h: 2, i: '8am', static: true },
// { x: 0, y: 3, w: 2, h: 2, i: '9am', static: true },
// { x: 0, y: 5, w: 2, h: 2, i: '10am', static: true },
// { x: 0, y: 7, w: 2, h: 2, i: '11am', static: true },
// { x: 0, y: 9, w: 2, h: 2, i: '12am', static: true },
// { x: 0, y: 11, w: 2, h: 2, i: '1pm', static: true },
// { x: 0, y: 13, w: 2, h: 2, i: '2pm', static: true },
// { x: 0, y: 15, w: 2, h: 2, i: '3pm', static: true },
// { x: 0, y: 17, w: 2, h: 2, i: '4pm', static: true },
// { x: 0, y: 19, w: 2, h: 2, i: '5pm', static: true },
// { x: 6, y: 8, w: 2, h: 2, i: 'Class1', static: false },
// ] )
// const real = reactive([{'x': 1, 'y': 0, 'w': 1, 'h': 1, 'i': 'Colmenares - Diaz', 'static': true},
//  {'x': 2, 'y': 0, 'w': 1, 'h': 1, 'i': 'Griffin', 'static': true},
//  {'x': 3, 'y': 0, 'w': 1, 'h': 1, 'i': 'Hood', 'static': true},
//  {'x': 4, 'y': 0, 'w': 1, 'h': 1, 'i': 'Johnson', 'static': true},
//  {'x': 5, 'y': 0, 'w': 1, 'h': 1, 'i': 'Morgan', 'static': true},
//  {'x': 6, 'y': 0, 'w': 1, 'h': 1, 'i': 'Passos', 'static': true},
//  {'x': 7, 'y': 0, 'w': 1, 'h': 1, 'i': 'Roychoudhuri', 'static': true},
//  {'x': 8, 'y': 0, 'w': 1, 'h': 1, 'i': 'Smith', 'static': true},
//  {'x': 9, 'y': 0, 'w': 1, 'h': 1, 'i': 'Stringfellow', 'static': true},
//  {'x': 0, 'y': 1, 'w': 1, 'h': 1, 'i': 'CMPS 1023', 'static': true},
//  {'x': 4, 'y': 1, 'w': 1, 'h': 1, 'i': 'TR 11:00 BO 103.0', 'static': true},
//  {'x': 0, 'y': 2, 'w': 1, 'h': 1, 'i': 'CMPS 1044', 'static': true},
//  {'x': 5, 'y': 2, 'w': 1, 'h': 1, 'i': 'MWF 9:00 BO 207.0', 'static': true},
//  {'x': 7, 'y': 2, 'w': 1, 'h': 1, 'i': 'TR 9:30 BO 109.0', 'static': true},
//  {'x': 0, 'y': 3, 'w': 1, 'h': 1, 'i': 'CMPS 1063', 'static': true},
//  {'x': 1, 'y': 3, 'w': 1, 'h': 1, 'i': 'TR 9:30 BO 103.0', 'static': true},
//  {'x': 9, 'y': 3, 'w': 1, 'h': 1, 'i': 'MWF 9:00 BO 320.0', 'static': true},
//  {'x': 0, 'y': 4, 'w': 1, 'h': 1, 'i': 'CMPS 2084', 'static': true},
//  {'x': 6, 'y': 4, 'w': 1, 'h': 1, 'i': 'TR 12:30 BO 320.0', 'static': true},
//  {'x': 0, 'y': 5, 'w': 1, 'h': 1, 'i': 'CMPS 2143', 'static': true},
//  {'x': 9, 'y': 5, 'w': 1, 'h': 1, 'i': 'TR 11:00 BO 320.0', 'static': true},
//  {'x': 0, 'y': 6, 'w': 1, 'h': 1, 'i': 'CMPS 2433', 'static': true},
//  {'x': 9, 'y': 6, 'w': 1, 'h': 1, 'i': 'MWF 11:00 BO 209.0', 'static': true},
//  {'x': 0, 'y': 7, 'w': 1, 'h': 1, 'i': 'CMPS 3013', 'static': true},
//  {'x': 1, 'y': 7, 'w': 1, 'h': 1, 'i': 'MWF 9:00 BO 213.0', 'static': true},
//  {'x': 0, 'y': 8, 'w': 1, 'h': 1, 'i': 'CMPS 3533', 'static': true},
//  {'x': 3, 'y': 8, 'w': 1, 'h': 1, 'i': 'MWF 9:00 BO 109.0', 'static': true},
//  {'x': 0, 'y': 9, 'w': 1, 'h': 1, 'i': 'CMPS 4103', 'static': true},
//  {'x': 6, 'y': 9, 'w': 1, 'h': 1, 'i': 'TR 8:00 BO 320.0', 'static': true},
//  {'x': 0, 'y': 10, 'w': 1, 'h': 1, 'i': 'CMPS 4123', 'static': true},
//  {'x': 7, 'y': 10, 'w': 1, 'h': 1, 'i': 'TR 14:00 BO 109.0', 'static': true},
//  {'x': 0, 'y': 11, 'w': 1, 'h': 1, 'i': 'CMPS 4143', 'static': true},
//  {'x': 2, 'y': 11, 'w': 1, 'h': 1, 'i': 'TR 9:30 BO 320.0', 'static': true},
//  {'x': 0, 'y': 12, 'w': 1, 'h': 1, 'i': 'CMPS 4453', 'static': true},
//  {'x': 6, 'y': 12, 'w': 1, 'h': 1, 'i': 'MWF 8:00 BO 320.0', 'static': true},
//  {'x': 0, 'y': 13, 'w': 1, 'h': 1, 'i': 'CMPS 4883', 'static': true},
//  {'x': 2, 'y': 13, 'w': 1, 'h': 1, 'i': 'MW 14:00 BO 103.0', 'static': true},
//  {'x': 0, 'y': 14, 'w': 1, 'h': 1, 'i': 'CMPS 5113', 'static': true},
//  {'x': 1, 'y': 14, 'w': 1, 'h': 1, 'i': 'MW 15:30 BO 209.0', 'static': true},
//  {'x': 4, 'y': 14, 'w': 1, 'h': 1, 'i': 'MW 15:30 BO 320.0', 'static': true},
//  {'x': 0, 'y': 15, 'w': 1, 'h': 1, 'i': 'CMPS 5133', 'static': true},
//  {'x': 7, 'y': 15, 'w': 1, 'h': 1, 'i': 'MW 14:00 BO 320.0', 'static': true},
//  {'x': 0, 'y': 16, 'w': 1, 'h': 1, 'i': 'CMPS 5143', 'static': true},
//  {'x': 2, 'y': 16, 'w': 1, 'h': 1, 'i': 'TR 14:00 BO 320.0', 'static': true},
//  {'x': 0, 'y': 17, 'w': 1, 'h': 1, 'i': 'CMPS 5363', 'static': true},
//  {'x': 8, 'y': 17, 'w': 1, 'h': 1, 'i': 'TR 15:30 BO 320.0', 'static': true},
//  {'x': 0, 'y': 18, 'w': 1, 'h': 1, 'i': 'CMPS 5443', 'static': true},
//  {'x': 4, 'y': 18, 'w': 1, 'h': 1, 'i': 'W 11:00 BO 320.0', 'static': true},
//  {'x': 0, 'y': 19, 'w': 1, 'h': 1, 'i': 'MATH 233', 'static': true},
//  {'x': 3, 'y': 19, 'w': 1, 'h': 1, 'i': 'TR 8:00 BO 101.0', 'static': true},
//  {'x': 0, 'y': 20, 'w': 1, 'h': 1, 'i': 'MATH 1233', 'static': true},
//  {'x': 3, 'y': 20, 'w': 1, 'h': 1, 'i': 'MWF 8:00 BO 101.0', 'static': true},
//  {'x': 0, 'y': 21, 'w': 1, 'h': 1, 'i': 'MATH 1634', 'static': true},
//  {'x': 3, 'y': 21, 'w': 1, 'h': 1, 'i': 'MF 11:00 BO 109.0', 'static': true},
//  {'x': 0, 'y': 22, 'w': 1, 'h': 1, 'i': 'MATH 3533', 'static': true},
// ])

const layout = computed(() => {
  switch (selected.value) {
    case '1': return reactive(store.getters.get_location_time_MWF);
    case '2': return reactive(store.getters.get_faculty_course);
    case '3': return reactive(store.getters.get_faculty_MWF);
    case '4': return reactive(store.getters.get_faculty_TR);
    case '5': return reactive(store.getters.get_location_time_TR);
    default: return reactive(store.getters.getExample);
  }
});

function dispLayout() {
  console.log(layout.value);
  switch (selected.value) {
    case '1':
      store.commit('updateExample', layout.value);
      break;
    case '2':
      store.commit('updateFacultyCourse', layout.value);
      break;
    case '3':
      store.commit('updateFacultyMWF', layout.value);
      break;
    case '4':
      store.commit('updateFacultyTR', layout.value);
      break;
    case '5':
      store.commit('updateFacultyTR', layout.value);
      break;
    default:
      store.commit('updateExample', layout.value);
      break; 
  }
}

const backgroundSize = computed(() => {
  switch (selected.value) {
    case '1': return 'calc(calc(100% - 4px) / 10) 60px';
    case '2': return 'calc(calc(100% - 4px) / 10) 60px';
    case '3': return 'calc(calc(100% - 4px) / 10) 60px';
    case '4': return 'calc(calc(100% - 4px) / 10) 60px';
    case '5': return 'calc(calc(100% - 4px) / 10) 60px';
    default: return 'calc(calc(100% - 4px) /7) 60px'; // Default or initial value
  }
});


// Index used for item names
let index = ref(0);

// Reactive state for selected dropdown value
const selected = ref('');

// Computed property for view description
const viewDescription = computed(() => {
  switch (selected.value) {
    case '1': return 1;
    case '2': return 2;
    case '3': return 3;
    case '4': return 4;
    default: return 0;
  }
});

// Methods
const colNum = computed(() => {
  let maxCol = 0;
  layout.value.forEach(item => {
    if (item.y === 0) { // Consider only items in the first row
      maxCol = Math.max(maxCol, item.x + item.w);
    }
  });
  return maxCol ; // Twice the number of entries
});

// Calculate the number of rows required
const rowNum = computed(() => {
  let maxRow = 0;
  layout.value.forEach(item => {
    if (item.x === 0) { // Consider only items in the first column
      maxRow = Math.max(maxRow, item.y + item.h);
    }
  });
  return maxRow; // Twice the number of entries
});

function addItem() {
  const itemName = window.prompt('Enter the name of the Course', `Item ${index.value++}`);
  const itemLocation = window.prompt('Enter the location of the Course', '');
  layout.value.push({
    x: (layout.value.length) % (colNum.value || 12),
    y: 3, // places it at the bottom
    w: 2,
    h: 2,
    i: `${itemName}\n${itemLocation}`,
    static: false,
    moved: false
  });
}

function removeItem(itemName) {
  const index = layout.value.findIndex(item => item.i === itemName);
  if (index !== -1) {
    layout.value.splice(index, 1);
  }
}

function anchor(itemName) {
  const item = layout.value.find(item => item.i === itemName);
  if (item) {
    item.static = !item.static;
  }
}


function getEmail() {
  console.log(store.getters.userEmail);
}

function getDepartment() {
  console.log(store.getters.userDepartment);
}

</script>

<template>
  <div class="dropdown">
    <label for="views">Views:</label>
    <select id="views" name="views" v-model="selected">
      <option disabled value="">Please select one</option>
      <option value="1">Course vs Location (1st Floor, MWF)</option>
      <option value="5">Course vs Location (1st Floor, TR)</option>
      <option value="2">Faculty vs Course</option>
      <option value="3">Faculty vs Time (MWF)</option>
      <option value="4">Faculty vs Time (TR)</option>
    </select>
  </div>
  <h3>This is the View: {{ viewDescription }}</h3>
  <button @click="addItem">Add Item</button>
  <button @click="dispLayout">Save</button>
  <button @click="getEmail">User Email</button>
  <button @click="getDepartment">User Dept</button>
  <div class="vgl-layout" :style="{ '--background-size': backgroundSize }">
  <GridLayout 
    v-model:layout="layout" 
    :row-height="50"
    :col-num="colNum"
    :vertical-compact="false"
    prevent-collision>
    <template #item="{ item }">
        <span class="text">{{ item.i }}</span>
        <span class="remove" @click="removeItem(item.i)">-</span>
        <span v-if="item.is_dept" class="anchor" @click="anchor(item.i)">⚓</span>
    </template>
  </GridLayout>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100%;
}


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
  width: 75%;
  height: 100%;
  margin: auto;
  font-size: calc(1.5vmin);
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
  background-size: var(--background-size);
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
    border-radius: 5px;
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