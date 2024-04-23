import { ChakraProvider } from '@chakra-ui/react';
import { RouterProvider, createBrowserRouter, createRoutesFromElements, Route } from "react-router-dom";

import Home from './pages/Home/Home';
import Result from './pages/Result/Result';
import Manga from './pages/Manga/Manga';
import NotFoundError from './pages/NotFoundError/NotFoundError';

// TODO: Create search result page 
// TODO: Create page for specifc book
// also use this on backend, https://www.geeksforgeeks.org/how-to-implement-search-and-filtering-in-a-rest-api-with-node-js-and-express-js/


const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/">
      <Route index element={<Home />} />
      <Route path='result/*'
        loader={({ request }) => {
          let url = new URL(request.url);
          console.log(url);
          return fetch(`http://localhost:3030/API/search${url.search}`);
        }}
        element={<Result />} />
      <Route
        path='manga/:bookid'
        loader={({ params }) => {
          return fetch(`http://localhost:3030/API/manga/${params.bookid}`);
        }}
        element={<Manga />} />
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
