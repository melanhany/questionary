import { Grid, GridItem, Show } from '@chakra-ui/react'
import NavBar from './components/NavBar'
import GameGrid from './components/GameGrid'
import GenreList from './components/GenreList'
import UserForm from './components/UserForm'

function App() {
  const apiUrl = 'http://localhost:8080/users'; // Replace with your actual endpoint URL

  return <Grid templateAreas = {{
    base: `"nav" "main"`,
    lg: `"nav nav" "aside main"`
  }}>
    <GridItem area='nav'>
      <NavBar/>
    </GridItem>
    <Show above="lg">
    <GridItem area='aside' paddingX={5}>
      <GenreList/>
    </GridItem>
    </Show>
    <GridItem area='main'>
      <GameGrid/>
      <UserForm apiUrl={apiUrl}/>
    </GridItem>

  </Grid>
}

export default App
