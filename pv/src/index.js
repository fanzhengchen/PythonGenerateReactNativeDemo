import React, {Component} from 'react';
import {
    AppRegistry,
    StyleSheet,
    Text,
    View,
} from 'react-native';

import Nfzcsku from 'fzc-sku';
import Nfzcprice from 'fzc-price';
export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {

        return (
            <View>
				<Nfzcsku/>
				<Nfzcprice/>
            </View>
        );
    }

}