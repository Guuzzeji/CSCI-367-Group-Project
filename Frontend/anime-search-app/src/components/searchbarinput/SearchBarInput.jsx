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
    // Note for update of search should dvide up theme/genure base on spacing
    const [selectSearchCategory, setSearchCategory] = React.useState('title');
    const [userSearchQuery, setUserSearchQuery] = React.useState('');
    const [isSending, setSending] = React.useState(false);

    let handleInputText = (e) => {
        let text = e.target.value;
        setUserSearchQuery(text);
    };

    let handleInputEnter = (e) => {
        if (e.key === 'Enter') {
            // TODO: Connect to backend and use isSending to handle disabling of user input to backend to block spamming
            console.log("User has inputed a value for to search", userSearchQuery);
        }
    };

    return (
        <Box bg="white" borderWidth='1px' borderRadius='lg' p={2} className='SearchBox'>
            <Stack spacing={4} direction='row'>
                <InputGroup>
                    <InputLeftElement pointerEvents='none'>
                        <SearchIcon color='gray.300' />
                    </InputLeftElement>
                    <Input
                        onChange={handleInputText}
                        onKeyDown={handleInputEnter}
                        isDisabled={false}
                        variant='unstyled'
                        placeholder='Search...' />
                </InputGroup>
                <Center>
                    <Menu>
                        <MenuButton isLoading={false} colorScheme='teal' variant="outline" alignContent="center" as={Button}>
                            {/** Switch this to a spinner when loading results and disable btn */}
                            <SmallAddIcon />
                        </MenuButton>
                        <MenuList>
                            <MenuGroup title='Search By'>
                                <RadioGroup colorScheme='teal' onChange={setSearchCategory} value={selectSearchCategory}>
                                    <Stack direction='column' p={2}>
                                        <Radio value='title'>Title</Radio>
                                        <Radio value='author'>Author</Radio>
                                        <Radio value='genre'>Genre</Radio>
                                        <Radio value='theme'>Theme</Radio>
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