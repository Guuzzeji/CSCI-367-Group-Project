import * as React from 'react';

import { Text, ScaleFade } from '@chakra-ui/react';

import { useLoaderData } from 'react-router-dom';

import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';

function SearchResult() {
    const resData = useLoaderData();
    console.log(resData);

    //TODO: Impliment stuff with resData
    //TODO: Handle possible error of no resData or it is empty



    return (
        <div>
            Result page {String(resData[0].title)}
        </div>
    );
}

export default SearchResult;