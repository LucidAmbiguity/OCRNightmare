import {  NavLink } from 'react-router-dom';
import { useLocation } from 'react-router-dom';

const Navbar = () => {
  const location = useLocation();

  return (
    <div className="px-6  mx-auto flex justify-between min-w-full bg-slate-300 text-indigo-900">
      <p>LucidAmbiguity</p>
      <p>{location.pathname === '/' ? 'OCR Nightmare' : location.pathname.slice(1)}</p>
      <ul className="flex child:mr-6 child-hover:text-blue-500 child:px-5">
        <NavLink to="/" className={({ isActive }) => (isActive ? 'bg-slate-400' : '')}>
          <li>Home</li>
        </NavLink>
        <NavLink to="quiz" className={({ isActive }) => (isActive ? 'bg-slate-400' : '')}>
          <li>Quiz</li>
        </NavLink>
        <NavLink to="ocrNightmare" className={({ isActive }) => (isActive ? 'bg-slate-400' : '')}>
          <li>OCR</li>
        </NavLink>
      </ul>
    </div>
  );
};

export default Navbar;
