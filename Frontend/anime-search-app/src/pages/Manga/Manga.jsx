import * as React from 'react';

import { Text, ScaleFade } from '@chakra-ui/react';
import { useLoaderData } from 'react-router-dom';

function Manga() {
    const state = useLoaderData();

    console.log(state);

    return (
        <div>
            Manga page {state.data}
        </div>
    );
}

export default Manga;