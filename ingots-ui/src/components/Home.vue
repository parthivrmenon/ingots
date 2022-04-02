<template>
<v-container>
    <v-row>
        <v-col cols="4">
            <AddBook />

        </v-col>
        <v-col cols="8">
            <v-card>
                <v-card-title> Check Out </v-card-title>

                <v-card-subtitle>
                    View your books here.
                </v-card-subtitle>
                <v-card-text>
                    <v-text-field
                      v-model="search"
                      append-icon="mdi-magnify"
                      label="Search"
                      single-line
                      hide-details
                    ></v-text-field>
                </v-card-text>
                <v-data-table :headers="headers" :items="books" :search="search">
                <template v-slot:item="row">
                    <tr>
                        <td>{{row.item.id}}</td>
                        <td>{{row.item.title}}</td>
                        <td>{{row.item.author}}</td>
                        <td>{{row.item.category}}</td>
                        <td>
                            <v-btn  small color=primary class="mx-1"  @click="downloadBook(row.item.title)">
                                <v-icon>mdi-download</v-icon>
                            </v-btn>
                            <v-btn  small color=error class="mx-1"  @click="deleteBook(row.item.title)">
                                <v-icon>mdi-delete</v-icon>
                            </v-btn>

                        </td>

                    </tr>
                </template>
                </v-data-table>
            </v-card>
        </v-col>
    </v-row>
</v-container>

</template>


<script>
import AddBook from './AddBook';
import axios from 'axios';

  export default {
    components: {
        AddBook,
    },
    data () {
      return {  
        search: '',
        headers: [
            { text: 'Id',align: 'start',filterable: false, value:'id'},
            { text: 'Title', align: 'start', filterable: true,value:'title'},
            { text: 'Author', align: 'start', filterable: true,value:'author'},
            { text: 'Category', align: 'start', filterable: true,value:'category'},
            { text: 'Actions', align: 'center', filterable: true},



        ],
        books: []
      }
    },

    methods: {
        async getBooks(){
            const server_url = "http://localhost:5000"
            await axios.get(server_url + "/")
            .then(response => (this.books = response.data['books']))
            .catch((error) => {
                console.log(error)
            })
        },

        async downloadBook(title){
            let config = {
            responseType: 'blob',
            timeout: 30000,
            }
            console.log(config)
            const server_url = "http://localhost:5000"
            await axios.get(server_url + "/uploads/" + title, config)
            .then(response => {
                console.log(response.data)
                const blob = new Blob([response.data],{ type: 'application/pdf' })
                const objectUrl = window.URL.createObjectURL(blob)
                window.open(objectUrl)

            })
            .catch((error) => {console.log(error)})
        },
        async deleteBook(title){
            const server_url = "http://localhost:5000"
            await axios.get(server_url + "/delete/" + title)
            .then(response => {console.log(response)})
            .catch(error => {console.log(error)})



        }
    },
    mounted () {
      this.getBooks();
    },
  }
</script>