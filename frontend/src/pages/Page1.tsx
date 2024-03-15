import React from 'react';
import Header from '../components/Header';
import MainContent from '../components/MainContent';

const Page1: React.FC = () => {
  return (
    <>
      <Header title="Page 1" description="Description of Page 1" />
      <MainContent>
        <h1 className="text-2xl font-semibold text-gray-800 mb-4">Page 1</h1>
        <div className="bg-white p-6 rounded shadow">
          <p className="text-gray-600">Main content area</p>
        </div>
      </MainContent>
    </>
  );
};

export default Page1;
