<template>
    <v-card>
        <v-card-title>Check-in</v-card-title>
        <v-card-subtitle>Add a new book by filling out the form.</v-card-subtitle>
        <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation class="pa-2">
            <v-text-field 
             v-model="title" 
             :counter="45"
             :rules="title_rules" 
             label="Title" 
             required
             >
            </v-text-field>
            <v-text-field
                v-model="author"
                :counter="45"
                :rules="author_rules"
                label="Author"
                required
            >
            </v-text-field>
            <v-select
              v-model="category"
              :items="items"
              :rules="[v => !!v || 'Category is required']"
              label="Category"
              required
            ></v-select>
            <v-file-input
                chips
                label="Upload File"
                v-model="uploaded_file"
            ></v-file-input>

        </v-form>
        </v-card-text>
        <v-card-actions>
        <v-btn
          :disabled="!valid"
          color="success"
          class="mr-4"
          @click="addBook()"
        >
          Add
        </v-btn>
        </v-card-actions>

    </v-card>
</template>

<script>
import axios from 'axios';
  export default {
    data: () => ({
      uploaded_file:null,
      valid: true,
      title: '',
      title_rules: [
        v => !!v || 'Title is required',
        v => (v && v.length <= 45) || 'Name must be less than 45 characters',
      ],
      author: '',
      author_rules: [
        v => !!v || 'An Author is required',
        v => (v && v.length <= 45) || 'Author must be less than 45 characters',

        // v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      category: null,
      items: [
        'Fiction',
        'Non-Fiction',
      ],
    }),

    methods: {
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    async addBook(){
        const body = {
            "title":this.title,
            "author":this.author,
            "category":this.category,
        }
        const formData = new FormData()
        formData.append('uploaded_file', this.uploaded_file)
        formData.append('data', JSON.stringify(body))
        console.log(formData)
        const server_url = "http://localhost:5000"

        await axios.post(server_url + "/",formData)
            .then(response => { console.log(response)})
            .catch((error) => {
                console.log(error)
            })
        },
    },
  }
</script>