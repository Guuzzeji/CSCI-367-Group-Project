import * as React from 'react';

import { Text, ScaleFade } from '@chakra-ui/react';
import { useLoaderData } from 'react-router-dom';

function Manga() {
    const resData = useLoaderData();
    console.log(resData);

    //TODO: Impliment json from resData
    //TODO: Handle error of new resData is found / is empty

    return (
        <div>
            Manga page {String(resData)}
        </div>
    );
}

export default Manga;