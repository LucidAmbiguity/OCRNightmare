import React from 'react'
import { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useGetPageWTL } from '../../../../hooks/useRQHooks'




const PageWTL = () => {

  let { projName, page_id:pageId } = useParams();
  const { data:pageWTL, refetch, isLoading, isIdle } = useGetPageWTL(projName, pageId,{ enabled: false });

  useEffect(() => {
   console.log('Page data:',pageWTL,':',projName, pageId)
  }, [pageWTL,pageId,projName]);

   return (
    <>
      <div>PageWTL</div>
      <button onClick={refetch} className="btn">
        Click Me TO get PageWTL
      </button>
      <div>for {projName}</div>
      <div className='mt-8'>
        <p>{isLoading && 'LOADING ...'}</p>
        <p>{isIdle && 'isIdle ...'}</p>
        <pre>
          {
            <p key={pageWTL?.id}>
              <span>
                {pageWTL?.id}
              </span>
              <span> </span>
               {pageWTL?.project_id} {projName}
            </p>
          }
          <div>
            {pageWTL?.text_lines.map((line)=>{
              return (<p key={line?.id}>
                {line.id}
                {line.page_id}
                {line.text_line}
              </p>
              )
            })}
          </div>
        </pre>
      </div>
    </>
  )
}

export default PageWTL