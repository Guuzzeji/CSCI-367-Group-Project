import * as React from 'react';

import {
    Text,
    ScaleFade
} from '@chakra-ui/react';

import './Home.css';

import SearchBarInput from '../../components/searchbarinput/SearchBarInput';

function Home() {
    return (
        <div className='Background'>
            <div className='BackgroundOverlay'>
                <ScaleFade delay={0.25} initialScale={0.9} in={true}>
                    <div className='CenterSearch'>
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