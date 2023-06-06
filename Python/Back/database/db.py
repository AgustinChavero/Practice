// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBRlVyztgj4VLRAQoPlTIOFV5JKm28MFSo",
  authDomain: "testagustinchavero.firebaseapp.com",
  projectId: "testagustinchavero",
  storageBucket: "testagustinchavero.appspot.com",
  messagingSenderId: "482419348072",
  appId: "1:482419348072:web:4a82fea3dc59a8cebc21dd",
  measurementId: "G-NKT032F60P"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);