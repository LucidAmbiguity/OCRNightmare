import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools';

// Components
import Navbar from './components/Navbar';

// Pages
import Home from './pages/Home/Home';
import OCRNightmare from './pages/OCRNightmare/OCRNightmare';
import E404 from './components/Errors/E404';

const queryClient = new QueryClient();

const App = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Navbar />
        {/* <Sidebar /> */}
        <div>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="ocrNightmare/*" element={<OCRNightmare />} />
            <Route path="*" element={<E404 />} />
          </Routes>
        </div>
      </BrowserRouter>
      <ReactQueryDevtools initialIsOpen={true} />
    </QueryClientProvider>
  );
};

export default App;
