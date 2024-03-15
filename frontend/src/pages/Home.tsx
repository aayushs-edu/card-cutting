import React from 'react';
import LoginButton from '../components/LoginButton';

const Home: React.FC = () => {
  return (
    <div className="flex justify-center items-center h-screen bg-blue-900 text-white">
      <div>
        <h1 className="text-4xl mb-8">Welcome to Card Cutting</h1>
        <div className="space-y-4">
          <LoginButton />
        </div>
      </div>
    </div>
  );
};

export default Home;