// CartScreen.js
import React, { useEffect, useState, useCallback } from 'react';
import { View, FlatList, StyleSheet, Text } from 'react-native';
import { Title, Card, Paragraph, Button } from 'react-native-paper';
import { useGlobalContext } from '../globalProvider';
import { useNavigation, useFocusEffect } from '@react-navigation/native';

const CartScreen = () => {
    const navigation = useNavigation(); // Get the navigation prop
    const { globalState, dispatch } = useGlobalContext();

    const removeFromCart = (itemId) => {
        dispatch({
            type: 'REMOVE_FROM_CART', // Update with your actual action type
            payload: { id: itemId },
        });
    };

    const calculateTotalPrice = () => {
        // Calculate the total price based on items in the cart
        const total = globalState.cart.reduce((acc, item) => acc + parseFloat(item.price), 0);

        // Ensure that total is a number before using toFixed
        const formattedTotal = !isNaN(total) ? total.toFixed(2) : '0.00';

        return formattedTotal;
    };

    const handlePurchase = () => {
        // Navigate to PurchaseScreen and pass the total price
        navigation.navigate('purchaseScreen', { totalPrice: calculateTotalPrice() });
    };

    const isPurchaseButtonVisible = globalState.cart.length >= 1;
    const isCartEmpty = globalState.cart.length === 0;
    
    useFocusEffect(
        useCallback(() => {

        }, [])
    );
    return (
        <View style={styles.container}>
            {isCartEmpty ? (
                <View style={styles.emptyCartContainer}>
                    <Text style={styles.emptyCartText}>No items in the cart</Text>
                </View>
            ) : (
                <>
                    <FlatList
                        data={globalState.cart}
                        renderItem={({ item }) => (
                            <Card style={styles.productContainer}>
                                <Card.Cover source={{ uri: item.image_url }} style={styles.productImage} />
                                <Card.Content>
                                    <Title style={styles.productName}>{item.name}</Title>
                                    <Paragraph style={styles.productPrice}>Price: ${item.price}</Paragraph>
                                    <Paragraph style={styles.productStock}>Stock: {item.stock}</Paragraph>
                                </Card.Content>
                                <Card.Actions>
                                    <Button icon="delete-empty" onPress={() => removeFromCart(item.id)}>Remove from Cart</Button>
                                </Card.Actions>
                            </Card>
                        )}
                        keyExtractor={(item) => item.id.toString()}
                    />
                    <View style={styles.totalContainer}>
                        <Text style={styles.totalText}>Total: ${calculateTotalPrice()}</Text>
                        <Button icon="cart" mode="elevated" onPress={handlePurchase}>
                            Make Purchase
                        </Button>
                    </View>
                </>
            )}
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
    totalContainer: {
        marginTop: 16,
        alignItems: 'flex-end',
    },
    totalText: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    emptyCartContainer: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    emptyCartText: {
        fontSize: 18,
        fontWeight: 'bold',
        color: '#555',
    },
});

export default CartScreen;
