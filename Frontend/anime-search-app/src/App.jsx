import { ChakraProvider } from '@chakra-ui/react';
import { RouterProvider, createBrowserRouter, createRoutesFromElements, Route } from "react-router-dom";

import Home from './pages/Home/Home';
import SearchResult from './pages/SearchResult/SearchResult';
import Manga from './pages/Manga/Manga';
import NotFoundError from './pages/NotFoundError/NotFoundError';

// TODO: Create search result page 
// TODO: Create page for specifc book
// also use this on backend, https://www.geeksforgeeks.org/how-to-implement-search-and-filtering-in-a-rest-api-with-node-js-and-express-js/


const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/">
      {/** Home Page */}
      <Route index element={<Home />} />

      {/** Search Result Page */}
      <Route path='result/*'
        loader={({ request }) => {
          let url = new URL(request.url);
          console.log(url);
          return fetch(`http://localhost:3030/API/search${url.search}`);
        }}
        element={<SearchResult />} />

      {/** Manga detail Info Page */}
      <Route
        path='manga/:bookid'
        loader={({ params }) => {
          return fetch(`http://localhost:3030/API/manga/${params.bookid}`);
        }}
        element={<Manga />} />

      {/** Page Does Not Exist Page */}
      <Route path='*' element={<NotFoundError />} />
    </Route>
  )
);


function App() {
  return (
    <ChakraProvider>
      <RouterProvider router={router} />
    </ChakraProvider>
  );
}

export default App;
