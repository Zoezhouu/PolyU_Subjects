
import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { Ionicons } from '@expo/vector-icons';
import UserScreen from '../user/UserScreen';
import LoginScreen from '../LoginScreen';
import RegisterScreen from '../user/RegisterScreen';

const Stack = createNativeStackNavigator();

const AccountRoute = () => {
    return (
        <Stack.Navigator initialRouteName="Account">
            <Stack.Screen name="Account" component={UserScreen} options={{ headerShown: false }}/>
            <Stack.Screen name="LoginScreen" component={LoginScreen} options={{ headerShown: false }} /> 
            <Stack.Screen name="RegisterScreen" component={RegisterScreen} options={{ headerShown: false }} /> 
        </Stack.Navigator>
    );
};

export default AccountRoute;
