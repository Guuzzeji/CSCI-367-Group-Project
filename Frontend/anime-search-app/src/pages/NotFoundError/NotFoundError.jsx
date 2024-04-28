import * as React from 'react';

import { Text, Image } from '@chakra-ui/react';

import './NotFoundError.css';
import towmadImg from './twomad-fall.gif';

function NotFoundError() {

    return (
        <div className="Background">
            <div className="BackgroundOverlay">
                <div className="CenterScreen">
                    <Image
                        className="GifImage"
                        borderRadius="10"
                        objectFit='cover'
                        src={towmadImg}
                        alt="bruh falls sad moments lol"
                    />
                    <Text className="BigText">Sorry This Page Does Not Exist 😔</Text>
                </div>
            </div>
        </div>
    );
}

export default NotFoundError;