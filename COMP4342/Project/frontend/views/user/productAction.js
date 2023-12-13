import axios from "axios";

export const getProduct = 
    (keyword = '') =>
    async dispatch => {
        try{
            dispatch({
                type: 'allProductRequest',
            });
            const {data} = await axios.get();
            dispatch({
                type:'allProductSuccess',
                payload: data
            })
        } catch(error){
            dispatch({
                type: 'allProductFail',
                payload: error.response.data.message,
            });
        }
    }

export const addCart = 
    (
        productName,
        quantity,
        productImage,
        productPrice,
        userID,
        productID,
        stock,
    ) =>
    async dispatch => {
        try{
            dispatch ({
                type: 'addCartRequest'
            });
            const {data} = await axios.post('addToCart',
            {
                productName,
                quantity,
                productImage,
                productPrice,
                userID,
                productID,
                stock
            })
            dispatch ({
                type: 'addCartSuccess',
                payload: data
            });
        } catch (error) {
            dispatch({
                type:'addCartFail',
                payload: error.response.data.message,
            });
        }
    };

// remove from wishlist
export const removeCart = id => async dispatch => {
    try{
        dispatch({
            type: 'removeCartRequest',
        });
        const {data} = await axios.delete('removeCart/${id}');
        dispatch ({
            type: 'removeCartSuccess',
            payload: data,
        });
    } catch (error) {
        dispatch({
            type: 'removeCartFail',
            payload: error.response.data.message,
        });
    }
};

export const getCart =() => async dispatch => {
    try{
        dispatch({
            type: 'getCartRequest',
        });
        const {data} = await axios.get ('cart');
        dispatch ({
            type: 'getCartSuccess',
            payload: data,
        });
    } catch(error){
        dispatch({
            type: 'getCartFail',
            payload: error.response.data.message,
        });
    }
}

export const updateCart = (id, quantity) => async dispatch =>{
    try {
        dispatch({
            type: 'updateCartRequest',
        });
        const {data} = await axios.put('update/${id}',{
            quantity
        });
        dispatch({
            type: 'updateCartSuccess',
            payload: data,
        });

    } catch (error){
        dispatch ({
            type: 'updateCartFail',
            payload: error.response.data.message,
        });
    }
};