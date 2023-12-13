import React, { useState, useEffect, SafeAreaView} from 'react'
import { useRoute } from "@react-navigation/native"
import {
  StyleSheet,
  Text,
  TextInput,
  View,
  Image,
  Alert,
  FlatList,
  Button,
} from 'react-native'
import axios from 'axios';
import {API_ENDPOINT} from '@env'


export default function Store ({ navigation }) {
  const [id, setId] = React.useState('');
  const [name, setName] = React.useState('');
  const [description, setDescription] = React.useState('');
  const [price, setPrice] = React.useState('');
  const [image_url, setImage_url] = React.useState('');
  const [category, setCategory] = React.useState('');
  const [stock, setStock] = React.useState('');
  const data = {
    id,
    name,
    description,
    price,
    image_url,
    category,
    stock,
  };

  const [products, setProducts] = useState()
  const [order, setOrder] = useState()
  const [user, setUser] = useState()
  const [orderPdtList, setOrderPdtList] = useState()
  const route = useRoute()
  const idvalue = route.params?.id
  const orderUrl = API_ENDPOINT + "/api/orders/" + idvalue + "/"
  const productUrl = API_ENDPOINT + "/api/products/"
  const userUrl = API_ENDPOINT + "/api/users/"
    useEffect( ()=>{
      const getOrderList= async()=>{
        axios.get(orderUrl)  
        .then(res=>setOrder([res.data]))
        .catch(error=>console.log(error)); 
        }
        const getOrderPdtList= async()=>{
          axios.get(productUrl)  
          .then(res=>setOrderPdtList([res.data.products]))
          .catch(error=>console.log(error)); 
          }
      const getPdtList= async()=>{
        axios.get(productUrl)  
        .then(res=>setProducts([res.data]))
        .catch(error=>console.log(error)); 
        }
      const getUserList= async()=>{
        axios.get(userUrl)  
        .then(res=>setUser([res.data]))
        .catch(error=>console.log(error)); 
        }
        getUserList();
        getPdtList();
        getOrderList();
        getOrderPdtList();

        // const result = order
        //   .map(item => ({
        //     ...item,
        //     children: item.products
        //       .filter(child => child.value.includes(value.toLowerCase()))
        //   }))
        //   .filter(item => item.products.length > 0)


    },[]);


    
    //const [products, setProducts] = useState(data)
    //<Text style={styles.title}>{item.name}</Text>
    //<Text style={styles.price}>${item.price}</Text>
    return (
      <View style={styles.container}>
        <FlatList
          style={styles.list}
          contentContainerStyle={styles.listContainer}
          data={order}
          horizontal={false}
          numColumns={2}
          keyExtractor={item => {
            return item.id
          }}
          ItemSeparatorComponent={() => {
            return <View style={styles.separator} />
          }}


          renderItem={post => {
            const item = post.item
            return (
              <View style={styles.card}>
                <View style={styles.cardHeader}>
                  <View>
                    <Text style={{fontSize: 16, fontWeight: 'bold', textAlign: 'left'}}>Order ID: {"\n"}{item.id}{"\n"}</Text>
                    <Text style={{fontSize: 16, fontWeight: 'bold'}}>Customer: {"\n"}{item.customer}{"\n"}</Text>
                    <Text style={{fontSize: 16, fontWeight: 'bold' , color: 'green'}}>Order Total: {"\n"}{item.total_amount}{"\n"}</Text>
                    <Text style={{fontSize: 16, fontWeight: 'bold' , color: 'purple'}}>Order Status: {"\n"}{item.status}{"\n"}</Text>
                    <Text style={{fontSize: 16, fontWeight: 'bold' , color: 'purple'}}>Delivery Status: {"\n"}{item.delivery_status}{"\n"}</Text>
                    <Text style={{fontSize: 16, fontWeight: 'bold'}}>Order Detail:{"\n"}</Text>

                    {/* {item.map((products, index) => {
                      return (
                        <div key={index}>
                          <h2>name: {products.product_id}</h2>
                          

                          <hr />
                        </div>
                      );
                    })} */}
                  </View>
                </View>
                {/* <Image style={styles.cardImage} source={ item.image_url ? { uri: item.image_url } : { uri:'https://bootdey.com/image/400x200/40E0D0/000000'}}/> */}

                      
                    </View>

                
            )
          }}





        />
      </View>

           
    )
  }
  
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      marginTop: 10,
    },
    input: {
      height: 40,
      margin: 12,
      borderWidth: 1,
      padding: 10,
    },
    list: {
      paddingHorizontal: 5,
      backgroundColor: '#E6E6E6',
    },
    list1: {
      paddingHorizontal: 0,
      backgroundColor: '#E6E6E6',
    },
    listContainer: {
      alignItems: 'center',
    },
    separator: {
      marginTop: 10,
    },
    /******** card **************/
    card: {
      shadowColor: '#00000021',
      shadowOffset: {
        width: 2,
      },
      shadowOpacity: 0.5,
      shadowRadius: 4,
      marginVertical: 0,
      backgroundColor: 'white',
      flexBasis: '75%',
      marginHorizontal: 0,
    },
    cardHeader: {
      paddingVertical: 17,
      paddingHorizontal: 16,
      borderTopLeftRadius: 1,
      borderTopRightRadius: 1,
      flexDirection: 'row',
      justifyContent: 'space-between',
    },
    cardContent: {
      paddingVertical: 12.5,
      paddingHorizontal: 16,
    },
    cardFooter: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      paddingTop: 12.5,
      paddingBottom: 25,
      paddingHorizontal: 16,
      borderBottomLeftRadius: 1,
      borderBottomRightRadius: 1,
    },
    cardImage: {
      flex: 1,
      height: 150,
      width: null,
    },

    title: {
      fontSize: 18,
      flex: 1,
    },
    price: {
      fontSize: 16,
      color: 'green',
      marginTop: 5,
    },
    buyNow: {
      color: 'purple',
    },
    icon: {
      width: 25,
      height: 25,
    },

    socialBarContainer: {
      justifyContent: 'center',
      alignItems: 'center',
      flexDirection: 'row',
      flex: 1,
    },
    socialBarSection: {
      justifyContent: 'center',
      flexDirection: 'row',
      flex: 1,
    },
    socialBarlabel: {
      marginLeft: 8,
      alignSelf: 'flex-end',
      justifyContent: 'center',
    },
    socialBarButton: {
      flexDirection: 'row',
      justifyContent: 'center',
      alignItems: 'center',
    },
  })
