<template>
  <div class="container">
    <h1>🏆 Sorteo San Valentín 💘</h1>
    <router-view></router-view>
  </div>
</template>

<style>
.container {
  max-width: 600px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 2rem;
}
input {
  display: block;
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  box-sizing: border-box; 
}
button {
  background-color: #ff4757;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  width: 100%;
}
button:hover {
  background-color: #ff6b81;
}
.error { color: red; }
.success { color: green; }
</style>