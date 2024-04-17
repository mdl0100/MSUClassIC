
<template>
  <div class="about">
    <h3>MSUClassIC helps you figure out  <br /> 
     your department's classes schedule</h3>
     <p>
        This was made as a project for Advanced Software Engineering class at MSU. <br />
        We had a lot of help making this project. Especially from the following sources:
        <ul>
          <li><a href="https://vuejs.org/guide/introduction.html">Vue.js JavaScript Framework</a></li>
          <li><a href="https://firebase.google.com/">Google Firebase Authenitcator</a></li>
          <li><a href="https://grid-layout-plus.netlify.app/">Grid Layout Plus</a></li>
        </ul>
      </p>
   
      <div>
      <h3>Team Members</h3>
        <p class="team">
          <ul>
            <li>Marcos Lopez</li>
            <li>Samuel Olatunde</li>
            <li>Athul Sajikumar</li> 
          </ul> 
        </p>
      </div>
    </div>

    
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex-box;
    justify-content: center;

    text-align: center;
    align-items: center;
    width: 100%;
  }
}

.about h3 {
  font-size: 2rem;
  margin-bottom: 2rem;
}

.about p {
  font-size: 1rem;
}

.about ul {
  list-style-type: none;
  padding: 0;
}

.about a {
  color: var(--color-text);
}

.about a:hover {
  background-color: var(--color-background);
}

.about .team {
  font-size: 1.5rem;
}

</style>
