// import { useEffect } from "react"

const ProjData = ({proj_data}) => {

  // useEffect(() => {
  //   console.log('ProjData',proj_data)
  // }, [proj_data])

  return (
    <>
      {proj_data ?
      (<div className="grid  grid-cols-3 gap-x-10" >
        <p>{proj_data.name}</p>
        <p>{proj_data.status}</p>
        <p>{proj_data.status === 0 ? 'N\\A' : proj_data.pages}</p>
      </div>)
      :null}

    </>
  )
}

export default ProjData