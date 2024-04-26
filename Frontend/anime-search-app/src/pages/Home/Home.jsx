import * as React from 'react';

import {
    Text,
    ScaleFade,
    Image
} from '@chakra-ui/react';

import './Home.css';
import icon_image from './gojo-home.gif';
import icon_image2 from './robinFace.png';
import icon_image3 from './funny-face.png';


import SearchBarInput from '../../components/searchbarinput/SearchBarInput';

function getRandomImage() {
    const images = [icon_image, icon_image2, icon_image3]; // Add more images here
    const index = Math.floor(Math.random() * images.length);
    return images[index];
}

function Home() {

    const randomImage = getRandomImage();

    return (
        <div className='Background'>
            <div className='BackgroundOverlay'>
                <ScaleFade delay={0.25} initialScale={0.9} in={true}>
                    <div className='CenterSearch'>
                        <Image
                            borderRadius='full'
                            boxSize='150px'
                            src={randomImage}
                            alt='some anime dude'
                        />
                        <Text className='LogoText'>OtakuOracle</Text>
                        <br />
                        <SearchBarInput />
                    </div>
                </ScaleFade>
            </div>
        </div>
    );
}

export default Home;