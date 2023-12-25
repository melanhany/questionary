// UserForm.tsx

import React, { useState } from 'react';
import {
    Box,
    Button,
    FormControl,
    FormLabel,
    Input,
  } from '@chakra-ui/react';
  

interface UserFormProps {
  apiUrl: string; // The FastAPI endpoint URL
}

const UserForm: React.FC<UserFormProps> = ({ apiUrl }) => {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        // Handle success
        console.log('User data submitted successfully!');
      } else {
        // Handle error
        console.error('Error submitting user data');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <Box maxW="sm" borderWidth="1px" borderRadius="lg" p="6">
      <form onSubmit={handleSubmit}>
        <FormControl>
          <FormLabel>First Name</FormLabel>
          <Input
            type="text"
            name="first_name"
            value={formData.first_name}
            onChange={handleChange}
          />
        </FormControl>
        <FormControl mt={4}>
          <FormLabel>Last Name</FormLabel>
          <Input
            type="text"
            name="last_name"
            value={formData.last_name}
            onChange={handleChange}
          />
        </FormControl>
        <FormControl mt={4}>
          <FormLabel>Email</FormLabel>
          <Input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
        </FormControl>
        <Button mt={4} colorScheme="teal" type="submit">
          Submit
        </Button>
      </form>
    </Box>
  );
};

export default UserForm;
