import React, {useEffect, useState} from 'react';
import {useDispatch, useSelector} from 'react-redux';
import {addCart, getCart} from '../user/productAction'
import {View, Text, FlatList, Button} from 'react-native';

// let shoppingCart = [];

// export function addToCart(item) {
//   shoppingCart.push(item);
// }

// export function removeFromCart(itemId) {
//   shoppingCart = shoppingCart.filter((item) => item.id !== itemId);
// }

// export function clearCart() {
//   shoppingCart = [];
// }


export default function ShoppingCart({ cartItems, onRemoveItem }) {
  const renderItem = ({ item }) => (
    <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', padding: 10 }}>
      <Text>{item.name}</Text>
      <Text> Quantity: {item.quantity}</Text>
      <Button title="Remove" onPress={() => onRemoveItem(item.id)} />
    </View>
  );

  const calculateTotalPrice = () => {
    let totalPrice = 0;
    cartItems.forEach(item => {
      totalPrice += item.price * item.quantity;
    });
    return totalPrice;
  };

  return (
    <View style={{ flex: 1 }}>
      {cartItems.length > 0 ? (
        <FlatList
          data={cartItems}
          renderItem={renderItem}
          keyExtractor={item => item.id.toString()}
        />
      ) : (
        <Text>Your cart is empty.</Text>
      )}
      <Text style={{ fontWeight: 'bold', marginVertical: 10 }}>Total Price: ${calculateTotalPrice()}</Text>
      <Button title = 'Check Out' onPress = {navigation.navigate('checkout')}/>
    </View>
  );
}