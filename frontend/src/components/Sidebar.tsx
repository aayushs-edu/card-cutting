import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar: React.FC = () => {
  return (
    <aside className="w-60 h-full bg-gray-200 border-r">
      <div className="px-5 py-4">
        <Link to="/" className="text-xl font-semibold text-gray-700 flex items-center space-x-2">
          <img src="/favicon.png" alt="Logo" className="h-8 w-8=" />
          <h1 className="text-xl font-semibold text-gray-700">Card Cutting</h1>
        </Link>
      </div>
      <nav className="flex flex-col p-4">
        <Link to="/page1" className="py-2 px-4 text-gray-700 hover:bg-gray-300 rounded transition duration-300">Page 1</Link>
        <Link to="/page2" className="py-2 px-4 text-gray-700 hover:bg-gray-300 rounded transition duration-300">Page 2</Link>
        <Link to="/page3" className="py-2 px-4 text-gray-700 hover:bg-gray-300 rounded transition duration-300">Page 3</Link>
      </nav>
    </aside>
  );
};

export default Sidebar;