import * as React from 'react';

import { Text, ScaleFade } from '@chakra-ui/react';
import { useLoaderData } from 'react-router-dom';

function Manga() {
    const resData = useLoaderData();
    console.log(resData);

    return (
        <div>
            Manga page {String(resData)}
        </div>
    );
}

export default Manga;