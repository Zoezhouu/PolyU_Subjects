import React from 'react';
import { View, Text } from 'react-native';

export default function ViewPersonalInfo() {
  // Fetch the personal information from an API or storage
  const firstName = 'John';
  const lastName = 'Doe';
  const phoneNumber = '1234567890';

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>View Personal Information</Text>
      <Text>First Name: {firstName}</Text>
      <Text>Last Name: {lastName}</Text>
      <Text>Phone Number: {phoneNumber}</Text>
    </View>
  );
}