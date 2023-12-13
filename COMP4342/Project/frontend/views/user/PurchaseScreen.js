import React, { useState, useEffect } from 'react';
import { View, Text, Button, StyleSheet, FlatList } from 'react-native';
import Ionicons from 'react-native-vector-icons/Ionicons';
import { Picker } from '@react-native-picker/picker';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import { useGlobalContext } from '../globalProvider'; // Update the path
import {API_ENDPOINT} from '@env'

const PurchaseScreen = ({ route, navigation }) => {
    // const { totalPrice } = route.params;
    const [selectedPaymentMethod, setSelectedPaymentMethod] = useState('creditCard');
    const [userId, setUserId] = useState(null);
    const { globalState } = useGlobalContext();
    const { cart: cartItems } = globalState;


    const [localCart, setLocalCart] = useState([]);
    const [totalPrice, setTotalPrice] = useState(0);

    useEffect(() => {
        const retrieveUserId = async () => {
            try {
                const userIdFromStorage = await AsyncStorage.getItem('user_id');
                setUserId(userIdFromStorage);
            } catch (error) {
                console.error('Error retrieving user ID:', error);
            }
        };

        retrieveUserId();
        calculateTotalPrice(cartItems);
    }, []);


    useEffect(() => {
        // Copy the cart items to local state when the cart changes
        setLocalCart([...cartItems]);
    }, [cartItems]);

    const handleQuantityChange = (index, quantity) => {

        const updatedLocalCart = [...localCart];
        updatedLocalCart[index].quantity = quantity;
        setLocalCart(updatedLocalCart);
        // console.log(localCart);
        calculateTotalPrice(localCart);
    };

    const calculateTotalPrice = (cart) => {
        let total = 0;
        cart.forEach((item) => {
            const quantity = item.quantity !== undefined ? item.quantity : 1;
            total += item.price * quantity;
        });
        setTotalPrice(total);
    };

    const handlePurchase = async () => {
        try {
            if (!localCart || localCart.length === 0) {
                console.error('Cart is empty. Cannot proceed with the purchase.');
                return;
            }
            console.log('localCart', localCart);
            if (!userId) {
                alert('Please log in to purchase items');
                return;
            }
            const orderData = {
                customer: parseInt(userId),
                total_amount: totalPrice,
                status: 'pending',
                delivery_status: 'not_delivered',
                products: localCart.map(item => ({
                    product_id: item.id,
                    quantity: item.quantity !== undefined ? parseInt(item.quantity) : 1,
                })),
            };
            
            const response = await axios.post(`${API_ENDPOINT}/api/orders/`, orderData);

            if (response.status === 201) {
                console.log('Order created successfully');
                alert('Order created successfully');
                navigation.push('index');
            } else {
                console.error('Failed to create order:', response.status);
            }
        } catch (error) {
            console.error('Error during purchase:', error);
        }
    };


    const renderCartItem = ({ item, index }) => (
        <View style={styles.cartItem}>
            <Text>{item.name}</Text>
            <Text>Price: ${item.price}</Text>
            <View style={styles.quantityContainer}>
                <Text>Quantity:</Text>
                <Picker
                    style={styles.quantityPicker}
                    selectedValue={item.quantity}
                    onValueChange={(quantity) => handleQuantityChange(index, quantity)}
                >
                    {[...Array(10).keys()].map((value) => (
                        <Picker.Item key={value} label={String(value + 1)} value={value + 1} />
                    ))}
                </Picker>
            </View>
        </View>
    );

    return (
        <View style={styles.container}>
            <Text style={styles.totalText}>Total: ${totalPrice}</Text>
            <Text style={styles.paymentMethodText}>Select Payment Method:</Text>
            <Picker
                selectedValue={selectedPaymentMethod}
                onValueChange={(itemValue) => setSelectedPaymentMethod(itemValue)}
                style={styles.picker}
            >
                <Picker.Item label="Credit Card" value="creditCard" />
                <Picker.Item label="PayPal" value="paypal" />
                {/* Add more payment methods as needed */}
            </Picker>
            <FlatList
                data={cartItems}
                renderItem={renderCartItem}
                keyExtractor={(item) => item.id.toString()}
                style={styles.orderSummary}
            />
            <Button title="Purchase" onPress={handlePurchase} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16,
    },
    totalText: {
        fontSize: 18,
        fontWeight: 'bold',
        marginBottom: 16,
    },
    paymentMethodText: {
        fontSize: 16,
        marginBottom: 8,
    },
    picker: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        marginBottom: 16,
    },
    orderSummary: {
        marginTop: 16,
    },
    cartItem: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        marginBottom: 8,
    },
});

export default PurchaseScreen;
