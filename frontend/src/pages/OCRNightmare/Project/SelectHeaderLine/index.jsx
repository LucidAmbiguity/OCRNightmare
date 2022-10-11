import React from 'react'
import { useEffect,useState } from 'react';
import { Link, Outlet, useParams } from 'react-router-dom';
import { useGetPageWTL } from '../../../../hooks/useRQHooks'



const SelectHeaderLine = () => {

  const initialStateCI = [];
  initialStateCI.push(new Set());
  const [txtLineIndexes, setTxtLineIndexes] = useState(initialStateCI)

  const testSpan = (a, i, p) => {
    console.log('testSpan', a, i, p);
    const temp = [...txtLineIndexes];
    if (temp[0].has(p)) {
      temp[0].delete(p);
    } else {
      temp[0].add(p);
    }

    setTxtLineIndexes(temp);
    console.log('testSpanA', txtLineIndexes);
  };



  let { projName, page_id:pageId } = useParams();
  const { data:pageWTL, refetch, isLoading, isIdle, isFetching } = useGetPageWTL(projName, pageId,{ enabled: true });

  useEffect(() => {
   console.log('Page data w_tl:',pageWTL,':',projName, pageId)
  }, [pageWTL,pageId,projName]);

  const handleClick = (lid) =>{
    console.log('PageWiSelectLine:hC:',lid)

  }

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
            {pageWTL?.text_lines?.map((line,idx)=>{
              return (
                <div
                  className='cursor-pointer'
                  key={line?.id}
                  onClick={() => testSpan(line?.id ,line.page_id ,idx)}
              >
                {line.id}:
                {line.page_id}:
                {line.text_line}
              </div>
              )
            })}
          </div>
        </pre>
      </div>
      <Outlet/>
    </>
  )
}

export default SelectHeaderLine