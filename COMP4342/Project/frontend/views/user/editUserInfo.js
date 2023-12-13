import React, {useState, useEffect} from 'react'
import {View, Text, Button, Alert, TextInput} from 'react-native'
import axios from 'axios';
import {API_ENDPOINT} from '@env'

export default function EditPersonalInfo({navigation}) {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [address, setAddress] = useState('');
    const [oldPassword, setOldPassword] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const data = {
      id,
      firstName,
      lastName,
      email,
      address, 
      newPassword,
      oldPassword,
      confirmPassword,
    };
    
    

    const profileUrl = API_ENDPOINT + "/api/${id}/profile"

  const handleSave = () => {
    axios.post(profileUrl, data)
      .then(response => {
        const token = response.data.token;
        if (!firstName || !lastName || !email || !address || !oldPassword || !newPassword || !confirmPassword) 
          {
            Alert.alert('Error', 'Please fill in all the fields.');
            return;
          } 
          else if (oldPassword == newPassword)
          {
              Alert.alert('Error', 'Old and new password cannot be same.');
              return;
          } 
          else if (newPassword != confirmPassword)
          {
            Alert.alert('Error','Password does not match.');
            return;
          }
          else{
            console.log(token);
            Alert.alert("Your profile updated successfully.")
            navigation.navigate('login')
          }
      })
      .catch(error => {
        alert("Your profile update action failed. Please try again");
        console.log(error);
      });
    
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Edit Personal Information</Text>
      <TextInput
        placeholder="First Name"
        value={firstName}
        onChangeText={text => setFirstName(text)}
        style={{ borderWidth: 1, width: 200, margin: 10, padding: 5 }}
      />
      <TextInput
        placeholder="Last Name"
        value={lastName}
        onChangeText={text => setLastName(text)}
        style={{ borderWidth: 1, width: 200, margin: 10, padding: 5 }}
      />
      <TextInput
        placeholder="Email"
        value={email}
        onChangeText={text => setEmail(text)}
        style={{ borderWidth: 1, width: 200, margin: 10, padding: 5 }}
      />
      <TextInput
        placeholder="Address"
        value={address}
        onChangeText={text => setAddress(text)}
        style={{ borderWidth: 1, width: 200, margin: 10, padding: 5 }}
      />
      <TextInput
        placeholder="Old Password"
        value={password}
        onChangeText={text => setOldPassword(text)}
        style={{ borderWidth: 1, width: 200, margin: 10, padding: 5 }}
        secureTextEntry
      />
      <TextInput
        placeholder="New Password"
        value={password}
        onChangeText={text => setNewPassword(text)}
        style={{ borderWidth: 1, width: 200, margin: 10, padding: 5 }}
        secureTextEntry
      />
      <TextInput
        placeholder="Confirm Password"
        value={password}
        onChangeText={text => setConfirmPassword(text)}
        style={{ borderWidth: 1, width: 200, margin: 10, padding: 5 }}
        secureTextEntry
      />

      <Button title="Save" onPress={handleSave} />
    </View>
  );
}