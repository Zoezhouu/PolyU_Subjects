// FavoritesScreen.js
import React from 'react';
import { View, FlatList, StyleSheet } from 'react-native';
import { Title, Card, Paragraph, Text, Button } from 'react-native-paper';
import { useGlobalContext } from '../globalProvider';

const FavoritesScreen = () => {
    const { globalState, dispatch } = useGlobalContext();

    const removeFromFavorites = (itemId) => {
        dispatch({
            type: 'REMOVE_FROM_FAVORITES', // Update with your actual action type
            payload: { id: itemId },
        });
    };

    const isFavoritesEmpty = globalState.favorites.length === 0;

    return (
        <View style={styles.container}>
            {isFavoritesEmpty ? (
                <View style={styles.emptyFavoritesContainer}>
                    <Text style={styles.emptyFavoritesText}>No items in favorites</Text>
                </View>
            ) : (
                <FlatList
                    data={globalState.favorites}
                    renderItem={({ item }) => (
                        <Card style={styles.productContainer}>
                            <Card.Cover source={{ uri: item.image_url }} style={styles.productImage} />
                            <Card.Content>
                                <Title style={styles.productName}>{item.name}</Title>
                                <Paragraph style={styles.productPrice}>Price: ${item.price}</Paragraph>
                                <Paragraph style={styles.productStock}>Stock: {item.stock}</Paragraph>
                            </Card.Content>
                            <Card.Actions>
                                <Button icon="delete-empty" onPress={() => removeFromFavorites(item.id)}>Remove from Favorites</Button>
                            </Card.Actions>
                        </Card>
                    )}
                    keyExtractor={(item) => item.id.toString()}
                />
            )}
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16,
    },
    productContainer: {
        marginBottom: 16,
    },
    productImage: {
        aspectRatio: 16 / 9,
        borderRadius: 8,
    },
    productName: {
        fontSize: 18,
        fontWeight: 'bold',
        marginBottom: 8,
    },
    productPrice: {
        fontSize: 16,
        color: '#555',
        marginBottom: 4,
    },
    productStock: {
        fontSize: 16,
        color: '#555',
    },
    emptyFavoritesContainer: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    emptyFavoritesText: {
        fontSize: 18,
        fontWeight: 'bold',
        color: '#555',
    },
});

export default FavoritesScreen;
