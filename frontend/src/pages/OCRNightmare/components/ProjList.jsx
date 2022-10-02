import { Link } from 'react-router-dom'

const ProjList = ({proj_list}) => {
  return (
    <>
     {proj_list && proj_list.map((proj, idx) => (
       <div className="grid  grid-cols-3 gap-x-10" key={`${idx}name`}>
                <Link to={`${proj.name}`}>
                  <p>{proj.name}</p>
                </Link>
                <p>{proj.status}</p>
                <p>{proj.status === 0 ? 'N\\A' : proj.pages}</p>
              </div>
            )

            )}
    </>
  )
}

export default ProjList