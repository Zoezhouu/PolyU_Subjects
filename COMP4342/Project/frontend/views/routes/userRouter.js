// userRouter.js
import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import IndexScreen from '../index/userIndex';
import ProductDetailScreen from '../user/productDetail';
import ProductListScreen from '../user/ProductListScreen';
import PurchaseScreen from '../user/PurchaseScreen';
import LoginScreen from '../LoginScreen';
import RegisterScreen from '../RegisterScreen';

const Stack = createNativeStackNavigator();

const UserRouter = () => {
    return (
        <Stack.Navigator initialRouteName="index">
            {/* <Stack.Screen name="login" component={LoginScreen} /> */}
            <Stack.Screen
                name="index"
                component={IndexScreen}
                options={{ headerShown: false }}
            />
            {/* <Stack.Screen name="register" component={RegisterScreen} /> */}
            {/* <Stack.Screen
                name="Product List"
                component={ProductListScreen}
                options={{ headerShown: false }}
            /> */}
            {/* <Stack.Screen name="productDetail" component={ProductDetailScreen} /> */}
            <Stack.Screen name="purchaseScreen" component={PurchaseScreen} />
            
        </Stack.Navigator>
    );
}

export default UserRouter;
