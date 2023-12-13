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

const productUrl = API_ENDPOINT + "/api/products/"
  useEffect( ()=>{
    const getPdtList= async()=>{
      axios.get(productUrl)  
      .then(res=>setProducts(res.data) )
      .catch(error=>console.log(error)); 

      }
      getPdtList();
    },[]);
  
    // const addProductToCart = () => {
    //   Alert.alert('Success'+ item.id)
    // }

    const selectProduct = (item) => {
      const value = item.id;
      navigation.navigate('Product Detail Edit', {id: value} )
   };
  
    return (
      <View style={styles.container}>
        <FlatList
          style={styles.list}
          contentContainerStyle={styles.listContainer}
          data={products}
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
              <TouchableOpacity
                        style={styles.card}
                        //onPress={() => navigation.navigate('Product Detail Edit', item.id )}>
                        onPress={() => selectProduct(item)}>
                        
                        
                <View style={styles.card}>
                  <View style={styles.cardHeader}>
                    <View>
                      <Text style={styles.title}>{item.name}</Text>
                      <Text style={styles.price}>${item.price}</Text>
                    </View>
                  </View>
                  <Image style={styles.cardImage} source={ item.image_url  ? { uri: item.image_url } : { uri:'https://bootdey.com/image/400x200/40E0D0/000000'}}/>
                  <View style={styles.cardFooter}>
                    <View style={styles.socialBarContainer}>
                      <View style={styles.socialBarSection}>
                        
                          <Image
                            style={styles.icon}
                            source={{
                              uri: 'https://cdn-icons-png.flaticon.com/512/4601/4601560.png',
                            }}
                          />
                          <Text style={[styles.socialBarLabel, styles.buyNow]}>{item.stock} Available </Text>
                        
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
      shadowColor: '#00000021',
      shadowOffset: {
        width: 2,
      },
      shadowOpacity: 0.5,
      shadowRadius: 4,
      marginVertical: 8,
      backgroundColor: 'white',
      flexBasis: '47%',
      marginHorizontal: 5,
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
  