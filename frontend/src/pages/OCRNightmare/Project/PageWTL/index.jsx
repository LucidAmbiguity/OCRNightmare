import React from 'react'
import { useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { useGetPageWTL } from '../../../../hooks/useRQHooks'




const PageWTL = () => {

  let { projName, page_id:pageId } = useParams();
  const { data:pageWTL, refetch, isLoading, isIdle, isFetching } = useGetPageWTL(projName, pageId,{ enabled: true });

  useEffect(() => {
   console.log('Page data w_tl:',pageWTL,':',projName, pageId)
  }, [pageWTL,pageId,projName]);


  return (
    <>

      <div className='mt-8'>
        <p>{isFetching && 'FETCHING ...'}</p>
        <p>{isLoading && 'LOADING ...'}</p>
        <p>{isIdle && 'isIdle ...'}</p>
        <p className='flex'>{pageWTL ? (
          <>
            <Link
              className='grow '
              to={`../pages/${parseInt(pageId)-1}`}>
                Previous
            </Link>:
            <Link
              className='grow text-right'
              to={`../pages/${parseInt(pageId)+1}`}>
                Next
            </Link>
          </>
          ):
          ('Almost') }
        </p>

        <pre>

          <div>
            {pageWTL?.text_lines?.map((line)=>{
              return (<p key={line?.id}>
                {line.id}:
                {line.page_id}:
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