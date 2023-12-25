import React from 'react'
import { List, ListItem, Image, HStack, Text } from '@chakra-ui/react'
import useGenres from "../hooks/useGenres"

const GenreList = () => {
    const { genres } = useGenres()
  return (
    <List>
        {genres.map(genre => 
            <ListItem key={genre.id} paddingY='5px'>
                <HStack> 
                    <Image boxSize='32px' borderRadius={8} src={genre.image_background} />
                    <Text fontSize='lg'>{genre.name}</Text>
                </HStack>
            </ListItem>)}
    </List>
  )
}

export default GenreList