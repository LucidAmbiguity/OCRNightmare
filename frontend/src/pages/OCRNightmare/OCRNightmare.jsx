// Framework
import React, { useEffect, useState } from 'react';
import { Routes, Route, Link, Outlet, useLocation } from 'react-router-dom';
import Project from './Project';
import Projects from './Projects';



const OCRNightmare = () => {

  const [isRootPath, setIsRootPath] = useState(true)
  const { pathname } = useLocation();

  useEffect(() => {
    const path = pathname.slice(-13)
    if (path === '/ocrNightmare') {
      setIsRootPath(true);
    }else{
      setIsRootPath(false);
    }
    console.log('pathname', pathname.slice(-13), pathname);
  }, [pathname]);



  return (
  <div className="main bg-stone-200 min-h-max pb-10">
    <h1>OCRNIGHTMARE</h1>
    {isRootPath && (
    <ul>
      <li>
        <Link to="projects">
          <button className="btn btn-sidebar" type="button">
            Projects
          </button>
        </Link>
      </li>
    </ul>
    )}
    <Routes>
      <Route path="projects" element={<Projects />} />
      <Route path="projects/:projName" element={<Project />} />
      {/* <Route path="availableProjects"> */}
        {/* <Route path=":projName" element={<CurrentProject isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />}> */}
          {/* <Route path="customers" element={<CustomersView />}> */}
            {/* <Route path=":custNum" element={<CustomerView />} /> */}

            {/* <Route path="" element={<NoCustomerView />} /> */}
          {/* </Route> */}
          {/* <Route path="tags" element={<TagsFormView />}> */}
            {/* <Route path=":tagNum" element={<TagFormView />} /> */}
            {/* <Route path="" element={<NoTagView />} /> */}
          {/* </Route> */}
          {/* <Route path="custForms" element={<CustomersView />}> */}
            {/* <Route path=":custNum" element={<CustFormView />} /> */}
            {/* <Route path=":custNum/saved" element={<SavedForm />} /> */}
            {/* <Route path="" element={<NoCustomerView />} /> */}
          {/* </Route> */}
          {/* <Route path="edit" element={<CustomerEdit />} /> */}
        {/* </Route> */}
        {/* <Route index element={<AvailableProjects isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />} /> */}
      {/* </Route> */}
      {/* <Route path="lastProject" element={<LastProject />} /> */}
      {/* <Route path="loadProject" element={<LoadProject />} /> */}
      {/* <Route path="newProject" element={<NewProject />} /> */}
      {/* <Route path="" element={<NoProject />} /> */}
      {/* <Route
        path="*"
        element={(
          <main style={{ padding: '1rem' }}>
            <p>There&pos;s nothing here! OCR!!!</p>
          </main>
        )}
      /> */}
    </Routes>

    <div>
       <Outlet />
    </div>
    </div>
  )
}

export default OCRNightmare