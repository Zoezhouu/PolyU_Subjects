import * as React from 'react';
import { View, Text, TextInput, Button, Alert } from 'react-native';
import axios from 'axios';
// import AsyncStorage from '@react-native-async-storage/async-storage';
import {API_ENDPOINT} from '@env'


export default function Pay({ totalPrice }) {
  const checkoutUrl = API_ENDPOINT + "pay"
  const handlePayment = () => {
    // assume the payment is successful
    Alert.alert('Payment Successful', 'Thank you for your purchase!');
    
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text style={{ fontSize: 20, marginBottom: 20 }}>Total Amount: ${totalPrice}</Text>
      <TextInput
        placeholder="Credit Card Number"
        style={{ width: 200, height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 10 }}
      />
      <TextInput
        placeholder="Expiration Date"
        style={{ width: 200, height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 10 }}
      />
      <TextInput
        placeholder="CVV"
        style={{ width: 200, height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 10 }}
      />
      <Button title="Pay Now" onPress={handlePayment} />
    </View>
  );
}