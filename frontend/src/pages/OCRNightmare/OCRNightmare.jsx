// Framework
import React, { useEffect, useState } from 'react';
import { Routes, Route, Link, Outlet, useLocation } from 'react-router-dom';
import Project from './Project';
import Extract from './Project/Extract';
import Page from './Project/Page';
import Pages from './Project/Pages';
import PageWTL from './Project/PageWTL';

import TextLines from './Project/TextLines';
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
      <Route path="projects/:projName" element={<Project />} >
        <Route path="extract" element={<Extract />} />
        <Route path="text_lines" element={<TextLines />} />
        <Route path="pages" element={<Pages />} />
        <Route path="pages/:page_id" element={<PageWTL />} >
          <Route path="w_tl" element={<PageWTL />} />

        </Route>
      </Route>

</Routes>

    <div>
       <Outlet />
    </div>
    </div>
  )
}

export default OCRNightmare



      // {/* <Route path="availableProjects"> */}
      //   {/* <Route path=":projName" element={<CurrentProject isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />}> */}
      //     {/* <Route path="customers" element={<CustomersView />}> */}
      //       {/* <Route path=":custNum" element={<CustomerView />} /> */}

      //       {/* <Route path="" element={<NoCustomerView />} /> */}
      //     {/* </Route> */}
      //     {/* <Route path="tags" element={<TagsFormView />}> */}
      //       {/* <Route path=":tagNum" element={<TagFormView />} /> */}
      //       {/* <Route path="" element={<NoTagView />} /> */}
      //     {/* </Route> */}
      //     {/* <Route path="custForms" element={<CustomersView />}> */}
      //       {/* <Route path=":custNum" element={<CustFormView />} /> */}
      //       {/* <Route path=":custNum/saved" element={<SavedForm />} /> */}
      //       {/* <Route path="" element={<NoCustomerView />} /> */}
      //     {/* </Route> */}
      //     {/* <Route path="edit" element={<CustomerEdit />} /> */}
      //   {/* </Route> */}
      //   {/* <Route index element={<AvailableProjects isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />} /> */}
      // {/* </Route> */}
      // {/* <Route path="lastProject" element={<LastProject />} /> */}
      // {/* <Route path="loadProject" element={<LoadProject />} /> */}
      // {/* <Route path="newProject" element={<NewProject />} /> */}
      // {/* <Route path="" element={<NoProject />} /> */}
      // {/* <Route
      //   path="*"
      //   element={(
      //     <main style={{ padding: '1rem' }}>
      //       <p>There&pos;s nothing here! OCR!!!</p>
      //     </main>
      //   )}
      // /> */}
