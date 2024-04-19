<template>
  <div >
    <form @submit.prevent="handleSubmit">
      <input v-model="email" type="email" placeholder="Enter your email" />
      <input v-model="password" type="password" placeholder="Enter your password" />
      <input v-model="department" type="text" placeholder="Enter your department" v-if="isRegistering" />

      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>

      <button type="submit">{{ isRegistering ? 'Register' : 'Login' }}</button>
      <button type="button" @click="toggleMode">{{ isRegistering ? 'Switch to Login' : 'Switch to Register' }}</button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useStore } from 'vuex';
import { auth } from '@/firebase.js'; // adjust this path to where your Firebase initialization file is located
import { signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut, onAuthStateChanged } from 'firebase/auth';
import router from '@/router';

export default {
  setup() {
    const store = useStore();
    const email = ref('');
    const password = ref('');
    const department = ref('');
    const errorMessage = ref('');
    const isRegistering = ref(false);
    const user = ref(null); // Ref to hold the user object

    onMounted(() => {
      onAuthStateChanged(auth, (currentUser) => {
      if (currentUser) {
        // User is signed in.
        store.commit('setUser', {
          email: currentUser.email,
          uid: currentUser.uid
        });
      } else {
        // User is signed out.
        store.commit('clearUser');
      }
      });
    });

    const login = async () => {
      try {
        await signInWithEmailAndPassword(auth, email.value, password.value);
        store.commit('setUser', {
          email: email.value,
          uid: auth.currentUser.uid
        });
        console.log('Logged in successfully');
         // Navigate to Scheduler after login
        // Check if the router is defined and if the navigation actually happens
        console.log('Attempting to navigate to /site');
        router.push('/site').catch(err => {
      console.error('Router push failed:', err);
    });
      } catch (error) {
        errorMessage.value = 'Failed to login. Check your credentials.';
      }
      
    };

    const register = async () => {
      try {
        const userCredential = await createUserWithEmailAndPassword(auth, email.value, password.value);
        store.commit('setUser', {
          email: userCredential.user.email,
          uid: userCredential.user.uid,
          department: department.value
        });
        router.push('/site');  // Navigate to home after registration
      } catch (error) {
        errorMessage.value = 'Failed to register.';
      }
    };

    const handleSignOut = async () => {
      try {
        await signOut(auth);
        errorMessage.value = 'You have been signed out successfully.';
      } catch (error) {
        errorMessage.value = 'Error signing out. Please try again.';
      }
    };

    const handleSubmit = () => {
      if (isRegistering.value) {
        register();
      } else {
        login();
      }
    };

    const toggleMode = () => {
      isRegistering.value = !isRegistering.value;
      errorMessage.value = ''; // Clear error message when toggling
    };

    return { email, password, department, errorMessage, isRegistering, handleSubmit, toggleMode, user, handleSignOut };
  },
};
</script>




<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.form {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 300px;  /* Reducing max width for a more compact form */
  gap: 20px;  /* Increased gap for more space between fields */
  padding: 20px;
  background: #fff;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

input {
  width: 100%;  /* Full width relative to the form container, but form container width reduced */
  padding: 10px;  /* Slightly reduced padding */
  border: 1px solid #ddd;
  border-radius: 0;  /* No rounded corners for input fields */
  margin-bottom: 10px;  /* Adds margin below each input for additional spacing */
}

button {
  padding: 12px 20px;  /* Adjusted padding for better proportion */
  margin: 10px 10px;  /* Added margin above and below the button */ 
  border: none;
  background-color: #02bd7e;  /* Custom green color for buttons */
  color: white;
  border-radius: 8px;  /* Rounded corners for buttons */
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: darken(#02bd7e, 10%);  /* Slightly darker on hover */
}

.error {
  color: red;
  text-align: center;
  margin-top: 10px;  
}
</style>

