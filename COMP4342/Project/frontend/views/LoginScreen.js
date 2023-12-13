import * as React from 'react';
import { View, Text } from 'react-native';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { API_ENDPOINT } from '@env'
import { TextInput, Button } from 'react-native-paper';

export default function LoginScreen({ navigation }) {
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');

    const handleLogin = () => {
        // Replace the URL with the actual login API endpoint.
        const loginUrl = API_ENDPOINT + "/login/";

        // Prepare the data to send to the server.
        const data = {
            username,
            password,
        };

        // Make a POST request to the login API endpoint.
        axios.post(loginUrl, data)
            .then(response => {
                // Check if the response contains a token (replace 'token' with the actual key in the response).
                const token = String(response.data.token);
                const user_id = String(response.data.user_id);
                const is_staff = String(response.data.is_superuser);
                if (token) {
                    // Store the token in local storage.
                    AsyncStorage.multiSet([
                        ['token', token],
                        ['user_id', user_id],
                        ['is_staff', is_staff]
                    ])
                        .then(() => {
                            if (!is_staff) {
                                navigation.navigate('Account');
                            } else {
                                navigation.navigate('StaffRouter');
                            }
                        })
                        .catch(error => {
                            console.error('Error storing token:', error);
                            
                        });
                } else {
                    alert('Login failed. Please try again.');
                }
            })
            .catch(error => {
                console.log(error);
                // Handle login failure (e.g., show an error message).
                alert('Login failed. Please try again.');
            });
    };

    return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
            <Text>Login Screen</Text>
            <TextInput
                label="Username"
                value={username}
                onChangeText={text => setUsername(text)}
                style={{ borderWidth: 1, width: 300, margin: 10, padding: 5 }}
            />
            <TextInput
                label="Password"
                value={password}
                onChangeText={text => setPassword(text)}
                secureTextEntry={true}
                style={{ borderWidth: 1, width: 300, margin: 10, padding: 5 }}
            />

            <Button icon="login" mode="elevated" onPress={handleLogin}>
                Login
            </Button>

            <View style={{ marginVertical: 10 }}>
                <Button icon="account-plus-outline" mode="elevated" onPress={() => navigation.navigate('RegisterScreen')}>
                    Registration
                </Button>
            </View>

            {/* <Button title="Directly Into Product List" onPress={() => navigation.navigate('Product List')}/> */}
        </View>
    );
}
