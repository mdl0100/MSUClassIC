<script>
import { GridLayout, GridItem } from 'grid-layout-plus';
import { defineComponent } from 'vue';


export default defineComponent({
    components: {
        GridLayout,
        GridItem
    }
})

</script>

<script setup>
import { reactive } from 'vue'

const layout = reactive([
    { x: 0, y: 0, w: 2, h: 1, i: '', static: true },
    { x: 2, y: 0, w: 2, h: 1, i: 'Prof 1', static: true },
    { x: 4, y: 0, w: 2, h: 1, i: 'Prof 2', static: true },
    { x: 6, y: 0, w: 2, h: 1, i: 'Prof 3', static: true },
    { x: 8, y: 0, w: 2, h: 1, i: 'Prof 4', static: true },
    { x: 10, y: 0, w: 2, h: 1, i: 'Prof 5', static: true },
    { x: 12, y: 0, w: 2, h: 1, i: 'Prof 6', static: true },
    { x: 0, y: 1, w: 2, h: 1, i: '8am', static: true },
    { x: 0, y: 2, w: 2, h: 1, i: '9am', static: true },
    { x: 0, y: 3, w: 2, h: 1, i: '10am', static: true },
    { x: 0, y: 4, w: 2, h: 1, i: '11am', static: true },
    { x: 0, y: 5, w: 2, h: 1, i: '12am', static: true },
    { x: 0, y: 6, w: 2, h: 1, i: '1pm', static: true },
    { x: 0, y: 7, w: 2, h: 1, i: '2pm', static: true },
    { x: 0, y: 8, w: 2, h: 1, i: '3pm', static: true },
    { x: 0, y: 9, w: 2, h: 1, i: '4pm', static: true },
    { x: 0, y: 10, w: 2, h: 1, i: '5pm', static: true },
] )
</script>

<template>
  <GridLayout 
    v-model:layout="layout" 
    :row-height="30"
    :col-num="14"
    vertical-compact=false
    is-resizable=false>
    <template #item="{ item }">
      <span class="text">{{ `${item.i}` }}</span>
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
</style>