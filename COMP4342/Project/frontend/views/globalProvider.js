import React, { createContext, useReducer, useContext } from 'react';

// Define action types
const ADD_TO_FAVORITES = 'ADD_TO_FAVORITES';
const ADD_TO_CART = 'ADD_TO_CART';

// Create context
const GlobalContext = createContext();

// Create a provider component
const GlobalProvider = ({ children }) => {
    const initialState = {
        favorites: [],
        cart: [],
    };

    const reducer = (state, action) => {
        switch (action.type) {
            case ADD_TO_FAVORITES:
                return {
                    ...state,
                    favorites: [...state.favorites, action.payload],
                };
            case ADD_TO_CART:
                return {
                    ...state,
                    cart: [...state.cart, action.payload],
                };
            case 'REMOVE_FROM_FAVORITES':
                return {
                    ...state,
                    favorites: state.favorites.filter(item => item.id !== action.payload.id),
                };
            case 'REMOVE_FROM_CART':
                return {
                    ...state,
                    cart: state.cart.filter(item => item.id !== action.payload.id),
                };
            default:
                return state;
        }
    };

    const [globalState, dispatch] = useReducer(reducer, initialState);

    return (
        <GlobalContext.Provider value={{ globalState, dispatch }}>
            {children}
        </GlobalContext.Provider>
    );
};

// Create a custom hook for using the context
const useGlobalContext = () => {
    const context = useContext(GlobalContext);
    if (!context) {
        throw new Error('useGlobalContext must be used within a GlobalProvider');
    }
    return context;
};

export { GlobalProvider, useGlobalContext, ADD_TO_FAVORITES, ADD_TO_CART };
