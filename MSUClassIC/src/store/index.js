// src/store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    user: {
      email: null,
      uid: null,
      isAuthenticated: false,
      department: null,
    },
  },
  mutations: {
    setUser(state, userData) {
        state.user.email = userData.email;
        state.user.uid = userData.uid;
        state.user.isAuthenticated = true;  // Set isAuthenticated to true when user is set
      },
    clearUser(state) {
        state.user = { email: null, uid: null, isAuthenticated: false };
      },
  },
  getters: {
    isUserAuthenticated: (state) => state.user.isAuthenticated,
    userId: (state) => state.user.uid,
  },
});
