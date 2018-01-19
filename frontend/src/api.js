import axios from 'axios'

export default {
  async uploadImages (imageFiles) {
    const data = new FormData()
    for (let i = 0; i < imageFiles.length; ++i) {
      data.append(i.toString(), imageFiles[i])
    }

    console.log('Predicting images...')
    const ret = await axios.post('/api/processImages', data)
    console.log(ret)

    return ret.data
  }
}
