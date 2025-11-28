<script setup>
import { ref } from 'vue'
import axios from 'axios'

const form = ref({ nombre: '', apellido: '', email: '' })
const mensaje = ref('')
const error = ref('')

const registrar = async () => {
  try {
    mensaje.value = ''
    error.value = ''
    // Conectamos directo al backend en el puerto 8000
    await axios.post('http://localhost:8000/api/participantes/registro/', form.value)
    mensaje.value = '¡Registro recibido! Revisa tu correo para verificar la cuenta.'
    form.value = { nombre: '', apellido: '', email: '' }
  } catch (e) {
    error.value = e.response?.data?.email ? 'El correo ya está registrado.' : 'Error en el servidor'
  }
}
</script>

<template>
  <div>
    <h2>Inscríbete y Gana</h2>
    <form @submit.prevent="registrar">
      <input v-model="form.nombre" placeholder="Nombre" required />
      <input v-model="form.apellido" placeholder="Apellido" required />
      <input v-model="form.email" type="email" placeholder="Correo Electrónico" required />
      <button type="submit">Registrarme</button>
    </form>
    <p v-if="mensaje" class="success">{{ mensaje }}</p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>