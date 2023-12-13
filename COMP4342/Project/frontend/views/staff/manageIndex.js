import React, { useState } from 'react'
import { View, Text, TextInput, Button } from 'react-native';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import {API_ENDPOINT} from '@env'
import {
  StyleSheet,
  TouchableOpacity,
  Image,
  Alert,
  FlatList,
} from 'react-native'

export default function IndexScreen({ navigation }) {

  return (
    <View style={styles.bg}>

                <>

                    <Button
                        style={styles.bt}
                        icon="camera" mode="contained" 
                        title="Product Management"
                        onPress={() => navigation.navigate('Product Management')}
                    >
                        Product Management
                    </Button>
                    <Text>{"\n"}</Text>
                    <Button
                        style={styles.bt}
                        icon="camera" mode="contained" 
                        title="Add New Product"
                        onPress={() => navigation.navigate('Create New Product')}
                    >
                        Add New Product
                    </Button>
                    <Text>{"\n"}</Text>
                    <Button
                        style={styles.bt}
                        icon="camera" mode="contained" 
                        title="Order List"
                        onPress={() => navigation.navigate('Order Overview')}
                    >
                        Order List
                    </Button>
   
                </>
            
        </View>
  )
}

const styles = StyleSheet.create({
    bg: {
      alignSelf: 'center',
      backgroundColor: '#ffffff',
      height: 30,
      width: '100%',
      justifyContent: 'center',
      flex: 1, 
      alignItems: 'center',
      display: 'flex'
    },
    bt: {
        height: 50,
        width: '100%',
      },



  });
