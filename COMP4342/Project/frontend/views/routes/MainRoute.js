// MainRoute.js
import React, { useState } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import StaffRouter from './staffRouter';
import UserRouter from './userRouter';
import { GlobalProvider } from '../../views/globalProvider';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const MainRoute = () => {
    const Stack = createNativeStackNavigator();


    return (
        <GlobalProvider>
            <NavigationContainer>
                <Stack.Navigator initialRouteName="UserRouter">
                    <Stack.Screen
                        name="StaffRouter"
                        component={StaffRouter}
                        options={{ headerShown: false }}
                    />
                    <Stack.Screen
                        name="UserRouter"
                        component={UserRouter}
                        options={{ headerShown: false }}
                    />
                </Stack.Navigator>
            </NavigationContainer>
        </GlobalProvider>
    );
};

export default MainRoute;
