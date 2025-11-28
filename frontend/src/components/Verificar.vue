<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const password = ref('')
const mensaje = ref('')
const error = ref('')
const verificado = ref(false)

const confirmar = async () => {
  try {
    await axios.post('http://localhost:8000/api/participantes/verificar/', {
      token: route.params.token,
      password: password.value
    })
    mensaje.value = '¡Cuenta activada exitosamente! Ya estás participando.'
    verificado.value = true
  } catch (e) {
    error.value = 'Error al verificar. El token puede ser inválido o ya usado.'
  }
}
</script>

<template>
  <div>
    <h2>Verificación de Cuenta</h2>
    <div v-if="!verificado">
      <p>Crea tu contraseña para finalizar:</p>
      <form @submit.prevent="confirmar">
        <input v-model="password" type="password" placeholder="Nueva Contraseña" minlength="6" required />
        <button type="submit">Activar Cuenta</button>
      </form>
    </div>
    <p v-if="mensaje" class="success">{{ mensaje }}</p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>