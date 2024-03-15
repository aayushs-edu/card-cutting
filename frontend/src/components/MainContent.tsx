import React, { ReactNode } from 'react';

interface MainContentProps {
  children: ReactNode;
}

const MainContent: React.FC<MainContentProps> = ({ children }) => {
  return (
    <main className="flex-1 overflow-y-auto p-4">
      {children}
    </main>
  );
};

export default MainContent;
