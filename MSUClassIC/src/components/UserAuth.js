// UserAuth.js
import { auth } from '@/firebase.js';
import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged } from 'firebase/auth';

export default class UserAuth {
  constructor() {
    this.user = null;
    this.data = {
      email: '',
      password: ''
    };
    this.mode = 'login';
    this.router = null;
    this.fetchUserData = this.fetchUserData.bind(this);
    this.onAuthStateChanged = this.onAuthStateChanged.bind(this);
    onAuthStateChanged(auth, this.onAuthStateChanged);
  }

  async login(email, password) {
    await signInWithEmailAndPassword(auth, email, password).then((res) => {
      console.log(res);
    }).catch((error) => {
      console.log(error);
    });
    if (this.user) {
      this.fetchUserData();
      this.router.push('/site');
    }
  }

  async register(email, password) {
    await createUserWithEmailAndPassword(auth, email, password).then((res) => {
      console.log(res);
    }).catch((error) => {
      console.log(error);
    });
  }

  submit() {
    const { email, password } = this.data;
    if (this.mode === 'login') {
      this.login(email, password);
    } else {
      this.register(email, password);
    }
  }

  async signout() {
    await signOut(auth).then(() => {
      console.log('signed out');
    }).catch((error) => {
      console.log(error);
    });
    this.router.push('/');
  }

  //NOT DONE
  fetchUserData() {
    console.log('fetching user data');
    // Fetch user data from the database
    // This will be used to populate the site page
  }

  onAuthStateChanged(currentUser) {
    this.user = currentUser;
  }
}
