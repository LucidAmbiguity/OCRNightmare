import React from 'react'
import { useEffect } from 'react';
import { Outlet, useParams } from 'react-router-dom';
import { useGetPage } from '../../../../hooks/useRQHooks'




const Page = () => {
  let { projName, page_id:pageId } = useParams();
  const { data:page, refetch, isLoading, isIdle } = useGetPage(projName, pageId,{ enabled: false });

  useEffect(() => {
   console.log('Page data:',page,':',projName, pageId)
  }, [page,pageId,projName]);

  return (
    <>
      <div>Page</div>
      <button onClick={refetch} className="btn">
        Click Me TO get Page
      </button>
      <div>for {projName}</div>
      <div className='mt-8'>
        <p>{isLoading && 'LOADING ...'}</p>
        <p>{isIdle && 'isIdle ...'}</p>
        <pre>
          {
            <p key={page?.id}>
              <span>
                {page?.id}
              </span>
              <span> </span>
               {page?.project_id} {projName}
            </p>
          }
        </pre>
      </div>
      <div className="mt-8 text-justify">
        <div className="w-9/12 mx-auto">
          <div className="px-6 py-6 odd:bg-white even:bg-slate-100">
            <Outlet />
          </div>
        </div>
      </div>
    </>
  )
}

export default Page