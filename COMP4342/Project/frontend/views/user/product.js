import React from "react";
import {View, Text} from 'react-native'

export default function Product({
    name, price, description, image_url, category, stock, id
}) 

{
    return(
        <View>
            <Text> Name: {name}</Text>
            <Text> Price: {price}</Text>
            <Text> Description: {description}</Text>
            <Text> Image: {image_url}</Text>
            <Text> Category: {category}</Text>
            <Text> Stock: {stock}</Text>
            {/* <Text> ID: {id}</Text> */}
        </View>
    )
}