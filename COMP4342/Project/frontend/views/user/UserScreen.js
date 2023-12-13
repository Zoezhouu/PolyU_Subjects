import React, { useEffect, useState, useCallback  } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useNavigation, useFocusEffect  } from '@react-navigation/native';
import axios from 'axios';
import {API_ENDPOINT} from '@env'

const UserScreen = () => {
    const [user, setUser] = useState(null);
    const navigation = useNavigation();

    useEffect(() => {
        // Check if the user is logged in
        checkLoginStatus();
    }, []);

    // useFocusEffect to refresh user data when the screen comes into focus
    useFocusEffect(
        useCallback(() => {
            checkLoginStatus();
        }, [])
    );

    const checkLoginStatus = async () => {
        try {
            // Check if there is a token in AsyncStorage
            const token = await AsyncStorage.getItem('token');
            if (token) {
                // If token exists, fetch user info or perform any necessary actions
                // For demonstration purposes, let's assume there's a function getUserInfo
                // that retrieves user information based on the token
                const userInfo = await getUserInfo(token);

                // Set the user state
                setUser(userInfo);
            } else {
                // If no token, navigate to the login screen
                navigation.navigate('LoginScreen');
            }
        } catch (error) {
            console.error('Error checking login status:', error);
        }
    };

    const getUserInfo = async () => {
        try {
            // Retrieve user ID from AsyncStorage
            const userId = await AsyncStorage.getItem('user_id');
            const  new_userId = parseInt(userId);
            // Make a GET request using axios
            const response = await axios.get(`${API_ENDPOINT}/api/users/${new_userId}/`);
    
            // Extract the required information from the response
            const { first_name, last_name, username } = response.data;
    
            // Return the extracted information
            return {
                first_name,
                last_name,
                username,
            };
        } catch (error) {
            // Handle errors here, e.g., log the error or throw an exception
            console.error('Error fetching user information:', error);
            throw error;
        }
    };

    const handleLogout = async () => {
        try {
            // Clear the token from AsyncStorage
            await AsyncStorage.removeItem('token');
            await AsyncStorage.removeItem('user_id');
            await AsyncStorage.removeItem('is_staff');
            // Navigate to the login screen
            navigation.navigate('LoginScreen');
        } catch (error) {
            console.error('Error logging out:', error);
        }
    };
    console.log(user)
    if (user) {
        return (
            <View style={styles.container}>
                <Text style={styles.userInfoText}>Welcome, {user.username}!</Text>
                <Button title="Logout" onPress={handleLogout} />
            </View>
        );
    } else {
        // You can show a loading spinner or other UI while checking the login status
        return (
            <View style={styles.container}>
                <Text>Loading...</Text>
            </View>
        );
    }
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    userInfoText: {
        fontSize: 18,
        fontWeight: 'bold',
        marginBottom: 16,
    },
});

export default UserScreen;
