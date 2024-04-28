import * as React from 'react';

import {
    Text,
    ScaleFade,
    Image
} from '@chakra-ui/react';

import './Home.css';
import icon_image from './gojo-home.gif';

import SearchBarInput from '../../components/searchbarinput/SearchBarInput';

function Home() {
    return (
        <div className='Background'>
            <div className='BackgroundOverlay'>
                <ScaleFade delay={0.25} initialScale={0.9} in={true}>
                    <div className='CenterSearch'>
                        <Image
                            borderRadius='full'
                            boxSize='150px'
                            src={icon_image}
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