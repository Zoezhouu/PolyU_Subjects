import React, { useState, useEffect, SafeAreaView} from 'react'
import { useRoute } from "@react-navigation/native"
import {
  StyleSheet,
  Text,
  TextInput,
  View,
  TouchableOpacity,
  Image,
  Alert,
  FlatList,
  Button,
} from 'react-native'
import axios from 'axios';
import { API_ENDPOINT } from '@env'
import * as ImagePicker from "expo-image-picker";


export default function Store ({ navigation }) {
  const [name, setName] = React.useState(null);
  const [description, setDescription] = React.useState(null);
  const [price, setPrice] = React.useState(null);
  //const [image_url, setImage_url] = React.useState(null);
  const [category, setCategory] = React.useState(null);
  const [stock, setStock] = React.useState(null);
  const [error, setError] = useState(null); 
  const [edit, setEdit] = useState(false);
  const data = [{
    name,
    description,
    price,
    //image_url,
    category,
    stock,
  }];

  const [products, setProducts] = useState()
  const route = useRoute()
  const idvalue = route.params?.id
  const productUrl = API_ENDPOINT + "/api/products/" + idvalue + "/"
  const [items, setItems] = useState(data);
    useEffect( ()=>{
      const getPdtList = async()=>{
        axios.get(productUrl)  
        //res.header("Access-Control-Allow-Origin", "*");
        .then(res=>setProducts([res.data]))
        .catch(error=>console.log(error)); 
        }
        getPdtList();
        // const listItems = products.map(item =>
        //   data.name = item.name, 
        //   data.description = item.description, 
        //   data.price = item.price, 
        //   data.category = item.category, 
        //   data.stock = item.stock
        // )
    
        
      })

        

  



    //   // Make a POST request to the login API endpoint.
    const handleItemManagement = () => {      
      
      let obj = [{}];
      //obj = []; // replacing it with a new object works
      console.log(name);
      if (name != null){
        obj[0].name=(name)
      }
      if (description != null){
        obj[0].description=(description)
      }
      if (price != null){
        obj[0].price=(price)
      }
      // if (image_url != null){
      //   obj[0].image_url=(image_url)
      // }
      if (category != null){
        obj[0].category=(category)
      }
      if (stock != null){
        obj[0].stock=(stock)
      }

      if(obj != null){
        axios.patch(productUrl, obj[0])
        .then(response => {
          alert("Your profile updated successsfully.")
        })
        .catch(error => {
          alert("Your profile update action failed. Please try again");
          console.log(error);
        });
      }
      
    };

    
    //const [products, setProducts] = useState(data)
    //<Text style={styles.title}>{item.name}</Text>
    //<Text style={styles.price}>${item.price}</Text>
    // const pickImage = async () => {
    //   const { status } = await ImagePicker.
    //     requestMediaLibraryPermissionsAsync();
  
    //   if (status !== "granted") {
  
    //     // If permission is denied, show an alert 
    //     Alert.alert(
    //       "Permission Denied",
    //       `Sorry, we need camera  
    //               roll permission to upload images.`
    //     );
    //   } else {
  
    //     // Launch the image library and get 
    //     // the selected image 
    //     const result =
    //       await ImagePicker.launchImageLibraryAsync();
  
    //     if (!result.cancelled) {
  
    //       // If an image is selected (not cancelled),  
    //       // update the file state variable 
    //       setImage_url(result.uri);
  
    //       // Clear any previous errors 
    //       setError(null);
    //     }
    //   }
    // };

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
            <View style={styles.card}>
              <View style={styles.cardHeader}>
                <View>
                  <Text style={{ fontSize: 16, fontWeight: 'bold', textAlign: 'center' }}>Product ID: {item.id}</Text>
                  <Text style={{ fontSize: 2 }}>{"\n"}</Text>
                  <Text style={{ fontSize: 14 }}>Item Name:</Text>
                  <TextInput
                    editable

                    defaultValue={item.name}
                    onChangeText={text => setName(text)}
                    
                    style={{ backgroundColor: '#f5f5f5', borderWidth: 1, width: 270, margin: 0, padding: 5, fontSize: 16 }}
                  />
                  <Text style={{ fontSize: 14, color: 'green' }}>Item Price:</Text>
                  <TextInput

                    defaultValue={item.price}
                    onChangeText={text => setPrice(Number(text))}
                    style={{ backgroundColor: '#f5f5f5', borderWidth: 1, borderColor: 'green', width: 270, margin: 0, padding: 5, fontSize: 16, color: 'green' }}
                    keyboardType="phone-pad"
                  />
                </View>
              </View>
              <Image style={styles.cardImage} source={ item.image_url ? { uri: item.image_url } : { uri:'https://bootdey.com/image/400x200/40E0D0/000000'}}/>

              <View style={styles.cardFooter}>
                <View>
                  {/* <Text style={{fontSize: 14}}>Image Link: </Text>
                      <TextInput
                        placeholder="Image Link"
                        value={image_url}
                        onChangeText={text => setImage_url(text)}
                        style={{ backgroundColor: '#f5f5f5', borderWidth: 1, width: 270, margin: 0, padding: 5 , fontSize: 16}}
                      /> */}
                  {/* <View style={styles.container}>
                    <Text style={styles.header}>
                      Add Image:
                    </Text>

                    
                    <TouchableOpacity style={styles.button}
                      onPress={pickImage}>
                      <Text style={styles.buttonText}>
                        Choose Image
                      </Text>
                    </TouchableOpacity>

                    
                    {image_url ? (
                      // Display the selected image 
                      <View style={styles.imageContainer}>
                        <Image source={{ uri: image_url }}
                          style={styles.image} />
                      </View>
                    ) : (
                      // Display an error message if there's  
                      // an error or no image selected 
                      <Text style={styles.errorText}>{error}</Text>
                    )}
                  </View> */}


                  <Text style={[styles.buyNow]}>Stock Available: </Text>
                  <TextInput

                    defaultValue={item.stock}
                    onChangeText={text => setStock(Number(text))}
                    style={{ backgroundColor: '#f5f5f5', borderColor: 'purple', borderWidth: 1, width: 270, margin: 0, padding: 5, fontSize: 16 }}
                    keyboardType="phone-pad"
                  />
                  <Text style={{ fontSize: 14, color: 'brown' }}>Category: </Text>
                  <TextInput

                    defaultValue={item.category}
                    onChangeText={text => setCategory(text)}
                    style={{ backgroundColor: '#f5f5f5', borderColor: 'brown', borderWidth: 1, width: 270, margin: 0, padding: 5, fontSize: 16 }}
                  />
                  <Text style={{ fontSize: 14 }}>Product description: </Text>
                  <TextInput
                    multiline={true}
                    numberOfLines={6}

                    defaultValue={item.description}
                    onChangeText={text => setDescription(text)}
                    style={{ backgroundColor: '#f5f5f5', borderWidth: 1, width: 270, margin: 0, padding: 5, fontSize: 16, textAlignVertical: "top" }}
                  />
                  <Text style={{ fontSize: 4 }}>{"\n"}</Text>
                  <Button title="Confirm" onPress={handleItemManagement} />
                </View>
              </View>

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
      marginTop: 20,
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
      flexBasis: '75%',
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
