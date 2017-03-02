import React, {Component} from 'react';
import {
    AppRegistry,
    StyleSheet,
    Text,
    View
} from 'react-native';
import App from './src';

export default class wx_sample extends Component {
    render() {
        return (
            <App/>
        );
    }
}

AppRegistry.registerComponent('wx_sample', () => wx_sample);