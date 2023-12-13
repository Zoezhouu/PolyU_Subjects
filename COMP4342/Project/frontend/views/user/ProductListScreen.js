import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity, Image, StyleSheet } from 'react-native';
import { Title, Card, Button, Avatar, Paragraph, Snackbar } from 'react-native-paper';
import { API_ENDPOINT } from '@env';
import axios from 'axios';
import { useGlobalContext, ADD_TO_FAVORITES, ADD_TO_CART } from '../globalProvider';

const ProductListScreen = ({ navigation }) => {
  const { globalState, dispatch } = useGlobalContext(); // Use the global context hook
  const [products, setProducts] = useState([]);
  const productUrl = API_ENDPOINT + '/api/products/';
  const [snackbarVisible, setSnackbarVisible] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');


  useEffect(() => {
    const getProductList = async () => {
      try {
        const response = await axios.get(productUrl);
        setProducts(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    getProductList();
  }, []);

  // const handleProductPress = (item) => {
  //   navigation.navigate('ProductDetail', { product: item });
  // };

  const handleAddToFavorites = (item) => {
    if (isItemInFavorites(item)) {
      setSnackbarMessage(`${item.name} is already in favorites`);
    } else {
      dispatch({
        type: ADD_TO_FAVORITES,
        payload: item,
      });
      setSnackbarMessage(`${item.name} added to favorites`);
    }
    setSnackbarVisible(true);
  };

  const handleAddToCart = (item) => {
    if (isItemInCart(item)) {
      setSnackbarMessage(`${item.name} is already in the cart`);
    } else {
      dispatch({
        type: ADD_TO_CART,
        payload: item,
      });
      setSnackbarMessage(`${item.name} added to cart`);
    }
    setSnackbarVisible(true);
  };

  const isItemInCart = (item) => {
    return globalState.cart.some((cartItem) => cartItem.id === item.id);
  };

  const isItemInFavorites = (item) => {
    return globalState.favorites.some((favItem) => favItem.id === item.id);
  };

  const onDismissSnackbar = () => {
    setSnackbarVisible(false);
  };

  const renderProduct = ({ item }) => (
    <TouchableOpacity onPress={() => handleProductPress(item)}>
      <Card style={styles.productContainer}>
        <Card.Cover source={{ uri: item.image_url }} style={styles.productImage} />
        <Card.Content>
          <Title style={styles.productName}>{item.name}</Title>
          <Paragraph style={styles.productPrice}>Price: ${item.price}</Paragraph>
          <Paragraph style={styles.productStock}>Stock: {item.stock}</Paragraph>
        </Card.Content>
        <Card.Actions>
          <Button icon="heart" onPress={() => handleAddToFavorites(item)}>Add to Favorites</Button>
          <Button icon="cart-arrow-down" onPress={() => handleAddToCart(item)}>Add to Cart</Button>
        </Card.Actions>
      </Card>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={products}
        renderItem={renderProduct}
        keyExtractor={(item) => item.id.toString()}
      />
      <Snackbar
        visible={snackbarVisible}
        onDismiss={onDismissSnackbar}
        action={{
          label: 'OK',
          onPress: onDismissSnackbar,
        }}
      >
        {snackbarMessage}
      </Snackbar>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  productContainer: {
    marginBottom: 16,
  },
  productImage: {
    aspectRatio: 16 / 9,
    borderRadius: 8,
  },
  productName: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  productPrice: {
    fontSize: 16,
    color: '#555',
    marginBottom: 4,
  },
  productStock: {
    fontSize: 16,
    color: '#555',
  },
});

export default ProductListScreen;
