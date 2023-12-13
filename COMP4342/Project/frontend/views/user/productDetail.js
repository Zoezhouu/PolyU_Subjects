import React from 'react'
import {View, Image, Button, FlatList, StyleSheet} from 'react-native'
// import axios from 'axios';
import { API_ENDPOINT } from '@env'


export default function ProductDetail({navigation}, id){
    const { globalState, dispatch } = useGlobalContext(); // Use the global context hook
    const [products, setProducts] = useState([]);
    const productUrl = API_ENDPOINT + '/api/products/' + id;
    const [snackbarVisible, setSnackbarVisible] = useState(false);
    const [snackbarMessage, setSnackbarMessage] = useState('');

    useEffect(() => {
        const getProduct = async() =>{
            try{
                const response = await axios.get(productUrl);
                setProducts(response.data);
            } catch (error) {
                console.log(error);
            }
        };
    })

    const handleAddToFavorites = (item) => {
        if (isItemInFavorites(item)) {
          setSnackbarMessage(`${item.name} is already in favorites`);
        } else {
          dispatch({
            type: ADD_TO_FAVORITES,
            payload: item,
          });
          setSnackbarMessage(`${item.name} added to favorites`);
        }
        setSnackbarVisible(true);
      };
    
    const handleAddToCart = (item) => {
        if (isItemInCart(item)) {
            setSnackbarMessage(`${item.name} is already in the cart`);
        } else {
            dispatch({
            type: ADD_TO_CART,
            payload: item,
            });
            setSnackbarMessage(`${item.name} added to cart`);
        }
        setSnackbarVisible(true);
    };

    const isItemInCart = (item) => {
        return globalState.cart.some((cartItem) => cartItem.id === item.id);
    };

    const isItemInFavorites = (item) => {
        return globalState.favorites.some((favItem) => favItem.id === item.id);
    };

    const onDismissSnackbar = () => {
        setSnackbarVisible(false);
    };

    const renderProduct = ({item}) => (
        <View>
            <Image style={styles.productImage} source={item.image_url}></Image>
            <Text style={styles.productName}>{item.name}</Text>
            <Text style={styles.productPrice}>Price: {item.price}</Text>
            <Text style={styles.productStock}>Stock:{item.stock}</Text>
            <Button icon="heart" onPress={()=> handleAddToFavorites(item)}>Add To Favorites</Button>
            <Button icon="cart-arrow-down" onPress={()=>handleAddToCart(item)}>Add To Cart</Button>

        </View>
    )
    return(
        <View style={styles.container}>
            <FlatList 
                data={products}
                renderItem={renderProduct}
                keyExtractor={(item) =>item.id.toString()}
            />
            <Snackbar
        visible={snackbarVisible}
        onDismiss={onDismissSnackbar}
        action={{
          label: 'OK',
          onPress: onDismissSnackbar,
        }}
      >
        {snackbarMessage}
      </Snackbar>
        </View>
    )
}

const styles = StyleSheet.create({
    container:{
        flex: 1,
        padding: 16,
    },
    list:{
        paddingHorizontal: 5,
        backgroundColor: '#E6E6E6'
    },
    productImage:{
        aspectRation: 16 / 9,
        borderRadius: 8
    },
    productName:{
        fontSize: 18,
        fontWeight: 'bold',
        marginBottom: 8,
    },
    productPrice:{
        fontSize: 16,
        color: '#555',
        marginBottom: 4,
    },
    productStock: {
        fontSize: 16,
        color: '#555',
    },
});