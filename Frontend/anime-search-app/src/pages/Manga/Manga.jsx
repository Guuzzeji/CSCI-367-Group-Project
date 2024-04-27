import * as React from 'react';

import { Text, ScaleFade } from '@chakra-ui/react';
import { useLoaderData } from 'react-router-dom';

import './Manga.css'
import { Divider } from '@chakra-ui/react'
import { Card, CardHeader, CardBody, CardFooter } from '@chakra-ui/react'

import NotFoundError from '../NotFoundError/NotFoundError';

function Manga() {
    try {
    const resData = useLoaderData();

    console.log(resData);

    const manga = resData[0];

    /*code to format authors name*/
    const formatAuthorName = (author) => {
        const splitName = author.split(", ");
        return `${splitName[1]} ${splitName[0]}`;
    };

    //TODO: Impliment json from resData
    //TODO: Handle error of new resData is found / is empty

    return (
        <div className='background'>
            
            <div className='container'>
        
            {/*Manga page {String(resData)}*/}
            
            <div className="manga-image">
                <h1 className="manga-title text">{manga.title}</h1>
                <img src={manga.image} alt={manga.title} style={{ maxWidth: '300px' }} /> 
            </div>
            <div className="speech-bubble">
                <p className='manga-details'><strong>Author: </strong>{formatAuthorName(manga.author)}</p> 
                <Divider orientation='horizontal' />
                <p className='manga-details'><strong>Genres: </strong>{manga.genres}</p>
                <Divider orientation='horizontal' />
                <p className='manga-details'><strong>Themes: </strong>{manga.themes}</p>
                <Divider orientation='horizontal' />

                <p className='manga-details'><strong>Published: </strong>{manga.published_start} - {manga.published_end}</p>
                <Divider orientation='horizontal' />
                
                <p className='manga-details'><strong>Synopsis: </strong>{manga.synopsis}</p> 
            </div>
            </div>
        </div>
    );
    } catch(error) {
        console.error('Error in Manga component:', error);
        return NotFoundError();
    }

    //TODO: Impliment json from resData
    //TODO: Handle error of new resData is found / is empty

    
}

export default Manga;