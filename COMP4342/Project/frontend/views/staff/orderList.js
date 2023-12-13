import React, { useState, useEffect,} from 'react'
import { useRoute } from "@react-navigation/native"
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  Image,
  Alert,
  FlatList,
} from 'react-native'
import axios from 'axios';
import {API_ENDPOINT} from '@env'



export default function Store({navigation}){
  const [products, setProducts] = useState()

const productUrl = API_ENDPOINT + "/api/orders/"
  useEffect( ()=>{
    const getPdtList= async()=>{
      axios.get(productUrl)  
      .then(res=>setProducts(res.data) )
      .catch(error=>console.log(error)); 
      }
      getPdtList();
    },[]);
  
    const selectProduct = (item) => {
      const value = item.id;
      navigation.navigate('Order View', {id: value} )
  };
  
    return (
      <View style={styles.container}>
        <FlatList
          style={styles.list}
          contentContainerStyle={styles.listContainer}
          data={products}
          horizontal={false}
          numColumns={1}
          keyExtractor={item => {
            return item.id
          }}
          ItemSeparatorComponent={() => {
            return <View style={styles.separator} />
          }}
          renderItem={post => {
            const item = post.item
            return (
              <TouchableOpacity
                        style={styles.card}
                        //onPress={() => navigation.navigate('Product Detail Edit', item.id )}>
                        onPress={() => selectProduct(item)}>
                        
                        
                <View style={styles.card}>
                  <View style={styles.cardHeader}>
                    
                      <Text style={styles.title}>Order {item.id}</Text>
                      
                      <Text style={styles.price}>${item.total_amount}</Text>
                    
                  </View>
                  <View style={styles.cardFooter}>
                    <View style={styles.socialBarContainer}>
                      <View style={styles.socialBarSection}>
                        
                          <Image
                            style={styles.icon}
                            source={{
                              uri: 'https://cdn-icons-png.flaticon.com/512/4601/4601560.png',
                            }}
                          />
                          <Text style={[styles.socialBarLabel, styles.buyNow]}>{item.status}</Text>
                        
                      </View>

                    </View>
                  </View>
                </View>
              </TouchableOpacity>
            )
          }}
        />
      </View>
    )
  }
  
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      marginTop: 20,
    },
    list: {
      paddingHorizontal: 5,
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
      shadowOpacity: 0.5,
      shadowRadius: 4,
      marginVertical: 8,
      backgroundColor: 'white',
      flexBasis: '100%',
      width: 380,
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
      fontSize: 18,
      color: 'green',
      
    },
    buyNow: {
      color: 'purple',
      fontSize: 16,
    },
    icon: {
      width: 25,
      height: 25,
    },

    socialBarContainer: {
      justifyContent: 'right',
      alignItems: 'right',
      flexDirection: 'row',
      flex: 1,
      fontSize: 18,
    },
    socialBarSection: {
      justifyContent: 'right',
      flexDirection: 'row',
      flex: 1,
    },
    socialBarlabel: {
      fontSize: 18,
      marginLeft: 8,
      alignSelf: 'flex-end',
      justifyContent: 'right',
      
    },
    socialBarButton: {
      flexDirection: 'row',
      justifyContent: 'right',
      alignItems: 'right',
    },
  })
  