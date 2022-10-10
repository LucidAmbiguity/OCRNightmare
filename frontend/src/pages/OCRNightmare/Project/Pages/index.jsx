import React from 'react'
import { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useGetPages } from '../../../../hooks/useRQHooks'
import PageList from '../../components/PageList';




const Pages = () => {
  let { projName } = useParams();
  const { data:page_list, refetch, isLoading, isIdle } = useGetPages(projName, { enabled: false });

  useEffect(() => {
   console.log('Pages data:',page_list)
  }, [page_list]);

  return (
    <>
      <p>{isLoading && 'LOADING ...'}</p>
        <p>{isIdle && 'isIdle ...'}</p>

        {/* !todo nnvoxvinhv */}
      <div>Pages</div>
      <button onClick={refetch} className="btn">
        Click Me TO get Pages
      </button>
      <div>for {projName}</div>
      {/* <div className='mt-8'>
        <p>{isLoading && 'LOADING ...'}</p>
        <p>{isIdle && 'isIdle ...'}</p>
        <pre>
          {data?.map((page, idxp) => (
            <p key={page.id}>
              <span>
                {page.id}
              </span>
              <span> </span>
               {page.project_id} {projName}
            </p>
          ))}
        </pre>
      </div> */}
      <div>AvailableProjects</div>
      <div className="mt-8 text-justify">
        <div className="w-9/12 mx-auto">
          <div className="px-6 py-6 odd:bg-white even:bg-slate-100">
            <div className="grid  grid-cols-3 gap-x-10">
              <p>name</p>
              <p>status</p>
              <p>pages</p>
            </div>
            <PageList page_list={page_list}/>
          </div>
        </div>
      </div>
    </>
  )
}

export default Pages