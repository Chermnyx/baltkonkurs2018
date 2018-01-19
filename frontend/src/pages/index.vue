<template>
  <div class="container">
    <ul class="collapsible" data-collapsible="accordion">
      <li>
        <div class="collapsible-header active">
          <i class="material-icons">assignment_ind</i>Регистрация</div>
        <div class="collapsible-body">
          <register/>
        </div>
      </li>
      <li :class="{ 'force-disabled': !store.registerDone }">
        <div class="collapsible-header">
          <i class="material-icons">insert_photo</i>Проверка изображений</div>
        <div class="collapsible-body">
          <image-uploader/>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import $ from 'jquery'
import Register from '../components/Register.vue'
import ImageUploader from '../components/ImageUploader.vue'

export default {
  name: 'app',
  data: () => ({
    store: window.store
  }),
  components: {
    register: Register,
    'image-uploader': ImageUploader
  },
  mounted() {
    $('.collapsible').collapsible()
  }
}
</script>
