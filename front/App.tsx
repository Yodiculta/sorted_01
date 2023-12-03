// import { Button } from '@ya.praktikum/react-developer-burger-ui-components';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, SafeAreaView, Pressable, Alert, TextInput} from 'react-native';
import DataInputForm from './app/DataInputForm';

import { rootStore, StoreProvider } from "./app/store/index";

export default function App() {
  const handleButtonPress = () => Alert.alert("Hello", 'message', [
    {text : "Yes", onPress: () => console.log('test')},
    {text: "no"}
  ])

  const handleButtonPressPrompt = () => Alert.prompt('test', 'test', text => console.log(text))
  return (
    <StoreProvider value={rootStore}>
    <SafeAreaView style={styles.container}>
      <DataInputForm/>
    </SafeAreaView>
    </StoreProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    // alignItems: 'center',
    // justifyContent: 'center',
  },
});
