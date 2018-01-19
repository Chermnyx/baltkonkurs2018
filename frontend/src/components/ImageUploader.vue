<template>
  <div class="container">
    <div class="row">
      <h3 class="center">Загрузите фотографии</h3>

    </div>
    <div class="row">
      <div class="col s8 push-s2 file-field input-field">
        <div class="btn green darken-4" style="width: 100%">
          <icon>insert_photo</icon>
        </div>
        <input ref="imagesInput" type="file" multiple accept="image/*" @change="onFilesInputChange" />
      </div>
    </div>

    <div class="row">
      <div class="col s12 m6 l4" v-for="(image, index) in images" :key="index">
        <div class="card">
          <div class="card-image">
            <img :src="image.image">
          </div>
          <div class="card-stacked">
            <div class="card-content flow-text" v-if="image.diag">
              <p class="center red-text text-accent-4" v-if="image.diag > 0.8">Высокий риск</p>
              <p class="center yellow-text text-darken-4" v-else-if="image.diag > 0.5">Средний риск</p>
              <p class="center" v-else>Низкий риск</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api'

export default {
  // TODO: flexbox cards
  data: () => ({
    images: []
  }),
  methods: {
    onFilesInputChange(e) {
      this.images = []
      for (let [index, file] of Array.entries(e.target.files)) {
        const reader = new FileReader()
        reader.onload = () => {
          this.images[index].image = reader.result
        }
        this.images.push({ image: null, diag: null, file: file })
        reader.readAsDataURL(file)
      }

      const files = this.images.map(x => x.file)
      api.uploadImages(files).then(data => {
        for (let [index, val] of Object.entries(data)) {
          this.images[parseInt(index)].diag = val
        }
      })
    }
  }
}
</script>

<style scoped>
.card .card-content {
  padding: 0em 0em;
  padding-bottom: 1em;
  border-radius: 0 0 2px 2px;
  font-size: 1.2em;
}

.card {
  margin: 0;
  box-shadow: none;
}
</style>
