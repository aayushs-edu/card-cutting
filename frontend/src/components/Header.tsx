import React from 'react';

interface HeaderProps {
  title: string;
  description?: string;
}

const Header: React.FC<HeaderProps> = ({ title, description }) => {
  return (
    <header className="w-full bg-white shadow flex flex-col justify-between px-6 py-4">
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-xl font-semibold text-gray-800">{title}</h2>
          <p className="text-sm text-gray-600">{description}</p>
        </div>
      </div>
    </header>
  );
};

export default Header;
