import React from "react";
import { 
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import {
  useAuth0,
} from '@auth0/auth0-react';
import './index.css'

import Sidebar from './components/Sidebar';
import Home from './pages/Home';
import Page1 from './pages/Page1';
import Page2 from './pages/Page2';
import Page3 from './pages/Page3';

const App: React.FC = () => {
  const { isAuthenticated } = useAuth0();

  return (
    <Router>
      {isAuthenticated ? (
        <div className="flex h-screen bg-gray-50">
          <Sidebar />
          <div className="flex-1 flex flex-col">
            <Routes>
              <Route path="/page1" element={<Page1/>} />
              <Route path="/page2" element={<Page2/>} />
              <Route path="/page3" element={<Page3/>} />
            </Routes>
          </div>
        </div>
      ) : (
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="*" element={<Navigate to="/"/>} />
        </Routes>
      )}
    </Router>
  );
}

export default App
