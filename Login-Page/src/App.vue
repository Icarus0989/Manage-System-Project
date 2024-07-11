<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <LoginView/>
  <link rel="stylesheet" href="https://classless.de/classless.css">

</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import LoginView from './components/LoginView.vue'
export default {
  name: 'App',
  components: {
    // HelloWorld,
    LoginView
  }
}
</script>