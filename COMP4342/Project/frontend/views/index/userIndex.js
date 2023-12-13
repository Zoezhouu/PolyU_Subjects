import * as React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import { Ionicons } from '@expo/vector-icons'; // Assuming you are using Expo

import ProductListScreen from '../user/ProductListScreen';
import FavoritesScreen from '../user/FavoritesScreen';
import CartScreen from '../user/CartScreen';
import PurchaseScreen from '../user/PurchaseScreen';
import UserScreen from '../user/UserScreen';
import LoginScreen from '../LoginScreen';
import AccountRoute from '../routes/AccountRoute';
import StaffRoute from '../routes/staffRouter';

const Tab = createBottomTabNavigator();

const IndexScreen = () => {
    return (

        <Tab.Navigator
            screenOptions={({ route }) => ({
                tabBarIcon: ({ focused, color, size }) => {
                    let iconName;

                    if (route.name === 'Products') {
                        iconName = focused ? 'list' : 'list';
                    } else if (route.name === 'Favorites') {
                        iconName = focused ? 'heart' : 'heart-outline';
                    } else if (route.name === 'Cart') {
                        iconName = focused ? 'cart' : 'cart-outline';
                    } else if (route.name === 'Account') {
                        iconName = focused ? 'person-circle' : 'person-circle-outline';
                    }

                    return <Ionicons name={iconName} size={size} color={color} />;
                },
            })}
            tabBarOptions={{
                activeTintColor: 'tomato',
                inactiveTintColor: 'gray',
            }}
        >
            <Tab.Screen name="Products" component={ProductListScreen} />
            <Tab.Screen name="Favorites" component={FavoritesScreen} />
            <Tab.Screen name="Cart" component={CartScreen} />
            <Tab.Screen name="Account" component={AccountRoute} />
        </Tab.Navigator>
    );
};

export default IndexScreen;
