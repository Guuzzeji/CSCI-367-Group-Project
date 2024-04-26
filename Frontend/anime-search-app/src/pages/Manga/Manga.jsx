import * as React from 'react';

import { Text, ScaleFade } from '@chakra-ui/react';
import { useLoaderData } from 'react-router-dom';

import './Manga.css'

function Manga() {
    const resData = useLoaderData();

    if (!resData) {
        return <div>Error: Manga not found</div>;
    }
    console.log(resData);

    const manga = resData[0];

    //TODO: Impliment json from resData
    //TODO: Handle error of new resData is found / is empty

    return (
        <div>
            {/*Manga page {String(resData)}*/}
            <h1 className="manga-title">{manga.title}</h1>
            <img className="manga-image" src={manga.image} alt={manga.title} style={{ maxWidth: '300px' }} /> 
            <p>Author: {manga.author}</p>
            <p>Genres: {manga.genres}</p>
            <p>Published: {manga.published_start} - {manga.published_end}</p>
            <p>Themes: {manga.themes}</p>
            <p>Synopsis: {manga.synopsis}</p>
        </div>
    );

    //TODO: Impliment json from resData
    //TODO: Handle error of new resData is found / is empty

    return (
        <div>
            {/*Manga page {String(resData)}*/}

        </div>
    );
}

export default Manga;