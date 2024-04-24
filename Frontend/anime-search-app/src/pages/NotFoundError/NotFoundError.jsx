import * as React from 'react';

import { Text, Image } from '@chakra-ui/react';

import './NotFoundError.css';

function NotFoundError() {

    return (
        <div className="Background">
            <div className="BackgroundOverlay">
                <div className="CenterScreen">
                    <Image
                        className="GifImage"
                        borderRadius="10"
                        objectFit='cover'
                        src='https://media.tenor.com/eH93eoeVWokAAAAC/twomad-fall.gif'
                        alt='Dan Abramov'
                    />
                    <Text className="BigText">Sorry This Page Does Not Exist 😔</Text>
                </div>
            </div>
        </div>
    );
}

export default NotFoundError;