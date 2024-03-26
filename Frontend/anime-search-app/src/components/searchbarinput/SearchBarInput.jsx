import * as React from 'react';

import {
    Input,
    Box,
    InputGroup,
    InputLeftElement,
    Button,
    Menu,
    MenuButton,
    MenuList,
    RadioGroup,
    Radio,
    Stack,
    Center,
    MenuGroup
} from '@chakra-ui/react';
import { SearchIcon, SmallAddIcon } from '@chakra-ui/icons';

import './SearchBarInput.css';

function SearchBarInput() {
    const [value, setValue] = React.useState('1');

    return (
        <Box bg="white" borderWidth='1px' borderRadius='lg' p={2} className='SearchBox'>
            <Stack spacing={4} direction='row'>
                <InputGroup>
                    <InputLeftElement pointerEvents='none'>
                        <SearchIcon color='gray.300' />
                    </InputLeftElement>
                    <Input isDisabled={false} variant='unstyled' placeholder='Search...' />
                </InputGroup>
                <Center>
                    <Menu>
                        <MenuButton isLoading={false} colorScheme='teal' variant="outline" alignContent="center" as={Button}>
                            {/** Switch this to a spinner when loading results and disable btn */}
                            <SmallAddIcon />
                        </MenuButton>
                        <MenuList>
                            <MenuGroup title='Search By'>
                                <RadioGroup colorScheme='teal' onChange={setValue} value={value}>
                                    <Stack direction='column' p={2}>
                                        <Radio value='1'>Title</Radio>
                                        <Radio value='2'>Author</Radio>
                                        <Radio value='3'>Genre</Radio>
                                        <Radio value='4'>Theme</Radio>
                                    </Stack>
                                </RadioGroup>
                            </MenuGroup>
                        </MenuList>
                    </Menu>
                </Center>
                {/** TODO: Show test if this btn is need or not */}
                {/* <Button variant="solid" colorScheme='teal'>
                    <ArrowForwardIcon />
                </Button> */}
            </Stack>
        </Box>
    );
}

export default SearchBarInput;