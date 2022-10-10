import React from 'react'
import { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { useGetTextLines } from '../../../../hooks/useRQHooks'




const TextLines = () => {
  let { projName } = useParams();
  const { data, refetch, isLoading, isIdle } = useGetTextLines(projName, { enabled: false });

  useEffect(() => {
   console.log('TextLines data:',data)
  }, [data]);

  return (
    <>
    <div>TextLines</div>
    <button onClick={refetch} className="btn">
                Click Me TO get TextLines
              </button>
              <div>for {projName}</div>
              <div className='mt-8'>
                <p>{isLoading && 'LOADING ...'}</p>
                <p>{isIdle && 'isIdle ...'}</p>
                <pre>
                  {data?.map((line, idxl) => (
                    <p key={line.id}>
                    <span>
                      {line.page_id}
                    </span>
                      {line.text_line}
                    </p>
                  ))}
                </pre>
              </div>
    </>
  )
}

export default TextLines