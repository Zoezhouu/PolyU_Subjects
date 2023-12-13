// staffRouter.js
import React from 'react';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import ManageIndex from '../staff/manageIndex';
import ManageProduct from '../staff/productManage';
import EditProduct from '../staff/productDetailEdit';
import NewProduct from '../staff/productCreate';
import OrderList from '../staff/orderList';
import OrderDetail from '../staff/orderDetail';

const Stack = createNativeStackNavigator();

const StaffRouter = () => {
    return (
        <Stack.Navigator initialRouteName="Management Page">
            <Stack.Screen name="Management Page" component={ManageIndex} />
            <Stack.Screen name="Product Management" component={ManageProduct} />
            <Stack.Screen name="Product Detail Edit" component={EditProduct} />
            <Stack.Screen name="Create New Product" component={NewProduct} />
            <Stack.Screen name="Order Overview" component={OrderList} />
            <Stack.Screen name="Order View" component={OrderDetail} />
        </Stack.Navigator>
    );
}

export default StaffRouter;
