import * as React from 'react';
import {
    Text
} from '@chakra-ui/react';

import main from './main.css';

import SearchBarInput from '../../components/searchbar/SearchBarInput';

function Home() {
    return (
        <div className='Background'>
            <div className='BackgroundOverlay'>
                <div className='CenterSearch'>
                    <Text fontSize="6xl" className='LogoText'>OtakuOracle</Text>
                    <br />
                    <SearchBarInput />
                </div>
            </div>
        </div>
    );
}

export default Home;