import * as React from 'react';

import { Text, ScaleFade } from '@chakra-ui/react';

import { useLoaderData } from 'react-router-dom';

function SearchResult() {
    const resData = useLoaderData();
    console.log(resData);

    return (
        <div>
            Result page {String(resData)}
        </div>
    );
}

export default SearchResult;