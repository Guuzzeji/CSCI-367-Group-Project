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

import { useNavigate } from 'react-router-dom';

import './SearchBarInput.css';

function SearchBarInput() {
    // Note for update of search should dvide up theme/genure base on spacing
    const [selectSearchCategory, setSearchCategory] = React.useState('title');
    const [userSearchQuery, setUserSearchQuery] = React.useState('');

    const navigate = useNavigate();

    let handleInputText = (e) => {
        let text = e.target.value;
        setUserSearchQuery(text);
    };

    let handleInputEnter = (e) => {
        if (e.key === 'Enter' && userSearchQuery !== '' && userSearchQuery !== null) {
            e.preventDefault();
            navToSearchResultPage(userSearchQuery, selectSearchCategory);
            // console.log(userSearchQuery);
        }
    };

    let navToSearchResultPage = (query, type) => {
        let queryUrl = `query=${query}&type=${type}`;
        navigate("/result/?" + queryUrl);
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
                                        <Radio value='Author'>Author</Radio>
                                        <Radio value='Genre'>Genre</Radio>
                                        <Radio value='Theme'>Theme</Radio>
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