<template>
    <form name="login-form" >
      <div class="mb-3">
        <label for="username">Username: </label>
        <input type="text" id="username" v-model="input.username" />
      </div>
    <div class="mb-3">
       <label for="password">Password: </label>
       <input type="password" id="password" v-model="input.password" />
    </div>
      <button class="btn btn-outline-dark" type="submit" v-on:click.prevent = "login()">
        Login
      </button>
    </form>
</template>

<script>
export default {
  name: 'LoginView',
  data(){
    return{
        input:{
            username: "",
            password: ""
        }
    }
  },
  methods:{
    login(){
      //make sure username OR password are not empty
      if(this.input.username != "" || this.input.password != ""){
        console.log("authenticated")
      }else{
        console.log("Username and Password can not be empty")
      }
    }
  },
}
</script>

<div class="mb-3">
    <label for="username">Username: </label>
    <input type="text" id="username" v-model="input.username" />
  </div>
  <div class="mb-3">
    <label for="password">Password: </label>
    <input type="password" id="password" v-model="input.password" />
  </div>
