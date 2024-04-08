import { ChakraProvider } from '@chakra-ui/react';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from './pages/Home/Home';
// import SearchItem from './components/searchitem/SearchItem';


// TODO: Create search result page 
// TODO: Create page for specifc book
// also use this on backend, https://www.geeksforgeeks.org/how-to-implement-search-and-filtering-in-a-rest-api-with-node-js-and-express-js/

function App() {
  return (
    <ChakraProvider>
      <BrowserRouter>
        <Routes path="/">
          <Route index element={<Home />} />
        </Routes>
      </BrowserRouter>
    </ChakraProvider>
  );
}

export default App;
