import * as React from 'react';

import {
    HStack,
    Box,
    Image,
    Text,
} from '@chakra-ui/react';

// TODO: Make this a btn that opens a model overlay that show more infomation regarding the manga
function SearchItem({ title, author, published, id }) {

    return (
        <Box bg="white" borderWidth='1px' borderRadius='lg' p={2} style={{ width: '400px', height: "auto" }}>
            <HStack alignItems="center" spacing={4}>
                <div style={{ width: '150px' }}>
                    <Image borderRadius='lg' src='https://cdn.myanimelist.net/images/manga/3/258224l.jpg' alt='Monster' />
                </div>

                <div>
                    <Text style={{ fontSize: '25px', fontWeight: 'bold' }}>Monster</Text>
                    <Text style={{ fontSize: '18px' }}>Urasawa, Naoki</Text>
                    <Text style={{ fontSize: '15px', fontWeight: 'lighter' }}>Dec 5, 1994 to Dec 20, 2001</Text>
                </div>
            </HStack>
        </Box>
    );
}

export default SearchItem;