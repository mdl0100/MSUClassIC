// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getAuth, onAuthStateChanged } from 'firebase/auth'


// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDr-aqK8XWOtbmhsgYxxgtX795FMDfiiiI",
  authDomain: "msuclassic.firebaseapp.com",
  projectId: "msuclassic",
  storageBucket: "msuclassic.appspot.com",
  messagingSenderId: "158292161968",
  appId: "1:158292161968:web:7689c16b6d34ae4e825275",
  measurementId: "G-RV8536ZXZF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

onAuthStateChanged(auth, user => {
    if (user != null) {
        console.log('logged!');
    } else {
        console.log('No user');
    }
});