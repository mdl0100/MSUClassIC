<template>
    <div class="dropdown">
      <label for="views">Views:</label>
      <select id="views" name="views">
        <option value="0">Select a view</option>
        <option value="1">Faculty vs Time</option>
        <option value="2">Faculty vs Course</option>
        <option value="3">Course vs Time</option>
        <option value="4">Course vs Location</option>
      </select>
    </div>
  </template>
  
<script>

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