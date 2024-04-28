import * as React from 'react';

import {
    Text,
    ScaleFade,
    Image
} from '@chakra-ui/react';

import { useLoaderData } from 'react-router-dom';
import './SearchResult.css';
import SearchBarInput from '../../components/searchbarinput/SearchBarInput';
import Errorimage from './gojoError.jpg';

function SearchResult() {
    const resData = useLoaderData();
    console.log(resData);

    if(resData  == 0){
        return (
            <div>
            <div className='BackgroundPageTwo'>
                    <ScaleFade delay={0.25} initialScale={0.9} in={true}>
                        <div className='CenterSearch'>
                            <Text className='LogoText'>OtakuOracle</Text>
                            <br />
                            <SearchBarInput />
                        </div>
                    </ScaleFade>
                    <table className="Error-table">
                        <tr>
                            <th align="center"><img src={Errorimage} alt="Error image" height="34%" width="34%"></img></th>
                        </tr>
                        <tr className='message'>
                            <th>Error: Manga not found</th>
                        </tr>
                    </table>
                    
                </div>
            </div>
        )
    }

    //TODO: Impliment stuff with resData
    //TODO: Handle possible error of no resData or it is empty
    return (
        <div>
            <div className='BackgroundPageTwo'>
                    <ScaleFade delay={0.25} initialScale={0.9} in={true}>
                        <div className='CenterSearch'>
                            <Text className='LogoText'>OtakuOracle</Text>
                            <br />
                            <SearchBarInput />
                        </div>
                    </ScaleFade>
                    <table className="bordered-table">
                        {resData.map(function(item) {
                            console.log(item)
                                return (
                                    <tr>
                                    <th><img src={item.imgurl} alt={item.title +" cover"} width='100' height='100'></img></th>
                                    <th><a href={"http://localhost:3030/manga/" + item.bookid}>{item.title}</a></th>
                                    </tr>
                                )
                            })}
                    </table>
                </div>
            </div>
    );
}

export default SearchResult;