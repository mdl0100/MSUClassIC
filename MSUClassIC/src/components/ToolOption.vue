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
  </template>
  
<script>
  export default{
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
  }
</script>

<style scoped>
  label {
    font-size: 1.5rem;
  }
  
  select {
    font-size: 1.5rem;
    margin-left: 2rem;
  }

  .dropdown {
    /* Center items on page */
    display: flex;
    align-items: center;

}
</style>