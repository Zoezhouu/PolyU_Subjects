import * as React from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import {API_ENDPOINT} from '@env'

export default function LoginScreen({navigation}) {
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');

    const handleLogin = () => {
        // Replace the URL with the actual login API endpoint.
        const loginUrl = API_ENDPOINT+"login/";

        // Prepare the data to send to the server.
        const data = {
            username,
            password,
        };

        // Make a POST request to the login API endpoint.
        axios.post(loginUrl, data)
            .then(response => {
                // Check if the response contains a token (replace 'token' with the actual key in the response).
                const token = response.data.token;
                console.log(token);
                if (token) {
                    // Store the token in local storage.
                    AsyncStorage.setItem('token', token)
                        .then(() => {

                            // Token is stored, navigate to another screen (replace 'TargetScreen' with the actual screen name).
                            navigation.navigate('Product List');
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
                placeholder="Username"
                value={username}
                onChangeText={text => setUsername(text)}
                style={{ borderWidth: 1, width: 200, margin: 10, padding: 5 }}
            />
            <TextInput
                placeholder="Password"
                value={password}
                onChangeText={text => setPassword(text)}
                secureTextEntry={true}
                style={{ borderWidth: 1, width: 200, margin: 10, padding: 5 }}
            />
            <Button title="Login" onPress={handleLogin} />
            <Button title="Registration" onPress={()=>navigation.navigate('register')}/>
            <Button title="Directly Into Product List" onPress={() => navigation.navigate('Product List')}/>
        </View>
    );
}
