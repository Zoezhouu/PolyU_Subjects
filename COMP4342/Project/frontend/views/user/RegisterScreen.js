import * as React from 'react';
import { View, Text, Alert } from 'react-native';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { API_ENDPOINT } from '@env';
import { TextInput, Button } from 'react-native-paper';

export function registerUser(username, password, confirmPassword, firstName, lastName, navigation) {
  const registrationUrl = `${API_ENDPOINT}/api/users/`;

  if (password !== confirmPassword) {
    Alert.alert('Error', 'Passwords do not match.');
    return;
  }

  const data = {
    username,
    password,
    confirmPassword,
    first_name: firstName,
    last_name: lastName,
  };

  axios.post(registrationUrl, data)
    .then(response => {
      if (response.status === 201) {
        const token = response.data.token;
        const user_id = response.data.user_id;
        const is_staff = response.data.is_staff;
        AsyncStorage.multiSet([
          ['token', token],
          ['user_id', user_id],
          ['is_staff', is_staff]
        ])
          .then(() => {
            navigation.navigate('Account');
          })
          .catch(error => {
            console.error('Error storing token:', error);
          });
      } else {
        const errorMessage = response.data.error || 'Registration failed. Please try again.';
        Alert.alert('Error', errorMessage);
      }
    })
    .catch(error => {
      console.log(error);
      Alert.alert('Error', 'Registration failed. Please try again.');
    });
}

export default function RegisterScreen({ navigation }) {
  const [username, setUsername] = React.useState('');
  const [password, setPassword] = React.useState('');
  const [confirmPassword, setConfirmPassword] = React.useState('');
  const [firstName, setFirstName] = React.useState('');
  const [lastName, setLastName] = React.useState('');

  const handleRegistration = () => {
    registerUser(username, password, confirmPassword, firstName, lastName, navigation);
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center', padding: 0 }}>
      <Text style={{ fontSize: 24, marginBottom: 20 }}>Registration Screen</Text>
      <TextInput
        label="First Name"
        value={firstName}
        onChangeText={text => setFirstName(text)}
        style={styles.input}
      />
      <TextInput
        label="Last Name"
        value={lastName}
        onChangeText={text => setLastName(text)}
        style={styles.input}
      />
      <TextInput
        label="Your username"
        value={username}
        onChangeText={text => setUsername(text)}
        style={styles.input}
      />
      <TextInput
        label="Password"
        value={password}
        onChangeText={text => setPassword(text)}
        secureTextEntry={true}
        style={styles.input}
      />
      <TextInput
        label="Confirm password"
        value={confirmPassword}
        onChangeText={text => setConfirmPassword(text)}
        secureTextEntry={true}
        style={styles.input}
      />

      <Button icon="account-plus" mode="elevated" onPress={handleRegistration}>
        Sign up
      </Button>
    </View>
  );
}

const styles = {
  input: {
    borderWidth: 1,
    width: 300,
    marginVertical: 10,
    padding: 10,
    borderRadius: 8,
  },
};
